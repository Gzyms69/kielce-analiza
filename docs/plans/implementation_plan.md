# Krytyczny Raport Audytu: National Transit Equity & Urban Gravity Platform

## Kontekst audytu

Przeprowadzono pełną analizę kodu źródłowego: 17 skryptów pipeline'u (`00`-`15` + `07_omnibus`), orkiestratora (`orchestrator.py`), 2 plików konfiguracyjnych, 5 dokumentów `.md` oraz istniejącego rejestru problemów `problems.txt`. Poniższy raport jest **bezlitośnie krytyczny** — identyfikuje zarówno problemy znane (z `problems.txt`), jak i całkowicie pominięte.

---

## CZĘŚĆ I: KRYTYCZNA OCENA SKRYPTÓW PIPELINE'U (Linia po linii)

---

### `00_init_environment.py` — KOPIOWANIE SAMEGO SIEBIE

| Waga | Problem |
|------|---------|
| 🔴 KRYTYCZNY | Linia 26-27: Skrypt kopiuje `data/poland/admin/powiaty.json` do... `data/poland/admin/powiaty.json`. Jeśli `PIPELINE_DATA_DIR=data` (domyślna wartość), to `source_powiaty == target_powiaty`. Cała logika `shutil.copy2` jest martwa — kopiujesz plik na samego siebie. Skrypt istnieje **bez sensu** w tym trybie. |
| ⚠️ WAŻNY | Brak walidacji integralności pliku `powiaty.json`. Sprawdzasz tylko `st_size > 100000`, co nie jest weryfikacją poprawności GeoJSON — plik mógłby być uszkodzony binarnie i nadal przejść ten check. |
| 💡 UWAGA | `raise SystemExit(1)` zamiast `sys.exit(1)` — działa, ale to jest anty-wzorzec. `SystemExit` to wyjątek bazowy, `sys.exit()` to poprawna ścieżka wyjścia. |

---

### `01_fetch_gtfs.py` — HARDCODED MONOLITH

| Waga | Problem |
|------|---------|
| 🔴 KRYTYCZNY | **218 linii hardcodowanego słownika URL-i bezpośrednio w kodzie źródłowym** (linia 13-147). To powinien być plik konfiguracyjny (JSON/YAML). Każda zmiana URL wymaga edycji kodu Pythona — naruszenie zasady separacji konfiguracji od logiki. |
| 🔴 KRYTYCZNY | Linia 175: `verify=False` — wyłączenie weryfikacji SSL dla **wszystkich** zapytań HTTP. `urllib3.disable_warnings` na linii 11 maskuje ostrzeżenia. To jest akceptowalne dla rządowych API, ale nie powinno być globalne. |
| ⚠️ WAŻNY | Linia 177: `r.content` ładuje **cały plik ZIP do RAM** przed rozpakowaniem. Dla dużych paczek GTFS (np. Warszawa z 17 źródłami) to może być kilkaset MB w pamięci jednocześnie. Powinno być `stream=True` + zapis na dysk + rozpakowanie. Uwaga: `stream=True` już jest na linii 175, ale `r.content` i tak ładuje **cały response do RAM** — `stream=True` jest martwy w tej konfiguracji. |
| ⚠️ WAŻNY | Brak weryfikacji zawartości ZIP. Po rozpakowaniu nie sprawdzasz, czy `stops.txt` faktycznie istnieje i jest poprawnym CSV. Uszkodzony lub niekompletny ZIP przejdzie niezauważony. |
| 💡 UWAGA | Linia 170: Idempotencja oparta tylko na istnieniu `stops.txt`. Jeśli ZIP został niepełnie rozpakowany w poprzednim uruchomieniu (OOM, przerwanie), `stops.txt` może istnieć ale być niekompletny. |

---

### `02_collect_stops.py` — FAŁSZYWY MAD

