# Full-Universe Horizon-Specific Decision Context

Profile: weekly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: tiingo_eod_adjusted_price_and_volume; yahoo_chart_adjusted_close_and_reported_volume
- As-of date requested: 2026-10-22
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | -1.01% |
| spy_return_21s | -0.50% |
| rsp_return_5s | 1.50% |
| rsp_return_21s | 3.27% |
| hyg_return_5s | -0.04% |
| hyg_return_21s | -0.84% |
| tlt_return_5s | 2.21% |
| tlt_return_21s | 2.00% |
| uup_return_5s | -0.34% |
| uup_return_21s | 0.87% |
| uso_return_5s | 3.31% |
| uso_return_21s | 9.19% |
| iau_return_5s | -3.58% |
| iau_return_21s | -6.04% |
| rsp_minus_spy_5s | 2.51% |
| rsp_minus_spy_21s | 3.77% |
| positive_asset_share_5s | 50.72% |
| positive_asset_share_21s | 46.38% |
| active_return_dispersion_5s | 2.48% |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_3s | active_return_5s | prior_16s_active_return | volatility_21s | max_drawdown_21s | volume_zscore_5v60 | corr_spy_63s | beta_spy_63s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | 1.01% | -0.52% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.03% | 1.08% | -0.29% | 0.26% | -0.01% | 0.205 | 0.217 | 0.004 | 0.00% |
| SP500 | SPY | diversified_us_equity | -0.33% | 0.00% | 0.00% | 9.59% | -2.03% | 0.167 | 1.000 | 1.000 | -1.94% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | -0.17% | 0.08% | -0.21% | 9.84% | -2.21% | -0.324 | 0.996 | 1.014 | -2.20% |
| NASDAQ100 | QQQ | technology_and_growth | -1.93% | -2.22% | -2.30% | 18.09% | -7.27% | 1.042 | 0.914 | 1.574 | -7.27% |
| LARGE_GROWTH | IWF | technology_and_growth | -2.06% | -2.33% | -1.44% | 17.71% | -7.04% | 1.197 | 0.936 | 1.538 | -7.04% |
| LARGE_VALUE | IWD | diversified_us_equity | 1.42% | 2.16% | 1.35% | 7.06% | -1.59% | 0.792 | 0.702 | 0.545 | 0.00% |
| MID_CAP | IJH | diversified_us_equity | 0.58% | 0.70% | -0.52% | 12.56% | -2.34% | 0.568 | 0.795 | 0.888 | -7.18% |
| SMALL_CAP | IWM | diversified_us_equity | 1.99% | 1.59% | -2.94% | 14.26% | -4.57% | 0.395 | 0.761 | 0.977 | -9.08% |
| SMALL_VALUE | IWN | diversified_us_equity | 2.62% | 2.33% | -1.82% | 12.72% | -2.71% | 0.442 | 0.595 | 0.624 | -5.83% |
| DIVIDEND | SCHD | diversified_us_equity | 3.39% | 4.83% | 1.95% | 12.86% | -2.25% | -0.081 | 0.054 | 0.057 | 0.00% |
| LOW_VOL | SPLV | diversified_us_equity | 3.53% | 4.56% | 2.79% | 12.17% | -1.18% | 0.399 | -0.043 | -0.040 | -1.74% |
| MOMENTUM | MTUM | diversified_us_equity | -2.41% | -3.29% | -5.38% | 21.57% | -11.06% | -0.164 | 0.692 | 1.630 | -16.24% |
| TECHNOLOGY | XLK | technology_and_growth | -1.95% | -2.61% | -3.67% | 22.89% | -9.73% | 1.485 | 0.819 | 1.946 | -9.73% |
| COMMUNICATIONS | XLC | technology_and_growth | -2.43% | -3.45% | -0.62% | 16.51% | -5.76% | 0.332 | 0.365 | 0.654 | -9.74% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | 0.48% | 2.43% | 1.98% | 13.38% | -1.66% | 1.154 | 0.632 | 0.962 | -7.07% |
| CONSUMER_STAPLES | XLP | consumer_defensive | 3.19% | 4.83% | 4.64% | 18.07% | -2.55% | 2.118 | -0.201 | -0.292 | 0.00% |
| HEALTHCARE | XLV | healthcare_and_biotech | 3.22% | 3.33% | 4.45% | 18.22% | -2.97% | -0.095 | 0.018 | 0.028 | 0.00% |
| FINANCIALS | XLF | financials | 2.89% | 3.51% | 0.82% | 12.01% | -2.63% | -0.248 | 0.451 | 0.522 | -2.92% |
| INDUSTRIALS | XLI | industrials_and_defense | 0.03% | 0.32% | -1.82% | 13.63% | -2.86% | 0.908 | 0.695 | 0.925 | -10.37% |
| ENERGY | XLE | energy | -0.34% | 2.53% | 6.20% | 19.04% | -1.76% | 0.686 | -0.291 | -0.570 | -0.98% |
| MATERIALS | XLB | materials_and_mining | 1.45% | 3.25% | 0.04% | 12.74% | -3.46% | -0.427 | 0.322 | 0.456 | -3.25% |
| UTILITIES | XLU | rate_sensitive_defensive | 3.65% | 3.94% | 4.26% | 17.16% | -2.01% | 0.306 | 0.085 | 0.121 | -8.31% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | 2.04% | 2.28% | -0.16% | 14.89% | -3.04% | 1.161 | 0.234 | 0.273 | -6.82% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | 1.24% | 1.96% | 0.00% | 6.09% | -1.07% | 0.316 | 0.302 | 0.157 | -4.42% |
| LONG_TREASURY | TLT | rates_and_duration | 2.87% | 3.23% | -0.73% | 12.04% | -3.78% | 0.096 | 0.276 | 0.283 | -7.21% |
| TIPS | TIP | rates_and_duration | 1.02% | 2.00% | -0.06% | 4.51% | -0.79% | -0.294 | 0.104 | 0.040 | -1.78% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | 1.36% | 1.77% | -0.47% | 6.69% | -1.65% | 0.407 | 0.387 | 0.226 | -3.67% |
| HIGH_YIELD_CREDIT | HYG | credit | 0.35% | 0.98% | -1.32% | 3.63% | -1.21% | 0.105 | 0.668 | 0.211 | -2.57% |
| AGGREGATE_BONDS | AGG | rates_and_duration | 1.06% | 1.76% | -0.16% | 5.02% | -0.99% | 0.098 | 0.340 | 0.149 | -2.61% |
| DEVELOPED_EX_US | VEA | international_equity | -0.14% | 0.44% | -2.98% | 11.54% | -3.59% | -0.705 | 0.764 | 0.988 | -5.91% |
| EMERGING_MARKETS | VWO | international_equity | -2.03% | -2.29% | -2.73% | 14.74% | -6.22% | 0.273 | 0.804 | 1.052 | -7.30% |
| EUROPE | VGK | international_equity | 0.43% | 0.54% | -1.43% | 12.73% | -3.61% | -0.280 | 0.646 | 0.703 | -6.62% |
| JAPAN | EWJ | international_equity | -0.41% | 0.14% | -2.19% | 15.23% | -4.75% | 0.243 | 0.689 | 1.153 | -4.75% |
| CHINA | MCHI | international_equity | -3.64% | -4.15% | -3.30% | 17.20% | -7.81% | -0.003 | 0.359 | 0.522 | -23.85% |
| INDIA | INDA | international_equity | -0.08% | -0.22% | -0.73% | 15.81% | -5.18% | 0.189 | 0.511 | 0.627 | -14.34% |
| GOLD | IAU | precious_metals | -2.81% | -2.57% | -3.06% | 21.52% | -6.20% | -0.089 | 0.363 | 0.787 | -25.51% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | -0.25% | 1.97% | 0.60% | 14.48% | -3.59% | -0.544 | -0.476 | -0.864 | -0.45% |
| SEMICONDUCTORS | SMH | technology_and_growth | -4.58% | -5.34% | -7.60% | 33.07% | -17.44% | 0.565 | 0.711 | 2.459 | -21.76% |
| SOFTWARE | IGV | technology_and_growth | 2.58% | 0.21% | 0.87% | 28.00% | -7.39% | -0.335 | 0.554 | 1.706 | -7.12% |
| BROAD_AI_TECH | AIQ | technology_and_growth | -1.41% | -2.14% | -3.40% | 23.27% | -7.50% | 0.334 | 0.888 | 2.055 | -11.50% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | -1.60% | -2.43% | -7.77% | 27.20% | -12.19% | 0.121 | 0.864 | 2.315 | -22.34% |
| CYBERSECURITY | CIBR | technology_and_growth | 2.89% | 0.32% | -0.98% | 30.69% | -10.16% | 1.834 | 0.512 | 1.596 | -6.54% |
| SOLAR | TAN | clean_energy | 0.10% | -2.26% | -5.62% | 31.04% | -8.30% | 0.145 | 0.710 | 2.188 | -44.07% |
| METALS_MINING | XME | materials_and_mining | -4.72% | -3.67% | -8.04% | 28.99% | -11.85% | -0.071 | 0.628 | 2.063 | -27.18% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | 2.26% | 2.51% | 1.23% | 9.89% | -1.56% | 0.668 | 0.629 | 0.585 | -1.68% |
| BIOTECH | XBI | healthcare_and_biotech | 2.56% | 2.26% | -4.01% | 31.21% | -8.47% | 0.665 | 0.383 | 1.066 | -10.56% |
| REGIONAL_BANKS | KRE | financials | 4.55% | 4.83% | -1.41% | 18.45% | -4.21% | 0.415 | 0.242 | 0.350 | -6.55% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | -1.58% | -0.16% | -3.79% | 14.78% | -4.82% | 1.594 | 0.503 | 0.855 | -19.15% |
| CANADA | EWC | international_equity | 1.09% | 2.03% | 0.62% | 14.58% | -2.87% | -0.121 | 0.589 | 0.710 | -2.71% |
| UNITED_KINGDOM | EWU | international_equity | 1.06% | 1.18% | 0.90% | 12.35% | -3.02% | -0.646 | 0.344 | 0.346 | -3.14% |
| AUSTRALIA | EWA | international_equity | 0.49% | 1.57% | 1.07% | 11.47% | -1.79% | -0.148 | 0.661 | 0.970 | -4.80% |
| SOUTH_KOREA | EWY | international_equity | -4.80% | -3.57% | -16.37% | 42.42% | -22.32% | 0.034 | 0.634 | 3.148 | -32.00% |
| TAIWAN | EWT | international_equity | -3.05% | -3.70% | -3.51% | 27.72% | -11.87% | -0.131 | 0.745 | 2.126 | -11.87% |
| BRAZIL | EWZ | international_equity | -0.19% | 1.66% | 10.75% | 49.33% | -4.50% | 0.894 | 0.281 | 0.861 | -3.88% |
| MEXICO | EWW | international_equity | -0.54% | 2.46% | 0.11% | 18.45% | -4.97% | -0.051 | 0.507 | 0.779 | -6.37% |
| SOUTH_AFRICA | EZA | international_equity | -1.16% | -0.75% | -2.67% | 23.29% | -6.30% | 0.991 | 0.516 | 1.254 | -20.03% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | 1.29% | 1.89% | -0.04% | 6.72% | -1.19% | 0.060 | 0.354 | 0.194 | -2.94% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | 0.88% | 1.76% | 0.19% | 6.98% | -1.72% | 0.467 | 0.265 | 0.126 | -3.23% |
| EMERGING_MARKET_BONDS | EMB | credit | 0.83% | 1.05% | -0.94% | 6.26% | -2.24% | 0.091 | 0.578 | 0.315 | -3.43% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | 0.40% | 1.04% | 0.30% | 2.42% | -0.38% | -0.023 | 0.506 | 0.170 | -2.20% |
| SILVER | SLV | precious_metals | -4.27% | -3.95% | -11.25% | 39.91% | -15.17% | -0.110 | 0.494 | 1.768 | -53.28% |
| COPPER | CPER | non_energy_commodities | -2.78% | -1.47% | -3.37% | 17.52% | -5.36% | -0.278 | 0.469 | 0.946 | -7.14% |
| AGRICULTURE | DBA | non_energy_commodities | -0.99% | -0.26% | -1.46% | 9.15% | -3.22% | -0.014 | 0.157 | 0.178 | -5.32% |
| OIL | USO | energy | 1.06% | 4.32% | 5.18% | 32.79% | -6.36% | 0.044 | -0.547 | -2.336 | 0.00% |
| US_DOLLAR | UUP | currencies | -0.34% | 0.67% | 0.70% | 5.04% | -0.79% | -0.388 | -0.231 | -0.111 | -0.79% |
| EURO | FXE | currencies | 0.05% | 1.06% | -1.97% | 5.10% | -1.98% | -0.610 | 0.212 | 0.094 | -6.24% |
| YEN | FXY | currencies | 1.12% | 1.89% | -0.43% | 5.91% | -0.89% | -0.596 | 0.301 | 0.273 | -3.42% |
| BITCOIN_ETF | IBIT | crypto_assets | -0.52% | -0.12% | -3.21% | 23.29% | -5.15% | -0.195 | 0.377 | 1.288 | -29.44% |
| ETHEREUM_ETF | ETHA | crypto_assets | -0.43% | -1.75% | -9.13% | 33.16% | -12.09% | -0.657 | 0.295 | 1.271 | -43.43% |
