import os
import shutil
from pathlib import Path

def get_data_dir():
    # Pobranie ścieżki z orkiestratora (domyślnie 'data')
    return Path(os.environ.get("PIPELINE_DATA_DIR", "data"))

def init_environment():
    data_dir = get_data_dir()
    print(f"=== INICJALIZACJA ŚRODOWISKA: {data_dir} ===")
    
    # Tworzenie szkieletu katalogów
    admin_dir = data_dir / "poland" / "admin"
    osm_dir = data_dir / "poland" / "osm"
    pop_dir = data_dir / "poland" / "population"
    cities_dir = data_dir / "cities"
    
    for d in [admin_dir, osm_dir, pop_dir, cities_dir]:
        d.mkdir(parents=True, exist_ok=True)
        print(f"[OK] Utworzono katalog: {d}")
        
    # Kopiowanie bazowego pliku powiaty.json z pierwotnego katalogu data/
    # (ze względu na to, że jest to zaufany plik, który nie zmienia się często)
    target_powiaty = admin_dir / "powiaty.json"
    source_powiaty = Path("data/poland/admin/powiaty.json")
    
    if target_powiaty.exists() and target_powiaty.stat().st_size > 100000:
        print(f"[SKIP] Plik powiaty.json już istnieje ({target_powiaty.stat().st_size // 1024} KB).")
        return
        
    if source_powiaty.exists():
        print(f"Kopiowanie mapy powiatów z {source_powiaty} do {target_powiaty} ...")
        shutil.copy2(source_powiaty, target_powiaty)
        print(f"[SUKCES] Skopiowano {target_powiaty.name}.")
    else:
        print(f"[BŁĄD] Nie znaleziono pliku źródłowego: {source_powiaty}")
        # Jeśli to padnie, cały pipeline musi się zatrzymać, bo bez tego nie zadziała WFS
        raise SystemExit(1)

if __name__ == "__main__":
    init_environment()
