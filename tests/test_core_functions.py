"""
Testy jednostkowe dla kluczowych funkcji pipeline'u kielce-analiza.
Uruchamianie: python3 -m pytest tests/ -v
"""
import sys
from pathlib import Path
import pandas as pd
import numpy as np

# Dodaj root projektu do sys.path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))


# ============================================================
# Test parse_hstore z 14_build_isc_valuation.py
# ============================================================
class TestParseHstore:
    """Test parsera HSTORE z 14_build_isc_valuation.py"""
    
    def _parse(self, val):
        from scripts.pipeline._14_build_isc_valuation_funcs import parse_hstore
        return parse_hstore(val)
    
    def test_none(self):
        from scripts.pipeline.build_isc_valuation_funcs import parse_hstore
        assert parse_hstore(None) == {}
    
    def test_nan(self):
        from scripts.pipeline.build_isc_valuation_funcs import parse_hstore
        assert parse_hstore(float('nan')) == {}
    
    def test_basic(self):
        from scripts.pipeline.build_isc_valuation_funcs import parse_hstore
        result = parse_hstore('"amenity"=>"hospital","name"=>"Szpital"')
        assert result["amenity"] == "hospital"
        assert result["name"] == "Szpital"
    
    def test_empty_string(self):
        from scripts.pipeline.build_isc_valuation_funcs import parse_hstore
        assert parse_hstore("") == {}


# ============================================================
# Test identify_v7_9_tag z 14_build_isc_valuation.py
# ============================================================
class TestIdentifyTag:
    """Test klasyfikatora POI z 14_build_isc_valuation.py"""
    
    def _tag(self, row_dict, city="kielce"):
        from scripts.pipeline.build_isc_valuation_funcs import identify_v7_9_tag
        row = pd.Series(row_dict)
        return identify_v7_9_tag(row, city)
    
    def test_hospital(self):
        cat, tier = self._tag({"amenity": "hospital"})
        assert cat == "hospital_clinical"
        assert tier == "T1_NATIONAL_MAGNET"
    
    def test_railway_station_with_uic(self):
        cat, tier = self._tag({"railway": "station", "all_tags": '"uic_ref"=>"5100001"'})
        assert "rail" in cat
        assert tier == "T0_MEGA_HUB"
    
    def test_railway_station_regional(self):
        cat, tier = self._tag({"railway": "station", "all_tags": '"name"=>"Mala Stacja"'})
        assert tier == "T1_NATIONAL_MAGNET"
    
    def test_unknown_tag(self):
        cat, tier = self._tag({"amenity": "unknown_thing_xyz"})
        assert cat is None
        assert tier is None
    
    def test_supermarket(self):
        cat, tier = self._tag({"shop": "supermarket"})
        assert cat == "supermarket"
        assert tier == "T2_STRATEGIC_HUB"


# ============================================================
# Standalone test: parse_hstore i identify_v7_9_tag
# Importowane bezposrednio bo modul nie jest pakietem
# ============================================================

def _import_funcs():
    """Importuje funkcje z 14_build_isc_valuation.py bez side-effectow."""
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "isc_valuation",
        PROJECT_ROOT / "scripts" / "pipeline" / "14_build_isc_valuation.py"
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.parse_hstore, mod.identify_v7_9_tag


class TestParseHstoreDirect:
    """Testy parse_hstore bezposrednio z pliku"""
    
    def setup_method(self):
        self.parse_hstore, self.identify_tag = _import_funcs()
    
    def test_none(self):
        assert self.parse_hstore(None) == {}
    
    def test_nan(self):
        assert self.parse_hstore(float('nan')) == {}
    
    def test_basic(self):
        result = self.parse_hstore('"amenity"=>"hospital","name"=>"Szpital"')
        assert result["amenity"] == "hospital"
        assert result["name"] == "Szpital"
    
    def test_empty_string(self):
        assert self.parse_hstore("") == {}
    
    def test_without_quotes(self):
        result = self.parse_hstore('amenity=>pharmacy,name=>Apteka')
        assert result["amenity"] == "pharmacy"


class TestIdentifyTagDirect:
    """Testy identify_v7_9_tag bezposrednio z pliku"""
    
    def setup_method(self):
        self.parse_hstore, self.identify_tag = _import_funcs()
    
    def test_hospital(self):
        row = pd.Series({"amenity": "hospital", "all_tags": ""})
        cat, tier = self.identify_tag(row, "kielce")
        assert cat == "hospital_clinical"
        assert tier == "T1_NATIONAL_MAGNET"
    
    def test_airport_international(self):
        row = pd.Series({"aeroway": "aerodrome", "all_tags": '"iata"=>"KRK","name"=>"Balice"'})
        cat, tier = self.identify_tag(row, "krakow")
        assert cat == "international_airport"
        assert tier == "T0_MEGA_HUB"
    
    def test_airport_local(self):
        row = pd.Series({"aeroway": "aerodrome", "all_tags": '"name"=>"Lotnisko Sportowe"'})
        cat, tier = self.identify_tag(row, "kielce")
        assert cat == "local_airfield"
        assert tier == "T5_SPEC_GASTRO"
    
    def test_rail_main_station(self):
        row = pd.Series({"railway": "station", "all_tags": '"name"=>"Kielce Główne"'})
        cat, tier = self.identify_tag(row, "kielce")
        assert "rail" in cat
        assert tier == "T0_MEGA_HUB"
    
    def test_rail_regional(self):
        row = pd.Series({"railway": "station", "all_tags": '"name"=>"Przystanek Leśny"'})
        cat, tier = self.identify_tag(row, "kielce")
        assert tier == "T1_NATIONAL_MAGNET"
    
    def test_supermarket(self):
        row = pd.Series({"shop": "supermarket", "all_tags": ""})
        cat, tier = self.identify_tag(row, "kielce")
        assert cat == "supermarket"
        assert tier == "T2_STRATEGIC_HUB"
    
    def test_unknown_returns_none(self):
        row = pd.Series({"amenity": "totally_unknown_xyz", "all_tags": ""})
        cat, tier = self.identify_tag(row, "kielce")
        assert cat is None
        assert tier is None
    
    def test_pharmacy(self):
        row = pd.Series({"amenity": "pharmacy", "all_tags": ""})
        cat, tier = self.identify_tag(row, "kielce")
        assert cat == "pharmacy"
        assert tier == "T4_DAILY_SERVICE"
    
    def test_restaurant(self):
        row = pd.Series({"amenity": "restaurant", "all_tags": ""})
        cat, tier = self.identify_tag(row, "kielce")
        assert cat == "gastronomy"
        assert tier == "T5_SPEC_GASTRO"