| Waga | Problem |
|------|---------|
| 🔴 KRYTYCZNY | Linia 147-149: **Fatalna implementacja MAD (Median Absolute Deviation)**. Obliczasz `mad = final_city_stops['final_dist'].median()`, ale MAD to `median(|X - median(X)|)`, a nie `median(X)`. To co obliczasz to **mediana odległości**, nie MAD. Mnożysz medianę przez 6 i nazywasz to "6 sigma" — to nie ma nic wspólnego z sigma statystycznym. Dla miasta z medianą odległości 5km, cutoff to 30km, co jest absurdalnie liberalne jako "filtr outlierów". |
| ⚠️ WAŻNY | Linia 107: Ręczna implementacja odległości euklidesowej zamiast `gdf.geometry.distance(center_point)`. Działa, ale jest nieczytelna i podatna na błędy. |
| ⚠️ WAŻNY | Linia 122: `union_all()` — ta metoda została dodana w GeoPandas 1.0+ i zastępuje `unary_union`. Kompatybilność wsteczna: zero. |
| ⚠️ WAŻNY | Linia 164: `buffer(1500, resolution=1)` — `resolution=1` oznacza kwadratowe bufory zamiast okrągłych. To jest celowe (Box Trick z devlogu), ale drastycznie zmienia geometrię stref transportowych — prostokąty zamiast kół wokół przystanków. Efekt: strefy transportowe nachodzą na siebie w sposób nienaturalny. |
| 💡 UWAGA | Linia 170-171: Zapis `stops.gpkg` i `transport_zone.gpkg` w **dwóch różnych CRS** — `transport_zone` w EPSG:4326, a `stops` w EPSG:4326 (po `to_crs`). Ale cała logika wewnętrzna działa w EPSG:2180. To powoduje konieczność reprojekcji przy każdym kolejnym odczycie. |

---

### `03_download_osm_pbf.py` — BRAK WERYFIKACJI INTEGRALNOŚCI

| Waga | Problem |
|------|---------|
| ⚠️ WAŻNY | Brak weryfikacji sumy kontrolnej (checksum). Geofabrik udostępnia pliki `.md5` — powinny być pobierane i porównywane. Przerwane pobieranie 2GB pliku PBF skutkuje uszkodzonym plikiem, który przejdzie check `st_size > 1_000_000_000`. |
| 💡 UWAGA | Brak progress baru w konsoli — 2GB pobieranie bez informacji zwrotnej (linia 33 ma rudymentarny pasek, ale jest prymitywny). |
| 💡 UWAGA | Brak obsługi wznowienia (Range header) — przerwane pobieranie zaczyna od zera. |

---

### `04_download_population.py` — OOM BOMB W DYSKRECJI

| Waga | Problem |
|------|---------|
| 🔴 KRYTYCZNY | Linia 36: `io.BytesIO(r.content)` — ładuje **cały ZIP siatki populacji GUS do RAM** (1-2 GB). To jest identyczny bug jak w `01_fetch_gtfs.py`. Przy ograniczonej pamięci systemowej to jest OOM natychmiast. |
| ⚠️ WAŻNY | Linia 41: `gpkg_names[0]` — bierze **pierwszy** plik GPKG z archiwum. Komentarz na linii 40 mówi "Wybieramy największy plik lub pierwszy pasujący", ale kod bierze po prostu pierwszy. Jeśli GUS zmieni strukturę ZIP, skrypt może wyciągnąć niewłaściwy plik. |
| ⚠️ WAŻNY | Linia 32: `verify=False` — ponowne wyłączenie SSL. |

---

### `05_extract_infrastructure.py` — CONCURRENCY BUG

| Waga | Problem |
|------|---------|
| 🔴 KRYTYCZNY | Linia 52: `os.environ["OSM_CONFIG_FILE"] = str(osmconf)` — **ustawienie zmiennej środowiskowej wewnątrz wątku Threadpool** (linia 96-98). Zmienne środowiskowe są **globalne dla procesu**. W kontekście `ThreadPoolExecutor`, wszystkie wątki współdzielą tę samą zmienną. To **działacotyko przypadkiem**, bo wszystkie wątki ustawiają tę samą wartość. Gdyby różne miasta miały różne konfig, byłby wyścig (race condition). |
| ⚠️ WAŻNY | Linia 65-66: Audit danych po konwersji ładuje **oba layery** (`points` + `multipolygons`) do pamięci tylko po to, żeby policzyć `len()`. To jest marnotrawstwo RAM — wystarczy `fiona.open()` z `len()` lub `ogrinfo`. |
| 💡 UWAGA | Linia 51: `Path("config/osmconf.ini")` — ścieżka względna. Jeśli skrypt jest uruchomiony z innego katalogu niż root projektu, nie znajdzie pliku. Brak walidacji istnienia. |

---

### `06_identify_rcn_teryt.py` — ŚLEPA KOLUMNA

| Waga | Problem |
|------|---------|
| 🔴 KRYTYCZNY | Linia 59: `teryt_col = 'JPT_KOD_JE' if 'JPT_KOD_JE' in intersecting.columns else intersecting.columns[0]`. Fallback bierze **pierwszą kolumnę** — która może być `geometry`, `FID`, `osm_id` lub czymkolwiek innym. To jest **absolutnie niebezpieczne** — lista TERYT może zawierać geometrie lub losowe identyfikatory. |
| ⚠️ WAŻNY | Brak filtrowania `intersecting` po minimalnej powierzchni przecięcia. Powiat, który dotyka się z transport_zone jednym pikselem (np. narożnikiem), zostaje włączony do listy WFS — generując tysiące zbędnych zapytań do Geoportalu. |

