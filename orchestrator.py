import argparse
import os
import sys
import json
import logging
from pathlib import Path
import subprocess
import concurrent.futures
from datetime import datetime

def setup_logger(data_dir):
    log_dir = Path(data_dir) / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)
    
    logger = logging.getLogger("TurboOrchestrator")
    logger.setLevel(logging.DEBUG)
    
    # Konsola - tylko INFO i wyżej, czysty format
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s | %(message)s', datefmt='%H:%M:%S')
    ch.setFormatter(formatter)
    
    # Plik - pełny debug
    fh = logging.FileHandler(log_dir / "pipeline_run.log")
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    
    logger.addHandler(ch)
    logger.addHandler(fh)
    return logger

class TurboOrchestrator:
    def __init__(self, data_dir, cities, force_update, max_workers):
        self.data_dir = Path(data_dir).resolve()
        self.force_update = force_update
        self.max_workers = max_workers
        self.state_file = self.data_dir / ".pipeline_state.json"
        self.state = self._load_state()
        self.logger = setup_logger(self.data_dir)
        
        # Inicjalizacja listy miast
        cities_root = self.data_dir / "cities"
        if cities == ['all']:
            if cities_root.exists():
                self.target_cities = sorted([d.name for d in cities_root.iterdir() if d.is_dir()])
            else:
                self.target_cities = []
        else:
            self.target_cities = cities

        # Zmienne środowiskowe dla skryptów potomnych
        os.environ["PIPELINE_DATA_DIR"] = str(self.data_dir)

    def _load_state(self):
        if not self.force_update and self.state_file.exists():
            try:
                with open(self.state_file, 'r') as f:
                    return json.load(f)
            except: return {}
        return {}

    def _save_state(self):
        with open(self.state_file, 'w') as f:
            json.dump(self.state, f, indent=4)

    def stream_process(self, cmd, label):
        """Uruchamia proces i strumieniuje KAŻDĄ linię outputu do konsoli."""
        process = subprocess.Popen(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            env=os.environ.copy(),
            bufsize=1,
            universal_newlines=True
        )
        
        output_lines = []
        for line in iter(process.stdout.readline, ""):
            line = line.strip()
            if line:
                self.logger.info(f"[{label}] {line}")
                output_lines.append(line)
        
        process.stdout.close()
        return process.wait(), output_lines

    def run_global_step(self, step_id, script_path):
        """Kroki globalne (00-04, 06, 11) - uruchamiane raz."""
        self.logger.info(f"\n>>> KROK GLOBALNY: {step_id} ({Path(script_path).name})")
        
        if not self.force_update and self.state.get(step_id) == "SUCCESS":
            self.logger.info(f"--- POMINIĘTO (już wykonane) ---")
            return True

        cmd = [sys.executable, str(script_path)]
        if self.force_update:
            # Przekazujemy flagę force do skryptu, jeśli ją obsługuje
            cmd.append("--force")

        rc, _ = self.stream_process(cmd, step_id)
        
        if rc == 0:
            self.state[step_id] = "SUCCESS"
            self._save_state()
            return True
        return False

    def run_city_parallel_step(self, step_id, script_path):
        """Kroki per-miasto (05, 07, 08, 09, 10, 12, 13, 14) - równolegle."""
        self.logger.info(f"\n>>> KROK RÓWNOLEGŁY ({self.max_workers} workers): {step_id} ({Path(script_path).name})")
        
        cities_to_do = []
        for city in self.target_cities:
            city_step_key = f"{step_id}_{city}"
            if self.force_update or self.state.get(city_step_key) != "SUCCESS":
                cities_to_do.append(city)

        if not cities_to_do:
            self.logger.info(f"--- WSZYSTKIE MIASTA GOTOWE ---")
            return True

        self.logger.info(f"Przetwarzanie {len(cities_to_do)} miast...")
        
        results = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = {}
            for city in cities_to_do:
                cmd = [sys.executable, str(script_path), "--city", city]
                if self.force_update:
                    cmd.append("--force")
                futures[executor.submit(self.stream_process, cmd, f"{city}")] = city
            
            done_count = 0
            for future in concurrent.futures.as_completed(futures):
                city = futures[future]
                rc, _ = future.result()
                done_count += 1
                if rc == 0:
                    self.state[f"{step_id}_{city}"] = "SUCCESS"
                    self.logger.info(f"[{done_count}/{len(cities_to_do)}] SUCCESS: {city}")
                else:
                    self.logger.error(f"[{done_count}/{len(cities_to_do)}] FAILED: {city}")
                    results.append(city)
                self._save_state()

        if results:
            self.logger.error(f"Krok {step_id} nie powiódł się dla miast: {', '.join(results)}")
            return False
        return True

def main():
    parser = argparse.ArgumentParser(description="TURBO Orchestrator 2.0 - Kielce Analiza")
    parser.add_argument("--data-dir", default="data", help="Katalog roboczy")
    parser.add_argument("--cities", nargs="+", default=["all"], help="Miasta lub 'all'")
    parser.add_argument("--force-update", action="store_true", help="Ignoruj stan")
    parser.add_argument("--workers", type=int, default=4, help="Ilość równoległych workerów")
    parser.add_argument("--step", type=int, help="Uruchom konkretny krok")
    
    args = parser.parse_args()
    
    orch = TurboOrchestrator(args.data_dir, args.cities, args.force_update, args.workers)
    
    # Klasyfikacja kroków: True = globalny, False = per-miasto
    pipeline = [
        (0, "scripts/pipeline/00_init_environment.py", True),
        (1, "scripts/pipeline/01_fetch_gtfs.py", True), # GTFS fetcher sam jest wielowątkowy
        (2, "scripts/pipeline/02_collect_stops.py", True), # Przetwarza wszystkie na raz
        (3, "scripts/pipeline/03_download_osm_pbf.py", True),
        (4, "scripts/pipeline/04_download_population.py", True),
        (5, "scripts/pipeline/05_extract_infrastructure.py", False), # CIĘŻKIE - OSM Scalpel
        (6, "scripts/pipeline/06_identify_rcn_teryt.py", True),
        (7, "scripts/pipeline/07_harvest_rcn_omnibus.py", True), # GLOBALNY CACHE I DYSTRYBUCJA
        (8, "scripts/pipeline/08_fix_relational_data.py", False),
        (9, "scripts/pipeline/09_fix_suwalki_geometry.py", False),
        (10, "scripts/pipeline/10_unify_schemas.py", False),
        (11, "scripts/pipeline/11_build_master_db.py", True),
        (12, "scripts/pipeline/12_audit_data_quality.py", False),
        (13, "scripts/pipeline/13_isolate_city_data.py", False),
        (14, "scripts/pipeline/14_build_isc_valuation.py", False)
    ]

    orch.logger.info("=== URUCHAMIANIE TURBO ORKIESTRATORA 2.0 ===")
    
    for num, script, is_global in pipeline:
        if args.step is not None and args.step != num:
            continue
            
        success = False
        if is_global:
            success = orch.run_global_step(f"step_{num:02d}", script)
        else:
            success = orch.run_city_parallel_step(f"step_{num:02d}", script)
            
        if not success and args.step is None:
            orch.logger.error(f"KRYTYCZNY PRZESTÓJ na kroku {num}. Popraw błędy i wznów.")
            sys.exit(1)

    orch.logger.info("\n=== POTOK ZAKOŃCZONY SUKCESEM DLA WSZYSTKICH MIAST ===")

if __name__ == "__main__":
    main()
