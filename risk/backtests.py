import numpy as np
import pandas as pd
from scipy.stats import chi2

def kupiec_test(breaches: pd.Series, alpha: float) -> dict:
    breaches = breaches.dropna().astype(int)
    T = len(breaches)
    x = breaches.sum()

    if T == 0:
        return {"status": "No Data"}

    p = alpha
    phat = x / T
    eps = 1e-12
    phat = min(max(phat, eps), 1 - eps)
    p = min(max(p, eps), 1 - eps)

    LR = -2 * np.log(((1 - p) ** (T - x) * p ** x) / ((1 - phat) ** (T - x) * phat ** x))
    p_value = 1 - chi2.cdf(LR, df=1)

    return {
        "observations": T,
        "breaches": int(x),
        "breach_rate": float(x / T),
        "p_value": float(p_value),
        "result": "PASS" if p_value >= 0.05 else "FAIL",
    }
