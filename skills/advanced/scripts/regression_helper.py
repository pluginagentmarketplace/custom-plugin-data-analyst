#!/usr/bin/env python3
import json
def regression_summary(r2, coeffs): return {"r_squared": r2, "coefficients": coeffs, "quality": "good" if r2 > 0.7 else "moderate" if r2 > 0.5 else "poor"}
if __name__ == "__main__":
    print(json.dumps(regression_summary(0.85, {"intercept": 10.5, "slope": 2.3}), indent=2))
