# Portfolio Risk Analytics Framework

Production-style multi-asset portfolio risk analytics pipeline built in Python and designed to mirror institutional market risk workflows.

---

## Overview

This project implements an end-to-end quantitative risk monitoring system that:

- Computes rolling risk metrics (Volatility, VaR, Expected Shortfall)
- Validates Value-at-Risk using statistical backtesting
- Decomposes portfolio risk contributions
- Performs historical stress testing
- Simulates forward-looking portfolio distributions via Monte Carlo
- Exports structured outputs for Tableau visualization

The framework integrates financial theory, statistical modeling, and modular software design into a cohesive risk analytics engine.

---

## Assets Included

The portfolio consists of diversified ETFs:

| Ticker | Asset Class | Purpose |
|--------|-------------|---------|
| SPY | Broad U.S. Equities | Market exposure |
| QQQ | Technology Sector | Growth concentration |
| GLD | Gold | Defensive diversification |
| TLT | Long-Term Treasuries | Interest-rate hedge |

This multi-asset mix allows analysis of diversification, correlation behavior, and regime-dependent risk.

---

## Risk Methodology

### 1. Returns

Daily simple returns are computed as:

$$r_t = \frac{P_t}{P_{t-1}} - 1$$

Adjusted prices are used to account for stock splits and dividends.

### 2. Rolling Risk Metrics (20-Day Window)

**Rolling Volatility (Annualized)**
Measures dispersion of returns.

**Value-at-Risk (95%)**
Estimates the maximum expected daily loss with 95% confidence.

**Expected Shortfall (95%)**
Measures the average loss in the worst 5% of outcomes.

### 3. VaR Backtesting

Implements the Kupiec Proportion-of-Failures test:

- Validates whether observed VaR breaches occur near the expected 5% frequency.
- Flags model underestimation of tail risk.

### 4. Drawdown Analysis

Measures peak-to-trough capital decline:

$$\text{Drawdown}_t = \frac{\text{Equity}_t}{\text{Peak}_t} - 1$$

Maximum drawdown quantifies historical capital risk.

### 5. Risk Contribution

Volatility is decomposed into asset-level contributions:

$$\sigma_p = \sqrt{w^T \Sigma w}$$

Identifies concentration risk drivers and diversification benefits.

### 6. Historical Stress Testing

Evaluates performance during:

- COVID-19 Crash (2020)
- 2022 Rate Hike Regime
- Q4 2018 Selloff

Metrics reported: total return, worst day, maximum drawdown, and annualized volatility.

### 7. Monte Carlo Simulation (5,000 Paths)

One-year (252-day) forward simulation assuming:

- Constant drift and volatility
- Multivariate normal return distribution
- IID shocks

Outputs: terminal return distribution, forward VaR and Expected Shortfall, and downside dispersion.

---

## Tableau Dashboard Components

- Portfolio Equity Curve
- Rolling Volatility, VaR, ES
- Drawdown Analysis
- Risk Contribution by Asset
- Correlation Heatmap
- Historical Stress Analysis
- Monte Carlo Distribution
- VaR Breach Timeline

Designed to resemble institutional risk dashboards.

---

## Key Insights

- Equity exposure dominates portfolio risk contribution.
- Treasuries and gold provide diversification in normal regimes.
- Correlations increase during stress environments.
- VaR exceedances cluster in crisis periods.
- Monte Carlo reveals asymmetric downside risk.

---

## Project Structure

```
portfolio-risk-analytics/
│
├── risk/                  # Core risk modules
│   ├── metrics.py
│   ├── backtests.py
│   ├── pipeline.py
│
├── scripts/               # Executable scripts
│   ├── download_prices.py
│   ├── build_risk.py
│   ├── monte_carlo.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── README.md
└── requirements.txt
```

---

## How to Run

From the project root:

```bash
pip install -r requirements.txt
python scripts/download_prices.py
python scripts/build_risk.py
python scripts/monte_carlo.py
```

Outputs will be generated in `data/processed/`.

---

## Model Assumptions

- Gaussian parametric VaR
- 95% confidence level
- 20-day rolling window
- Constant drift and volatility
- IID return assumption for simulation

---

## Limitations

- Gaussian VaR underestimates extreme tail events
- Correlation is assumed stationary
- No volatility clustering modeling (e.g., GARCH)
- Historical stress limited to observed regimes

Future enhancements may include Student-t distributions, GARCH volatility modeling, bootstrapped Monte Carlo, and regime-switching correlation structures.

---

## Technologies Used

- Python (pandas, numpy, scipy, yfinance)
- Tableau
- Modular package architecture
- Git version control

---

## Project Goal

Demonstrate the integration of quantitative risk modeling, statistical validation, and professional data engineering into a structured portfolio risk monitoring system.

This project bridges financial theory and practical implementation, reflecting workflows used in asset management and market risk functions.