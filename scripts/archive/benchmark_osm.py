import os
import sys
import time
import psutil
import threading
from pathlib import Path

# Ścieżka do skryptu core
sys.path.append(str(Path("scripts/core").absolute()))
from extract_all_osm_turbo import process_city_turbo

class ResourceMonitor(threading.Thread):
    def __init__(self):
        super().__init__()
        self.max_rss = 0
        self.cpu_samples = []
        self.stop_flag = False

    def run(self):
        process = psutil.Process(os.getpid())
        while not self.stop_flag:
            try:
                # Pobieramy RSS (RAM) dla głównego procesu i wszystkich potomnych (GDAL/Osmium)
                total_rss = process.memory_info().rss
                for child in process.children(recursive=True):
                    total_rss += child.memory_info().rss
                
                self.max_rss = max(self.max_rss, total_rss)
                self.cpu_samples.append(psutil.cpu_percent(interval=None))
                time.sleep(0.5)
            except:
                pass

def run_benchmark():
    city_name = "poznan"
    city_dir = Path(f"data/cities/{city_name}")
    output_gpkg = city_dir / "osm_full.gpkg"
    
    if output_gpkg.exists():
        output_gpkg.unlink()

    print(f"=== BENCHMARK: OSM EXTRACTION ({city_name.upper()}) ===")
    print("Metoda: Osmium Clipping -> GDAL Conversion")
    
    monitor = ResourceMonitor()
    monitor.start()
    
    start_time = time.time()
    result = process_city_turbo(city_dir)
    end_time = time.time()
    
    monitor.stop_flag = True
    monitor.join()
    
    duration = end_time - start_time
    avg_cpu = sum(monitor.cpu_samples) / len(monitor.cpu_samples) if monitor.cpu_samples else 0
    peak_ram_mb = monitor.max_rss / (1024 * 1024)
    
    print("-" * 40)
    print(f"STATUS: {result}")
    print(f"CZAS TRWANIA: {duration:.2f} s")
    print(f"SZCZYTOWY RAM: {peak_ram_mb:.2f} MB")
    print(f"ŚREDNIE CPU:   {avg_cpu:.1f} %")
    
    if output_gpkg.exists():
        print(f"ROZMIAR PLIKU: {output_gpkg.stat().st_size / (1024*1024):.2f} MB")
    print("-" * 40)

if __name__ == "__main__":
    run_benchmark()
