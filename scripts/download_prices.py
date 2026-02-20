import yfinance as yf
from pathlib import Path

tickers = ["SPY","QQQ","TLT","GLD"]
start = "2015-01-01"

root = Path(__file__).resolve().parents[1]
outpath = root / "data" / "raw" / "prices.csv"
outpath.parent.mkdir(parents=True, exist_ok=True)

df = yf.download(tickers, start=start, auto_adjust=True, progress=False)
prices = df["Close"]
prices.index.name = "date"
prices.to_csv(outpath)