---

### `07_harvest_rcn.py` — DEAD CODE

| Waga | Problem |
|------|---------|
| 🔴 KRYTYCZNY | **Cały skrypt jest martwy.** Orkiestrator na linii 230-231 komentuje go: "Krok 08 usunięty (dead code — czytał z nieistniejącej ścieżki rcn/)". Ale **07_harvest_rcn.py sam też jest dead code** — linia 27 odwołuje się do `data/cities/{city}/rcn/transactions.gpkg`, ścieżki, która nie istnieje w nowej architekturze. Orkiestrator na linii 229 uruchamia `07_harvest_rcn_omnibus.py` zamiast tego. Skrypt powinien zostać usunięty lub przeniesiony do `scripts/archive_temp/`. |
| ⚠️ WAŻNY | Linia 38: `capture_output=True` bez sprawdzenia `returncode` — ukrywa błędy `ogr2ogr`. Identyczny bug jak problemy 1.4 z `problems.txt`. |

---

### `07_harvest_rcn_omnibus.py` — REGEX XML + BRAK RETRY

| Waga | Problem |
|------|---------|
| 🔴 KRYTYCZNY | Linia 76: **Parsowanie XML za pomocą regexa**. `re.search(r'<wfs:FeatureCollection.*?>(.*)</wfs:FeatureCollection>', part, re.DOTALL)` — klasyczny "Zalgo Text" problem. Jeśli Geoportal doda namespace, zmieni białe znaki lub doda atrybuty, regex nie złapie contentu. Ponadto `.*?` w `FeatureCollection.*?>` jest greedy w kontekście re.DOTALL — może dopasować zbyt wiele. |
| 🔴 KRYTYCZNY | Linia 72-78: Ręczne składanie XML'a ze stringów. Konstruujesz poprawny XML document header, ale wklejasz body z wielu stron **bez usuwania duplikatów namespace'ów** — wynikowy XML może być nievalidny. |
| 🔴 KRYTYCZNY | Linia 131: `subprocess.run([...], capture_output=True)` — **brak `check=True`**, brak sprawdzenia `returncode`. Jeśli `ogr2ogr` padnie, skrypt tego nie zauważy i pójdzie dalej. Dokładnie problem 1.4 z `problems.txt`. |
| ⚠️ WAŻNY | Linia 60: Brak strategii retry. Jedno `requests.get` z `timeout=60`. Jeśli Geoportal poda timeout, powiat jest stracony. Brak `tenacity` ani żadnego mechanizmu ponawiania. |
| ⚠️ WAŻNY | Linia 114: `if len(t) == 4` — filtruje tylko 4-znakowe TERYT-y. Ale `rcn_targets.json` może zawierać 6-znakowe kody gminne. Te zostaną pominięte bez żadnego ostrzeżenia. |
| ⚠️ WAŻNY | Linia 118: `import subprocess` **wewnątrz ciała funkcji `main()`** — poprawne składniowo, ale niehigieniczne. Import powinien być na górze pliku. |

---

### `08_fix_relational_data.py` — ŚLEPA DETEKCJA CRS

| Waga | Problem |
|------|---------|
| ⚠️ WAŻNY | Linia 89-95: Detekcja CRS na podstawie **pierwszego rekordu** (`df['easting'].iloc[0]`). Jeśli pierwszy rekord ma anomalną współrzędną (błąd urzędnika), cały dataset zostanie zreprojektowany z niewłaściwego CRS. Powinno być oparte na medianie lub modzie. |
| ⚠️ WAŻNY | Linia 49-51: Logika koordynatów: `if coords[0] > 6000000: easting, northing = coords[0], coords[1]` — ale jeśli obie współrzędne są > 6000000 (co jest możliwe w strefach EPSG:2177-2179), to pierwszy warunek jest zawsze prawdziwy, niezależnie od kolejności osi. |
| ⚠️ WAŻNY | Linia 86: `df['dok_data'] >= '2025-01-01'` — porównanie stringowe dat. Działa, bo format ISO pozwala na porównanie leksykograficzne, ale to jest kruche. Użyj `pd.Timestamp`. |
| 💡 UWAGA | Linia 104-109: Append do istniejącego pliku bez deduplikacji. Wielokrotne uruchomienie skryptu doda duplikaty transakcji. |

---

### `09_fix_suwalki_geometry.py` — HARDCODED NA JEDNO MIASTO

