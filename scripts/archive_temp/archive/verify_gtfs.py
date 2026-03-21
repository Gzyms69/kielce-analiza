from pathlib import Path

def verify_gtfs():
    cities_root = Path('data/cities')
    cities = sorted([d for d in cities_root.iterdir() if d.is_dir()])
    
    print(f"Liczba sprawdzanych aglomeracji: {len(cities)}\n")
    
    missing_count = 0
    
    for city in cities:
        gtfs_dir = city / 'gtfs'
        if not gtfs_dir.exists():
            print(f"[BRAK] {city.name}: Brak folderu 'gtfs'!")
            missing_count += 1
            continue
            
        gtfs_subdirs = [d for d in gtfs_dir.iterdir() if d.is_dir()]
        
        valid_gtfs = [d.name for d in gtfs_subdirs if (d / 'stops.txt').exists()]
        invalid_gtfs = [d.name for d in gtfs_subdirs if not (d / 'stops.txt').exists()]
        
        if not valid_gtfs:
            print(f"[BRAK] {city.name}: Rozpakowano foldery, ale żaden nie zawiera 'stops.txt'!")
            missing_count += 1
        else:
            print(f"[OK] {city.name.ljust(15)} -> Poprawne źródła ({len(valid_gtfs)}): {valid_gtfs}")
            
        if invalid_gtfs:
            print(f"     -> UWAGA: Te archiwa są uszkodzone (brak stops.txt): {invalid_gtfs}")
            
    print(f"\nPodsumowanie: {len(cities) - missing_count} aglomeracji GOTOWYCH, {missing_count} z BRAKAMI.")

if __name__ == "__main__":
    verify_gtfs()
