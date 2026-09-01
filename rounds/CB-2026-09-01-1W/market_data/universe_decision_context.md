# Full-Universe Horizon-Specific Decision Context

Profile: weekly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: yahoo_chart_adjusted_close_and_reported_volume
- As-of date requested: 2026-08-31
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | 0.47% |
| spy_return_21s | 2.68% |
| rsp_return_5s | -1.03% |
| rsp_return_21s | 1.86% |
| hyg_return_5s | 0.25% |
| hyg_return_21s | 0.92% |
| tlt_return_5s | 0.57% |
| tlt_return_21s | 0.06% |
| uup_return_5s | 0.79% |
| uup_return_21s | -0.07% |
| uso_return_5s | 1.13% |
| uso_return_21s | 3.51% |
| iau_return_5s | -3.55% |
| iau_return_21s | 8.29% |
| rsp_minus_spy_5s | -1.50% |
| rsp_minus_spy_21s | -0.82% |
| positive_asset_share_5s | 39.13% |
| positive_asset_share_21s | 71.01% |
| active_return_dispersion_5s | 1.92% |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_3s | active_return_5s | prior_16s_active_return | volatility_21s | max_drawdown_21s | volume_zscore_5v60 | corr_spy_63s | beta_spy_63s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | -0.47% | -2.20% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.03% | -0.41% | -1.98% | 0.16% | 0.00% | -0.382 | -0.138 | -0.002 | 0.00% |
| SP500 | SPY | diversified_us_equity | 0.13% | 0.00% | 0.00% | 10.30% | -1.96% | -1.220 | 1.000 | 1.000 | -1.39% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | 0.00% | -0.49% | 1.07% | 11.08% | -2.01% | -0.656 | 0.992 | 0.988 | -1.60% |
| NASDAQ100 | QQQ | technology_and_growth | 0.76% | 1.01% | 0.46% | 17.91% | -3.52% | -1.043 | 0.919 | 1.718 | -3.83% |
| LARGE_GROWTH | IWF | technology_and_growth | 0.72% | -0.21% | 2.02% | 17.46% | -3.68% | -0.479 | 0.903 | 1.402 | -4.62% |
| LARGE_VALUE | IWD | diversified_us_equity | -0.53% | -0.62% | 0.42% | 7.99% | -1.00% | -0.215 | 0.690 | 0.563 | -0.72% |
| MID_CAP | IJH | diversified_us_equity | -1.04% | -2.32% | -0.32% | 13.73% | -4.22% | 0.141 | 0.775 | 0.791 | -4.22% |
| SMALL_CAP | IWM | diversified_us_equity | -1.77% | -2.48% | 0.32% | 15.26% | -3.66% | -1.253 | 0.778 | 0.962 | -3.66% |
| SMALL_VALUE | IWN | diversified_us_equity | -1.26% | -1.81% | -0.84% | 11.12% | -2.48% | -0.689 | 0.654 | 0.640 | -2.48% |
| DIVIDEND | SCHD | diversified_us_equity | -0.46% | -1.38% | 3.00% | 9.63% | -1.08% | 0.355 | 0.105 | 0.090 | -0.91% |
| LOW_VOL | SPLV | diversified_us_equity | -1.26% | -1.10% | -3.60% | 7.83% | -2.04% | -0.516 | -0.292 | -0.276 | -4.03% |
| MOMENTUM | MTUM | diversified_us_equity | -0.67% | -2.05% | -0.06% | 23.21% | -6.74% | -0.984 | 0.698 | 1.943 | -12.99% |
| TECHNOLOGY | XLK | technology_and_growth | 2.62% | 1.27% | 2.11% | 26.30% | -5.62% | -1.001 | 0.832 | 2.131 | -5.80% |
| COMMUNICATIONS | XLC | technology_and_growth | -1.52% | -0.42% | 2.32% | 17.59% | -2.19% | -1.184 | 0.392 | 0.563 | -6.64% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | -1.15% | -1.68% | 2.81% | 19.14% | -3.32% | -1.396 | 0.660 | 1.043 | -5.99% |
| CONSUMER_STAPLES | XLP | consumer_defensive | -1.78% | -1.64% | -1.59% | 14.16% | -2.82% | -1.055 | -0.289 | -0.367 | -4.40% |
| HEALTHCARE | XLV | healthcare_and_biotech | -1.73% | -2.85% | 5.27% | 18.45% | -2.93% | -1.400 | -0.135 | -0.193 | -2.93% |
| FINANCIALS | XLF | financials | -0.94% | -1.34% | 0.05% | 10.11% | -2.25% | -1.176 | 0.282 | 0.274 | -1.03% |
| INDUSTRIALS | XLI | industrials_and_defense | -1.83% | -3.31% | -1.16% | 15.73% | -6.10% | -0.271 | 0.634 | 0.877 | -6.10% |
| ENERGY | XLE | energy | 2.45% | 0.88% | 3.78% | 23.83% | -3.76% | -0.637 | -0.327 | -0.540 | 0.00% |
| MATERIALS | XLB | materials_and_mining | -1.66% | -2.06% | 1.48% | 18.20% | -2.74% | -0.636 | 0.413 | 0.587 | -1.83% |
| UTILITIES | XLU | rate_sensitive_defensive | -2.49% | -1.73% | -6.43% | 14.64% | -5.44% | -0.341 | -0.108 | -0.131 | -10.34% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | -2.17% | -3.16% | -1.62% | 11.32% | -2.76% | -0.520 | -0.162 | -0.185 | -4.13% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | -0.82% | -0.56% | -2.28% | 5.17% | -0.82% | 0.087 | 0.432 | 0.154 | -3.49% |
| LONG_TREASURY | TLT | rates_and_duration | -1.14% | 0.10% | -2.71% | 11.10% | -1.99% | 0.019 | 0.316 | 0.225 | -7.06% |
| TIPS | TIP | rates_and_duration | -0.76% | -0.76% | -2.04% | 3.81% | -0.76% | -0.416 | 0.381 | 0.102 | -1.33% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | -0.61% | -0.20% | -2.23% | 6.05% | -0.99% | -0.521 | 0.510 | 0.201 | -2.71% |
| HIGH_YIELD_CREDIT | HYG | credit | -0.14% | -0.22% | -1.54% | 2.47% | -0.33% | -0.279 | 0.808 | 0.179 | -0.14% |
| AGGREGATE_BONDS | AGG | rates_and_duration | -0.61% | -0.41% | -2.13% | 4.47% | -0.61% | -0.583 | 0.477 | 0.141 | -1.99% |
| DEVELOPED_EX_US | VEA | international_equity | -1.18% | -1.15% | 1.08% | 12.15% | -1.76% | -0.549 | 0.806 | 1.108 | -1.18% |
| EMERGING_MARKETS | VWO | international_equity | -0.20% | -0.35% | 1.68% | 11.30% | -1.37% | -1.107 | 0.855 | 1.186 | -1.18% |
| EUROPE | VGK | international_equity | -1.64% | -1.61% | -0.30% | 8.06% | -1.64% | -0.692 | 0.730 | 0.760 | -1.64% |
| JAPAN | EWJ | international_equity | 0.26% | 0.27% | -0.17% | 16.86% | -4.27% | -1.087 | 0.750 | 1.295 | -2.63% |
| CHINA | MCHI | international_equity | -0.73% | -2.16% | -1.91% | 13.15% | -4.41% | -1.052 | 0.415 | 0.563 | -16.77% |
| INDIA | INDA | international_equity | -1.06% | -0.35% | -2.32% | 9.63% | -2.34% | -0.340 | 0.560 | 0.552 | -10.11% |
| GOLD | IAU | precious_metals | -4.61% | -4.02% | 10.08% | 28.19% | -4.61% | -0.560 | 0.471 | 0.923 | -17.58% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | 2.64% | -0.47% | 4.37% | 20.43% | -3.76% | -0.211 | -0.168 | -0.269 | -1.37% |
| SEMICONDUCTORS | SMH | technology_and_growth | 0.15% | -1.15% | 1.79% | 34.32% | -7.96% | -0.981 | 0.750 | 2.938 | -16.79% |
| SOFTWARE | IGV | technology_and_growth | 7.41% | 6.88% | 6.12% | 39.61% | -4.17% | -0.419 | 0.497 | 1.236 | -6.61% |
| BROAD_AI_TECH | AIQ | technology_and_growth | 1.93% | 0.90% | 5.88% | 24.82% | -3.59% | -0.473 | 0.829 | 2.351 | -8.33% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | -0.20% | -2.92% | 7.98% | 32.23% | -6.62% | -1.065 | 0.863 | 2.364 | -14.82% |
| CYBERSECURITY | CIBR | technology_and_growth | 8.32% | 5.12% | 3.16% | 39.15% | -9.53% | -0.123 | 0.567 | 1.384 | -2.01% |
| SOLAR | TAN | clean_energy | -2.62% | -4.02% | -3.24% | 36.26% | -10.87% | -0.666 | 0.774 | 2.442 | -35.66% |
| METALS_MINING | XME | materials_and_mining | -2.32% | -1.48% | 14.96% | 41.78% | -3.96% | -0.461 | 0.648 | 1.973 | -11.01% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | -1.07% | -1.50% | 0.72% | 10.31% | -1.52% | -1.137 | 0.681 | 0.555 | -1.52% |
| BIOTECH | XBI | healthcare_and_biotech | -3.90% | -2.42% | 7.22% | 35.10% | -4.16% | -0.449 | 0.306 | 0.731 | -4.16% |
| REGIONAL_BANKS | KRE | financials | -1.04% | -2.21% | -3.57% | 13.60% | -5.61% | -1.001 | 0.155 | 0.214 | -5.61% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | -2.54% | -4.26% | -2.53% | 23.51% | -9.82% | -0.326 | 0.417 | 0.776 | -9.82% |
| CANADA | EWC | international_equity | -1.93% | -1.96% | 2.10% | 10.65% | -1.93% | -0.477 | 0.583 | 0.510 | -1.93% |
| UNITED_KINGDOM | EWU | international_equity | -2.07% | -1.63% | -1.67% | 7.85% | -2.07% | -0.504 | 0.395 | 0.372 | -2.07% |
| AUSTRALIA | EWA | international_equity | -1.35% | -0.87% | -1.13% | 14.90% | -2.83% | 0.191 | 0.581 | 0.711 | -1.35% |
| SOUTH_KOREA | EWY | international_equity | 0.39% | 0.94% | 8.43% | 51.51% | -8.13% | -1.190 | 0.674 | 3.811 | -17.49% |
| TAIWAN | EWT | international_equity | 2.50% | 3.11% | 8.76% | 25.51% | -4.15% | -0.742 | 0.793 | 2.422 | -3.14% |
| BRAZIL | EWZ | international_equity | 0.42% | 2.30% | -6.22% | 20.03% | -8.05% | 0.581 | 0.389 | 0.613 | -12.84% |
| MEXICO | EWW | international_equity | -1.45% | -1.32% | -1.85% | 13.80% | -3.95% | -0.175 | 0.586 | 0.817 | -4.16% |
| SOUTH_AFRICA | EZA | international_equity | -2.77% | -3.24% | 10.90% | 29.93% | -3.77% | -0.362 | 0.670 | 1.521 | -11.71% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | -0.71% | -0.49% | -2.02% | 5.16% | -0.71% | 0.386 | 0.481 | 0.164 | -1.87% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | -0.45% | -0.70% | -2.33% | 2.97% | -1.00% | -0.111 | 0.530 | 0.113 | -2.03% |
| EMERGING_MARKET_BONDS | EMB | credit | -0.64% | -0.42% | -1.84% | 5.38% | -0.76% | -0.417 | 0.717 | 0.284 | -1.28% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | -0.75% | -0.68% | -2.43% | 3.97% | -0.92% | -0.262 | 0.471 | 0.125 | -2.00% |
| SILVER | SLV | precious_metals | -2.37% | -3.80% | 16.59% | 37.46% | -4.38% | 0.025 | 0.555 | 1.808 | -43.06% |
| COPPER | CPER | non_energy_commodities | -1.86% | -0.44% | -0.55% | 17.80% | -4.09% | -0.219 | 0.623 | 1.148 | -2.08% |
| AGRICULTURE | DBA | non_energy_commodities | 3.68% | 3.06% | 0.86% | 11.77% | -1.30% | 1.149 | 0.144 | 0.139 | 0.00% |
| OIL | USO | energy | 4.99% | 0.66% | 0.15% | 47.14% | -11.06% | -0.941 | -0.327 | -1.236 | -12.59% |
| US_DOLLAR | UUP | currencies | 0.64% | 0.32% | -3.05% | 4.64% | -1.13% | -1.272 | -0.386 | -0.146 | -1.68% |
| EURO | FXE | currencies | -0.51% | -0.98% | -0.87% | 4.20% | -0.51% | -0.493 | 0.397 | 0.142 | -3.02% |
| YEN | FXY | currencies | -0.42% | -1.01% | -1.99% | 8.40% | -1.90% | 0.140 | 0.257 | 0.148 | -8.64% |
| BITCOIN_ETF | IBIT | crypto_assets | 0.47% | -0.40% | 23.05% | 38.78% | -3.18% | 0.370 | 0.354 | 1.071 | -37.34% |
| ETHEREUM_ETF | ETHA | crypto_assets | 0.38% | -0.15% | 30.42% | 52.06% | -2.65% | 0.699 | 0.425 | 1.840 | -47.69% |