| Waga | Problem |
|------|---------|
| ⚠️ WAŻNY | Linia 18: `if city_name.lower() != "suwalki": return True` — skrypt **może obsługiwać tylko Suwałki**. Jest to jawnie zaznaczone w komentarzu, ale architektura jest zła: jeśli pojawi się drugie miasto z tą samą patologią GML (polygon-based), trzeba będzie pisać nowy skrypt zamiast parametryzować istniejący. |
| ⚠️ WAŻNY | Linia 60-65: Tworzenie `Point` z 2 koordynat lub `Polygon.centroid` z N koordynat — bez weryfikacji, czy `Polygon` jest zamknięty (pierwszy punkt == ostatni). Otwarty polygon da `Polygon` ShapelyError. |
| 💡 UWAGA | Linia 29: `gml_files[0]` — bierze **pierwszy** plik GML. Jeśli jest ich więcej, reszta jest ignorowana. |

---

### `10_unify_schemas.py` — UNBOUND VARIABLES (ZNANY BUG)

| Waga | Problem |
|------|---------|
| 🔴 KRYTYCZNY | Linia 60-61: `min_allowed` i `max_allowed` definiowane **wyłącznie** wewnątrz `if not valid_prices.empty:`. Jeśli `valid_prices` jest puste, linia 77-78 próbuje odwołać się do `min_allowed` i `max_allowed` — `UnboundLocalError`. **Znany** z `problems.txt` 1.1, ale **nienażywiony**. |
| ⚠️ WAŻNY | Linia 66: `rcn.to_file(rcn_path)` — nadpisuje plik źródłowy bez atomowego zapisu (tmp + rename). Znany z `problems.txt` 1.2, ale **nienaprawiony**. |
| ⚠️ WAŻNY | Podwójna logika czyszczenie RCN (ten skrypt + IQR w `15_compute_stop_dna.py`). Znany z `problems.txt` 5.7 jako redundancja, ale **nierozwiązany**. |
| 💡 UWAGA | Linia 26: Hardcoded lista nazw kolumn powierzchniowych — kruche. Znany z `problems.txt` punkt 4. |

---

### `11_build_master_db.py` — OOM BOMB

| Waga | Problem |
|------|---------|
| 🔴 KRYTYCZNY | Linia 26-27: `all_stops = []` i `all_transactions = []` — ładuje **wszystkie GeoDataFrame'y ze wszystkich miast do RAM** przed `pd.concat`. Przy 60+ miastach i 220k+ transakcjach, to skaluje się kwadratowo i rzuci OOM. **Znany** z `problems.txt` 1.5, ale **nienaprawiony**. |
| ⚠️ WAŻNY | Linia 18-19: `if master_db.exists(): os.remove(master_db)` — bezwarunkowe usunięcie przed odbudową. Jeśli odbudowa padnie w połowie, tracisz **zarówno starą, jak i nową bazę**. Zero atomowości. |

---

### `12_audit_data_quality.py` — UDAWANY AUDYT

| Waga | Problem |
|------|---------|
| 🔴 KRYTYCZNY | Ten skrypt **nie robi żadnego audytu jakości danych**. Sprawdza wyłącznie, czy pliki `.gpkg` istnieją i czy można je otworzyć (`rows=5`). Nie sprawdza: CRS parity, kompletności kolumn, zakresów wartości, pustych geometrii, duplikatów, spójności TERYT. Nazwa "audit_data_quality" jest **kłamliwa**. |
| ⚠️ WAŻNY | Linia 14: `gdf = gpd.read_file(path, rows=5)` — odczytuje tylko 5 wierszy. CRS może być poprawne w nagłówku, ale dane mogą mieć geometrie w innym CRS (np. problem Łodzi z EPSG:2177). Ten audyt tego nie wykryje. |

---

### `13_isolate_city_data.py` — DOBRE, ALE KRUCHE

| Waga | Problem |
|------|---------|
| ⚠️ WAŻNY | Linia 38: `import fiona` wewnątrz bloku warunkowego — poprawne, ale nieczytelne. Fiona powinna być w imporcie na górze pliku (wraz z obsługą `ImportError`). |
| ⚠️ WAŻNY | Linia 63: `cols_to_save = ['TOT', 'geometry'] if 'TOT' in clipped_pop.columns else list(clipped_pop.columns)` — jeśli kolumna `TOT` nie istnieje, zapisuje **wszystkie kolumny z siatki GUS**, co może obejmować dziesiątki kolumn demograficznych i drastycznie zwiększyć rozmiar pliku. |
| 💡 UWAGA | Brak obsługi `--force` w logice — jeśli plik `population_250m.gpkg` istnieje, skrypt go przeskakuje nawet jeśli dane źródłowe się zmieniły. Zmienna `force` jest usuwana w `main()` ale nie przekazywana do `isolate_city`. |

---

### `14_build_isc_valuation.py` — ITERROWS HELL + ŹLE ZAMASKOWANY TIER

