#!/usr/bin/env python3
import json
def profile(data): return {"rows": len(data), "columns": len(data[0]) if data else 0, "types": "mixed"}
if __name__ == "__main__":
    import sys, csv
    with open(sys.argv[1]) if len(sys.argv)>1 else sys.stdin as f:
        print(json.dumps(profile(list(csv.reader(f))), indent=2))
