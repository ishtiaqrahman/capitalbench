# Full-Universe Horizon-Specific Decision Context

Profile: weekly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: yahoo_chart_adjusted_close_and_reported_volume
- As-of date requested: 2026-08-19
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | -0.44% |
| spy_return_21s | 2.78% |
| rsp_return_5s | 0.45% |
| rsp_return_21s | 4.08% |
| hyg_return_5s | 0.13% |
| hyg_return_21s | 0.56% |
| tlt_return_5s | 1.11% |
| tlt_return_21s | -0.37% |
| uup_return_5s | -1.13% |
| uup_return_21s | -2.11% |
| uso_return_5s | 2.84% |
| uso_return_21s | 1.60% |
| iau_return_5s | 2.24% |
| iau_return_21s | 10.44% |
| rsp_minus_spy_5s | 0.89% |
| rsp_minus_spy_21s | 1.30% |
| positive_asset_share_5s | 53.62% |
| positive_asset_share_21s | 75.36% |
| active_return_dispersion_5s | 2.58% |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_3s | active_return_5s | prior_16s_active_return | volatility_21s | max_drawdown_21s | volume_zscore_5v60 | corr_spy_63s | beta_spy_63s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | 0.44% | -3.24% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.04% | 0.51% | -2.99% | 0.17% | 0.00% | -0.810 | -0.133 | -0.002 | 0.00% |
| SP500 | SPY | diversified_us_equity | -0.94% | 0.00% | 0.00% | 13.31% | -2.52% | -1.077 | 1.000 | 1.000 | -1.13% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | -1.01% | -0.04% | 0.12% | 13.36% | -2.44% | -0.521 | 0.993 | 0.989 | -1.12% |
| NASDAQ100 | QQQ | technology_and_growth | -2.05% | -0.61% | -1.16% | 23.41% | -6.66% | -0.729 | 0.924 | 1.740 | -3.93% |
| LARGE_GROWTH | IWF | technology_and_growth | -2.09% | -0.96% | -0.58% | 22.22% | -5.90% | -0.927 | 0.896 | 1.357 | -4.65% |
| LARGE_VALUE | IWD | diversified_us_equity | 0.08% | 0.83% | 0.69% | 9.70% | -1.00% | -0.471 | 0.717 | 0.594 | 0.00% |
| MID_CAP | IJH | diversified_us_equity | -2.07% | -0.86% | 0.10% | 13.89% | -2.07% | -0.654 | 0.786 | 0.820 | -2.07% |
| SMALL_CAP | IWM | diversified_us_equity | -1.10% | 0.12% | -1.15% | 14.92% | -2.69% | -1.401 | 0.778 | 0.986 | -1.10% |
| SMALL_VALUE | IWN | diversified_us_equity | -0.80% | 0.30% | -2.45% | 11.06% | -1.61% | -1.469 | 0.663 | 0.693 | -0.80% |
| DIVIDEND | SCHD | diversified_us_equity | 1.65% | 2.87% | 1.15% | 11.37% | -1.42% | 0.236 | 0.086 | 0.076 | 0.00% |
| LOW_VOL | SPLV | diversified_us_equity | -0.50% | 0.66% | -4.51% | 9.34% | -2.98% | -1.069 | -0.256 | -0.243 | -2.55% |
| MOMENTUM | MTUM | diversified_us_equity | -3.57% | -2.37% | 0.50% | 37.54% | -9.83% | -0.464 | 0.668 | 1.900 | -11.40% |
| TECHNOLOGY | XLK | technology_and_growth | -3.35% | -2.32% | 1.23% | 32.81% | -7.86% | -1.206 | 0.840 | 2.163 | -7.24% |
| COMMUNICATIONS | XLC | technology_and_growth | -1.44% | 1.40% | -3.58% | 27.23% | -4.89% | -1.147 | 0.410 | 0.621 | -6.76% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | 0.33% | 1.04% | -1.11% | 29.72% | -5.79% | -1.004 | 0.669 | 1.166 | -4.38% |
| CONSUMER_STAPLES | XLP | consumer_defensive | 0.52% | 2.16% | -2.02% | 16.30% | -3.07% | -0.485 | -0.326 | -0.411 | -2.64% |
| HEALTHCARE | XLV | healthcare_and_biotech | 4.97% | 4.74% | 1.88% | 18.73% | -3.09% | -0.649 | -0.177 | -0.249 | 0.00% |
| FINANCIALS | XLF | financials | -1.17% | -0.32% | -0.01% | 11.17% | -1.60% | -0.351 | 0.286 | 0.271 | -1.34% |
| INDUSTRIALS | XLI | industrials_and_defense | -2.44% | -1.67% | 0.81% | 18.08% | -3.57% | -1.070 | 0.656 | 0.881 | -2.44% |
| ENERGY | XLE | energy | 2.70% | 4.62% | 1.09% | 24.70% | -3.87% | -1.050 | -0.343 | -0.599 | -0.16% |
| MATERIALS | XLB | materials_and_mining | -0.04% | 0.33% | 1.71% | 19.68% | -3.65% | -0.874 | 0.440 | 0.617 | -1.35% |
| UTILITIES | XLU | rate_sensitive_defensive | -0.65% | 0.85% | -5.64% | 13.90% | -6.83% | -0.642 | -0.105 | -0.119 | -6.54% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | -0.62% | 1.57% | -4.81% | 14.13% | -4.19% | 0.527 | -0.142 | -0.165 | -2.22% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | 0.37% | 0.90% | -3.51% | 4.94% | -0.74% | -0.183 | 0.491 | 0.176 | -2.82% |
| LONG_TREASURY | TLT | rates_and_duration | 1.19% | 1.55% | -4.69% | 11.43% | -3.04% | 0.500 | 0.352 | 0.246 | -6.50% |
| TIPS | TIP | rates_and_duration | 0.49% | 1.00% | -4.21% | 4.55% | -1.39% | -0.157 | 0.383 | 0.112 | -1.42% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | 0.42% | 0.87% | -4.52% | 6.38% | -1.73% | 0.323 | 0.564 | 0.235 | -2.81% |
| HIGH_YIELD_CREDIT | HYG | credit | 0.00% | 0.57% | -2.80% | 3.31% | -0.56% | -0.589 | 0.812 | 0.202 | -0.10% |
| AGGREGATE_BONDS | AGG | rates_and_duration | 0.35% | 0.84% | -3.95% | 4.66% | -0.98% | -0.162 | 0.534 | 0.170 | -1.92% |
| DEVELOPED_EX_US | VEA | international_equity | -1.02% | -0.20% | 0.78% | 16.26% | -2.18% | -0.814 | 0.814 | 1.146 | -1.17% |
| EMERGING_MARKETS | VWO | international_equity | -0.12% | -0.17% | -0.60% | 14.77% | -3.30% | -0.794 | 0.851 | 1.201 | -1.96% |
| EUROPE | VGK | international_equity | -0.15% | 0.42% | 0.70% | 11.98% | -1.41% | -0.513 | 0.735 | 0.792 | -0.40% |
| JAPAN | EWJ | international_equity | -3.49% | -2.63% | 2.21% | 23.91% | -3.75% | -0.687 | 0.753 | 1.305 | -3.75% |
| CHINA | MCHI | international_equity | 1.39% | 1.01% | -1.50% | 18.76% | -4.41% | -0.573 | 0.446 | 0.634 | -15.75% |
| INDIA | INDA | international_equity | -0.48% | -0.38% | -1.11% | 12.08% | -2.62% | -1.414 | 0.618 | 0.607 | -10.40% |
| GOLD | IAU | precious_metals | 3.11% | 2.69% | 4.78% | 25.97% | -2.56% | -0.382 | 0.490 | 0.927 | -16.47% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | 2.35% | 2.45% | 0.16% | 26.74% | -6.42% | -0.491 | -0.222 | -0.366 | -3.07% |
| SEMICONDUCTORS | SMH | technology_and_growth | -4.58% | -3.64% | -3.11% | 45.81% | -14.09% | -0.634 | 0.763 | 3.008 | -16.14% |
| SOFTWARE | IGV | technology_and_growth | -1.22% | 0.18% | 9.03% | 34.60% | -5.14% | -0.623 | 0.472 | 1.218 | -12.70% |
| BROAD_AI_TECH | AIQ | technology_and_growth | -1.88% | -0.78% | 5.40% | 34.90% | -8.23% | -0.802 | 0.846 | 2.465 | -10.19% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | -3.36% | -1.82% | 5.90% | 37.10% | -7.26% | -1.262 | 0.852 | 2.379 | -12.38% |
| CYBERSECURITY | CIBR | technology_and_growth | -4.08% | -4.39% | 6.13% | 29.98% | -6.52% | 0.250 | 0.557 | 1.340 | -6.52% |
| SOLAR | TAN | clean_energy | -2.89% | -3.11% | -6.65% | 40.50% | -12.00% | -0.950 | 0.732 | 2.410 | -31.73% |
| METALS_MINING | XME | materials_and_mining | -0.06% | 0.68% | 14.75% | 43.69% | -5.42% | -0.193 | 0.597 | 1.864 | -11.80% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | -0.31% | 0.89% | 0.38% | 10.76% | -1.34% | -1.271 | 0.708 | 0.575 | -0.31% |
| BIOTECH | XBI | healthcare_and_biotech | 7.71% | 6.82% | -0.07% | 29.78% | -4.85% | -0.301 | 0.300 | 0.680 | 0.00% |
| REGIONAL_BANKS | KRE | financials | -3.76% | -2.63% | -1.39% | 15.08% | -3.76% | -0.360 | 0.186 | 0.264 | -3.76% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | -2.79% | -1.73% | 5.74% | 26.39% | -3.56% | -1.340 | 0.450 | 0.857 | -2.79% |
| CANADA | EWC | international_equity | -0.64% | 0.54% | 0.77% | 10.46% | -1.40% | 1.050 | 0.584 | 0.497 | -0.64% |
| UNITED_KINGDOM | EWU | international_equity | 0.64% | 0.86% | -0.25% | 10.50% | -1.23% | -0.672 | 0.376 | 0.391 | -0.23% |
| AUSTRALIA | EWA | international_equity | 1.08% | 0.71% | 0.98% | 17.27% | -2.83% | -0.537 | 0.584 | 0.705 | -1.45% |
| SOUTH_KOREA | EWY | international_equity | -2.95% | -0.37% | -1.52% | 73.91% | -17.05% | -0.201 | 0.683 | 4.018 | -20.42% |
| TAIWAN | EWT | international_equity | -2.21% | -0.95% | 2.33% | 39.29% | -12.07% | -1.381 | 0.782 | 2.481 | -6.12% |
| BRAZIL | EWZ | international_equity | 0.97% | 1.63% | -7.80% | 23.62% | -8.05% | -0.097 | 0.404 | 0.651 | -17.12% |
| MEXICO | EWW | international_equity | 0.17% | -1.28% | -2.42% | 16.84% | -3.95% | 0.067 | 0.602 | 0.827 | -6.14% |
| SOUTH_AFRICA | EZA | international_equity | 4.09% | 3.31% | 5.33% | 29.77% | -3.99% | -0.637 | 0.691 | 1.603 | -11.97% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | 0.40% | 0.85% | -3.84% | 5.85% | -1.13% | 0.684 | 0.528 | 0.201 | -1.74% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | -0.17% | 0.16% | -3.36% | 4.37% | -1.07% | 0.497 | 0.546 | 0.133 | -1.49% |
| EMERGING_MARKET_BONDS | EMB | credit | 0.06% | 0.62% | -3.92% | 5.89% | -1.11% | -0.777 | 0.738 | 0.313 | -1.36% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | 0.04% | 0.28% | -3.53% | 3.49% | -0.83% | -0.330 | 0.519 | 0.152 | -1.86% |
| SILVER | SLV | precious_metals | 2.62% | 2.05% | 8.03% | 38.04% | -4.12% | -0.641 | 0.584 | 1.886 | -43.17% |
| COPPER | CPER | non_energy_commodities | -1.55% | -1.13% | 1.91% | 18.65% | -4.09% | 0.036 | 0.645 | 1.228 | -3.57% |
| AGRICULTURE | DBA | non_energy_commodities | 1.87% | 2.06% | -4.34% | 13.80% | -2.87% | -0.384 | 0.116 | 0.113 | -1.53% |
| OIL | USO | energy | 3.40% | 3.28% | -4.44% | 63.43% | -17.64% | -0.791 | -0.337 | -1.311 | -14.42% |
| US_DOLLAR | UUP | currencies | -0.82% | -0.69% | -4.22% | 5.81% | -2.52% | -1.398 | -0.390 | -0.146 | -2.52% |
| EURO | FXE | currencies | 0.93% | 1.80% | -2.10% | 4.97% | -0.36% | -0.314 | 0.411 | 0.148 | -2.55% |
| YEN | FXY | currencies | 0.76% | 1.31% | -1.36% | 12.21% | -1.74% | -0.060 | 0.258 | 0.147 | -7.64% |
| BITCOIN_ETF | IBIT | crypto_assets | 8.84% | 8.50% | -7.96% | 29.64% | -5.42% | 0.476 | 0.402 | 1.101 | -45.60% |
| ETHEREUM_ETF | ETHA | crypto_assets | 11.99% | 12.59% | -5.78% | 44.66% | -4.35% | 1.003 | 0.491 | 1.978 | -56.60% |
