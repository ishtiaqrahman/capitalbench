# Full-Universe Horizon-Specific Decision Context

Profile: monthly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: tiingo_eod_history_through_2026-09-25; repository_daily_price_snapshots_2026-09-28_to_2026-10-06_(tiingo_eod_or_yahoo_chart_adjclose); yahoo_chart_reported_volume_2026-09-28_to_2026-10-06
- As-of date requested: 2026-10-06
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | 1.95% |
| spy_return_21s | 1.41% |
| rsp_return_5s | 1.35% |
| rsp_return_21s | -2.68% |
| hyg_return_5s | -0.12% |
| hyg_return_21s | -2.39% |
| tlt_return_5s | -1.21% |
| tlt_return_21s | -6.00% |
| uup_return_5s | 0.52% |
| uup_return_21s | 2.92% |
| uso_return_5s | 1.09% |
| uso_return_21s | 2.08% |
| iau_return_5s | -0.19% |
| iau_return_21s | -6.02% |
| rsp_minus_spy_5s | -0.60% |
| rsp_minus_spy_21s | -4.09% |
| positive_asset_share_5s | 62.32% |
| positive_asset_share_21s | 31.88% |
| active_return_dispersion_5s |  |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_5s | active_return_21s | prior_105s_active_return | volatility_63s | max_drawdown_63s | volume_zscore_20v120 | corr_spy_252s | beta_spy_252s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | -1.41% | -17.13% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | -0.22% | -1.41% | -15.64% | 0.56% | -0.26% | 0.345 | -0.052 | -0.001 | -0.22% |
| SP500 | SPY | diversified_us_equity | 1.95% | 0.00% | 0.00% | 11.06% | -3.38% | -0.402 | 1.000 | 1.000 | 0.00% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | 1.94% | -0.67% | -0.11% | 11.23% | -3.39% | -0.416 | 0.995 | 1.012 | -0.46% |
| NASDAQ100 | QQQ | technology_and_growth | 2.94% | 4.36% | 5.15% | 18.71% | -8.79% | -0.666 | 0.929 | 1.424 | 0.00% |
| LARGE_GROWTH | IWF | technology_and_growth | 3.10% | 3.37% | -2.76% | 17.86% | -7.99% | -0.486 | 0.935 | 1.288 | 0.00% |
| LARGE_VALUE | IWD | diversified_us_equity | 1.11% | -3.33% | 2.14% | 8.75% | -4.06% | -0.293 | 0.808 | 0.703 | -2.59% |
| MID_CAP | IJH | diversified_us_equity | 2.25% | -3.54% | -6.21% | 11.64% | -8.26% | -0.023 | 0.816 | 0.967 | -5.65% |
| SMALL_CAP | IWM | diversified_us_equity | 0.84% | -6.11% | 0.19% | 13.17% | -8.68% | -0.173 | 0.821 | 1.178 | -7.54% |
| SMALL_VALUE | IWN | diversified_us_equity | 0.65% | -6.48% | -0.61% | 10.80% | -7.53% | -0.178 | 0.741 | 0.924 | -6.24% |
| DIVIDEND | SCHD | diversified_us_equity | 0.00% | -6.25% | -2.35% | 11.06% | -6.87% | 0.166 | 0.300 | 0.258 | -5.96% |
| LOW_VOL | SPLV | diversified_us_equity | 0.76% | -5.24% | -14.86% | 9.50% | -9.22% | -0.658 | 0.035 | 0.028 | -7.65% |
| MOMENTUM | MTUM | diversified_us_equity | 2.37% | 5.23% | 5.30% | 26.69% | -12.01% | 0.375 | 0.763 | 1.556 | -5.83% |
| TECHNOLOGY | XLK | technology_and_growth | 3.86% | 6.58% | 19.30% | 25.48% | -10.34% | -0.839 | 0.852 | 1.734 | 0.00% |
| COMMUNICATIONS | XLC | technology_and_growth | 0.16% | -1.43% | -16.68% | 20.52% | -7.06% | 0.119 | 0.558 | 0.686 | -6.18% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | 2.35% | -3.97% | -10.29% | 19.03% | -9.02% | -0.414 | 0.778 | 1.165 | -9.73% |
| CONSUMER_STAPLES | XLP | consumer_defensive | -0.06% | -4.06% | -12.32% | 15.33% | -7.54% | -0.280 | -0.044 | -0.049 | -7.37% |
| HEALTHCARE | XLV | healthcare_and_biotech | -2.13% | -3.58% | 0.36% | 16.69% | -5.87% | -0.619 | 0.225 | 0.271 | -4.53% |
| FINANCIALS | XLF | financials | 0.00% | -8.12% | -0.25% | 12.04% | -8.49% | 0.111 | 0.545 | 0.618 | -7.45% |
| INDUSTRIALS | XLI | industrials_and_defense | 1.45% | -3.25% | -10.18% | 14.31% | -10.23% | -0.283 | 0.708 | 0.942 | -7.76% |
| ENERGY | XLE | energy | 3.59% | -1.28% | -9.89% | 20.80% | -6.15% | -0.167 | -0.172 | -0.289 | -2.72% |
| MATERIALS | XLB | materials_and_mining | 1.28% | -6.14% | -12.03% | 16.04% | -9.14% | -0.000 | 0.534 | 0.734 | -6.92% |
| UTILITIES | XLU | rate_sensitive_defensive | 3.65% | -5.16% | -23.43% | 14.93% | -14.58% | 1.864 | 0.130 | 0.155 | -11.97% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | -0.58% | -7.07% | -10.92% | 12.18% | -10.87% | 0.234 | 0.263 | 0.286 | -9.93% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | -0.36% | -4.79% | -18.62% | 5.10% | -4.58% | 0.543 | 0.311 | 0.115 | -6.91% |
| LONG_TREASURY | TLT | rates_and_duration | -1.21% | -7.40% | -20.41% | 9.76% | -8.05% | 1.728 | 0.268 | 0.193 | -12.62% |
| TIPS | TIP | rates_and_duration | 0.16% | -4.01% | -17.37% | 3.77% | -3.40% | 0.127 | 0.282 | 0.076 | -3.77% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | -0.26% | -4.57% | -18.50% | 5.84% | -4.65% | 0.600 | 0.482 | 0.203 | -6.05% |
| HIGH_YIELD_CREDIT | HYG | credit | -0.12% | -3.79% | -15.29% | 3.40% | -3.25% | 1.411 | 0.760 | 0.230 | -2.78% |
| AGGREGATE_BONDS | AGG | rates_and_duration | -0.25% | -4.13% | -17.65% | 4.36% | -3.62% | 0.925 | 0.410 | 0.124 | -4.73% |
| DEVELOPED_EX_US | VEA | international_equity | -0.10% | -4.76% | -3.22% | 14.94% | -4.62% | -0.518 | 0.803 | 1.090 | -3.39% |
| EMERGING_MARKETS | VWO | international_equity | 1.68% | -2.55% | -3.41% | 14.41% | -4.96% | -0.464 | 0.823 | 1.132 | -1.15% |
| EUROPE | VGK | international_equity | -1.45% | -6.79% | -5.81% | 12.01% | -8.03% | -0.156 | 0.745 | 0.911 | -6.86% |
| JAPAN | EWJ | international_equity | 2.91% | -0.35% | -1.59% | 19.90% | -5.50% | -0.555 | 0.732 | 1.197 | 0.00% |
| CHINA | MCHI | international_equity | 0.23% | -6.31% | -17.74% | 15.96% | -9.99% | -0.770 | 0.577 | 0.874 | -20.15% |
| INDIA | INDA | international_equity | -0.45% | -7.78% | -11.75% | 12.20% | -8.25% | -0.542 | 0.577 | 0.684 | -15.48% |
| GOLD | IAU | precious_metals | -0.19% | -7.43% | -22.86% | 24.22% | -11.69% | -0.382 | 0.334 | 0.754 | -22.84% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | 1.94% | 0.96% | -8.63% | 21.33% | -6.42% | -0.242 | -0.187 | -0.298 | -3.18% |
| SEMICONDUCTORS | SMH | technology_and_growth | 4.22% | 10.14% | 24.66% | 38.08% | -17.48% | -0.873 | 0.773 | 2.367 | -5.44% |
| SOFTWARE | IGV | technology_and_growth | 5.65% | 4.90% | 12.79% | 32.28% | -8.27% | -1.244 | 0.492 | 1.206 | -5.04% |
| BROAD_AI_TECH | AIQ | technology_and_growth | 3.07% | 2.84% | 17.29% | 26.28% | -12.30% | -0.692 | 0.851 | 1.923 | -4.40% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | 4.93% | 2.64% | -11.15% | 28.79% | -12.14% | -0.827 | 0.809 | 2.184 | -11.56% |
| CYBERSECURITY | CIBR | technology_and_growth | 6.04% | 12.91% | 27.96% | 32.92% | -9.53% | 0.482 | 0.498 | 1.117 | 0.00% |
| SOLAR | TAN | clean_energy | 2.23% | -8.98% | -27.29% | 34.90% | -22.94% | -0.683 | 0.650 | 1.926 | -39.94% |
| METALS_MINING | XME | materials_and_mining | 4.18% | -10.10% | -9.02% | 35.82% | -15.75% | -0.771 | 0.599 | 1.774 | -18.40% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | 1.35% | -4.09% | -3.51% | 9.76% | -6.27% | -0.536 | 0.780 | 0.701 | -4.33% |
| BIOTECH | XBI | healthcare_and_biotech | -3.77% | -9.29% | 10.12% | 29.39% | -11.00% | 0.169 | 0.470 | 1.025 | -11.00% |
| REGIONAL_BANKS | KRE | financials | 0.34% | -7.78% | -3.71% | 15.58% | -10.38% | 0.284 | 0.424 | 0.719 | -9.57% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | -0.50% | -8.99% | -16.03% | 19.69% | -18.16% | 0.262 | 0.568 | 1.015 | -17.66% |
| CANADA | EWC | international_equity | 0.42% | -6.02% | -5.27% | 11.86% | -6.96% | -0.114 | 0.680 | 0.762 | -5.52% |
| UNITED_KINGDOM | EWU | international_equity | -1.02% | -5.98% | -10.72% | 10.88% | -7.09% | -0.289 | 0.605 | 0.699 | -6.11% |
| AUSTRALIA | EWA | international_equity | 0.63% | -6.96% | -9.71% | 16.14% | -8.02% | 0.275 | 0.681 | 0.948 | -6.18% |
| SOUTH_KOREA | EWY | international_equity | -0.37% | -2.71% | 31.36% | 58.22% | -21.94% | -0.857 | 0.638 | 2.805 | -14.96% |
| TAIWAN | EWT | international_equity | 3.07% | 3.43% | 39.06% | 32.47% | -15.80% | -0.782 | 0.758 | 1.865 | -0.33% |
| BRAZIL | EWZ | international_equity | 17.91% | 12.17% | -17.75% | 33.77% | -8.05% | 1.083 | 0.460 | 1.003 | 0.00% |
| MEXICO | EWW | international_equity | 0.89% | -6.55% | -14.75% | 17.08% | -10.38% | -0.392 | 0.562 | 0.959 | -9.20% |
| SOUTH_AFRICA | EZA | international_equity | -1.84% | -12.55% | -10.19% | 27.04% | -13.31% | -0.279 | 0.629 | 1.616 | -20.33% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | -0.18% | -5.03% | -17.62% | 5.56% | -4.64% | 4.858 | 0.404 | 0.147 | -5.47% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | 0.74% | -4.30% | -18.19% | 4.38% | -5.77% | 8.167 | 0.363 | 0.094 | -5.57% |
| EMERGING_MARKET_BONDS | EMB | credit | -0.36% | -5.13% | -14.45% | 5.99% | -5.27% | 0.735 | 0.688 | 0.316 | -4.84% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | -0.02% | -2.67% | -16.89% | 3.80% | -2.25% | 0.313 | 0.478 | 0.138 | -3.20% |
| SILVER | SLV | precious_metals | -0.05% | -8.71% | -26.41% | 37.84% | -13.16% | -0.558 | 0.372 | 1.794 | -47.49% |
| COPPER | CPER | non_energy_commodities | 0.25% | -1.21% | 0.09% | 22.85% | -6.80% | -0.255 | 0.572 | 1.262 | -3.38% |
| AGRICULTURE | DBA | non_energy_commodities | 2.12% | -1.41% | -10.32% | 12.86% | -4.61% | -0.271 | 0.065 | 0.056 | -2.17% |
| OIL | USO | energy | 1.09% | 0.67% | -14.32% | 51.89% | -17.64% | -0.436 | -0.349 | -1.332 | -10.47% |
| US_DOLLAR | UUP | currencies | 0.52% | 1.51% | -15.94% | 5.24% | -2.52% | -0.239 | -0.296 | -0.126 | -0.31% |
| EURO | FXE | currencies | -0.71% | -4.42% | -16.66% | 4.66% | -3.83% | -0.317 | 0.280 | 0.117 | -5.96% |
| YEN | FXY | currencies | -0.58% | -2.67% | -15.19% | 9.96% | -3.38% | -0.046 | 0.177 | 0.116 | -5.39% |
| BITCOIN_ETF | IBIT | crypto_assets | 2.45% | 5.80% | -1.45% | 37.36% | -7.14% | -0.073 | 0.500 | 1.750 | -31.98% |
| ETHEREUM_ETF | ETHA | crypto_assets | 200.25% | 227.37% | -1.02% | 397.26% | -5.32% | 0.059 | 0.195 | 3.125 | 0.00% |
