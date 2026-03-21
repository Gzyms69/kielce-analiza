# Plan Audytu Absolutnego (100% DNA Validation)

Poniższy dokument stanowi krytyczną analizę obecnych, rozproszonych narzędzi audytowych oraz wyczerpujący plan budowy ostatecznego "Orkiestratora Audytowego" (skryptu `100_percent_dna_validator.py`), który w stu procentach udowodni poprawność matematyczną, przestrzenną i relacyjną danych stworzonych przez pipeline.

---

## 1. Analiza obecnych skryptów audytowych (Stan Zastany)

Obecnie w katalogu `scripts/tools/` znajduje się 5 głównych skryptów próbujących walidować dane. Ich analiza linijka po linijce obnaża następujące braki:

### A. `absolute_master_audit.py`
*   **Co robi:** Przelicza surową liczbę punktów przestrzennych. Weryfikuje czy istnieją puste nazwy przystanków, zlicza całkowitą populację w `population_250m.gpkg` oraz obiekty punktowe/poligonowe w OSMIUM, a także daty skrajne dla RCN.
*   **Krytyczne braki:** Skrypt bada pliki *przed* ich fuzją analityczną. W ogóle nie dotyka ostatecznego pliku wektorowego (wyników DNA z kroku 15). Stanowi dowód zebrania danych, a nie dowód ich poprawnego połączenia. Nie bada krzyżowania się warstw.

### B. `master_national_auditor.py`
*   **Co robi:** Bada rozkład RCN (interkwartyle). Porównuje populację z "zhardkodowanym" słownikiem `CITY_BASELINES` (weryfikacja rzędu wielkości). Jako jedyny wczytuje `stop_dna.gpkg` i sprawdza wskaźnik fallbacku RCN (zapożyczenia mediany dla przystanku). Drukuje na ekran Top 5 i Bottom 5 przystanków z podziałem na 7 okrojonych kolumn.
*   **Krytyczne braki:**
    *   Wydruk Top/Bottom ucina ponad połowę wygenerowanych wektorów (np. szczegółowych wyników wag Tier 1-4).
    *   Całkowity brak analizy środka rozkładu Gaussa (Random 5).
    *   Nie sprawdza braków we wskaźnikach innych niż cena nieruchomości.

### C. `deep_dna_audit.py`
*   **Co robi:** Podlicza całkowitą populację i sumuje transakcje. Tworzy listę "Top 20 kategorii POI według wagi".
*   **Krytyczne braki:** Oszukuje. Czyta "Top 20" z fizycznego pliku konfiguracyjnego `poi_valuation.json`, zamiast faktycznie policzyć fizyczne intersekcje na mapie. To udowadnia jedynie, że plik konfiguracyjny istnieje, a nie, że infrastruktura została w ogóle poprawnie powiązana z węzłami H3.

### D. `verify_final_pipeline.py`
*   **Co robi:** Typowy skrypt typu "status-checker". Sprawdza istnienie 5 plików kluczowych w folderach miejskich i generuje wynik "100% INTEGRITY" jeśli pliki fizycznie leżą na dysku.
*   **Krytyczne braki:** Plik może być pełen pustych wartości (NaN) lub zawierać 1 wiersz, a skrypt i tak wyda werdykt pozytywny. Nie schodzi poniżej warstwy systemu plików.

### E. `comprehensive_national_audit.py`
*   **Co robi:** Powiela logikę status-checkera, łącząc go z okrojonym wydrukiem tabelarycznym z `master_national_auditor.py`.
*   **Krytyczne braki:** Te same co wyżej – redundancja kodu i brak analityki wektorowej.

---

## 2. Projekt Ostatecznego "Orkiestratora Audytowego" (`100_percent_dna_validator.py`)

Zamiast łatać obecny bałagan, stworzymy jeden bezkompromisowy skrypt sprawdzający na wylot plik `04_results/stop_dna.gpkg` oraz bazowe przestrzenie `02_spatial/infrastructure.gpkg` i `transactions.gpkg`.

Skrypt zostanie zaprojektowany obiektowo, by móc analizować miasta równolegle (wzorem głównego orkiestratora), ale jego wyniki będą zbierane do jednego ustrukturyzowanego i eleganckiego raportu.

### Faza I: Twarda Weryfikacja Integralności, Schematów i Anomalii (Data Integrity Check)
Algorytm przeskanuje wektor każdego z heksagonów H3 w poszukiwaniu błędów krytycznych matematyki z kroku 15 oraz sprawdzi poprawność struktur bazowych:
1.  **Skanowanie NaN/NULL w plikach wynikowych:** Skrypt rzuci twardym błędem i odrzuci jakość, jeśli w kolumnach analitycznych (`pop_val`, `infra_score`, `market_val`, `transit_freq`, `local_score`, `grade`) znajdzie się choć jedna pusta wartość (`NaN`).
2.  **Skanowanie anomalii liczbowych (Bounds Checking):** Wykrywanie wartości niemożliwych fizycznie, np.:
    *   Wartości ujemne dla atrybutów wagowych (`infra_score < 0`, `pop_val < 0`).
    *   Anomalnie niskie/wysokie ceny nieruchomości wykraczające poza granice błędu statystycznego (np. `market_val < 100` lub `market_val > 500000`).
