import osmium
import sys
from collections import Counter

class TaxonomyHandler(osmium.SimpleHandler):
    def __init__(self):
        super(TaxonomyHandler, self).__init__()
        self.stats = Counter()
        self.keys_of_interest = ['amenity', 'shop', 'leisure', 'office', 'industrial', 'aeroway', 'railway', 'landuse', 'craft', 'tourism', 'military']

    def count_tags(self, tags):
        for k in self.keys_of_interest:
            if k in tags:
                self.stats[f"{k}={tags[k]}"] += 1

    def node(self, n):
        self.count_tags(n.tags)

    def way(self, w):
        self.count_tags(w.tags)

    def relation(self, r):
        self.count_tags(r.tags)

def main():
    if len(sys.argv) < 2:
        print("Użycie: python extract_osm_taxonomy.py <file.osm.pbf>")
        return

    handler = TaxonomyHandler()
    handler.apply_file(sys.argv[1])

    print("--- TOP 200 OSM TAGS IN POLAND ---")
    for tag, count in handler.stats.most_common(200):
        print(f"{count:<10} | {tag}")

if __name__ == "__main__":
    main()