| Waga | Problem |
|------|---------|
| 🔴 KRYTYCZNY | Linia 153-162: `for _, row in gdf.iterrows():` — **iteracja po wierszach GeoDataFrame**. Dla miasta z 200k+ POI, to zajmie minuty. Powinno być wektoryzowane z użyciem `.apply()` + bulk lookup. |
| ⚠️ WAŻNY | Linia 32: `"station": ("rail_hub", "T0_MEGA_HUB")` — **KAŻDY** obiekt OSM z tagiem `railway=station` jest potencjalnym Mega Hubem, zanim logika w `identify_v7_9_tag` sprawdzi `uic_ref`. Ale `TAG_WHITELIST` jest używany jako **fallback** (linia 131-133), więc jeśli funkcja `identify_v7_9_tag` nie dopasuje specyficznej logiki (linia 126-129), to `station` z `TAG_WHITELIST` będzie użyty. Problem: tag `station` w OSM pojawia się w wielu kontekstach (stacja benzynowa, stacja transformatorowa). Brak kontekstowej weryfikacji. |
| ⚠️ WAŻNY | Linia 110: Regex HSTORE parser `r'"?([^"=>]+)"?=>"?([^",]+)"?'` — nie obsługuje wartości zawierających cudzysłowy, znaki specjalne ani HSTORE z zagnieżdżeniami. Dla danych OSM z polskimi znakami diakrytycznymi i apostrofami w nazwach, regex może nie dopasować. |
| 💡 UWAGA | Linia 159: `if "rail" in cat_name or "airport" in cat_name: d_mult = 15.0` — mnożnik gęstości 15x jest hardcoded bez żadnej konfigurowalnej tablicy. Zmiana wymaga edycji kodu. |

---

### `15_compute_stop_dna.py` — NAJCIĘŻSZY TECHNICZNIE, NAJWIĘCEJ BUGÓW

| Waga | Problem |
|------|---------|
| 🔴 KRYTYCZNY | Linia 137-139: `gpd.sjoin(infra, h3_hubs, ...)` — sjoin między infrastrukturą (**centroidy poligonów**) a heksagonami H3. Ale `h3_hubs` powstaje z `stops.dissolve()` (linia 91), który tworzy **MultiPoint** geometrie — nie heksagony. `predicate="intersects"` między punkatami a punktami praktycznie nigdy nie zwróci dopasowania, chyba że geometria dissolve przypadkowo jest poligonem. **Cała logika infra_stats może być de facto pusta.** |
| 🔴 KRYTYCZNY | Linia 139: `joined_infra['category'] = joined_infra.get('amenity') or joined_infra.get('shop') or ...` — `DataFrame.get()` zwraca **całą kolumnę (Series)**, nie pojedynczą wartość. Operator `or` między Seriami rzuci `ValueError: The truth value of a Series is ambiguous`. Ten kod **nie może działać** w obecnej formie, chyba że żadne dopasowanie nie istnieje i blok jest pomijany. |
| 🔴 KRYTYCZNY | Linia 152-156: `for _, p in group.iterrows():` wewnątrz `groupby().apply()` — podwójna iteracja, O(N²) złożoność. Znany z `problems.txt` 2.2. |
| ⚠️ WAŻNY | Linia 154: `w = poi_weights.get(tag, {"final_value": 10.0})['final_value']` — `tag` pochodzi z `p.get('amenity')`, ale HSTORE tags zostały w `14_build_isc_valuation.py` przetworzone do **kategorii**, a `poi_valuation.json` zawiera klucze jak `"hospital_clinical"`, nie surowe tagi OSM jak `"hospital"`. Niezgodność kluczy. |
| ⚠️ WAŻNY | Linia 175: `gpd.overlay(pop, h3_hubs, how="intersection")` — O(N*M) złożoność geometryczna. Znany z `problems.txt` punkt 2 (GIS Bottleneck). |
| ⚠️ WAŻNY | Linia 96-99: Filtr IQR po unifikacji — duplikuje logikę z `10_unify_schemas.py`. Znany z `problems.txt` 5.7. |
| 💡 UWAGA | Linia 126: `counts = st.groupby('stop_id').size() / 14.0` — magiczna liczba 14.0 (godziny od 6:00 do 20:00). Hardcoded, bez komentarza wyjaśniającego. |

---

### `orchestrator.py` — WYCIEK LOGIKI BIZNESOWEJ + EMPTY ARG BUG

