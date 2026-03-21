# ABSOLUTE 100% DNA VALIDATION REPORT - 2026-03-21
**Dokładny czas generowania:** 2026-03-21 23:07:35
---
## ZBIORCZE PODSUMOWANIE MIAST
- **Miasta:** 30 | **Błędy:** 0 | **Węzły H3:** 60,265

# WERDYKT: 🟢 **SUKCES**
---


## PODSUMOWANIE POLSKI

- **POPULACJA:** 16,867,234 | **RCN:** 1,104,389
- **OSM PUNKTY:** 4,327,125 | **OSM POLIGONY:** 6,313,682
---

## AGLOMERACJA: BIALYSTOK
**Status:** ✅ SUKCES

### Faza 0: Stan Danych
- **Całkowita populacja w strefie miasta:** 383,482 (Baseline: 290,000) [✅ OK]
- **Ilość Transakcji RCN:** 34,402
- **Zakres Dat RCN:** 2020-01-02 do 2026-03-05
- **Ceny RCN (PLN/m²):** Średnia=7,968 | Mediana=7,004 | Max=350,000 | IQR=[5,656 - 9,059]
- **Infrastruktura OSM (Punkty):** 53,630
- **Infrastruktura OSM (Poligony/Budynki):** 122,204
- Baza transakcyjna `.gpkg` ustrukturyzowana poprawnie.

### Faza I & II: Pokrycie (Zero-Values)
- **Pustynia Populacyjna:** 332 (12.2%)
- **Pustynia Infrastrukturalna:** 7 (0.3%)
- **Głuche Przystanki:** 21 (0.8%)
- **Wskaźnik Fallback RCN:** 1757 (64.8%) (Mediana RCN dla miasta: 6830)

### Faza III: Udowodnione POI w Promieniu 500m

**Rzeczywiste TOP 20 zwalidowanych obiektów (Intersekcja bufor 500m):**

| Tag OSM | Zliczone (Ilość) | Prawdziwa Waga JSON | Całkowita Siła (Score) |
|---|---|---|---|
| `supermarket` | 2433 | 9,968,397.96 | **24,253,112,236.68** |
| `sports_centre` | 481 | 1,071,369.87 | **515,328,907.47** |
| `marketplace` | 213 | 1,605,275.61 | **341,923,704.93** |
| `place_of_worship` | 2689 | 92,069.44 | **247,574,724.16** |
| `pharmacy` | 2927 | 61,862.54 | **181,071,654.58** |
| `bank` | 1831 | 67,844.84 | **124,223,902.04** |
| `post_office` | 1140 | 66,458.89 | **75,763,134.60** |
| `bench` | 27740 | 0.00 | **0.00** |
| `waste_basket` | 9761 | 0.00 | **0.00** |
| `parking` | 74326 | 0.00 | **0.00** |
| `parcel_locker` | 7524 | 0.00 | **0.00** |
| `bicycle_parking` | 7050 | 0.00 | **0.00** |
| `vending_machine` | 6570 | 0.00 | **0.00** |
| `parking_entrance` | 5145 | 0.00 | **0.00** |
| `restaurant` | 4602 | 0.00 | **0.00** |
| `recycling` | 3757 | 0.00 | **0.00** |
| `atm` | 2840 | 0.00 | **0.00** |
| `fast_food` | 2772 | 0.00 | **0.00** |
| `taxi` | 2626 | 0.00 | **0.00** |
| `doctors` | 1702 | 0.00 | **0.00** |

### Faza IV: Badanie Próbek Oceny Złotej

#### 🏆 TOP 5 (Najlepsze 5 przystanków w mieście)
<details><summary><b>Paszport Węzła: Składowa/Tunel (438) (H3: 891f5133693ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Składowa/Tunel (438)
  stop_id             : 438
  city                : bialystok
  h3_index            : 891f5133693ffff
  stop_lat            : 53.1225
  stop_lon            : 23.1225
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : bialystok

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 3.1376

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 914.0284
  raw_gravity         : 914.0284
  domain_count        : 0.0000
  infra_score_log     : 6.8190

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 63.7143
  hourly_freq         : 11.2143
  transit_freq_log    : 4.1700

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 31329.1139
  liquidity           : 1.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 80
  pop_val_log         : 4.3944
```
</details>
<details><summary><b>Paszport Węzła: Składowa/Octowa (439) (H3: 891f5133693ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Składowa/Octowa (439)
  stop_id             : 439
  city                : bialystok
  h3_index            : 891f5133693ffff
  stop_lat            : 53.1227
  stop_lon            : 23.1218
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : bialystok

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 3.1376

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 914.0284
  raw_gravity         : 914.0284
  domain_count        : 0.0000
  infra_score_log     : 6.8190

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 63.7143
  hourly_freq         : 13.4286
  transit_freq_log    : 4.1700

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 31329.1139
  liquidity           : 1.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 80
  pop_val_log         : 4.3944
```
</details>
<details><summary><b>Paszport Węzła: Składowa/Tunel(438) (H3: 891f5133693ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Składowa/Tunel(438)
  stop_id             : 438
  city                : bialystok
  h3_index            : 891f5133693ffff
  stop_lat            : 53.1225
  stop_lon            : 23.1225
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : google_transit

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 3.1376

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 914.0284
  raw_gravity         : 914.0284
  domain_count        : 0.0000
  infra_score_log     : 6.8190

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 63.7143
  hourly_freq         : 11.2143
  transit_freq_log    : 4.1700

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 31329.1139
  liquidity           : 1.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 80
  pop_val_log         : 4.3944
```
</details>
<details><summary><b>Paszport Węzła: Składowa/Octowa(439) (H3: 891f5133693ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Składowa/Octowa(439)
  stop_id             : 439
  city                : bialystok
  h3_index            : 891f5133693ffff
  stop_lat            : 53.1227
  stop_lon            : 23.1218
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : google_transit

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 3.1376

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 914.0284
  raw_gravity         : 914.0284
  domain_count        : 0.0000
  infra_score_log     : 6.8190

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 63.7143
  hourly_freq         : 13.4286
  transit_freq_log    : 4.1700

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 31329.1139
  liquidity           : 1.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 80
  pop_val_log         : 4.3944
```
</details>
<details><summary><b>Paszport Węzła: Kopernika/Składowa(177) (H3: 891f5133693ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Kopernika/Składowa(177)
  stop_id             : 177
  city                : bialystok
  h3_index            : 891f5133693ffff
  stop_lat            : 53.1234
  stop_lon            : 23.1227
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : google_transit

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 3.1376

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 914.0284
  raw_gravity         : 914.0284
  domain_count        : 0.0000
  infra_score_log     : 6.8190

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 63.7143
  hourly_freq         : 7.2143
  transit_freq_log    : 4.1700

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 31329.1139
  liquidity           : 1.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 80
  pop_val_log         : 4.3944
```
</details>

#### 🎲 RANDOM 5 (Środkowe przystanki miasta)
<details><summary><b>Paszport Węzła: Pogorzałki Klub (H3: 891f5114c13ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Pogorzałki Klub
  stop_id             : 124
  city                : bialystok
  h3_index            : 891f5114c13ffff
  stop_lat            : 53.2222
  stop_lon            : 22.9515
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : bialystok-wschod

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : C
  local_percentile    : 60.9557
  local_score_raw     : 0.0884

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 166.1534
  raw_gravity         : 166.1534
  domain_count        : 0.0000
  infra_score_log     : 5.1189

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 28.5000
  hourly_freq         : 3.5714
  transit_freq_log    : 3.3844

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6830.4583
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 33
  pop_val_log         : 3.5264
```
</details>
<details><summary><b>Paszport Węzła: Szaciły (H3: 891f51ab40fffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Szaciły
  stop_id             : 150
  city                : bialystok
  h3_index            : 891f51ab40fffff
  stop_lat            : 53.2492
  stop_lon            : 23.0300
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : bialystok-wschod

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : D
  local_percentile    : 47.0862
  local_score_raw     : -0.1789

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 87.6682
  raw_gravity         : 87.6682
  domain_count        : 0.0000
  infra_score_log     : 4.4849

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 16.7143
  hourly_freq         : 8.2857
  transit_freq_log    : 2.8744

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6830.4583
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 18
  pop_val_log         : 2.9444
```
</details>
<details><summary><b>Paszport Węzła: Sikorskiego/Pętla(433) (H3: 891f51069d7ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Sikorskiego/Pętla(433)
  stop_id             : 433
  city                : bialystok
  h3_index            : 891f51069d7ffff
  stop_lat            : 53.1350
  stop_lon            : 23.1021
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : google_transit

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : D
  local_percentile    : 36.3636
  local_score_raw     : -0.3425

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 52.1363
  raw_gravity         : 52.1363
  domain_count        : 0.0000
  infra_score_log     : 3.9729

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 21.7143
  hourly_freq         : 2.7857
  transit_freq_log    : 3.1230

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6830.4583
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Niemeńska I (C)(264) (H3: 891f513248fffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Niemeńska I (C)(264)
  stop_id             : 264
  city                : bialystok
  h3_index            : 891f513248fffff
  stop_lat            : 53.1675
  stop_lon            : 23.2212
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : google_transit

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : D
  local_percentile    : 44.9883
  local_score_raw     : -0.2128

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 774.9851
  raw_gravity         : 774.9851
  domain_count        : 0.0000
  infra_score_log     : 6.6541

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 9.0000
  hourly_freq         : 4.5000
  transit_freq_log    : 2.3026

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 5067.5908
  liquidity           : 20.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 153
  pop_val_log         : 5.0370
```
</details>
<details><summary><b>Paszport Węzła: Gen. Sosabowskiego/Kapralska(191) (H3: 891f5132653ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Gen. Sosabowskiego/Kapralska(191)
  stop_id             : 191
  city                : bialystok
  h3_index            : 891f5132653ffff
  stop_lat            : 53.1442
  stop_lon            : 23.1877
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : google_transit

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : B
  local_percentile    : 77.6224
  local_score_raw     : 0.5068

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 1037.4578
  raw_gravity         : 1037.4578
  domain_count        : 0.0000
  infra_score_log     : 6.9455

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 36.5714
  hourly_freq         : 9.0714
  transit_freq_log    : 3.6262

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6942.5901
  liquidity           : 1.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 351
  pop_val_log         : 5.8636
```
</details>

#### 💩 BOTTOM 5 (Najsłabsze 5 przystanków)
<details><summary><b>Paszport Węzła: Dobrzyniewo Duże (H3: 891f511497bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Dobrzyniewo Duże
  stop_id             : 24075
  city                : bialystok
  h3_index            : 891f511497bffff
  stop_lat            : 53.1943
  stop_lon            : 23.0027
  lat_grid            : 53.1900
  lon_grid            : 23.0000
  norm_name           : dobrzyniewoduze
  source              : polish_trains

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.2331
  local_score_raw     : -1.4065

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 39.1230
  raw_gravity         : 39.1230
  domain_count        : 0.0000
  infra_score_log     : 3.6919

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.0000
  hourly_freq         : 0.0000
  transit_freq_log    : 0.0000

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6830.4583
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Złotniki/Kolonia(1477) (H3: 891f513816fffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Złotniki/Kolonia(1477)
  stop_id             : 1477
  city                : bialystok
  h3_index            : 891f513816fffff
  stop_lat            : 52.9655
  stop_lon            : 23.1568
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : google_transit

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.1166
  local_score_raw     : -1.4933

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 0.0000
  raw_gravity         : 0.0000
  domain_count        : 0.0000
  infra_score_log     : 0.0000

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 1.1429
  hourly_freq         : 0.2857
  transit_freq_log    : 0.7621

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6830.4583
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Złotniki/Kolonia (1353) (H3: 891f513816fffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Złotniki/Kolonia (1353)
  stop_id             : 1353
  city                : bialystok
  h3_index            : 891f513816fffff
  stop_lat            : 52.9655
  stop_lon            : 23.1568
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : bialystok

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.1166
  local_score_raw     : -1.4933

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 0.0000
  raw_gravity         : 0.0000
  domain_count        : 0.0000
  infra_score_log     : 0.0000

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 1.1429
  hourly_freq         : 0.2857
  transit_freq_log    : 0.7621

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6830.4583
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Złotniki/Kolonia (1477) (H3: 891f513816fffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Złotniki/Kolonia (1477)
  stop_id             : 1477
  city                : bialystok
  h3_index            : 891f513816fffff
  stop_lat            : 52.9655
  stop_lon            : 23.1568
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : bialystok

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.1166
  local_score_raw     : -1.4933

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 0.0000
  raw_gravity         : 0.0000
  domain_count        : 0.0000
  infra_score_log     : 0.0000

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 1.1429
  hourly_freq         : 0.2857
  transit_freq_log    : 0.7621

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6830.4583
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Złotniki/Kolonia(1353) (H3: 891f513816fffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Złotniki/Kolonia(1353)
  stop_id             : 1353
  city                : bialystok
  h3_index            : 891f513816fffff
  stop_lat            : 52.9655
  stop_lon            : 23.1568
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : google_transit

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.1166
  local_score_raw     : -1.4933

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 0.0000
  raw_gravity         : 0.0000
  domain_count        : 0.0000
  infra_score_log     : 0.0000

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 1.1429
  hourly_freq         : 0.2857
  transit_freq_log    : 0.7621

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6830.4583
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>

---

## AGLOMERACJA: BYDGOSZCZ
**Status:** ✅ SUKCES

### Faza 0: Stan Danych
- **Całkowita populacja w strefie miasta:** 403,938 (Baseline: 340,000) [✅ OK]
- **Ilość Transakcji RCN:** 11,410
- **Zakres Dat RCN:** 2020-01-02 do 2026-02-27
- **Ceny RCN (PLN/m²):** Średnia=5,143 | Mediana=4,420 | Max=498,399 | IQR=[2,757 - 5,873]
- **Infrastruktura OSM (Punkty):** 74,484
- **Infrastruktura OSM (Poligony/Budynki):** 121,570
- Baza transakcyjna `.gpkg` ustrukturyzowana poprawnie.

### Faza I & II: Pokrycie (Zero-Values)
- **Pustynia Populacyjna:** 199 (16.3%)
- **Pustynia Infrastrukturalna:** 0 (0.0%)
- **Głuche Przystanki:** 16 (1.3%)
- **Wskaźnik Fallback RCN:** 1150 (94.3%) (Mediana RCN dla miasta: 4378)

### Faza III: Udowodnione POI w Promieniu 500m

**Rzeczywiste TOP 20 zwalidowanych obiektów (Intersekcja bufor 500m):**

| Tag OSM | Zliczone (Ilość) | Prawdziwa Waga JSON | Całkowita Siła (Score) |
|---|---|---|---|
| `supermarket` | 1215 | 10,387,612.64 | **12,620,949,357.60** |
| `sports_centre` | 563 | 1,263,162.78 | **711,160,645.14** |
| `marketplace` | 116 | 1,402,944.47 | **162,741,558.52** |
| `place_of_worship` | 802 | 106,782.62 | **85,639,661.24** |
| `bank` | 1183 | 69,958.16 | **82,760,503.28** |
| `pharmacy` | 1295 | 63,846.57 | **82,681,308.15** |
| `post_office` | 475 | 79,416.01 | **37,722,604.75** |
| `bench` | 12306 | 0.00 | **0.00** |
| `parcel_locker` | 4930 | 0.00 | **0.00** |
| `restaurant` | 2699 | 0.00 | **0.00** |
| `waste_basket` | 1852 | 0.00 | **0.00** |
| `recycling` | 1752 | 0.00 | **0.00** |
| `atm` | 1548 | 0.00 | **0.00** |
| `bicycle_parking` | 2254 | 0.00 | **0.00** |
| `fast_food` | 1082 | 0.00 | **0.00** |
| `parking` | 38082 | 0.00 | **0.00** |
| `parking_entrance` | 822 | 0.00 | **0.00** |
| `cafe` | 812 | 0.00 | **0.00** |
| `vending_machine` | 711 | 0.00 | **0.00** |
| `charging_station` | 724 | 0.00 | **0.00** |

### Faza IV: Badanie Próbek Oceny Złotej

#### 🏆 TOP 5 (Najlepsze 5 przystanków w mieście)
<details><summary><b>Paszport Węzła: Szarych Szeregów (H3: 891f0b3762bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Szarych Szeregów
  stop_id             : 11087
  city                : bydgoszcz
  h3_index            : 891f0b3762bffff
  stop_lat            : 53.1070
  stop_lon            : 18.0458
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : bydgoszcz

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 1.7167

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 5345559.2550
  raw_gravity         : 4454632.7125
  domain_count        : 2
  infra_score_log     : 15.4918

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 59.6429
  hourly_freq         : 5.8571
  transit_freq_log    : 4.1050

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 4378.2837
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 1623
  pop_val_log         : 7.3926
```
</details>
<details><summary><b>Paszport Węzła: Szarych Szeregów (H3: 891f0b3762bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Szarych Szeregów
  stop_id             : 11012
  city                : bydgoszcz
  h3_index            : 891f0b3762bffff
  stop_lat            : 53.1083
  stop_lon            : 18.0449
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : bydgoszcz

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 1.7167

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 5345559.2550
  raw_gravity         : 4454632.7125
  domain_count        : 2
  infra_score_log     : 15.4918

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 59.6429
  hourly_freq         : 2.9286
  transit_freq_log    : 4.1050

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 4378.2837
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 1623
  pop_val_log         : 7.3926
```
</details>
<details><summary><b>Paszport Węzła: Szarych Szeregów (H3: 891f0b3762bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Szarych Szeregów
  stop_id             : 11086
  city                : bydgoszcz
  h3_index            : 891f0b3762bffff
  stop_lat            : 53.1077
  stop_lon            : 18.0438
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : bydgoszcz

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 1.7167

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 5345559.2550
  raw_gravity         : 4454632.7125
  domain_count        : 2
  infra_score_log     : 15.4918

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 59.6429
  hourly_freq         : 5.9286
  transit_freq_log    : 4.1050

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 4378.2837
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 1623
  pop_val_log         : 7.3926
```
</details>
<details><summary><b>Paszport Węzła: Szarych Szeregów (H3: 891f0b3762bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Szarych Szeregów
  stop_id             : 11084
  city                : bydgoszcz
  h3_index            : 891f0b3762bffff
  stop_lat            : 53.1079
  stop_lon            : 18.0436
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : bydgoszcz

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 1.7167

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 5345559.2550
  raw_gravity         : 4454632.7125
  domain_count        : 2
  infra_score_log     : 15.4918

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 59.6429
  hourly_freq         : 8.7857
  transit_freq_log    : 4.1050

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 4378.2837
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 1623
  pop_val_log         : 7.3926
```
</details>
<details><summary><b>Paszport Węzła: Szarych Szeregów (H3: 891f0b3762bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Szarych Szeregów
  stop_id             : 11085
  city                : bydgoszcz
  h3_index            : 891f0b3762bffff
  stop_lat            : 53.1078
  stop_lon            : 18.0438
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : bydgoszcz

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 1.7167

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 5345559.2550
  raw_gravity         : 4454632.7125
  domain_count        : 2
  infra_score_log     : 15.4918

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 59.6429
  hourly_freq         : 3.0714
  transit_freq_log    : 4.1050

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 4378.2837
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 1623
  pop_val_log         : 7.3926
```
</details>

#### 🎲 RANDOM 5 (Środkowe przystanki miasta)
<details><summary><b>Paszport Węzła: Kotomierz (H3: 891f0ba5337ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Kotomierz
  stop_id             : 16691
  city                : bydgoszcz
  h3_index            : 891f0ba5337ffff
  stop_lat            : 53.2844
  stop_lon            : 18.1208
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : pkp-ar

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : D
  local_percentile    : 39.4410
  local_score_raw     : -0.3642

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 834.0015
  raw_gravity         : 834.0015
  domain_count        : 0
  infra_score_log     : 6.7274

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 1.4286
  hourly_freq         : 0.7143
  transit_freq_log    : 0.8873

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 4378.2837
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 103
  pop_val_log         : 4.6444
```
</details>
<details><summary><b>Paszport Węzła: Przylesie (H3: 891f0b36627ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Przylesie
  stop_id             : 8092
  city                : bydgoszcz
  h3_index            : 891f0b36627ffff
  stop_lat            : 53.1462
  stop_lon            : 18.1245
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : bydgoszcz

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : B
  local_percentile    : 84.3168
  local_score_raw     : 0.8202

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 1300391.0171
  raw_gravity         : 1182173.6519
  domain_count        : 1
  infra_score_log     : 14.0782

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 23.8571
  hourly_freq         : 9.1429
  transit_freq_log    : 3.2131

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 4378.2837
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Fordońska - Wiadukt (H3: 891f0b36153ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Fordońska - Wiadukt
  stop_id             : 7035
  city                : bydgoszcz
  h3_index            : 891f0b36153ffff
  stop_lat            : 53.1470
  stop_lon            : 18.1661
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : bydgoszcz

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : C
  local_percentile    : 66.1491
  local_score_raw     : 0.2852

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 613.2377
  raw_gravity         : 613.2377
  domain_count        : 0
  infra_score_log     : 6.4204

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 13.7143
  hourly_freq         : 6.9286
  transit_freq_log    : 2.6888

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 4378.2837
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 280
  pop_val_log         : 5.6384
```
</details>
<details><summary><b>Paszport Węzła: Dobrcz - Urząd Gminy (H3: 891f0baed27ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Dobrcz - Urząd Gminy
  stop_id             : 13270
  city                : bydgoszcz
  h3_index            : 891f0baed27ffff
  stop_lat            : 53.2653
  stop_lon            : 18.1449
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : bydgoszcz

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : C
  local_percentile    : 52.7950
  local_score_raw     : -0.0406

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 144920.7208
  raw_gravity         : 120767.2674
  domain_count        : 2
  infra_score_log     : 11.8839

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.5000
  hourly_freq         : 0.2143
  transit_freq_log    : 0.4055

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 4378.2837
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 125
  pop_val_log         : 4.8363
```
</details>
<details><summary><b>Paszport Węzła: Łochowice - Nakielska - Zajęcza - Pętla (H3: 891f0b3348bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Łochowice - Nakielska - Zajęcza - Pętla
  stop_id             : 13215
  city                : bydgoszcz
  h3_index            : 891f0b3348bffff
  stop_lat            : 53.1287
  stop_lon            : 17.7953
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : bydgoszcz

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : D
  local_percentile    : 36.6460
  local_score_raw     : -0.4016

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 237.7420
  raw_gravity         : 237.7420
  domain_count        : 0
  infra_score_log     : 5.4754

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 2.7857
  hourly_freq         : 2.7857
  transit_freq_log    : 1.3312

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 4378.2837
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 31
  pop_val_log         : 3.4657
```
</details>

#### 💩 BOTTOM 5 (Najsłabsze 5 przystanków)
<details><summary><b>Paszport Węzła: Stronno - Dworcowa (H3: 891f0ba5283ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Stronno - Dworcowa
  stop_id             : 13325
  city                : bydgoszcz
  h3_index            : 891f0ba5283ffff
  stop_lat            : 53.2917
  stop_lon            : 18.0654
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : bydgoszcz

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.4658
  local_score_raw     : -1.3644

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 721.5050
  raw_gravity         : 721.5050
  domain_count        : 0
  infra_score_log     : 6.5827

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 1.0000
  hourly_freq         : 0.5000
  transit_freq_log    : 0.6931

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 1373.3407
  liquidity           : 4.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 74
  pop_val_log         : 4.3175
```
</details>
<details><summary><b>Paszport Węzła: Strzelce Górne - Szkolna (H3: 891f0bacd2fffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Strzelce Górne - Szkolna
  stop_id             : 13129
  city                : bydgoszcz
  h3_index            : 891f0bacd2fffff
  stop_lat            : 53.2113
  stop_lon            : 18.1591
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : bydgoszcz

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.3106
  local_score_raw     : -1.4682

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 522.7193
  raw_gravity         : 522.7193
  domain_count        : 0
  infra_score_log     : 6.2610

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 1.0714
  hourly_freq         : 0.7857
  transit_freq_log    : 0.7282

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 950.3897
  liquidity           : 3.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 143
  pop_val_log         : 4.9698
```
</details>
<details><summary><b>Paszport Węzła: Strzelce Górne - Gądecka (H3: 891f0bacd2fffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Strzelce Górne - Gądecka
  stop_id             : 13160
  city                : bydgoszcz
  h3_index            : 891f0bacd2fffff
  stop_lat            : 53.2121
  stop_lon            : 18.1567
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : bydgoszcz

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.3106
  local_score_raw     : -1.4682

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 522.7193
  raw_gravity         : 522.7193
  domain_count        : 0
  infra_score_log     : 6.2610

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 1.0714
  hourly_freq         : 0.2857
  transit_freq_log    : 0.7282

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 950.3897
  liquidity           : 3.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 143
  pop_val_log         : 4.9698
```
</details>
<details><summary><b>Paszport Węzła: Sienno - Jesionowa (H3: 891f0ba5e2fffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Sienno - Jesionowa
  stop_id             : 13278
  city                : bydgoszcz
  h3_index            : 891f0ba5e2fffff
  stop_lat            : 53.2797
  stop_lon            : 18.1584
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : bydgoszcz

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.1553
  local_score_raw     : -1.8602

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 205.3993
  raw_gravity         : 205.3993
  domain_count        : 0
  infra_score_log     : 5.3298

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.5000
  hourly_freq         : 0.2143
  transit_freq_log    : 0.4055

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 591.7452
  liquidity           : 2.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 34
  pop_val_log         : 3.5553
```
</details>
<details><summary><b>Paszport Węzła: Sienno - Jesionowa (H3: 891f0ba5e2fffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Sienno - Jesionowa
  stop_id             : 13279
  city                : bydgoszcz
  h3_index            : 891f0ba5e2fffff
  stop_lat            : 53.2801
  stop_lon            : 18.1581
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : bydgoszcz

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.1553
  local_score_raw     : -1.8602

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 205.3993
  raw_gravity         : 205.3993
  domain_count        : 0
  infra_score_log     : 5.3298

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.5000
  hourly_freq         : 0.2857
  transit_freq_log    : 0.4055

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 591.7452
  liquidity           : 2.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 34
  pop_val_log         : 3.5553
```
</details>

---

## AGLOMERACJA: CZESTOCHOWA
**Status:** ✅ SUKCES

### Faza 0: Stan Danych
- **Całkowita populacja w strefie miasta:** 240,937 (Baseline: 210,000) [✅ OK]
- **Ilość Transakcji RCN:** 10,835
- **Zakres Dat RCN:** 2020-07-10 do 2026-02-24
- **Ceny RCN (PLN/m²):** Średnia=7,495 | Mediana=5,747 | Max=466,786 | IQR=[4,345 - 7,000]
- **Infrastruktura OSM (Punkty):** 51,277
- **Infrastruktura OSM (Poligony/Budynki):** 81,877
- Baza transakcyjna `.gpkg` ustrukturyzowana poprawnie.

### Faza I & II: Pokrycie (Zero-Values)
- **Pustynia Populacyjna:** 72 (8.0%)
- **Pustynia Infrastrukturalna:** 1 (0.1%)
- **Głuche Przystanki:** 13 (1.4%)
- **Wskaźnik Fallback RCN:** 560 (62.3%) (Mediana RCN dla miasta: 5690)

### Faza III: Udowodnione POI w Promieniu 500m

**Rzeczywiste TOP 20 zwalidowanych obiektów (Intersekcja bufor 500m):**

| Tag OSM | Zliczone (Ilość) | Prawdziwa Waga JSON | Całkowita Siła (Score) |
|---|---|---|---|
| `supermarket` | 721 | 9,860,359.49 | **7,109,319,192.29** |
| `sports_centre` | 214 | 1,310,642.96 | **280,477,593.44** |
| `marketplace` | 140 | 1,296,084.41 | **181,451,817.40** |
| `place_of_worship` | 713 | 96,142.45 | **68,549,566.85** |
| `pharmacy` | 1130 | 59,184.16 | **66,878,100.80** |
| `bank` | 525 | 67,259.95 | **35,311,473.75** |
| `post_office` | 315 | 67,399.91 | **21,230,971.65** |
| `bench` | 12109 | 0.00 | **0.00** |
| `bicycle_parking` | 4145 | 0.00 | **0.00** |
| `waste_basket` | 3427 | 0.00 | **0.00** |
| `restaurant` | 1495 | 0.00 | **0.00** |
| `recycling` | 1178 | 0.00 | **0.00** |
| `atm` | 1088 | 0.00 | **0.00** |
| `parcel_locker` | 927 | 0.00 | **0.00** |
| `parking_space` | 2946 | 0.00 | **0.00** |
| `parking` | 18688 | 0.00 | **0.00** |
| `shelter` | 1916 | 0.00 | **0.00** |
| `vending_machine` | 609 | 0.00 | **0.00** |
| `fast_food` | 721 | 0.00 | **0.00** |
| `taxi` | 595 | 0.00 | **0.00** |

### Faza IV: Badanie Próbek Oceny Złotej

#### 🏆 TOP 5 (Najlepsze 5 przystanków w mieście)
<details><summary><b>Paszport Węzła: Dworzec PKS (H3: 891e23a6b0bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Dworzec PKS
  stop_id             : 25
  city                : czestochowa
  h3_index            : 891e23a6b0bffff
  stop_lat            : 50.8056
  stop_lon            : 19.1169
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : czestochowa

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 4.1581

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 34635.1269
  raw_gravity         : 31486.4790
  domain_count        : 1.0000
  infra_score_log     : 10.4527

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 49.3571
  hourly_freq         : 11.1429
  transit_freq_log    : 3.9191

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 47665.3956
  liquidity           : 15.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 421
  pop_val_log         : 6.0450
```
</details>
<details><summary><b>Paszport Węzła: Dworzec PKS (H3: 891e23a6b0bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Dworzec PKS
  stop_id             : 54
  city                : czestochowa
  h3_index            : 891e23a6b0bffff
  stop_lat            : 50.8058
  stop_lon            : 19.1182
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : czestochowa

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 4.1581

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 34635.1269
  raw_gravity         : 31486.4790
  domain_count        : 1.0000
  infra_score_log     : 10.4527

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 49.3571
  hourly_freq         : 9.0000
  transit_freq_log    : 3.9191

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 47665.3956
  liquidity           : 15.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 421
  pop_val_log         : 6.0450
```
</details>
<details><summary><b>Paszport Węzła: Dworzec PKS (H3: 891e23a6b0bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Dworzec PKS
  stop_id             : 53
  city                : czestochowa
  h3_index            : 891e23a6b0bffff
  stop_lat            : 50.8059
  stop_lon            : 19.1184
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : czestochowa

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 4.1581

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 34635.1269
  raw_gravity         : 31486.4790
  domain_count        : 1.0000
  infra_score_log     : 10.4527

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 49.3571
  hourly_freq         : 8.8571
  transit_freq_log    : 3.9191

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 47665.3956
  liquidity           : 15.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 421
  pop_val_log         : 6.0450
```
</details>
<details><summary><b>Paszport Węzła: Dworzec PKS (H3: 891e23a6b0bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Dworzec PKS
  stop_id             : 935
  city                : czestochowa
  h3_index            : 891e23a6b0bffff
  stop_lat            : 50.8059
  stop_lon            : 19.1182
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : czestochowa

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 4.1581

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 34635.1269
  raw_gravity         : 31486.4790
  domain_count        : 1.0000
  infra_score_log     : 10.4527

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 49.3571
  hourly_freq         : 14.1429
  transit_freq_log    : 3.9191

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 47665.3956
  liquidity           : 15.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 421
  pop_val_log         : 6.0450
```
</details>
<details><summary><b>Paszport Węzła: Dworzec PKS (H3: 891e23a6b0bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Dworzec PKS
  stop_id             : 202
  city                : czestochowa
  h3_index            : 891e23a6b0bffff
  stop_lat            : 50.8051
  stop_lon            : 19.1178
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : czestochowa

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 4.1581

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 34635.1269
  raw_gravity         : 31486.4790
  domain_count        : 1.0000
  infra_score_log     : 10.4527

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 49.3571
  hourly_freq         : 6.2143
  transit_freq_log    : 3.9191

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 47665.3956
  liquidity           : 15.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 421
  pop_val_log         : 6.0450
```
</details>

#### 🎲 RANDOM 5 (Środkowe przystanki miasta)
<details><summary><b>Paszport Węzła: Stradom - Dworzec PKP (H3: 891e23a4c87ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Stradom - Dworzec PKP
  stop_id             : 199
  city                : czestochowa
  h3_index            : 891e23a4c87ffff
  stop_lat            : 50.7978
  stop_lon            : 19.1077
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : czestochowa

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : C
  local_percentile    : 65.7505
  local_score_raw     : 0.2008

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 30610.5123
  raw_gravity         : 27827.7384
  domain_count        : 1.0000
  infra_score_log     : 10.3291

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 11.9286
  hourly_freq         : 3.9286
  transit_freq_log    : 2.5594

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 5689.9050
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Grabówka (H3: 891e23a612bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Grabówka
  stop_id             : 235
  city                : czestochowa
  h3_index            : 891e23a612bffff
  stop_lat            : 50.8363
  stop_lon            : 19.0614
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : czestochowa

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : B
  local_percentile    : 80.7611
  local_score_raw     : 0.6311

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 108725.7853
  raw_gravity         : 98841.6230
  domain_count        : 1.0000
  infra_score_log     : 11.5966

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 11.2857
  hourly_freq         : 3.0000
  transit_freq_log    : 2.5084

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 5689.9050
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 71
  pop_val_log         : 4.2767
```
</details>
<details><summary><b>Paszport Węzła: Żabiniec (H3: 891e216920bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Żabiniec
  stop_id             : 640
  city                : czestochowa
  h3_index            : 891e216920bffff
  stop_lat            : 50.8576
  stop_lon            : 19.0660
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : czestochowa

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : D
  local_percentile    : 31.2896
  local_score_raw     : -0.4060

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 400.8239
  raw_gravity         : 400.8239
  domain_count        : 0.0000
  infra_score_log     : 5.9960

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 3.1429
  hourly_freq         : 3.1429
  transit_freq_log    : 1.4214

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 5689.9050
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 41
  pop_val_log         : 3.7377
```
</details>
<details><summary><b>Paszport Węzła: Fieldorfa - NILA (H3: 891e23a6d2bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Fieldorfa - NILA
  stop_id             : 215
  city                : czestochowa
  h3_index            : 891e23a6d2bffff
  stop_lat            : 50.8392
  stop_lon            : 19.1325
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : czestochowa

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : B
  local_percentile    : 79.4926
  local_score_raw     : 0.6008

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 107762.5420
  raw_gravity         : 97965.9473
  domain_count        : 1.0000
  infra_score_log     : 11.5877

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 6.4286
  hourly_freq         : 6.4286
  transit_freq_log    : 2.0053

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 5661.6092
  liquidity           : 20.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 748
  pop_val_log         : 6.6187
```
</details>
<details><summary><b>Paszport Węzła: Rolnicza - Cmentarz KULE (H3: 891e23a69cfffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Rolnicza - Cmentarz KULE
  stop_id             : 519
  city                : czestochowa
  h3_index            : 891e23a69cfffff
  stop_lat            : 50.8263
  stop_lon            : 19.1299
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : czestochowa

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : D
  local_percentile    : 38.4778
  local_score_raw     : -0.3279

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 365.8289
  raw_gravity         : 365.8289
  domain_count        : 0.0000
  infra_score_log     : 5.9049

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 5.2857
  hourly_freq         : 2.6429
  transit_freq_log    : 1.8383

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 5689.9050
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 13
  pop_val_log         : 2.6391
```
</details>

#### 💩 BOTTOM 5 (Najsłabsze 5 przystanków)
<details><summary><b>Paszport Węzła: Blachownia - Szkoła (H3: 891e23a736bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Blachownia - Szkoła
  stop_id             : 1594
  city                : czestochowa
  h3_index            : 891e23a736bffff
  stop_lat            : 50.7788
  stop_lon            : 18.9621
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : czestochowa

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 1.0571
  local_score_raw     : -1.3050

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 46.2452
  raw_gravity         : 46.2452
  domain_count        : 0.0000
  infra_score_log     : 3.8554

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 1.0714
  hourly_freq         : 1.0714
  transit_freq_log    : 0.7282

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 3986.9147
  liquidity           : 9.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Rząsawa (H3: 891e2169dd3ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Rząsawa
  stop_id             : 63123
  city                : czestochowa
  h3_index            : 891e2169dd3ffff
  stop_lat            : 50.8856
  stop_lon            : 19.1780
  lat_grid            : 50.8900
  lon_grid            : 19.1800
  norm_name           : rzasawa
  source              : polish_trains

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.8457
  local_score_raw     : -1.3669

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 156.5673
  raw_gravity         : 156.5673
  domain_count        : 0.0000
  infra_score_log     : 5.0599

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.0000
  hourly_freq         : 0.0000
  transit_freq_log    : 0.0000

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 5689.9050
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Przeprośna Górka (H3: 891e2ed31b3ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Przeprośna Górka
  stop_id             : 1258
  city                : czestochowa
  h3_index            : 891e2ed31b3ffff
  stop_lat            : 50.8175
  stop_lon            : 19.2355
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : czestochowa

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.6342
  local_score_raw     : -1.3784

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 16.5932
  raw_gravity         : 16.5932
  domain_count        : 0.0000
  infra_score_log     : 2.8675

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.6429
  hourly_freq         : 0.6429
  transit_freq_log    : 0.4964

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 5689.9050
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Rząsawa - Dworzec PKP (H3: 891e2169ddbffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Rząsawa - Dworzec PKP
  stop_id             : 534
  city                : czestochowa
  h3_index            : 891e2169ddbffff
  stop_lat            : 50.8828
  stop_lon            : 19.1757
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : czestochowa

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.4228
  local_score_raw     : -1.4088

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 4.6729
  raw_gravity         : 4.6729
  domain_count        : 0.0000
  infra_score_log     : 1.7357

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 1.0000
  hourly_freq         : 1.0000
  transit_freq_log    : 0.6931

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 5689.9050
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Przeprośna Górka (H3: 891e2ed224fffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Przeprośna Górka
  stop_id             : 1259
  city                : czestochowa
  h3_index            : 891e2ed224fffff
  stop_lat            : 50.8175
  stop_lon            : 19.2363
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : czestochowa

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.2114
  local_score_raw     : -1.6599

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 0.0000
  raw_gravity         : 0.0000
  domain_count        : 0.0000
  infra_score_log     : 0.0000

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.6429
  hourly_freq         : 0.6429
  transit_freq_log    : 0.4964

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 5689.9050
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>

---

## AGLOMERACJA: ELBLAG
**Status:** ✅ SUKCES

### Faza 0: Stan Danych
- **Całkowita populacja w strefie miasta:** 119,411 (Baseline: 110,000) [✅ OK]
- **Ilość Transakcji RCN:** 5,907
- **Zakres Dat RCN:** 2020-08-20 do 2026-03-02
- **Ceny RCN (PLN/m²):** Średnia=7,083 | Mediana=6,550 | Max=187,972 | IQR=[5,060 - 7,735]
- **Infrastruktura OSM (Punkty):** 15,961
- **Infrastruktura OSM (Poligony/Budynki):** 35,383
- Baza transakcyjna `.gpkg` ustrukturyzowana poprawnie.

### Faza I & II: Pokrycie (Zero-Values)
- **Pustynia Populacyjna:** 43 (12.3%)
- **Pustynia Infrastrukturalna:** 0 (0.0%)
- **Głuche Przystanki:** 0 (0.0%)
- **Wskaźnik Fallback RCN:** 129 (37.0%) (Mediana RCN dla miasta: 6478)

### Faza III: Udowodnione POI w Promieniu 500m

**Rzeczywiste TOP 20 zwalidowanych obiektów (Intersekcja bufor 500m):**

| Tag OSM | Zliczone (Ilość) | Prawdziwa Waga JSON | Całkowita Siła (Score) |
|---|---|---|---|
| `supermarket` | 634 | 8,584,735.02 | **5,442,722,002.68** |
| `marketplace` | 85 | 1,126,502.42 | **95,752,705.70** |
| `sports_centre` | 34 | 1,347,359.29 | **45,810,215.86** |
| `bank` | 657 | 60,594.23 | **39,810,409.11** |
| `place_of_worship` | 347 | 93,356.27 | **32,394,625.69** |
| `pharmacy` | 439 | 56,564.34 | **24,831,745.26** |
| `post_office` | 235 | 69,662.60 | **16,370,711.00** |
| `bench` | 7051 | 0.00 | **0.00** |
| `waste_basket` | 2101 | 0.00 | **0.00** |
| `parcel_locker` | 839 | 0.00 | **0.00** |
| `bicycle_parking` | 670 | 0.00 | **0.00** |
| `restaurant` | 640 | 0.00 | **0.00** |
| `atm` | 436 | 0.00 | **0.00** |
| `charging_station` | 383 | 0.00 | **0.00** |
| `parking_entrance` | 324 | 0.00 | **0.00** |
| `vending_machine` | 268 | 0.00 | **0.00** |
| `doctors` | 362 | 0.00 | **0.00** |
| `fast_food` | 361 | 0.00 | **0.00** |
| `dentist` | 182 | 0.00 | **0.00** |
| `recycling` | 153 | 0.00 | **0.00** |

### Faza IV: Badanie Próbek Oceny Złotej

#### 🏆 TOP 5 (Najlepsze 5 przystanków w mieście)
<details><summary><b>Paszport Węzła: Nad Jarem (H3: 891f54d0d03ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Nad Jarem
  stop_id             : 166
  city                : elblag
  h3_index            : 891f54d0d03ffff
  stop_lat            : 54.1876
  stop_lon            : 19.4279
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : elblag

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 1.7158

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 7611690.8738
  raw_gravity         : 6919718.9762
  domain_count        : 1
  infra_score_log     : 15.8452

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 37.1429
  hourly_freq         : 20.4286
  transit_freq_log    : 3.6413

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 8995.6616
  liquidity           : 31.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 395
  pop_val_log         : 5.9814
```
</details>
<details><summary><b>Paszport Węzła: Ogólna - Pętla (H3: 891f54d0d03ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Ogólna - Pętla
  stop_id             : 167
  city                : elblag
  h3_index            : 891f54d0d03ffff
  stop_lat            : 54.1872
  stop_lon            : 19.4277
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : elblag

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 1.7158

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 7611690.8738
  raw_gravity         : 6919718.9762
  domain_count        : 1
  infra_score_log     : 15.8452

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 37.1429
  hourly_freq         : 4.9286
  transit_freq_log    : 3.6413

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 8995.6616
  liquidity           : 31.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 395
  pop_val_log         : 5.9814
```
</details>
<details><summary><b>Paszport Węzła: Nad Jarem (H3: 891f54d0d03ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Nad Jarem
  stop_id             : 280
  city                : elblag
  h3_index            : 891f54d0d03ffff
  stop_lat            : 54.1878
  stop_lon            : 19.4271
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : elblag

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 1.7158

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 7611690.8738
  raw_gravity         : 6919718.9762
  domain_count        : 1
  infra_score_log     : 15.8452

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 37.1429
  hourly_freq         : 11.7857
  transit_freq_log    : 3.6413

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 8995.6616
  liquidity           : 31.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 395
  pop_val_log         : 5.9814
```
</details>
<details><summary><b>Paszport Węzła: Płk. Dąbka - Os. Na Stoku (H3: 891f54d08c7ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Płk. Dąbka - Os. Na Stoku
  stop_id             : 85
  city                : elblag
  h3_index            : 891f54d08c7ffff
  stop_lat            : 54.1735
  stop_lon            : 19.4050
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : elblag

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 99.4048
  local_score_raw     : 1.3407

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 14614071.4482
  raw_gravity         : 13285519.4983
  domain_count        : 1
  infra_score_log     : 16.4975

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 19.5000
  hourly_freq         : 9.7143
  transit_freq_log    : 3.0204

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 5974.6797
  liquidity           : 54.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 2861
  pop_val_log         : 7.9593
```
</details>
<details><summary><b>Paszport Węzła: Płk. Dąbka - Os. Na Stoku (H3: 891f54d08c7ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Płk. Dąbka - Os. Na Stoku
  stop_id             : 84
  city                : elblag
  h3_index            : 891f54d08c7ffff
  stop_lat            : 54.1725
  stop_lon            : 19.4044
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : elblag

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 99.4048
  local_score_raw     : 1.3407

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 14614071.4482
  raw_gravity         : 13285519.4983
  domain_count        : 1
  infra_score_log     : 16.4975

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 19.5000
  hourly_freq         : 9.7857
  transit_freq_log    : 3.0204

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 5974.6797
  liquidity           : 54.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 2861
  pop_val_log         : 7.9593
```
</details>

#### 🎲 RANDOM 5 (Środkowe przystanki miasta)
<details><summary><b>Paszport Węzła: Królewiecka - Szpital (H3: 891f54d0d6bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Królewiecka - Szpital
  stop_id             : 624
  city                : elblag
  h3_index            : 891f54d0d6bffff
  stop_lat            : 54.1780
  stop_lon            : 19.4264
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : elblag

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : B
  local_percentile    : 77.3810
  local_score_raw     : 0.6736

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 39600.1669
  raw_gravity         : 36000.1518
  domain_count        : 1
  infra_score_log     : 10.5866

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 13.9286
  hourly_freq         : 2.4286
  transit_freq_log    : 2.7033

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6652.8067
  liquidity           : 5.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 558
  pop_val_log         : 6.3261
```
</details>
<details><summary><b>Paszport Węzła: Zakłady Meblowe (H3: 891f54d0c83ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Zakłady Meblowe
  stop_id             : 50
  city                : elblag
  h3_index            : 891f54d0c83ffff
  stop_lat            : 54.1954
  stop_lon            : 19.3884
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : elblag

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : D
  local_percentile    : 38.6905
  local_score_raw     : -0.3892

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 264.4104
  raw_gravity         : 264.4104
  domain_count        : 0
  infra_score_log     : 5.5813

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 4.2857
  hourly_freq         : 2.0714
  transit_freq_log    : 1.6650

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6477.9572
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 23
  pop_val_log         : 3.1781
```
</details>
<details><summary><b>Paszport Węzła: Królewiecka - Zespół Szkół Gospodarczych (H3: 891f54d0807ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Królewiecka - Zespół Szkół Gospodarczych
  stop_id             : 445
  city                : elblag
  h3_index            : 891f54d0807ffff
  stop_lat            : 54.1718
  stop_lon            : 19.4135
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : elblag

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : C
  local_percentile    : 63.6905
  local_score_raw     : 0.2941

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 1165.4545
  raw_gravity         : 1165.4545
  domain_count        : 0
  infra_score_log     : 7.0617

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 13.7857
  hourly_freq         : 2.4286
  transit_freq_log    : 2.6937

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6058.2469
  liquidity           : 20.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 406
  pop_val_log         : 6.0088
```
</details>
<details><summary><b>Paszport Węzła: Dębica I (H3: 891f54d5683ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Dębica I
  stop_id             : 614
  city                : elblag
  h3_index            : 891f54d5683ffff
  stop_lat            : 54.1620
  stop_lon            : 19.4631
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : elblag

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : D
  local_percentile    : 30.3571
  local_score_raw     : -0.5425

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 274.5121
  raw_gravity         : 274.5121
  domain_count        : 0
  infra_score_log     : 5.6186

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 4.7143
  hourly_freq         : 2.3571
  transit_freq_log    : 1.7430

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6477.9572
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Malborska - Piekarnia (H3: 891f54d0a2bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Malborska - Piekarnia
  stop_id             : 109
  city                : elblag
  h3_index            : 891f54d0a2bffff
  stop_lat            : 54.1501
  stop_lon            : 19.4030
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : elblag

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : C
  local_percentile    : 69.6429
  local_score_raw     : 0.3971

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 547.5425
  raw_gravity         : 547.5425
  domain_count        : 0
  infra_score_log     : 6.3073

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 8.7143
  hourly_freq         : 4.3571
  transit_freq_log    : 2.2736

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 9260.1068
  liquidity           : 48.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 744
  pop_val_log         : 6.6134
```
</details>

#### 💩 BOTTOM 5 (Najsłabsze 5 przystanków)
<details><summary><b>Paszport Węzła: ROD "Jagiellończyka" - Komunialnik (H3: 891f54d0da7ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : ROD "Jagiellończyka" - Komunialnik
  stop_id             : 329
  city                : elblag
  h3_index            : 891f54d0da7ffff
  stop_lat            : 54.1920
  stop_lon            : 19.4455
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : elblag

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 2.3810
  local_score_raw     : -1.1617

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 38.1096
  raw_gravity         : 38.1096
  domain_count        : 0
  infra_score_log     : 3.6664

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.9286
  hourly_freq         : 0.9286
  transit_freq_log    : 0.6568

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6477.9572
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: ROD "Jagiellończyka" (H3: 891f54d0dafffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : ROD "Jagiellończyka"
  stop_id             : 312
  city                : elblag
  h3_index            : 891f54d0dafffff
  stop_lat            : 54.1916
  stop_lon            : 19.4416
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : elblag

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 1.7857
  local_score_raw     : -1.1732

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 33.1556
  raw_gravity         : 33.1556
  domain_count        : 0
  infra_score_log     : 3.5309

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.9286
  hourly_freq         : 0.9286
  transit_freq_log    : 0.6568

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6477.9572
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: ZUO (H3: 891f54d2bdbffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : ZUO
  stop_id             : 532
  city                : elblag
  h3_index            : 891f54d2bdbffff
  stop_lat            : 54.2071
  stop_lon            : 19.3934
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : elblag

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 1.1905
  local_score_raw     : -1.1885

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 159.1044
  raw_gravity         : 159.1044
  domain_count        : 0
  infra_score_log     : 5.0758

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.3571
  hourly_freq         : 0.2143
  transit_freq_log    : 0.3054

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6477.9572
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: ZUO (H3: 891f54d2bdbffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : ZUO
  stop_id             : 533
  city                : elblag
  h3_index            : 891f54d2bdbffff
  stop_lat            : 54.2071
  stop_lon            : 19.3934
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : elblag

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 1.1905
  local_score_raw     : -1.1885

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 159.1044
  raw_gravity         : 159.1044
  domain_count        : 0
  infra_score_log     : 5.0758

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.3571
  hourly_freq         : 0.1429
  transit_freq_log    : 0.3054

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6477.9572
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: ROD "Skowronek I" (H3: 891f54d72dbffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : ROD "Skowronek I"
  stop_id             : 314
  city                : elblag
  h3_index            : 891f54d72dbffff
  stop_lat            : 54.1912
  stop_lon            : 19.4501
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : elblag

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.5952
  local_score_raw     : -1.2072

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 26.5597
  raw_gravity         : 26.5597
  domain_count        : 0
  infra_score_log     : 3.3164

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.8571
  hourly_freq         : 0.8571
  transit_freq_log    : 0.6190

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6477.9572
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>

---

## AGLOMERACJA: ELK
**Status:** ✅ SUKCES

### Faza 0: Stan Danych
- **Całkowita populacja w strefie miasta:** 72,490 (Baseline: 60,000) [✅ OK]
- **Ilość Transakcji RCN:** 3,570
- **Zakres Dat RCN:** 2021-01-12 do 2026-03-02
- **Ceny RCN (PLN/m²):** Średnia=7,253 | Mediana=4,953 | Max=207,602 | IQR=[2,353 - 6,703]
- **Infrastruktura OSM (Punkty):** 33,169
- **Infrastruktura OSM (Poligony/Budynki):** 27,453
- Baza transakcyjna `.gpkg` ustrukturyzowana poprawnie.

### Faza I & II: Pokrycie (Zero-Values)
- **Pustynia Populacyjna:** 63 (19.7%)
- **Pustynia Infrastrukturalna:** 1 (0.3%)
- **Głuche Przystanki:** 19 (5.9%)
- **Wskaźnik Fallback RCN:** 221 (69.1%) (Mediana RCN dla miasta: 4880)

### Faza III: Udowodnione POI w Promieniu 500m

**Rzeczywiste TOP 20 zwalidowanych obiektów (Intersekcja bufor 500m):**

| Tag OSM | Zliczone (Ilość) | Prawdziwa Waga JSON | Całkowita Siła (Score) |
|---|---|---|---|
| `supermarket` | 257 | 9,981,363.19 | **2,565,210,339.83** |
| `sports_centre` | 183 | 1,030,842.67 | **188,644,208.61** |
| `marketplace` | 25 | 1,267,537.56 | **31,688,439.00** |
| `bank` | 309 | 54,380.75 | **16,803,651.75** |
| `place_of_worship` | 209 | 80,279.59 | **16,778,434.31** |
| `pharmacy` | 199 | 54,874.10 | **10,919,945.90** |
| `post_office` | 136 | 60,042.77 | **8,165,816.72** |
| `bench` | 6764 | 0.00 | **0.00** |
| `waste_basket` | 2314 | 0.00 | **0.00** |
| `bicycle_parking` | 1582 | 0.00 | **0.00** |
| `restaurant` | 435 | 0.00 | **0.00** |
| `parcel_locker` | 353 | 0.00 | **0.00** |
| `doctors` | 357 | 0.00 | **0.00** |
| `school` | 492 | 0.00 | **0.00** |
| `atm` | 235 | 0.00 | **0.00** |
| `dentist` | 211 | 0.00 | **0.00** |
| `fast_food` | 213 | 0.00 | **0.00** |
| `kindergarten` | 234 | 0.00 | **0.00** |
| `post_box` | 110 | 0.00 | **0.00** |
| `parking_entrance` | 106 | 0.00 | **0.00** |

### Faza IV: Badanie Próbek Oceny Złotej

#### 🏆 TOP 5 (Najlepsze 5 przystanków w mieście)
<details><summary><b>Paszport Węzła: Wojska Polskiego — Park (H3: 891f5538c6fffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Wojska Polskiego — Park
  stop_id             : 9
  city                : elk
  h3_index            : 891f5538c6fffff
  stop_lat            : 53.8185
  stop_lon            : 22.3529
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : elk

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 2.5227

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 7041248.5952
  raw_gravity         : 5867707.1626
  domain_count        : 2.0000
  infra_score_log     : 15.7673

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 13.8571
  hourly_freq         : 6.9286
  transit_freq_log    : 2.6985

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 8293.2748
  liquidity           : 4.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 838
  pop_val_log         : 6.7322
```
</details>
<details><summary><b>Paszport Węzła: Wojska Polskiego — Most (H3: 891f5538c6fffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Wojska Polskiego — Most
  stop_id             : 26
  city                : elk
  h3_index            : 891f5538c6fffff
  stop_lat            : 53.8187
  stop_lon            : 22.3531
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : elk

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 2.5227

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 7041248.5952
  raw_gravity         : 5867707.1626
  domain_count        : 2.0000
  infra_score_log     : 15.7673

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 13.8571
  hourly_freq         : 6.9286
  transit_freq_log    : 2.6985

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 8293.2748
  liquidity           : 4.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 838
  pop_val_log         : 6.7322
```
</details>
<details><summary><b>Paszport Węzła: Jeziorna — Pętla (H3: 891f5538ab3ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Jeziorna — Pętla
  stop_id             : 20
  city                : elk
  h3_index            : 891f5538ab3ffff
  stop_lat            : 53.7996
  stop_lon            : 22.3530
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : elk

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 99.5146
  local_score_raw     : 2.3458

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 281092.6480
  raw_gravity         : 234243.8733
  domain_count        : 2.0000
  infra_score_log     : 12.5464

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 20.0000
  hourly_freq         : 6.6429
  transit_freq_log    : 3.0445

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 7823.8027
  liquidity           : 62.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 1755
  pop_val_log         : 7.4708
```
</details>
<details><summary><b>Paszport Węzła: Jana Pawła Ⅱ — Kolbego (H3: 891f5538ab3ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Jana Pawła Ⅱ — Kolbego
  stop_id             : 15
  city                : elk
  h3_index            : 891f5538ab3ffff
  stop_lat            : 53.8002
  stop_lon            : 22.3550
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : elk

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 99.5146
  local_score_raw     : 2.3458

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 281092.6480
  raw_gravity         : 234243.8733
  domain_count        : 2.0000
  infra_score_log     : 12.5464

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 20.0000
  hourly_freq         : 6.7143
  transit_freq_log    : 3.0445

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 7823.8027
  liquidity           : 62.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 1755
  pop_val_log         : 7.4708
```
</details>
<details><summary><b>Paszport Węzła: Jana Pawła Ⅱ — Skwer Foksa (H3: 891f5538ab3ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Jana Pawła Ⅱ — Skwer Foksa
  stop_id             : 21
  city                : elk
  h3_index            : 891f5538ab3ffff
  stop_lat            : 53.8007
  stop_lon            : 22.3564
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : elk

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 99.5146
  local_score_raw     : 2.3458

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 281092.6480
  raw_gravity         : 234243.8733
  domain_count        : 2.0000
  infra_score_log     : 12.5464

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 20.0000
  hourly_freq         : 6.6429
  transit_freq_log    : 3.0445

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 7823.8027
  liquidity           : 62.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 1755
  pop_val_log         : 7.4708
```
</details>

#### 🎲 RANDOM 5 (Środkowe przystanki miasta)
<details><summary><b>Paszport Węzła: Siedliska — Przejazd (H3: 891f55381a7ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Siedliska — Przejazd
  stop_id             : 91
  city                : elk
  h3_index            : 891f55381a7ffff
  stop_lat            : 53.8335
  stop_lon            : 22.3283
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : elk

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : B
  local_percentile    : 72.3301
  local_score_raw     : 0.2627

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 711.7271
  raw_gravity         : 711.7271
  domain_count        : 0.0000
  infra_score_log     : 6.5691

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 3.4286
  hourly_freq         : 0.5000
  transit_freq_log    : 1.4881

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 4879.9143
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 19
  pop_val_log         : 2.9957
```
</details>
<details><summary><b>Paszport Węzła: Chrzanowo (H3: 891f55384bbffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Chrzanowo
  stop_id             : 226
  city                : elk
  h3_index            : 891f55384bbffff
  stop_lat            : 53.8501
  stop_lon            : 22.2630
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : elk

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : D
  local_percentile    : 44.6602
  local_score_raw     : -0.3520

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 97.2583
  raw_gravity         : 97.2583
  domain_count        : 0.0000
  infra_score_log     : 4.5876

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 1.1429
  hourly_freq         : 0.5714
  transit_freq_log    : 0.7621

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 4879.9143
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 4
  pop_val_log         : 1.6094
```
</details>
<details><summary><b>Paszport Węzła: Juranda (H3: 891f5538eabffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Juranda
  stop_id             : 147
  city                : elk
  h3_index            : 891f5538eabffff
  stop_lat            : 53.8128
  stop_lon            : 22.3367
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : elk

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : C
  local_percentile    : 62.6214
  local_score_raw     : -0.1131

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 426.7998
  raw_gravity         : 426.7998
  domain_count        : 0.0000
  infra_score_log     : 6.0587

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.6429
  hourly_freq         : 0.2857
  transit_freq_log    : 0.4964

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 4879.9143
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 158
  pop_val_log         : 5.0689
```
</details>
<details><summary><b>Paszport Węzła: Ełk Szyba Wschód (H3: 891f553886fffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Ełk Szyba Wschód
  stop_id             : 12237
  city                : elk
  h3_index            : 891f553886fffff
  stop_lat            : 53.8011
  stop_lon            : 22.3729
  lat_grid            : 53.8000
  lon_grid            : 22.3700
  norm_name           : ekszybawschod
  source              : polish_trains

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : D
  local_percentile    : 41.7476
  local_score_raw     : -0.3654

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 519.0293
  raw_gravity         : 519.0293
  domain_count        : 0.0000
  infra_score_log     : 6.2539

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.0000
  hourly_freq         : 0.0000
  transit_freq_log    : 0.0000

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 4506.7601
  liquidity           : 157.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 230
  pop_val_log         : 5.4424
```
</details>
<details><summary><b>Paszport Węzła: Bartosze Ⅱ (H3: 891f553800bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Bartosze Ⅱ
  stop_id             : 200
  city                : elk
  h3_index            : 891f553800bffff
  stop_lat            : 53.8268
  stop_lon            : 22.2738
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : elk

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : C
  local_percentile    : 52.4272
  local_score_raw     : -0.2777

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 320.5096
  raw_gravity         : 320.5096
  domain_count        : 0.0000
  infra_score_log     : 5.7730

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.5714
  hourly_freq         : 0.2857
  transit_freq_log    : 0.4520

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 4879.9143
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 25
  pop_val_log         : 3.2581
```
</details>

#### 💩 BOTTOM 5 (Najsłabsze 5 przystanków)
<details><summary><b>Paszport Węzła: Buczki (H3: 891f5523043ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Buczki
  stop_id             : 253
  city                : elk
  h3_index            : 891f5523043ffff
  stop_lat            : 53.8385
  stop_lon            : 22.4308
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : elk

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 2.4272
  local_score_raw     : -0.9146

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 31.6617
  raw_gravity         : 31.6617
  domain_count        : 0.0000
  infra_score_log     : 3.4862

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.0000
  hourly_freq         : 0.0000
  transit_freq_log    : 0.0000

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 4879.9143
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Mrozy Wielkie n/ż (H3: 891f5538ba3ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Mrozy Wielkie n/ż
  stop_id             : 323-02
  city                : elk
  h3_index            : 891f5538ba3ffff
  stop_lat            : 53.7984
  stop_lon            : 22.3961
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : elk

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 1.9417
  local_score_raw     : -0.9158

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 4.6001
  raw_gravity         : 4.6001
  domain_count        : 0.0000
  infra_score_log     : 1.7228

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.4286
  hourly_freq         : 0.4286
  transit_freq_log    : 0.3567

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 4879.9143
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Janisze — Zalesie (H3: 891f553115bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Janisze — Zalesie
  stop_id             : 277
  city                : elk
  h3_index            : 891f553115bffff
  stop_lat            : 53.9067
  stop_lon            : 22.3584
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : elk

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 1.4563
  local_score_raw     : -0.9690

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 8.5521
  raw_gravity         : 8.5521
  domain_count        : 0.0000
  infra_score_log     : 2.2568

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.1429
  hourly_freq         : 0.1429
  transit_freq_log    : 0.1335

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 4879.9143
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Nowa Wieś — GR (H3: 891f5539bd7ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Nowa Wieś — GR
  stop_id             : 250
  city                : elk
  h3_index            : 891f5539bd7ffff
  stop_lat            : 53.7649
  stop_lon            : 22.3002
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : elk

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.9709
  local_score_raw     : -1.0315

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 81.5464
  raw_gravity         : 81.5464
  domain_count        : 0.0000
  infra_score_log     : 4.4134

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.3571
  hourly_freq         : 0.3571
  transit_freq_log    : 0.3054

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 1334.3328
  liquidity           : 3.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 56
  pop_val_log         : 4.0431
```
</details>
<details><summary><b>Paszport Węzła: Regiel — Krzyżówka (H3: 891f55216c3ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Regiel — Krzyżówka
  stop_id             : 172
  city                : elk
  h3_index            : 891f55216c3ffff
  stop_lat            : 53.7961
  stop_lon            : 22.4086
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : elk

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.4854
  local_score_raw     : -1.0790

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 0.0000
  raw_gravity         : 0.0000
  domain_count        : 0.0000
  infra_score_log     : 0.0000

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.4286
  hourly_freq         : 0.4286
  transit_freq_log    : 0.3567

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 4879.9143
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>

---

## AGLOMERACJA: GIZYCKO
**Status:** ✅ SUKCES

### Faza 0: Stan Danych
- **Całkowita populacja w strefie miasta:** 35,698 (Baseline: 30,000) [✅ OK]
- **Ilość Transakcji RCN:** 605
- **Zakres Dat RCN:** 2021-01-12 do 2026-02-18
- **Ceny RCN (PLN/m²):** Średnia=5,512 | Mediana=4,410 | Max=175,949 | IQR=[2,356 - 6,171]
- **Infrastruktura OSM (Punkty):** 7,056
- **Infrastruktura OSM (Poligony/Budynki):** 12,734
- Baza transakcyjna `.gpkg` ustrukturyzowana poprawnie.

### Faza I & II: Pokrycie (Zero-Values)
- **Pustynia Populacyjna:** 20 (14.0%)
- **Pustynia Infrastrukturalna:** 2 (1.4%)
- **Głuche Przystanki:** 9 (6.3%)
- **Wskaźnik Fallback RCN:** 119 (83.2%) (Mediana RCN dla miasta: 4358)

### Faza III: Udowodnione POI w Promieniu 500m

**Rzeczywiste TOP 20 zwalidowanych obiektów (Intersekcja bufor 500m):**

| Tag OSM | Zliczone (Ilość) | Prawdziwa Waga JSON | Całkowita Siła (Score) |
|---|---|---|---|
| `supermarket` | 96 | 7,642,037.30 | **733,635,580.80** |
| `sports_centre` | 36 | 907,914.83 | **32,684,933.88** |
| `marketplace` | 10 | 1,555,027.59 | **15,550,275.90** |
| `place_of_worship` | 133 | 74,304.25 | **9,882,465.25** |
| `pharmacy` | 108 | 51,466.39 | **5,558,370.12** |
| `bank` | 42 | 54,628.23 | **2,294,385.66** |
| `post_office` | 22 | 51,448.36 | **1,131,863.92** |
| `bench` | 256 | 0.00 | **0.00** |
| `parcel_locker` | 128 | 0.00 | **0.00** |
| `restaurant` | 116 | 0.00 | **0.00** |
| `waste_basket` | 103 | 0.00 | **0.00** |
| `bicycle_parking` | 86 | 0.00 | **0.00** |
| `kindergarten` | 91 | 0.00 | **0.00** |
| `parking` | 2598 | 0.00 | **0.00** |
| `atm` | 46 | 0.00 | **0.00** |
| `fast_food` | 41 | 0.00 | **0.00** |
| `cafe` | 39 | 0.00 | **0.00** |
| `waste_disposal` | 40 | 0.00 | **0.00** |
| `toilets` | 22 | 0.00 | **0.00** |
| `ice_cream` | 26 | 0.00 | **0.00** |

### Faza IV: Badanie Próbek Oceny Złotej

#### 🏆 TOP 5 (Najlepsze 5 przystanków w mieście)
<details><summary><b>Paszport Węzła: Warszawska — Wieża Ciśnień (H3: 891f5511c33ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Warszawska — Wieża Ciśnień
  stop_id             : 77
  city                : gizycko
  h3_index            : 891f5511c33ffff
  stop_lat            : 54.0362
  stop_lon            : 21.7789
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : gizycko

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 1.7058

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 1083997.5496
  raw_gravity         : 985452.3178
  domain_count        : 1.0000
  infra_score_log     : 13.8962

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 4.2143
  hourly_freq         : 1.8571
  transit_freq_log    : 1.6514

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 4358.1467
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 248
  pop_val_log         : 5.5175
```
</details>
<details><summary><b>Paszport Węzła: Warszawska — Gimnazjum (H3: 891f5511c33ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Warszawska — Gimnazjum
  stop_id             : 78
  city                : gizycko
  h3_index            : 891f5511c33ffff
  stop_lat            : 54.0361
  stop_lon            : 21.7802
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : gizycko

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 1.7058

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 1083997.5496
  raw_gravity         : 985452.3178
  domain_count        : 1.0000
  infra_score_log     : 13.8962

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 4.2143
  hourly_freq         : 2.3571
  transit_freq_log    : 1.6514

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 4358.1467
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 248
  pop_val_log         : 5.5175
```
</details>
<details><summary><b>Paszport Węzła: Bystry (H3: 891f55119cfffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Bystry
  stop_id             : 106
  city                : gizycko
  h3_index            : 891f55119cfffff
  stop_lat            : 54.0200
  stop_lon            : 21.8151
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : gizycko

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 98.9011
  local_score_raw     : 1.6779

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 5943600.2450
  raw_gravity         : 5403272.9500
  domain_count        : 1.0000
  infra_score_log     : 15.5978

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 3.0000
  hourly_freq         : 3.0000
  transit_freq_log    : 1.3863

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 4358.1467
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 377
  pop_val_log         : 5.9349
```
</details>
<details><summary><b>Paszport Węzła: Nowowiejska — Sklep (H3: 891f5511c8bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Nowowiejska — Sklep
  stop_id             : 48
  city                : gizycko
  h3_index            : 891f5511c8bffff
  stop_lat            : 54.0420
  stop_lon            : 21.7660
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : gizycko

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 97.8022
  local_score_raw     : 1.5953

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 9636417.4319
  raw_gravity         : 8760379.4836
  domain_count        : 1.0000
  infra_score_log     : 16.0811

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 2.3571
  hourly_freq         : 1.2143
  transit_freq_log    : 1.2111

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 4412.7273
  liquidity           : 2.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 379
  pop_val_log         : 5.9402
```
</details>
<details><summary><b>Paszport Węzła: Nowowiejska — Sklep (H3: 891f5511c8bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Nowowiejska — Sklep
  stop_id             : 49
  city                : gizycko
  h3_index            : 891f5511c8bffff
  stop_lat            : 54.0422
  stop_lon            : 21.7662
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : gizycko

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 97.8022
  local_score_raw     : 1.5953

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 9636417.4319
  raw_gravity         : 8760379.4836
  domain_count        : 1.0000
  infra_score_log     : 16.0811

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 2.3571
  hourly_freq         : 1.1429
  transit_freq_log    : 1.2111

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 4412.7273
  liquidity           : 2.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 379
  pop_val_log         : 5.9402
```
</details>

#### 🎲 RANDOM 5 (Środkowe przystanki miasta)
<details><summary><b>Paszport Węzła: Wilkasy ul. Moniuszki (H3: 891f5511ec3ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Wilkasy ul. Moniuszki
  stop_id             : 163
  city                : gizycko
  h3_index            : 891f5511ec3ffff
  stop_lat            : 54.0225
  stop_lon            : 21.7394
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : gizycko

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : D
  local_percentile    : 32.9670
  local_score_raw     : -0.4480

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 55.4138
  raw_gravity         : 55.4138
  domain_count        : 0.0000
  infra_score_log     : 4.0327

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.7857
  hourly_freq         : 0.7857
  transit_freq_log    : 0.5798

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 4358.1467
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Wilkasy — Leśna (H3: 891f551ad8fffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Wilkasy — Leśna
  stop_id             : 140
  city                : gizycko
  h3_index            : 891f551ad8fffff
  stop_lat            : 54.0088
  stop_lon            : 21.7302
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : gizycko

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : B
  local_percentile    : 82.4176
  local_score_raw     : 0.7350

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 551.8760
  raw_gravity         : 551.8760
  domain_count        : 0.0000
  infra_score_log     : 6.3151

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 2.7143
  hourly_freq         : 1.3571
  transit_freq_log    : 1.3122

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 4358.1467
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 252
  pop_val_log         : 5.5334
```
</details>
<details><summary><b>Paszport Węzła: Sulimy Skrzyżowanie (H3: 891f5511d07ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Sulimy Skrzyżowanie
  stop_id             : 171
  city                : gizycko
  h3_index            : 891f5511d07ffff
  stop_lat            : 54.0376
  stop_lon            : 21.8132
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : gizycko

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : D
  local_percentile    : 36.2637
  local_score_raw     : -0.4080

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 343.5714
  raw_gravity         : 343.5714
  domain_count        : 0.0000
  infra_score_log     : 5.8423

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.1429
  hourly_freq         : 0.0714
  transit_freq_log    : 0.1335

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 4358.1467
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 28
  pop_val_log         : 3.3673
```
</details>
<details><summary><b>Paszport Węzła: Wilkasy — Przemysłowa (H3: 891f5511ecbffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Wilkasy — Przemysłowa
  stop_id             : 92
  city                : gizycko
  h3_index            : 891f5511ecbffff
  stop_lat            : 54.0204
  stop_lon            : 21.7338
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : gizycko

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : B
  local_percentile    : 70.3297
  local_score_raw     : 0.2063

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 267.4991
  raw_gravity         : 267.4991
  domain_count        : 0.0000
  infra_score_log     : 5.5928

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 1.5714
  hourly_freq         : 1.5714
  transit_freq_log    : 0.9445

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 4358.1467
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 22
  pop_val_log         : 3.1355
```
</details>
<details><summary><b>Paszport Węzła: Wiejska — Łąkowa (H3: 891f5510223ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Wiejska — Łąkowa
  stop_id             : 83
  city                : gizycko
  h3_index            : 891f5510223ffff
  stop_lat            : 54.0516
  stop_lon            : 21.7649
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : gizycko

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : B
  local_percentile    : 78.0220
  local_score_raw     : 0.6172

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 34819.1597
  raw_gravity         : 34819.1597
  domain_count        : 0.0000
  infra_score_log     : 10.4580

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 1.0000
  hourly_freq         : 0.5000
  transit_freq_log    : 0.6931

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 4358.1467
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 249
  pop_val_log         : 5.5215
```
</details>

#### 💩 BOTTOM 5 (Najsłabsze 5 przystanków)
<details><summary><b>Paszport Węzła: Spytkowo (H3: 891f55101b7ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Spytkowo
  stop_id             : 64
  city                : gizycko
  h3_index            : 891f55101b7ffff
  stop_lat            : 54.0780
  stop_lon            : 21.8230
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : gizycko

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 4.3956
  local_score_raw     : -0.8767

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 205.1743
  raw_gravity         : 205.1743
  domain_count        : 0.0000
  infra_score_log     : 5.3287

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.1429
  hourly_freq         : 0.1429
  transit_freq_log    : 0.1335

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 2497.6807
  liquidity           : 1.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 55
  pop_val_log         : 4.0254
```
</details>
<details><summary><b>Paszport Węzła: Sulimy — Kolonia (H3: 891f5510e37ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Sulimy — Kolonia
  stop_id             : 68
  city                : gizycko
  h3_index            : 891f5510e37ffff
  stop_lat            : 54.0525
  stop_lon            : 21.8406
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : gizycko

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 3.2967
  local_score_raw     : -0.9125

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 17.0644
  raw_gravity         : 17.0644
  domain_count        : 0.0000
  infra_score_log     : 2.8939

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.1429
  hourly_freq         : 0.1429
  transit_freq_log    : 0.1335

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 4358.1467
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Sterławki Małe (H3: 891f551a56fffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Sterławki Małe
  stop_id             : 12666
  city                : gizycko
  h3_index            : 891f551a56fffff
  stop_lat            : 54.0117
  stop_lon            : 21.6464
  lat_grid            : 54.0100
  lon_grid            : 21.6500
  norm_name           : sterawkimae
  source              : polish_trains

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 2.1978
  local_score_raw     : -1.0697

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 9.5410
  raw_gravity         : 9.5410
  domain_count        : 0.0000
  infra_score_log     : 2.3553

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.0000
  hourly_freq         : 0.0000
  transit_freq_log    : 0.0000

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 4358.1467
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Kożuchy Kolonia (H3: 891f5510a03ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Kożuchy Kolonia
  stop_id             : 134
  city                : gizycko
  h3_index            : 891f5510a03ffff
  stop_lat            : 54.0359
  stop_lon            : 21.8457
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : gizycko

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 1.0989
  local_score_raw     : -1.0833

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 0.0000
  raw_gravity         : 0.0000
  domain_count        : 0.0000
  infra_score_log     : 0.0000

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.1429
  hourly_freq         : 0.0714
  transit_freq_log    : 0.1335

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 4358.1467
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 3
  pop_val_log         : 1.3863
```
</details>
<details><summary><b>Paszport Węzła: Kożuchy Kolonia (H3: 891f5510a03ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Kożuchy Kolonia
  stop_id             : 135
  city                : gizycko
  h3_index            : 891f5510a03ffff
  stop_lat            : 54.0361
  stop_lon            : 21.8459
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : gizycko

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 1.0989
  local_score_raw     : -1.0833

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 0.0000
  raw_gravity         : 0.0000
  domain_count        : 0.0000
  infra_score_log     : 0.0000

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.1429
  hourly_freq         : 0.0714
  transit_freq_log    : 0.1335

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 4358.1467
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 3
  pop_val_log         : 1.3863
```
</details>

---

## AGLOMERACJA: GORZOW
**Status:** ✅ SUKCES

### Faza 0: Stan Danych
- **Całkowita populacja w strefie miasta:** 129,431 (Baseline: 120,000) [✅ OK]
- **Ilość Transakcji RCN:** 3,895
- **Zakres Dat RCN:** 2020-03-12 do 2026-03-05
- **Ceny RCN (PLN/m²):** Średnia=8,298 | Mediana=6,393 | Max=378,857 | IQR=[4,745 - 8,242]
- **Infrastruktura OSM (Punkty):** 37,962
- **Infrastruktura OSM (Poligony/Budynki):** 64,319
- Baza transakcyjna `.gpkg` ustrukturyzowana poprawnie.

### Faza I & II: Pokrycie (Zero-Values)
- **Pustynia Populacyjna:** 125 (14.6%)
- **Pustynia Infrastrukturalna:** 0 (0.0%)
- **Głuche Przystanki:** 9 (1.1%)
- **Wskaźnik Fallback RCN:** 429 (50.1%) (Mediana RCN dla miasta: 6218)

### Faza III: Udowodnione POI w Promieniu 500m

**Rzeczywiste TOP 20 zwalidowanych obiektów (Intersekcja bufor 500m):**

| Tag OSM | Zliczone (Ilość) | Prawdziwa Waga JSON | Całkowita Siła (Score) |
|---|---|---|---|
| `supermarket` | 1251 | 9,565,640.39 | **11,966,616,127.89** |
| `sports_centre` | 341 | 1,288,599.63 | **439,412,473.83** |
| `marketplace` | 135 | 1,138,625.38 | **153,714,426.30** |
| `bank` | 1018 | 61,295.04 | **62,398,350.72** |
| `place_of_worship` | 561 | 99,008.82 | **55,543,948.02** |
| `pharmacy` | 885 | 59,279.22 | **52,462,109.70** |
| `post_office` | 418 | 67,660.40 | **28,282,047.20** |
| `bench` | 15768 | 0.00 | **0.00** |
| `waste_basket` | 5809 | 0.00 | **0.00** |
| `parcel_locker` | 2159 | 0.00 | **0.00** |
| `restaurant` | 2261 | 0.00 | **0.00** |
| `bicycle_parking` | 1795 | 0.00 | **0.00** |
| `fast_food` | 1383 | 0.00 | **0.00** |
| `loading_dock` | 1056 | 0.00 | **0.00** |
| `cafe` | 917 | 0.00 | **0.00** |
| `vending_machine` | 811 | 0.00 | **0.00** |
| `waste_disposal` | 2101 | 0.00 | **0.00** |
| `atm` | 782 | 0.00 | **0.00** |
| `parking_entrance` | 652 | 0.00 | **0.00** |
| `parking` | 24636 | 0.00 | **0.00** |

### Faza IV: Badanie Próbek Oceny Złotej

#### 🏆 TOP 5 (Najlepsze 5 przystanków w mieście)
<details><summary><b>Paszport Węzła: Ossolińskich (H3: 891f0a40d8bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Ossolińskich
  stop_id             : 94
  city                : gorzow
  h3_index            : 891f0a40d8bffff
  stop_lat            : 52.7652
  stop_lon            : 15.2464
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : gorzow_wlkp

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 2.0182

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 1790.2298
  raw_gravity         : 1790.2298
  domain_count        : 0
  infra_score_log     : 7.4907

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 16.0000
  hourly_freq         : 8.0000
  transit_freq_log    : 2.8332

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 34838.1345
  liquidity           : 23.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 1102
  pop_val_log         : 7.0058
```
</details>
<details><summary><b>Paszport Węzła: Ossolińskich (H3: 891f0a40d8bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Ossolińskich
  stop_id             : 94
  city                : gorzow
  h3_index            : 891f0a40d8bffff
  stop_lat            : 52.7652
  stop_lon            : 15.2464
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : gorzow

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 2.0182

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 1790.2298
  raw_gravity         : 1790.2298
  domain_count        : 0
  infra_score_log     : 7.4907

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 16.0000
  hourly_freq         : 8.0000
  transit_freq_log    : 2.8332

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 34838.1345
  liquidity           : 23.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 1102
  pop_val_log         : 7.0058
```
</details>
<details><summary><b>Paszport Węzła: Rondo Myśliborskie (H3: 891f0a40a93ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Rondo Myśliborskie
  stop_id             : 3
  city                : gorzow
  h3_index            : 891f0a40a93ffff
  stop_lat            : 52.7348
  stop_lon            : 15.2091
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : gorzow_wlkp

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 99.5305
  local_score_raw     : 1.5101

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 21195213.7109
  raw_gravity         : 16304010.5469
  domain_count        : 3
  infra_score_log     : 16.8693

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 192.2857
  hourly_freq         : 42.1429
  transit_freq_log    : 5.2642

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6185.5670
  liquidity           : 13.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 487
  pop_val_log         : 6.1903
```
</details>
<details><summary><b>Paszport Węzła: Rondo Myśliborskie (H3: 891f0a40a93ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Rondo Myśliborskie
  stop_id             : 3
  city                : gorzow
  h3_index            : 891f0a40a93ffff
  stop_lat            : 52.7348
  stop_lon            : 15.2091
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : gorzow

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 99.5305
  local_score_raw     : 1.5101

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 21195213.7109
  raw_gravity         : 16304010.5469
  domain_count        : 3
  infra_score_log     : 16.8693

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 192.2857
  hourly_freq         : 42.1429
  transit_freq_log    : 5.2642

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6185.5670
  liquidity           : 13.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 487
  pop_val_log         : 6.1903
```
</details>
<details><summary><b>Paszport Węzła: Rondo Myśliborskie (H3: 891f0a40a93ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Rondo Myśliborskie
  stop_id             : 54
  city                : gorzow
  h3_index            : 891f0a40a93ffff
  stop_lat            : 52.7345
  stop_lon            : 15.2112
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : gorzow

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 99.5305
  local_score_raw     : 1.5101

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 21195213.7109
  raw_gravity         : 16304010.5469
  domain_count        : 3
  infra_score_log     : 16.8693

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 192.2857
  hourly_freq         : 24.7143
  transit_freq_log    : 5.2642

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6185.5670
  liquidity           : 13.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 487
  pop_val_log         : 6.1903
```
</details>

#### 🎲 RANDOM 5 (Środkowe przystanki miasta)
<details><summary><b>Paszport Węzła: Wał Okrężny (H3: 891f0a40bc7ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Wał Okrężny
  stop_id             : 174
  city                : gorzow
  h3_index            : 891f0a40bc7ffff
  stop_lat            : 52.7283
  stop_lon            : 15.2425
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : gorzow

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : C
  local_percentile    : 55.8685
  local_score_raw     : 0.1320

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 1047.2537
  raw_gravity         : 1047.2537
  domain_count        : 0
  infra_score_log     : 6.9549

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 39.7143
  hourly_freq         : 10.2857
  transit_freq_log    : 3.7066

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6218.2741
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 208
  pop_val_log         : 5.3423
```
</details>
<details><summary><b>Paszport Węzła: Kręta (H3: 891f0a4e473ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Kręta
  stop_id             : 380
  city                : gorzow
  h3_index            : 891f0a4e473ffff
  stop_lat            : 52.7046
  stop_lon            : 15.2367
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : gorzow_wlkp

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : D
  local_percentile    : 29.1080
  local_score_raw     : -0.4811

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 447.7720
  raw_gravity         : 447.7720
  domain_count        : 0
  infra_score_log     : 6.1065

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 10.0000
  hourly_freq         : 2.5714
  transit_freq_log    : 2.3979

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6218.2741
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 13
  pop_val_log         : 2.6391
```
</details>
<details><summary><b>Paszport Węzła: Marmurowa (H3: 891f0a40c13ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Marmurowa
  stop_id             : 309
  city                : gorzow
  h3_index            : 891f0a40c13ffff
  stop_lat            : 52.7614
  stop_lon            : 15.2102
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : gorzow

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : D
  local_percentile    : 37.0892
  local_score_raw     : -0.3729

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 347.5837
  raw_gravity         : 347.5837
  domain_count        : 0
  infra_score_log     : 5.8539

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 10.0000
  hourly_freq         : 2.4286
  transit_freq_log    : 2.3979

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6218.2741
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 107
  pop_val_log         : 4.6821
```
</details>
<details><summary><b>Paszport Węzła: Zakład Karny (H3: 891f0a40937ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Zakład Karny
  stop_id             : 271
  city                : gorzow
  h3_index            : 891f0a40937ffff
  stop_lat            : 52.7467
  stop_lon            : 15.2863
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : gorzow

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : C
  local_percentile    : 69.9531
  local_score_raw     : 0.3913

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 4182676.0138
  raw_gravity         : 3802432.7398
  domain_count        : 1
  infra_score_log     : 15.2465

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 12.8571
  hourly_freq         : 3.2857
  transit_freq_log    : 2.6288

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6218.2741
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 10
  pop_val_log         : 2.3979
```
</details>
<details><summary><b>Paszport Węzła: Kręta (H3: 891f0a4e473ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Kręta
  stop_id             : 442
  city                : gorzow
  h3_index            : 891f0a4e473ffff
  stop_lat            : 52.7044
  stop_lon            : 15.2365
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : gorzow

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : D
  local_percentile    : 29.1080
  local_score_raw     : -0.4811

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 447.7720
  raw_gravity         : 447.7720
  domain_count        : 0
  infra_score_log     : 6.1065

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 10.0000
  hourly_freq         : 2.4286
  transit_freq_log    : 2.3979

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6218.2741
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 13
  pop_val_log         : 2.6391
```
</details>

#### 💩 BOTTOM 5 (Najsłabsze 5 przystanków)
<details><summary><b>Paszport Węzła: Gorzów Wielkopolski Karnin (H3: 891f0a4e143ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Gorzów Wielkopolski Karnin
  stop_id             : 13946
  city                : gorzow
  h3_index            : 891f0a4e143ffff
  stop_lat            : 52.6889
  stop_lon            : 15.2810
  lat_grid            : 52.6900
  lon_grid            : 15.2800
  norm_name           : gorzowwielkopolskikarnin
  source              : polish_trains

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 1.4085
  local_score_raw     : -1.2731

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 201.1007
  raw_gravity         : 201.1007
  domain_count        : 0
  infra_score_log     : 5.3088

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.0000
  hourly_freq         : 0.0000
  transit_freq_log    : 0.0000

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6218.2741
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 5
  pop_val_log         : 1.7918
```
</details>
<details><summary><b>Paszport Węzła: Chróścik INNEKO (H3: 891f0a41c1bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Chróścik INNEKO
  stop_id             : 397
  city                : gorzow
  h3_index            : 891f0a41c1bffff
  stop_lat            : 52.7219
  stop_lon            : 15.1378
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : gorzow

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.9390
  local_score_raw     : -1.3098

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 70.4006
  raw_gravity         : 70.4006
  domain_count        : 0
  infra_score_log     : 4.2683

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.8571
  hourly_freq         : 0.4286
  transit_freq_log    : 0.6190

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6218.2741
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Chróścik INNEKO (H3: 891f0a41c1bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Chróścik INNEKO
  stop_id             : 397
  city                : gorzow
  h3_index            : 891f0a41c1bffff
  stop_lat            : 52.7219
  stop_lon            : 15.1378
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : gorzow_wlkp

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.9390
  local_score_raw     : -1.3098

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 70.4006
  raw_gravity         : 70.4006
  domain_count        : 0
  infra_score_log     : 4.2683

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.8571
  hourly_freq         : 0.4286
  transit_freq_log    : 0.6190

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6218.2741
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Działkowców Pętla  (H3: 891f0a40db3ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Działkowców Pętla 
  stop_id             : 548
  city                : gorzow
  h3_index            : 891f0a40db3ffff
  stop_lat            : 52.7681
  stop_lon            : 15.2605
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : gorzow_wlkp

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.4695
  local_score_raw     : -1.3217

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 39.2958
  raw_gravity         : 39.2958
  domain_count        : 0
  infra_score_log     : 3.6962

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 1.1429
  hourly_freq         : 0.5714
  transit_freq_log    : 0.7621

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6218.2741
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Działkowców Pętla  (H3: 891f0a40db3ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Działkowców Pętla 
  stop_id             : 548
  city                : gorzow
  h3_index            : 891f0a40db3ffff
  stop_lat            : 52.7681
  stop_lon            : 15.2605
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : gorzow

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.4695
  local_score_raw     : -1.3217

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 39.2958
  raw_gravity         : 39.2958
  domain_count        : 0
  infra_score_log     : 3.6962

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 1.1429
  hourly_freq         : 0.5714
  transit_freq_log    : 0.7621

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6218.2741
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>

---

## AGLOMERACJA: GZM
**Status:** ✅ SUKCES

### Faza 0: Stan Danych
- **Całkowita populacja w strefie miasta:** 3,664,676 (Baseline: 2,300,000) [✅ OK]
- **Ilość Transakcji RCN:** 212,099
- **Zakres Dat RCN:** 2020-01-02 do 2026-03-09
- **Ceny RCN (PLN/m²):** Średnia=9,171 | Mediana=6,389 | Max=498,949 | IQR=[4,272 - 10,355]
- **Infrastruktura OSM (Punkty):** 679,629
- **Infrastruktura OSM (Poligony/Budynki):** 1,271,377
- Baza transakcyjna `.gpkg` ustrukturyzowana poprawnie.

### Faza I & II: Pokrycie (Zero-Values)
- **Pustynia Populacyjna:** 1107 (10.8%)
- **Pustynia Infrastrukturalna:** 6 (0.1%)
- **Głuche Przystanki:** 45 (0.4%)
- **Wskaźnik Fallback RCN:** 5973 (58.3%) (Mediana RCN dla miasta: 6257)

### Faza III: Udowodnione POI w Promieniu 500m

**Rzeczywiste TOP 20 zwalidowanych obiektów (Intersekcja bufor 500m):**

| Tag OSM | Zliczone (Ilość) | Prawdziwa Waga JSON | Całkowita Siła (Score) |
|---|---|---|---|
| `supermarket` | 8190 | 12,619,128.96 | **103,350,666,182.40** |
| `sports_centre` | 2719 | 1,577,216.70 | **4,288,452,207.30** |
| `exhibition_centre` | 46 | 85,830,557.65 | **3,948,205,651.90** |
| `marketplace` | 892 | 1,779,219.05 | **1,587,063,392.60** |
| `place_of_worship` | 7307 | 117,911.04 | **861,575,969.28** |
| `pharmacy` | 9083 | 73,790.37 | **670,237,930.71** |
| `bank` | 7211 | 78,854.93 | **568,622,900.23** |
| `post_office` | 2943 | 83,401.89 | **245,451,762.27** |
| `bench` | 187365 | 0.00 | **0.00** |
| `waste_basket` | 59186 | 0.00 | **0.00** |
| `bicycle_parking` | 25130 | 0.00 | **0.00** |
| `parcel_locker` | 16086 | 0.00 | **0.00** |
| `restaurant` | 14971 | 0.00 | **0.00** |
| `recycling` | 13562 | 0.00 | **0.00** |
| `waste_disposal` | 17891 | 0.00 | **0.00** |
| `shelter` | 19472 | 0.00 | **0.00** |
| `fast_food` | 9840 | 0.00 | **0.00** |
| `bicycle_rental` | 8061 | 0.00 | **0.00** |
| `vending_machine` | 7737 | 0.00 | **0.00** |
| `atm` | 6893 | 0.00 | **0.00** |

### Faza IV: Badanie Próbek Oceny Złotej

#### 🏆 TOP 5 (Najlepsze 5 przystanków w mieście)
<details><summary><b>Paszport Węzła: Wilkowice Bystra (H3: 891e0510a93ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Wilkowice Bystra
  stop_id             : 76372
  city                : gzm
  h3_index            : 891e0510a93ffff
  stop_lat            : 49.7603
  stop_lon            : 19.0881
  lat_grid            : 49.7600
  lon_grid            : 19.0900
  norm_name           : wilkowicebystra
  source              : polish_trains

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 4.5944

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 14984524.1971
  raw_gravity         : 13622294.7247
  domain_count        : 1.0000
  infra_score_log     : 16.5225

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 113.9286
  hourly_freq         : 37.1429
  transit_freq_log    : 4.7443

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 38209.7883
  liquidity           : 18.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 119.0000
  pop_val_log         : 4.7875
```
</details>
<details><summary><b>Paszport Węzła: Wilkowice Bystra (H3: 891e0510a93ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Wilkowice Bystra
  stop_id             : 76372_BUS
  city                : gzm
  h3_index            : 891e0510a93ffff
  stop_lat            : 49.7600
  stop_lon            : 19.0882
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : pkp-ks

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 4.5944

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 14984524.1971
  raw_gravity         : 13622294.7247
  domain_count        : 1.0000
  infra_score_log     : 16.5225

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 113.9286
  hourly_freq         : 0.0000
  transit_freq_log    : 4.7443

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 38209.7883
  liquidity           : 18.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 119.0000
  pop_val_log         : 4.7875
```
</details>
<details><summary><b>Paszport Węzła: Wilkowice Bystra (H3: 891e0510a93ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Wilkowice Bystra
  stop_id             : 76372_II
  city                : gzm
  h3_index            : 891e0510a93ffff
  stop_lat            : 49.7600
  stop_lon            : 19.0882
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : pkp-ks

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 4.5944

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 14984524.1971
  raw_gravity         : 13622294.7247
  domain_count        : 1.0000
  infra_score_log     : 16.5225

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 113.9286
  hourly_freq         : 2.5000
  transit_freq_log    : 4.7443

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 38209.7883
  liquidity           : 18.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 119.0000
  pop_val_log         : 4.7875
```
</details>
<details><summary><b>Paszport Węzła: Wilkowice Bystra (H3: 891e0510a93ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Wilkowice Bystra
  stop_id             : 76372_I
  city                : gzm
  h3_index            : 891e0510a93ffff
  stop_lat            : 49.7600
  stop_lon            : 19.0882
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : pkp-ks

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 4.5944

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 14984524.1971
  raw_gravity         : 13622294.7247
  domain_count        : 1.0000
  infra_score_log     : 16.5225

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 113.9286
  hourly_freq         : 0.0000
  transit_freq_log    : 4.7443

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 38209.7883
  liquidity           : 18.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 119.0000
  pop_val_log         : 4.7875
```
</details>
<details><summary><b>Paszport Węzła: Wilkowice Bystra (H3: 891e0510a93ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Wilkowice Bystra
  stop_id             : 76372
  city                : gzm
  h3_index            : 891e0510a93ffff
  stop_lat            : 49.7600
  stop_lon            : 19.0882
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : 2025-2026

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 4.5944

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 14984524.1971
  raw_gravity         : 13622294.7247
  domain_count        : 1.0000
  infra_score_log     : 16.5225

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 113.9286
  hourly_freq         : 37.1429
  transit_freq_log    : 4.7443

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 38209.7883
  liquidity           : 18.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 119.0000
  pop_val_log         : 4.7875
```
</details>

#### 🎲 RANDOM 5 (Środkowe przystanki miasta)
<details><summary><b>Paszport Węzła: Obszary PKP (H3: 891e236c6d3ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Obszary PKP
  stop_id             : 396
  city                : gzm
  h3_index            : 891e236c6d3ffff
  stop_lat            : 50.0353
  stop_lon            : 18.4923
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : rybnik-jastrzebie

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : C
  local_percentile    : 63.4711
  local_score_raw     : 0.1259

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 388.2621
  raw_gravity         : 388.2621
  domain_count        : 0.0000
  infra_score_log     : 5.9643

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 16.4286
  hourly_freq         : 4.7857
  transit_freq_log    : 2.8581

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6257.3298
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 47.0000
  pop_val_log         : 3.8712
```
</details>
<details><summary><b>Paszport Węzła: Połomia Gospoda (H3: 891e23312afffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Połomia Gospoda
  stop_id             : 5886
  city                : gzm
  h3_index            : 891e23312afffff
  stop_lat            : 50.4836
  stop_lon            : 18.7126
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : gzm

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : D
  local_percentile    : 27.3554
  local_score_raw     : -0.4373

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 546.1896
  raw_gravity         : 546.1896
  domain_count        : 0.0000
  infra_score_log     : 6.3048

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 1.9286
  hourly_freq         : 0.9286
  transit_freq_log    : 1.0745

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6257.3298
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 61.0000
  pop_val_log         : 4.1271
```
</details>
<details><summary><b>Paszport Węzła: Warszowice Kolonia Borki II (H3: 891e0599ec7ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Warszowice Kolonia Borki II
  stop_id             : 759
  city                : gzm
  h3_index            : 891e0599ec7ffff
  stop_lat            : 49.9828
  stop_lon            : 18.7591
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : rybnik-jastrzebie

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : D
  local_percentile    : 37.2314
  local_score_raw     : -0.2894

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 133.6805
  raw_gravity         : 133.6805
  domain_count        : 0.0000
  infra_score_log     : 4.9029

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 8.5714
  hourly_freq         : 7.3571
  transit_freq_log    : 2.2588

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6257.3298
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 10.0000
  pop_val_log         : 2.3979
```
</details>
<details><summary><b>Paszport Węzła: Boniowice Szkoła (H3: 891e2338e8bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Boniowice Szkoła
  stop_id             : 3709
  city                : gzm
  h3_index            : 891e2338e8bffff
  stop_lat            : 50.3978
  stop_lon            : 18.7119
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : gzm

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : D
  local_percentile    : 43.3264
  local_score_raw     : -0.2013

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 223.6171
  raw_gravity         : 223.6171
  domain_count        : 0.0000
  infra_score_log     : 5.4144

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 7.3571
  hourly_freq         : 7.3571
  transit_freq_log    : 2.1231

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6257.3298
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 35.0000
  pop_val_log         : 3.5835
```
</details>
<details><summary><b>Paszport Węzła: Dąbrowa Miejska Kościół nż (H3: 891e2321c4bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Dąbrowa Miejska Kościół nż
  stop_id             : 7905
  city                : gzm
  h3_index            : 891e2321c4bffff
  stop_lat            : 50.3700
  stop_lon            : 18.8951
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : gzm

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : D
  local_percentile    : 40.9298
  local_score_raw     : -0.2337

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 379.7771
  raw_gravity         : 379.7771
  domain_count        : 0.0000
  infra_score_log     : 5.9422

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 12.8571
  hourly_freq         : 5.7143
  transit_freq_log    : 2.6288

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6257.3298
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0.0000
  pop_val_log         : 0.0000
```
</details>

#### 💩 BOTTOM 5 (Najsłabsze 5 przystanków)
<details><summary><b>Paszport Węzła: Lyski Las (H3: 891e2360257ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Lyski Las
  stop_id             : 936
  city                : gzm
  h3_index            : 891e2360257ffff
  stop_lat            : 50.1325
  stop_lon            : 18.3962
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : rybnik

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.0826
  local_score_raw     : -1.3335

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 16.3631
  raw_gravity         : 16.3631
  domain_count        : 0.0000
  infra_score_log     : 2.8543

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.3571
  hourly_freq         : 0.0000
  transit_freq_log    : 0.3054

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6257.3298
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0.0000
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Paczyna (H3: 891e233b2a7ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Paczyna
  stop_id             : 70243
  city                : gzm
  h3_index            : 891e233b2a7ffff
  stop_lat            : 50.4121
  stop_lon            : 18.5722
  lat_grid            : 50.4100
  lon_grid            : 18.5700
  norm_name           : paczyna
  source              : polish_trains

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.0620
  local_score_raw     : -1.3599

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 38.1630
  raw_gravity         : 38.1630
  domain_count        : 0.0000
  infra_score_log     : 3.6677

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.0000
  hourly_freq         : 0.0000
  transit_freq_log    : 0.0000

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6257.3298
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0.0000
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Karb Łanowa (H3: 891e2321ecbffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Karb Łanowa
  stop_id             : 5059
  city                : gzm
  h3_index            : 891e2321ecbffff
  stop_lat            : 50.3576
  stop_lon            : 18.8761
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : gzm

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.0413
  local_score_raw     : -1.3780

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 123.6018
  raw_gravity         : 123.6018
  domain_count        : 0.0000
  infra_score_log     : 4.8251

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 1.0714
  hourly_freq         : 0.5000
  transit_freq_log    : 0.7282

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 1795.8657
  liquidity           : 4.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0.0000
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Karb Łanowa (H3: 891e2321ecbffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Karb Łanowa
  stop_id             : 5058
  city                : gzm
  h3_index            : 891e2321ecbffff
  stop_lat            : 50.3577
  stop_lon            : 18.8762
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : gzm

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.0413
  local_score_raw     : -1.3780

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 123.6018
  raw_gravity         : 123.6018
  domain_count        : 0.0000
  infra_score_log     : 4.8251

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 1.0714
  hourly_freq         : 0.5714
  transit_freq_log    : 0.7282

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 1795.8657
  liquidity           : 4.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0.0000
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Płużniczka Skrzyżowanie z DK-94 (H3: 891e230ecb7ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Płużniczka Skrzyżowanie z DK-94
  stop_id             : 5912
  city                : gzm
  h3_index            : 891e230ecb7ffff
  stop_lat            : 50.4665
  stop_lon            : 18.4856
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : gzm

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.0207
  local_score_raw     : -1.4021

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 158.3300
  raw_gravity         : 158.3300
  domain_count        : 0.0000
  infra_score_log     : 5.0710

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.7857
  hourly_freq         : 0.7857
  transit_freq_log    : 0.5798

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 195.1872
  liquidity           : 1.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 6.0000
  pop_val_log         : 1.9459
```
</details>

---

## AGLOMERACJA: KIELCE
**Status:** ✅ SUKCES

### Faza 0: Stan Danych
- **Całkowita populacja w strefie miasta:** 287,314 (Baseline: 190,000) [✅ OK]
- **Ilość Transakcji RCN:** 9,588
- **Zakres Dat RCN:** 2021-07-06 do 2026-02-26
- **Ceny RCN (PLN/m²):** Średnia=7,905 | Mediana=7,545 | Max=361,345 | IQR=[5,151 - 9,273]
- **Infrastruktura OSM (Punkty):** 107,276
- **Infrastruktura OSM (Poligony/Budynki):** 150,037
- Baza transakcyjna `.gpkg` ustrukturyzowana poprawnie.

### Faza I & II: Pokrycie (Zero-Values)
- **Pustynia Populacyjna:** 117 (8.6%)
- **Pustynia Infrastrukturalna:** 0 (0.0%)
- **Głuche Przystanki:** 12 (0.9%)
- **Wskaźnik Fallback RCN:** 1032 (76.1%) (Mediana RCN dla miasta: 7442)

### Faza III: Udowodnione POI w Promieniu 500m

**Rzeczywiste TOP 20 zwalidowanych obiektów (Intersekcja bufor 500m):**

| Tag OSM | Zliczone (Ilość) | Prawdziwa Waga JSON | Całkowita Siła (Score) |
|---|---|---|---|
| `supermarket` | 874 | 8,927,501.20 | **7,802,636,048.80** |
| `exhibition_centre` | 8 | 283,047,535.45 | **2,264,380,283.60** |
| `sports_centre` | 239 | 1,329,471.32 | **317,743,645.48** |
| `marketplace` | 52 | 1,556,896.83 | **80,958,635.16** |
| `place_of_worship` | 641 | 99,064.48 | **63,500,331.68** |
| `pharmacy` | 991 | 63,399.78 | **62,829,181.98** |
| `bank` | 611 | 68,341.24 | **41,756,497.64** |
| `post_office` | 442 | 64,849.05 | **28,663,280.10** |
| `bench` | 22190 | 0.00 | **0.00** |
| `waste_basket` | 8298 | 0.00 | **0.00** |
| `parcel_locker` | 2253 | 0.00 | **0.00** |
| `restaurant` | 1843 | 0.00 | **0.00** |
| `fast_food` | 1592 | 0.00 | **0.00** |
| `bicycle_parking` | 1357 | 0.00 | **0.00** |
| `grit_bin` | 1224 | 0.00 | **0.00** |
| `parking_entrance` | 1185 | 0.00 | **0.00** |
| `atm` | 1045 | 0.00 | **0.00** |
| `fountain` | 965 | 0.00 | **0.00** |
| `vending_machine` | 917 | 0.00 | **0.00** |
| `recycling` | 810 | 0.00 | **0.00** |

### Faza IV: Badanie Próbek Oceny Złotej

#### 🏆 TOP 5 (Najlepsze 5 przystanków w mieście)
<details><summary><b>Paszport Węzła: Husarska (H3: 891e2eb5ac3ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Husarska
  stop_id             : 1388
  city                : kielce
  h3_index            : 891e2eb5ac3ffff
  stop_lat            : 50.8536
  stop_lon            : 20.6229
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : kielce

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 2.6707

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 1072.4220
  raw_gravity         : 1072.4220
  domain_count        : 0
  infra_score_log     : 6.9786

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 5.6429
  hourly_freq         : 5.6429
  transit_freq_log    : 1.8935

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 25300.4428
  liquidity           : 3.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 182
  pop_val_log         : 5.2095
```
</details>
<details><summary><b>Paszport Węzła: Dworzec Kolejowy (H3: 891e2eb5ebbffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Dworzec Kolejowy
  stop_id             : 1424
  city                : kielce
  h3_index            : 891e2eb5ebbffff
  stop_lat            : 50.8736
  stop_lon            : 20.6193
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : kielce

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 99.8737
  local_score_raw     : 2.3487

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 21597730.1795
  raw_gravity         : 15426950.1282
  domain_count        : 4
  infra_score_log     : 16.8881

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 92.5000
  hourly_freq         : 21.0000
  transit_freq_log    : 4.5380

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6930.0628
  liquidity           : 50.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 608
  pop_val_log         : 6.4118
```
</details>
<details><summary><b>Paszport Węzła: Czarnowska / Dworzec Autobusowy (H3: 891e2eb5ebbffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Czarnowska / Dworzec Autobusowy
  stop_id             : 1187
  city                : kielce
  h3_index            : 891e2eb5ebbffff
  stop_lat            : 50.8748
  stop_lon            : 20.6220
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : kielce

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 99.8737
  local_score_raw     : 2.3487

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 21597730.1795
  raw_gravity         : 15426950.1282
  domain_count        : 4
  infra_score_log     : 16.8881

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 92.5000
  hourly_freq         : 31.6429
  transit_freq_log    : 4.5380

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6930.0628
  liquidity           : 50.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 608
  pop_val_log         : 6.4118
```
</details>
<details><summary><b>Paszport Węzła: Czarnowska / Dworzec Autobusowy (H3: 891e2eb5ebbffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Czarnowska / Dworzec Autobusowy
  stop_id             : 67
  city                : kielce
  h3_index            : 891e2eb5ebbffff
  stop_lat            : 50.8746
  stop_lon            : 20.6218
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : kielce

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 99.8737
  local_score_raw     : 2.3487

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 21597730.1795
  raw_gravity         : 15426950.1282
  domain_count        : 4
  infra_score_log     : 16.8881

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 92.5000
  hourly_freq         : 30.8571
  transit_freq_log    : 4.5380

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6930.0628
  liquidity           : 50.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 608
  pop_val_log         : 6.4118
```
</details>
<details><summary><b>Paszport Węzła: Dworzec Kolejowy (H3: 891e2eb5ebbffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Dworzec Kolejowy
  stop_id             : 102
  city                : kielce
  h3_index            : 891e2eb5ebbffff
  stop_lat            : 50.8742
  stop_lon            : 20.6193
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : kielce

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 99.8737
  local_score_raw     : 2.3487

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 21597730.1795
  raw_gravity         : 15426950.1282
  domain_count        : 4
  infra_score_log     : 16.8881

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 92.5000
  hourly_freq         : 9.0000
  transit_freq_log    : 4.5380

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6930.0628
  liquidity           : 50.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 608
  pop_val_log         : 6.4118
```
</details>

#### 🎲 RANDOM 5 (Środkowe przystanki miasta)
<details><summary><b>Paszport Węzła: Domaszowska WORD (H3: 891e2eb58a3ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Domaszowska WORD
  stop_id             : 985
  city                : kielce
  h3_index            : 891e2eb58a3ffff
  stop_lat            : 50.8748
  stop_lon            : 20.6627
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : kielce

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : C
  local_percentile    : 69.3182
  local_score_raw     : 0.1486

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 648.3166
  raw_gravity         : 648.3166
  domain_count        : 0
  infra_score_log     : 6.4759

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 5.7857
  hourly_freq         : 2.9286
  transit_freq_log    : 1.9148

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 7442.2073
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 80
  pop_val_log         : 4.3944
```
</details>
<details><summary><b>Paszport Węzła: Długa / Skrajna (H3: 891e2eb518bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Długa / Skrajna
  stop_id             : 1340
  city                : kielce
  h3_index            : 891e2eb518bffff
  stop_lat            : 50.8908
  stop_lon            : 20.5933
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : kielce

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : D
  local_percentile    : 43.5606
  local_score_raw     : -0.2979

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 336.5008
  raw_gravity         : 336.5008
  domain_count        : 0
  infra_score_log     : 5.8216

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 1.5000
  hourly_freq         : 1.5000
  transit_freq_log    : 0.9163

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 7442.2073
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 71
  pop_val_log         : 4.2767
```
</details>
<details><summary><b>Paszport Węzła: Zagórze II (H3: 891e2eb5b87ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Zagórze II
  stop_id             : 616
  city                : kielce
  h3_index            : 891e2eb5b87ffff
  stop_lat            : 50.8589
  stop_lon            : 20.6708
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : kielce

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : B
  local_percentile    : 70.5808
  local_score_raw     : 0.1756

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 1120.1006
  raw_gravity         : 1120.1006
  domain_count        : 0
  infra_score_log     : 7.0221

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 3.4286
  hourly_freq         : 3.4286
  transit_freq_log    : 1.4881

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 7903.6757
  liquidity           : 10.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 166
  pop_val_log         : 5.1180
```
</details>
<details><summary><b>Paszport Węzła: Cedzyna I (H3: 891e2ea6403ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Cedzyna I
  stop_id             : 48
  city                : kielce
  h3_index            : 891e2ea6403ffff
  stop_lat            : 50.8679
  stop_lon            : 20.7200
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : kielce

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : C
  local_percentile    : 66.0354
  local_score_raw     : 0.0726

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 1038.5957
  raw_gravity         : 1038.5957
  domain_count        : 0
  infra_score_log     : 6.9466

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 4.0714
  hourly_freq         : 4.0714
  transit_freq_log    : 1.6236

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 7442.2073
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 62
  pop_val_log         : 4.1431
```
</details>
<details><summary><b>Paszport Węzła: Suków Rogatka (H3: 891e2ea71cbffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Suków Rogatka
  stop_id             : 411
  city                : kielce
  h3_index            : 891e2ea71cbffff
  stop_lat            : 50.8145
  stop_lon            : 20.6870
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : kielce

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : D
  local_percentile    : 47.4747
  local_score_raw     : -0.2483

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 631.2881
  raw_gravity         : 631.2881
  domain_count        : 0
  infra_score_log     : 6.4493

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 1.2143
  hourly_freq         : 1.2143
  transit_freq_log    : 0.7949

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 7442.2073
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 96
  pop_val_log         : 4.5747
```
</details>

#### 💩 BOTTOM 5 (Najsłabsze 5 przystanków)
<details><summary><b>Paszport Węzła: Słopiec III (H3: 891e2ea43bbffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Słopiec III
  stop_id             : 1386
  city                : kielce
  h3_index            : 891e2ea43bbffff
  stop_lat            : 50.7853
  stop_lon            : 20.7758
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : kielce

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.6313
  local_score_raw     : -1.0792

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 54.4856
  raw_gravity         : 54.4856
  domain_count        : 0
  infra_score_log     : 4.0161

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.3571
  hourly_freq         : 0.3571
  transit_freq_log    : 0.3054

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 7442.2073
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Kostomłoty (H3: 891e2eb4637ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Kostomłoty
  stop_id             : 63784
  city                : kielce
  h3_index            : 891e2eb4637ffff
  stop_lat            : 50.9215
  stop_lon            : 20.6160
  lat_grid            : 50.9200
  lon_grid            : 20.6200
  norm_name           : kostomoty
  source              : polish_trains

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.5051
  local_score_raw     : -1.1192

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 105.5746
  raw_gravity         : 105.5746
  domain_count        : 0
  infra_score_log     : 4.6688

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.0000
  hourly_freq         : 0.0000
  transit_freq_log    : 0.0000

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 7442.2073
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Dębska Wola (H3: 891e2eae263ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Dębska Wola
  stop_id             : 64097
  city                : kielce
  h3_index            : 891e2eae263ffff
  stop_lat            : 50.7012
  stop_lon            : 20.5972
  lat_grid            : 50.7000
  lon_grid            : 20.6000
  norm_name           : debskawola
  source              : polish_trains

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.3788
  local_score_raw     : -1.1666

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 68.1354
  raw_gravity         : 68.1354
  domain_count        : 0
  infra_score_log     : 4.2361

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.0000
  hourly_freq         : 0.0000
  transit_freq_log    : 0.0000

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 7442.2073
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Dębska Wola (H3: 891e2eae2afffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Dębska Wola
  stop_id             : 1242
  city                : kielce
  h3_index            : 891e2eae2afffff
  stop_lat            : 50.7108
  stop_lon            : 20.6046
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : kielce

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.2525
  local_score_raw     : -1.2426

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 17.0905
  raw_gravity         : 17.0905
  domain_count        : 0
  infra_score_log     : 2.8954

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.2143
  hourly_freq         : 0.2143
  transit_freq_log    : 0.1942

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 7442.2073
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Nida (H3: 891e2ea0a03ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Nida
  stop_id             : 63875
  city                : kielce
  h3_index            : 891e2ea0a03ffff
  stop_lat            : 50.7609
  stop_lon            : 20.5783
  lat_grid            : 50.7600
  lon_grid            : 20.5800
  norm_name           : nida
  source              : polish_trains

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.1263
  local_score_raw     : -1.3041

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 18.7082
  raw_gravity         : 18.7082
  domain_count        : 0
  infra_score_log     : 2.9810

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.0000
  hourly_freq         : 0.0000
  transit_freq_log    : 0.0000

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 7442.2073
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>

---

## AGLOMERACJA: KRAKOW
**Status:** ✅ SUKCES

### Faza 0: Stan Danych
- **Całkowita populacja w strefie miasta:** 1,126,209 (Baseline: 800,000) [✅ OK]
- **Ilość Transakcji RCN:** 76,536
- **Zakres Dat RCN:** 2020-01-02 do 2026-03-10
- **Ceny RCN (PLN/m²):** Średnia=13,807 | Mediana=11,013 | Max=498,949 | IQR=[7,176 - 14,477]
- **Infrastruktura OSM (Punkty):** 380,147
- **Infrastruktura OSM (Poligony/Budynki):** 491,827
- Baza transakcyjna `.gpkg` ustrukturyzowana poprawnie.

### Faza I & II: Pokrycie (Zero-Values)
- **Pustynia Populacyjna:** 317 (7.4%)
- **Pustynia Infrastrukturalna:** 0 (0.0%)
- **Głuche Przystanki:** 10 (0.2%)
- **Wskaźnik Fallback RCN:** 2214 (52.0%) (Mediana RCN dla miasta: 10796)

### Faza III: Udowodnione POI w Promieniu 500m

**Rzeczywiste TOP 20 zwalidowanych obiektów (Intersekcja bufor 500m):**

| Tag OSM | Zliczone (Ilość) | Prawdziwa Waga JSON | Całkowita Siła (Score) |
|---|---|---|---|
| `supermarket` | 3706 | 10,442,980.20 | **38,701,684,621.20** |
| `exhibition_centre` | 11 | 244,011,281.66 | **2,684,124,098.26** |
| `sports_centre` | 1429 | 1,210,762.31 | **1,730,179,340.99** |
| `marketplace` | 452 | 1,658,454.43 | **749,621,402.36** |
| `place_of_worship` | 3981 | 106,451.25 | **423,782,426.25** |
| `pharmacy` | 5095 | 68,709.61 | **350,075,462.95** |
| `bank` | 2909 | 72,376.25 | **210,542,511.25** |
| `post_office` | 2311 | 74,210.74 | **171,501,020.14** |
| `bench` | 171356 | 0.00 | **0.00** |
| `bicycle_parking` | 83149 | 0.00 | **0.00** |
| `waste_basket` | 72119 | 0.00 | **0.00** |
| `parking_entrance` | 18586 | 0.00 | **0.00** |
| `parcel_locker` | 18777 | 0.00 | **0.00** |
| `vending_machine` | 15374 | 0.00 | **0.00** |
| `recycling` | 13921 | 0.00 | **0.00** |
| `restaurant` | 14383 | 0.00 | **0.00** |
| `fast_food` | 13883 | 0.00 | **0.00** |
| `atm` | 10025 | 0.00 | **0.00** |
| `cafe` | 7815 | 0.00 | **0.00** |
| `waste_disposal` | 18208 | 0.00 | **0.00** |

### Faza IV: Badanie Próbek Oceny Złotej

#### 🏆 TOP 5 (Najlepsze 5 przystanków w mieście)
<details><summary><b>Paszport Węzła: Praska (H3: 891e2e6b3d7ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Praska
  stop_id             : stop_416_58001
  city                : krakow
  h3_index            : 891e2e6b3d7ffff
  stop_lat            : 50.0498
  stop_lon            : 19.9205
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : krakow-bus

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 2.2340

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 3718.3719
  raw_gravity         : 3718.3719
  domain_count        : 0
  infra_score_log     : 8.2213

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 9.1429
  hourly_freq         : 4.5000
  transit_freq_log    : 2.3168

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 55500.0000
  liquidity           : 9.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 204
  pop_val_log         : 5.3230
```
</details>
<details><summary><b>Paszport Węzła: Praska (H3: 891e2e6b3d7ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Praska
  stop_id             : stop_416_58002
  city                : krakow
  h3_index            : 891e2e6b3d7ffff
  stop_lat            : 50.0497
  stop_lon            : 19.9206
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : krakow-bus

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 2.2340

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 3718.3719
  raw_gravity         : 3718.3719
  domain_count        : 0
  infra_score_log     : 8.2213

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 9.1429
  hourly_freq         : 4.6429
  transit_freq_log    : 2.3168

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 55500.0000
  liquidity           : 9.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 204
  pop_val_log         : 5.3230
```
</details>
<details><summary><b>Paszport Węzła: św. Gertrudy (H3: 891e2e6b143ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : św. Gertrudy
  stop_id             : stop_1102_347019
  city                : krakow
  h3_index            : 891e2e6b143ffff
  stop_lat            : 50.0586
  stop_lon            : 19.9410
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : krakow-tram

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 99.9460
  local_score_raw     : 2.2309

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 318229.0710
  raw_gravity         : 289299.1554
  domain_count        : 1
  infra_score_log     : 12.6705

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 61.5000
  hourly_freq         : 6.5000
  transit_freq_log    : 4.1352

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 31351.2452
  liquidity           : 54.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 211
  pop_val_log         : 5.3566
```
</details>
<details><summary><b>Paszport Węzła: Plac Wszystkich Świętych (H3: 891e2e6b143ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Plac Wszystkich Świętych
  stop_id             : stop_325_136019
  city                : krakow
  h3_index            : 891e2e6b143ffff
  stop_lat            : 50.0591
  stop_lon            : 19.9382
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : krakow-tram

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 99.9460
  local_score_raw     : 2.2309

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 318229.0710
  raw_gravity         : 289299.1554
  domain_count        : 1
  infra_score_log     : 12.6705

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 61.5000
  hourly_freq         : 14.2857
  transit_freq_log    : 4.1352

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 31351.2452
  liquidity           : 54.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 211
  pop_val_log         : 5.3566
```
</details>
<details><summary><b>Paszport Węzła: Plac Wszystkich Świętych (H3: 891e2e6b143ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Plac Wszystkich Świętych
  stop_id             : stop_967_136001
  city                : krakow
  h3_index            : 891e2e6b143ffff
  stop_lat            : 50.0591
  stop_lon            : 19.9383
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : krakow-bus

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 99.9460
  local_score_raw     : 2.2309

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 318229.0710
  raw_gravity         : 289299.1554
  domain_count        : 1
  infra_score_log     : 12.6705

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 61.5000
  hourly_freq         : 0.0000
  transit_freq_log    : 4.1352

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 31351.2452
  liquidity           : 54.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 211
  pop_val_log         : 5.3566
```
</details>

#### 🎲 RANDOM 5 (Środkowe przystanki miasta)
<details><summary><b>Paszport Węzła: Arctowskiego (H3: 891e2e68097ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Arctowskiego
  stop_id             : stop_3213_384801
  city                : krakow
  h3_index            : 891e2e68097ffff
  stop_lat            : 50.0570
  stop_lon            : 20.0017
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : krakow-bus

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : C
  local_percentile    : 64.2009
  local_score_raw     : 0.0777

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 869.5631
  raw_gravity         : 869.5631
  domain_count        : 0
  infra_score_log     : 6.7691

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 17.9286
  hourly_freq         : 3.4286
  transit_freq_log    : 2.9407

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 10795.7632
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 13
  pop_val_log         : 2.6391
```
</details>
<details><summary><b>Paszport Węzła: KRAKÓW LOTNISKO (H3: 891e05b6a9bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : KRAKÓW LOTNISKO
  stop_id             : 235879
  city                : krakow
  h3_index            : 891e05b6a9bffff
  stop_lat            : 50.0709
  stop_lon            : 19.8014
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : pkp-kml

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : C
  local_percentile    : 52.7538
  local_score_raw     : -0.1853

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 673.0629
  raw_gravity         : 673.0629
  domain_count        : 0
  infra_score_log     : 6.5133

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 8.0000
  hourly_freq         : 4.0000
  transit_freq_log    : 2.1972

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 10795.7632
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 16
  pop_val_log         : 2.8332
```
</details>
<details><summary><b>Paszport Węzła: Rusocice Granica (H3: 891e05b0a0fffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Rusocice Granica
  stop_id             : stop_2196_340501
  city                : krakow
  h3_index            : 891e05b0a0fffff
  stop_lat            : 50.0049
  stop_lon            : 19.5882
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : krakow-bus

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : D
  local_percentile    : 44.8704
  local_score_raw     : -0.3122

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 574.8715
  raw_gravity         : 574.8715
  domain_count        : 0
  infra_score_log     : 6.3559

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 3.0000
  hourly_freq         : 1.5000
  transit_freq_log    : 1.3863

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 10795.7632
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 129
  pop_val_log         : 4.8675
```
</details>
<details><summary><b>Paszport Węzła: Cmentarz Bieżanów (H3: 891e2e69dc3ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Cmentarz Bieżanów
  stop_id             : stop_1641_312601
  city                : krakow
  h3_index            : 891e2e69dc3ffff
  stop_lat            : 50.0115
  stop_lon            : 20.0245
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : krakow-bus

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : B
  local_percentile    : 82.5594
  local_score_raw     : 0.8089

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 4801047.9095
  raw_gravity         : 4364589.0086
  domain_count        : 1
  infra_score_log     : 15.3843

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 3.1429
  hourly_freq         : 3.1429
  transit_freq_log    : 1.4214

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 10321.0260
  liquidity           : 18.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 1555
  pop_val_log         : 7.3499
```
</details>
<details><summary><b>Paszport Węzła: Smardzowice Remiza (H3: 891e2e784c3ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Smardzowice Remiza
  stop_id             : stop_2304_345401
  city                : krakow
  h3_index            : 891e2e784c3ffff
  stop_lat            : 50.1919
  stop_lon            : 19.8537
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : krakow-bus

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : C
  local_percentile    : 57.8834
  local_score_raw     : -0.0895

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 48442.1701
  raw_gravity         : 44038.3365
  domain_count        : 1
  infra_score_log     : 10.7881

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 1.7857
  hourly_freq         : 0.9286
  transit_freq_log    : 1.0245

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 10795.7632
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 32
  pop_val_log         : 3.4965
```
</details>

#### 💩 BOTTOM 5 (Najsłabsze 5 przystanków)
<details><summary><b>Paszport Węzła: Kępa Grabska (H3: 891e2e6f3dbffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Kępa Grabska
  stop_id             : 3313
  city                : krakow
  h3_index            : 891e2e6f3dbffff
  stop_lat            : 50.0491
  stop_lon            : 20.1557
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : krakow-mobilis

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.2700
  local_score_raw     : -1.3164

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 76.9881
  raw_gravity         : 76.9881
  domain_count        : 0
  infra_score_log     : 4.3566

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.2143
  hourly_freq         : 0.2143
  transit_freq_log    : 0.1942

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 10795.7632
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Balice Airport (H3: 891e05b4587ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Balice Airport
  stop_id             : STRATEGIC
  city                : krakow
  h3_index            : 891e05b4587ffff
  stop_lat            : nan
  stop_lon            : nan
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : STRATEGIC_HUB

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.2160
  local_score_raw     : -1.3181

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 144.4028
  raw_gravity         : 144.4028
  domain_count        : 0
  infra_score_log     : 4.9795

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.0000
  hourly_freq         : 0.0000
  transit_freq_log    : 0.0000

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 10795.7632
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Podolany (H3: 891e05a090bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Podolany
  stop_id             : 178077
  city                : krakow
  h3_index            : 891e05a090bffff
  stop_lat            : 49.8982
  stop_lon            : 19.7534
  lat_grid            : 49.9000
  lon_grid            : 19.7500
  norm_name           : podolany
  source              : polish_trains

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.1620
  local_score_raw     : -1.3389

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 117.8441
  raw_gravity         : 117.8441
  domain_count        : 0
  infra_score_log     : 4.7778

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.0000
  hourly_freq         : 0.0000
  transit_freq_log    : 0.0000

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 10795.7632
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Przeginia Duchowna Rezerwat (H3: 891e05b09b7ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Przeginia Duchowna Rezerwat
  stop_id             : stop_3296_388401
  city                : krakow
  h3_index            : 891e05b09b7ffff
  stop_lat            : 50.0344
  stop_lon            : 19.6462
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : krakow-bus

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.1080
  local_score_raw     : -1.3557

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 21.7659
  raw_gravity         : 21.7659
  domain_count        : 0
  infra_score_log     : 3.1253

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.5714
  hourly_freq         : 0.5714
  transit_freq_log    : 0.4520

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 10795.7632
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Balice Autostrada (H3: 891e05b6eafffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Balice Autostrada
  stop_id             : stop_169_22102
  city                : krakow
  h3_index            : 891e05b6eafffff
  stop_lat            : 50.0843
  stop_lon            : 19.8071
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : krakow-bus

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.0540
  local_score_raw     : -1.3722

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 18.3864
  raw_gravity         : 18.3864
  domain_count        : 0
  infra_score_log     : 2.9646

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.5714
  hourly_freq         : 0.5714
  transit_freq_log    : 0.4520

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 10795.7632
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>

---

## AGLOMERACJA: KUTNO
**Status:** ✅ SUKCES

### Faza 0: Stan Danych
- **Całkowita populacja w strefie miasta:** 47,419 (Baseline: 50,000) [✅ OK]
- **Ilość Transakcji RCN:** 533
- **Zakres Dat RCN:** 2023-08-25 do 2525-10-09
- **Ceny RCN (PLN/m²):** Średnia=6,281 | Mediana=6,345 | Max=48,145 | IQR=[4,686 - 7,207]
- **Infrastruktura OSM (Punkty):** 9,054
- **Infrastruktura OSM (Poligony/Budynki):** 15,714
- Baza transakcyjna `.gpkg` ustrukturyzowana poprawnie.

### Faza I & II: Pokrycie (Zero-Values)
- **Pustynia Populacyjna:** 44 (19.6%)
- **Pustynia Infrastrukturalna:** 0 (0.0%)
- **Głuche Przystanki:** 3 (1.3%)
- **Wskaźnik Fallback RCN:** 142 (63.4%) (Mediana RCN dla miasta: 6343)

### Faza III: Udowodnione POI w Promieniu 500m

**Rzeczywiste TOP 20 zwalidowanych obiektów (Intersekcja bufor 500m):**

| Tag OSM | Zliczone (Ilość) | Prawdziwa Waga JSON | Całkowita Siła (Score) |
|---|---|---|---|
| `supermarket` | 173 | 9,934,767.62 | **1,718,714,798.26** |
| `marketplace` | 22 | 1,565,679.42 | **34,444,947.24** |
| `sports_centre` | 22 | 1,092,229.03 | **24,029,038.66** |
| `pharmacy` | 229 | 51,226.09 | **11,730,774.61** |
| `bank` | 206 | 56,405.85 | **11,619,605.10** |
| `place_of_worship` | 132 | 83,289.81 | **10,994,254.92** |
| `post_office` | 35 | 66,321.78 | **2,321,262.30** |
| `bench` | 1424 | 0.00 | **0.00** |
| `parcel_locker` | 302 | 0.00 | **0.00** |
| `waste_basket` | 200 | 0.00 | **0.00** |
| `restaurant` | 173 | 0.00 | **0.00** |
| `atm` | 159 | 0.00 | **0.00** |
| `bicycle_parking` | 78 | 0.00 | **0.00** |
| `fuel` | 117 | 0.00 | **0.00** |
| `parking_entrance` | 51 | 0.00 | **0.00** |
| `cafe` | 68 | 0.00 | **0.00** |
| `drinking_water` | 48 | 0.00 | **0.00** |
| `veterinary` | 60 | 0.00 | **0.00** |
| `fast_food` | 71 | 0.00 | **0.00** |
| `fountain` | 76 | 0.00 | **0.00** |

### Faza IV: Badanie Próbek Oceny Złotej

#### 🏆 TOP 5 (Najlepsze 5 przystanków w mieście)
<details><summary><b>Paszport Węzła: Grunwaldzka (H3: 891f52c8a77ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Grunwaldzka
  stop_id             : 16
  city                : kutno
  h3_index            : 891f52c8a77ffff
  stop_lat            : 52.2288
  stop_lon            : 19.3717
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : kutno

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 1.8753

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 15344402.7991
  raw_gravity         : 11803386.7685
  domain_count        : 3
  infra_score_log     : 16.5463

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 13.0714
  hourly_freq         : 6.3571
  transit_freq_log    : 2.6441

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6343.4992
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 1143
  pop_val_log         : 7.0423
```
</details>
<details><summary><b>Paszport Węzła: Grunwaldzka (H3: 891f52c8a77ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Grunwaldzka
  stop_id             : 32
  city                : kutno
  h3_index            : 891f52c8a77ffff
  stop_lat            : 52.2288
  stop_lon            : 19.3727
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : kutno

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 1.8753

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 15344402.7991
  raw_gravity         : 11803386.7685
  domain_count        : 3
  infra_score_log     : 16.5463

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 13.0714
  hourly_freq         : 6.7143
  transit_freq_log    : 2.6441

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6343.4992
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 1143
  pop_val_log         : 7.0423
```
</details>
<details><summary><b>Paszport Węzła: Tarnowskiego (H3: 891f52c8a9bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Tarnowskiego
  stop_id             : 23
  city                : kutno
  h3_index            : 891f52c8a9bffff
  stop_lat            : 52.2420
  stop_lon            : 19.3584
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : kutno

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 99.1597
  local_score_raw     : 1.7071

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 12389300.6699
  raw_gravity         : 9530231.2845
  domain_count        : 3
  infra_score_log     : 16.3323

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 10.2857
  hourly_freq         : 5.3571
  transit_freq_log    : 2.4235

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 5980.5906
  liquidity           : 8.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 1471
  pop_val_log         : 7.2944
```
</details>
<details><summary><b>Paszport Węzła: Tarnowskiego (H3: 891f52c8a9bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Tarnowskiego
  stop_id             : 10
  city                : kutno
  h3_index            : 891f52c8a9bffff
  stop_lat            : 52.2425
  stop_lon            : 19.3591
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : kutno

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 99.1597
  local_score_raw     : 1.7071

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 12389300.6699
  raw_gravity         : 9530231.2845
  domain_count        : 3
  infra_score_log     : 16.3323

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 10.2857
  hourly_freq         : 4.9286
  transit_freq_log    : 2.4235

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 5980.5906
  liquidity           : 8.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 1471
  pop_val_log         : 7.2944
```
</details>
<details><summary><b>Paszport Węzła: Wyszyńskiego (H3: 891f52c8a73ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Wyszyńskiego
  stop_id             : 15
  city                : kutno
  h3_index            : 891f52c8a73ffff
  stop_lat            : 52.2300
  stop_lon            : 19.3663
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : kutno

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 98.3193
  local_score_raw     : 1.6443

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 6208741.9567
  raw_gravity         : 5173951.6306
  domain_count        : 2
  infra_score_log     : 15.6415

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 16.2857
  hourly_freq         : 7.8571
  transit_freq_log    : 2.8499

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 4564.3154
  liquidity           : 9.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 801
  pop_val_log         : 6.6871
```
</details>

#### 🎲 RANDOM 5 (Środkowe przystanki miasta)
<details><summary><b>Paszport Węzła: Kościuszki / Aquapark (H3: 891f52c8847ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Kościuszki / Aquapark
  stop_id             : 226
  city                : kutno
  h3_index            : 891f52c8847ffff
  stop_lat            : 52.2462
  stop_lon            : 19.3783
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : kutno

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : D
  local_percentile    : 42.0168
  local_score_raw     : -0.3513

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 234.5099
  raw_gravity         : 234.5099
  domain_count        : 0
  infra_score_log     : 5.4618

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 1.7143
  hourly_freq         : 1.7143
  transit_freq_log    : 0.9985

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6343.4992
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 11
  pop_val_log         : 2.4849
```
</details>
<details><summary><b>Paszport Węzła: Jesienna (H3: 891f52c830fffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Jesienna
  stop_id             : 502
  city                : kutno
  h3_index            : 891f52c830fffff
  stop_lat            : 52.2485
  stop_lon            : 19.3168
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : kutno

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : C
  local_percentile    : 56.3025
  local_score_raw     : -0.0571

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 338.4186
  raw_gravity         : 338.4186
  domain_count        : 0
  infra_score_log     : 5.8272

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 2.2857
  hourly_freq         : 1.1429
  transit_freq_log    : 1.1896

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6565.5963
  liquidity           : 5.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 91
  pop_val_log         : 4.5218
```
</details>
<details><summary><b>Paszport Węzła: Raszewska / Zimowa (H3: 891f52c9dc3ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Raszewska / Zimowa
  stop_id             : 543
  city                : kutno
  h3_index            : 891f52c9dc3ffff
  stop_lat            : 52.2374
  stop_lon            : 19.3176
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : kutno

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : D
  local_percentile    : 38.6555
  local_score_raw     : -0.3923

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 494.9191
  raw_gravity         : 494.9191
  domain_count        : 0
  infra_score_log     : 6.2064

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.9286
  hourly_freq         : 0.9286
  transit_freq_log    : 0.6568

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6343.4992
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 34
  pop_val_log         : 3.5553
```
</details>
<details><summary><b>Paszport Węzła: Skłodowskiej / Północna (H3: 891f52c8e63ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Skłodowskiej / Północna
  stop_id             : 142
  city                : kutno
  h3_index            : 891f52c8e63ffff
  stop_lat            : 52.2439
  stop_lon            : 19.3518
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : kutno

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : B
  local_percentile    : 78.1513
  local_score_raw     : 0.5051

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 922.9300
  raw_gravity         : 922.9300
  domain_count        : 0
  infra_score_log     : 6.8286

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 6.7143
  hourly_freq         : 1.8571
  transit_freq_log    : 2.0431

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 5723.1229
  liquidity           : 2.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 645
  pop_val_log         : 6.4708
```
</details>
<details><summary><b>Paszport Węzła: Metalowa / Sklęczkowska (H3: 891f52524abffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Metalowa / Sklęczkowska
  stop_id             : 368
  city                : kutno
  h3_index            : 891f52524abffff
  stop_lat            : 52.2190
  stop_lon            : 19.3938
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : kutno

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : C
  local_percentile    : 68.0672
  local_score_raw     : 0.2298

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 325.6006
  raw_gravity         : 325.6006
  domain_count        : 0
  infra_score_log     : 5.7887

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 4.5000
  hourly_freq         : 0.4286
  transit_freq_log    : 1.7047

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6343.4992
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 192
  pop_val_log         : 5.2627
```
</details>

#### 💩 BOTTOM 5 (Najsłabsze 5 przystanków)
<details><summary><b>Paszport Węzła: Stalowa / Pętla (H3: 891f5252527ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Stalowa / Pętla
  stop_id             : 687
  city                : kutno
  h3_index            : 891f5252527ffff
  stop_lat            : 52.2160
  stop_lon            : 19.4361
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : kutno

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 3.3613
  local_score_raw     : -0.8807

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 31.3648
  raw_gravity         : 31.3648
  domain_count        : 0
  infra_score_log     : 3.4771

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.9286
  hourly_freq         : 0.4286
  transit_freq_log    : 0.6568

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6343.4992
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Stalowa / Pętla (H3: 891f5252527ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Stalowa / Pętla
  stop_id             : 688
  city                : kutno
  h3_index            : 891f5252527ffff
  stop_lat            : 52.2160
  stop_lon            : 19.4361
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : kutno

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 3.3613
  local_score_raw     : -0.8807

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 31.3648
  raw_gravity         : 31.3648
  domain_count        : 0
  infra_score_log     : 3.4771

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.9286
  hourly_freq         : 0.5000
  transit_freq_log    : 0.6568

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6343.4992
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Kutno Azory (H3: 891f52c9ca3ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Kutno Azory
  stop_id             : 32326
  city                : kutno
  h3_index            : 891f52c9ca3ffff
  stop_lat            : 52.2400
  stop_lon            : 19.3040
  lat_grid            : 52.2400
  lon_grid            : 19.3000
  norm_name           : kutnoazory
  source              : polish_trains

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 2.5210
  local_score_raw     : -0.9261

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 741.3718
  raw_gravity         : 741.3718
  domain_count        : 0
  infra_score_log     : 6.6099

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.0000
  hourly_freq         : 0.0000
  transit_freq_log    : 0.0000

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6343.4992
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Metalowa / Sklęczkowska (H3: 891f5252433ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Metalowa / Sklęczkowska
  stop_id             : 367
  city                : kutno
  h3_index            : 891f5252433ffff
  stop_lat            : 52.2190
  stop_lon            : 19.3938
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : kutno

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 1.6807
  local_score_raw     : -1.0463

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 38.8702
  raw_gravity         : 38.8702
  domain_count        : 0
  infra_score_log     : 3.6856

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.3571
  hourly_freq         : 0.3571
  transit_freq_log    : 0.3054

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6343.4992
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Sklęczki (H3: 891f52c8b6fffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Sklęczki
  stop_id             : 32441
  city                : kutno
  h3_index            : 891f52c8b6fffff
  stop_lat            : 52.2254
  stop_lon            : 19.4056
  lat_grid            : 52.2300
  lon_grid            : 19.4100
  norm_name           : skleczki
  source              : polish_trains

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.8403
  local_score_raw     : -1.0488

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 206.7133
  raw_gravity         : 206.7133
  domain_count        : 0
  infra_score_log     : 5.3362

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.0000
  hourly_freq         : 0.0000
  transit_freq_log    : 0.0000

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6343.4992
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>

---

## AGLOMERACJA: LEGNICA
**Status:** ✅ SUKCES

### Faza 0: Stan Danych
- **Całkowita populacja w strefie miasta:** 115,261 (Baseline: 90,000) [✅ OK]
- **Ilość Transakcji RCN:** 17,704
- **Zakres Dat RCN:** 2020-01-02 do 2026-02-27
- **Ceny RCN (PLN/m²):** Średnia=5,741 | Mediana=4,929 | Max=302,000 | IQR=[3,609 - 6,322]
- **Infrastruktura OSM (Punkty):** 15,108
- **Infrastruktura OSM (Poligony/Budynki):** 32,598
- Baza transakcyjna `.gpkg` ustrukturyzowana poprawnie.

### Faza I & II: Pokrycie (Zero-Values)
- **Pustynia Populacyjna:** 41 (11.6%)
- **Pustynia Infrastrukturalna:** 0 (0.0%)
- **Głuche Przystanki:** 6 (1.7%)
- **Wskaźnik Fallback RCN:** 151 (42.8%) (Mediana RCN dla miasta: 4868)

### Faza III: Udowodnione POI w Promieniu 500m

**Rzeczywiste TOP 20 zwalidowanych obiektów (Intersekcja bufor 500m):**

| Tag OSM | Zliczone (Ilość) | Prawdziwa Waga JSON | Całkowita Siła (Score) |
|---|---|---|---|
| `supermarket` | 301 | 9,092,765.40 | **2,736,922,385.40** |
| `place_of_worship` | 351 | 86,806.63 | **30,469,127.13** |
| `marketplace` | 20 | 1,287,981.48 | **25,759,629.60** |
| `pharmacy` | 415 | 56,074.70 | **23,271,000.50** |
| `sports_centre` | 18 | 1,052,665.73 | **18,947,983.14** |
| `bank` | 219 | 56,615.51 | **12,398,796.69** |
| `post_office` | 186 | 61,834.15 | **11,501,151.90** |
| `bench` | 2173 | 0.00 | **0.00** |
| `bicycle_parking` | 971 | 0.00 | **0.00** |
| `parcel_locker` | 622 | 0.00 | **0.00** |
| `recycling` | 562 | 0.00 | **0.00** |
| `grit_bin` | 446 | 0.00 | **0.00** |
| `parking_space` | 3384 | 0.00 | **0.00** |
| `restaurant` | 444 | 0.00 | **0.00** |
| `vending_machine` | 430 | 0.00 | **0.00** |
| `fast_food` | 271 | 0.00 | **0.00** |
| `parking` | 3515 | 0.00 | **0.00** |
| `shelter` | 362 | 0.00 | **0.00** |
| `library` | 163 | 0.00 | **0.00** |
| `school` | 383 | 0.00 | **0.00** |

### Faza IV: Badanie Próbek Oceny Złotej

#### 🏆 TOP 5 (Najlepsze 5 przystanków w mieście)
<details><summary><b>Paszport Węzła: Piastowska - M. Skłodowskiej (H3: 891e2638c23ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Piastowska - M. Skłodowskiej
  stop_id             : 1785
  city                : legnica
  h3_index            : 891e2638c23ffff
  stop_lat            : 51.2111
  stop_lon            : 16.1594
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : legnica

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 2.1402

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 5981861.9430
  raw_gravity         : 4984884.9525
  domain_count        : 2
  infra_score_log     : 15.6042

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 14.5714
  hourly_freq         : 7.1429
  transit_freq_log    : 2.7454

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 10463.4941
  liquidity           : 85.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 629
  pop_val_log         : 6.4457
```
</details>
<details><summary><b>Paszport Węzła: Piastowska - Rycerska (H3: 891e2638c23ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Piastowska - Rycerska
  stop_id             : 1786
  city                : legnica
  h3_index            : 891e2638c23ffff
  stop_lat            : 51.2112
  stop_lon            : 16.1592
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : legnica

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 2.1402

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 5981861.9430
  raw_gravity         : 4984884.9525
  domain_count        : 2
  infra_score_log     : 15.6042

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 14.5714
  hourly_freq         : 7.4286
  transit_freq_log    : 2.7454

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 10463.4941
  liquidity           : 85.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 629
  pop_val_log         : 6.4457
```
</details>
<details><summary><b>Paszport Węzła: Piłsudskiego - Heweliusza (H3: 891e2638d63ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Piłsudskiego - Heweliusza
  stop_id             : 1790
  city                : legnica
  h3_index            : 891e2638d63ffff
  stop_lat            : 51.2053
  stop_lon            : 16.1865
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : legnica

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 99.5098
  local_score_raw     : 1.9059

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 10647536.5717
  raw_gravity         : 8872947.1431
  domain_count        : 2
  infra_score_log     : 16.1808

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 30.2143
  hourly_freq         : 15.0714
  transit_freq_log    : 3.4409

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 5533.8399
  liquidity           : 68.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 2033
  pop_val_log         : 7.6178
```
</details>
<details><summary><b>Paszport Węzła: Piłsudskiego - Galaktyczna (H3: 891e2638d63ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Piłsudskiego - Galaktyczna
  stop_id             : 1799
  city                : legnica
  h3_index            : 891e2638d63ffff
  stop_lat            : 51.2058
  stop_lon            : 16.1854
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : legnica

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 99.5098
  local_score_raw     : 1.9059

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 10647536.5717
  raw_gravity         : 8872947.1431
  domain_count        : 2
  infra_score_log     : 16.1808

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 30.2143
  hourly_freq         : 15.1429
  transit_freq_log    : 3.4409

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 5533.8399
  liquidity           : 68.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 2033
  pop_val_log         : 7.6178
```
</details>
<details><summary><b>Paszport Węzła: Sikorskiego - Śląska (H3: 891e26389afffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Sikorskiego - Śląska
  stop_id             : 1852
  city                : legnica
  h3_index            : 891e26389afffff
  stop_lat            : 51.2004
  stop_lon            : 16.2121
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : legnica

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 99.0196
  local_score_raw     : 1.7859

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 14748686.4607
  raw_gravity         : 11345143.4313
  domain_count        : 3
  infra_score_log     : 16.5067

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 13.2857
  hourly_freq         : 7.7143
  transit_freq_log    : 2.6593

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6710.8168
  liquidity           : 39.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 1558
  pop_val_log         : 7.3518
```
</details>

#### 🎲 RANDOM 5 (Środkowe przystanki miasta)
<details><summary><b>Paszport Węzła: Rzeczypospolitej - Świerkowa (H3: 891e26388afffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Rzeczypospolitej - Świerkowa
  stop_id             : 1813
  city                : legnica
  h3_index            : 891e26388afffff
  stop_lat            : 51.1978
  stop_lon            : 16.1789
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : legnica

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : B
  local_percentile    : 75.4902
  local_score_raw     : 0.5723

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 27976.6980
  raw_gravity         : 25433.3618
  domain_count        : 1
  infra_score_log     : 10.2392

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 4.7143
  hourly_freq         : 4.7143
  transit_freq_log    : 1.7430

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 5144.5087
  liquidity           : 59.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 436
  pop_val_log         : 6.0799
```
</details>
<details><summary><b>Paszport Węzła: Szczytniki Nad Kaczawą - Świetlica (H3: 891e26226a7ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Szczytniki Nad Kaczawą - Świetlica
  stop_id             : 2044
  city                : legnica
  h3_index            : 891e26226a7ffff
  stop_lat            : 51.2749
  stop_lon            : 16.2860
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : legnica

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : D
  local_percentile    : 37.2549
  local_score_raw     : -0.4411

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 369.3748
  raw_gravity         : 369.3748
  domain_count        : 0
  infra_score_log     : 5.9145

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.8571
  hourly_freq         : 0.4286
  transit_freq_log    : 0.6190

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 4868.4211
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 39
  pop_val_log         : 3.6889
```
</details>
<details><summary><b>Paszport Węzła: Rzeszotary - Szkoła (H3: 891e263a9dbffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Rzeszotary - Szkoła
  stop_id             : 2069
  city                : legnica
  h3_index            : 891e263a9dbffff
  stop_lat            : 51.2504
  stop_lon            : 16.1628
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : legnica

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : D
  local_percentile    : 46.5686
  local_score_raw     : -0.3521

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 52630.9164
  raw_gravity         : 52630.9164
  domain_count        : 0
  infra_score_log     : 10.8711

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.5714
  hourly_freq         : 0.2857
  transit_freq_log    : 0.4520

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 2107.1115
  liquidity           : 1.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 51
  pop_val_log         : 3.9512
```
</details>
<details><summary><b>Paszport Węzła: Sudecka - Armii Krajowej (H3: 891e26214c3ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Sudecka - Armii Krajowej
  stop_id             : 1841
  city                : legnica
  h3_index            : 891e26214c3ffff
  stop_lat            : 51.2013
  stop_lon            : 16.2232
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : legnica

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : C
  local_percentile    : 64.2157
  local_score_raw     : 0.1430

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 972.3740
  raw_gravity         : 972.3740
  domain_count        : 0
  infra_score_log     : 6.8808

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 4.1429
  hourly_freq         : 2.0714
  transit_freq_log    : 1.6376

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 4575.4717
  liquidity           : 1.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 460
  pop_val_log         : 6.1334
```
</details>
<details><summary><b>Paszport Węzła: Domejki - MPK (H3: 891e2638127ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Domejki - MPK
  stop_id             : 1711
  city                : legnica
  h3_index            : 891e2638127ffff
  stop_lat            : 51.2088
  stop_lon            : 16.1303
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : legnica

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : C
  local_percentile    : 68.6275
  local_score_raw     : 0.2935

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 348.2182
  raw_gravity         : 348.2182
  domain_count        : 0
  infra_score_log     : 5.8557

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 27.5714
  hourly_freq         : 8.5714
  transit_freq_log    : 3.3524

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 4868.4211
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>

#### 💩 BOTTOM 5 (Najsłabsze 5 przystanków)
<details><summary><b>Paszport Węzła: Legnica Strefa (H3: 891e262a4a7ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Legnica Strefa
  stop_id             : 279503
  city                : legnica
  h3_index            : 891e262a4a7ffff
  stop_lat            : 51.1654
  stop_lon            : 16.1854
  lat_grid            : 51.1700
  lon_grid            : 16.1900
  norm_name           : legnicastrefa
  source              : polish_trains

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 1.9608
  local_score_raw     : -0.9819

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 169.3685
  raw_gravity         : 169.3685
  domain_count        : 0
  infra_score_log     : 5.1380

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.0000
  hourly_freq         : 0.0000
  transit_freq_log    : 0.0000

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 4868.4211
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Cmentarz - Jaszków (H3: 891e263817bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Cmentarz - Jaszków
  stop_id             : 1985
  city                : legnica
  h3_index            : 891e263817bffff
  stop_lat            : 51.2037
  stop_lon            : 16.1123
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : legnica

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 1.4706
  local_score_raw     : -1.0119

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 123.8081
  raw_gravity         : 123.8081
  domain_count        : 0
  infra_score_log     : 4.8268

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.0000
  hourly_freq         : 0.0000
  transit_freq_log    : 0.0000

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 4868.4211
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Koskowice - Cmentarz (H3: 891e2621007ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Koskowice - Cmentarz
  stop_id             : 2095
  city                : legnica
  h3_index            : 891e2621007ffff
  stop_lat            : 51.1812
  stop_lon            : 16.2591
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : legnica

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.9804
  local_score_raw     : -1.0382

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 165.5721
  raw_gravity         : 165.5721
  domain_count        : 0
  infra_score_log     : 5.1154

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.3571
  hourly_freq         : 0.3571
  transit_freq_log    : 0.3054

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 2463.2930
  liquidity           : 2.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 7
  pop_val_log         : 2.0794
```
</details>
<details><summary><b>Paszport Węzła: Szczedrzykowice - Stacja (H3: 891e2620147ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Szczedrzykowice - Stacja
  stop_id             : 2055
  city                : legnica
  h3_index            : 891e2620147ffff
  stop_lat            : 51.2162
  stop_lon            : 16.3534
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : legnica

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.4902
  local_score_raw     : -1.0850

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 354.6059
  raw_gravity         : 354.6059
  domain_count        : 0
  infra_score_log     : 5.8738

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.1429
  hourly_freq         : 0.0714
  transit_freq_log    : 0.1335

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 1090.6040
  liquidity           : 1.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 44
  pop_val_log         : 3.8067
```
</details>
<details><summary><b>Paszport Węzła: Szczedrzykowice - Stacja (H3: 891e2620147ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Szczedrzykowice - Stacja
  stop_id             : 2054
  city                : legnica
  h3_index            : 891e2620147ffff
  stop_lat            : 51.2162
  stop_lon            : 16.3535
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : legnica

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.4902
  local_score_raw     : -1.0850

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 354.6059
  raw_gravity         : 354.6059
  domain_count        : 0
  infra_score_log     : 5.8738

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.1429
  hourly_freq         : 0.0714
  transit_freq_log    : 0.1335

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 1090.6040
  liquidity           : 1.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 44
  pop_val_log         : 3.8067
```
</details>

---

## AGLOMERACJA: LESZNO
**Status:** ✅ SUKCES

### Faza 0: Stan Danych
- **Całkowita populacja w strefie miasta:** 81,945 (Baseline: 50,000) [✅ OK]
- **Ilość Transakcji RCN:** 3,695
- **Zakres Dat RCN:** 2020-01-07 do 2026-01-28
- **Ceny RCN (PLN/m²):** Średnia=8,563 | Mediana=5,145 | Max=387,755 | IQR=[3,686 - 7,469]
- **Infrastruktura OSM (Punkty):** 14,823
- **Infrastruktura OSM (Poligony/Budynki):** 32,544
- Baza transakcyjna `.gpkg` ustrukturyzowana poprawnie.

### Faza I & II: Pokrycie (Zero-Values)
- **Pustynia Populacyjna:** 23 (8.8%)
- **Pustynia Infrastrukturalna:** 0 (0.0%)
- **Głuche Przystanki:** 2 (0.8%)
- **Wskaźnik Fallback RCN:** 137 (52.5%) (Mediana RCN dla miasta: 5092)

### Faza III: Udowodnione POI w Promieniu 500m

**Rzeczywiste TOP 20 zwalidowanych obiektów (Intersekcja bufor 500m):**

| Tag OSM | Zliczone (Ilość) | Prawdziwa Waga JSON | Całkowita Siła (Score) |
|---|---|---|---|
| `supermarket` | 335 | 8,272,730.67 | **2,771,364,774.45** |
| `sports_centre` | 92 | 871,951.92 | **80,219,576.64** |
| `marketplace` | 22 | 1,268,369.97 | **27,904,139.34** |
| `bank` | 372 | 59,160.76 | **22,007,802.72** |
| `pharmacy` | 324 | 54,394.70 | **17,623,882.80** |
| `place_of_worship` | 154 | 90,700.06 | **13,967,809.24** |
| `post_office` | 175 | 55,047.97 | **9,633,394.75** |
| `bench` | 2465 | 0.00 | **0.00** |
| `parking` | 4568 | 0.00 | **0.00** |
| `restaurant` | 578 | 0.00 | **0.00** |
| `parcel_locker` | 443 | 0.00 | **0.00** |
| `atm` | 356 | 0.00 | **0.00** |
| `bicycle_parking` | 301 | 0.00 | **0.00** |
| `doctors` | 305 | 0.00 | **0.00** |
| `waste_disposal` | 221 | 0.00 | **0.00** |
| `college` | 213 | 0.00 | **0.00** |
| `cafe` | 164 | 0.00 | **0.00** |
| `kindergarten` | 328 | 0.00 | **0.00** |
| `bureau_de_change` | 155 | 0.00 | **0.00** |
| `ice_cream` | 158 | 0.00 | **0.00** |

### Faza IV: Badanie Próbek Oceny Złotej

#### 🏆 TOP 5 (Najlepsze 5 przystanków w mieście)
<details><summary><b>Paszport Węzła: Klonowicza (H3: 891e2463203ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Klonowicza
  stop_id             : 276
  city                : leszno
  h3_index            : 891e2463203ffff
  stop_lat            : 51.8420
  stop_lon            : 16.5686
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : leszno

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 1.8487

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 1306648.6151
  raw_gravity         : 1005114.3193
  domain_count        : 3
  infra_score_log     : 14.0830

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 12.0000
  hourly_freq         : 1.8571
  transit_freq_log    : 2.5649

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 8710.8014
  liquidity           : 47.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 832
  pop_val_log         : 6.7250
```
</details>
<details><summary><b>Paszport Węzła: Krasińskiego (H3: 891e2463203ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Krasińskiego
  stop_id             : 81
  city                : leszno
  h3_index            : 891e2463203ffff
  stop_lat            : 51.8420
  stop_lon            : 16.5706
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : leszno

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 1.8487

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 1306648.6151
  raw_gravity         : 1005114.3193
  domain_count        : 3
  infra_score_log     : 14.0830

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 12.0000
  hourly_freq         : 4.1429
  transit_freq_log    : 2.5649

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 8710.8014
  liquidity           : 47.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 832
  pop_val_log         : 6.7250
```
</details>
<details><summary><b>Paszport Węzła: Klonowicza (H3: 891e2463203ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Klonowicza
  stop_id             : 175
  city                : leszno
  h3_index            : 891e2463203ffff
  stop_lat            : 51.8420
  stop_lon            : 16.5685
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : leszno

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 1.8487

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 1306648.6151
  raw_gravity         : 1005114.3193
  domain_count        : 3
  infra_score_log     : 14.0830

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 12.0000
  hourly_freq         : 1.9286
  transit_freq_log    : 2.5649

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 8710.8014
  liquidity           : 47.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 832
  pop_val_log         : 6.7250
```
</details>
<details><summary><b>Paszport Węzła: Krasińskiego (H3: 891e2463203ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Krasińskiego
  stop_id             : 108
  city                : leszno
  h3_index            : 891e2463203ffff
  stop_lat            : 51.8427
  stop_lon            : 16.5709
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : leszno

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 1.8487

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 1306648.6151
  raw_gravity         : 1005114.3193
  domain_count        : 3
  infra_score_log     : 14.0830

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 12.0000
  hourly_freq         : 4.0714
  transit_freq_log    : 2.5649

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 8710.8014
  liquidity           : 47.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 832
  pop_val_log         : 6.7250
```
</details>
<details><summary><b>Paszport Węzła: Gronowska MEIBES (H3: 891e24630d7ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Gronowska MEIBES
  stop_id             : 39
  city                : leszno
  h3_index            : 891e24630d7ffff
  stop_lat            : 51.8633
  stop_lon            : 16.5763
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : leszno

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 99.3151
  local_score_raw     : 1.5233

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 6112508.3809
  raw_gravity         : 5093756.9841
  domain_count        : 2
  infra_score_log     : 15.6258

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 5.9286
  hourly_freq         : 2.8571
  transit_freq_log    : 1.9357

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 8195.0026
  liquidity           : 125.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 485
  pop_val_log         : 6.1862
```
</details>

#### 🎲 RANDOM 5 (Środkowe przystanki miasta)
<details><summary><b>Paszport Węzła: Spółdzielcza II (H3: 891e246362bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Spółdzielcza II
  stop_id             : 85
  city                : leszno
  h3_index            : 891e246362bffff
  stop_lat            : 51.8542
  stop_lon            : 16.5633
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : leszno

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : C
  local_percentile    : 50.6849
  local_score_raw     : -0.1211

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 473.4232
  raw_gravity         : 473.4232
  domain_count        : 0
  infra_score_log     : 6.1621

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 3.0714
  hourly_freq         : 1.5714
  transit_freq_log    : 1.4040

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 5092.0091
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 55
  pop_val_log         : 4.0254
```
</details>
<details><summary><b>Paszport Węzła: Krasińskiego ZUS (H3: 891e246328fffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Krasińskiego ZUS
  stop_id             : 129
  city                : leszno
  h3_index            : 891e246328fffff
  stop_lat            : 51.8466
  stop_lon            : 16.5704
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : leszno

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : C
  local_percentile    : 61.6438
  local_score_raw     : 0.1330

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 1067.9265
  raw_gravity         : 1067.9265
  domain_count        : 0
  infra_score_log     : 6.9744

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 4.8571
  hourly_freq         : 2.3571
  transit_freq_log    : 1.7677

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 3713.5279
  liquidity           : 1.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 246
  pop_val_log         : 5.5094
```
</details>
<details><summary><b>Paszport Węzła: Lipowa MPWiK (H3: 891e246149bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Lipowa MPWiK
  stop_id             : 31
  city                : leszno
  h3_index            : 891e246149bffff
  stop_lat            : 51.8329
  stop_lon            : 16.5787
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : leszno

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : C
  local_percentile    : 56.8493
  local_score_raw     : 0.0716

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 1271.3591
  raw_gravity         : 1271.3591
  domain_count        : 0
  infra_score_log     : 7.1486

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 2.9286
  hourly_freq         : 1.3571
  transit_freq_log    : 1.3683

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 5092.0091
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 307
  pop_val_log         : 5.7301
```
</details>
<details><summary><b>Paszport Węzła: 1 Maja MPWiK (H3: 891e24614cfffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : 1 Maja MPWiK
  stop_id             : 29
  city                : leszno
  h3_index            : 891e24614cfffff
  stop_lat            : 51.8250
  stop_lon            : 16.5807
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : leszno

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : C
  local_percentile    : 59.5890
  local_score_raw     : 0.0815

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 830.1407
  raw_gravity         : 830.1407
  domain_count        : 0
  infra_score_log     : 6.7228

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 3.7143
  hourly_freq         : 1.8571
  transit_freq_log    : 1.5506

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 5092.0091
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 136
  pop_val_log         : 4.9200
```
</details>
<details><summary><b>Paszport Węzła: 17 Stycznia stadion (H3: 891e2461497ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : 17 Stycznia stadion
  stop_id             : 198
  city                : leszno
  h3_index            : 891e2461497ffff
  stop_lat            : 51.8348
  stop_lon            : 16.5863
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : leszno

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : D
  local_percentile    : 43.8356
  local_score_raw     : -0.1925

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 1089.6686
  raw_gravity         : 1089.6686
  domain_count        : 0
  infra_score_log     : 6.9945

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 2.0000
  hourly_freq         : 2.0000
  transit_freq_log    : 1.0986

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 5092.0091
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 88
  pop_val_log         : 4.4886
```
</details>

#### 💩 BOTTOM 5 (Najsłabsze 5 przystanków)
<details><summary><b>Paszport Węzła: Klonówiec pętla (H3: 891e247182fffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Klonówiec pętla
  stop_id             : 289
  city                : leszno
  h3_index            : 891e247182fffff
  stop_lat            : 51.9065
  stop_lon            : 16.5840
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : leszno

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 3.4247
  local_score_raw     : -1.3351

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 184.6656
  raw_gravity         : 184.6656
  domain_count        : 0
  infra_score_log     : 5.2239

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.2857
  hourly_freq         : 0.2857
  transit_freq_log    : 0.2513

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 1510.5740
  liquidity           : 1.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 18
  pop_val_log         : 2.9444
```
</details>
<details><summary><b>Paszport Węzła: Kosmonautów (H3: 891e2478dcfffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Kosmonautów
  stop_id             : 162
  city                : leszno
  h3_index            : 891e2478dcfffff
  stop_lat            : 51.8416
  stop_lon            : 16.5265
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : leszno

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 2.7397
  local_score_raw     : -1.3431

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 65.3465
  raw_gravity         : 65.3465
  domain_count        : 0
  infra_score_log     : 4.1949

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.1429
  hourly_freq         : 0.1429
  transit_freq_log    : 0.1335

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 5092.0091
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Wilkowice (H3: 891e2471a4fffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Wilkowice
  stop_id             : 42952
  city                : leszno
  h3_index            : 891e2471a4fffff
  stop_lat            : 51.8868
  stop_lon            : 16.5412
  lat_grid            : 51.8900
  lon_grid            : 16.5400
  norm_name           : wilkowice
  source              : polish_trains

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 2.0548
  local_score_raw     : -1.3687

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 199.7905
  raw_gravity         : 199.7905
  domain_count        : 0
  infra_score_log     : 5.3023

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.0000
  hourly_freq         : 0.0000
  transit_freq_log    : 0.0000

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 2099.7296
  liquidity           : 6.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 35
  pop_val_log         : 3.5835
```
</details>
<details><summary><b>Paszport Węzła: Kosmonautów (H3: 891e2478dc7ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Kosmonautów
  stop_id             : 160
  city                : leszno
  h3_index            : 891e2478dc7ffff
  stop_lat            : 51.8419
  stop_lon            : 16.5261
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : leszno

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 1.3699
  local_score_raw     : -1.4808

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 13.3712
  raw_gravity         : 13.3712
  domain_count        : 0
  infra_score_log     : 2.6652

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.1429
  hourly_freq         : 0.1429
  transit_freq_log    : 0.1335

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 5092.0091
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Dożynkowa II (H3: 891e24789b7ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Dożynkowa II
  stop_id             : 140
  city                : leszno
  h3_index            : 891e24789b7ffff
  stop_lat            : 51.8331
  stop_lon            : 16.5668
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : leszno

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.6849
  local_score_raw     : -1.5149

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 8.8405
  raw_gravity         : 8.8405
  domain_count        : 0
  infra_score_log     : 2.2865

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.1429
  hourly_freq         : 0.1429
  transit_freq_log    : 0.1335

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 5092.0091
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>

---

## AGLOMERACJA: LODZ
**Status:** ✅ SUKCES

### Faza 0: Stan Danych
- **Całkowita populacja w strefie miasta:** 1,041,306 (Baseline: 670,000) [✅ OK]
- **Ilość Transakcji RCN:** 9,351
- **Zakres Dat RCN:** 2020-01-02 do 2026-03-04
- **Ceny RCN (PLN/m²):** Średnia=7,030 | Mediana=5,594 | Max=425,735 | IQR=[4,257 - 7,217]
- **Infrastruktura OSM (Punkty):** 212,817
- **Infrastruktura OSM (Poligony/Budynki):** 378,838
- Baza transakcyjna `.gpkg` ustrukturyzowana poprawnie.

### Faza I & II: Pokrycie (Zero-Values)
- **Pustynia Populacyjna:** 309 (10.6%)
- **Pustynia Infrastrukturalna:** 0 (0.0%)
- **Głuche Przystanki:** 129 (4.4%)
- **Wskaźnik Fallback RCN:** 2243 (76.7%) (Mediana RCN dla miasta: 5571)

### Faza III: Udowodnione POI w Promieniu 500m

**Rzeczywiste TOP 20 zwalidowanych obiektów (Intersekcja bufor 500m):**

| Tag OSM | Zliczone (Ilość) | Prawdziwa Waga JSON | Całkowita Siła (Score) |
|---|---|---|---|
| `supermarket` | 2833 | 11,887,365.98 | **33,676,907,821.34** |
| `sports_centre` | 1268 | 1,233,043.60 | **1,563,499,284.80** |
| `marketplace` | 461 | 1,517,153.85 | **699,407,924.85** |
| `pharmacy` | 4351 | 67,234.54 | **292,537,483.54** |
| `place_of_worship` | 1914 | 115,157.75 | **220,411,933.50** |
| `bank` | 2322 | 72,977.39 | **169,453,499.58** |
| `post_office` | 1192 | 77,152.26 | **91,965,493.92** |
| `bench` | 97866 | 0.00 | **0.00** |
| `bicycle_parking` | 50300 | 0.00 | **0.00** |
| `waste_basket` | 18252 | 0.00 | **0.00** |
| `shelter` | 12888 | 0.00 | **0.00** |
| `parcel_locker` | 8535 | 0.00 | **0.00** |
| `restaurant` | 7092 | 0.00 | **0.00** |
| `parking_entrance` | 5179 | 0.00 | **0.00** |
| `atm` | 4288 | 0.00 | **0.00** |
| `recycling` | 4289 | 0.00 | **0.00** |
| `vending_machine` | 2146 | 0.00 | **0.00** |
| `fast_food` | 2552 | 0.00 | **0.00** |
| `cafe` | 2138 | 0.00 | **0.00** |
| `doctors` | 2492 | 0.00 | **0.00** |

### Faza IV: Badanie Próbek Oceny Złotej

#### 🏆 TOP 5 (Najlepsze 5 przystanków w mieście)
<details><summary><b>Paszport Węzła: Brzeźna-Piotrkowska (H3: 891e21b109bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Brzeźna-Piotrkowska
  stop_id             : 2
  city                : lodz
  h3_index            : 891e21b109bffff
  stop_lat            : 51.7529
  stop_lon            : 19.4603
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : lodz

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 2.2490

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 13506513.2505
  raw_gravity         : 10389625.5773
  domain_count        : 3
  infra_score_log     : 16.4187

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 55.2857
  hourly_freq         : 9.7857
  transit_freq_log    : 4.0304

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 10425.2401
  liquidity           : 5.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 1841
  pop_val_log         : 7.5186
```
</details>
<details><summary><b>Paszport Węzła: Piotrkowska-Brzeźna (H3: 891e21b109bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Piotrkowska-Brzeźna
  stop_id             : 546
  city                : lodz
  h3_index            : 891e21b109bffff
  stop_lat            : 51.7530
  stop_lon            : 19.4598
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : lodz

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 2.2490

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 13506513.2505
  raw_gravity         : 10389625.5773
  domain_count        : 3
  infra_score_log     : 16.4187

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 55.2857
  hourly_freq         : 22.7143
  transit_freq_log    : 4.0304

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 10425.2401
  liquidity           : 5.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 1841
  pop_val_log         : 7.5186
```
</details>
<details><summary><b>Paszport Węzła: Piotrkowska-Żwirki (H3: 891e21b109bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Piotrkowska-Żwirki
  stop_id             : 961
  city                : lodz
  h3_index            : 891e21b109bffff
  stop_lat            : 51.7555
  stop_lon            : 19.4595
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : lodz

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 2.2490

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 13506513.2505
  raw_gravity         : 10389625.5773
  domain_count        : 3
  infra_score_log     : 16.4187

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 55.2857
  hourly_freq         : 22.7857
  transit_freq_log    : 4.0304

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 10425.2401
  liquidity           : 5.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 1841
  pop_val_log         : 7.5186
```
</details>
<details><summary><b>Paszport Węzła: Żeromskiego-Radwańska (kampus PŁ) (H3: 891e21b16a7ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Żeromskiego-Radwańska (kampus PŁ)
  stop_id             : 1562
  city                : lodz
  h3_index            : 891e21b16a7ffff
  stop_lat            : 51.7522
  stop_lon            : 19.4494
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : lodz

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 99.9281
  local_score_raw     : 2.0772

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 7544779.2342
  raw_gravity         : 6858890.2129
  domain_count        : 1
  infra_score_log     : 15.8364

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 23.9286
  hourly_freq         : 12.3571
  transit_freq_log    : 3.2160

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 11988.7165
  liquidity           : 1.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 829
  pop_val_log         : 6.7214
```
</details>
<details><summary><b>Paszport Węzła: Radwańska-Politechniki (kampus PŁ) (H3: 891e21b16a7ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Radwańska-Politechniki (kampus PŁ)
  stop_id             : 1103
  city                : lodz
  h3_index            : 891e21b16a7ffff
  stop_lat            : 51.7517
  stop_lon            : 19.4479
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : lodz

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 99.9281
  local_score_raw     : 2.0772

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 7544779.2342
  raw_gravity         : 6858890.2129
  domain_count        : 1
  infra_score_log     : 15.8364

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 23.9286
  hourly_freq         : 2.0000
  transit_freq_log    : 3.2160

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 11988.7165
  liquidity           : 1.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 829
  pop_val_log         : 6.7214
```
</details>

#### 🎲 RANDOM 5 (Środkowe przystanki miasta)
<details><summary><b>Paszport Węzła: Tuszyńska-Piaseczna NŻ (H3: 891e21b13dbffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Tuszyńska-Piaseczna NŻ
  stop_id             : 3809
  city                : lodz
  h3_index            : 891e21b13dbffff
  stop_lat            : 51.7321
  stop_lon            : 19.4667
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : lodz

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : B
  local_percentile    : 78.4173
  local_score_raw     : 0.6407

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 39311.4997
  raw_gravity         : 35737.7270
  domain_count        : 1
  infra_score_log     : 10.5793

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 4.2143
  hourly_freq         : 2.0714
  transit_freq_log    : 1.6514

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 8511.1484
  liquidity           : 1.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 657
  pop_val_log         : 6.4892
```
</details>
<details><summary><b>Paszport Węzła: Słowiańska-szkoła (Rąbień) (H3: 891e2184193ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Słowiańska-szkoła (Rąbień)
  stop_id             : 2433
  city                : lodz
  h3_index            : 891e2184193ffff
  stop_lat            : 51.7897
  stop_lon            : 19.3225
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : lodz

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : B
  local_percentile    : 75.6835
  local_score_raw     : 0.5315

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 12479527.7411
  raw_gravity         : 10399606.4509
  domain_count        : 2
  infra_score_log     : 16.3396

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 2.4286
  hourly_freq         : 1.1429
  transit_freq_log    : 1.2321

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 5571.4871
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 68
  pop_val_log         : 4.2341
```
</details>
<details><summary><b>Paszport Węzła: Zgierska-Sędziowska (H3: 891e21b300bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Zgierska-Sędziowska
  stop_id             : 1504
  city                : lodz
  h3_index            : 891e21b300bffff
  stop_lat            : 51.7955
  stop_lon            : 19.4460
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : lodz

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : B
  local_percentile    : 75.8273
  local_score_raw     : 0.5369

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 127165.1586
  raw_gravity         : 105970.9655
  domain_count        : 2
  infra_score_log     : 11.7532

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 6.5000
  hourly_freq         : 6.5000
  transit_freq_log    : 2.0149

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 5571.4871
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 1127
  pop_val_log         : 7.0282
```
</details>
<details><summary><b>Paszport Węzła: Legionów-Włókniarzy (H3: 891e21849a3ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Legionów-Włókniarzy
  stop_id             : 833
  city                : lodz
  h3_index            : 891e21849a3ffff
  stop_lat            : 51.7694
  stop_lon            : 19.4270
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : lodz

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : B
  local_percentile    : 73.6691
  local_score_raw     : 0.4786

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 1198.1479
  raw_gravity         : 1198.1479
  domain_count        : 0
  infra_score_log     : 7.0894

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 48.7857
  hourly_freq         : 12.0714
  transit_freq_log    : 3.9077

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 5571.4871
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 42
  pop_val_log         : 3.7612
```
</details>
<details><summary><b>Paszport Węzła: Konstantynowska-Unii Lubelskiej (Fala) (H3: 891e21849abffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Konstantynowska-Unii Lubelskiej (Fala)
  stop_id             : 1235
  city                : lodz
  h3_index            : 891e21849abffff
  stop_lat            : 51.7674
  stop_lon            : 19.4219
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : lodz

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : C
  local_percentile    : 51.7266
  local_score_raw     : -0.0963

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 1169.0538
  raw_gravity         : 1169.0538
  domain_count        : 0
  infra_score_log     : 7.0648

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 17.1429
  hourly_freq         : 9.0714
  transit_freq_log    : 2.8983

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 5571.4871
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>

#### 💩 BOTTOM 5 (Najsłabsze 5 przystanków)
<details><summary><b>Paszport Węzła: Huta Bardzyńska (H3: 891e2194003ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Huta Bardzyńska
  stop_id             : 1600063
  city                : lodz
  h3_index            : 891e2194003ffff
  stop_lat            : 51.9010
  stop_lon            : 19.1673
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : lodz-lka

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.2158
  local_score_raw     : -1.3258

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 14.0299
  raw_gravity         : 14.0299
  domain_count        : 0
  infra_score_log     : 2.7100

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.3571
  hourly_freq         : 0.1429
  transit_freq_log    : 0.3054

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 5571.4871
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Huta Bardzyńska (H3: 891e2194003ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Huta Bardzyńska
  stop_id             : 1600070
  city                : lodz
  h3_index            : 891e2194003ffff
  stop_lat            : 51.9010
  stop_lon            : 19.1672
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : lodz-lka

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.2158
  local_score_raw     : -1.3258

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 14.0299
  raw_gravity         : 14.0299
  domain_count        : 0
  infra_score_log     : 2.7100

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.3571
  hourly_freq         : 0.2143
  transit_freq_log    : 0.3054

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 5571.4871
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Ślądkowice Skrzyżowanie kier. Pabianice (H3: 891e2116ed7ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Ślądkowice Skrzyżowanie kier. Pabianice
  stop_id             : 14100007
  city                : lodz
  h3_index            : 891e2116ed7ffff
  stop_lat            : 51.5748
  stop_lon            : 19.3134
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : lodz-lka

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.1439
  local_score_raw     : -1.3470

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 32.6064
  raw_gravity         : 32.6064
  domain_count        : 0
  infra_score_log     : 3.5147

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.0000
  hourly_freq         : 0.0000
  transit_freq_log    : 0.0000

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 5571.4871
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Ślądkowice Skrzyżowanie kier. Dłutów (H3: 891e2116ed7ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Ślądkowice Skrzyżowanie kier. Dłutów
  stop_id             : 14100044
  city                : lodz
  h3_index            : 891e2116ed7ffff
  stop_lat            : 51.5748
  stop_lon            : 19.3133
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : lodz-lka

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.1439
  local_score_raw     : -1.3470

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 32.6064
  raw_gravity         : 32.6064
  domain_count        : 0
  infra_score_log     : 3.5147

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.0000
  hourly_freq         : 0.0000
  transit_freq_log    : 0.0000

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 5571.4871
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Janków Skrzyżowanie (H3: 891e21a5457ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Janków Skrzyżowanie
  stop_id             : 1700028
  city                : lodz
  h3_index            : 891e21a5457ffff
  stop_lat            : 51.6407
  stop_lon            : 19.8151
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : lodz-lka

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.0719
  local_score_raw     : -1.4257

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 5.2237
  raw_gravity         : 5.2237
  domain_count        : 0
  infra_score_log     : 1.8284

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.2857
  hourly_freq         : 0.2857
  transit_freq_log    : 0.2513

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 5571.4871
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>

---

## AGLOMERACJA: LOMZA
**Status:** ✅ SUKCES

### Faza 0: Stan Danych
- **Całkowita populacja w strefie miasta:** 65,199 (Baseline: 60,000) [✅ OK]
- **Ilość Transakcji RCN:** 5,045
- **Zakres Dat RCN:** 2020-01-01 do 2026-01-21
- **Ceny RCN (PLN/m²):** Średnia=5,965 | Mediana=5,644 | Max=76,710 | IQR=[3,888 - 7,400]
- **Infrastruktura OSM (Punkty):** 6,891
- **Infrastruktura OSM (Poligony/Budynki):** 17,058
- Baza transakcyjna `.gpkg` ustrukturyzowana poprawnie.

### Faza I & II: Pokrycie (Zero-Values)
- **Pustynia Populacyjna:** 15 (8.5%)
- **Pustynia Infrastrukturalna:** 0 (0.0%)
- **Głuche Przystanki:** 0 (0.0%)
- **Wskaźnik Fallback RCN:** 95 (54.0%) (Mediana RCN dla miasta: 5489)

### Faza III: Udowodnione POI w Promieniu 500m

**Rzeczywiste TOP 20 zwalidowanych obiektów (Intersekcja bufor 500m):**

| Tag OSM | Zliczone (Ilość) | Prawdziwa Waga JSON | Całkowita Siła (Score) |
|---|---|---|---|
| `supermarket` | 290 | 8,484,178.02 | **2,460,411,625.80** |
| `place_of_worship` | 308 | 75,842.26 | **23,359,416.08** |
| `marketplace` | 17 | 1,104,263.38 | **18,772,477.46** |
| `pharmacy` | 280 | 52,477.63 | **14,693,736.40** |
| `sports_centre` | 12 | 1,161,598.52 | **13,939,182.24** |
| `bank` | 252 | 54,905.36 | **13,836,150.72** |
| `post_office` | 48 | 68,389.31 | **3,282,686.88** |
| `parcel_locker` | 321 | 0.00 | **0.00** |
| `bench` | 314 | 0.00 | **0.00** |
| `restaurant` | 302 | 0.00 | **0.00** |
| `atm` | 223 | 0.00 | **0.00** |
| `bureau_de_change` | 151 | 0.00 | **0.00** |
| `bicycle_parking` | 143 | 0.00 | **0.00** |
| `bicycle_rental` | 114 | 0.00 | **0.00** |
| `car_wash` | 117 | 0.00 | **0.00** |
| `fast_food` | 131 | 0.00 | **0.00** |
| `fuel` | 134 | 0.00 | **0.00** |
| `waste_basket` | 96 | 0.00 | **0.00** |
| `kindergarten` | 239 | 0.00 | **0.00** |
| `school` | 260 | 0.00 | **0.00** |

### Faza IV: Badanie Próbek Oceny Złotej

#### 🏆 TOP 5 (Najlepsze 5 przystanków w mieście)
<details><summary><b>Paszport Węzła: Aleja Piłsudzkiego — Prusa (H3: 891f51cad0bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Aleja Piłsudzkiego — Prusa
  stop_id             : 52
  city                : lomza
  h3_index            : 891f51cad0bffff
  stop_lat            : 53.1621
  stop_lon            : 22.0690
  source              : lomza

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 1.7448

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 5317991.2083
  raw_gravity         : 4431659.3402
  domain_count        : 2
  infra_score_log     : 15.4866

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 14.0000
  hourly_freq         : 7.0714
  transit_freq_log    : 2.7081

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 8079.9340
  liquidity           : 43.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 1632
  pop_val_log         : 7.3982
```
</details>
<details><summary><b>Paszport Węzła: Aleja Piłsudzkiego — Konstytucji 3 Maja (H3: 891f51cad0bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Aleja Piłsudzkiego — Konstytucji 3 Maja
  stop_id             : 53
  city                : lomza
  h3_index            : 891f51cad0bffff
  stop_lat            : 53.1619
  stop_lon            : 22.0688
  source              : lomza

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 1.7448

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 5317991.2083
  raw_gravity         : 4431659.3402
  domain_count        : 2
  infra_score_log     : 15.4866

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 14.0000
  hourly_freq         : 6.9286
  transit_freq_log    : 2.7081

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 8079.9340
  liquidity           : 43.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 1632
  pop_val_log         : 7.3982
```
</details>
<details><summary><b>Paszport Węzła: Rządowa (H3: 891f51c1e53ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Rządowa
  stop_id             : 36
  city                : lomza
  h3_index            : 891f51c1e53ffff
  stop_lat            : 53.1803
  stop_lon            : 22.0804
  source              : lomza

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 99.0099
  local_score_raw     : 1.4521

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 5377941.5699
  raw_gravity         : 4136878.1307
  domain_count        : 3
  infra_score_log     : 15.4978

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 26.8571
  hourly_freq         : 12.6429
  transit_freq_log    : 3.3271

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 5123.4125
  liquidity           : 88.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 875
  pop_val_log         : 6.7754
```
</details>
<details><summary><b>Paszport Węzła: Plac Kościuszki — Jantar (H3: 891f51c1e53ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Plac Kościuszki — Jantar
  stop_id             : 2
  city                : lomza
  h3_index            : 891f51c1e53ffff
  stop_lat            : 53.1806
  stop_lon            : 22.0773
  source              : lomza

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 99.0099
  local_score_raw     : 1.4521

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 5377941.5699
  raw_gravity         : 4136878.1307
  domain_count        : 3
  infra_score_log     : 15.4978

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 26.8571
  hourly_freq         : 14.2143
  transit_freq_log    : 3.3271

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 5123.4125
  liquidity           : 88.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 875
  pop_val_log         : 6.7754
```
</details>
<details><summary><b>Paszport Węzła: Aleja Piłsudzkiego — Empik (H3: 891f51cad77ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Aleja Piłsudzkiego — Empik
  stop_id             : 49
  city                : lomza
  h3_index            : 891f51cad77ffff
  stop_lat            : 53.1608
  stop_lon            : 22.0792
  source              : lomza

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 98.0198
  local_score_raw     : 1.4191

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 12745078.2223
  raw_gravity         : 10620898.5185
  domain_count        : 2
  infra_score_log     : 16.3607

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 11.7143
  hourly_freq         : 4.7857
  transit_freq_log    : 2.5427

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6622.9512
  liquidity           : 243.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 584
  pop_val_log         : 6.3716
```
</details>

#### 🎲 RANDOM 5 (Środkowe przystanki miasta)
<details><summary><b>Paszport Węzła: Szosa Zambrowska — Rondo Lutosławskiego (H3: 891f51cadb3ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Szosa Zambrowska — Rondo Lutosławskiego
  stop_id             : 41
  city                : lomza
  h3_index            : 891f51cadb3ffff
  stop_lat            : 53.1714
  stop_lon            : 22.0823
  source              : lomza

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : C
  local_percentile    : 68.3168
  local_score_raw     : 0.3063

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 49129.1894
  raw_gravity         : 44662.8994
  domain_count        : 1
  infra_score_log     : 10.8022

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 6.2143
  hourly_freq         : 5.4286
  transit_freq_log    : 1.9761

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 5488.6677
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 99
  pop_val_log         : 4.6052
```
</details>
<details><summary><b>Paszport Węzła: Nowogrodzka — Stacha Konwy (H3: 891f51c1337ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Nowogrodzka — Stacha Konwy
  stop_id             : 102
  city                : lomza
  h3_index            : 891f51c1337ffff
  stop_lat            : 53.1817
  stop_lon            : 22.0699
  source              : lomza

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : D
  local_percentile    : 49.5050
  local_score_raw     : -0.0882

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 675.0864
  raw_gravity         : 675.0864
  domain_count        : 0
  infra_score_log     : 6.5163

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 4.6429
  hourly_freq         : 4.6429
  transit_freq_log    : 1.7304

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 5288.1790
  liquidity           : 38.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 807
  pop_val_log         : 6.6946
```
</details>
<details><summary><b>Paszport Węzła: Przykoszarowa — Pętla (H3: 891f51cad43ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Przykoszarowa — Pętla
  stop_id             : 148
  city                : lomza
  h3_index            : 891f51cad43ffff
  stop_lat            : 53.1598
  stop_lon            : 22.0625
  source              : lomza

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : C
  local_percentile    : 50.4950
  local_score_raw     : -0.0841

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 431.4981
  raw_gravity         : 431.4981
  domain_count        : 0
  infra_score_log     : 6.0696

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 5.8571
  hourly_freq         : 2.6429
  transit_freq_log    : 1.9253

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 5038.8651
  liquidity           : 25.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 847
  pop_val_log         : 6.7429
```
</details>
<details><summary><b>Paszport Węzła: Sikorskiego — Szeroka (H3: 891f51c1303ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Sikorskiego — Szeroka
  stop_id             : 68
  city                : lomza
  h3_index            : 891f51c1303ffff
  stop_lat            : 53.1814
  stop_lon            : 22.0569
  source              : lomza

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : C
  local_percentile    : 56.4356
  local_score_raw     : -0.0389

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 1026.4853
  raw_gravity         : 1026.4853
  domain_count        : 0
  infra_score_log     : 6.9349

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 4.9286
  hourly_freq         : 4.9286
  transit_freq_log    : 1.7798

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 5488.6677
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 426
  pop_val_log         : 6.0568
```
</details>
<details><summary><b>Paszport Węzła: Nowogrodzka — Zabawna (H3: 891f51c13abffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Nowogrodzka — Zabawna
  stop_id             : 103
  city                : lomza
  h3_index            : 891f51c13abffff
  stop_lat            : 53.1835
  stop_lon            : 22.0635
  source              : lomza

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : C
  local_percentile    : 59.4059
  local_score_raw     : 0.0716

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 525.7839
  raw_gravity         : 525.7839
  domain_count        : 0
  infra_score_log     : 6.2668

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 9.5000
  hourly_freq         : 4.8571
  transit_freq_log    : 2.3514

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 5488.6677
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 144
  pop_val_log         : 4.9767
```
</details>

#### 💩 BOTTOM 5 (Najsłabsze 5 przystanków)
<details><summary><b>Paszport Węzła: Al. Legionów — Strusia 14 (H3: 891f51ca88bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Al. Legionów — Strusia 14
  stop_id             : 258
  city                : lomza
  h3_index            : 891f51ca88bffff
  stop_lat            : 53.1519
  stop_lon            : 22.0492
  source              : lomza

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 3.9604
  local_score_raw     : -1.1727

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 408.2664
  raw_gravity         : 408.2664
  domain_count        : 0
  infra_score_log     : 6.0144

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.5714
  hourly_freq         : 0.5714
  transit_freq_log    : 0.4520

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 5488.6677
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Poligonowa — UniGlass (H3: 891f51cac6bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Poligonowa — UniGlass
  stop_id             : 217
  city                : lomza
  h3_index            : 891f51cac6bffff
  stop_lat            : 53.1551
  stop_lon            : 22.0339
  source              : lomza

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 2.9703
  local_score_raw     : -1.2628

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 531.4998
  raw_gravity         : 531.4998
  domain_count        : 0
  infra_score_log     : 6.2776

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.2143
  hourly_freq         : 0.1429
  transit_freq_log    : 0.1942

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 5488.6677
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Poligonowa — Poznańska (H3: 891f51cac6bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Poligonowa — Poznańska
  stop_id             : 218
  city                : lomza
  h3_index            : 891f51cac6bffff
  stop_lat            : 53.1553
  stop_lon            : 22.0338
  source              : lomza

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 2.9703
  local_score_raw     : -1.2628

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 531.4998
  raw_gravity         : 531.4998
  domain_count        : 0
  infra_score_log     : 6.2776

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.2143
  hourly_freq         : 0.0714
  transit_freq_log    : 0.1942

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 5488.6677
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Piątnica — Hotel Baranowski (H3: 891f51c1cd7ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Piątnica — Hotel Baranowski
  stop_id             : 1204
  city                : lomza
  h3_index            : 891f51c1cd7ffff
  stop_lat            : 53.2024
  stop_lon            : 22.1008
  source              : lomza

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 1.9802
  local_score_raw     : -1.2680

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 44.2233
  raw_gravity         : 44.2233
  domain_count        : 0
  infra_score_log     : 3.8116

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.4286
  hourly_freq         : 0.4286
  transit_freq_log    : 0.3567

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 5488.6677
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 7
  pop_val_log         : 2.0794
```
</details>
<details><summary><b>Paszport Węzła: Al. Legionów — Pawia 16 (H3: 891f51ca81bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Al. Legionów — Pawia 16
  stop_id             : 259
  city                : lomza
  h3_index            : 891f51ca81bffff
  stop_lat            : 53.1493
  stop_lon            : 22.0478
  source              : lomza

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.9901
  local_score_raw     : -1.2966

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 219.9354
  raw_gravity         : 219.9354
  domain_count        : 0
  infra_score_log     : 5.3979

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.3571
  hourly_freq         : 0.3571
  transit_freq_log    : 0.3054

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 5488.6677
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>

---

## AGLOMERACJA: LUBLIN
**Status:** ✅ SUKCES

### Faza 0: Stan Danych
- **Całkowita populacja w strefie miasta:** 446,126 (Baseline: 330,000) [✅ OK]
- **Ilość Transakcji RCN:** 40,868
- **Zakres Dat RCN:** 2020-01-02 do 2026-12-31
- **Ceny RCN (PLN/m²):** Średnia=8,963 | Mediana=7,600 | Max=287,655 | IQR=[5,876 - 9,645]
- **Infrastruktura OSM (Punkty):** 126,448
- **Infrastruktura OSM (Poligony/Budynki):** 172,713
- Baza transakcyjna `.gpkg` ustrukturyzowana poprawnie.

### Faza I & II: Pokrycie (Zero-Values)
- **Pustynia Populacyjna:** 178 (13.5%)
- **Pustynia Infrastrukturalna:** 0 (0.0%)
- **Głuche Przystanki:** 42 (3.2%)
- **Wskaźnik Fallback RCN:** 753 (57.3%) (Mediana RCN dla miasta: 7436)

### Faza III: Udowodnione POI w Promieniu 500m

**Rzeczywiste TOP 20 zwalidowanych obiektów (Intersekcja bufor 500m):**

| Tag OSM | Zliczone (Ilość) | Prawdziwa Waga JSON | Całkowita Siła (Score) |
|---|---|---|---|
| `supermarket` | 1251 | 10,016,194.46 | **12,530,259,269.46** |
| `sports_centre` | 550 | 999,456.13 | **549,700,871.50** |
| `marketplace` | 264 | 1,198,959.04 | **316,525,186.56** |
| `place_of_worship` | 1062 | 103,744.51 | **110,176,669.62** |
| `pharmacy` | 1450 | 63,106.04 | **91,503,758.00** |
| `bank` | 881 | 68,602.46 | **60,438,767.26** |
| `post_office` | 440 | 67,420.76 | **29,665,134.40** |
| `bench` | 32217 | 0.00 | **0.00** |
| `parking_entrance` | 5538 | 0.00 | **0.00** |
| `waste_basket` | 4696 | 0.00 | **0.00** |
| `bicycle_parking` | 4633 | 0.00 | **0.00** |
| `vending_machine` | 3327 | 0.00 | **0.00** |
| `parcel_locker` | 3193 | 0.00 | **0.00** |
| `shelter` | 3303 | 0.00 | **0.00** |
| `restaurant` | 2226 | 0.00 | **0.00** |
| `kindergarten` | 2384 | 0.00 | **0.00** |
| `recycling` | 4383 | 0.00 | **0.00** |
| `atm` | 1202 | 0.00 | **0.00** |
| `fast_food` | 1375 | 0.00 | **0.00** |
| `school` | 2162 | 0.00 | **0.00** |

### Faza IV: Badanie Próbek Oceny Złotej

#### 🏆 TOP 5 (Najlepsze 5 przystanków w mieście)
<details><summary><b>Paszport Węzła: Krakowskie Przedmieście (H3: 891e2d09db7ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Krakowskie Przedmieście
  stop_id             : 1012
  city                : lublin
  h3_index            : 891e2d09db7ffff
  stop_lat            : 51.2476
  stop_lon            : 22.5528
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : lublin

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 2.2228

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 8412340.4766
  raw_gravity         : 6471031.1359
  domain_count        : 3
  infra_score_log     : 15.9452

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 25.2857
  hourly_freq         : 11.4286
  transit_freq_log    : 3.2690

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 14532.8720
  liquidity           : 507.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 332
  pop_val_log         : 5.8081
```
</details>
<details><summary><b>Paszport Węzła: Krakowskie Przedmieście (H3: 891e2d09db7ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Krakowskie Przedmieście
  stop_id             : 1014
  city                : lublin
  h3_index            : 891e2d09db7ffff
  stop_lat            : 51.2476
  stop_lon            : 22.5536
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : lublin

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 2.2228

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 8412340.4766
  raw_gravity         : 6471031.1359
  domain_count        : 3
  infra_score_log     : 15.9452

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 25.2857
  hourly_freq         : 13.8571
  transit_freq_log    : 3.2690

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 14532.8720
  liquidity           : 507.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 332
  pop_val_log         : 5.8081
```
</details>
<details><summary><b>Paszport Węzła: Zamojska (H3: 891e2d08a1bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Zamojska
  stop_id             : 2232
  city                : lublin
  h3_index            : 891e2d08a1bffff
  stop_lat            : 51.2415
  stop_lon            : 22.5694
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : lublin

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 99.8672
  local_score_raw     : 1.9491

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 8656466.7887
  raw_gravity         : 7869515.2624
  domain_count        : 1
  infra_score_log     : 15.9738

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 24.6429
  hourly_freq         : 24.6429
  transit_freq_log    : 3.2443

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 12177.0000
  liquidity           : 122.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 344
  pop_val_log         : 5.8435
```
</details>
<details><summary><b>Paszport Węzła: Brama Krakowska (H3: 891e2d08e6fffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Brama Krakowska
  stop_id             : 1031
  city                : lublin
  h3_index            : 891e2d08e6fffff
  stop_lat            : 51.2484
  stop_lon            : 22.5662
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : lublin

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 99.7344
  local_score_raw     : 1.7716

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 345816.7776
  raw_gravity         : 288180.6480
  domain_count        : 2
  infra_score_log     : 12.7537

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 16.5000
  hourly_freq         : 16.5000
  transit_freq_log    : 2.8622

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 14050.4379
  liquidity           : 58.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 596
  pop_val_log         : 6.3919
```
</details>
<details><summary><b>Paszport Węzła: Skrzetuskiego (H3: 891e2d09c3bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Skrzetuskiego
  stop_id             : 5512
  city                : lublin
  h3_index            : 891e2d09c3bffff
  stop_lat            : 51.2397
  stop_lon            : 22.5152
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : lublin

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 99.6016
  local_score_raw     : 1.7452

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 14954122.9592
  raw_gravity         : 11503171.5071
  domain_count        : 3
  infra_score_log     : 16.5205

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 32.4286
  hourly_freq         : 15.5714
  transit_freq_log    : 3.5094

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 8338.5580
  liquidity           : 33.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 1355
  pop_val_log         : 7.2123
```
</details>

#### 🎲 RANDOM 5 (Środkowe przystanki miasta)
<details><summary><b>Paszport Węzła: Łagiewnicka (H3: 891e2d0898bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Łagiewnicka
  stop_id             : 2341
  city                : lublin
  h3_index            : 891e2d0898bffff
  stop_lat            : 51.2615
  stop_lon            : 22.6254
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : lublin

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : D
  local_percentile    : 47.1448
  local_score_raw     : -0.2441

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 555.2773
  raw_gravity         : 555.2773
  domain_count        : 0
  infra_score_log     : 6.3213

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 3.4286
  hourly_freq         : 3.4286
  transit_freq_log    : 1.4881

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 7435.9435
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 40
  pop_val_log         : 3.7136
```
</details>
<details><summary><b>Paszport Węzła: Felin Europark (H3: 891e2d72523ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Felin Europark
  stop_id             : 3011
  city                : lublin
  h3_index            : 891e2d72523ffff
  stop_lat            : 51.2201
  stop_lon            : 22.6411
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : lublin

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : B
  local_percentile    : 80.7437
  local_score_raw     : 0.6676

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 7855843.8454
  raw_gravity         : 7141676.2231
  domain_count        : 1
  infra_score_log     : 15.8768

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 7.5714
  hourly_freq         : 2.1429
  transit_freq_log    : 2.1484

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 7891.8534
  liquidity           : 184.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Krasienin-Kolonia - szkoła (H3: 891e2d18a2bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Krasienin-Kolonia - szkoła
  stop_id             : 7231
  city                : lublin
  h3_index            : 891e2d18a2bffff
  stop_lat            : 51.3617
  stop_lon            : 22.4687
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : lublin

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : C
  local_percentile    : 68.3931
  local_score_raw     : 0.2807

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 5711315.1922
  raw_gravity         : 4759429.3268
  domain_count        : 2
  infra_score_log     : 15.5580

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.7143
  hourly_freq         : 0.3571
  transit_freq_log    : 0.5390

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 7435.9435
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 27
  pop_val_log         : 3.3322
```
</details>
<details><summary><b>Paszport Węzła: Herberta - szpital (H3: 891e2d72693ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Herberta - szpital
  stop_id             : 4211
  city                : lublin
  h3_index            : 891e2d72693ffff
  stop_lat            : 51.2149
  stop_lon            : 22.5706
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : lublin

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : C
  local_percentile    : 69.3227
  local_score_raw     : 0.3034

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 70637.9377
  raw_gravity         : 64216.3070
  domain_count        : 1
  infra_score_log     : 11.1653

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 2.7143
  hourly_freq         : 2.7143
  transit_freq_log    : 1.3122

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6895.5981
  liquidity           : 72.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 828
  pop_val_log         : 6.7202
```
</details>
<details><summary><b>Paszport Węzła: Majdanek (H3: 891e2d725dbffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Majdanek
  stop_id             : 3152
  city                : lublin
  h3_index            : 891e2d725dbffff
  stop_lat            : 51.2248
  stop_lon            : 22.6101
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : lublin

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : C
  local_percentile    : 66.4011
  local_score_raw     : 0.2293

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 1206.9219
  raw_gravity         : 1206.9219
  domain_count        : 0
  infra_score_log     : 7.0967

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 30.9286
  hourly_freq         : 15.1429
  transit_freq_log    : 3.4635

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 7435.9435
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>

#### 💩 BOTTOM 5 (Najsłabsze 5 przystanków)
<details><summary><b>Paszport Węzła: Dys - Słoneczna NŻ (H3: 891e2d0a863ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Dys - Słoneczna NŻ
  stop_id             : 7171
  city                : lublin
  h3_index            : 891e2d0a863ffff
  stop_lat            : 51.3052
  stop_lon            : 22.5827
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : lublin

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.5312
  local_score_raw     : -1.0995

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 82.6313
  raw_gravity         : 82.6313
  domain_count        : 0
  infra_score_log     : 4.4264

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.2857
  hourly_freq         : 0.2857
  transit_freq_log    : 0.2513

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 7435.9435
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Majdan Krasieniński - sklep (H3: 891e2d0a407ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Majdan Krasieniński - sklep
  stop_id             : 7193
  city                : lublin
  h3_index            : 891e2d0a407ffff
  stop_lat            : 51.3485
  stop_lon            : 22.4794
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : lublin

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.3984
  local_score_raw     : -1.1047

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 37.7632
  raw_gravity         : 37.7632
  domain_count        : 0
  infra_score_log     : 3.6575

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.5714
  hourly_freq         : 0.2143
  transit_freq_log    : 0.4520

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 7435.9435
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Majdan Krasieniński NŻ (H3: 891e2d0a407ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Majdan Krasieniński NŻ
  stop_id             : 7202
  city                : lublin
  h3_index            : 891e2d0a407ffff
  stop_lat            : 51.3480
  stop_lon            : 22.4798
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : lublin

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.3984
  local_score_raw     : -1.1047

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 37.7632
  raw_gravity         : 37.7632
  domain_count        : 0
  infra_score_log     : 3.6575

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.5714
  hourly_freq         : 0.3571
  transit_freq_log    : 0.4520

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 7435.9435
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Krasienin - Lipy NŻ (H3: 891e2d0a493ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Krasienin - Lipy NŻ
  stop_id             : 7221
  city                : lublin
  h3_index            : 891e2d0a493ffff
  stop_lat            : 51.3573
  stop_lon            : 22.4704
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : lublin

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.2656
  local_score_raw     : -1.1203

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 54.3445
  raw_gravity         : 54.3445
  domain_count        : 0
  infra_score_log     : 4.0136

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.3571
  hourly_freq         : 0.3571
  transit_freq_log    : 0.3054

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 7435.9435
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Snopków II (H3: 891e2d0a22fffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Snopków II
  stop_id             : 9521
  city                : lublin
  h3_index            : 891e2d0a22fffff
  stop_lat            : 51.3080
  stop_lon            : 22.4909
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : lublin

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.1328
  local_score_raw     : -1.1333

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 323.0926
  raw_gravity         : 323.0926
  domain_count        : 0
  infra_score_log     : 5.7810

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.7143
  hourly_freq         : 0.7143
  transit_freq_log    : 0.5390

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 3717.7935
  liquidity           : 3.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 10
  pop_val_log         : 2.3979
```
</details>

---

## AGLOMERACJA: OLSZTYN
**Status:** ✅ SUKCES

### Faza 0: Stan Danych
- **Całkowita populacja w strefie miasta:** 238,431 (Baseline: 170,000) [✅ OK]
- **Ilość Transakcji RCN:** 20,397
- **Zakres Dat RCN:** 2020-01-02 do 2052-06-06
- **Ceny RCN (PLN/m²):** Średnia=8,341 | Mediana=6,911 | Max=445,427 | IQR=[5,500 - 8,763]
- **Infrastruktura OSM (Punkty):** 28,923
- **Infrastruktura OSM (Poligony/Budynki):** 48,316
- Baza transakcyjna `.gpkg` ustrukturyzowana poprawnie.

### Faza I & II: Pokrycie (Zero-Values)
- **Pustynia Populacyjna:** 175 (21.4%)
- **Pustynia Infrastrukturalna:** 4 (0.5%)
- **Głuche Przystanki:** 177 (21.7%)
- **Wskaźnik Fallback RCN:** 423 (51.8%) (Mediana RCN dla miasta: 6819)

### Faza III: Udowodnione POI w Promieniu 500m

**Rzeczywiste TOP 20 zwalidowanych obiektów (Intersekcja bufor 500m):**

| Tag OSM | Zliczone (Ilość) | Prawdziwa Waga JSON | Całkowita Siła (Score) |
|---|---|---|---|
| `supermarket` | 778 | 9,217,817.18 | **7,171,461,766.04** |
| `sports_centre` | 183 | 1,145,874.73 | **209,695,075.59** |
| `marketplace` | 59 | 1,399,519.98 | **82,571,678.82** |
| `place_of_worship` | 789 | 84,957.43 | **67,031,412.27** |
| `pharmacy` | 777 | 59,514.60 | **46,242,844.20** |
| `bank` | 394 | 64,266.42 | **25,320,969.48** |
| `post_office` | 332 | 68,657.34 | **22,794,236.88** |
| `bench` | 12829 | 0.00 | **0.00** |
| `waste_basket` | 5747 | 0.00 | **0.00** |
| `bicycle_parking` | 3524 | 0.00 | **0.00** |
| `parcel_locker` | 1905 | 0.00 | **0.00** |
| `restaurant` | 1337 | 0.00 | **0.00** |
| `atm` | 903 | 0.00 | **0.00** |
| `fast_food` | 1144 | 0.00 | **0.00** |
| `vending_machine` | 740 | 0.00 | **0.00** |
| `recycling` | 717 | 0.00 | **0.00** |
| `waste_disposal` | 2323 | 0.00 | **0.00** |
| `parking` | 18083 | 0.00 | **0.00** |
| `charging_station` | 423 | 0.00 | **0.00** |
| `kindergarten` | 736 | 0.00 | **0.00** |

### Faza IV: Badanie Próbek Oceny Złotej

#### 🏆 TOP 5 (Najlepsze 5 przystanków w mieście)
<details><summary><b>Paszport Węzła: Słoneczny Stok (Słoneczna) (H3: 891f547690bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Słoneczny Stok (Słoneczna)
  stop_id             : 64
  city                : olsztyn
  h3_index            : 891f547690bffff
  stop_lat            : 53.7518
  stop_lon            : 20.4492
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : olsztyn

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 2.2878

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 501.2854
  raw_gravity         : 501.2854
  domain_count        : 0.0000
  infra_score_log     : 6.2192

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 7.5000
  hourly_freq         : 3.7857
  transit_freq_log    : 2.1401

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 47546.1573
  liquidity           : 4.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 145
  pop_val_log         : 4.9836
```
</details>
<details><summary><b>Paszport Węzła: Słoneczny Stok (Słoneczna) (H3: 891f547690bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Słoneczny Stok (Słoneczna)
  stop_id             : 401
  city                : olsztyn
  h3_index            : 891f547690bffff
  stop_lat            : 53.7518
  stop_lon            : 20.4488
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : olsztyn

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 2.2878

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 501.2854
  raw_gravity         : 501.2854
  domain_count        : 0.0000
  infra_score_log     : 6.2192

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 7.5000
  hourly_freq         : 3.7143
  transit_freq_log    : 2.1401

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 47546.1573
  liquidity           : 4.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 145
  pop_val_log         : 4.9836
```
</details>
<details><summary><b>Paszport Węzła: Żurawia (Bałtycka) (H3: 891f543903bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Żurawia (Bałtycka)
  stop_id             : 155
  city                : olsztyn
  h3_index            : 891f543903bffff
  stop_lat            : 53.8029
  stop_lon            : 20.4054
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : olsztyn

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 99.7506
  local_score_raw     : 2.2854

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 139058.8823
  raw_gravity         : 126417.1657
  domain_count        : 1.0000
  infra_score_log     : 11.8427

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 12.6429
  hourly_freq         : 6.2857
  transit_freq_log    : 2.6132

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 34829.0879
  liquidity           : 10.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 336
  pop_val_log         : 5.8201
```
</details>
<details><summary><b>Paszport Węzła: Żurawia (Bałtycka) (H3: 891f543903bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Żurawia (Bałtycka)
  stop_id             : 156
  city                : olsztyn
  h3_index            : 891f543903bffff
  stop_lat            : 53.8031
  stop_lon            : 20.4046
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : olsztyn

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 99.7506
  local_score_raw     : 2.2854

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 139058.8823
  raw_gravity         : 126417.1657
  domain_count        : 1.0000
  infra_score_log     : 11.8427

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 12.6429
  hourly_freq         : 6.3571
  transit_freq_log    : 2.6132

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 34829.0879
  liquidity           : 10.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 336
  pop_val_log         : 5.8201
```
</details>
<details><summary><b>Paszport Węzła: Carrefour (Krasickiego) (H3: 891f542b42fffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Carrefour (Krasickiego)
  stop_id             : 747
  city                : olsztyn
  h3_index            : 891f542b42fffff
  stop_lat            : 53.7494
  stop_lon            : 20.5052
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : olsztyn

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 99.5012
  local_score_raw     : 1.6624

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 9048521.1069
  raw_gravity         : 6960400.8515
  domain_count        : 3.0000
  infra_score_log     : 16.0181

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 46.8571
  hourly_freq         : 8.5714
  transit_freq_log    : 3.8682

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 7852.2066
  liquidity           : 262.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 1359
  pop_val_log         : 7.2152
```
</details>

#### 🎲 RANDOM 5 (Środkowe przystanki miasta)
<details><summary><b>Paszport Węzła: Zatoka Miła (Miła) (H3: 891f5476dabffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Zatoka Miła (Miła)
  stop_id             : 343
  city                : olsztyn
  h3_index            : 891f5476dabffff
  stop_lat            : 53.7732
  stop_lon            : 20.4402
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : olsztyn

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : D
  local_percentile    : 30.9227
  local_score_raw     : -0.4735

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 79.8335
  raw_gravity         : 79.8335
  domain_count        : 0.0000
  infra_score_log     : 4.3924

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.0000
  hourly_freq         : 0.0000
  transit_freq_log    : 0.0000

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 11690.6011
  liquidity           : 6.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 19
  pop_val_log         : 2.9957
```
</details>
<details><summary><b>Paszport Węzła: Św. Arnolda (Hozjusza) (H3: 891f54391abffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Św. Arnolda (Hozjusza)
  stop_id             : 2
  city                : olsztyn
  h3_index            : 891f54391abffff
  stop_lat            : 53.8082
  stop_lon            : 20.4407
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : olsztyn

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : B
  local_percentile    : 76.8080
  local_score_raw     : 0.5824

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 47142.1594
  raw_gravity         : 47142.1594
  domain_count        : 0.0000
  infra_score_log     : 10.7609

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 11.1429
  hourly_freq         : 5.5714
  transit_freq_log    : 2.4967

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6819.3887
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 58
  pop_val_log         : 4.0775
```
</details>
<details><summary><b>Paszport Węzła: Gutkowo-Przyjazna (Gutkowo) (H3: 891f543904bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Gutkowo-Przyjazna (Gutkowo)
  stop_id             : 807
  city                : olsztyn
  h3_index            : 891f543904bffff
  stop_lat            : 53.7987
  stop_lon            : 20.3842
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : olsztyn

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : D
  local_percentile    : 33.4165
  local_score_raw     : -0.4278

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 106.9440
  raw_gravity         : 106.9440
  domain_count        : 0.0000
  infra_score_log     : 4.6816

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.7857
  hourly_freq         : 0.7857
  transit_freq_log    : 0.5798

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 9053.0952
  liquidity           : 1.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 18
  pop_val_log         : 2.9444
```
</details>
<details><summary><b>Paszport Węzła: Gady wieś (Gady) (H3: 891f543a98bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Gady wieś (Gady)
  stop_id             : 563
  city                : olsztyn
  h3_index            : 891f543a98bffff
  stop_lat            : 53.8772
  stop_lon            : 20.5788
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : olsztyn

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : D
  local_percentile    : 27.1820
  local_score_raw     : -0.5480

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 340.0138
  raw_gravity         : 340.0138
  domain_count        : 0.0000
  infra_score_log     : 5.8319

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.0000
  hourly_freq         : 0.0000
  transit_freq_log    : 0.0000

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6819.3887
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 51
  pop_val_log         : 3.9512
```
</details>
<details><summary><b>Paszport Węzła: Synów Pułku (Synów Pułku) (H3: 891f542b4abffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Synów Pułku (Synów Pułku)
  stop_id             : 772
  city                : olsztyn
  h3_index            : 891f542b4abffff
  stop_lat            : 53.7573
  stop_lon            : 20.4976
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : olsztyn

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : D
  local_percentile    : 34.4140
  local_score_raw     : -0.4151

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 384.1987
  raw_gravity         : 384.1987
  domain_count        : 0.0000
  infra_score_log     : 5.9538

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.0000
  hourly_freq         : 0.0000
  transit_freq_log    : 0.0000

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6419.1447
  liquidity           : 76.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 553
  pop_val_log         : 6.3172
```
</details>

#### 💩 BOTTOM 5 (Najsłabsze 5 przystanków)
<details><summary><b>Paszport Węzła: Derc 62 (Derc) (H3: 891f5430317ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Derc 62 (Derc)
  stop_id             : 718
  city                : olsztyn
  h3_index            : 891f5430317ffff
  stop_lat            : 53.9426
  stop_lon            : 20.6270
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : olsztyn

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.7481
  local_score_raw     : -1.1491

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 4.0456
  raw_gravity         : 4.0456
  domain_count        : 0.0000
  infra_score_log     : 1.6185

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.0000
  hourly_freq         : 0.0000
  transit_freq_log    : 0.0000

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6819.3887
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Podleśna Kolonia (Podleśna) (H3: 891f5404d37ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Podleśna Kolonia (Podleśna)
  stop_id             : 679
  city                : olsztyn
  h3_index            : 891f5404d37ffff
  stop_lat            : 53.9575
  stop_lon            : 20.4728
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : olsztyn

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.4988
  local_score_raw     : -1.2039

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 0.0000
  raw_gravity         : 0.0000
  domain_count        : 0.0000
  infra_score_log     : 0.0000

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.0000
  hourly_freq         : 0.0000
  transit_freq_log    : 0.0000

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6819.3887
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 3
  pop_val_log         : 1.3863
```
</details>
<details><summary><b>Paszport Węzła: Podleśna Kolonia (Podleśna) (H3: 891f5404d37ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Podleśna Kolonia (Podleśna)
  stop_id             : 680
  city                : olsztyn
  h3_index            : 891f5404d37ffff
  stop_lat            : 53.9576
  stop_lon            : 20.4729
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : olsztyn

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.4988
  local_score_raw     : -1.2039

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 0.0000
  raw_gravity         : 0.0000
  domain_count        : 0.0000
  infra_score_log     : 0.0000

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.0000
  hourly_freq         : 0.0000
  transit_freq_log    : 0.0000

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6819.3887
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 3
  pop_val_log         : 1.3863
```
</details>
<details><summary><b>Paszport Węzła: Nowe Włóki kolonia 2 (Nowe Włóki) (H3: 891f5431363ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Nowe Włóki kolonia 2 (Nowe Włóki)
  stop_id             : 522
  city                : olsztyn
  h3_index            : 891f5431363ffff
  stop_lat            : 53.8997
  stop_lon            : 20.5477
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : olsztyn

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.2494
  local_score_raw     : -1.2880

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 0.0000
  raw_gravity         : 0.0000
  domain_count        : 0.0000
  infra_score_log     : 0.0000

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.0000
  hourly_freq         : 0.0000
  transit_freq_log    : 0.0000

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6819.3887
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Nowe Włóki kolonia 2 (Nowe Włóki) (H3: 891f5431363ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Nowe Włóki kolonia 2 (Nowe Włóki)
  stop_id             : 521
  city                : olsztyn
  h3_index            : 891f5431363ffff
  stop_lat            : 53.8997
  stop_lon            : 20.5477
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : olsztyn

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.2494
  local_score_raw     : -1.2880

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 0.0000
  raw_gravity         : 0.0000
  domain_count        : 0.0000
  infra_score_log     : 0.0000

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.0000
  hourly_freq         : 0.0000
  transit_freq_log    : 0.0000

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6819.3887
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>

---

## AGLOMERACJA: OPOLE
**Status:** ✅ SUKCES

### Faza 0: Stan Danych
- **Całkowita populacja w strefie miasta:** 150,715 (Baseline: 120,000) [✅ OK]
- **Ilość Transakcji RCN:** 5,560
- **Zakres Dat RCN:** 2022-10-04 do 2026-02-11
- **Ceny RCN (PLN/m²):** Średnia=9,745 | Mediana=8,097 | Max=265,909 | IQR=[6,115 - 10,090]
- **Infrastruktura OSM (Punkty):** 27,704
- **Infrastruktura OSM (Poligony/Budynki):** 62,121
- Baza transakcyjna `.gpkg` ustrukturyzowana poprawnie.

### Faza I & II: Pokrycie (Zero-Values)
- **Pustynia Populacyjna:** 75 (13.8%)
- **Pustynia Infrastrukturalna:** 0 (0.0%)
- **Głuche Przystanki:** 17 (3.1%)
- **Wskaźnik Fallback RCN:** 306 (56.4%) (Mediana RCN dla miasta: 7916)

### Faza III: Udowodnione POI w Promieniu 500m

**Rzeczywiste TOP 20 zwalidowanych obiektów (Intersekcja bufor 500m):**

| Tag OSM | Zliczone (Ilość) | Prawdziwa Waga JSON | Całkowita Siła (Score) |
|---|---|---|---|
| `supermarket` | 506 | 8,909,957.07 | **4,508,438,277.42** |
| `sports_centre` | 102 | 1,204,840.36 | **122,893,716.72** |
| `place_of_worship` | 315 | 91,038.51 | **28,677,130.65** |
| `pharmacy` | 460 | 57,825.55 | **26,599,753.00** |
| `bank` | 185 | 61,569.99 | **11,390,448.15** |
| `post_office` | 99 | 64,015.37 | **6,337,521.63** |
| `marketplace` | 2 | 1,351,468.90 | **2,702,937.80** |
| `bench` | 5521 | 0.00 | **0.00** |
| `waste_basket` | 2826 | 0.00 | **0.00** |
| `bicycle_parking` | 1023 | 0.00 | **0.00** |
| `restaurant` | 687 | 0.00 | **0.00** |
| `recycling` | 491 | 0.00 | **0.00** |
| `parking_entrance` | 411 | 0.00 | **0.00** |
| `parcel_locker` | 409 | 0.00 | **0.00** |
| `shelter` | 533 | 0.00 | **0.00** |
| `fast_food` | 344 | 0.00 | **0.00** |
| `atm` | 248 | 0.00 | **0.00** |
| `cafe` | 208 | 0.00 | **0.00** |
| `vending_machine` | 189 | 0.00 | **0.00** |
| `parking` | 8450 | 0.00 | **0.00** |

### Faza IV: Badanie Próbek Oceny Złotej

#### 🏆 TOP 5 (Najlepsze 5 przystanków w mieście)
<details><summary><b>Paszport Węzła: Ozimska - Malinka (266) (H3: 891e23c6ad3ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Ozimska - Malinka (266)
  stop_id             : 266
  city                : opole
  h3_index            : 891e23c6ad3ffff
  stop_lat            : 50.6695
  stop_lon            : 17.9678
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : opole

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 1.9298

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 5840168.0717
  raw_gravity         : 5309243.7015
  domain_count        : 1
  infra_score_log     : 15.5803

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 20.0714
  hourly_freq         : 9.7143
  transit_freq_log    : 3.0479

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 12186.5065
  liquidity           : 83.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 923
  pop_val_log         : 6.8287
```
</details>
<details><summary><b>Paszport Węzła: Piotrkowska (951) (H3: 891e23c6ad3ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Piotrkowska (951)
  stop_id             : 951
  city                : opole
  h3_index            : 891e23c6ad3ffff
  stop_lat            : 50.6701
  stop_lon            : 17.9672
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : opole

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 1.9298

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 5840168.0717
  raw_gravity         : 5309243.7015
  domain_count        : 1
  infra_score_log     : 15.5803

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 20.0714
  hourly_freq         : 0.4286
  transit_freq_log    : 3.0479

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 12186.5065
  liquidity           : 83.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 923
  pop_val_log         : 6.8287
```
</details>
<details><summary><b>Paszport Węzła: Ozimska - Malinka (265) (H3: 891e23c6ad3ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Ozimska - Malinka (265)
  stop_id             : 265
  city                : opole
  h3_index            : 891e23c6ad3ffff
  stop_lat            : 50.6694
  stop_lon            : 17.9690
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : opole

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 1.9298

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 5840168.0717
  raw_gravity         : 5309243.7015
  domain_count        : 1
  infra_score_log     : 15.5803

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 20.0714
  hourly_freq         : 9.9286
  transit_freq_log    : 3.0479

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 12186.5065
  liquidity           : 83.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 923
  pop_val_log         : 6.8287
```
</details>
<details><summary><b>Paszport Węzła: Niemodlińska - Koszyka (218) (H3: 891e23c44d7ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Niemodlińska - Koszyka (218)
  stop_id             : 218
  city                : opole
  h3_index            : 891e23c44d7ffff
  stop_lat            : 50.6666
  stop_lon            : 17.9039
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : opole

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 99.6815
  local_score_raw     : 1.8974

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 6203303.0177
  raw_gravity         : 5639366.3797
  domain_count        : 1
  infra_score_log     : 15.6406

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 41.8571
  hourly_freq         : 21.0714
  transit_freq_log    : 3.7579

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 8185.8872
  liquidity           : 34.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 1670
  pop_val_log         : 7.4212
```
</details>
<details><summary><b>Paszport Węzła: Niemodlińska - Koszyka (217) (H3: 891e23c44d7ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Niemodlińska - Koszyka (217)
  stop_id             : 217
  city                : opole
  h3_index            : 891e23c44d7ffff
  stop_lat            : 50.6666
  stop_lon            : 17.9045
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : opole

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 99.6815
  local_score_raw     : 1.8974

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 6203303.0177
  raw_gravity         : 5639366.3797
  domain_count        : 1
  infra_score_log     : 15.6406

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 41.8571
  hourly_freq         : 20.7857
  transit_freq_log    : 3.7579

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 8185.8872
  liquidity           : 34.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 1670
  pop_val_log         : 7.4212
```
</details>

#### 🎲 RANDOM 5 (Środkowe przystanki miasta)
<details><summary><b>Paszport Węzła: Sobieskiego - Sołtysów (395) (H3: 891e23c609bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Sobieskiego - Sołtysów (395)
  stop_id             : 395
  city                : opole
  h3_index            : 891e23c609bffff
  stop_lat            : 50.7070
  stop_lon            : 17.9050
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : opole

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : D
  local_percentile    : 44.2675
  local_score_raw     : -0.2343

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 1148.1979
  raw_gravity         : 1148.1979
  domain_count        : 0
  infra_score_log     : 7.0468

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 9.0714
  hourly_freq         : 2.4286
  transit_freq_log    : 2.3097

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 2525.2525
  liquidity           : 1.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 93
  pop_val_log         : 4.5433
```
</details>
<details><summary><b>Paszport Węzła: Prószkowska - Wiosenna (468) (H3: 891e23c46a3ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Prószkowska - Wiosenna (468)
  stop_id             : 468
  city                : opole
  h3_index            : 891e23c46a3ffff
  stop_lat            : 50.6500
  stop_lon            : 17.9061
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : opole

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : C
  local_percentile    : 67.8344
  local_score_raw     : 0.1645

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 527.9240
  raw_gravity         : 527.9240
  domain_count        : 0
  infra_score_log     : 6.2708

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 9.4286
  hourly_freq         : 4.8571
  transit_freq_log    : 2.3445

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 7915.9935
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 69
  pop_val_log         : 4.2485
```
</details>
<details><summary><b>Paszport Węzła: Polska Nowa Wieś - Cmentarz (297) (H3: 891e23c0d2fffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Polska Nowa Wieś - Cmentarz (297)
  stop_id             : 297
  city                : opole
  h3_index            : 891e23c0d2fffff
  stop_lat            : 50.6371
  stop_lon            : 17.8076
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : opole

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : D
  local_percentile    : 41.7197
  local_score_raw     : -0.2719

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 294.4637
  raw_gravity         : 294.4637
  domain_count        : 0
  infra_score_log     : 5.6885

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 2.7857
  hourly_freq         : 1.4286
  transit_freq_log    : 1.3312

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 7915.9935
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 91
  pop_val_log         : 4.5218
```
</details>
<details><summary><b>Paszport Węzła: Mikołajczyka (524) (H3: 891e23c63afffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Mikołajczyka (524)
  stop_id             : 524
  city                : opole
  h3_index            : 891e23c63afffff
  stop_lat            : 50.6829
  stop_lon            : 17.9441
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : opole

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : B
  local_percentile    : 83.7580
  local_score_raw     : 0.7574

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 4965347.4936
  raw_gravity         : 4513952.2669
  domain_count        : 1
  infra_score_log     : 15.4180

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 4.0714
  hourly_freq         : 2.0000
  transit_freq_log    : 1.6236

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 7915.9935
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 42
  pop_val_log         : 3.7612
```
</details>
<details><summary><b>Paszport Węzła: Marka z Jemielnicy - Aleja Przyjaźni (195) (H3: 891e23c40afffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Marka z Jemielnicy - Aleja Przyjaźni (195)
  stop_id             : 195
  city                : opole
  h3_index            : 891e23c40afffff
  stop_lat            : 50.6473
  stop_lon            : 17.9424
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : opole

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : B
  local_percentile    : 70.3822
  local_score_raw     : 0.2239

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 441.8050
  raw_gravity         : 441.8050
  domain_count        : 0
  infra_score_log     : 6.0931

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 19.0000
  hourly_freq         : 4.8571
  transit_freq_log    : 2.9957

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 4824.5614
  liquidity           : 1.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 285
  pop_val_log         : 5.6560
```
</details>

#### 💩 BOTTOM 5 (Najsłabsze 5 przystanków)
<details><summary><b>Paszport Węzła: Częstochowska - Działki Pętla (68) (H3: 891e23c6b83ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Częstochowska - Działki Pętla (68)
  stop_id             : 68
  city                : opole
  h3_index            : 891e23c6b83ffff
  stop_lat            : 50.6723
  stop_lon            : 18.0139
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : opole

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 1.2739
  local_score_raw     : -1.1222

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 63.5576
  raw_gravity         : 63.5576
  domain_count        : 0
  infra_score_log     : 4.1676

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.4286
  hourly_freq         : 0.4286
  transit_freq_log    : 0.3567

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 7915.9935
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Kępska - MZK (146) (H3: 891e23c603bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Kępska - MZK (146)
  stop_id             : 146
  city                : opole
  h3_index            : 891e23c603bffff
  stop_lat            : 50.6952
  stop_lon            : 17.9203
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : opole

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.9554
  local_score_raw     : -1.1252

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 254.6959
  raw_gravity         : 254.6959
  domain_count        : 0
  infra_score_log     : 5.5440

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.0000
  hourly_freq         : 0.0000
  transit_freq_log    : 0.0000

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 7915.9935
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Kępska - MZK (145) (H3: 891e23c603bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Kępska - MZK (145)
  stop_id             : 145
  city                : opole
  h3_index            : 891e23c603bffff
  stop_lat            : 50.6953
  stop_lon            : 17.9203
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : opole

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.9554
  local_score_raw     : -1.1252

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 254.6959
  raw_gravity         : 254.6959
  domain_count        : 0
  infra_score_log     : 5.5440

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.0000
  hourly_freq         : 0.0000
  transit_freq_log    : 0.0000

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 7915.9935
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Wrocławska - Kościół (511) (H3: 891e23c7483ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Wrocławska - Kościół (511)
  stop_id             : 511
  city                : opole
  h3_index            : 891e23c7483ffff
  stop_lat            : 50.6850
  stop_lon            : 17.8207
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : opole

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.6369
  local_score_raw     : -1.1765

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 474.2218
  raw_gravity         : 474.2218
  domain_count        : 0
  infra_score_log     : 6.1638

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 1.4286
  hourly_freq         : 1.4286
  transit_freq_log    : 0.8873

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 467.7998
  liquidity           : 1.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 18
  pop_val_log         : 2.9444
```
</details>
<details><summary><b>Paszport Węzła: Luboszycka - Harcerska (174) (H3: 891e23c6313ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Luboszycka - Harcerska (174)
  stop_id             : 174
  city                : opole
  h3_index            : 891e23c6313ffff
  stop_lat            : 50.6844
  stop_lon            : 17.9258
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : opole

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.3185
  local_score_raw     : -1.3716

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 92.0588
  raw_gravity         : 92.0588
  domain_count        : 0
  infra_score_log     : 4.5332

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 1.3571
  hourly_freq         : 1.3571
  transit_freq_log    : 0.8575

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 2531.6456
  liquidity           : 9.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>

---

## AGLOMERACJA: POZNAN
**Status:** ✅ SUKCES

### Faza 0: Stan Danych
- **Całkowita populacja w strefie miasta:** 1,361,470 (Baseline: 530,000) [✅ OK]
- **Ilość Transakcji RCN:** 105,538
- **Zakres Dat RCN:** 2020-01-01 do 9200-02-28
- **Ceny RCN (PLN/m²):** Średnia=10,720 | Mediana=7,849 | Max=497,835 | IQR=[5,919 - 10,020]
- **Infrastruktura OSM (Punkty):** 447,022
- **Infrastruktura OSM (Poligony/Budynki):** 585,107
- Baza transakcyjna `.gpkg` ustrukturyzowana poprawnie.

### Faza I & II: Pokrycie (Zero-Values)
- **Pustynia Populacyjna:** 911 (16.3%)
- **Pustynia Infrastrukturalna:** 23 (0.4%)
- **Głuche Przystanki:** 57 (1.0%)
- **Wskaźnik Fallback RCN:** 3339 (59.8%) (Mediana RCN dla miasta: 7543)

### Faza III: Udowodnione POI w Promieniu 500m

**Rzeczywiste TOP 20 zwalidowanych obiektów (Intersekcja bufor 500m):**

| Tag OSM | Zliczone (Ilość) | Prawdziwa Waga JSON | Całkowita Siła (Score) |
|---|---|---|---|
| `supermarket` | 4253 | 11,550,079.41 | **49,122,487,730.73** |
| `exhibition_centre` | 47 | 345,833,139.65 | **16,254,157,563.55** |
| `sports_centre` | 1699 | 1,299,897.25 | **2,208,525,427.75** |
| `marketplace` | 398 | 1,471,107.86 | **585,500,928.28** |
| `place_of_worship` | 3707 | 103,564.38 | **383,913,156.66** |
| `pharmacy` | 4903 | 69,078.62 | **338,692,473.86** |
| `bank` | 2840 | 74,227.25 | **210,805,390.00** |
| `post_office` | 1692 | 74,045.86 | **125,285,595.12** |
| `bench` | 113985 | 0.00 | **0.00** |
| `waste_basket` | 68582 | 0.00 | **0.00** |
| `bicycle_parking` | 28923 | 0.00 | **0.00** |
| `vending_machine` | 16202 | 0.00 | **0.00** |
| `parcel_locker` | 15290 | 0.00 | **0.00** |
| `restaurant` | 10171 | 0.00 | **0.00** |
| `recycling` | 6461 | 0.00 | **0.00** |
| `atm` | 5661 | 0.00 | **0.00** |
| `parking_entrance` | 5193 | 0.00 | **0.00** |
| `shelter` | 17711 | 0.00 | **0.00** |
| `waste_disposal` | 12138 | 0.00 | **0.00** |
| `fast_food` | 4809 | 0.00 | **0.00** |

### Faza IV: Badanie Próbek Oceny Złotej

#### 🏆 TOP 5 (Najlepsze 5 przystanków w mieście)
<details><summary><b>Paszport Węzła: Aleje Marcinkowskiego (H3: 891e24aa527ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Aleje Marcinkowskiego
  stop_id             : 121
  city                : poznan
  h3_index            : 891e24aa527ffff
  stop_lat            : 52.4073
  stop_lon            : 16.9289
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : poznan

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 5.2444

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 432138.7120
  raw_gravity         : 392853.3745
  domain_count        : 1.0000
  infra_score_log     : 12.9765

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 41.3571
  hourly_freq         : 41.3571
  transit_freq_log    : 3.7461

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 86464.5452
  liquidity           : 54.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 481
  pop_val_log         : 6.1779
```
</details>
<details><summary><b>Paszport Węzła: Koźmińska (H3: 891e24aa273ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Koźmińska
  stop_id             : 1040
  city                : poznan
  h3_index            : 891e24aa273ffff
  stop_lat            : 52.3692
  stop_lon            : 16.8766
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : poznan

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 99.9651
  local_score_raw     : 5.0504

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 7703546.6125
  raw_gravity         : 7003224.1932
  domain_count        : 1.0000
  infra_score_log     : 15.8572

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 6.5714
  hourly_freq         : 3.2857
  transit_freq_log    : 2.0244

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 89204.3932
  liquidity           : 9.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 344
  pop_val_log         : 5.8435
```
</details>
<details><summary><b>Paszport Węzła: Koźmińska (H3: 891e24aa273ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Koźmińska
  stop_id             : 1039
  city                : poznan
  h3_index            : 891e24aa273ffff
  stop_lat            : 52.3690
  stop_lon            : 16.8768
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : poznan

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 99.9651
  local_score_raw     : 5.0504

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 7703546.6125
  raw_gravity         : 7003224.1932
  domain_count        : 1.0000
  infra_score_log     : 15.8572

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 6.5714
  hourly_freq         : 3.2857
  transit_freq_log    : 2.0244

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 89204.3932
  liquidity           : 9.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 344
  pop_val_log         : 5.8435
```
</details>
<details><summary><b>Paszport Węzła: Pl. Wiosny Ludów (H3: 891e24a125bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Pl. Wiosny Ludów
  stop_id             : 167
  city                : poznan
  h3_index            : 891e24a125bffff
  stop_lat            : 52.4050
  stop_lon            : 16.9317
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : poznan

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 99.9302
  local_score_raw     : 2.4658

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 18583670.9363
  raw_gravity         : 14295131.4894
  domain_count        : 3.0000
  infra_score_log     : 16.7378

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 83.8571
  hourly_freq         : 15.5714
  transit_freq_log    : 4.4410

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 16684.6500
  liquidity           : 154.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 614
  pop_val_log         : 6.4216
```
</details>
<details><summary><b>Paszport Węzła: Pl. Wiosny Ludów (H3: 891e24a125bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Pl. Wiosny Ludów
  stop_id             : 168
  city                : poznan
  h3_index            : 891e24a125bffff
  stop_lat            : 52.4051
  stop_lon            : 16.9315
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : poznan

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 99.9302
  local_score_raw     : 2.4658

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 18583670.9363
  raw_gravity         : 14295131.4894
  domain_count        : 3.0000
  infra_score_log     : 16.7378

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 83.8571
  hourly_freq         : 15.6429
  transit_freq_log    : 4.4410

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 16684.6500
  liquidity           : 154.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 614
  pop_val_log         : 6.4216
```
</details>

#### 🎲 RANDOM 5 (Środkowe przystanki miasta)
<details><summary><b>Paszport Węzła: Murowana Goślina (H3: 891e24b0d6bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Murowana Goślina
  stop_id             : 7296
  city                : poznan
  h3_index            : 891e24b0d6bffff
  stop_lat            : 52.5748
  stop_lon            : 17.0155
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : pkp-kw

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : C
  local_percentile    : 67.7363
  local_score_raw     : 0.1865

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 628.2015
  raw_gravity         : 628.2015
  domain_count        : 0.0000
  infra_score_log     : 6.4445

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 7.1429
  hourly_freq         : 2.4286
  transit_freq_log    : 2.0971

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 8208.3662
  liquidity           : 5.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 228
  pop_val_log         : 5.4337
```
</details>
<details><summary><b>Paszport Węzła: Stobnicka (H3: 891e24b802fffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Stobnicka
  stop_id             : 587
  city                : poznan
  h3_index            : 891e24b802fffff
  stop_lat            : 52.4535
  stop_lon            : 16.8013
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : poznan

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : D
  local_percentile    : 47.6456
  local_score_raw     : -0.1538

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 144.3087
  raw_gravity         : 144.3087
  domain_count        : 0.0000
  infra_score_log     : 4.9789

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 10.0714
  hourly_freq         : 5.1429
  transit_freq_log    : 2.4044

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 7543.4661
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 4
  pop_val_log         : 1.6094
```
</details>
<details><summary><b>Paszport Węzła: Masłowo, Wieś NŻ (H3: 891e242aeafffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Masłowo, Wieś NŻ
  stop_id             : 285
  city                : poznan
  h3_index            : 891e242aeafffff
  stop_lat            : 52.0180
  stop_lon            : 17.0912
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : poznan-pks

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : D
  local_percentile    : 40.7394
  local_score_raw     : -0.2474

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 559.4933
  raw_gravity         : 559.4933
  domain_count        : 0.0000
  infra_score_log     : 6.3288

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 2.4286
  hourly_freq         : 2.4286
  transit_freq_log    : 1.2321

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 7543.4661
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 57
  pop_val_log         : 4.0604
```
</details>
<details><summary><b>Paszport Węzła: Wiry/Nowa (H3: 891e24a952bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Wiry/Nowa
  stop_id             : 943
  city                : poznan
  h3_index            : 891e24a952bffff
  stop_lat            : 52.3176
  stop_lon            : 16.8703
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : poznan

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : C
  local_percentile    : 66.4806
  local_score_raw     : 0.1598

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 1195.7495
  raw_gravity         : 1195.7495
  domain_count        : 0.0000
  infra_score_log     : 7.0874

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 3.7857
  hourly_freq         : 1.9286
  transit_freq_log    : 1.5656

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 9304.0293
  liquidity           : 14.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 390
  pop_val_log         : 5.9687
```
</details>
<details><summary><b>Paszport Węzła: Turowo (H3: 891e2488503ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Turowo
  stop_id             : 599
  city                : poznan
  h3_index            : 891e2488503ffff
  stop_lat            : 52.4586
  stop_lon            : 16.3040
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : poznan-pks

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : D
  local_percentile    : 27.7642
  local_score_raw     : -0.4190

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 316.8763
  raw_gravity         : 316.8763
  domain_count        : 0.0000
  infra_score_log     : 5.7617

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 3.6429
  hourly_freq         : 3.6429
  transit_freq_log    : 1.5353

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 1998.6741
  liquidity           : 2.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 118
  pop_val_log         : 4.7791
```
</details>

#### 💩 BOTTOM 5 (Najsłabsze 5 przystanków)
<details><summary><b>Paszport Węzła: Albertowsko, I (H3: 891e24c5b8fffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Albertowsko, I
  stop_id             : 857
  city                : poznan
  h3_index            : 891e24c5b8fffff
  stop_lat            : 52.2523
  stop_lon            : 16.2018
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : poznan-pks

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.1744
  local_score_raw     : -1.3991

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 0.0000
  raw_gravity         : 0.0000
  domain_count        : 0.0000
  infra_score_log     : 0.0000

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.6429
  hourly_freq         : 0.1429
  transit_freq_log    : 0.4964

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 7543.4661
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Iłówiec Wielki, III (H3: 891e2405a47ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Iłówiec Wielki, III
  stop_id             : 922
  city                : poznan
  h3_index            : 891e2405a47ffff
  stop_lat            : 52.1407
  stop_lon            : 16.7904
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : poznan-pks

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.1395
  local_score_raw     : -1.4300

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 0.0000
  raw_gravity         : 0.0000
  domain_count        : 0.0000
  infra_score_log     : 0.0000

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.5000
  hourly_freq         : 0.5000
  transit_freq_log    : 0.4055

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 7543.4661
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Borzejewo (H3: 891e25d9627ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Borzejewo
  stop_id             : 3:332:00
  city                : poznan
  h3_index            : 891e25d9627ffff
  stop_lat            : 52.3170
  stop_lon            : 17.3249
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : poznan-sroda

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.1046
  local_score_raw     : -1.4315

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 51.9097
  raw_gravity         : 51.9097
  domain_count        : 0.0000
  infra_score_log     : 3.9686

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.2143
  hourly_freq         : 0.2143
  transit_freq_log    : 0.1942

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 1050.9563
  liquidity           : 2.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Dębicz/Pałac (H3: 891e2436323ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Dębicz/Pałac
  stop_id             : 3:176:03
  city                : poznan
  h3_index            : 891e2436323ffff
  stop_lat            : 52.2619
  stop_lon            : 17.3049
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : poznan-sroda

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.0698
  local_score_raw     : -1.4465

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 0.0000
  raw_gravity         : 0.0000
  domain_count        : 0.0000
  infra_score_log     : 0.0000

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.4286
  hourly_freq         : 0.4286
  transit_freq_log    : 0.3567

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 7543.4661
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Aleksandrów (H3: 891e2425ea3ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Aleksandrów
  stop_id             : SW:07:00
  city                : poznan
  h3_index            : 891e2425ea3ffff
  stop_lat            : 52.0633
  stop_lon            : 17.4094
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : poznan-sroda

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.0349
  local_score_raw     : -1.5017

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 0.0000
  raw_gravity         : 0.0000
  domain_count        : 0.0000
  infra_score_log     : 0.0000

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.2143
  hourly_freq         : 0.2143
  transit_freq_log    : 0.1942

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 7543.4661
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>

---

## AGLOMERACJA: PRZEMYSL
**Status:** ✅ SUKCES

### Faza 0: Stan Danych
- **Całkowita populacja w strefie miasta:** 71,214 (Baseline: 60,000) [✅ OK]
- **Ilość Transakcji RCN:** 902
- **Zakres Dat RCN:** 2024-01-01 do 2027-09-29
- **Ceny RCN (PLN/m²):** Średnia=7,653 | Mediana=6,157 | Max=177,518 | IQR=[3,737 - 7,672]
- **Infrastruktura OSM (Punkty):** 11,795
- **Infrastruktura OSM (Poligony/Budynki):** 33,805
- Baza transakcyjna `.gpkg` ustrukturyzowana poprawnie.

### Faza I & II: Pokrycie (Zero-Values)
- **Pustynia Populacyjna:** 13 (4.2%)
- **Pustynia Infrastrukturalna:** 0 (0.0%)
- **Głuche Przystanki:** 0 (0.0%)
- **Wskaźnik Fallback RCN:** 207 (66.8%) (Mediana RCN dla miasta: 6142)

### Faza III: Udowodnione POI w Promieniu 500m

**Rzeczywiste TOP 20 zwalidowanych obiektów (Intersekcja bufor 500m):**

| Tag OSM | Zliczone (Ilość) | Prawdziwa Waga JSON | Całkowita Siła (Score) |
|---|---|---|---|
| `supermarket` | 220 | 9,801,324.02 | **2,156,291,284.40** |
| `marketplace` | 38 | 1,679,434.93 | **63,818,527.34** |
| `sports_centre` | 50 | 1,172,422.09 | **58,621,104.50** |
| `place_of_worship` | 387 | 78,735.71 | **30,470,719.77** |
| `pharmacy` | 272 | 58,344.32 | **15,869,655.04** |
| `bank` | 231 | 61,074.35 | **14,108,174.85** |
| `post_office` | 101 | 61,446.56 | **6,206,102.56** |
| `bench` | 1899 | 0.00 | **0.00** |
| `shelter` | 1011 | 0.00 | **0.00** |
| `waste_basket` | 376 | 0.00 | **0.00** |
| `atm` | 329 | 0.00 | **0.00** |
| `fast_food` | 434 | 0.00 | **0.00** |
| `restaurant` | 419 | 0.00 | **0.00** |
| `parcel_locker` | 217 | 0.00 | **0.00** |
| `pub` | 169 | 0.00 | **0.00** |
| `doctors` | 235 | 0.00 | **0.00** |
| `cafe` | 169 | 0.00 | **0.00** |
| `parking` | 5308 | 0.00 | **0.00** |
| `parking_entrance` | 120 | 0.00 | **0.00** |
| `bicycle_parking` | 128 | 0.00 | **0.00** |

### Faza IV: Badanie Próbek Oceny Złotej

#### 🏆 TOP 5 (Najlepsze 5 przystanków w mieście)
<details><summary><b>Paszport Węzła: Krasińskiego - PL. Konstytucji - Kier. Centrum (H3: 891e2b16b23ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Krasińskiego - PL. Konstytucji - Kier. Centrum
  stop_id             : 479
  city                : przemysl
  h3_index            : 891e2b16b23ffff
  stop_lat            : 49.7865
  stop_lon            : 22.7672
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : przemysl

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 1.9459

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 351257.9393
  raw_gravity         : 292714.9494
  domain_count        : 2
  infra_score_log     : 12.7693

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 17.7857
  hourly_freq         : 1.7143
  transit_freq_log    : 2.9331

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 5945.3782
  liquidity           : 3.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 1262
  pop_val_log         : 7.1412
```
</details>
<details><summary><b>Paszport Węzła: Grunwaldzka - PL. Konstytucji - Kier. Ostrów (H3: 891e2b16b23ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Grunwaldzka - PL. Konstytucji - Kier. Ostrów
  stop_id             : 44
  city                : przemysl
  h3_index            : 891e2b16b23ffff
  stop_lat            : 49.7865
  stop_lon            : 22.7648
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : przemysl

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 1.9459

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 351257.9393
  raw_gravity         : 292714.9494
  domain_count        : 2
  infra_score_log     : 12.7693

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 17.7857
  hourly_freq         : 4.7143
  transit_freq_log    : 2.9331

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 5945.3782
  liquidity           : 3.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 1262
  pop_val_log         : 7.1412
```
</details>
<details><summary><b>Paszport Węzła: Grunwaldzka - PL. Konstytucji - Kier. Centrum (H3: 891e2b16b23ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Grunwaldzka - PL. Konstytucji - Kier. Centrum
  stop_id             : 43
  city                : przemysl
  h3_index            : 891e2b16b23ffff
  stop_lat            : 49.7864
  stop_lon            : 22.7650
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : przemysl

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 1.9459

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 351257.9393
  raw_gravity         : 292714.9494
  domain_count        : 2
  infra_score_log     : 12.7693

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 17.7857
  hourly_freq         : 4.7143
  transit_freq_log    : 2.9331

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 5945.3782
  liquidity           : 3.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 1262
  pop_val_log         : 7.1412
```
</details>
<details><summary><b>Paszport Węzła: Krasińskiego - PL. Konstytucji - Kier. Buszkowice (H3: 891e2b16b23ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Krasińskiego - PL. Konstytucji - Kier. Buszkowice
  stop_id             : 42
  city                : przemysl
  h3_index            : 891e2b16b23ffff
  stop_lat            : 49.7864
  stop_lon            : 22.7671
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : przemysl

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 1.9459

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 351257.9393
  raw_gravity         : 292714.9494
  domain_count        : 2
  infra_score_log     : 12.7693

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 17.7857
  hourly_freq         : 1.7857
  transit_freq_log    : 2.9331

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 5945.3782
  liquidity           : 3.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 1262
  pop_val_log         : 7.1412
```
</details>
<details><summary><b>Paszport Węzła: 3 - GO MAJA - DOM Handlowy - Kier. Centrum (H3: 891e2b16b23ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : 3 - GO MAJA - DOM Handlowy - Kier. Centrum
  stop_id             : 3
  city                : przemysl
  h3_index            : 891e2b16b23ffff
  stop_lat            : 49.7878
  stop_lon            : 22.7663
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : przemysl

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 1.9459

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 351257.9393
  raw_gravity         : 292714.9494
  domain_count        : 2
  infra_score_log     : 12.7693

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 17.7857
  hourly_freq         : 2.4286
  transit_freq_log    : 2.9331

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 5945.3782
  liquidity           : 3.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 1262
  pop_val_log         : 7.1412
```
</details>

#### 🎲 RANDOM 5 (Środkowe przystanki miasta)
<details><summary><b>Paszport Węzła: Sanocka - Kruhel Wielki - Kier. Centrum (H3: 891e2b14c17ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Sanocka - Kruhel Wielki - Kier. Centrum
  stop_id             : 70
  city                : przemysl
  h3_index            : 891e2b14c17ffff
  stop_lat            : 49.7743
  stop_lon            : 22.7415
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : przemysl

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : C
  local_percentile    : 50.0000
  local_score_raw     : -0.1128

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 302.7631
  raw_gravity         : 302.7631
  domain_count        : 0
  infra_score_log     : 5.7162

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 2.0714
  hourly_freq         : 1.0714
  transit_freq_log    : 1.1221

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6141.8478
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 41
  pop_val_log         : 3.7377
```
</details>
<details><summary><b>Paszport Węzła: Grochowce SKR - Kier. Przemyśl (H3: 891e2b14aafffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Grochowce SKR - Kier. Przemyśl
  stop_id             : 376
  city                : przemysl
  h3_index            : 891e2b14aafffff
  stop_lat            : 49.7377
  stop_lon            : 22.7466
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : przemysl

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : D
  local_percentile    : 31.3953
  local_score_raw     : -0.3966

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 404.3758
  raw_gravity         : 404.3758
  domain_count        : 0
  infra_score_log     : 6.0048

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.5714
  hourly_freq         : 0.2857
  transit_freq_log    : 0.4520

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6141.8478
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 104
  pop_val_log         : 4.6540
```
</details>
<details><summary><b>Paszport Węzła: Grochowce Wieś - Kier. Przemyśl (H3: 891e2b14b53ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Grochowce Wieś - Kier. Przemyśl
  stop_id             : 374
  city                : przemysl
  h3_index            : 891e2b14b53ffff
  stop_lat            : 49.7325
  stop_lon            : 22.7543
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : przemysl

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : D
  local_percentile    : 30.2326
  local_score_raw     : -0.4181

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 500.9796
  raw_gravity         : 500.9796
  domain_count        : 0
  infra_score_log     : 6.2186

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.5714
  hourly_freq         : 0.2857
  transit_freq_log    : 0.4520

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6141.8478
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 61
  pop_val_log         : 4.1271
```
</details>
<details><summary><b>Paszport Węzła: Ostrów I - Kier. Przemyśl (H3: 891e2b16a07ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Ostrów I - Kier. Przemyśl
  stop_id             : 473
  city                : przemysl
  h3_index            : 891e2b16a07ffff
  stop_lat            : 49.7908
  stop_lon            : 22.7245
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : przemysl

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : C
  local_percentile    : 52.9070
  local_score_raw     : -0.0508

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 1013.0445
  raw_gravity         : 1013.0445
  domain_count        : 0
  infra_score_log     : 6.9217

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 1.3571
  hourly_freq         : 0.7143
  transit_freq_log    : 0.8575

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6141.8478
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 120
  pop_val_log         : 4.7958
```
</details>
<details><summary><b>Paszport Węzła: Lwowska - Sanwil - Kier. Centrum (H3: 891e2bab043ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Lwowska - Sanwil - Kier. Centrum
  stop_id             : 147
  city                : przemysl
  h3_index            : 891e2bab043ffff
  stop_lat            : 49.7834
  stop_lon            : 22.8135
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : przemysl

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : C
  local_percentile    : 53.4884
  local_score_raw     : -0.0484

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 818.6792
  raw_gravity         : 818.6792
  domain_count        : 0
  infra_score_log     : 6.7089

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 1.7143
  hourly_freq         : 1.7143
  transit_freq_log    : 0.9985

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6141.8478
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 60
  pop_val_log         : 4.1109
```
</details>

#### 💩 BOTTOM 5 (Najsłabsze 5 przystanków)
<details><summary><b>Paszport Węzła: Malhowice PKP N / Ż (H3: 891e2ba92afffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Malhowice PKP N / Ż
  stop_id             : 355
  city                : przemysl
  h3_index            : 891e2ba92afffff
  stop_lat            : 49.7182
  stop_lon            : 22.8329
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : przemysl

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 2.3256
  local_score_raw     : -1.0485

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 75.8254
  raw_gravity         : 75.8254
  domain_count        : 0
  infra_score_log     : 4.3415

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.3571
  hourly_freq         : 0.3571
  transit_freq_log    : 0.3054

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6141.8478
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Łuczyce II N / Ż - Kier. Przemyśl (H3: 891e2ba9467ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Łuczyce II N / Ż - Kier. Przemyśl
  stop_id             : 300
  city                : przemysl
  h3_index            : 891e2ba9467ffff
  stop_lat            : 49.7430
  stop_lon            : 22.8279
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : przemysl

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 1.7442
  local_score_raw     : -1.0737

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 20.1802
  raw_gravity         : 20.1802
  domain_count        : 0
  infra_score_log     : 3.0531

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.6429
  hourly_freq         : 0.3571
  transit_freq_log    : 0.4964

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6141.8478
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Łuczyce II N / Ż - Kier. Rożubowice (H3: 891e2ba9467ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Łuczyce II N / Ż - Kier. Rożubowice
  stop_id             : 301
  city                : przemysl
  h3_index            : 891e2ba9467ffff
  stop_lat            : 49.7432
  stop_lon            : 22.8274
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : przemysl

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 1.7442
  local_score_raw     : -1.0737

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 20.1802
  raw_gravity         : 20.1802
  domain_count        : 0
  infra_score_log     : 3.0531

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.6429
  hourly_freq         : 0.2857
  transit_freq_log    : 0.4964

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6141.8478
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Malhowice III N / Ż (H3: 891e2ba9227ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Malhowice III N / Ż
  stop_id             : 677
  city                : przemysl
  h3_index            : 891e2ba9227ffff
  stop_lat            : 49.7130
  stop_lon            : 22.8366
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : przemysl

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 1.1628
  local_score_raw     : -1.1238

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 36.8057
  raw_gravity         : 36.8057
  domain_count        : 0
  infra_score_log     : 3.6325

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.3571
  hourly_freq         : 0.3571
  transit_freq_log    : 0.3054

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6141.8478
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Hermanowice N / Ż - Kier. Malhowice (H3: 891e2ba962bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Hermanowice N / Ż - Kier. Malhowice
  stop_id             : 342
  city                : przemysl
  h3_index            : 891e2ba962bffff
  stop_lat            : 49.7282
  stop_lon            : 22.8112
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : przemysl

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.5814
  local_score_raw     : -1.1966

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 3.9578
  raw_gravity         : 3.9578
  domain_count        : 0
  infra_score_log     : 1.6010

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.2857
  hourly_freq         : 0.2857
  transit_freq_log    : 0.2513

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6141.8478
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 7
  pop_val_log         : 2.0794
```
</details>

---

## AGLOMERACJA: RADOM
**Status:** ✅ SUKCES

### Faza 0: Stan Danych
- **Całkowita populacja w strefie miasta:** 239,185 (Baseline: 200,000) [✅ OK]
- **Ilość Transakcji RCN:** 4,179
- **Zakres Dat RCN:** 2021-07-12 do 2026-01-28
- **Ceny RCN (PLN/m²):** Średnia=6,672 | Mediana=6,553 | Max=105,973 | IQR=[5,226 - 7,938]
- **Infrastruktura OSM (Punkty):** 127,473
- **Infrastruktura OSM (Poligony/Budynki):** 123,433
- Baza transakcyjna `.gpkg` ustrukturyzowana poprawnie.

### Faza I & II: Pokrycie (Zero-Values)
- **Pustynia Populacyjna:** 47 (6.5%)
- **Pustynia Infrastrukturalna:** 0 (0.0%)
- **Głuche Przystanki:** 41 (5.6%)
- **Wskaźnik Fallback RCN:** 465 (64.0%) (Mediana RCN dla miasta: 6488)

### Faza III: Udowodnione POI w Promieniu 500m

**Rzeczywiste TOP 20 zwalidowanych obiektów (Intersekcja bufor 500m):**

| Tag OSM | Zliczone (Ilość) | Prawdziwa Waga JSON | Całkowita Siła (Score) |
|---|---|---|---|
| `supermarket` | 594 | 10,257,185.49 | **6,092,768,181.06** |
| `sports_centre` | 235 | 963,531.13 | **226,429,815.55** |
| `marketplace` | 78 | 1,658,798.40 | **129,386,275.20** |
| `place_of_worship` | 945 | 88,875.81 | **83,987,640.45** |
| `bank` | 824 | 62,238.56 | **51,284,573.44** |
| `pharmacy` | 771 | 62,066.94 | **47,853,610.74** |
| `post_office` | 311 | 63,008.04 | **19,595,500.44** |
| `bench` | 25271 | 0.00 | **0.00** |
| `bicycle_parking` | 7801 | 0.00 | **0.00** |
| `waste_basket` | 6141 | 0.00 | **0.00** |
| `recycling` | 3418 | 0.00 | **0.00** |
| `waste_disposal` | 3459 | 0.00 | **0.00** |
| `shelter` | 3223 | 0.00 | **0.00** |
| `vending_machine` | 1723 | 0.00 | **0.00** |
| `restaurant` | 1695 | 0.00 | **0.00** |
| `parcel_locker` | 1723 | 0.00 | **0.00** |
| `parking_entrance` | 1346 | 0.00 | **0.00** |
| `atm` | 712 | 0.00 | **0.00** |
| `fast_food` | 746 | 0.00 | **0.00** |
| `dentist` | 686 | 0.00 | **0.00** |

### Faza IV: Badanie Próbek Oceny Złotej

#### 🏆 TOP 5 (Najlepsze 5 przystanków w mieście)
<details><summary><b>Paszport Węzła: Chrobrego / Rapackiego (H3: 891e2c040a7ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Chrobrego / Rapackiego
  stop_id             : 63
  city                : radom
  h3_index            : 891e2c040a7ffff
  stop_lat            : 51.4222
  stop_lon            : 21.1629
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : radom

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 2.0314

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 9444380.2473
  raw_gravity         : 7870316.8727
  domain_count        : 2
  infra_score_log     : 16.0609

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 21.0714
  hourly_freq         : 9.0000
  transit_freq_log    : 3.0943

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 7782.4944
  liquidity           : 3.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 1473
  pop_val_log         : 7.2957
```
</details>
<details><summary><b>Paszport Węzła: Chrobrego / Rapackiego (H3: 891e2c040a7ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Chrobrego / Rapackiego
  stop_id             : 159
  city                : radom
  h3_index            : 891e2c040a7ffff
  stop_lat            : 51.4213
  stop_lon            : 21.1628
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : radom

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 2.0314

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 9444380.2473
  raw_gravity         : 7870316.8727
  domain_count        : 2
  infra_score_log     : 16.0609

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 21.0714
  hourly_freq         : 8.9286
  transit_freq_log    : 3.0943

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 7782.4944
  liquidity           : 3.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 1473
  pop_val_log         : 7.2957
```
</details>
<details><summary><b>Paszport Węzła: Rapackiego / Chrobrego (H3: 891e2c040a7ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Rapackiego / Chrobrego
  stop_id             : 700
  city                : radom
  h3_index            : 891e2c040a7ffff
  stop_lat            : 51.4219
  stop_lon            : 21.1646
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : radom

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 2.0314

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 9444380.2473
  raw_gravity         : 7870316.8727
  domain_count        : 2
  infra_score_log     : 16.0609

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 21.0714
  hourly_freq         : 3.1429
  transit_freq_log    : 3.0943

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 7782.4944
  liquidity           : 3.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 1473
  pop_val_log         : 7.2957
```
</details>
<details><summary><b>Paszport Węzła: 11 Listopada / Starowolska (H3: 891e2c04023ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : 11 Listopada / Starowolska
  stop_id             : 54
  city                : radom
  h3_index            : 891e2c04023ffff
  stop_lat            : 51.4141
  stop_lon            : 21.1586
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : radom

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 99.7531
  local_score_raw     : 1.7296

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 14282443.3253
  raw_gravity         : 12984039.3866
  domain_count        : 1
  infra_score_log     : 16.4745

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 17.6429
  hourly_freq         : 2.7857
  transit_freq_log    : 2.9255

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6378.8660
  liquidity           : 39.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 1396
  pop_val_log         : 7.2421
```
</details>
<details><summary><b>Paszport Węzła: Chrobrego / Sowińskiego (H3: 891e2c04023ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Chrobrego / Sowińskiego
  stop_id             : 155
  city                : radom
  h3_index            : 891e2c04023ffff
  stop_lat            : 51.4124
  stop_lon            : 21.1600
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : radom

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 99.7531
  local_score_raw     : 1.7296

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 14282443.3253
  raw_gravity         : 12984039.3866
  domain_count        : 1
  infra_score_log     : 16.4745

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 17.6429
  hourly_freq         : 6.0714
  transit_freq_log    : 2.9255

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6378.8660
  liquidity           : 39.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 1396
  pop_val_log         : 7.2421
```
</details>

#### 🎲 RANDOM 5 (Środkowe przystanki miasta)
<details><summary><b>Paszport Węzła: Antoniówka (H3: 891e2c3363bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Antoniówka
  stop_id             : 1521
  city                : radom
  h3_index            : 891e2c3363bffff
  stop_lat            : 51.4304
  stop_lon            : 21.2797
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : radom

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : D
  local_percentile    : 31.6049
  local_score_raw     : -0.4324

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 569.8492
  raw_gravity         : 569.8492
  domain_count        : 0
  infra_score_log     : 6.3471

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 1.3571
  hourly_freq         : 0.2857
  transit_freq_log    : 0.8575

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6487.5104
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 57
  pop_val_log         : 4.0604
```
</details>
<details><summary><b>Paszport Węzła: Brata Alberta / Ostrowiecka (H3: 891e2c05893ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Brata Alberta / Ostrowiecka
  stop_id             : 1348
  city                : radom
  h3_index            : 891e2c05893ffff
  stop_lat            : 51.3737
  stop_lon            : 21.1589
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : radom

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : B
  local_percentile    : 75.8025
  local_score_raw     : 0.4212

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 73544.7607
  raw_gravity         : 73544.7607
  domain_count        : 0
  infra_score_log     : 11.2057

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 10.7143
  hourly_freq         : 5.3571
  transit_freq_log    : 2.4608

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 3699.9984
  liquidity           : 2.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 789
  pop_val_log         : 6.6720
```
</details>
<details><summary><b>Paszport Węzła: Kozienicka / Gryczana (NŻ) (H3: 891e2c04123ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Kozienicka / Gryczana (NŻ)
  stop_id             : 312
  city                : radom
  h3_index            : 891e2c04123ffff
  stop_lat            : 51.4126
  stop_lon            : 21.1938
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : radom

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : C
  local_percentile    : 50.8642
  local_score_raw     : -0.0619

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 1120.8079
  raw_gravity         : 1120.8079
  domain_count        : 0
  infra_score_log     : 7.0227

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 3.2143
  hourly_freq         : 3.2143
  transit_freq_log    : 1.4385

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6487.5104
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 116
  pop_val_log         : 4.7622
```
</details>
<details><summary><b>Paszport Węzła: Godowska / Godna (NŻ) (H3: 891e2c0588bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Godowska / Godna (NŻ)
  stop_id             : 799
  city                : radom
  h3_index            : 891e2c0588bffff
  stop_lat            : 51.3685
  stop_lon            : 21.1585
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : radom

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : D
  local_percentile    : 47.4074
  local_score_raw     : -0.1330

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 1174.9501
  raw_gravity         : 1174.9501
  domain_count        : 0
  infra_score_log     : 7.0698

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 2.9286
  hourly_freq         : 1.5000
  transit_freq_log    : 1.3683

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6487.5104
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 64
  pop_val_log         : 4.1744
```
</details>
<details><summary><b>Paszport Węzła: Bielicha II (H3: 891e2c07323ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Bielicha II
  stop_id             : 1867
  city                : radom
  h3_index            : 891e2c07323ffff
  stop_lat            : 51.4141
  stop_lon            : 21.0905
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : radom

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : D
  local_percentile    : 44.4444
  local_score_raw     : -0.1826

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 1553.3534
  raw_gravity         : 1553.3534
  domain_count        : 0
  infra_score_log     : 7.3488

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 1.8571
  hourly_freq         : 0.9286
  transit_freq_log    : 1.0498

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6487.5104
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 129
  pop_val_log         : 4.8675
```
</details>

#### 💩 BOTTOM 5 (Najsłabsze 5 przystanków)
<details><summary><b>Paszport Węzła: Kończyce-Kolonia (H3: 891e2c05207ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Kończyce-Kolonia
  stop_id             : 1077
  city                : radom
  h3_index            : 891e2c05207ffff
  stop_lat            : 51.3642
  stop_lon            : 21.0621
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : radom

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.7407
  local_score_raw     : -1.2247

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 197.8411
  raw_gravity         : 197.8411
  domain_count        : 0
  infra_score_log     : 5.2925

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.0000
  hourly_freq         : 0.0000
  transit_freq_log    : 0.0000

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6487.5104
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Kozłów I (NŻ) (H3: 891e2c068afffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Kozłów I (NŻ)
  stop_id             : 902
  city                : radom
  h3_index            : 891e2c068afffff
  stop_lat            : 51.4521
  stop_lon            : 21.2321
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : radom

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.4938
  local_score_raw     : -1.2583

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 143.3047
  raw_gravity         : 143.3047
  domain_count        : 0
  infra_score_log     : 4.9719

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.0000
  hourly_freq         : 0.0000
  transit_freq_log    : 0.0000

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6487.5104
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Kozłów I (NŻ) (H3: 891e2c068afffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Kozłów I (NŻ)
  stop_id             : 903
  city                : radom
  h3_index            : 891e2c068afffff
  stop_lat            : 51.4520
  stop_lon            : 21.2319
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : radom

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.4938
  local_score_raw     : -1.2583

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 143.3047
  raw_gravity         : 143.3047
  domain_count        : 0
  infra_score_log     : 4.9719

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.0000
  hourly_freq         : 0.0000
  transit_freq_log    : 0.0000

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6487.5104
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Grzmucin I (NŻ) (H3: 891e2c3a5a3ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Grzmucin I (NŻ)
  stop_id             : 743
  city                : radom
  h3_index            : 891e2c3a5a3ffff
  stop_lat            : 51.3660
  stop_lon            : 21.2810
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : radom

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.2469
  local_score_raw     : -1.3226

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 77.1708
  raw_gravity         : 77.1708
  domain_count        : 0
  infra_score_log     : 4.3589

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.0000
  hourly_freq         : 0.0000
  transit_freq_log    : 0.0000

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6487.5104
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Grzmucin I (NŻ) (H3: 891e2c3a5a3ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Grzmucin I (NŻ)
  stop_id             : 744
  city                : radom
  h3_index            : 891e2c3a5a3ffff
  stop_lat            : 51.3660
  stop_lon            : 21.2807
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : radom

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.2469
  local_score_raw     : -1.3226

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 77.1708
  raw_gravity         : 77.1708
  domain_count        : 0
  infra_score_log     : 4.3589

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.0000
  hourly_freq         : 0.0000
  transit_freq_log    : 0.0000

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6487.5104
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>

---

## AGLOMERACJA: RZESZOW
**Status:** ✅ SUKCES

### Faza 0: Stan Danych
- **Całkowita populacja w strefie miasta:** 439,622 (Baseline: 190,000) [✅ OK]
- **Ilość Transakcji RCN:** 12,298
- **Zakres Dat RCN:** 2020-01-07 do 2027-04-28
- **Ceny RCN (PLN/m²):** Średnia=10,168 | Mediana=8,240 | Max=477,621 | IQR=[6,000 - 10,449]
- **Infrastruktura OSM (Punkty):** 105,012
- **Infrastruktura OSM (Poligony/Budynki):** 295,048
- Baza transakcyjna `.gpkg` ustrukturyzowana poprawnie.

### Faza I & II: Pokrycie (Zero-Values)
- **Pustynia Populacyjna:** 149 (5.7%)
- **Pustynia Infrastrukturalna:** 0 (0.0%)
- **Głuche Przystanki:** 33 (1.3%)
- **Wskaźnik Fallback RCN:** 2087 (80.4%) (Mediana RCN dla miasta: 8110)

### Faza III: Udowodnione POI w Promieniu 500m

**Rzeczywiste TOP 20 zwalidowanych obiektów (Intersekcja bufor 500m):**

| Tag OSM | Zliczone (Ilość) | Prawdziwa Waga JSON | Całkowita Siła (Score) |
|---|---|---|---|
| `supermarket` | 1385 | 8,932,258.84 | **12,371,178,493.40** |
| `sports_centre` | 346 | 1,324,261.88 | **458,194,610.48** |
| `marketplace` | 100 | 1,479,453.41 | **147,945,341.00** |
| `place_of_worship` | 1105 | 102,491.34 | **113,252,930.70** |
| `pharmacy` | 1436 | 63,585.85 | **91,309,280.60** |
| `bank` | 959 | 75,740.79 | **72,635,417.61** |
| `post_office` | 477 | 69,762.79 | **33,276,850.83** |
| `bench` | 40893 | 0.00 | **0.00** |
| `waste_basket` | 21825 | 0.00 | **0.00** |
| `bicycle_parking` | 3977 | 0.00 | **0.00** |
| `parking_entrance` | 2908 | 0.00 | **0.00** |
| `parcel_locker` | 2454 | 0.00 | **0.00** |
| `recycling` | 2697 | 0.00 | **0.00** |
| `shelter` | 2908 | 0.00 | **0.00** |
| `restaurant` | 2238 | 0.00 | **0.00** |
| `fast_food` | 1505 | 0.00 | **0.00** |
| `vending_machine` | 1314 | 0.00 | **0.00** |
| `school` | 2439 | 0.00 | **0.00** |
| `atm` | 1015 | 0.00 | **0.00** |
| `training` | 1031 | 0.00 | **0.00** |

### Faza IV: Badanie Próbek Oceny Złotej

#### 🏆 TOP 5 (Najlepsze 5 przystanków w mieście)
<details><summary><b>Paszport Węzła: Rejtana / Armii Krajowej 12 (H3: 891e286c8dbffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Rejtana / Armii Krajowej 12
  stop_id             : 124
  city                : rzeszow
  h3_index            : 891e286c8dbffff
  stop_lat            : 50.0195
  stop_lon            : 22.0175
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : rzeszow

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 6.8390

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 12463492.0636
  raw_gravity         : 9587301.5874
  domain_count        : 3
  infra_score_log     : 16.3383

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 22.7857
  hourly_freq         : 17.2143
  transit_freq_log    : 3.1691

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 164319.2488
  liquidity           : 91.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 109
  pop_val_log         : 4.7005
```
</details>
<details><summary><b>Paszport Węzła: Rejtana / Armii Krajowej 12 (H3: 891e286c8dbffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Rejtana / Armii Krajowej 12
  stop_id             : 1504
  city                : rzeszow
  h3_index            : 891e286c8dbffff
  stop_lat            : 50.0196
  stop_lon            : 22.0174
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : rzeszow-pks

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 6.8390

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 12463492.0636
  raw_gravity         : 9587301.5874
  domain_count        : 3
  infra_score_log     : 16.3383

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 22.7857
  hourly_freq         : 5.5714
  transit_freq_log    : 3.1691

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 164319.2488
  liquidity           : 91.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 109
  pop_val_log         : 4.7005
```
</details>
<details><summary><b>Paszport Węzła: Rzeszów D.A. 0 (H3: 891e286ccd3ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Rzeszów D.A. 0
  stop_id             : 65
  city                : rzeszow
  h3_index            : 891e286ccd3ffff
  stop_lat            : 50.0421
  stop_lon            : 22.0043
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : rzeszow-pks

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 99.9235
  local_score_raw     : 2.7258

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 20341868.8426
  raw_gravity         : 15647591.4174
  domain_count        : 3
  infra_score_log     : 16.8282

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 188.6429
  hourly_freq         : 28.9286
  transit_freq_log    : 5.2451

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 16747.5456
  liquidity           : 33.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 260
  pop_val_log         : 5.5645
```
</details>
<details><summary><b>Paszport Węzła: Rzeszów D.A. 10 (H3: 891e286ccd3ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Rzeszów D.A. 10
  stop_id             : 58
  city                : rzeszow
  h3_index            : 891e286ccd3ffff
  stop_lat            : 50.0421
  stop_lon            : 22.0031
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : rzeszow-pks

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 99.9235
  local_score_raw     : 2.7258

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 20341868.8426
  raw_gravity         : 15647591.4174
  domain_count        : 3
  infra_score_log     : 16.8282

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 188.6429
  hourly_freq         : 52.8571
  transit_freq_log    : 5.2451

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 16747.5456
  liquidity           : 33.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 260
  pop_val_log         : 5.5645
```
</details>
<details><summary><b>Paszport Węzła: Rzeszów D.A. 3 (H3: 891e286ccd3ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Rzeszów D.A. 3
  stop_id             : 66
  city                : rzeszow
  h3_index            : 891e286ccd3ffff
  stop_lat            : 50.0424
  stop_lon            : 22.0037
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : rzeszow-pks

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 99.9235
  local_score_raw     : 2.7258

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 20341868.8426
  raw_gravity         : 15647591.4174
  domain_count        : 3
  infra_score_log     : 16.8282

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 188.6429
  hourly_freq         : 28.3571
  transit_freq_log    : 5.2451

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 16747.5456
  liquidity           : 33.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 260
  pop_val_log         : 5.5645
```
</details>

#### 🎲 RANDOM 5 (Środkowe przystanki miasta)
<details><summary><b>Paszport Węzła: Rudna Mała hotel 03 (H3: 891e286e1dbffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Rudna Mała hotel 03
  stop_id             : 537
  city                : rzeszow
  h3_index            : 891e286e1dbffff
  stop_lat            : 50.0934
  stop_lon            : 21.9546
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : rzeszow-pks

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : D
  local_percentile    : 29.0520
  local_score_raw     : -0.3984

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 294.4402
  raw_gravity         : 294.4402
  domain_count        : 0
  infra_score_log     : 5.6885

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 9.1429
  hourly_freq         : 4.5714
  transit_freq_log    : 2.3168

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 8110.0258
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Brzóza Królewska nadleśnictwo 07 (H3: 891e282886bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Brzóza Królewska nadleśnictwo 07
  stop_id             : 1252
  city                : rzeszow
  h3_index            : 891e282886bffff
  stop_lat            : 50.2548
  stop_lon            : 22.2931
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : rzeszow-pks

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : B
  local_percentile    : 80.1223
  local_score_raw     : 0.4526

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 6732971.9520
  raw_gravity         : 6120883.5927
  domain_count        : 1
  infra_score_log     : 15.7225

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 1.0000
  hourly_freq         : 0.5000
  transit_freq_log    : 0.6931

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 8110.0258
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 18
  pop_val_log         : 2.9444
```
</details>
<details><summary><b>Paszport Węzła: Zaczernie 04 (H3: 891e286e1a3ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Zaczernie 04
  stop_id             : 747
  city                : rzeszow
  h3_index            : 891e286e1a3ffff
  stop_lat            : 50.0949
  stop_lon            : 21.9802
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : rzeszow

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : B
  local_percentile    : 74.3119
  local_score_raw     : 0.3031

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 739.3088
  raw_gravity         : 739.3088
  domain_count        : 0
  infra_score_log     : 6.6071

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 16.1429
  hourly_freq         : 1.9286
  transit_freq_log    : 2.8416

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 8110.0258
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 65
  pop_val_log         : 4.1897
```
</details>
<details><summary><b>Paszport Węzła: Wieniawskiego / Dunikowskiego 10 (H3: 891e286c87bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Wieniawskiego / Dunikowskiego 10
  stop_id             : 998
  city                : rzeszow
  h3_index            : 891e286c87bffff
  stop_lat            : 50.0092
  stop_lon            : 22.0359
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : rzeszow

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : B
  local_percentile    : 70.4893
  local_score_raw     : 0.2295

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 1166.7237
  raw_gravity         : 1166.7237
  domain_count        : 0
  infra_score_log     : 7.0628

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 5.5000
  hourly_freq         : 5.5000
  transit_freq_log    : 1.8718

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 10856.1220
  liquidity           : 9.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 228
  pop_val_log         : 5.4337
```
</details>
<details><summary><b>Paszport Węzła: Zaczernie - Miłocin 05 (H3: 891e286ee93ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Zaczernie - Miłocin 05
  stop_id             : 700
  city                : rzeszow
  h3_index            : 891e286ee93ffff
  stop_lat            : 50.0829
  stop_lon            : 21.9849
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : rzeszow

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : D
  local_percentile    : 33.0275
  local_score_raw     : -0.3381

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 271.6313
  raw_gravity         : 271.6313
  domain_count        : 0
  infra_score_log     : 5.6081

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 11.3571
  hourly_freq         : 2.2143
  transit_freq_log    : 2.5142

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 8110.0258
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>

#### 💩 BOTTOM 5 (Najsłabsze 5 przystanków)
<details><summary><b>Paszport Węzła: Wólka Sokołowska skrzyżowanie 02 (H3: 891e2829557ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Wólka Sokołowska skrzyżowanie 02
  stop_id             : 1045
  city                : rzeszow
  h3_index            : 891e2829557ffff
  stop_lat            : 50.2643
  stop_lon            : 22.1469
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : rzeszow-pks

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.3823
  local_score_raw     : -1.3870

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 19.5226
  raw_gravity         : 19.5226
  domain_count        : 0
  infra_score_log     : 3.0215

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.4286
  hourly_freq         : 0.4286
  transit_freq_log    : 0.3567

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 8110.0258
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Głogów Małopolski Południowy (H3: 891e286528bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Głogów Małopolski Południowy
  stop_id             : 280424
  city                : rzeszow
  h3_index            : 891e286528bffff
  stop_lat            : 50.1135
  stop_lon            : 21.9859
  lat_grid            : 50.1100
  lon_grid            : 21.9900
  norm_name           : gogowmaopolskipoudniowy
  source              : polish_trains

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.3058
  local_score_raw     : -1.3917

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 58.8641
  raw_gravity         : 58.8641
  domain_count        : 0
  infra_score_log     : 4.0921

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.0000
  hourly_freq         : 0.0000
  transit_freq_log    : 0.0000

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 8110.0258
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Hyżne Nieborów Wygon 04 (H3: 891e2bd6b43ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Hyżne Nieborów Wygon 04
  stop_id             : 1578
  city                : rzeszow
  h3_index            : 891e2bd6b43ffff
  stop_lat            : 49.9196
  stop_lon            : 22.1439
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : rzeszow-pks

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.2294
  local_score_raw     : -1.3921

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 47.0888
  raw_gravity         : 47.0888
  domain_count        : 0
  infra_score_log     : 3.8731

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.0714
  hourly_freq         : 0.0714
  transit_freq_log    : 0.0690

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 8110.0258
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Kamień Krzywa Wieś / Markowska 11 (H3: 891e282b623ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Kamień Krzywa Wieś / Markowska 11
  stop_id             : 1038
  city                : rzeszow
  h3_index            : 891e282b623ffff
  stop_lat            : 50.3007
  stop_lon            : 22.0961
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : rzeszow-pks

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.1529
  local_score_raw     : -1.4509

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 4.1398
  raw_gravity         : 4.1398
  domain_count        : 0
  infra_score_log     : 1.6370

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.8571
  hourly_freq         : 0.8571
  transit_freq_log    : 0.6190

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 8110.0258
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Jasionka Airport (H3: 891e28653c3ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Jasionka Airport
  stop_id             : STRATEGIC
  city                : rzeszow
  h3_index            : 891e28653c3ffff
  stop_lat            : nan
  stop_lon            : nan
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : STRATEGIC_HUB

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.0765
  local_score_raw     : -1.6322

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 6.0768
  raw_gravity         : 6.0768
  domain_count        : 0
  infra_score_log     : 1.9568

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.0000
  hourly_freq         : 0.0000
  transit_freq_log    : 0.0000

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 8110.0258
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>

---

## AGLOMERACJA: SUWALKI
**Status:** ✅ SUKCES

### Faza 0: Stan Danych
- **Całkowita populacja w strefie miasta:** 74,387 (Baseline: 70,000) [✅ OK]
- **Ilość Transakcji RCN:** 1,306
- **Zakres Dat RCN:** 2021-04-27 do 2026-02-27
- **Ceny RCN (PLN/m²):** Średnia=6,166 | Mediana=6,168 | Max=48,207 | IQR=[3,785 - 8,258]
- **Infrastruktura OSM (Punkty):** 13,131
- **Infrastruktura OSM (Poligony/Budynki):** 25,017
- Baza transakcyjna `.gpkg` ustrukturyzowana poprawnie.

### Faza I & II: Pokrycie (Zero-Values)
- **Pustynia Populacyjna:** 71 (21.3%)
- **Pustynia Infrastrukturalna:** 0 (0.0%)
- **Głuche Przystanki:** 2 (0.6%)
- **Wskaźnik Fallback RCN:** 329 (98.8%) (Mediana RCN dla miasta: 6138)

### Faza III: Udowodnione POI w Promieniu 500m

**Rzeczywiste TOP 20 zwalidowanych obiektów (Intersekcja bufor 500m):**

| Tag OSM | Zliczone (Ilość) | Prawdziwa Waga JSON | Całkowita Siła (Score) |
|---|---|---|---|
| `supermarket` | 357 | 9,433,518.69 | **3,367,766,172.33** |
| `marketplace` | 21 | 1,876,115.68 | **39,398,429.28** |
| `pharmacy` | 350 | 55,449.30 | **19,407,255.00** |
| `place_of_worship` | 165 | 93,378.65 | **15,407,477.25** |
| `sports_centre` | 16 | 931,652.80 | **14,906,444.80** |
| `bank` | 237 | 58,623.96 | **13,893,878.52** |
| `post_office` | 47 | 75,042.36 | **3,526,990.92** |
| `bench` | 4837 | 0.00 | **0.00** |
| `waste_basket` | 1752 | 0.00 | **0.00** |
| `parcel_locker` | 491 | 0.00 | **0.00** |
| `restaurant` | 422 | 0.00 | **0.00** |
| `fast_food` | 427 | 0.00 | **0.00** |
| `atm` | 207 | 0.00 | **0.00** |
| `bicycle_rental` | 182 | 0.00 | **0.00** |
| `parking_space` | 12138 | 0.00 | **0.00** |
| `kindergarten` | 141 | 0.00 | **0.00** |
| `bicycle_parking` | 121 | 0.00 | **0.00** |
| `doctors` | 130 | 0.00 | **0.00** |
| `dentist` | 94 | 0.00 | **0.00** |
| `ice_cream` | 75 | 0.00 | **0.00** |

### Faza IV: Badanie Próbek Oceny Złotej

#### 🏆 TOP 5 (Najlepsze 5 przystanków w mieście)
<details><summary><b>Paszport Węzła: Dwernickiego / Plaza (01) (H3: 891f42d1a1bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Dwernickiego / Plaza (01)
  stop_id             : 2
  city                : suwalki
  h3_index            : 891f42d1a1bffff
  stop_lat            : 54.1068
  stop_lon            : 22.9330
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : suwalki

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 2.1505

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 6503933.5093
  raw_gravity         : 5003025.7764
  domain_count        : 3
  infra_score_log     : 15.6879

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 29.9286
  hourly_freq         : 6.9286
  transit_freq_log    : 3.4317

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6138.3483
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 1468
  pop_val_log         : 7.2923
```
</details>
<details><summary><b>Paszport Węzła: Noniewicza / Stokrotka (05) (H3: 891f42d1a1bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Noniewicza / Stokrotka (05)
  stop_id             : 3
  city                : suwalki
  h3_index            : 891f42d1a1bffff
  stop_lat            : 54.1052
  stop_lon            : 22.9318
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : suwalki

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 2.1505

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 6503933.5093
  raw_gravity         : 5003025.7764
  domain_count        : 3
  infra_score_log     : 15.6879

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 29.9286
  hourly_freq         : 8.5000
  transit_freq_log    : 3.4317

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6138.3483
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 1468
  pop_val_log         : 7.2923
```
</details>
<details><summary><b>Paszport Węzła: Dwernickiego / Os. Korczaka (02) (H3: 891f42d1a1bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Dwernickiego / Os. Korczaka (02)
  stop_id             : 94
  city                : suwalki
  h3_index            : 891f42d1a1bffff
  stop_lat            : 54.1069
  stop_lon            : 22.9339
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : suwalki

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 2.1505

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 6503933.5093
  raw_gravity         : 5003025.7764
  domain_count        : 3
  infra_score_log     : 15.6879

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 29.9286
  hourly_freq         : 8.0000
  transit_freq_log    : 3.4317

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6138.3483
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 1468
  pop_val_log         : 7.2923
```
</details>
<details><summary><b>Paszport Węzła: Noniewicza / Wigry (06) (H3: 891f42d1a1bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Noniewicza / Wigry (06)
  stop_id             : 17
  city                : suwalki
  h3_index            : 891f42d1a1bffff
  stop_lat            : 54.1051
  stop_lon            : 22.9315
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : suwalki

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 2.1505

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 6503933.5093
  raw_gravity         : 5003025.7764
  domain_count        : 3
  infra_score_log     : 15.6879

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 29.9286
  hourly_freq         : 6.5000
  transit_freq_log    : 3.4317

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6138.3483
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 1468
  pop_val_log         : 7.2923
```
</details>
<details><summary><b>Paszport Węzła: Kowalskiego / MERK (01) (H3: 891f42d18dbffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Kowalskiego / MERK (01)
  stop_id             : 304
  city                : suwalki
  h3_index            : 891f42d18dbffff
  stop_lat            : 54.1260
  stop_lon            : 22.9395
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : suwalki

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 99.4819
  local_score_raw     : 1.9254

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 4576437.8855
  raw_gravity         : 4160398.0777
  domain_count        : 1
  infra_score_log     : 15.3364

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 18.2143
  hourly_freq         : 9.5714
  transit_freq_log    : 2.9557

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6138.3483
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 1965
  pop_val_log         : 7.5838
```
</details>

#### 🎲 RANDOM 5 (Środkowe przystanki miasta)
<details><summary><b>Paszport Węzła: Sejneńska / 100 - Lecia Niepodległości (07) Nż (H3: 891f42d1b4bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Sejneńska / 100 - Lecia Niepodległości (07) Nż
  stop_id             : 23
  city                : suwalki
  h3_index            : 891f42d1b4bffff
  stop_lat            : 54.0978
  stop_lon            : 22.9615
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : suwalki

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : C
  local_percentile    : 60.1036
  local_score_raw     : 0.0274

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 424.7495
  raw_gravity         : 424.7495
  domain_count        : 0
  infra_score_log     : 6.0539

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 3.5000
  hourly_freq         : 3.4286
  transit_freq_log    : 1.5041

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6138.3483
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 3
  pop_val_log         : 1.3863
```
</details>
<details><summary><b>Paszport Węzła: Nowomiejska (03) (H3: 891f42d185bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Nowomiejska (03)
  stop_id             : 349
  city                : suwalki
  h3_index            : 891f42d185bffff
  stop_lat            : 54.1191
  stop_lon            : 22.9425
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : suwalki

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : B
  local_percentile    : 82.9016
  local_score_raw     : 0.8098

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 742.9898
  raw_gravity         : 742.9898
  domain_count        : 0
  infra_score_log     : 6.6120

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 10.2857
  hourly_freq         : 9.2857
  transit_freq_log    : 2.4235

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6138.3483
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 809
  pop_val_log         : 6.6970
```
</details>
<details><summary><b>Paszport Węzła: Jana Pawła II / Aquapark (02) (H3: 891f42d1a97ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Jana Pawła II / Aquapark (02)
  stop_id             : 379
  city                : suwalki
  h3_index            : 891f42d1a97ffff
  stop_lat            : 54.1142
  stop_lon            : 22.9399
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : suwalki

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : B
  local_percentile    : 79.7927
  local_score_raw     : 0.5395

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 585.8439
  raw_gravity         : 585.8439
  domain_count        : 0
  infra_score_log     : 6.3748

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 15.2857
  hourly_freq         : 0.3571
  transit_freq_log    : 2.7903

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6138.3483
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Ogrodowa (01) (H3: 891f42d1e6bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Ogrodowa (01)
  stop_id             : 429
  city                : suwalki
  h3_index            : 891f42d1e6bffff
  stop_lat            : 54.1143
  stop_lon            : 22.9208
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : suwalki

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : D
  local_percentile    : 38.8601
  local_score_raw     : -0.3717

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 324.7558
  raw_gravity         : 324.7558
  domain_count        : 0
  infra_score_log     : 5.7861

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.2143
  hourly_freq         : 0.2143
  transit_freq_log    : 0.1942

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6138.3483
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 110
  pop_val_log         : 4.7095
```
</details>
<details><summary><b>Paszport Węzła: Raczkowska / Urząd Celny (09) (H3: 891f42d8ddbffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Raczkowska / Urząd Celny (09)
  stop_id             : 29
  city                : suwalki
  h3_index            : 891f42d8ddbffff
  stop_lat            : 54.0589
  stop_lon            : 22.9001
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : suwalki

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : D
  local_percentile    : 49.2228
  local_score_raw     : -0.1459

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 166.2284
  raw_gravity         : 166.2284
  domain_count        : 0
  infra_score_log     : 5.1194

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 3.5000
  hourly_freq         : 1.2143
  transit_freq_log    : 1.5041

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6138.3483
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>

#### 💩 BOTTOM 5 (Najsłabsze 5 przystanków)
<details><summary><b>Paszport Węzła: Pułaskiego / Studzieniczne (16) (H3: 891f42d0367ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Pułaskiego / Studzieniczne (16)
  stop_id             : 121
  city                : suwalki
  h3_index            : 891f42d0367ffff
  stop_lat            : 54.1477
  stop_lon            : 22.9676
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : suwalki

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 1.5544
  local_score_raw     : -0.9752

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 10.6678
  raw_gravity         : 10.6678
  domain_count        : 0
  infra_score_log     : 2.4568

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.2143
  hourly_freq         : 0.2143
  transit_freq_log    : 0.1942

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6138.3483
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Płociczno / Szkoła (H3: 891f42c10c7ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Płociczno / Szkoła
  stop_id             : 312
  city                : suwalki
  h3_index            : 891f42c10c7ffff
  stop_lat            : 54.0222
  stop_lon            : 22.9826
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : suwalki

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 1.0363
  local_score_raw     : -1.6579

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 425.4668
  raw_gravity         : 425.4668
  domain_count        : 0
  infra_score_log     : 6.0555

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 1.0714
  hourly_freq         : 0.2857
  transit_freq_log    : 0.7282

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 2644.2308
  liquidity           : 5.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 73
  pop_val_log         : 4.3041
```
</details>
<details><summary><b>Paszport Węzła: Płociczno 11 (H3: 891f42c10c7ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Płociczno 11
  stop_id             : 146
  city                : suwalki
  h3_index            : 891f42c10c7ffff
  stop_lat            : 54.0232
  stop_lon            : 22.9812
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : suwalki

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 1.0363
  local_score_raw     : -1.6579

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 425.4668
  raw_gravity         : 425.4668
  domain_count        : 0
  infra_score_log     : 6.0555

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 1.0714
  hourly_freq         : 0.5000
  transit_freq_log    : 0.7282

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 2644.2308
  liquidity           : 5.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 73
  pop_val_log         : 4.3041
```
</details>
<details><summary><b>Paszport Węzła: Płociczno 10 (H3: 891f42c10c7ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Płociczno 10
  stop_id             : 59
  city                : suwalki
  h3_index            : 891f42c10c7ffff
  stop_lat            : 54.0235
  stop_lon            : 22.9812
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : suwalki

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 1.0363
  local_score_raw     : -1.6579

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 425.4668
  raw_gravity         : 425.4668
  domain_count        : 0
  infra_score_log     : 6.0555

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 1.0714
  hourly_freq         : 0.2857
  transit_freq_log    : 0.7282

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 2644.2308
  liquidity           : 5.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 73
  pop_val_log         : 4.3041
```
</details>
<details><summary><b>Paszport Węzła: Przebród / Osiedle16 P (H3: 891f42d8593ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Przebród / Osiedle16 P
  stop_id             : 152
  city                : suwalki
  h3_index            : 891f42d8593ffff
  stop_lat            : 54.0846
  stop_lon            : 22.8206
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : suwalki

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.5181
  local_score_raw     : -1.8099

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 138.9182
  raw_gravity         : 138.9182
  domain_count        : 0
  infra_score_log     : 4.9411

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.4286
  hourly_freq         : 0.4286
  transit_freq_log    : 0.3567

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 2852.9179
  liquidity           : 2.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 113
  pop_val_log         : 4.7362
```
</details>

---

## AGLOMERACJA: SWINOUJSCIE
**Status:** ✅ SUKCES

### Faza 0: Stan Danych
- **Całkowita populacja w strefie miasta:** 45,308 (Baseline: 40,000) [✅ OK]
- **Ilość Transakcji RCN:** 5,875
- **Zakres Dat RCN:** 2020-02-24 do 2026-03-09
- **Ceny RCN (PLN/m²):** Średnia=24,444 | Mediana=15,674 | Max=487,329 | IQR=[9,955 - 22,915]
- **Infrastruktura OSM (Punkty):** 10,427
- **Infrastruktura OSM (Poligony/Budynki):** 12,236
- Baza transakcyjna `.gpkg` ustrukturyzowana poprawnie.

### Faza I & II: Pokrycie (Zero-Values)
- **Pustynia Populacyjna:** 41 (21.1%)
- **Pustynia Infrastrukturalna:** 1 (0.5%)
- **Głuche Przystanki:** 1 (0.5%)
- **Wskaźnik Fallback RCN:** 94 (48.5%) (Mediana RCN dla miasta: 15459)

### Faza III: Udowodnione POI w Promieniu 500m

**Rzeczywiste TOP 20 zwalidowanych obiektów (Intersekcja bufor 500m):**

| Tag OSM | Zliczone (Ilość) | Prawdziwa Waga JSON | Całkowita Siła (Score) |
|---|---|---|---|
| `supermarket` | 241 | 7,575,875.38 | **1,825,785,966.58** |
| `sports_centre` | 23 | 1,194,617.01 | **27,476,191.23** |
| `marketplace` | 16 | 1,414,489.19 | **22,631,827.04** |
| `pharmacy` | 215 | 52,522.11 | **11,292,253.65** |
| `place_of_worship` | 120 | 83,121.81 | **9,974,617.20** |
| `bank` | 105 | 59,318.24 | **6,228,415.20** |
| `post_office` | 59 | 68,086.26 | **4,017,089.34** |
| `bench` | 4022 | 0.00 | **0.00** |
| `bicycle_parking` | 872 | 0.00 | **0.00** |
| `waste_basket` | 588 | 0.00 | **0.00** |
| `restaurant` | 606 | 0.00 | **0.00** |
| `parking_space` | 5241 | 0.00 | **0.00** |
| `parking_entrance` | 280 | 0.00 | **0.00** |
| `atm` | 258 | 0.00 | **0.00** |
| `cafe` | 288 | 0.00 | **0.00** |
| `shelter` | 268 | 0.00 | **0.00** |
| `fast_food` | 351 | 0.00 | **0.00** |
| `parcel_locker` | 188 | 0.00 | **0.00** |
| `bureau_de_change` | 184 | 0.00 | **0.00** |
| `vending_machine` | 148 | 0.00 | **0.00** |

### Faza IV: Badanie Próbek Oceny Złotej

#### 🏆 TOP 5 (Najlepsze 5 przystanków w mieście)
<details><summary><b>Paszport Węzła: Plac Kościelny (H3: 891f0ec7317ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Plac Kościelny
  stop_id             : 135
  city                : swinoujscie
  h3_index            : 891f0ec7317ffff
  stop_lat            : 53.9083
  stop_lon            : 14.2468
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : swinoujscie

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 1.7843

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 11402036.7390
  raw_gravity         : 8770797.4915
  domain_count        : 3.0000
  infra_score_log     : 16.2493

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 20.5714
  hourly_freq         : 5.0000
  transit_freq_log    : 3.0714

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 12338.6980
  liquidity           : 32.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 481.0000
  pop_val_log         : 6.1779
```
</details>
<details><summary><b>Paszport Węzła: Port (H3: 891f0ec7317ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Port
  stop_id             : 83
  city                : swinoujscie
  h3_index            : 891f0ec7317ffff
  stop_lat            : 53.9073
  stop_lon            : 14.2495
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : swinoujscie

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 1.7843

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 11402036.7390
  raw_gravity         : 8770797.4915
  domain_count        : 3.0000
  infra_score_log     : 16.2493

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 20.5714
  hourly_freq         : 5.2857
  transit_freq_log    : 3.0714

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 12338.6980
  liquidity           : 32.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 481.0000
  pop_val_log         : 6.1779
```
</details>
<details><summary><b>Paszport Węzła: Plac Kościelny (H3: 891f0ec7317ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Plac Kościelny
  stop_id             : 81
  city                : swinoujscie
  h3_index            : 891f0ec7317ffff
  stop_lat            : 53.9084
  stop_lon            : 14.2470
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : swinoujscie

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 1.7843

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 11402036.7390
  raw_gravity         : 8770797.4915
  domain_count        : 3.0000
  infra_score_log     : 16.2493

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 20.5714
  hourly_freq         : 4.2143
  transit_freq_log    : 3.0714

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 12338.6980
  liquidity           : 32.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 481.0000
  pop_val_log         : 6.1779
```
</details>
<details><summary><b>Paszport Węzła: Plac Wolności (H3: 891f0ec7317ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Plac Wolności
  stop_id             : 82
  city                : swinoujscie
  h3_index            : 891f0ec7317ffff
  stop_lat            : 53.9087
  stop_lon            : 14.2489
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : swinoujscie

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 1.7843

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 11402036.7390
  raw_gravity         : 8770797.4915
  domain_count        : 3.0000
  infra_score_log     : 16.2493

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 20.5714
  hourly_freq         : 6.0714
  transit_freq_log    : 3.0714

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 12338.6980
  liquidity           : 32.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 481.0000
  pop_val_log         : 6.1779
```
</details>
<details><summary><b>Paszport Węzła: Piastowska - kościół (H3: 891f0ec73bbffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Piastowska - kościół
  stop_id             : 192
  city                : swinoujscie
  h3_index            : 891f0ec73bbffff
  stop_lat            : 53.9104
  stop_lon            : 14.2507
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : swinoujscie

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 99.0099
  local_score_raw     : 1.5886

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 10857871.8637
  raw_gravity         : 8352209.1259
  domain_count        : 3.0000
  infra_score_log     : 16.2004

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 10.5000
  hourly_freq         : 3.7857
  transit_freq_log    : 2.4423

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 15766.6345
  liquidity           : 53.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 970.0000
  pop_val_log         : 6.8783
```
</details>

#### 🎲 RANDOM 5 (Środkowe przystanki miasta)
<details><summary><b>Paszport Węzła: Osiedle Krzywa (H3: 891f0ec5483ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Osiedle Krzywa
  stop_id             : 77
  city                : swinoujscie
  h3_index            : 891f0ec5483ffff
  stop_lat            : 53.8951
  stop_lon            : 14.2247
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : swinoujscie

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : C
  local_percentile    : 67.3267
  local_score_raw     : 0.2257

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 228.1980
  raw_gravity         : 228.1980
  domain_count        : 0.0000
  infra_score_log     : 5.4346

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 8.8571
  hourly_freq         : 4.4286
  transit_freq_log    : 2.2882

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 9596.4264
  liquidity           : 33.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 680.0000
  pop_val_log         : 6.5236
```
</details>
<details><summary><b>Paszport Węzła: Kołłątaja - Rynek (H3: 891f0ec73c7ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Kołłątaja - Rynek
  stop_id             : 48
  city                : swinoujscie
  h3_index            : 891f0ec73c7ffff
  stop_lat            : 53.9060
  stop_lon            : 14.2394
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : swinoujscie

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A
  local_percentile    : 85.1485
  local_score_raw     : 0.7782

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 6458155.5541
  raw_gravity         : 5381796.2951
  domain_count        : 2.0000
  infra_score_log     : 15.6809

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 3.4286
  hourly_freq         : 1.4286
  transit_freq_log    : 1.4881

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 9554.1699
  liquidity           : 28.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 661.0000
  pop_val_log         : 6.4953
```
</details>
<details><summary><b>Paszport Węzła: Karsiborska / Steyera (H3: 891f0ec54b3ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Karsiborska / Steyera
  stop_id             : 198
  city                : swinoujscie
  h3_index            : 891f0ec54b3ffff
  stop_lat            : 53.8956
  stop_lon            : 14.2376
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : swinoujscie

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : C
  local_percentile    : 62.3762
  local_score_raw     : 0.1473

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 160.0220
  raw_gravity         : 160.0220
  domain_count        : 0.0000
  infra_score_log     : 5.0815

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 11.9286
  hourly_freq         : 5.9286
  transit_freq_log    : 2.5594

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 15459.4556
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0.0000
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Świnoujście Port (H3: 891f0ec732fffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Świnoujście Port
  stop_id             : 1073
  city                : swinoujscie
  h3_index            : 891f0ec732fffff
  stop_lat            : 53.9012
  stop_lon            : 14.2601
  lat_grid            : 53.9000
  lon_grid            : 14.2600
  norm_name           : swinoujscieport
  source              : polish_trains

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : C
  local_percentile    : 68.3168
  local_score_raw     : 0.2360

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 1206.9637
  raw_gravity         : 1206.9637
  domain_count        : 0.0000
  infra_score_log     : 7.0967

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 9.6429
  hourly_freq         : 0.0000
  transit_freq_log    : 2.3649

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 15459.4556
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0.0000
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Uzdrowiskowa - Promenada (H3: 891f0ec7147ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Uzdrowiskowa - Promenada
  stop_id             : 86
  city                : swinoujscie
  h3_index            : 891f0ec7147ffff
  stop_lat            : 53.9190
  stop_lon            : 14.2573
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : swinoujscie

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : B
  local_percentile    : 83.1683
  local_score_raw     : 0.6737

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 716.8141
  raw_gravity         : 716.8141
  domain_count        : 0.0000
  infra_score_log     : 6.5762

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 10.7143
  hourly_freq         : 5.3571
  transit_freq_log    : 2.4608

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 22022.8385
  liquidity           : 45.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 35.0000
  pop_val_log         : 3.5835
```
</details>

#### 💩 BOTTOM 5 (Najsłabsze 5 przystanków)
<details><summary><b>Paszport Węzła: Mostowa / Pomorska (H3: 891f0ec516bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Mostowa / Pomorska
  stop_id             : 87
  city                : swinoujscie
  h3_index            : 891f0ec516bffff
  stop_lat            : 53.8632
  stop_lon            : 14.2874
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : swinoujscie

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 4.9505
  local_score_raw     : -0.9287

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 68.8801
  raw_gravity         : 68.8801
  domain_count        : 0.0000
  infra_score_log     : 4.2468

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 1.1429
  hourly_freq         : 1.1429
  transit_freq_log    : 0.7621

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 15459.4556
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0.0000
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Świnoujście Warszów (H3: 891f0ec4663ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Świnoujście Warszów
  stop_id             : 1057
  city                : swinoujscie
  h3_index            : 891f0ec4663ffff
  stop_lat            : 53.9004
  stop_lon            : 14.2853
  lat_grid            : 53.9000
  lon_grid            : 14.2900
  norm_name           : swinoujsciewarszow
  source              : polish_trains

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 3.9604
  local_score_raw     : -0.9419

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 443.3763
  raw_gravity         : 443.3763
  domain_count        : 0.0000
  infra_score_log     : 6.0967

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.0000
  hourly_freq         : 0.0000
  transit_freq_log    : 0.0000

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 15459.4556
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 44.0000
  pop_val_log         : 3.8067
```
</details>
<details><summary><b>Paszport Węzła: Ludzi Morza / Wrzosowa (H3: 891f0ec42dbffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Ludzi Morza / Wrzosowa
  stop_id             : 57
  city                : swinoujscie
  h3_index            : 891f0ec42dbffff
  stop_lat            : 53.8925
  stop_lon            : 14.2842
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : swinoujscie

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 2.9703
  local_score_raw     : -0.9707

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 54.0333
  raw_gravity         : 54.0333
  domain_count        : 0.0000
  infra_score_log     : 4.0079

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 1.0714
  hourly_freq         : 1.0714
  transit_freq_log    : 0.7282

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 15459.4556
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0.0000
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Krzywa - Ogrody (H3: 891f0ec5413ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Krzywa - Ogrody
  stop_id             : 50
  city                : swinoujscie
  h3_index            : 891f0ec5413ffff
  stop_lat            : 53.8888
  stop_lon            : 14.2235
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : swinoujscie

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 1.9802
  local_score_raw     : -0.9971

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 0.0000
  raw_gravity         : 0.0000
  domain_count        : 0.0000
  infra_score_log     : 0.0000

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 3.0000
  hourly_freq         : 3.0000
  transit_freq_log    : 1.3863

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 15459.4556
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0.0000
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Wolińska - Przystań Żeglarska (H3: 891f0ec4c47ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Wolińska - Przystań Żeglarska
  stop_id             : 139
  city                : swinoujscie
  h3_index            : 891f0ec4c47ffff
  stop_lat            : 53.9070
  stop_lon            : 14.3883
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : swinoujscie

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.9901
  local_score_raw     : -1.1301

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 23.8941
  raw_gravity         : 23.8941
  domain_count        : 0.0000
  infra_score_log     : 3.2146

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.7857
  hourly_freq         : 0.7857
  transit_freq_log    : 0.5798

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 15459.4556
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0.0000
  pop_val_log         : 0.0000
```
</details>

---

## AGLOMERACJA: SZCZECIN
**Status:** ✅ SUKCES

### Faza 0: Stan Danych
- **Całkowita populacja w strefie miasta:** 511,323 (Baseline: 400,000) [✅ OK]
- **Ilość Transakcji RCN:** 45,297
- **Zakres Dat RCN:** 2020-01-02 do 2026-02-27
- **Ceny RCN (PLN/m²):** Średnia=10,345 | Mediana=6,980 | Max=499,631 | IQR=[5,061 - 9,020]
- **Infrastruktura OSM (Punkty):** 337,672
- **Infrastruktura OSM (Poligony/Budynki):** 148,669
- Baza transakcyjna `.gpkg` ustrukturyzowana poprawnie.

### Faza I & II: Pokrycie (Zero-Values)
- **Pustynia Populacyjna:** 320 (18.0%)
- **Pustynia Infrastrukturalna:** 0 (0.0%)
- **Głuche Przystanki:** 32 (1.8%)
- **Wskaźnik Fallback RCN:** 728 (41.0%) (Mediana RCN dla miasta: 6788)

### Faza III: Udowodnione POI w Promieniu 500m

**Rzeczywiste TOP 20 zwalidowanych obiektów (Intersekcja bufor 500m):**

| Tag OSM | Zliczone (Ilość) | Prawdziwa Waga JSON | Całkowita Siła (Score) |
|---|---|---|---|
| `supermarket` | 2248 | 10,316,319.61 | **23,191,086,483.28** |
| `sports_centre` | 563 | 1,182,493.18 | **665,743,660.34** |
| `marketplace` | 306 | 1,334,813.67 | **408,452,983.02** |
| `pharmacy` | 2512 | 63,588.23 | **159,733,633.76** |
| `place_of_worship` | 1496 | 98,855.04 | **147,887,139.84** |
| `bank` | 1964 | 67,776.87 | **133,113,772.68** |
| `post_office` | 1035 | 66,555.78 | **68,885,232.30** |
| `bench` | 49324 | 0.00 | **0.00** |
| `waste_basket` | 15843 | 0.00 | **0.00** |
| `bicycle_parking` | 12063 | 0.00 | **0.00** |
| `recycling` | 6246 | 0.00 | **0.00** |
| `vending_machine` | 5780 | 0.00 | **0.00** |
| `restaurant` | 6071 | 0.00 | **0.00** |
| `parking_entrance` | 5310 | 0.00 | **0.00** |
| `parcel_locker` | 4696 | 0.00 | **0.00** |
| `fast_food` | 4865 | 0.00 | **0.00** |
| `waste_disposal` | 5068 | 0.00 | **0.00** |
| `shelter` | 6306 | 0.00 | **0.00** |
| `cafe` | 2442 | 0.00 | **0.00** |
| `atm` | 2238 | 0.00 | **0.00** |

### Faza IV: Badanie Próbek Oceny Złotej

#### 🏆 TOP 5 (Najlepsze 5 przystanków w mieście)
<details><summary><b>Paszport Węzła: Plac Rodła 26 (H3: 891f0e795abffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Plac Rodła 26
  stop_id             : 11526
  city                : szczecin
  h3_index            : 891f0e795abffff
  stop_lat            : 53.4314
  stop_lon            : 14.5566
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : szczecin

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 1.9830

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 7855852.0501
  raw_gravity         : 6042963.1155
  domain_count        : 3
  infra_score_log     : 15.8768

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 159.2143
  hourly_freq         : 0.0000
  transit_freq_log    : 5.0765

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 8656.4763
  liquidity           : 46.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 150.0000
  pop_val_log         : 5.0173
```
</details>
<details><summary><b>Paszport Węzła: Plac Rodła 25 (H3: 891f0e795abffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Plac Rodła 25
  stop_id             : 11525
  city                : szczecin
  h3_index            : 891f0e795abffff
  stop_lat            : 53.4315
  stop_lon            : 14.5557
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : szczecin

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 1.9830

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 7855852.0501
  raw_gravity         : 6042963.1155
  domain_count        : 3
  infra_score_log     : 15.8768

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 159.2143
  hourly_freq         : 0.0000
  transit_freq_log    : 5.0765

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 8656.4763
  liquidity           : 46.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 150.0000
  pop_val_log         : 5.0173
```
</details>
<details><summary><b>Paszport Węzła: Plac Rodła 27 (H3: 891f0e795abffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Plac Rodła 27
  stop_id             : 11527
  city                : szczecin
  h3_index            : 891f0e795abffff
  stop_lat            : 53.4313
  stop_lon            : 14.5563
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : szczecin

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 1.9830

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 7855852.0501
  raw_gravity         : 6042963.1155
  domain_count        : 3
  infra_score_log     : 15.8768

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 159.2143
  hourly_freq         : 4.0714
  transit_freq_log    : 5.0765

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 8656.4763
  liquidity           : 46.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 150.0000
  pop_val_log         : 5.0173
```
</details>
<details><summary><b>Paszport Węzła: Plac Rodła 12 (H3: 891f0e795abffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Plac Rodła 12
  stop_id             : 11512
  city                : szczecin
  h3_index            : 891f0e795abffff
  stop_lat            : 53.4324
  stop_lon            : 14.5546
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : szczecin

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 1.9830

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 7855852.0501
  raw_gravity         : 6042963.1155
  domain_count        : 3
  infra_score_log     : 15.8768

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 159.2143
  hourly_freq         : 17.7143
  transit_freq_log    : 5.0765

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 8656.4763
  liquidity           : 46.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 150.0000
  pop_val_log         : 5.0173
```
</details>
<details><summary><b>Paszport Węzła: Plac Rodła 11 (H3: 891f0e795abffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Plac Rodła 11
  stop_id             : 11511
  city                : szczecin
  h3_index            : 891f0e795abffff
  stop_lat            : 53.4324
  stop_lon            : 14.5545
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : szczecin

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 1.9830

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 7855852.0501
  raw_gravity         : 6042963.1155
  domain_count        : 3
  infra_score_log     : 15.8768

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 159.2143
  hourly_freq         : 17.1429
  transit_freq_log    : 5.0765

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 8656.4763
  liquidity           : 46.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 150.0000
  pop_val_log         : 5.0173
```
</details>

#### 🎲 RANDOM 5 (Środkowe przystanki miasta)
<details><summary><b>Paszport Węzła: Osiedle Bukowe 13 (H3: 891f0e6b51bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Osiedle Bukowe 13
  stop_id             : 84613
  city                : szczecin
  h3_index            : 891f0e6b51bffff
  stop_lat            : 53.3675
  stop_lon            : 14.6535
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : szczecin

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A
  local_percentile    : 87.2242
  local_score_raw     : 0.9119

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 118653.2528
  raw_gravity         : 98877.7107
  domain_count        : 2
  infra_score_log     : 11.6840

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 17.6429
  hourly_freq         : 6.0000
  transit_freq_log    : 2.9255

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 7171.7172
  liquidity           : 19.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 2057.0000
  pop_val_log         : 7.6295
```
</details>
<details><summary><b>Paszport Węzła: Thugutta 11 (H3: 891f0e7b123ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Thugutta 11
  stop_id             : 45111
  city                : szczecin
  h3_index            : 891f0e7b123ffff
  stop_lat            : 53.4614
  stop_lon            : 14.5575
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : szczecin

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : D
  local_percentile    : 45.2962
  local_score_raw     : -0.1499

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 11776.2360
  raw_gravity         : 11776.2360
  domain_count        : 0
  infra_score_log     : 9.3739

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 1.0000
  hourly_freq         : 1.0000
  transit_freq_log    : 0.6931

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6784.7720
  liquidity           : 11.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 464.0000
  pop_val_log         : 6.1420
```
</details>
<details><summary><b>Paszport Węzła: Frysztacka 91 (H3: 891f0e7907bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Frysztacka 91
  stop_id             : 21591
  city                : szczecin
  h3_index            : 891f0e7907bffff
  stop_lat            : 53.4046
  stop_lon            : 14.5270
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : szczecin

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : B
  local_percentile    : 70.2671
  local_score_raw     : 0.3388

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 682.0936
  raw_gravity         : 682.0936
  domain_count        : 0
  infra_score_log     : 6.5266

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 15.0000
  hourly_freq         : 15.0000
  transit_freq_log    : 2.7726

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 7180.1567
  liquidity           : 9.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 1086.0000
  pop_val_log         : 6.9912
```
</details>
<details><summary><b>Paszport Węzła: Wielgowo Borsucza 11 (H3: 891f0e61267ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Wielgowo Borsucza 11
  stop_id             : 74511
  city                : szczecin
  h3_index            : 891f0e61267ffff
  stop_lat            : 53.3992
  stop_lon            : 14.7728
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : szczecin

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : D
  local_percentile    : 30.1974
  local_score_raw     : -0.4427

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 471.9421
  raw_gravity         : 471.9421
  domain_count        : 0
  infra_score_log     : 6.1590

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 4.0000
  hourly_freq         : 2.0000
  transit_freq_log    : 1.6094

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 5535.9839
  liquidity           : 1.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 32.0000
  pop_val_log         : 3.4965
```
</details>
<details><summary><b>Paszport Węzła: Stołczyńska 11 (H3: 891f0e7a5a3ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Stołczyńska 11
  stop_id             : 41511
  city                : szczecin
  h3_index            : 891f0e7a5a3ffff
  stop_lat            : 53.5214
  stop_lon            : 14.6094
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : szczecin

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : D
  local_percentile    : 42.5087
  local_score_raw     : -0.2154

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 871.0454
  raw_gravity         : 871.0454
  domain_count        : 0
  infra_score_log     : 6.7708

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 9.8571
  hourly_freq         : 4.9286
  transit_freq_log    : 2.3848

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 3249.5402
  liquidity           : 3.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 357.0000
  pop_val_log         : 5.8805
```
</details>

#### 💩 BOTTOM 5 (Najsłabsze 5 przystanków)
<details><summary><b>Paszport Węzła: Święta (H3: 891f0e7148fffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Święta
  stop_id             : 114
  city                : szczecin
  h3_index            : 891f0e7148fffff
  stop_lat            : 53.5578
  stop_lon            : 14.6306
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : szczecin-goleniow

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.5807
  local_score_raw     : -1.2515

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 258.5472
  raw_gravity         : 258.5472
  domain_count        : 0
  infra_score_log     : 5.5589

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.1429
  hourly_freq         : 0.1429
  transit_freq_log    : 0.1335

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 1885.0987
  liquidity           : 5.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 119.0000
  pop_val_log         : 4.7875
```
</details>
<details><summary><b>Paszport Węzła: Borzysławiec I (H3: 891f0e7184bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Borzysławiec I
  stop_id             : 89
  city                : szczecin
  h3_index            : 891f0e7184bffff
  stop_lat            : 53.5151
  stop_lon            : 14.7277
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : szczecin-goleniow

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.4646
  local_score_raw     : -1.2879

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 18.3344
  raw_gravity         : 18.3344
  domain_count        : 0
  infra_score_log     : 2.9619

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.2143
  hourly_freq         : 0.2143
  transit_freq_log    : 0.1942

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6788.0196
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0.0000
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Łozienica Ferma Gil nż. (H3: 891f0e718afffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Łozienica Ferma Gil nż.
  stop_id             : 87
  city                : szczecin
  h3_index            : 891f0e718afffff
  stop_lat            : 53.5268
  stop_lon            : 14.7565
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : szczecin-goleniow

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.3484
  local_score_raw     : -1.2930

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 17.3172
  raw_gravity         : 17.3172
  domain_count        : 0
  infra_score_log     : 2.9078

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.2143
  hourly_freq         : 0.2143
  transit_freq_log    : 0.1942

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6788.0196
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0.0000
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Białuń (H3: 891f0e729afffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Białuń
  stop_id             : 1420
  city                : szczecin
  h3_index            : 891f0e729afffff
  stop_lat            : 53.6151
  stop_lon            : 14.8409
  lat_grid            : 53.6200
  lon_grid            : 14.8400
  norm_name           : biaun
  source              : polish_trains

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.2323
  local_score_raw     : -1.3162

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 26.7083
  raw_gravity         : 26.7083
  domain_count        : 0
  infra_score_log     : 3.3217

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.0000
  hourly_freq         : 0.0000
  transit_freq_log    : 0.0000

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6788.0196
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0.0000
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Grambow (H3: 891f0e4c237ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Grambow
  stop_id             : 179218
  city                : szczecin
  h3_index            : 891f0e4c237ffff
  stop_lat            : 53.4173
  stop_lon            : 14.3472
  lat_grid            : 53.4200
  lon_grid            : 14.3500
  norm_name           : grambow
  source              : polish_trains

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.1161
  local_score_raw     : -1.4709

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 4.3718
  raw_gravity         : 4.3718
  domain_count        : 0
  infra_score_log     : 1.6812

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.0000
  hourly_freq         : 0.0000
  transit_freq_log    : 0.0000

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6788.0196
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0.0000
  pop_val_log         : 0.0000
```
</details>

---

## AGLOMERACJA: TORUN
**Status:** ✅ SUKCES

### Faza 0: Stan Danych
- **Całkowita populacja w strefie miasta:** 255,210 (Baseline: 190,000) [✅ OK]
- **Ilość Transakcji RCN:** 16,216
- **Zakres Dat RCN:** 2020-01-02 do 2026-03-09
- **Ceny RCN (PLN/m²):** Średnia=7,837 | Mediana=6,738 | Max=439,560 | IQR=[4,620 - 8,884]
- **Infrastruktura OSM (Punkty):** 63,145
- **Infrastruktura OSM (Poligony/Budynki):** 112,555
- Baza transakcyjna `.gpkg` ustrukturyzowana poprawnie.

### Faza I & II: Pokrycie (Zero-Values)
- **Pustynia Populacyjna:** 144 (16.5%)
- **Pustynia Infrastrukturalna:** 1 (0.1%)
- **Głuche Przystanki:** 14 (1.6%)
- **Wskaźnik Fallback RCN:** 473 (54.1%) (Mediana RCN dla miasta: 6513)

### Faza III: Udowodnione POI w Promieniu 500m

**Rzeczywiste TOP 20 zwalidowanych obiektów (Intersekcja bufor 500m):**

| Tag OSM | Zliczone (Ilość) | Prawdziwa Waga JSON | Całkowita Siła (Score) |
|---|---|---|---|
| `supermarket` | 1061 | 9,226,060.24 | **9,788,849,914.64** |
| `sports_centre` | 263 | 1,122,212.60 | **295,141,913.80** |
| `marketplace` | 117 | 1,173,341.20 | **137,280,920.40** |
| `place_of_worship` | 694 | 88,584.22 | **61,477,448.68** |
| `pharmacy` | 863 | 61,912.10 | **53,430,142.30** |
| `bank` | 723 | 64,551.48 | **46,670,720.04** |
| `post_office` | 520 | 65,365.29 | **33,989,950.80** |
| `bench` | 12545 | 0.00 | **0.00** |
| `parking_entrance` | 4187 | 0.00 | **0.00** |
| `waste_basket` | 3239 | 0.00 | **0.00** |
| `parcel_locker` | 2463 | 0.00 | **0.00** |
| `waste_disposal` | 3658 | 0.00 | **0.00** |
| `restaurant` | 2374 | 0.00 | **0.00** |
| `bicycle_parking` | 2506 | 0.00 | **0.00** |
| `dentist` | 1344 | 0.00 | **0.00** |
| `doctors` | 1263 | 0.00 | **0.00** |
| `fast_food` | 1058 | 0.00 | **0.00** |
| `shelter` | 1664 | 0.00 | **0.00** |
| `atm` | 752 | 0.00 | **0.00** |
| `university` | 1177 | 0.00 | **0.00** |

### Faza IV: Badanie Próbek Oceny Złotej

#### 🏆 TOP 5 (Najlepsze 5 przystanków w mieście)
<details><summary><b>Paszport Węzła: Dworzec Wschodni (H3: 891f56529d3ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Dworzec Wschodni
  stop_id             : 3504
  city                : torun
  h3_index            : 891f56529d3ffff
  stop_lat            : 53.0252
  stop_lon            : 18.6341
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : torun

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 2.1552

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 121042.6252
  raw_gravity         : 100868.8544
  domain_count        : 2.0000
  infra_score_log     : 11.7039

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 97.2857
  hourly_freq         : 28.7857
  transit_freq_log    : 4.5879

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 14446.6681
  liquidity           : 2.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 178
  pop_val_log         : 5.1874
```
</details>
<details><summary><b>Paszport Węzła: Dworzec Wschodni (H3: 891f56529d3ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Dworzec Wschodni
  stop_id             : 35502
  city                : torun
  h3_index            : 891f56529d3ffff
  stop_lat            : 53.0240
  stop_lon            : 18.6354
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : torun

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 2.1552

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 121042.6252
  raw_gravity         : 100868.8544
  domain_count        : 2.0000
  infra_score_log     : 11.7039

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 97.2857
  hourly_freq         : 25.5000
  transit_freq_log    : 4.5879

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 14446.6681
  liquidity           : 2.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 178
  pop_val_log         : 5.1874
```
</details>
<details><summary><b>Paszport Węzła: Dworzec Wschodni (H3: 891f56529d3ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Dworzec Wschodni
  stop_id             : 3303
  city                : torun
  h3_index            : 891f56529d3ffff
  stop_lat            : 53.0252
  stop_lon            : 18.6335
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : torun

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 2.1552

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 121042.6252
  raw_gravity         : 100868.8544
  domain_count        : 2.0000
  infra_score_log     : 11.7039

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 97.2857
  hourly_freq         : 22.1429
  transit_freq_log    : 4.5879

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 14446.6681
  liquidity           : 2.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 178
  pop_val_log         : 5.1874
```
</details>
<details><summary><b>Paszport Węzła: Dworzec Wschodni (H3: 891f56529d3ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Dworzec Wschodni
  stop_id             : 3606
  city                : torun
  h3_index            : 891f56529d3ffff
  stop_lat            : 53.0250
  stop_lon            : 18.6341
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : torun

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 2.1552

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 121042.6252
  raw_gravity         : 100868.8544
  domain_count        : 2.0000
  infra_score_log     : 11.7039

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 97.2857
  hourly_freq         : 10.4286
  transit_freq_log    : 4.5879

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 14446.6681
  liquidity           : 2.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 178
  pop_val_log         : 5.1874
```
</details>
<details><summary><b>Paszport Węzła: Dworzec Wschodni (H3: 891f56529d3ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Dworzec Wschodni
  stop_id             : 3405
  city                : torun
  h3_index            : 891f56529d3ffff
  stop_lat            : 53.0249
  stop_lon            : 18.6339
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : torun

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 2.1552

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 121042.6252
  raw_gravity         : 100868.8544
  domain_count        : 2.0000
  infra_score_log     : 11.7039

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 97.2857
  hourly_freq         : 10.4286
  transit_freq_log    : 4.5879

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 14446.6681
  liquidity           : 2.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 178
  pop_val_log         : 5.1874
```
</details>

#### 🎲 RANDOM 5 (Środkowe przystanki miasta)
<details><summary><b>Paszport Węzła: Tofama (H3: 891f5652d27ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Tofama
  stop_id             : 4302
  city                : torun
  h3_index            : 891f5652d27ffff
  stop_lat            : 53.0350
  stop_lon            : 18.6531
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : torun

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : C
  local_percentile    : 53.9957
  local_score_raw     : -0.0402

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 811.8140
  raw_gravity         : 811.8140
  domain_count        : 0.0000
  infra_score_log     : 6.7005

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 21.4286
  hourly_freq         : 8.4286
  transit_freq_log    : 3.1103

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6513.0865
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Włocławska (H3: 891f5650dafffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Włocławska
  stop_id             : 17602
  city                : torun
  h3_index            : 891f5650dafffff
  stop_lat            : 52.9878
  stop_lon            : 18.6652
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : torun

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : D
  local_percentile    : 44.9244
  local_score_raw     : -0.2073

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 531.1118
  raw_gravity         : 531.1118
  domain_count        : 0.0000
  infra_score_log     : 6.2769

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 13.7857
  hourly_freq         : 6.9286
  transit_freq_log    : 2.6937

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6513.0865
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Gołębia (H3: 891f565282fffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Gołębia
  stop_id             : 13904
  city                : torun
  h3_index            : 891f565282fffff
  stop_lat            : 53.0156
  stop_lon            : 18.6314
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : torun

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A
  local_percentile    : 85.3132
  local_score_raw     : 0.8571

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 62242.1864
  raw_gravity         : 56583.8059
  domain_count        : 1.0000
  infra_score_log     : 11.0388

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 25.5714
  hourly_freq         : 0.0000
  transit_freq_log    : 3.2798

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6725.9188
  liquidity           : 109.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 726
  pop_val_log         : 6.5889
```
</details>
<details><summary><b>Paszport Węzła: Lubicz Górny - DK10 (H3: 891f56562afffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Lubicz Górny - DK10
  stop_id             : 99011
  city                : torun
  h3_index            : 891f56562afffff
  stop_lat            : 53.0254
  stop_lon            : 18.7751
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : torun

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : C
  local_percentile    : 68.6825
  local_score_raw     : 0.3162

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 10459702.1191
  raw_gravity         : 8045924.7070
  domain_count        : 3.0000
  infra_score_log     : 16.1630

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 1.2857
  hourly_freq         : 1.2857
  transit_freq_log    : 0.8267

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 5081.0597
  liquidity           : 59.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 291
  pop_val_log         : 5.6768
```
</details>
<details><summary><b>Paszport Węzła: Strobanda (H3: 891f56cd353ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Strobanda
  stop_id             : 27901
  city                : torun
  h3_index            : 891f56cd353ffff
  stop_lat            : 53.0518
  stop_lon            : 18.6035
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : torun

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : B
  local_percentile    : 79.4816
  local_score_raw     : 0.6299

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 40504.5389
  raw_gravity         : 40504.5389
  domain_count        : 0.0000
  infra_score_log     : 10.6092

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 17.4286
  hourly_freq         : 3.0714
  transit_freq_log    : 2.9139

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 7320.2136
  liquidity           : 341.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 73
  pop_val_log         : 4.3041
```
</details>

#### 💩 BOTTOM 5 (Najsłabsze 5 przystanków)
<details><summary><b>Paszport Węzła: Ostaszewo Toruńskie (H3: 891f56cc68bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Ostaszewo Toruńskie
  stop_id             : 20370
  city                : torun
  h3_index            : 891f56cc68bffff
  stop_lat            : 53.1106
  stop_lon            : 18.6273
  lat_grid            : 53.1100
  lon_grid            : 18.6300
  norm_name           : ostaszewotorunskie
  source              : polish_trains

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 1.0799
  local_score_raw     : -1.2043

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 83.9680
  raw_gravity         : 83.9680
  domain_count        : 0.0000
  infra_score_log     : 4.4423

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.0000
  hourly_freq         : 0.0000
  transit_freq_log    : 0.0000

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6513.0865
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Osiedle Pancernych (H3: 891f56cdbd3ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Osiedle Pancernych
  stop_id             : 52901
  city                : torun
  h3_index            : 891f56cdbd3ffff
  stop_lat            : 53.0435
  stop_lon            : 18.6913
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : torun

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.8639
  local_score_raw     : -1.2355

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 844.9959
  raw_gravity         : 844.9959
  domain_count        : 0.0000
  infra_score_log     : 6.7405

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 1.0000
  hourly_freq         : 1.0000
  transit_freq_log    : 0.6931

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 1671.0432
  liquidity           : 3.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 6
  pop_val_log         : 1.9459
```
</details>
<details><summary><b>Paszport Węzła: Młyniec II - Dolina Drwęcy (H3: 891f5656507ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Młyniec II - Dolina Drwęcy
  stop_id             : 99030
  city                : torun
  h3_index            : 891f5656507ffff
  stop_lat            : 53.0571
  stop_lon            : 18.8043
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : torun

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.6479
  local_score_raw     : -1.3359

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 7.6886
  raw_gravity         : 7.6886
  domain_count        : 0.0000
  infra_score_log     : 2.1620

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.2857
  hourly_freq         : 0.2857
  transit_freq_log    : 0.2513

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6513.0865
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Cierpice - Skrzyżowanie (H3: 891f565314bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Cierpice - Skrzyżowanie
  stop_id             : 99314
  city                : torun
  h3_index            : 891f565314bffff
  stop_lat            : 52.9916
  stop_lon            : 18.4757
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : torun

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.4320
  local_score_raw     : -1.4208

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 0.0000
  raw_gravity         : 0.0000
  domain_count        : 0.0000
  infra_score_log     : 0.0000

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.8571
  hourly_freq         : 0.8571
  transit_freq_log    : 0.6190

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6513.0865
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Cierpice (H3: 891f565338fffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Cierpice
  stop_id             : 19810
  city                : torun
  h3_index            : 891f565338fffff
  stop_lat            : 52.9888
  stop_lon            : 18.4699
  lat_grid            : 52.9900
  lon_grid            : 18.4700
  norm_name           : cierpice
  source              : polish_trains

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.2160
  local_score_raw     : -1.4666

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 338.2988
  raw_gravity         : 338.2988
  domain_count        : 0.0000
  infra_score_log     : 5.8269

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.0000
  hourly_freq         : 0.0000
  transit_freq_log    : 0.0000

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 1180.1731
  liquidity           : 1.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 48
  pop_val_log         : 3.8918
```
</details>

---

## AGLOMERACJA: TROJMIASTO
**Status:** ✅ SUKCES

### Faza 0: Stan Danych
- **Całkowita populacja w strefie miasta:** 1,057,375 (Baseline: 50,000) [✅ OK]
- **Ilość Transakcji RCN:** 150,122
- **Zakres Dat RCN:** 2020-01-02 do 3021-12-02
- **Ceny RCN (PLN/m²):** Średnia=11,841 | Mediana=9,237 | Max=494,118 | IQR=[6,754 - 12,303]
- **Infrastruktura OSM (Punkty):** 206,166
- **Infrastruktura OSM (Poligony/Budynki):** 260,906
- Baza transakcyjna `.gpkg` ustrukturyzowana poprawnie.

### Faza I & II: Pokrycie (Zero-Values)
- **Pustynia Populacyjna:** 555 (11.8%)
- **Pustynia Infrastrukturalna:** 0 (0.0%)
- **Głuche Przystanki:** 56 (1.2%)
- **Wskaźnik Fallback RCN:** 1660 (35.3%) (Mediana RCN dla miasta: 9076)

### Faza III: Udowodnione POI w Promieniu 500m

**Rzeczywiste TOP 20 zwalidowanych obiektów (Intersekcja bufor 500m):**

| Tag OSM | Zliczone (Ilość) | Prawdziwa Waga JSON | Całkowita Siła (Score) |
|---|---|---|---|
| `supermarket` | 5180 | 10,769,653.40 | **55,786,804,612.00** |
| `sports_centre` | 2214 | 1,192,245.77 | **2,639,632,134.78** |
| `marketplace` | 490 | 1,563,066.17 | **765,902,423.30** |
| `place_of_worship` | 4105 | 113,697.14 | **466,726,759.70** |
| `pharmacy` | 6170 | 67,617.13 | **417,197,692.10** |
| `bank` | 4908 | 69,649.28 | **341,838,666.24** |
| `post_office` | 2874 | 72,542.28 | **208,486,512.72** |
| `bench` | 201955 | 0.00 | **0.00** |
| `waste_basket` | 92639 | 0.00 | **0.00** |
| `bicycle_parking` | 43158 | 0.00 | **0.00** |
| `parking_entrance` | 25971 | 0.00 | **0.00** |
| `parcel_locker` | 20165 | 0.00 | **0.00** |
| `restaurant` | 19086 | 0.00 | **0.00** |
| `shelter` | 21086 | 0.00 | **0.00** |
| `vending_machine` | 16383 | 0.00 | **0.00** |
| `recycling` | 14854 | 0.00 | **0.00** |
| `bicycle_rental` | 12732 | 0.00 | **0.00** |
| `fast_food` | 12283 | 0.00 | **0.00** |
| `atm` | 10544 | 0.00 | **0.00** |
| `waste_disposal` | 14689 | 0.00 | **0.00** |

### Faza IV: Badanie Próbek Oceny Złotej

#### 🏆 TOP 5 (Najlepsze 5 przystanków w mieście)
<details><summary><b>Paszport Węzła: Jaśkowa Dolina 05 (H3: 891f7248acfffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Jaśkowa Dolina 05
  stop_id             : 1345
  city                : trojmiasto
  h3_index            : 891f7248acfffff
  stop_lat            : 54.3778
  stop_lon            : 18.6067
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : tricity-gdansk

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 1.8247

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 10845720.7000
  raw_gravity         : 8342862.0769
  domain_count        : 3
  infra_score_log     : 16.1993

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 285.1429
  hourly_freq         : 19.4286
  transit_freq_log    : 5.6565

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 11607.6488
  liquidity           : 70.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 1331
  pop_val_log         : 7.1944
```
</details>
<details><summary><b>Paszport Węzła: Jaśkowa Dolina 02 (H3: 891f7248acfffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Jaśkowa Dolina 02
  stop_id             : 2020
  city                : trojmiasto
  h3_index            : 891f7248acfffff
  stop_lat            : 54.3783
  stop_lon            : 18.6066
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : gtfsgoogle

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 1.8247

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 10845720.7000
  raw_gravity         : 8342862.0769
  domain_count        : 3
  infra_score_log     : 16.1993

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 285.1429
  hourly_freq         : 42.5714
  transit_freq_log    : 5.6565

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 11607.6488
  liquidity           : 70.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 1331
  pop_val_log         : 7.1944
```
</details>
<details><summary><b>Paszport Węzła: Jaśkowa Dolina 04 (H3: 891f7248acfffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Jaśkowa Dolina 04
  stop_id             : 1593
  city                : trojmiasto
  h3_index            : 891f7248acfffff
  stop_lat            : 54.3776
  stop_lon            : 18.6081
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : tricity-gdansk

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 1.8247

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 10845720.7000
  raw_gravity         : 8342862.0769
  domain_count        : 3
  infra_score_log     : 16.1993

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 285.1429
  hourly_freq         : 17.5714
  transit_freq_log    : 5.6565

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 11607.6488
  liquidity           : 70.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 1331
  pop_val_log         : 7.1944
```
</details>
<details><summary><b>Paszport Węzła: Jaśkowa Dolina 03 (H3: 891f7248acfffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Jaśkowa Dolina 03
  stop_id             : 1594
  city                : trojmiasto
  h3_index            : 891f7248acfffff
  stop_lat            : 54.3786
  stop_lon            : 18.6066
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : gtfsgoogle

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 1.8247

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 10845720.7000
  raw_gravity         : 8342862.0769
  domain_count        : 3
  infra_score_log     : 16.1993

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 285.1429
  hourly_freq         : 19.4286
  transit_freq_log    : 5.6565

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 11607.6488
  liquidity           : 70.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 1331
  pop_val_log         : 7.1944
```
</details>
<details><summary><b>Paszport Węzła: Jaśkowa Dolina 03 (H3: 891f7248acfffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Jaśkowa Dolina 03
  stop_id             : 1594
  city                : trojmiasto
  h3_index            : 891f7248acfffff
  stop_lat            : 54.3786
  stop_lon            : 18.6066
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : tricity-gdansk

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 1.8247

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 10845720.7000
  raw_gravity         : 8342862.0769
  domain_count        : 3
  infra_score_log     : 16.1993

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 285.1429
  hourly_freq         : 19.4286
  transit_freq_log    : 5.6565

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 11607.6488
  liquidity           : 70.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 1331
  pop_val_log         : 7.1944
```
</details>

#### 🎲 RANDOM 5 (Środkowe przystanki miasta)
<details><summary><b>Paszport Węzła: Starogardzka 04 (H3: 891f09b33b3ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Starogardzka 04
  stop_id             : 1326
  city                : trojmiasto
  h3_index            : 891f09b33b3ffff
  stop_lat            : 54.3016
  stop_lon            : 18.6069
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : tricity-gdansk

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : C
  local_percentile    : 62.2842
  local_score_raw     : 0.1648

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 530.9770
  raw_gravity         : 530.9770
  domain_count        : 0
  infra_score_log     : 6.2766

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 69.4286
  hourly_freq         : 12.5714
  transit_freq_log    : 4.2546

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 8976.6267
  liquidity           : 141.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 38
  pop_val_log         : 3.6636
```
</details>
<details><summary><b>Paszport Węzła: Sopot Kasztanowa 01 (H3: 891f724850fffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Sopot Kasztanowa 01
  stop_id             : 14479
  city                : trojmiasto
  h3_index            : 891f724850fffff
  stop_lat            : 54.4249
  stop_lon            : 18.5636
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : tricity-gdansk

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : C
  local_percentile    : 64.7410
  local_score_raw     : 0.2279

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 819.1309
  raw_gravity         : 819.1309
  domain_count        : 0
  infra_score_log     : 6.7095

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 27.8571
  hourly_freq         : 6.4286
  transit_freq_log    : 3.3624

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 12049.1387
  liquidity           : 10.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 253
  pop_val_log         : 5.5373
```
</details>
<details><summary><b>Paszport Węzła: Życzliwa 01 (H3: 891f7249ac7ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Życzliwa 01
  stop_id             : 1720
  city                : trojmiasto
  h3_index            : 891f7249ac7ffff
  stop_lat            : 54.3451
  stop_lon            : 18.5363
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : gtfsgoogle

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : C
  local_percentile    : 63.6122
  local_score_raw     : 0.1983

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 63843.3844
  raw_gravity         : 58039.4403
  domain_count        : 1
  infra_score_log     : 11.0642

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 48.2857
  hourly_freq         : 12.1429
  transit_freq_log    : 3.8976

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 7126.9215
  liquidity           : 362.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Pruszcz Gdański Kopernika/Kasprowicza 62 (H3: 891f09b1c13ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Pruszcz Gdański Kopernika/Kasprowicza 62
  stop_id             : 14883
  city                : trojmiasto
  h3_index            : 891f09b1c13ffff
  stop_lat            : 54.2652
  stop_lon            : 18.6673
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : gtfsgoogle

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : B
  local_percentile    : 81.8061
  local_score_raw     : 0.6604

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 784244.9920
  raw_gravity         : 712949.9927
  domain_count        : 1
  infra_score_log     : 13.5725

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 28.2857
  hourly_freq         : 3.4286
  transit_freq_log    : 3.3771

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 6359.1277
  liquidity           : 36.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 416
  pop_val_log         : 6.0331
```
</details>
<details><summary><b>Paszport Węzła: Gdynia Bielińskiego 01 (H3: 891f7259b57ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Gdynia Bielińskiego 01
  stop_id             : 14941
  city                : trojmiasto
  h3_index            : 891f7259b57ffff
  stop_lat            : 54.4574
  stop_lon            : 18.4449
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : tricity-gdansk

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : D
  local_percentile    : 40.8367
  local_score_raw     : -0.2334

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 353.9906
  raw_gravity         : 353.9906
  domain_count        : 0
  infra_score_log     : 5.8721

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 23.0000
  hourly_freq         : 4.0000
  transit_freq_log    : 3.1781

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 9075.5275
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 11
  pop_val_log         : 2.4849
```
</details>

#### 💩 BOTTOM 5 (Najsłabsze 5 przystanków)
<details><summary><b>Paszport Węzła: Kieleńska Huta 19 (H3: 891f0996547ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Kieleńska Huta 19
  stop_id             : 31640
  city                : trojmiasto
  h3_index            : 891f0996547ffff
  stop_lat            : 54.4684
  stop_lon            : 18.2810
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : tricity-gdynia

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.2656
  local_score_raw     : -1.3706

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 38.0192
  raw_gravity         : 38.0192
  domain_count        : 0
  infra_score_log     : 3.6641

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.3571
  hourly_freq         : 0.3571
  transit_freq_log    : 0.3054

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 9075.5275
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Wejherowo Kąpino Skrzyżowanie 01 n/ż (H3: 891f0d242b3ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Wejherowo Kąpino Skrzyżowanie 01 n/ż
  stop_id             : 98
  city                : trojmiasto
  h3_index            : 891f0d242b3ffff
  stop_lat            : 54.6312
  stop_lon            : 18.2705
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : wejherowo

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.1992
  local_score_raw     : -1.4200

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 14.2986
  raw_gravity         : 14.2986
  domain_count        : 0
  infra_score_log     : 2.7278

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.5714
  hourly_freq         : 0.5714
  transit_freq_log    : 0.4520

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 9075.5275
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Wejherowo Kąpino Skrzyżowanie 02 n/ż (H3: 891f0d24287ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Wejherowo Kąpino Skrzyżowanie 02 n/ż
  stop_id             : 97
  city                : trojmiasto
  h3_index            : 891f0d24287ffff
  stop_lat            : 54.6315
  stop_lon            : 18.2698
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : wejherowo

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.1328
  local_score_raw     : -1.4785

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 8.3873
  raw_gravity         : 8.3873
  domain_count        : 0
  infra_score_log     : 2.2394

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.5000
  hourly_freq         : 0.5000
  transit_freq_log    : 0.4055

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 9075.5275
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Bojano Graniczna 04 (H3: 891f0996dd3ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Bojano Graniczna 04
  stop_id             : 31624
  city                : trojmiasto
  h3_index            : 891f0996dd3ffff
  stop_lat            : 54.4639
  stop_lon            : 18.3611
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : tricity-gdynia

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.0664
  local_score_raw     : -1.4960

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 142.4640
  raw_gravity         : 142.4640
  domain_count        : 0
  infra_score_log     : 4.9661

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.0000
  hourly_freq         : 0.0000
  transit_freq_log    : 0.0000

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 5308.3718
  liquidity           : 2.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Bojano Graniczna 03 (H3: 891f0996dd3ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Bojano Graniczna 03
  stop_id             : 31627
  city                : trojmiasto
  h3_index            : 891f0996dd3ffff
  stop_lat            : 54.4640
  stop_lon            : 18.3614
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : tricity-gdynia

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.0664
  local_score_raw     : -1.4960

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 142.4640
  raw_gravity         : 142.4640
  domain_count        : 0
  infra_score_log     : 4.9661

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.0000
  hourly_freq         : 0.0000
  transit_freq_log    : 0.0000

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 5308.3718
  liquidity           : 2.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>

---

## AGLOMERACJA: WARSZAWA
**Status:** ✅ SUKCES

### Faza 0: Stan Danych
- **Całkowita populacja w strefie miasta:** 3,081,843 (Baseline: 1,800,000) [✅ OK]
- **Ilość Transakcji RCN:** 227,085
- **Zakres Dat RCN:** 2020-01-01 do 2923-08-25
- **Ceny RCN (PLN/m²):** Średnia=12,016 | Mediana=10,820 | Max=496,692 | IQR=[7,429 - 14,547]
- **Infrastruktura OSM (Punkty):** 840,606
- **Infrastruktura OSM (Poligony/Budynki):** 1,156,778
- Baza transakcyjna `.gpkg` ustrukturyzowana poprawnie.

### Faza I & II: Pokrycie (Zero-Values)
- **Pustynia Populacyjna:** 877 (8.4%)
- **Pustynia Infrastrukturalna:** 1 (0.0%)
- **Głuche Przystanki:** 6461 (62.2%)
- **Wskaźnik Fallback RCN:** 4929 (47.4%) (Mediana RCN dla miasta: 10327)

### Faza III: Udowodnione POI w Promieniu 500m

**Rzeczywiste TOP 20 zwalidowanych obiektów (Intersekcja bufor 500m):**

| Tag OSM | Zliczone (Ilość) | Prawdziwa Waga JSON | Całkowita Siła (Score) |
|---|---|---|---|
| `supermarket` | 10566 | 11,161,293.74 | **117,930,229,656.84** |
| `exhibition_centre` | 64 | 172,631,243.98 | **11,048,399,614.72** |
| `sports_centre` | 4189 | 1,324,428.92 | **5,548,032,745.88** |
| `marketplace` | 1527 | 1,911,856.74 | **2,919,405,241.98** |
| `pharmacy` | 14033 | 74,385.36 | **1,043,849,756.88** |
| `bank` | 10071 | 77,729.72 | **782,816,010.12** |
| `place_of_worship` | 6561 | 119,017.79 | **780,875,720.19** |
| `post_office` | 5362 | 79,049.60 | **423,863,955.20** |
| `bench` | 351997 | 0.00 | **0.00** |
| `waste_basket` | 164536 | 0.00 | **0.00** |
| `bicycle_parking` | 151193 | 0.00 | **0.00** |
| `vending_machine` | 67101 | 0.00 | **0.00** |
| `parking_entrance` | 48350 | 0.00 | **0.00** |
| `parcel_locker` | 43525 | 0.00 | **0.00** |
| `restaurant` | 42175 | 0.00 | **0.00** |
| `fast_food` | 32299 | 0.00 | **0.00** |
| `atm` | 26061 | 0.00 | **0.00** |
| `cafe` | 20036 | 0.00 | **0.00** |
| `doctors` | 14346 | 0.00 | **0.00** |
| `dentist` | 13093 | 0.00 | **0.00** |

### Faza IV: Badanie Próbek Oceny Złotej

#### 🏆 TOP 5 (Najlepsze 5 przystanków w mieście)
<details><summary><b>Paszport Węzła: PKP Targówek (H3: 891f53c82a7ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : PKP Targówek
  stop_id             : 130101
  city                : warszawa
  h3_index            : 891f53c82a7ffff
  stop_lat            : 52.2626
  stop_lon            : 21.0526
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : warsaw

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 8.2624

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 6478404.2754
  raw_gravity         : 5398670.2295
  domain_count        : 2.0000
  infra_score_log     : 15.6840

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.0000
  hourly_freq         : 0.0000
  transit_freq_log    : 0.0000

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 305714.2857
  liquidity           : 71.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 456
  pop_val_log         : 6.1247
```
</details>
<details><summary><b>Paszport Węzła: Miłobędzka (H3: 891f5226893ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Miłobędzka
  stop_id             : 325502
  city                : warszawa
  h3_index            : 891f5226893ffff
  stop_lat            : 52.1970
  stop_lon            : 20.9921
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : warsaw

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 99.9787
  local_score_raw     : 4.1918

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 1535.5550
  raw_gravity         : 1535.5550
  domain_count        : 0.0000
  infra_score_log     : 7.3373

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.0000
  hourly_freq         : 0.0000
  transit_freq_log    : 0.0000

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 185830.6272
  liquidity           : 4.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 47
  pop_val_log         : 3.8712
```
</details>
<details><summary><b>Paszport Węzła: Miłobędzka (H3: 891f5226893ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Miłobędzka
  stop_id             : 325501
  city                : warszawa
  h3_index            : 891f5226893ffff
  stop_lat            : 52.1965
  stop_lon            : 20.9935
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : warsaw

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 99.9787
  local_score_raw     : 4.1918

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 1535.5550
  raw_gravity         : 1535.5550
  domain_count        : 0.0000
  infra_score_log     : 7.3373

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.0000
  hourly_freq         : 0.0000
  transit_freq_log    : 0.0000

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 185830.6272
  liquidity           : 4.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 47
  pop_val_log         : 3.8712
```
</details>
<details><summary><b>Paszport Węzła: Pl. Zawiszy (H3: 891f53c93c7ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Pl. Zawiszy
  stop_id             : 400103
  city                : warszawa
  h3_index            : 891f53c93c7ffff
  stop_lat            : 52.2250
  stop_lon            : 20.9906
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : warsaw

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 99.9574
  local_score_raw     : 2.4864

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 10561619.7206
  raw_gravity         : 8124322.8620
  domain_count        : 3.0000
  infra_score_log     : 16.1727

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 106.5714
  hourly_freq         : 0.0000
  transit_freq_log    : 4.6782

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 14573.4084
  liquidity           : 39.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 791
  pop_val_log         : 6.6746
```
</details>
<details><summary><b>Paszport Węzła: Pl. Zawiszy (H3: 891f53c93c7ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Pl. Zawiszy
  stop_id             : 400106
  city                : warszawa
  h3_index            : 891f53c93c7ffff
  stop_lat            : 52.2250
  stop_lon            : 20.9898
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : warsaw

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 99.9574
  local_score_raw     : 2.4864

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 10561619.7206
  raw_gravity         : 8124322.8620
  domain_count        : 3.0000
  infra_score_log     : 16.1727

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 106.5714
  hourly_freq         : 0.0000
  transit_freq_log    : 4.6782

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 14573.4084
  liquidity           : 39.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 791
  pop_val_log         : 6.6746
```
</details>

#### 🎲 RANDOM 5 (Środkowe przystanki miasta)
<details><summary><b>Paszport Węzła: Marki Ząbkowska (H3: 891f53cac6fffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Marki Ząbkowska
  stop_id             : 197701
  city                : warszawa
  h3_index            : 891f53cac6fffff
  stop_lat            : 52.3172
  stop_lon            : 21.1157
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : warsaw

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : B
  local_percentile    : 83.9659
  local_score_raw     : 0.5675

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 12999220.7888
  raw_gravity         : 11817473.4443
  domain_count        : 1.0000
  infra_score_log     : 16.3804

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.0000
  hourly_freq         : 0.0000
  transit_freq_log    : 0.0000

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 7302.0574
  liquidity           : 68.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 232
  pop_val_log         : 5.4510
```
</details>
<details><summary><b>Paszport Węzła: Michałowice Wesoła (H3: 891f522445bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Michałowice Wesoła
  stop_id             : 1889979
  city                : warszawa
  h3_index            : 891f522445bffff
  stop_lat            : 52.1653
  stop_lon            : 20.8919
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : warsaw-gpa

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : B
  local_percentile    : 73.8166
  local_score_raw     : 0.3324

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 2521.8026
  raw_gravity         : 2521.8026
  domain_count        : 0.0000
  infra_score_log     : 7.8331

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 4.6429
  hourly_freq         : 2.3571
  transit_freq_log    : 1.7304

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 8116.4617
  liquidity           : 9.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 129
  pop_val_log         : 4.8675
```
</details>
<details><summary><b>Paszport Węzła: Pileckiego (H3: 891f52249d7ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Pileckiego
  stop_id             : 333301
  city                : warszawa
  h3_index            : 891f52249d7ffff
  stop_lat            : 52.1410
  stop_lon            : 21.0401
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : warsaw

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : C
  local_percentile    : 62.0043
  local_score_raw     : 0.0809

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 4901.1439
  raw_gravity         : 4901.1439
  domain_count        : 0.0000
  infra_score_log     : 8.4974

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.0000
  hourly_freq         : 0.0000
  transit_freq_log    : 0.0000

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 13460.9767
  liquidity           : 2.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 1241
  pop_val_log         : 7.1245
```
</details>
<details><summary><b>Paszport Węzła: PKP Legionowo Przystanek (H3: 891f53d840bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : PKP Legionowo Przystanek
  stop_id             : 119701
  city                : warszawa
  h3_index            : 891f53d840bffff
  stop_lat            : 52.4108
  stop_lon            : 20.9154
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : warsaw

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A
  local_percentile    : 85.6716
  local_score_raw     : 0.6217

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 1290.2432
  raw_gravity         : 1290.2432
  domain_count        : 0.0000
  infra_score_log     : 7.1634

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 10.5714
  hourly_freq         : 0.0000
  transit_freq_log    : 2.4485

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 11924.6260
  liquidity           : 1.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 130
  pop_val_log         : 4.8752
```
</details>
<details><summary><b>Paszport Węzła: Aspekt (H3: 891f53cb2c3ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Aspekt
  stop_id             : 602403
  city                : warszawa
  h3_index            : 891f53cb2c3ffff
  stop_lat            : 52.2784
  stop_lon            : 20.9332
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : warsaw

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : D
  local_percentile    : 48.2942
  local_score_raw     : -0.1448

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 784.0493
  raw_gravity         : 784.0493
  domain_count        : 0.0000
  infra_score_log     : 6.6657

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.0000
  hourly_freq         : 0.0000
  transit_freq_log    : 0.0000

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 12272.6277
  liquidity           : 1.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 976
  pop_val_log         : 6.8845
```
</details>

#### 💩 BOTTOM 5 (Najsłabsze 5 przystanków)
<details><summary><b>Paszport Węzła: Łomna-Las Wiśniowa (H3: 891f52acbb3ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Łomna-Las Wiśniowa
  stop_id             : 666201
  city                : warszawa
  h3_index            : 891f52acbb3ffff
  stop_lat            : 52.3707
  stop_lon            : 20.7940
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : warsaw

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.0853
  local_score_raw     : -1.0458

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 18.4949
  raw_gravity         : 18.4949
  domain_count        : 0.0000
  infra_score_log     : 2.9702

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.0000
  hourly_freq         : 0.0000
  transit_freq_log    : 0.0000

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 10326.6596
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Modlin Airport (H3: 891f52ae0cbffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Modlin Airport
  stop_id             : STRATEGIC
  city                : warszawa
  h3_index            : 891f52ae0cbffff
  stop_lat            : nan
  stop_lon            : nan
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : STRATEGIC_HUB

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.0640
  local_score_raw     : -1.0501

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 17.6617
  raw_gravity         : 17.6617
  domain_count        : 0.0000
  infra_score_log     : 2.9265

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.0000
  hourly_freq         : 0.0000
  transit_freq_log    : 0.0000

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 10326.6596
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Rajszew Nadzorcówka (H3: 891f53db377ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Rajszew Nadzorcówka
  stop_id             : 179002
  city                : warszawa
  h3_index            : 891f53db377ffff
  stop_lat            : 52.3926
  stop_lon            : 20.8690
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : warsaw

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.0426
  local_score_raw     : -1.0866

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 11.8157
  raw_gravity         : 11.8157
  domain_count        : 0.0000
  infra_score_log     : 2.5507

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.0000
  hourly_freq         : 0.0000
  transit_freq_log    : 0.0000

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 10326.6596
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Góra Pałacowa (H3: 891f52aed07ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Góra Pałacowa
  stop_id             : 187601
  city                : warszawa
  h3_index            : 891f52aed07ffff
  stop_lat            : 52.4488
  stop_lon            : 20.7758
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : warsaw

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.0213
  local_score_raw     : -1.2298

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 43.6697
  raw_gravity         : 43.6697
  domain_count        : 0.0000
  infra_score_log     : 3.7993

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.0000
  hourly_freq         : 0.0000
  transit_freq_log    : 0.0000

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 96.5696
  liquidity           : 1.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Góra Pałacowa (H3: 891f52aed07ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Góra Pałacowa
  stop_id             : 187602
  city                : warszawa
  h3_index            : 891f52aed07ffff
  stop_lat            : 52.4485
  stop_lon            : 20.7762
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : warsaw

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.0213
  local_score_raw     : -1.2298

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 43.6697
  raw_gravity         : 43.6697
  domain_count        : 0.0000
  infra_score_log     : 3.7993

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.0000
  hourly_freq         : 0.0000
  transit_freq_log    : 0.0000

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 96.5696
  liquidity           : 1.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>

---

## AGLOMERACJA: WROCLAW
**Status:** ✅ SUKCES

### Faza 0: Stan Danych
- **Całkowita populacja w strefie miasta:** 938,629 (Baseline: 640,000) [✅ OK]
- **Ilość Transakcji RCN:** 58,508
- **Zakres Dat RCN:** 2020-01-02 do 2026-02-27
- **Ceny RCN (PLN/m²):** Średnia=8,266 | Mediana=7,533 | Max=481,876 | IQR=[5,080 - 10,441]
- **Infrastruktura OSM (Punkty):** 251,132
- **Infrastruktura OSM (Poligony/Budynki):** 379,765
- Baza transakcyjna `.gpkg` ustrukturyzowana poprawnie.

### Faza I & II: Pokrycie (Zero-Values)
- **Pustynia Populacyjna:** 486 (14.7%)
- **Pustynia Infrastrukturalna:** 4 (0.1%)
- **Głuche Przystanki:** 44 (1.3%)
- **Wskaźnik Fallback RCN:** 1407 (42.5%) (Mediana RCN dla miasta: 7238)

### Faza III: Udowodnione POI w Promieniu 500m

**Rzeczywiste TOP 20 zwalidowanych obiektów (Intersekcja bufor 500m):**

| Tag OSM | Zliczone (Ilość) | Prawdziwa Waga JSON | Całkowita Siła (Score) |
|---|---|---|---|
| `supermarket` | 3172 | 10,380,262.14 | **32,926,191,508.08** |
| `sports_centre` | 1198 | 1,146,089.73 | **1,373,015,496.54** |
| `marketplace` | 236 | 1,594,400.03 | **376,278,407.08** |
| `pharmacy` | 4296 | 67,991.31 | **292,090,667.76** |
| `place_of_worship` | 2343 | 112,505.16 | **263,599,589.88** |
| `bank` | 3061 | 70,077.05 | **214,505,850.05** |
| `post_office` | 1653 | 70,290.16 | **116,189,634.48** |
| `bench` | 130137 | 0.00 | **0.00** |
| `bicycle_parking` | 39981 | 0.00 | **0.00** |
| `waste_basket` | 31187 | 0.00 | **0.00** |
| `fast_food` | 15691 | 0.00 | **0.00** |
| `parking_entrance` | 14507 | 0.00 | **0.00** |
| `parcel_locker` | 11788 | 0.00 | **0.00** |
| `restaurant` | 9544 | 0.00 | **0.00** |
| `vending_machine` | 8317 | 0.00 | **0.00** |
| `recycling` | 8194 | 0.00 | **0.00** |
| `atm` | 7106 | 0.00 | **0.00** |
| `cafe` | 6804 | 0.00 | **0.00** |
| `waste_disposal` | 13216 | 0.00 | **0.00** |
| `doctors` | 4758 | 0.00 | **0.00** |

### Faza IV: Badanie Próbek Oceny Złotej

#### 🏆 TOP 5 (Najlepsze 5 przystanków w mieście)
<details><summary><b>Paszport Węzła: Renoma (H3: 891e2040817ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Renoma
  stop_id             : 1565
  city                : wroclaw
  h3_index            : 891e2040817ffff
  stop_lat            : 51.1043
  stop_lon            : 17.0300
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : wroclaw

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 2.1250

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 10779954.0999
  raw_gravity         : 8292272.3846
  domain_count        : 3.0000
  infra_score_log     : 16.1932

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 56.5000
  hourly_freq         : 13.7857
  transit_freq_log    : 4.0518

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 18439.1706
  liquidity           : 70.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 519
  pop_val_log         : 6.2538
```
</details>
<details><summary><b>Paszport Węzła: Renoma (H3: 891e2040817ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Renoma
  stop_id             : 848
  city                : wroclaw
  h3_index            : 891e2040817ffff
  stop_lat            : 51.1038
  stop_lon            : 17.0307
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : wroclaw

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 2.1250

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 10779954.0999
  raw_gravity         : 8292272.3846
  domain_count        : 3.0000
  infra_score_log     : 16.1932

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 56.5000
  hourly_freq         : 0.0000
  transit_freq_log    : 4.0518

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 18439.1706
  liquidity           : 70.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 519
  pop_val_log         : 6.2538
```
</details>
<details><summary><b>Paszport Węzła: Renoma (H3: 891e2040817ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Renoma
  stop_id             : 1564
  city                : wroclaw
  h3_index            : 891e2040817ffff
  stop_lat            : 51.1037
  stop_lon            : 17.0306
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : wroclaw

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 2.1250

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 10779954.0999
  raw_gravity         : 8292272.3846
  domain_count        : 3.0000
  infra_score_log     : 16.1932

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 56.5000
  hourly_freq         : 18.3571
  transit_freq_log    : 4.0518

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 18439.1706
  liquidity           : 70.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 519
  pop_val_log         : 6.2538
```
</details>
<details><summary><b>Paszport Węzła: Renoma (H3: 891e2040817ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Renoma
  stop_id             : 849
  city                : wroclaw
  h3_index            : 891e2040817ffff
  stop_lat            : 51.1043
  stop_lon            : 17.0301
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : wroclaw

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 2.1250

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 10779954.0999
  raw_gravity         : 8292272.3846
  domain_count        : 3.0000
  infra_score_log     : 16.1932

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 56.5000
  hourly_freq         : 10.2857
  transit_freq_log    : 4.0518

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 18439.1706
  liquidity           : 70.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 519
  pop_val_log         : 6.2538
```
</details>
<details><summary><b>Paszport Węzła: Renoma (H3: 891e2040817ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Renoma
  stop_id             : 522
  city                : wroclaw
  h3_index            : 891e2040817ffff
  stop_lat            : 51.1041
  stop_lon            : 17.0323
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : wroclaw

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 2.1250

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 10779954.0999
  raw_gravity         : 8292272.3846
  domain_count        : 3.0000
  infra_score_log     : 16.1932

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 56.5000
  hourly_freq         : 14.0714
  transit_freq_log    : 4.0518

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 18439.1706
  liquidity           : 70.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 519
  pop_val_log         : 6.2538
```
</details>

#### 🎲 RANDOM 5 (Środkowe przystanki miasta)
<details><summary><b>Paszport Węzła: Hala Targowa (H3: 891e2040d43ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Hala Targowa
  stop_id             : 2583
  city                : wroclaw
  h3_index            : 891e2040d43ffff
  stop_lat            : 51.1135
  stop_lon            : 17.0388
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : wroclaw

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : B
  local_percentile    : 83.6934
  local_score_raw     : 0.7886

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 315002.9502
  raw_gravity         : 315002.9502
  domain_count        : 0.0000
  infra_score_log     : 12.6603

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 9.2143
  hourly_freq         : 4.6429
  transit_freq_log    : 2.3238

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 11863.5438
  liquidity           : 3.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 178
  pop_val_log         : 5.1874
```
</details>
<details><summary><b>Paszport Węzła: Nyska (H3: 891e2040b07ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Nyska
  stop_id             : 1530
  city                : wroclaw
  h3_index            : 891e2040b07ffff
  stop_lat            : 51.0831
  stop_lon            : 17.0544
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : wroclaw

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : B
  local_percentile    : 77.9094
  local_score_raw     : 0.6070

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 1836.2626
  raw_gravity         : 1836.2626
  domain_count        : 0.0000
  infra_score_log     : 7.5160

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 35.5000
  hourly_freq         : 9.1429
  transit_freq_log    : 3.5973

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 8549.8743
  liquidity           : 39.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 1131
  pop_val_log         : 7.0317
```
</details>
<details><summary><b>Paszport Węzła: Graniczna (Strachowicka) (H3: 891e2040657ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Graniczna (Strachowicka)
  stop_id             : 2777
  city                : wroclaw
  h3_index            : 891e2040657ffff
  stop_lat            : 51.1110
  stop_lon            : 16.8982
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : wroclaw

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : D
  local_percentile    : 45.2962
  local_score_raw     : -0.2179

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 810.6470
  raw_gravity         : 810.6470
  domain_count        : 0.0000
  infra_score_log     : 6.6991

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 8.2143
  hourly_freq         : 4.0714
  transit_freq_log    : 2.2208

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 7238.1258
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 27
  pop_val_log         : 3.3322
```
</details>
<details><summary><b>Paszport Węzła: Iwiny - Pogodna (H3: 891e204e147ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Iwiny - Pogodna
  stop_id             : 15
  city                : wroclaw
  h3_index            : 891e204e147ffff
  stop_lat            : 51.0431
  stop_lon            : 17.0779
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : wroclaw-siechnice

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : C
  local_percentile    : 50.4530
  local_score_raw     : -0.1192

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 603.4854
  raw_gravity         : 603.4854
  domain_count        : 0.0000
  infra_score_log     : 6.4044

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 7.2857
  hourly_freq         : 7.2857
  transit_freq_log    : 2.1145

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 10132.5744
  liquidity           : 56.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 23
  pop_val_log         : 3.1781
```
</details>
<details><summary><b>Paszport Węzła: Zacisze (H3: 891e204728bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Zacisze
  stop_id             : 610
  city                : wroclaw
  h3_index            : 891e204728bffff
  stop_lat            : 51.1242
  stop_lon            : 17.0782
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : wroclaw

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : B
  local_percentile    : 77.3519
  local_score_raw     : 0.5802

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 1792.4687
  raw_gravity         : 1792.4687
  domain_count        : 0.0000
  infra_score_log     : 7.4919

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 49.6429
  hourly_freq         : 24.7857
  transit_freq_log    : 3.9248

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 8375.4741
  liquidity           : 1.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 192
  pop_val_log         : 5.2627
```
</details>

#### 💩 BOTTOM 5 (Najsłabsze 5 przystanków)
<details><summary><b>Paszport Węzła: Lutynia - Kolonia (H3: 891e205aaabffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Lutynia - Kolonia
  stop_id             : 3864
  city                : wroclaw
  h3_index            : 891e205aaabffff
  stop_lat            : 51.1318
  stop_lon            : 16.7560
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : wroclaw

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.2787
  local_score_raw     : -1.4725

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 4.3728
  raw_gravity         : 4.3728
  domain_count        : 0.0000
  infra_score_log     : 1.6814

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.5714
  hourly_freq         : 0.2857
  transit_freq_log    : 0.4520

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 7238.1258
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Lutynia - Kolonia (H3: 891e205aaabffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Lutynia - Kolonia
  stop_id             : 3865
  city                : wroclaw
  h3_index            : 891e205aaabffff
  stop_lat            : 51.1317
  stop_lon            : 16.7563
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : wroclaw

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.2787
  local_score_raw     : -1.4725

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 4.3728
  raw_gravity         : 4.3728
  domain_count        : 0.0000
  infra_score_log     : 1.6814

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.5714
  hourly_freq         : 0.2857
  transit_freq_log    : 0.4520

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 7238.1258
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Zimnica NŻ (H3: 891e20722cfffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Zimnica NŻ
  stop_id             : 135
  city                : wroclaw
  h3_index            : 891e20722cfffff
  stop_lat            : 51.1647
  stop_lon            : 17.3886
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : wroclaw-polbus

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.2091
  local_score_raw     : -1.4795

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 5.7696
  raw_gravity         : 5.7696
  domain_count        : 0.0000
  infra_score_log     : 1.9124

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.4286
  hourly_freq         : 0.4286
  transit_freq_log    : 0.3567

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 7238.1258
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Niedary skrz. (H3: 891e2019ba7ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Niedary skrz.
  stop_id             : 252
  city                : wroclaw
  h3_index            : 891e2019ba7ffff
  stop_lat            : 51.3075
  stop_lon            : 17.2346
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : wroclaw-polbus

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.1394
  local_score_raw     : -1.4853

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 18.8140
  raw_gravity         : 18.8140
  domain_count        : 0.0000
  infra_score_log     : 2.9864

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.0000
  hourly_freq         : 0.0000
  transit_freq_log    : 0.0000

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 7238.1258
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Kopiec (H3: 891e200b54bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Kopiec
  stop_id             : 255
  city                : wroclaw
  h3_index            : 891e200b54bffff
  stop_lat            : 51.2766
  stop_lon            : 17.2249
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : wroclaw-polbus

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.0697
  local_score_raw     : -1.4937

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 102.9820
  raw_gravity         : 102.9820
  domain_count        : 0.0000
  infra_score_log     : 4.6442

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.0000
  hourly_freq         : 0.0000
  transit_freq_log    : 0.0000

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 229.5333
  liquidity           : 1.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 40
  pop_val_log         : 3.7136
```
</details>

---

## AGLOMERACJA: ZIELONA-GORA
**Status:** ✅ SUKCES

### Faza 0: Stan Danych
- **Całkowita populacja w strefie miasta:** 141,680 (Baseline: 50,000) [✅ OK]
- **Ilość Transakcji RCN:** 5,063
- **Zakres Dat RCN:** 2021-09-06 do 2026-02-19
- **Ceny RCN (PLN/m²):** Średnia=6,359 | Mediana=5,758 | Max=135,556 | IQR=[3,665 - 7,533]
- **Infrastruktura OSM (Punkty):** 31,185
- **Infrastruktura OSM (Poligony/Budynki):** 41,680
- Baza transakcyjna `.gpkg` ustrukturyzowana poprawnie.

### Faza I & II: Pokrycie (Zero-Values)
- **Pustynia Populacyjna:** 69 (14.5%)
- **Pustynia Infrastrukturalna:** 0 (0.0%)
- **Głuche Przystanki:** 14 (2.9%)
- **Wskaźnik Fallback RCN:** 290 (60.8%) (Mediana RCN dla miasta: 5644)

### Faza III: Udowodnione POI w Promieniu 500m

**Rzeczywiste TOP 20 zwalidowanych obiektów (Intersekcja bufor 500m):**

| Tag OSM | Zliczone (Ilość) | Prawdziwa Waga JSON | Całkowita Siła (Score) |
|---|---|---|---|
| `supermarket` | 543 | 10,081,031.46 | **5,474,000,082.78** |
| `sports_centre` | 211 | 905,806.73 | **191,125,220.03** |
| `pharmacy` | 531 | 58,516.30 | **31,072,155.30** |
| `bank` | 457 | 65,875.58 | **30,105,140.06** |
| `place_of_worship` | 283 | 97,624.33 | **27,627,685.39** |
| `post_office` | 180 | 77,536.02 | **13,956,483.60** |
| `bench` | 22807 | 0.00 | **0.00** |
| `waste_basket` | 8148 | 0.00 | **0.00** |
| `recycling` | 2069 | 0.00 | **0.00** |
| `vending_machine` | 1318 | 0.00 | **0.00** |
| `restaurant` | 1355 | 0.00 | **0.00** |
| `parcel_locker` | 1109 | 0.00 | **0.00** |
| `bicycle_parking` | 999 | 0.00 | **0.00** |
| `grit_bin` | 820 | 0.00 | **0.00** |
| `lounger` | 740 | 0.00 | **0.00** |
| `drinking_water` | 640 | 0.00 | **0.00** |
| `waste_disposal` | 2387 | 0.00 | **0.00** |
| `atm` | 399 | 0.00 | **0.00** |
| `fast_food` | 580 | 0.00 | **0.00** |
| `cafe` | 431 | 0.00 | **0.00** |

### Faza IV: Badanie Próbek Oceny Złotej

#### 🏆 TOP 5 (Najlepsze 5 przystanków w mieście)
<details><summary><b>Paszport Węzła: DWORZEC GŁÓWNY (H3: 891f192f1a7ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : DWORZEC GŁÓWNY
  stop_id             : 460
  city                : zielona-gora
  h3_index            : 891f192f1a7ffff
  stop_lat            : 51.9473
  stop_lon            : 15.5168
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : dla_deweloperow_yyvw6

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 2.0978

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 32448.6605
  raw_gravity         : 29498.7822
  domain_count        : 1
  infra_score_log     : 10.3874

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 57.5000
  hourly_freq         : 1.2857
  transit_freq_log    : 4.0690

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 10985.3766
  liquidity           : 4.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 607
  pop_val_log         : 6.4102
```
</details>
<details><summary><b>Paszport Węzła: Staszica (H3: 891f192f1a7ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Staszica
  stop_id             : 12
  city                : zielona-gora
  h3_index            : 891f192f1a7ffff
  stop_lat            : 51.9462
  stop_lon            : 15.5197
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : dla_deweloperow_yyvw6

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 2.0978

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 32448.6605
  raw_gravity         : 29498.7822
  domain_count        : 1
  infra_score_log     : 10.3874

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 57.5000
  hourly_freq         : 11.7857
  transit_freq_log    : 4.0690

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 10985.3766
  liquidity           : 4.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 607
  pop_val_log         : 6.4102
```
</details>
<details><summary><b>Paszport Węzła: Dworzec Główny (H3: 891f192f1a7ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Dworzec Główny
  stop_id             : 11
  city                : zielona-gora
  h3_index            : 891f192f1a7ffff
  stop_lat            : 51.9472
  stop_lon            : 15.5166
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : dla_deweloperow_yyvw6

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 2.0978

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 32448.6605
  raw_gravity         : 29498.7822
  domain_count        : 1
  infra_score_log     : 10.3874

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 57.5000
  hourly_freq         : 20.6429
  transit_freq_log    : 4.0690

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 10985.3766
  liquidity           : 4.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 607
  pop_val_log         : 6.4102
```
</details>
<details><summary><b>Paszport Węzła: DWORZEC GŁÓWNY (H3: 891f192f1a7ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : DWORZEC GŁÓWNY
  stop_id             : 111
  city                : zielona-gora
  h3_index            : 891f192f1a7ffff
  stop_lat            : 51.9472
  stop_lon            : 15.5167
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : dla_deweloperow_yyvw6

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 2.0978

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 32448.6605
  raw_gravity         : 29498.7822
  domain_count        : 1
  infra_score_log     : 10.3874

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 57.5000
  hourly_freq         : 5.9286
  transit_freq_log    : 4.0690

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 10985.3766
  liquidity           : 4.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 607
  pop_val_log         : 6.4102
```
</details>
<details><summary><b>Paszport Węzła: Dworzec Główny (H3: 891f192f1a7ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Dworzec Główny
  stop_id             : 28
  city                : zielona-gora
  h3_index            : 891f192f1a7ffff
  stop_lat            : 51.9470
  stop_lon            : 15.5163
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : dla_deweloperow_yyvw6

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : A+
  local_percentile    : 100.0000
  local_score_raw     : 2.0978

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 32448.6605
  raw_gravity         : 29498.7822
  domain_count        : 1
  infra_score_log     : 10.3874

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 57.5000
  hourly_freq         : 17.8571
  transit_freq_log    : 4.0690

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 10985.3766
  liquidity           : 4.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 607
  pop_val_log         : 6.4102
```
</details>

#### 🎲 RANDOM 5 (Środkowe przystanki miasta)
<details><summary><b>Paszport Węzła: Dąbrówki (H3: 891f192f157ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Dąbrówki
  stop_id             : 7
  city                : zielona-gora
  h3_index            : 891f192f157ffff
  stop_lat            : 51.9380
  stop_lon            : 15.4942
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : dla_deweloperow_yyvw6

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : B
  local_percentile    : 81.2261
  local_score_raw     : 0.7114

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 10346275.4521
  raw_gravity         : 8621896.2101
  domain_count        : 2
  infra_score_log     : 16.1521

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 6.3571
  hourly_freq         : 3.1429
  transit_freq_log    : 1.9957

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 796.8127
  liquidity           : 3.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 671
  pop_val_log         : 6.5103
```
</details>
<details><summary><b>Paszport Węzła: Zatonie Parkowa (H3: 891f192da8fffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Zatonie Parkowa
  stop_id             : 355
  city                : zielona-gora
  h3_index            : 891f192da8fffff
  stop_lat            : 51.8602
  stop_lon            : 15.5614
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : dla_deweloperow_yyvw6

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : D
  local_percentile    : 29.8851
  local_score_raw     : -0.5134

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 477.0958
  raw_gravity         : 477.0958
  domain_count        : 0
  infra_score_log     : 6.1698

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 1.0000
  hourly_freq         : 0.5000
  transit_freq_log    : 0.6931

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 5644.4026
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 40
  pop_val_log         : 3.7136
```
</details>
<details><summary><b>Paszport Węzła: Krępa Dolna (H3: 891f192e5d3ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Krępa Dolna
  stop_id             : 911
  city                : zielona-gora
  h3_index            : 891f192e5d3ffff
  stop_lat            : 51.9991
  stop_lon            : 15.5368
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : dla_deweloperow_yyvw6

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : C
  local_percentile    : 56.3218
  local_score_raw     : -0.0057

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 63630.8085
  raw_gravity         : 63630.8085
  domain_count        : 0
  infra_score_log     : 11.0609

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 1.0000
  hourly_freq         : 0.5000
  transit_freq_log    : 0.6931

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 5644.4026
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 88
  pop_val_log         : 4.4886
```
</details>
<details><summary><b>Paszport Węzła: Anny Jagiellonki (H3: 891f192f53bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Anny Jagiellonki
  stop_id             : 881
  city                : zielona-gora
  h3_index            : 891f192f53bffff
  stop_lat            : 51.9542
  stop_lon            : 15.4933
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : dla_deweloperow_yyvw6

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : D
  local_percentile    : 42.1456
  local_score_raw     : -0.2880

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 636.5020
  raw_gravity         : 636.5020
  domain_count        : 0
  infra_score_log     : 6.4576

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 1.0714
  hourly_freq         : 1.0714
  transit_freq_log    : 0.7282

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 5644.4026
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 609
  pop_val_log         : 6.4135
```
</details>
<details><summary><b>Paszport Węzła: WROCŁAWSKA (H3: 891f192c0cbffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : WROCŁAWSKA
  stop_id             : 450
  city                : zielona-gora
  h3_index            : 891f192c0cbffff
  stop_lat            : 51.9260
  stop_lon            : 15.5402
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : dla_deweloperow_yyvw6

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : D
  local_percentile    : 39.4636
  local_score_raw     : -0.3312

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 228.3862
  raw_gravity         : 228.3862
  domain_count        : 0
  infra_score_log     : 5.4354

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 5.1429
  hourly_freq         : 1.9286
  transit_freq_log    : 1.8153

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 5644.4026
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>

#### 💩 BOTTOM 5 (Najsłabsze 5 przystanków)
<details><summary><b>Paszport Węzła: Ochla Kożuchowska (H3: 891f192d2a7ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Ochla Kożuchowska
  stop_id             : 230
  city                : zielona-gora
  h3_index            : 891f192d2a7ffff
  stop_lat            : 51.8742
  stop_lon            : 15.4838
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : dla_deweloperow_yyvw6

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 1.9157
  local_score_raw     : -1.1374

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 72.2472
  raw_gravity         : 72.2472
  domain_count        : 0
  infra_score_log     : 4.2938

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.2857
  hourly_freq         : 0.2857
  transit_freq_log    : 0.2513

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 5644.4026
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Ochla działki (H3: 891f192d3dbffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Ochla działki
  stop_id             : 229
  city                : zielona-gora
  h3_index            : 891f192d3dbffff
  stop_lat            : 51.8726
  stop_lon            : 15.4901
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : dla_deweloperow_yyvw6

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 1.5326
  local_score_raw     : -1.1545

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 59.9408
  raw_gravity         : 59.9408
  domain_count        : 0
  infra_score_log     : 4.1099

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.2857
  hourly_freq         : 0.2857
  transit_freq_log    : 0.2513

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 5644.4026
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: NAFTOWA (H3: 891f192f5cbffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : NAFTOWA
  stop_id             : 103
  city                : zielona-gora
  h3_index            : 891f192f5cbffff
  stop_lat            : 51.9572
  stop_lon            : 15.4701
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : dla_deweloperow_yyvw6

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 1.1494
  local_score_raw     : -1.1703

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 171.2872
  raw_gravity         : 171.2872
  domain_count        : 0
  infra_score_log     : 5.1492

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.0000
  hourly_freq         : 0.0000
  transit_freq_log    : 0.0000

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 5644.4026
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Ochla działki  (H3: 891f192d3c3ffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Ochla działki 
  stop_id             : 874
  city                : zielona-gora
  h3_index            : 891f192d3c3ffff
  stop_lat            : 51.8721
  stop_lon            : 15.4917
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : dla_deweloperow_yyvw6

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.7663
  local_score_raw     : -1.1938

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 38.9466
  raw_gravity         : 38.9466
  domain_count        : 0
  infra_score_log     : 3.6875

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.2857
  hourly_freq         : 0.2857
  transit_freq_log    : 0.2513

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 5644.4026
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>
<details><summary><b>Paszport Węzła: Kiełpin Os. Sawanna (H3: 891f192d31bffff)</b></summary>

```text

--- IDENTYFIKACJA I LOKALIZACJA ---
  stop_name           : Kiełpin Os. Sawanna
  stop_id             : 1001
  city                : zielona-gora
  h3_index            : 891f192d31bffff
  stop_lat            : 51.8694
  stop_lon            : 15.5008
  lat_grid            : nan
  lon_grid            : nan
  norm_name           : nan
  source              : dla_deweloperow_yyvw6

--- OCENA KOŃCOWA DNA (Z-SCORE) ---
  grade               : F
  local_percentile    : 0.3831
  local_score_raw     : -1.2041

--- FILAR 1: INFRASTRUKTURA (POI) ---
  infra_score         : 34.7468
  raw_gravity         : 34.7468
  domain_count        : 0
  infra_score_log     : 3.5765

--- FILAR 2: TRANSPORT (GTFS) ---
  transit_freq        : 0.2857
  hourly_freq         : 0.2857
  transit_freq_log    : 0.2513

--- FILAR 3: NIERUCHOMOŚCI (RCN) ---
  market_val          : 5644.4026
  liquidity           : 0.0000

--- FILAR 4: DEMOGRAFIA (NSP2021) ---
  pop_val             : 0
  pop_val_log         : 0.0000
```
</details>

---
