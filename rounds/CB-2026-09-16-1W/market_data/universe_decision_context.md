# Full-Universe Horizon-Specific Decision Context

Profile: weekly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: tiingo_eod_adjusted_price_and_volume
- As-of date requested: 2026-09-16
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | -1.10% |
| spy_return_21s | -2.41% |
| rsp_return_5s | -1.10% |
| rsp_return_21s | -3.85% |
| hyg_return_5s | -0.71% |
| hyg_return_21s | -0.95% |
| tlt_return_5s | -1.04% |
| tlt_return_21s | -0.20% |
| uup_return_5s | 1.50% |
| uup_return_21s | 1.07% |
| uso_return_5s | 4.13% |
| uso_return_21s | 19.86% |
| iau_return_5s | -2.87% |
| iau_return_21s | -3.36% |
| rsp_minus_spy_5s | -0.00% |
| rsp_minus_spy_21s | -1.44% |
| positive_asset_share_5s | 14.49% |
| positive_asset_share_21s | 21.74% |
| active_return_dispersion_5s | 2.37% |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_3s | active_return_5s | prior_16s_active_return | volatility_21s | max_drawdown_21s | volume_zscore_5v60 | corr_spy_63s | beta_spy_63s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | 1.10% | 1.33% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.01% | 1.15% | 1.54% | 0.17% | 0.00% | 0.276 | 0.079 | 0.001 | 0.00% |
| SP500 | SPY | diversified_us_equity | -1.34% | 0.00% | 0.00% | 8.68% | -2.47% | -0.044 | 1.000 | 1.000 | -3.06% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | -1.34% | -0.05% | -0.39% | 9.04% | -2.84% | -0.170 | 0.991 | 0.979 | -3.39% |
| NASDAQ100 | QQQ | technology_and_growth | -1.42% | -0.52% | -0.53% | 12.72% | -3.47% | -0.692 | 0.893 | 1.619 | -5.45% |
| LARGE_GROWTH | IWF | technology_and_growth | -1.33% | -0.38% | -0.77% | 13.61% | -3.61% | -0.140 | 0.882 | 1.455 | -6.23% |
| LARGE_VALUE | IWD | diversified_us_equity | -1.37% | 0.32% | 0.33% | 9.26% | -2.81% | -0.236 | 0.605 | 0.510 | -2.81% |
| MID_CAP | IJH | diversified_us_equity | -1.90% | -0.96% | -3.67% | 11.40% | -6.95% | 0.126 | 0.784 | 0.834 | -7.18% |
| SMALL_CAP | IWM | diversified_us_equity | -1.46% | -0.96% | -3.08% | 12.37% | -6.38% | 0.909 | 0.734 | 0.850 | -6.69% |
| SMALL_VALUE | IWN | diversified_us_equity | -1.34% | -0.60% | -1.31% | 10.18% | -4.29% | -0.355 | 0.612 | 0.575 | -4.70% |
| DIVIDEND | SCHD | diversified_us_equity | -0.82% | 0.36% | 0.75% | 11.69% | -3.89% | -0.423 | 0.083 | 0.086 | -3.89% |
| LOW_VOL | SPLV | diversified_us_equity | -1.18% | -0.39% | -0.76% | 8.31% | -4.07% | -0.317 | -0.129 | -0.129 | -6.30% |
| MOMENTUM | MTUM | diversified_us_equity | -2.15% | -1.77% | -2.64% | 21.11% | -7.93% | -1.100 | 0.606 | 1.743 | -12.97% |
| TECHNOLOGY | XLK | technology_and_growth | -1.99% | -1.00% | 0.04% | 21.15% | -5.40% | -0.563 | 0.773 | 1.931 | -7.09% |
| COMMUNICATIONS | XLC | technology_and_growth | 0.36% | 3.05% | 1.34% | 16.05% | -2.25% | -0.521 | 0.376 | 0.656 | -5.35% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | -2.46% | -0.93% | -2.35% | 17.08% | -7.09% | 0.106 | 0.649 | 1.150 | -11.16% |
| CONSUMER_STAPLES | XLP | consumer_defensive | -0.06% | 1.43% | -0.60% | 14.49% | -5.03% | 0.146 | -0.137 | -0.198 | -6.25% |
| HEALTHCARE | XLV | healthcare_and_biotech | 1.46% | 1.81% | 1.05% | 20.58% | -5.87% | -0.586 | -0.136 | -0.224 | -4.50% |
| FINANCIALS | XLF | financials | -2.31% | -0.89% | 0.43% | 13.57% | -4.49% | 0.580 | 0.407 | 0.450 | -4.49% |
| INDUSTRIALS | XLI | industrials_and_defense | -2.12% | -0.70% | -6.47% | 13.38% | -9.45% | 0.498 | 0.626 | 0.872 | -9.54% |
| ENERGY | XLE | energy | -1.70% | -0.86% | 5.69% | 19.69% | -2.88% | 1.576 | -0.309 | -0.569 | -2.88% |
| MATERIALS | XLB | materials_and_mining | -1.16% | -0.91% | -0.30% | 15.21% | -6.17% | -0.514 | 0.318 | 0.468 | -6.17% |
| UTILITIES | XLU | rate_sensitive_defensive | -2.52% | -2.68% | -1.48% | 14.11% | -6.47% | 0.267 | -0.050 | -0.062 | -12.28% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | -1.40% | -0.29% | -1.84% | 10.24% | -5.62% | -0.112 | -0.033 | -0.041 | -6.96% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | -0.31% | -0.17% | 0.67% | 4.66% | -2.62% | 0.506 | 0.397 | 0.160 | -5.23% |
| LONG_TREASURY | TLT | rates_and_duration | 0.01% | 0.06% | 2.18% | 9.86% | -2.93% | 1.236 | 0.307 | 0.246 | -8.55% |
| TIPS | TIP | rates_and_duration | -0.43% | -0.22% | 1.36% | 4.11% | -2.09% | 0.409 | 0.250 | 0.078 | -2.65% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | 0.12% | 0.28% | 1.38% | 5.62% | -2.00% | 0.701 | 0.458 | 0.204 | -3.92% |
| HIGH_YIELD_CREDIT | HYG | credit | -0.23% | 0.39% | 1.08% | 2.77% | -1.39% | 1.748 | 0.754 | 0.180 | -1.34% |
| AGGREGATE_BONDS | AGG | rates_and_duration | -0.18% | 0.20% | 1.09% | 4.13% | -1.90% | 1.209 | 0.431 | 0.145 | -3.27% |
| DEVELOPED_EX_US | VEA | international_equity | -1.97% | -1.05% | 0.15% | 13.35% | -3.43% | -0.439 | 0.759 | 1.038 | -3.43% |
| EMERGING_MARKETS | VWO | international_equity | -1.94% | -1.68% | 2.12% | 11.68% | -3.68% | -0.222 | 0.778 | 1.052 | -3.68% |
| EUROPE | VGK | international_equity | -1.54% | -0.66% | -0.72% | 9.77% | -4.89% | -0.742 | 0.724 | 0.748 | -4.89% |
| JAPAN | EWJ | international_equity | -1.57% | 1.11% | 0.14% | 17.22% | -3.97% | -0.586 | 0.707 | 1.308 | -1.57% |
| CHINA | MCHI | international_equity | -1.23% | -0.84% | -1.79% | 12.41% | -6.02% | -0.811 | 0.356 | 0.509 | -20.43% |
| INDIA | INDA | international_equity | -2.29% | -1.39% | -0.51% | 13.12% | -5.51% | 0.166 | 0.515 | 0.562 | -14.16% |
| GOLD | IAU | precious_metals | -1.70% | -1.77% | 0.82% | 27.18% | -8.48% | 0.615 | 0.331 | 0.693 | -20.92% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | 0.05% | 2.12% | 8.96% | 18.60% | -2.57% | -0.110 | -0.313 | -0.589 | -1.49% |
| SEMICONDUCTORS | SMH | technology_and_growth | -4.04% | -3.91% | -2.00% | 33.98% | -8.85% | -0.569 | 0.658 | 2.582 | -18.44% |
| SOFTWARE | IGV | technology_and_growth | 3.39% | 4.17% | 1.17% | 40.73% | -8.27% | -0.879 | 0.438 | 1.279 | -10.88% |
| BROAD_AI_TECH | AIQ | technology_and_growth | -1.52% | -0.62% | 1.50% | 19.45% | -2.66% | -0.565 | 0.786 | 2.095 | -10.16% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | -1.62% | -1.07% | -5.14% | 23.14% | -8.83% | -0.503 | 0.800 | 2.146 | -16.99% |
| CYBERSECURITY | CIBR | technology_and_growth | 6.25% | 7.26% | -2.06% | 42.98% | -7.19% | 0.644 | 0.433 | 1.220 | -1.86% |
| SOLAR | TAN | clean_energy | -5.37% | -5.44% | -4.92% | 25.15% | -12.37% | 0.057 | 0.717 | 2.211 | -39.65% |
| METALS_MINING | XME | materials_and_mining | -4.28% | -7.65% | 2.25% | 36.97% | -11.57% | -0.507 | 0.530 | 1.649 | -18.06% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | -1.21% | -0.00% | -1.46% | 9.87% | -4.43% | -0.290 | 0.646 | 0.582 | -4.71% |
| BIOTECH | XBI | healthcare_and_biotech | -1.29% | -2.17% | 1.24% | 33.05% | -9.15% | 0.022 | 0.196 | 0.489 | -9.07% |
| REGIONAL_BANKS | KRE | financials | -1.57% | 0.13% | -3.76% | 16.00% | -6.16% | 0.628 | 0.288 | 0.422 | -6.66% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | -1.59% | -0.69% | -11.31% | 18.39% | -15.03% | 1.284 | 0.375 | 0.683 | -14.89% |
| CANADA | EWC | international_equity | -1.19% | -0.76% | -0.58% | 13.56% | -4.44% | -0.131 | 0.536 | 0.523 | -4.44% |
| UNITED_KINGDOM | EWU | international_equity | -1.00% | 0.32% | 0.64% | 9.72% | -3.91% | -0.398 | 0.373 | 0.373 | -3.91% |
| AUSTRALIA | EWA | international_equity | -2.66% | -2.72% | 1.57% | 15.32% | -6.38% | 2.390 | 0.612 | 0.793 | -6.38% |
| SOUTH_KOREA | EWY | international_equity | -6.98% | -6.89% | 4.40% | 51.14% | -8.13% | -0.678 | 0.568 | 3.245 | -19.92% |
| TAIWAN | EWT | international_equity | -2.26% | -1.91% | 5.00% | 25.54% | -4.91% | -1.004 | 0.699 | 2.221 | -3.37% |
| BRAZIL | EWZ | international_equity | -1.86% | -0.45% | 13.40% | 23.32% | -2.93% | -0.131 | 0.232 | 0.434 | -9.33% |
| MEXICO | EWW | international_equity | -3.30% | -3.62% | 3.45% | 15.83% | -6.37% | -0.390 | 0.539 | 0.763 | -8.95% |
| SOUTH_AFRICA | EZA | international_equity | -3.64% | -4.18% | 5.90% | 29.19% | -6.84% | -0.327 | 0.578 | 1.329 | -15.47% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | -0.17% | 0.02% | 0.80% | 4.73% | -2.36% | 0.898 | 0.462 | 0.184 | -3.49% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | -0.34% | 0.46% | -0.37% | 4.09% | -2.53% | 5.087 | 0.487 | 0.146 | -3.89% |
| EMERGING_MARKET_BONDS | EMB | credit | -0.30% | -0.08% | 1.21% | 4.79% | -2.08% | 1.285 | 0.665 | 0.279 | -2.64% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | -0.04% | 0.54% | 0.70% | 3.94% | -1.92% | 0.269 | 0.477 | 0.147 | -2.95% |
| SILVER | SLV | precious_metals | -1.84% | -4.95% | 3.26% | 41.23% | -9.45% | -0.009 | 0.421 | 1.483 | -45.98% |
| COPPER | CPER | non_energy_commodities | -1.51% | -4.90% | 3.62% | 26.93% | -6.80% | 0.736 | 0.485 | 1.003 | -5.99% |
| AGRICULTURE | DBA | non_energy_commodities | -0.38% | 0.47% | 4.39% | 11.66% | -2.27% | 0.570 | 0.021 | 0.024 | -2.27% |
| OIL | USO | energy | 0.82% | 5.23% | 16.43% | 41.50% | -6.31% | 0.633 | -0.401 | -1.761 | -3.52% |
| US_DOLLAR | UUP | currencies | 1.18% | 2.60% | 0.90% | 5.69% | -0.92% | -0.027 | -0.354 | -0.164 | -0.70% |
| EURO | FXE | currencies | -1.08% | -0.28% | 1.84% | 4.96% | -1.73% | 1.047 | 0.340 | 0.143 | -4.21% |
| YEN | FXY | currencies | -1.61% | -0.55% | 5.10% | 11.27% | -1.64% | -0.232 | 0.320 | 0.269 | -6.53% |
| BITCOIN_ETF | IBIT | crypto_assets | -1.67% | -1.73% | 22.94% | 48.28% | -7.14% | 0.128 | 0.289 | 0.929 | -39.63% |
| ETHEREUM_ETF | ETHA | crypto_assets | -5.27% | -1.22% | 30.36% | 61.02% | -5.32% | 1.528 | 0.273 | 1.143 | -49.29% |