| Waga | Problem |
|------|---------|
| 🔴 KRYTYCZNY | Linia 162: `"--force" if self.force_update else ""` — przekazuje **pusty string** jako argument do procesu. `subprocess.Popen(["python3", "script.py", "--city", "kielce", ""])` — pusty argument na końcu może powodować błędy w `argparse` w niektórych skryptach. |
| ⚠️ WAŻNY | Linia 169-182: Walidacja biznesowa (km², populacja) w orkiestratorze. Znany z `problems.txt` 4.1. |
| ⚠️ WAŻNY | Linia 68: `self.logger.warning(...)` — logger nie jest jeszcze zainicjowany w `_load_state()`, bo `self.logger` jest ustawiany na linii 42, po `self.state = self._load_state()` na linii 41. Potencjalny `AttributeError`. |

---

## CZĘŚĆ II: ANALIZA KRZYŻOWA Z `problems.txt`

### Problemy ZNANE, ale NIENAPRAWIONE w kodzie:

| # | Problem | Status |
|---|---------|--------|
| 1.1 | UnboundLocalError w `10_unify_schemas.py` | ❌ **Wciąż obecny** (linia 60-61) |
| 1.2 | Brak atomowego zapisu | ❌ **Wciąż obecny** (wszystkie skrypty) |
| 1.3 | Regex XML w `07_omnibus` | ❌ **Wciąż obecny** (linia 76) |
| 1.4 | Brak `check=True` w subprocess | ❌ **Wciąż obecny** (linia 131 `07_omnibus`, inne) |
| 1.5 | OOM w `11_build_master_db.py` | ❌ **Wciąż obecny** (linia 26-27) |
| 2.2 | iterrows() w `15_compute_stop_dna.py` | ❌ **Wciąż obecny** (linia 152-156) |
| 2.5 | Calendar w GTFS | ✅ Naprawiony (v9.0 w `15_compute_stop_dna.py`) |
| 3.3 | Śmieci w RCN (IQR) | ⚠️ Częściowo — ale zduplikowana logika |
| 3.4 | GTFS > 24:00 | ✅ Naprawiony (`parse_gtfs_time_safe`) |
| 4.1 | Wyciek logiki do orkiestratora | ❌ **Wciąż obecny** (linia 169-182) |
| 4.2 | ZIP-y w GIT | ❌ **Wciąż obecny** (`archive_old_scripts.zip`) |
| 5.5 | OOM eliminacja Streaming | ❌ **Wciąż obecny** |
| 5.6 | Rygor XML/Subprocess | ❌ **Wciąż obecny** |
| 5.7 | Redundancja logiki czyszczenia | ❌ **Wciąż obecny** |

### Problemy z `problems.txt` POMINIĘTE w audycie, ale POPRAWNE:

Dodatkowe 4 punkty z końca `problems.txt` (Frontend Bridge, gpd.overlay, Network Fragility, Hardcoded columns) są trafne i potwierdzone w kodzie.

---

## CZĘŚĆ III: PROBLEMY NOWE — NIEOBECNE W `problems.txt`

| # | Problem | Skrypt | Waga |
|---|---------|--------|------|
| N1 | `00_init_environment.py` kopiuje plik na samego siebie | `00` | 🔴 |
| N2 | `r.content` ładuje cały ZIP/response do RAM (stream=True jest martwy) | `01`, `04` | 🔴 |
| N3 | Fałszywy MAD — oblicza medianę zamiast MAD | `02` | 🔴 |
| N4 | `07_harvest_rcn.py` jest dead code | `07` | ⚠️ |
| N5 | TERYT fallback bierze pierwszą losową kolumnę | `06` | 🔴 |
| N6 | CRS detekcja na podstawie jednego rekordu | `08` | ⚠️ |
| N7 | `12_audit_data_quality.py` nie robi żadnego audytu jakości | `12` | 🔴 |
| N8 | `sjoin(infra, h3_hubs)` — punkty vs punkty nigdy nie dają intersects | `15` | 🔴 |
| N9 | `DataFrame.get()` z operatorem `or` rzuci ValueError | `15` | 🔴 |
| N10 | Niezgodność kluczy `poi_valuation.json` (kategorie vs surowe OSM tagi) | `15` | ⚠️ |
| N11 | Orchestrator: pusty string jako argument do subprocess | `orch` | 🔴 |
| N12 | Orchestrator: logger niezainicjalizowany w `_load_state()` | `orch` | ⚠️ |
| N13 | `requirements.txt` brak: `lxml`, `h3`, `tenacity`, `urllib3` | global | ⚠️ |
| N14 | Zero testów jednostkowych/integracyjnych — 0 plików testowych w main codebase | global | 🔴 |
| N15 | Brak spójnego interfejsu CLI — argumenty `--city` vs none vs `--force` są niespójne | global | ⚠️ |
| N16 | `extract_config.json` — Łódź ma BBOX z ujemnymi współrzędnymi (-0.01, -0.01) | config | 🔴 |
| N17 | `warnings.filterwarnings("ignore")` — w 5 skryptach, maskuje realne błędy | global | ⚠️ |

