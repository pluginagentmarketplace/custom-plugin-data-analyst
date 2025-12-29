#!/usr/bin/env python3
import json
REQUIRED = {"junior": ["Excel", "SQL"], "mid": ["Python", "Tableau"], "senior": ["ML basics", "Leadership"]}
def assess(skills, level): return {"level": level, "has": [s for s in REQUIRED.get(level, []) if s in skills], "missing": [s for s in REQUIRED.get(level, []) if s not in skills]}
if __name__ == "__main__":
    print(json.dumps(assess(["Excel", "SQL", "Python"], "mid"), indent=2))
