import numpy as np
import pandas as pd

def compute_simple_returns(prices: pd.DataFrame) -> pd.DataFrame:
    return prices.pct_change().dropna()

def compute_portfolio_return(returns: pd.DataFrame, weights: pd.Series) -> pd.Series:
    return returns.mul(weights, axis=1).sum(axis=1)

def compute_equity_curve(port_ret: pd.Series) -> pd.Series:
    return (1.0 + port_ret).cumprod()

def compute_drawdown(equity: pd.Series) -> pd.Series:
    peak = equity.cummax()
    return equity / peak - 1.0

def rolling_volatility(port_ret: pd.Series, window: int, trading_days: int = 252) -> pd.Series:
    return port_ret.rolling(window).std() * np.sqrt(trading_days)

def rolling_var_loss(port_ret: pd.Series, window: int, alpha: float) -> pd.Series:
    return -port_ret.rolling(window).quantile(alpha)

def rolling_es_loss(port_ret: pd.Series, window: int, alpha: float) -> pd.Series:
    def es_func(x):
        q = x.quantile(alpha)
        tail = x[x <= q]
        if tail.empty:
            return np.nan
        return float(-tail.mean())
    return port_ret.rolling(window).apply(es_func, raw=False)