---

## CZĘŚĆ IV: PODSUMOWANIE STATYSTYCZNE

| Metryka | Wartość |
|---------|---------|
| Skryptów pipeline | 17 |
| Skryptów z krytycznymi bugami (🔴) | **13 / 17 (76%)** |
| Plików testowych | **0** |
| Bugów z `problems.txt` nienaprawionych | **11 / 15 (73%)** |
| Nowych bugów nieznanych w `problems.txt` | **17** |
| Łącznie zidentyfikowanych problemów | **~45** |
| Testy jednostkowe | **0** |
| Testy integracyjne | **0** |

---

## CZĘŚĆ V: PLAN IMPLEMENTACJI NAPRAWCZEJ

### Priorytet 1 — SHOW-STOPPERY (Blokują działanie pipeline'u)

> [!CAUTION]
> Te bugi mogą powodować crash, uszkodzenie danych lub ciche generowanie absurdalnych wyników.

#### [MODIFY] [10_unify_schemas.py](file:///home/gzyms/Dev%20Projects/kielce-analiza/scripts/pipeline/10_unify_schemas.py)
- Inicjalizacja `min_allowed = 0` i `max_allowed = 0` oraz `avg_price = 0`, `median_price = 0` **przed** blokiem warunkowym
- Wdrożenie atomowego zapisu: `tmp_path = rcn_path.with_suffix('.tmp.gpkg')` → `os.replace()`

#### [MODIFY] [15_compute_stop_dna.py](file:///home/gzyms/Dev%20Projects/kielce-analiza/scripts/pipeline/15_compute_stop_dna.py)
- **Naprawić linię 91**: `dissolve()` tworzy MultiPoint — musi tworzyć H3 hex polygony via `h3.cell_to_boundary()` 
- **Naprawić linię 139**: Zamienić `DataFrame.get()` z `or` na `.apply()` per-row lub wektorowe `np.where`/`fillna`
- **Naprawić linię 137**: sjoin infra → h3_hubs wymaga h3_hubs jako poligonów (heksagonów), nie punktów
- **Naprawić linię 175**: Zastąpić `gpd.overlay` → `sjoin` + proporcjonalne wagi populacyjne
- **Usunąć redundantny IQR filter** (linia 96-99) — dane powinny być już oczyszczone w kroku 10

#### [MODIFY] [orchestrator.py](file:///home/gzyms/Dev%20Projects/kielce-analiza/orchestrator.py)
- **Naprawić linię 162**: Usunąć pusty string — `cmd = [sys.executable, str(script_path), "--city", city]; if self.force_update: cmd.append("--force")`
- Przenieść logger init **przed** `_load_state()` (zamienić linie 41-42)
- Usunąć sanity checks biznesowe (linia 169-182) — przenieść do poszczególnych skryptów

---

### Priorytet 2 — INTEGRALNOŚĆ DANYCH (Ciche generowanie złych wyników)

#### [MODIFY] [02_collect_stops.py](file:///home/gzyms/Dev%20Projects/kielce-analiza/scripts/pipeline/02_collect_stops.py)
- **Naprawić MAD**: `deviations = (final_city_stops['final_dist'] - final_city_stops['final_dist'].median()).abs()` → `mad = deviations.median()` → `cutoff = mad * 6`

#### [MODIFY] [06_identify_rcn_teryt.py](file:///home/gzyms/Dev%20Projects/kielce-analiza/scripts/pipeline/06_identify_rcn_teryt.py)
- **Naprawić fallback kolumny**: zamienić `intersecting.columns[0]` na jawne szukanie kolumny TERYT (regex na "JPT", "KOD", "TERYT") z `sys.exit(1)` jeśli nie znaleziono

#### [MODIFY] [07_harvest_rcn_omnibus.py](file:///home/gzyms/Dev%20Projects/kielce-analiza/scripts/pipeline/07_harvest_rcn_omnibus.py)
- Zastąpić regex XML parserem `lxml.etree`
- Dodać `subprocess.run(..., check=True)` na linii 131
- Dodać retry z `tenacity` (`@retry(wait=wait_exponential(...), stop=stop_after_attempt(5))`)
- Przenieść `import subprocess` na górę pliku

#### [MODIFY] [14_build_isc_valuation.py](file:///home/gzyms/Dev%20Projects/kielce-analiza/scripts/pipeline/14_build_isc_valuation.py)
- Wektoryzacja: zamienić `for _, row in gdf.iterrows()` na `gdf.apply(identify_v7_9_tag, axis=1)` lub bulk lookup

---

### Priorytet 3 — ODPORNOŚĆ I SKALOWALNOŚĆ

