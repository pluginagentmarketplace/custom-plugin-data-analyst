#!/usr/bin/env python3
import json, statistics
def calc(numbers): return {"mean": statistics.mean(numbers), "median": statistics.median(numbers), "stdev": statistics.stdev(numbers) if len(numbers)>1 else 0}
if __name__ == "__main__":
    import sys; nums = [float(x) for x in (open(sys.argv[1]).read() if len(sys.argv)>1 else sys.stdin.read()).split()]; print(json.dumps(calc(nums), indent=2))