3.  **Weryfikacja Przestrzenna i Układu Współrzędnych:**
    *   Bezwzględne żądanie weryfikacji układu współrzędnych: Plik docelowy MUSI znajdować się w systemie metrycznym `EPSG:2180`. Jeśli układ nie zostanie poprawnie odczytany przez geopandas, miasto oblewa audyt.
    *   Sprawdzenie, czy każdy wiersz wynikowy posiada poprawny, zamknięty typ geometrii `Polygon` reprezentujący rzeczywisty obrys H3, a nie tylko centroid w postaci punktu.
4.  **Weryfikacja danych źródłowych RCN (Kluczowe kolumny):** Sprawdzenie czy pierwotne pliki bazy nieruchomości miały na 100% poprawnie parsowane kluczowe wskaźniki (powierzchnia, data, cena brutto). 

### Faza II: Bezwzględne Pokrycie Wzajemne Danych (Mutual Coverage Analysis)
Prawdziwe udowodnienie fuzji polega na znalezieniu "białych plam" w krzyżowaniu danych dla każdego miasta:
1.  **Test Pustyni Populacyjnej:** Odsetek i bezwzględna liczba heksagonów, w których zmapowana liczba ludności wyniosła równe `0.0`. Jeśli ten wskaźnik jest zbyt duży, oznacza to rozwarstwienie geometrii (grid minął się z przystankami).
2.  **Test Pustyni Infrastrukturalnej:** Odsetek heksagonów, w których bufor H3 nie przeciął ani jednego punktu POI z OSM (`infra_score == 0`).
3.  **Test Głuchego Przystanku (Ghost Stop):** Odsetek heksagonów, do których dane z GTFS nie potrafiły dowiązać żadnego odjazdu (`transit_freq == 0`).
4.  **Wskaźnik Bezpieczeństwa Interpolacji RCN (Fallback Ratio):** Dokładny odsetek heksagonów, które nie miały w promieniu kilku kilometrów żadnej transakcji deweloperskiej i musiały użyć średniej ratunkowej (mediany) dla całego miasta. Jest to doskonała miara jakości pokrycia historycznego z Geoportalu.

### Faza III: Realny Dowód Występowania Infrastruktury (True Top 20 POI Intersections)
Skrypt przestanie ufać plikom konfiguracyjnym. Zmierzy się z gołą mapą przestrzenną:
1.  Skrypt otworzy `infrastructure.gpkg` (warstwy `points` oraz `multipolygons`) bezpośrednio wyprodukowane przez silnik OSMIUM.
2.  Wykona fizyczne nałożenie (Spatial Join) wszystkich elementów na obrysy wynikowych przystanków.
3.  Zsumuje wystąpienia każdego konkretnego unikalnego tagu (klucze `amenity`, `shop`, `leisure`).
4.  Przemnoży je przez odpowiednie wagi i wylistuje **rzeczywiste TOP 20 zwalidowanych obiektów**, które wygenerowały największy ruch punktowy w DNA miasta. Udowodni to ostatecznie bezbłędność całego mechanizmu pobierania z Geofabrik.

### Faza IV: Pełny Deep-Dump Badawczy (Próbki Top 5 / Bottom 5 / Random 5)
Tu nastąpi najpotężniejsza zmiana – stworzymy złotą jakość weryfikacji ręcznej (Data Spot-Checking), niezbędną by nie ufać ślepo maszynom:
1.  **Ekstrakcja próbek według skali ocen (`local_score`):** Algorytm wyłuska wektory z każdego miasta tworząc 3 wiązki testowe:
    *   **Top 5:** Absolutna elita miejska, ścisłe najwyższe noty.
    *   **Bottom 5:** Najgorsze, peryferyjne "dziury" w rankingu miasta.
    *   **Random 5 (Środek krzywej Gaussa):** Ekstrakcja 5 przystanków losowanych w sposób deterministyczny (stały Seed do reprodukcji), wyłącznie ze "środkowych 60%" zbioru (odrzucamy górne 20% i dolne 20%). Udowodni to, że wartości uśrednione mają racjonalny sens matematyczny.
2.  **Pełny Zrzut Pionowy (Cross-Dump):** Dla każdego z wylosowanych 15 przystanków per miasto, skrypt nie wydrukuje zwykłej spłaszczonej tabeli tekstowej. Dla tych rekordów dokona transpozycji. Wypisze szczegółowo:
    *   Klucz H3.
    *   Oryginalną nazwę przystanku i doczepioną częstotliwość GTFS.
    *   Wszystkie wyliczone metryki cząstkowe: od `local_rank` po każdą wyodrębnioną wartość jak `market_val`, `infra_score`.
    *   Będzie to miało format łatwy do skopiowania i załadowania w środowiskach typu Excel czy QGIS.

### Faza V: Mechanizm Konkluzji i Raportowania
Nowy Audytor zaprzestanie wysyłania tysięcy niewygodnych danych do ulotnej konsoli terminala.
1.  Logika skryptu zrzuci całą zebraną analizę do ustrukturyzowanego dokumentu: `reports/100_PERCENT_VALIDATION_REPORT.md`.
2.  Użyje profesjonalnego formatowania Markdown, wykorzystując tabele, podział na sekcje per miasto oraz pogrubienia anomalii.
3.  Zakończy się potężną sekcją **"ZBIORCZY WERDYKT JAKOŚCIOWY"** z flagą SUKCESU lub KRYTYCZNEGO BŁĘDU, generowaną rygorystycznie na podstawie procenta akceptowalnych braków we wszystkich filarach danych. Skrypt musi sam podjąć decyzję czy praca analityczna jest godna zaufania, a my dostaniemy na to żelazny certyfikat tekstowy.