#### [MODIFY] [11_build_master_db.py](file:///home/gzyms/Dev%20Projects/kielce-analiza/scripts/pipeline/11_build_master_db.py)
- Zastąpić `pd.concat()` w RAM na **strumieniowe dopisywanie** via `ogr2ogr -update -append` lub iteracyjne `to_file(..., mode='a')`

#### [MODIFY] [01_fetch_gtfs.py](file:///home/gzyms/Dev%20Projects/kielce-analiza/scripts/pipeline/01_fetch_gtfs.py)
- Ekstrakcja `GTFS_SOURCES` do `config/gtfs_sources.json`
- Naprawić martwego `stream=True` — zapis response do pliku tymczasowego zamiast `r.content`

#### [MODIFY] [04_download_population.py](file:///home/gzyms/Dev%20Projects/kielce-analiza/scripts/pipeline/04_download_population.py)
- Zapis streamu na dysk zamiast `io.BytesIO(r.content)`

#### [MODIFY] [12_audit_data_quality.py](file:///home/gzyms/Dev%20Projects/kielce-analiza/scripts/pipeline/12_audit_data_quality.py)
- Dodać prawdziwe testy jakości: weryfikacja CRS, kompletność kolumn, zakresy `price_m2`, puste geometrie, duplikaty, spójność `city` z folderem

---

### Priorytet 4 — HIGIENA KODU I DEVOPS

#### [DELETE] [07_harvest_rcn.py](file:///home/gzyms/Dev%20Projects/kielce-analiza/scripts/pipeline/07_harvest_rcn.py)
- Dead code — przenieść do archiwum

#### [MODIFY] [requirements.txt](file:///home/gzyms/Dev%20Projects/kielce-analiza/requirements.txt)
- Dodać: `lxml`, `h3`, `tenacity`, `urllib3`
- Dodać pinowane wersje (`pandas>=2.0`, `geopandas>=1.0`)

#### [MODIFY] [.gitignore](file:///home/gzyms/Dev%20Projects/kielce-analiza/.gitignore)
- Dodać: `scripts/archive_old_scripts.zip`, `scripts/archive_temp/`, `cache/`, `*.pyc`

#### [NEW] `tests/` directory
- Dodać testy jednostkowe dla kluczowych funkcji: `normalize_name()`, `parse_hstore()`, `clean_ref()`, `parse_gtfs_time_safe()`, `identify_v7_9_tag()`

#### [MODIFY] [config/extract_config.json](file:///home/gzyms/Dev%20Projects/kielce-analiza/config/extract_config.json)
- **Naprawić BBOX Łodzi** (linia 137-141): wartości `-0.012` to oczywiście błąd — powinny być ok. `19.3, 51.6, 19.7, 51.9`

#### Globalna zmiana: usunąć `warnings.filterwarnings("ignore")` ze wszystkich skryptów
- Zastąpić selektywnymi filtrami: `warnings.filterwarnings("ignore", category=FutureWarning, module="geopandas")`

---

## Verification Plan

### Automated Tests

**Po naprawach Priorytetu 1:**
```bash
# Dry-run orkiestratora na 1 mieście (np. kielce)
python3 orchestrator.py --cities kielce --data-dir data --force-update --step 10
python3 orchestrator.py --cities kielce --data-dir data --force-update --step 15

# Sprawdzenie, czy brak ValueError/UnboundLocalError w logach
grep -i "error\|traceback\|exception" data/logs/pipeline_run.log
```

**Test `10_unify_schemas.py` z pustymi danymi:**
```bash
# Stworzenie pustego GeoPackage dla miasta testowego
python3 -c "
import geopandas as gpd
from shapely.geometry import Point
gdf = gpd.GeoDataFrame(geometry=[], crs='EPSG:2180')
gdf.to_file('/tmp/test_empty.gpkg', driver='GPKG')
"
# Uruchomienie unifikacji na pustym zestawie — nie powinno rzucić UnboundLocalError
python3 scripts/pipeline/10_unify_schemas.py --city test_empty
```

**Test `15_compute_stop_dna.py` — weryfikacja, że sjoin zwraca wyniki:**
```bash
python3 scripts/pipeline/15_compute_stop_dna.py --city kielce 2>&1 | grep -E "CRITICAL|ERROR|h3_hubs"
```

### Manual Verification
- Po naprawach Priorytetu 1-2: uruchomienie pełnego pipeline na jednym mieście (kielce) i porównanie wynikowego `stop_dna.gpkg` — czy kolumny `infra_score`, `transit_freq`, `pop_val` zawierają sensowne wartości ≠ 0
- Sprawdzenie w QGIS, czy heksagony H3 pokrywają się z przystankami (wizualna weryfikacja)
