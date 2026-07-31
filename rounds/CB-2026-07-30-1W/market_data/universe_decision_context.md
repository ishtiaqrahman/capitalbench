# Full-Universe Horizon-Specific Decision Context

Profile: weekly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: yahoo_chart_adjusted_close_and_reported_volume
- As-of date requested: 2026-07-30
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | 0.48% |
| spy_return_21s | -0.68% |
| rsp_return_5s | 1.63% |
| rsp_return_21s | 1.23% |
| hyg_return_5s | 0.30% |
| hyg_return_21s | -0.16% |
| tlt_return_5s | -0.44% |
| tlt_return_21s | -3.83% |
| uup_return_5s | -1.47% |
| uup_return_21s | -0.95% |
| uso_return_5s | -8.61% |
| uso_return_21s | 19.77% |
| iau_return_5s | 1.51% |
| iau_return_21s | 2.37% |
| rsp_minus_spy_5s | 1.16% |
| rsp_minus_spy_21s | 1.91% |
| positive_asset_share_5s | 68.12% |
| positive_asset_share_21s | 50.72% |
| active_return_dispersion_5s | 2.95% |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_3s | active_return_5s | prior_16s_active_return | volatility_21s | max_drawdown_21s | volume_zscore_5v60 | corr_spy_63s | beta_spy_63s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | -0.48% | 1.15% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.03% | -0.40% | 1.38% | 0.23% | -0.01% | -0.521 | -0.182 | -0.003 | 0.00% |
| SP500 | SPY | diversified_us_equity | 0.35% | 0.00% | 0.00% | 12.12% | -3.38% | 0.132 | 1.000 | 1.000 | -2.10% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | 0.30% | -0.04% | -0.30% | 11.83% | -3.29% | -0.435 | 0.993 | 0.988 | -1.88% |
| NASDAQ100 | QQQ | technology_and_growth | 0.21% | -1.69% | -4.88% | 24.02% | -10.14% | 0.686 | 0.917 | 1.708 | -8.29% |
| LARGE_GROWTH | IWF | technology_and_growth | 0.26% | -1.45% | -3.34% | 22.40% | -8.15% | -0.723 | 0.892 | 1.304 | -8.73% |
| LARGE_VALUE | IWD | diversified_us_equity | 0.39% | 1.36% | 2.70% | 9.97% | -1.31% | -0.261 | 0.717 | 0.639 | -0.53% |
| MID_CAP | IJH | diversified_us_equity | -0.86% | -0.61% | -1.00% | 12.27% | -3.09% | -0.483 | 0.799 | 0.863 | -2.28% |
| SMALL_CAP | IWM | diversified_us_equity | -0.11% | -0.30% | -1.63% | 13.22% | -3.95% | -0.470 | 0.791 | 1.076 | -2.62% |
| SMALL_VALUE | IWN | diversified_us_equity | -0.17% | 0.07% | 0.87% | 11.12% | -1.83% | 0.615 | 0.676 | 0.755 | -1.07% |
| DIVIDEND | SCHD | diversified_us_equity | -0.06% | 1.38% | 4.59% | 14.30% | -1.42% | 2.156 | 0.095 | 0.086 | -1.42% |
| LOW_VOL | SPLV | diversified_us_equity | -1.09% | -0.45% | 3.29% | 15.31% | -2.04% | -0.143 | -0.285 | -0.280 | -2.04% |
| MOMENTUM | MTUM | diversified_us_equity | -1.18% | -5.32% | -7.26% | 41.15% | -17.42% | 0.673 | 0.751 | 2.146 | -13.46% |
| TECHNOLOGY | XLK | technology_and_growth | 0.82% | -2.00% | -5.19% | 34.39% | -12.57% | -0.240 | 0.838 | 2.147 | -11.24% |
| COMMUNICATIONS | XLC | technology_and_growth | -1.00% | 0.66% | -0.48% | 23.46% | -7.06% | 0.333 | 0.365 | 0.478 | -10.73% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | 1.40% | 2.86% | -6.11% | 22.09% | -7.90% | -0.380 | 0.715 | 1.091 | -9.38% |
| CONSUMER_STAPLES | XLP | consumer_defensive | 0.13% | 2.24% | 1.32% | 21.01% | -3.03% | 1.104 | -0.300 | -0.383 | -3.85% |
| HEALTHCARE | XLV | healthcare_and_biotech | 0.07% | 0.81% | 2.90% | 20.87% | -3.74% | 0.005 | -0.125 | -0.171 | -2.24% |
| FINANCIALS | XLF | financials | 0.21% | 1.62% | 5.29% | 15.63% | -2.08% | 0.033 | 0.254 | 0.253 | -1.04% |
| INDUSTRIALS | XLI | industrials_and_defense | -2.63% | -2.43% | -0.63% | 16.58% | -4.80% | -0.498 | 0.658 | 0.963 | -3.86% |
| ENERGY | XLE | energy | 1.03% | -1.18% | 12.96% | 20.66% | -3.44% | -0.503 | -0.370 | -0.654 | -5.07% |
| MATERIALS | XLB | materials_and_mining | 0.49% | 2.21% | 0.09% | 18.56% | -3.81% | 0.018 | 0.517 | 0.759 | -2.90% |
| UTILITIES | XLU | rate_sensitive_defensive | -2.23% | -3.79% | 3.03% | 16.37% | -3.52% | -0.173 | -0.045 | -0.056 | -5.18% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | -1.01% | 0.30% | 3.24% | 15.52% | -1.65% | 0.184 | -0.104 | -0.124 | -1.54% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | -0.08% | -0.09% | -0.34% | 4.08% | -1.49% | -0.886 | 0.529 | 0.193 | -3.33% |
| LONG_TREASURY | TLT | rates_and_duration | -1.13% | -0.92% | -2.25% | 8.48% | -3.83% | 0.602 | 0.432 | 0.295 | -7.12% |
| TIPS | TIP | rates_and_duration | 0.33% | -0.24% | 0.34% | 2.59% | -1.01% | -0.080 | 0.500 | 0.128 | -1.21% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | -0.09% | -0.33% | -1.08% | 4.76% | -2.27% | 0.591 | 0.593 | 0.230 | -2.95% |
| HIGH_YIELD_CREDIT | HYG | credit | 0.25% | -0.17% | 0.68% | 2.77% | -0.80% | 0.364 | 0.784 | 0.209 | -0.50% |
| AGGREGATE_BONDS | AGG | rates_and_duration | -0.07% | -0.19% | -0.18% | 3.52% | -1.34% | -0.147 | 0.575 | 0.173 | -2.12% |
| DEVELOPED_EX_US | VEA | international_equity | 1.56% | 1.40% | -0.91% | 19.19% | -4.09% | -0.311 | 0.842 | 1.320 | -1.80% |
| EMERGING_MARKETS | VWO | international_equity | -0.07% | -0.32% | -1.51% | 19.15% | -5.24% | -0.619 | 0.869 | 1.317 | -4.98% |
| EUROPE | VGK | international_equity | 2.42% | 3.12% | 0.35% | 15.71% | -2.53% | -0.355 | 0.742 | 0.994 | 0.00% |
| JAPAN | EWJ | international_equity | 1.95% | 1.93% | -1.18% | 26.46% | -6.21% | -0.571 | 0.785 | 1.372 | -3.79% |
| CHINA | MCHI | international_equity | 2.29% | 3.55% | 5.70% | 19.45% | -2.22% | -0.572 | 0.447 | 0.686 | -15.58% |
| INDIA | INDA | international_equity | 1.66% | 3.87% | -2.41% | 14.30% | -4.51% | 0.844 | 0.571 | 0.666 | -10.11% |
| GOLD | IAU | precious_metals | 0.68% | 1.03% | 2.00% | 21.36% | -4.47% | -0.884 | 0.652 | 1.145 | -23.89% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | 0.92% | -3.58% | 14.88% | 24.55% | -5.54% | -0.305 | -0.178 | -0.289 | -7.46% |
| SEMICONDUCTORS | SMH | technology_and_growth | -1.76% | -7.59% | -10.39% | 53.49% | -23.12% | 2.764 | 0.790 | 3.183 | -19.44% |
| SOFTWARE | IGV | technology_and_growth | 2.64% | 6.65% | -2.71% | 25.34% | -8.11% | 0.147 | 0.310 | 0.756 | -20.77% |
| BROAD_AI_TECH | AIQ | technology_and_growth | 0.67% | -1.55% | -8.42% | 37.25% | -14.68% | 0.127 | 0.821 | 2.414 | -16.32% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | -0.77% | -2.93% | -10.47% | 33.39% | -17.14% | -0.080 | 0.861 | 2.477 | -20.75% |
| CYBERSECURITY | CIBR | technology_and_growth | 1.03% | 2.15% | -1.22% | 24.90% | -7.40% | -0.946 | 0.430 | 1.013 | -4.97% |
| SOLAR | TAN | clean_energy | -3.34% | -6.17% | -9.50% | 41.71% | -19.39% | 0.729 | 0.743 | 2.531 | -32.58% |
| METALS_MINING | XME | materials_and_mining | -1.21% | -1.75% | -2.37% | 36.47% | -8.74% | -0.235 | 0.705 | 2.108 | -23.26% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | 0.09% | 1.16% | 0.75% | 9.99% | -1.46% | 0.244 | 0.690 | 0.564 | -1.06% |
| BIOTECH | XBI | healthcare_and_biotech | 0.58% | -0.98% | -2.65% | 27.06% | -9.96% | -0.307 | 0.384 | 0.854 | -7.80% |
| REGIONAL_BANKS | KRE | financials | 0.50% | 0.52% | 1.55% | 20.27% | -3.73% | -0.705 | 0.202 | 0.293 | -2.59% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | -2.37% | -0.52% | -0.58% | 25.12% | -8.58% | 0.422 | 0.489 | 0.925 | -5.04% |
| CANADA | EWC | international_equity | 0.67% | 1.17% | 3.20% | 9.93% | -1.46% | -0.538 | 0.622 | 0.598 | -0.08% |
| UNITED_KINGDOM | EWU | international_equity | 2.77% | 3.76% | 2.36% | 15.34% | -1.93% | -0.367 | 0.496 | 0.616 | 0.00% |
| AUSTRALIA | EWA | international_equity | 3.25% | 4.19% | 2.32% | 15.96% | -1.63% | -0.351 | 0.644 | 0.892 | -0.07% |
| SOUTH_KOREA | EWY | international_equity | 0.01% | -7.75% | -12.74% | 81.16% | -28.57% | 1.597 | 0.721 | 4.365 | -26.46% |
| TAIWAN | EWT | international_equity | -3.90% | -6.32% | -6.92% | 45.53% | -17.68% | -0.165 | 0.794 | 2.569 | -15.72% |
| BRAZIL | EWZ | international_equity | 1.84% | 0.52% | 5.99% | 23.72% | -3.14% | -0.781 | 0.485 | 0.858 | -11.63% |
| MEXICO | EWW | international_equity | 0.74% | 2.34% | 0.79% | 18.07% | -2.98% | -0.293 | 0.662 | 1.002 | -3.68% |
| SOUTH_AFRICA | EZA | international_equity | 3.50% | 5.61% | -3.22% | 25.67% | -6.50% | -0.268 | 0.764 | 1.835 | -19.71% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | -0.09% | -0.03% | -0.23% | 4.32% | -1.48% | 0.601 | 0.581 | 0.206 | -2.03% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | -0.04% | -0.00% | -0.78% | 3.35% | -2.15% | 2.323 | 0.563 | 0.126 | -1.68% |
| EMERGING_MARKET_BONDS | EMB | credit | -0.18% | -0.20% | -0.42% | 4.85% | -1.89% | -0.032 | 0.753 | 0.323 | -1.69% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | -0.08% | -0.12% | -0.11% | 3.68% | -1.26% | -0.736 | 0.561 | 0.173 | -1.57% |
| SILVER | SLV | precious_metals | 1.08% | 2.29% | -1.49% | 38.13% | -10.19% | -0.761 | 0.629 | 2.322 | -49.34% |
| COPPER | CPER | non_energy_commodities | 1.47% | 2.40% | 2.50% | 22.58% | -3.26% | -0.529 | 0.703 | 1.510 | -3.10% |
| AGRICULTURE | DBA | non_energy_commodities | -0.51% | -3.17% | 7.04% | 16.53% | -2.69% | -0.546 | 0.090 | 0.092 | -4.35% |
| OIL | USO | energy | 2.18% | -9.09% | 32.20% | 63.19% | -13.62% | 0.015 | -0.351 | -1.371 | -16.66% |
| US_DOLLAR | UUP | currencies | -1.61% | -1.95% | 1.68% | 5.81% | -1.61% | 0.018 | -0.483 | -0.190 | -1.61% |
| EURO | FXE | currencies | 1.45% | 0.90% | 0.83% | 4.90% | -0.81% | -0.533 | 0.514 | 0.186 | -3.80% |
| YEN | FXY | currencies | 2.80% | 2.33% | 0.39% | 10.50% | -1.67% | 2.387 | 0.278 | 0.169 | -8.34% |
| BITCOIN_ETF | IBIT | crypto_assets | -0.19% | -0.34% | 11.24% | 30.48% | -4.43% | -0.635 | 0.463 | 1.256 | -48.52% |
| ETHEREUM_ETF | ETHA | crypto_assets | -1.36% | 2.36% | 19.82% | 45.59% | -4.20% | 0.137 | 0.564 | 2.180 | -60.34% |
