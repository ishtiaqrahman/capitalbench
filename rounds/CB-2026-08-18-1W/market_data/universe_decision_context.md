# Full-Universe Horizon-Specific Decision Context

Profile: weekly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: yahoo_chart_adjusted_close_and_reported_volume
- As-of date requested: 2026-08-17
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | -0.05% |
| spy_return_21s | 3.95% |
| rsp_return_5s | 0.26% |
| rsp_return_21s | 3.48% |
| hyg_return_5s | 0.16% |
| hyg_return_21s | 0.23% |
| tlt_return_5s | -0.87% |
| tlt_return_21s | -3.36% |
| uup_return_5s | -0.14% |
| uup_return_21s | -0.81% |
| uso_return_5s | 3.47% |
| uso_return_21s | 5.11% |
| iau_return_5s | 0.73% |
| iau_return_21s | 10.08% |
| rsp_minus_spy_5s | 0.31% |
| rsp_minus_spy_21s | -0.48% |
| positive_asset_share_5s | 59.42% |
| positive_asset_share_21s | 73.91% |
| active_return_dispersion_5s | 2.37% |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_3s | active_return_5s | prior_16s_active_return | volatility_21s | max_drawdown_21s | volume_zscore_5v60 | corr_spy_63s | beta_spy_63s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | 0.05% | -4.00% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.04% | 0.12% | -3.78% | 0.17% | 0.00% | -0.872 | -0.139 | -0.002 | 0.00% |
| SP500 | SPY | diversified_us_equity | 0.02% | 0.00% | 0.00% | 13.24% | -2.52% | -1.360 | 1.000 | 1.000 | -0.67% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | 0.08% | 0.18% | -0.02% | 13.21% | -2.44% | -0.480 | 0.993 | 0.986 | -0.56% |
| NASDAQ100 | QQQ | technology_and_growth | 0.85% | 1.30% | -0.33% | 23.25% | -6.66% | -1.145 | 0.922 | 1.725 | -2.08% |
| LARGE_GROWTH | IWF | technology_and_growth | 0.53% | 0.78% | 0.01% | 21.17% | -6.00% | -0.866 | 0.908 | 1.380 | -2.78% |
| LARGE_VALUE | IWD | diversified_us_equity | -0.45% | -0.61% | 0.46% | 10.13% | -1.31% | -0.466 | 0.729 | 0.609 | -0.80% |
| MID_CAP | IJH | diversified_us_equity | 0.54% | 1.26% | -1.35% | 12.58% | -1.71% | -0.682 | 0.797 | 0.805 | -0.24% |
| SMALL_CAP | IWM | diversified_us_equity | 0.45% | 1.41% | -1.98% | 15.01% | -2.69% | -1.554 | 0.777 | 0.984 | -0.34% |
| SMALL_VALUE | IWN | diversified_us_equity | 0.23% | 1.01% | -3.12% | 11.23% | -1.38% | -1.384 | 0.652 | 0.667 | -0.43% |
| DIVIDEND | SCHD | diversified_us_equity | 0.09% | 0.34% | -0.11% | 10.44% | -1.42% | -0.168 | 0.089 | 0.077 | -0.67% |
| LOW_VOL | SPLV | diversified_us_equity | -0.11% | 0.10% | -4.95% | 9.44% | -2.98% | -0.887 | -0.286 | -0.274 | -2.86% |
| MOMENTUM | MTUM | diversified_us_equity | 2.33% | 4.85% | -2.27% | 34.89% | -9.98% | -0.773 | 0.711 | 1.982 | -6.71% |
| TECHNOLOGY | XLK | technology_and_growth | 0.77% | 2.19% | 2.11% | 32.39% | -7.86% | -1.469 | 0.839 | 2.141 | -3.87% |
| COMMUNICATIONS | XLC | technology_and_growth | 0.50% | -0.86% | -5.37% | 27.86% | -7.06% | -1.021 | 0.417 | 0.621 | -7.18% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | -0.97% | -2.39% | -0.34% | 24.48% | -5.79% | -1.493 | 0.681 | 1.088 | -5.86% |
| CONSUMER_STAPLES | XLP | consumer_defensive | -0.47% | -0.27% | -4.28% | 15.93% | -3.07% | -0.983 | -0.322 | -0.405 | -4.74% |
| HEALTHCARE | XLV | healthcare_and_biotech | -0.83% | -0.78% | 0.56% | 15.13% | -3.09% | -1.395 | -0.190 | -0.250 | -0.83% |
| FINANCIALS | XLF | financials | -0.59% | -0.35% | -1.25% | 10.94% | -1.60% | -1.004 | 0.305 | 0.297 | -1.17% |
| INDUSTRIALS | XLI | industrials_and_defense | 0.24% | 0.98% | -1.70% | 18.80% | -3.57% | -1.719 | 0.658 | 0.907 | -0.10% |
| ENERGY | XLE | energy | 2.54% | 4.03% | 0.33% | 24.23% | -3.87% | -1.266 | -0.338 | -0.594 | 0.00% |
| MATERIALS | XLB | materials_and_mining | -0.65% | -1.72% | 1.31% | 17.97% | -2.54% | -0.734 | 0.450 | 0.646 | -1.88% |
| UTILITIES | XLU | rate_sensitive_defensive | 0.78% | 2.48% | -8.52% | 13.94% | -6.83% | -0.647 | -0.123 | -0.140 | -6.20% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | 0.76% | 1.02% | -6.25% | 13.80% | -4.19% | 0.446 | -0.158 | -0.185 | -2.56% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | -0.13% | 0.13% | -4.69% | 4.76% | -1.05% | -0.305 | 0.529 | 0.194 | -3.38% |
| LONG_TREASURY | TLT | rates_and_duration | -0.93% | -0.82% | -6.52% | 9.75% | -3.36% | -0.068 | 0.392 | 0.259 | -8.38% |
| TIPS | TIP | rates_and_duration | -0.14% | -0.04% | -5.07% | 4.10% | -1.39% | -0.479 | 0.401 | 0.112 | -2.10% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | -0.40% | -0.20% | -5.06% | 5.37% | -1.30% | -0.376 | 0.575 | 0.223 | -3.18% |
| HIGH_YIELD_CREDIT | HYG | credit | -0.00% | 0.21% | -3.93% | 3.28% | -0.73% | -1.022 | 0.807 | 0.205 | -0.23% |
| AGGREGATE_BONDS | AGG | rates_and_duration | -0.18% | 0.06% | -4.63% | 3.87% | -0.88% | 0.107 | 0.543 | 0.157 | -2.15% |
| DEVELOPED_EX_US | VEA | international_equity | 0.53% | 1.69% | 0.02% | 15.94% | -2.18% | -0.674 | 0.812 | 1.127 | 0.00% |
| EMERGING_MARKETS | VWO | international_equity | -0.03% | 0.15% | 0.30% | 14.72% | -3.30% | -0.547 | 0.851 | 1.196 | -1.39% |
| EUROPE | VGK | international_equity | -0.16% | -0.13% | 0.48% | 11.21% | -1.60% | -1.435 | 0.698 | 0.758 | -0.54% |
| JAPAN | EWJ | international_equity | 0.39% | 2.25% | 2.14% | 22.54% | -3.66% | -1.514 | 0.758 | 1.273 | -0.30% |
| CHINA | MCHI | international_equity | -0.04% | -3.24% | 2.95% | 19.35% | -4.41% | -0.251 | 0.402 | 0.610 | -16.25% |
| INDIA | INDA | international_equity | -0.74% | -1.07% | -1.09% | 12.01% | -2.62% | -1.640 | 0.627 | 0.612 | -10.33% |
| GOLD | IAU | precious_metals | 0.16% | 0.77% | 5.28% | 22.51% | -2.56% | -0.724 | 0.507 | 0.915 | -18.17% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | 1.34% | 2.18% | -0.64% | 26.06% | -6.42% | -0.423 | -0.207 | -0.338 | -3.70% |
| SEMICONDUCTORS | SMH | technology_and_growth | 1.58% | 4.38% | -1.69% | 45.72% | -14.09% | -0.947 | 0.759 | 2.959 | -11.19% |
| SOFTWARE | IGV | technology_and_growth | -1.06% | -2.83% | 9.16% | 35.11% | -6.32% | -0.430 | 0.475 | 1.229 | -13.40% |
| BROAD_AI_TECH | AIQ | technology_and_growth | 0.36% | 0.82% | 4.19% | 32.52% | -8.23% | -1.054 | 0.832 | 2.391 | -8.75% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | 1.19% | 2.06% | 6.12% | 35.57% | -8.78% | -1.238 | 0.863 | 2.382 | -9.28% |
| CYBERSECURITY | CIBR | technology_and_growth | -2.59% | -2.75% | 5.48% | 29.03% | -5.02% | 0.120 | 0.542 | 1.286 | -4.32% |
| SOLAR | TAN | clean_energy | -2.69% | -1.77% | -7.79% | 41.94% | -11.54% | -0.942 | 0.761 | 2.557 | -31.12% |
| METALS_MINING | XME | materials_and_mining | 1.12% | 0.52% | 8.56% | 43.84% | -6.55% | -1.078 | 0.576 | 1.754 | -11.03% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | -0.13% | 0.31% | -0.79% | 10.31% | -1.23% | -1.359 | 0.703 | 0.564 | -0.89% |
| BIOTECH | XBI | healthcare_and_biotech | 0.09% | 1.00% | -1.56% | 24.97% | -4.85% | -0.971 | 0.319 | 0.690 | -2.89% |
| REGIONAL_BANKS | KRE | financials | 0.01% | 1.84% | -4.86% | 12.75% | -2.33% | -1.347 | 0.193 | 0.264 | -0.69% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | -0.17% | 0.07% | 4.84% | 22.17% | -3.56% | -1.587 | 0.455 | 0.805 | -0.80% |
| CANADA | EWC | international_equity | 0.66% | 1.15% | -0.08% | 9.72% | -1.46% | 0.517 | 0.559 | 0.475 | -0.08% |
| UNITED_KINGDOM | EWU | international_equity | -0.43% | -0.63% | -0.70% | 11.43% | -1.17% | -0.544 | 0.393 | 0.398 | -1.07% |
| AUSTRALIA | EWA | international_equity | -1.14% | -1.62% | 0.67% | 16.37% | -2.83% | -0.717 | 0.574 | 0.691 | -2.83% |
| SOUTH_KOREA | EWY | international_equity | 5.25% | 13.52% | -3.64% | 69.98% | -17.05% | -0.729 | 0.678 | 3.903 | -15.56% |
| TAIWAN | EWT | international_equity | 1.53% | 5.55% | 0.98% | 40.96% | -12.07% | -1.361 | 0.781 | 2.463 | -3.34% |
| BRAZIL | EWZ | international_equity | 0.32% | -3.42% | -4.40% | 22.82% | -7.86% | 0.109 | 0.418 | 0.678 | -17.82% |
| MEXICO | EWW | international_equity | -2.03% | -2.58% | -1.89% | 13.92% | -3.37% | -0.295 | 0.561 | 0.761 | -6.42% |
| SOUTH_AFRICA | EZA | international_equity | -0.20% | -2.16% | 7.82% | 28.21% | -4.05% | -0.673 | 0.705 | 1.558 | -14.60% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | -0.15% | 0.19% | -4.80% | 5.56% | -1.18% | -0.306 | 0.534 | 0.199 | -2.28% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | -0.40% | -0.23% | -4.42% | 3.71% | -1.24% | 0.064 | 0.552 | 0.124 | -1.60% |
| EMERGING_MARKET_BONDS | EMB | credit | -0.25% | -0.10% | -4.29% | 5.58% | -1.05% | -1.167 | 0.751 | 0.301 | -1.35% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | -0.36% | -0.25% | -4.04% | 3.63% | -0.71% | -0.648 | 0.513 | 0.140 | -1.80% |
| SILVER | SLV | precious_metals | 0.86% | 0.32% | 12.99% | 34.44% | -4.12% | -0.725 | 0.591 | 1.880 | -43.59% |
| COPPER | CPER | non_energy_commodities | 0.27% | -0.08% | 0.25% | 17.29% | -2.45% | -0.742 | 0.626 | 1.170 | -1.76% |
| AGRICULTURE | DBA | non_energy_commodities | 1.08% | 1.20% | -4.07% | 13.61% | -2.87% | -0.759 | 0.097 | 0.095 | -2.05% |
| OIL | USO | energy | 2.35% | 3.52% | -2.42% | 64.11% | -17.64% | -0.557 | -0.345 | -1.350 | -14.82% |
| US_DOLLAR | UUP | currencies | -0.35% | -0.10% | -4.67% | 5.18% | -1.85% | -1.323 | -0.413 | -0.146 | -1.75% |
| EURO | FXE | currencies | 0.49% | 0.38% | -2.94% | 4.61% | -0.81% | -0.476 | 0.434 | 0.151 | -3.45% |
| YEN | FXY | currencies | 0.02% | -0.11% | -2.04% | 11.86% | -1.68% | -0.047 | 0.243 | 0.134 | -8.42% |
| BITCOIN_ETF | IBIT | crypto_assets | 1.48% | 0.57% | -4.33% | 22.78% | -5.42% | -0.851 | 0.422 | 1.102 | -48.91% |
| ETHEREUM_ETF | ETHA | crypto_assets | 1.69% | 1.89% | -2.35% | 30.45% | -4.35% | -1.052 | 0.519 | 1.976 | -60.64% |
