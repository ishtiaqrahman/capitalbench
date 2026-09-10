# Full-Universe Horizon-Specific Decision Context

Profile: weekly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: tiingo_eod_adjusted_price_and_volume
- As-of date requested: 2026-09-09
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | 0.08% |
| spy_return_21s | -1.38% |
| rsp_return_5s | -1.36% |
| rsp_return_21s | -2.53% |
| hyg_return_5s | -0.15% |
| hyg_return_21s | -0.08% |
| tlt_return_5s | -0.17% |
| tlt_return_21s | -0.02% |
| uup_return_5s | -0.82% |
| uup_return_21s | -0.57% |
| uso_return_5s | 6.36% |
| uso_return_21s | 19.10% |
| iau_return_5s | 1.65% |
| iau_return_21s | 0.22% |
| rsp_minus_spy_5s | -1.44% |
| rsp_minus_spy_21s | -1.16% |
| positive_asset_share_5s | 53.62% |
| positive_asset_share_21s | 36.23% |
| active_return_dispersion_5s | 2.30% |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_3s | active_return_5s | prior_16s_active_return | volatility_21s | max_drawdown_21s | volume_zscore_5v60 | corr_spy_63s | beta_spy_63s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | -0.08% | 1.46% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.04% | -0.00% | 1.66% | 0.15% | 0.00% | -0.392 | -0.001 | -0.000 | 0.00% |
| SP500 | SPY | diversified_us_equity | -1.39% | 0.00% | 0.00% | 8.24% | -2.07% | -0.865 | 1.000 | 1.000 | -1.99% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | -1.41% | 0.02% | -0.24% | 8.60% | -2.38% | -0.476 | 0.992 | 0.981 | -2.27% |
| NASDAQ100 | QQQ | technology_and_growth | -0.19% | 1.14% | -0.38% | 12.53% | -3.52% | -0.994 | 0.911 | 1.668 | -3.89% |
| LARGE_GROWTH | IWF | technology_and_growth | -0.79% | 0.95% | -0.93% | 13.50% | -3.68% | -0.659 | 0.891 | 1.404 | -4.82% |
| LARGE_VALUE | IWD | diversified_us_equity | -2.05% | -0.82% | 0.54% | 8.47% | -2.05% | -0.391 | 0.669 | 0.561 | -2.05% |
| MID_CAP | IJH | diversified_us_equity | -1.57% | -0.14% | -2.34% | 11.13% | -5.22% | -0.663 | 0.790 | 0.825 | -5.22% |
| SMALL_CAP | IWM | diversified_us_equity | -1.54% | -0.06% | -1.68% | 12.61% | -4.76% | -0.613 | 0.756 | 0.878 | -4.74% |
| SMALL_VALUE | IWN | diversified_us_equity | -1.45% | 0.16% | -0.48% | 10.17% | -3.29% | -0.082 | 0.616 | 0.573 | -3.06% |
| DIVIDEND | SCHD | diversified_us_equity | -2.82% | -2.15% | 3.27% | 10.68% | -3.18% | 0.809 | 0.090 | 0.084 | -3.18% |
| LOW_VOL | SPLV | diversified_us_equity | -1.62% | -0.78% | 0.11% | 8.64% | -2.88% | -0.495 | -0.174 | -0.158 | -4.89% |
| MOMENTUM | MTUM | diversified_us_equity | 3.30% | 4.23% | -2.06% | 20.47% | -7.93% | -1.032 | 0.657 | 1.810 | -10.41% |
| TECHNOLOGY | XLK | technology_and_growth | 1.02% | 2.22% | 0.02% | 20.17% | -5.62% | -0.788 | 0.805 | 1.970 | -5.10% |
| COMMUNICATIONS | XLC | technology_and_growth | -2.25% | -0.13% | 0.61% | 16.59% | -2.25% | -0.743 | 0.394 | 0.605 | -7.16% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | -3.43% | -1.94% | -2.79% | 16.52% | -6.02% | -0.494 | 0.689 | 1.155 | -9.32% |
| CONSUMER_STAPLES | XLP | consumer_defensive | -2.59% | -2.66% | 1.81% | 15.12% | -5.03% | 0.024 | -0.193 | -0.255 | -6.57% |
| HEALTHCARE | XLV | healthcare_and_biotech | -3.86% | -3.05% | 3.37% | 19.98% | -5.18% | -0.652 | -0.089 | -0.134 | -5.18% |
| FINANCIALS | XLF | financials | -2.56% | -0.33% | 0.40% | 12.75% | -2.56% | -0.163 | 0.373 | 0.377 | -2.56% |
| INDUSTRIALS | XLI | industrials_and_defense | -1.59% | -0.63% | -4.97% | 12.72% | -7.89% | 0.267 | 0.678 | 0.986 | -7.89% |
| ENERGY | XLE | energy | 1.07% | 0.75% | 9.08% | 15.12% | -2.65% | -0.548 | -0.462 | -0.789 | 0.00% |
| MATERIALS | XLB | materials_and_mining | -2.34% | -1.39% | -0.63% | 14.88% | -4.25% | 0.459 | 0.413 | 0.612 | -4.25% |
| UTILITIES | XLU | rate_sensitive_defensive | -0.21% | 0.81% | 0.13% | 14.12% | -4.69% | 0.366 | -0.054 | -0.060 | -8.84% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | -1.90% | -1.51% | 0.64% | 11.90% | -4.30% | 0.092 | -0.098 | -0.111 | -5.65% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | -0.42% | -0.30% | 1.10% | 4.34% | -1.37% | -0.282 | 0.415 | 0.152 | -4.02% |
| LONG_TREASURY | TLT | rates_and_duration | -0.41% | -0.25% | 1.61% | 9.89% | -1.71% | -0.465 | 0.318 | 0.237 | -7.59% |
| TIPS | TIP | rates_and_duration | -0.19% | -0.09% | 1.41% | 3.53% | -0.78% | -0.527 | 0.325 | 0.088 | -1.35% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | -0.18% | 0.00% | 1.18% | 5.25% | -1.12% | -0.888 | 0.491 | 0.199 | -3.13% |
| HIGH_YIELD_CREDIT | HYG | credit | -0.29% | -0.23% | 1.52% | 2.49% | -0.63% | -0.427 | 0.782 | 0.176 | -0.63% |
| AGGREGATE_BONDS | AGG | rates_and_duration | -0.28% | -0.17% | 1.32% | 3.83% | -1.01% | -0.071 | 0.448 | 0.137 | -2.39% |
| DEVELOPED_EX_US | VEA | international_equity | -0.84% | 0.90% | 0.92% | 11.71% | -2.28% | -0.127 | 0.776 | 1.049 | -1.31% |
| EMERGING_MARKETS | VWO | international_equity | -0.20% | 0.23% | 2.04% | 9.37% | -1.27% | -0.469 | 0.815 | 1.068 | -0.93% |
| EUROPE | VGK | international_equity | -1.67% | -0.64% | -0.21% | 8.64% | -3.20% | -0.730 | 0.722 | 0.763 | -3.20% |
| JAPAN | EWJ | international_equity | -0.92% | 1.79% | 0.59% | 15.87% | -4.27% | -0.520 | 0.736 | 1.293 | -1.49% |
| CHINA | MCHI | international_equity | -1.89% | -2.05% | -2.97% | 14.40% | -6.31% | -0.539 | 0.372 | 0.485 | -18.87% |
| INDIA | INDA | international_equity | -2.50% | -1.92% | 0.34% | 10.73% | -3.11% | -0.365 | 0.549 | 0.551 | -11.97% |
| GOLD | IAU | precious_metals | -1.68% | 1.57% | 0.05% | 27.02% | -7.30% | -0.464 | 0.437 | 0.903 | -18.59% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | 2.67% | 2.81% | 8.30% | 15.77% | -2.57% | -0.263 | -0.315 | -0.530 | 0.00% |
| SEMICONDUCTORS | SMH | technology_and_growth | 3.93% | 5.25% | -2.79% | 29.68% | -8.22% | -0.757 | 0.711 | 2.706 | -14.15% |
| SOFTWARE | IGV | technology_and_growth | -4.79% | -4.18% | 2.57% | 39.58% | -7.70% | -0.581 | 0.468 | 1.204 | -13.53% |
| BROAD_AI_TECH | AIQ | technology_and_growth | -0.30% | 1.58% | 0.75% | 18.62% | -3.59% | -0.718 | 0.817 | 2.150 | -8.60% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | -0.64% | 1.48% | -4.60% | 22.91% | -7.91% | -0.431 | 0.837 | 2.243 | -15.15% |
| CYBERSECURITY | CIBR | technology_and_growth | -0.88% | -1.87% | -2.92% | 39.19% | -9.53% | -0.346 | 0.522 | 1.276 | -7.55% |
| SOLAR | TAN | clean_energy | 0.04% | 1.80% | -8.19% | 25.12% | -11.08% | -0.705 | 0.727 | 2.189 | -35.43% |
| METALS_MINING | XME | materials_and_mining | 0.68% | 2.87% | -0.05% | 34.07% | -5.88% | -0.895 | 0.570 | 1.655 | -10.21% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | -2.46% | -1.44% | 0.26% | 9.79% | -3.65% | -0.774 | 0.683 | 0.591 | -3.65% |
| BIOTECH | XBI | healthcare_and_biotech | -3.04% | -2.54% | 4.85% | 32.44% | -6.00% | -0.997 | 0.284 | 0.653 | -6.00% |
| REGIONAL_BANKS | KRE | financials | -1.90% | 1.06% | -3.03% | 16.05% | -6.81% | -0.354 | 0.218 | 0.294 | -5.75% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | -2.89% | -2.75% | -8.77% | 19.28% | -13.33% | -0.152 | 0.466 | 0.876 | -13.33% |
| CANADA | EWC | international_equity | -2.37% | 0.56% | -0.01% | 13.07% | -3.26% | 0.703 | 0.556 | 0.494 | -2.63% |
| UNITED_KINGDOM | EWU | international_equity | -1.75% | -0.83% | 0.84% | 8.75% | -3.16% | 0.214 | 0.379 | 0.372 | -3.16% |
| AUSTRALIA | EWA | international_equity | -2.47% | -0.28% | 0.22% | 12.91% | -2.66% | 0.662 | 0.543 | 0.659 | -2.66% |
| SOUTH_KOREA | EWY | international_equity | 5.66% | 8.44% | 9.23% | 45.97% | -8.13% | -0.951 | 0.616 | 3.376 | -12.97% |
| TAIWAN | EWT | international_equity | 1.48% | 1.76% | 8.85% | 20.63% | -4.15% | -0.955 | 0.740 | 2.204 | -0.37% |
| BRAZIL | EWZ | international_equity | -0.16% | 4.02% | 5.38% | 25.68% | -4.23% | 1.661 | 0.293 | 0.507 | -7.90% |
| MEXICO | EWW | international_equity | -0.61% | 1.03% | -0.20% | 14.40% | -3.21% | -0.675 | 0.557 | 0.776 | -4.44% |
| SOUTH_AFRICA | EZA | international_equity | -0.71% | 2.46% | 1.18% | 26.77% | -4.10% | 0.026 | 0.651 | 1.456 | -10.76% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | -0.47% | -0.29% | 1.27% | 4.31% | -1.29% | -0.245 | 0.469 | 0.169 | -2.44% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | -0.50% | -0.90% | 0.29% | 3.19% | -2.25% | 2.826 | 0.499 | 0.121 | -3.27% |
| EMERGING_MARKET_BONDS | EMB | credit | -0.30% | 0.00% | 1.10% | 4.50% | -0.92% | 0.906 | 0.719 | 0.286 | -1.47% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | -0.36% | -0.17% | 0.62% | 3.69% | -1.17% | 0.122 | 0.510 | 0.144 | -2.42% |
| SILVER | SLV | precious_metals | 0.28% | 4.75% | -1.05% | 36.86% | -7.73% | -0.645 | 0.485 | 1.572 | -42.50% |
| COPPER | CPER | non_energy_commodities | 2.86% | 4.99% | -1.31% | 18.72% | -4.15% | 0.370 | 0.547 | 0.978 | 0.00% |
| AGRICULTURE | DBA | non_energy_commodities | -0.31% | -1.74% | 7.46% | 11.94% | -2.17% | 0.822 | 0.039 | 0.039 | -1.66% |
| OIL | USO | energy | 5.55% | 6.28% | 13.43% | 34.11% | -6.31% | -0.436 | -0.419 | -1.692 | -1.95% |
| US_DOLLAR | UUP | currencies | -0.11% | -0.90% | 1.70% | 5.15% | -1.13% | -0.490 | -0.335 | -0.137 | -2.17% |
| EURO | FXE | currencies | 0.04% | 0.29% | 1.93% | 4.40% | -0.76% | -0.263 | 0.312 | 0.115 | -2.88% |
| YEN | FXY | currencies | 1.41% | 4.29% | 0.73% | 10.25% | -1.41% | 0.459 | 0.270 | 0.200 | -4.97% |
| BITCOIN_ETF | IBIT | crypto_assets | -4.44% | 1.13% | 22.24% | 45.57% | -4.44% | 0.107 | 0.353 | 1.037 | -37.87% |
| ETHEREUM_ETF | ETHA | crypto_assets | -2.31% | 1.84% | 30.38% | 56.36% | -4.35% | 0.109 | 0.346 | 1.382 | -48.09% |
