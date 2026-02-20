import numpy as np
import pandas as pd
from pathlib import Path

root = Path(__file__).resolve().parents[1]
returns = pd.read_csv(root/"data/processed/returns.csv", parse_dates=["date"]).set_index("date")

weights = np.array([0.4,0.3,0.15,0.15])
T = 252
n_sims = 5000

mu = returns.mean().values
cov = returns.cov().values

sims = np.random.multivariate_normal(mu, cov, (n_sims, T))
port = sims @ weights
equity = np.cumprod(1 + port, axis=1)
final = equity[:,-1] - 1

summary = pd.DataFrame({
    "expected_return":[final.mean()],
    "var_95_loss":[-np.quantile(final,0.05)],
    "es_95_loss":[-final[final<=np.quantile(final,0.05)].mean()]
})

summary.to_csv(root/"data/processed/mc_summary.csv", index=False)
