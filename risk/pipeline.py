import logging
import numpy as np
import pandas as pd
from pathlib import Path
from .metrics import *
from .backtests import kupiec_test

logging.basicConfig(level=logging.INFO)

def run_pipeline():
    root = Path(__file__).resolve().parents[1]
    prices_path = root / "data" / "raw" / "prices.csv"
    out_dir = root / "data" / "processed"
    out_dir.mkdir(parents=True, exist_ok=True)

    prices = pd.read_csv(prices_path, parse_dates=["date"]).set_index("date")
    returns = compute_simple_returns(prices)

    weights = pd.Series({"SPY":0.4,"QQQ":0.3,"TLT":0.15,"GLD":0.15})
    weights = weights.reindex(returns.columns).fillna(0)

    port_ret = compute_portfolio_return(returns, weights)
    equity = compute_equity_curve(port_ret)
    drawdown = compute_drawdown(equity)

    vol = rolling_volatility(port_ret, 20)
    var = rolling_var_loss(port_ret, 20, 0.05)
    es = rolling_es_loss(port_ret, 20, 0.05)

    df = pd.DataFrame({
        "date": port_ret.index,
        "portfolio_return": port_ret.values,
        "equity": equity.values,
        "drawdown": drawdown.values,
        "vol_20d": vol.values,
        "var_95_loss_20d": var.values,
        "es_95_loss_20d": es.values
    }).dropna()

    df["var_breach"] = (df["portfolio_return"] < -df["var_95_loss_20d"]).astype(int)

    df.to_csv(out_dir / "risk_timeseries.csv", index=False)
    returns.reset_index().to_csv(out_dir / "returns.csv", index=False)

    pd.DataFrame([kupiec_test(df["var_breach"], 0.05)]).to_csv(out_dir / "var_backtest.csv", index=False)
