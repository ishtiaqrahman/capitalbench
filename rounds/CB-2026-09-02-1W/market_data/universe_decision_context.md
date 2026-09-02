# Full-Universe Horizon-Specific Decision Context

Profile: weekly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: yahoo_chart_adjusted_close_and_reported_volume
- As-of date requested: 2026-09-01
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | -0.54% |
| spy_return_21s | 0.54% |
| rsp_return_5s | -1.96% |
| rsp_return_21s | 1.20% |
| hyg_return_5s | -0.21% |
| hyg_return_21s | 0.55% |
| tlt_return_5s | -0.46% |
| tlt_return_21s | 0.32% |
| uup_return_5s | 0.89% |
| uup_return_21s | 0.14% |
| uso_return_5s | 11.77% |
| uso_return_21s | 15.46% |
| iau_return_5s | -7.00% |
| iau_return_21s | 6.80% |
| rsp_minus_spy_5s | -1.42% |
| rsp_minus_spy_21s | 0.66% |
| positive_asset_share_5s | 24.64% |
| positive_asset_share_21s | 63.77% |
| active_return_dispersion_5s | 2.75% |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_3s | active_return_5s | prior_16s_active_return | volatility_21s | max_drawdown_21s | volume_zscore_5v60 | corr_spy_63s | beta_spy_63s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | 0.54% | -1.09% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.04% | 0.59% | -0.87% | 0.16% | 0.00% | 0.108 | -0.134 | -0.002 | 0.00% |
| SP500 | SPY | diversified_us_equity | -1.21% | 0.00% | 0.00% | 9.52% | -2.07% | -1.000 | 1.000 | 1.000 | -2.07% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | -0.81% | 0.04% | 1.32% | 11.46% | -2.38% | -0.630 | 0.992 | 0.990 | -2.38% |
| NASDAQ100 | QQQ | technology_and_growth | -1.87% | 0.11% | 0.43% | 17.67% | -3.52% | -0.871 | 0.920 | 1.717 | -5.06% |
| LARGE_GROWTH | IWF | technology_and_growth | -0.44% | 0.68% | 1.21% | 18.03% | -3.68% | -0.466 | 0.904 | 1.402 | -5.79% |
| LARGE_VALUE | IWD | diversified_us_equity | -0.97% | -0.38% | 1.49% | 8.07% | -1.09% | -0.361 | 0.697 | 0.567 | -1.09% |
| MID_CAP | IJH | diversified_us_equity | -2.64% | -1.56% | 0.15% | 14.15% | -5.17% | 0.253 | 0.779 | 0.799 | -5.17% |
| SMALL_CAP | IWM | diversified_us_equity | -2.80% | -1.94% | 1.24% | 15.70% | -4.76% | -0.940 | 0.785 | 0.974 | -4.76% |
| SMALL_VALUE | IWN | diversified_us_equity | -1.96% | -1.30% | 0.19% | 11.47% | -3.29% | -0.506 | 0.664 | 0.651 | -3.29% |
| DIVIDEND | SCHD | diversified_us_equity | -0.06% | -0.32% | 3.53% | 9.73% | -1.14% | 0.142 | 0.110 | 0.093 | -1.14% |
| LOW_VOL | SPLV | diversified_us_equity | -1.77% | -1.39% | -1.19% | 7.83% | -2.24% | -0.854 | -0.284 | -0.262 | -4.22% |
| MOMENTUM | MTUM | diversified_us_equity | -2.46% | -0.81% | -0.75% | 23.63% | -7.93% | -1.280 | 0.699 | 1.941 | -14.11% |
| TECHNOLOGY | XLK | technology_and_growth | 0.44% | 2.53% | 1.59% | 27.01% | -5.62% | -0.939 | 0.837 | 2.120 | -7.24% |
| COMMUNICATIONS | XLC | technology_and_growth | -1.54% | -0.74% | 2.68% | 17.06% | -2.19% | -1.092 | 0.394 | 0.565 | -7.13% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | -2.19% | -2.60% | 0.82% | 16.57% | -4.40% | -1.252 | 0.686 | 1.070 | -7.61% |
| CONSUMER_STAPLES | XLP | consumer_defensive | -1.18% | -1.98% | 1.73% | 14.11% | -2.82% | -1.075 | -0.289 | -0.361 | -4.09% |
| HEALTHCARE | XLV | healthcare_and_biotech | 0.05% | -1.53% | 6.96% | 18.44% | -2.93% | -1.189 | -0.137 | -0.194 | -2.28% |
| FINANCIALS | XLF | financials | -1.17% | -1.36% | 0.53% | 10.28% | -2.25% | -0.940 | 0.294 | 0.288 | -1.90% |
| INDUSTRIALS | XLI | industrials_and_defense | -4.22% | -2.96% | -1.55% | 15.98% | -7.39% | 0.153 | 0.642 | 0.893 | -7.39% |
| ENERGY | XLE | energy | 3.98% | 4.91% | 4.47% | 23.26% | -2.65% | -0.483 | -0.337 | -0.553 | 0.00% |
| MATERIALS | XLB | materials_and_mining | -2.98% | -2.28% | 5.16% | 16.60% | -2.98% | -0.489 | 0.423 | 0.603 | -2.98% |
| UTILITIES | XLU | rate_sensitive_defensive | -2.18% | -0.99% | -3.64% | 14.98% | -4.80% | 0.132 | -0.112 | -0.126 | -9.63% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | -1.39% | -2.37% | -0.69% | 11.25% | -2.91% | -0.003 | -0.160 | -0.181 | -4.28% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | -0.95% | -0.08% | -0.68% | 5.21% | -1.15% | 0.153 | 0.443 | 0.159 | -3.81% |
| LONG_TREASURY | TLT | rates_and_duration | -1.34% | 0.08% | -0.31% | 10.94% | -1.99% | -0.043 | 0.320 | 0.228 | -7.44% |
| TIPS | TIP | rates_and_duration | -0.65% | 0.13% | -0.71% | 3.79% | -0.77% | -0.219 | 0.377 | 0.100 | -1.34% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | -1.05% | 0.05% | -0.72% | 6.30% | -1.12% | -0.182 | 0.518 | 0.206 | -3.22% |
| HIGH_YIELD_CREDIT | HYG | credit | -0.46% | 0.33% | -0.32% | 2.82% | -0.48% | 0.392 | 0.810 | 0.183 | -0.48% |
| AGGREGATE_BONDS | AGG | rates_and_duration | -0.77% | 0.08% | -0.55% | 4.51% | -0.92% | -0.286 | 0.485 | 0.145 | -2.30% |
| DEVELOPED_EX_US | VEA | international_equity | -1.82% | -0.76% | 2.37% | 12.61% | -2.28% | -0.675 | 0.808 | 1.114 | -2.28% |
| EMERGING_MARKETS | VWO | international_equity | 0.03% | 1.72% | 0.99% | 10.96% | -1.37% | -1.103 | 0.849 | 1.166 | -0.91% |
| EUROPE | VGK | international_equity | -2.14% | -1.50% | 1.14% | 8.72% | -2.65% | -0.288 | 0.740 | 0.773 | -2.65% |
| JAPAN | EWJ | international_equity | -0.22% | 0.94% | 1.56% | 16.66% | -4.27% | -0.908 | 0.752 | 1.295 | -3.30% |
| CHINA | MCHI | international_equity | -1.25% | -0.41% | -2.65% | 13.07% | -4.43% | -1.015 | 0.417 | 0.563 | -17.24% |
| INDIA | INDA | international_equity | -0.34% | 1.01% | -1.99% | 9.64% | -2.34% | -0.095 | 0.577 | 0.558 | -10.33% |
| GOLD | IAU | precious_metals | -5.81% | -6.46% | 13.75% | 29.67% | -7.30% | -0.681 | 0.486 | 0.964 | -19.91% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | 4.79% | 3.68% | 4.09% | 21.39% | -3.76% | -0.117 | -0.189 | -0.305 | 0.00% |
| SEMICONDUCTORS | SMH | technology_and_growth | -1.90% | 0.25% | 0.07% | 35.17% | -8.22% | -1.041 | 0.752 | 2.931 | -18.49% |
| SOFTWARE | IGV | technology_and_growth | -3.75% | 4.79% | 3.46% | 41.26% | -4.17% | -0.251 | 0.515 | 1.283 | -9.84% |
| BROAD_AI_TECH | AIQ | technology_and_growth | -0.02% | 1.76% | 4.70% | 26.15% | -3.59% | -0.456 | 0.837 | 2.340 | -10.09% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | -1.78% | -0.84% | 4.79% | 33.09% | -7.91% | -1.077 | 0.873 | 2.377 | -16.46% |
| CYBERSECURITY | CIBR | technology_and_growth | 2.71% | 3.72% | 0.44% | 41.68% | -9.53% | 0.241 | 0.594 | 1.403 | -5.87% |
| SOLAR | TAN | clean_energy | -3.94% | -2.48% | -3.13% | 36.43% | -12.20% | -0.704 | 0.788 | 2.448 | -36.62% |
| METALS_MINING | XME | materials_and_mining | -3.77% | -1.24% | 16.02% | 42.34% | -5.88% | -0.673 | 0.651 | 1.973 | -12.78% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | -2.04% | -1.42% | 2.13% | 10.75% | -2.33% | -0.987 | 0.685 | 0.563 | -2.33% |
| BIOTECH | XBI | healthcare_and_biotech | -2.96% | 0.07% | 10.59% | 32.99% | -4.16% | -0.468 | 0.313 | 0.734 | -3.63% |
| REGIONAL_BANKS | KRE | financials | -2.63% | -2.32% | -2.80% | 14.08% | -6.81% | -0.690 | 0.180 | 0.243 | -6.81% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | -4.62% | -2.86% | -3.70% | 23.59% | -10.96% | -0.131 | 0.437 | 0.800 | -10.96% |
| CANADA | EWC | international_equity | -2.62% | -1.91% | 3.51% | 11.52% | -3.26% | -0.390 | 0.591 | 0.528 | -3.26% |
| UNITED_KINGDOM | EWU | international_equity | -1.37% | -1.31% | 0.34% | 7.72% | -2.43% | -0.265 | 0.404 | 0.379 | -2.43% |
| AUSTRALIA | EWA | international_equity | -1.56% | -0.72% | 1.37% | 14.32% | -2.83% | 0.394 | 0.590 | 0.725 | -2.46% |
| SOUTH_KOREA | EWY | international_equity | -1.89% | 1.78% | 9.44% | 51.71% | -8.13% | -1.200 | 0.678 | 3.786 | -19.80% |
| TAIWAN | EWT | international_equity | 3.15% | 6.74% | 5.93% | 24.66% | -4.15% | -0.614 | 0.785 | 2.358 | -1.60% |
| BRAZIL | EWZ | international_equity | 2.38% | 4.52% | -5.13% | 20.71% | -8.05% | 1.045 | 0.373 | 0.589 | -11.53% |
| MEXICO | EWW | international_equity | -2.44% | -1.39% | -0.64% | 14.54% | -3.95% | -0.223 | 0.597 | 0.833 | -5.49% |
| SOUTH_AFRICA | EZA | international_equity | -2.99% | -1.97% | 11.03% | 30.31% | -4.10% | -0.298 | 0.690 | 1.543 | -12.91% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | -0.89% | -0.06% | -0.30% | 5.15% | -1.09% | 0.745 | 0.492 | 0.169 | -2.24% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | -0.79% | -0.21% | -1.03% | 3.33% | -1.45% | 0.658 | 0.534 | 0.118 | -2.48% |
| EMERGING_MARKET_BONDS | EMB | credit | -0.85% | 0.17% | -0.45% | 5.46% | -0.92% | 0.210 | 0.721 | 0.286 | -1.56% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | -0.81% | -0.07% | -1.03% | 4.06% | -1.25% | 0.061 | 0.487 | 0.129 | -2.33% |
| SILVER | SLV | precious_metals | -7.73% | -6.52% | 17.71% | 40.39% | -7.73% | 0.122 | 0.561 | 1.840 | -45.15% |
| COPPER | CPER | non_energy_commodities | -2.47% | -1.96% | 0.20% | 19.55% | -4.36% | -0.420 | 0.636 | 1.158 | -4.36% |
| AGRICULTURE | DBA | non_energy_commodities | 3.15% | 4.74% | 1.78% | 11.78% | -1.30% | 1.947 | 0.136 | 0.132 | 0.00% |
| OIL | USO | energy | 8.45% | 12.31% | 2.21% | 45.77% | -6.31% | -0.733 | -0.340 | -1.308 | -7.82% |
| US_DOLLAR | UUP | currencies | 0.68% | 1.43% | -1.83% | 4.76% | -1.13% | -1.089 | -0.402 | -0.151 | -1.36% |
| EURO | FXE | currencies | -0.55% | -0.05% | 0.08% | 4.30% | -0.73% | -0.470 | 0.409 | 0.146 | -3.24% |
| YEN | FXY | currencies | -0.61% | -0.22% | -1.12% | 8.45% | -2.22% | 0.158 | 0.265 | 0.153 | -8.95% |
| BITCOIN_ETF | IBIT | crypto_assets | -3.38% | -1.61% | 22.59% | 40.25% | -3.38% | 0.245 | 0.384 | 1.109 | -38.62% |
| ETHEREUM_ETF | ETHA | crypto_assets | -3.39% | -1.45% | 30.73% | 53.80% | -3.39% | 0.581 | 0.441 | 1.881 | -49.06% |
