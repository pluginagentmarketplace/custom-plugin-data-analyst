#!/usr/bin/env python3
import re, json
PATTERNS = {"select": r"\bSELECT\b", "join": r"\bJOIN\b", "groupby": r"\bGROUP BY\b", "window": r"\bOVER\s*\("}
def validate(sql): return {k: bool(re.search(v, sql, re.I)) for k, v in PATTERNS.items()}
if __name__ == "__main__":
    import sys; print(json.dumps(validate(open(sys.argv[1]).read() if len(sys.argv)>1 else sys.stdin.read()), indent=2))
