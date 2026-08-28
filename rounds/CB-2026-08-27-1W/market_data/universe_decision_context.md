# Full-Universe Horizon-Specific Decision Context

Profile: weekly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: yahoo_chart_adjusted_close_and_reported_volume
- As-of date requested: 2026-08-27
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | 1.11% |
| spy_return_21s | 5.71% |
| rsp_return_5s | 0.53% |
| rsp_return_21s | 2.65% |
| hyg_return_5s | 0.39% |
| hyg_return_21s | 1.28% |
| tlt_return_5s | 0.96% |
| tlt_return_21s | 0.74% |
| uup_return_5s | 0.39% |
| uup_return_21s | -1.41% |
| uso_return_5s | -3.37% |
| uso_return_21s | 0.54% |
| iau_return_5s | 1.75% |
| iau_return_21s | 13.91% |
| rsp_minus_spy_5s | -0.58% |
| rsp_minus_spy_21s | -3.06% |
| positive_asset_share_5s | 71.01% |
| positive_asset_share_21s | 86.96% |
| active_return_dispersion_5s | 2.38% |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_3s | active_return_5s | prior_16s_active_return | volatility_21s | max_drawdown_21s | volume_zscore_5v60 | corr_spy_63s | beta_spy_63s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | -1.11% | -4.54% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.02% | -1.05% | -4.32% | 0.17% | 0.00% | -0.807 | -0.131 | -0.002 | 0.00% |
| SP500 | SPY | diversified_us_equity | 1.00% | 0.00% | 0.00% | 11.48% | -1.96% | -1.301 | 1.000 | 1.000 | -0.87% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | 0.94% | -0.04% | -0.06% | 11.78% | -2.01% | -0.742 | 0.993 | 0.986 | -0.95% |
| NASDAQ100 | QQQ | technology_and_growth | 2.09% | 0.32% | 2.89% | 20.55% | -3.52% | -0.977 | 0.921 | 1.723 | -3.25% |
| LARGE_GROWTH | IWF | technology_and_growth | 2.35% | 0.58% | 2.27% | 19.33% | -3.68% | -0.480 | 0.903 | 1.400 | -3.70% |
| LARGE_VALUE | IWD | diversified_us_equity | -0.29% | -0.56% | -1.88% | 7.96% | -1.00% | -0.311 | 0.688 | 0.560 | -0.46% |
| MID_CAP | IJH | diversified_us_equity | 0.59% | -0.75% | -2.35% | 12.52% | -3.22% | 0.034 | 0.789 | 0.780 | -2.57% |
| SMALL_CAP | IWM | diversified_us_equity | 0.62% | -0.40% | -1.39% | 14.14% | -2.43% | -1.199 | 0.785 | 0.947 | -1.73% |
| SMALL_VALUE | IWN | diversified_us_equity | 0.30% | -0.70% | -3.55% | 10.04% | -1.59% | -0.837 | 0.650 | 0.627 | -1.18% |
| DIVIDEND | SCHD | diversified_us_equity | -1.08% | -1.11% | -1.59% | 10.83% | -1.24% | 0.488 | 0.093 | 0.081 | -1.08% |
| LOW_VOL | SPLV | diversified_us_equity | -1.17% | -1.83% | -6.97% | 8.78% | -3.12% | -0.810 | -0.299 | -0.284 | -3.66% |
| MOMENTUM | MTUM | diversified_us_equity | 1.21% | -1.40% | 3.23% | 29.49% | -6.67% | -0.935 | 0.697 | 1.939 | -11.87% |
| TECHNOLOGY | XLK | technology_and_growth | 4.75% | 1.89% | 5.38% | 31.32% | -5.62% | -0.995 | 0.828 | 2.136 | -4.73% |
| COMMUNICATIONS | XLC | technology_and_growth | -0.81% | -0.46% | -3.47% | 20.25% | -2.68% | -1.042 | 0.389 | 0.561 | -6.68% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | -2.05% | -1.80% | -0.00% | 19.17% | -3.32% | -1.244 | 0.660 | 1.045 | -6.57% |
| CONSUMER_STAPLES | XLP | consumer_defensive | -2.71% | -1.40% | -6.88% | 15.99% | -3.07% | -0.824 | -0.291 | -0.377 | -4.29% |
| HEALTHCARE | XLV | healthcare_and_biotech | -1.79% | -1.58% | -0.84% | 19.60% | -2.49% | -1.198 | -0.146 | -0.212 | -2.33% |
| FINANCIALS | XLF | financials | -0.58% | 0.52% | -4.07% | 9.86% | -2.25% | -1.020 | 0.278 | 0.269 | -0.74% |
| INDUSTRIALS | XLI | industrials_and_defense | -0.11% | -1.65% | -2.78% | 14.40% | -4.35% | -0.483 | 0.637 | 0.861 | -4.13% |
| ENERGY | XLE | energy | -1.30% | -3.40% | 4.15% | 23.15% | -3.76% | -0.617 | -0.316 | -0.523 | -2.29% |
| MATERIALS | XLB | materials_and_mining | -0.65% | 0.43% | -3.23% | 17.78% | -2.74% | -0.468 | 0.408 | 0.578 | -0.82% |
| UTILITIES | XLU | rate_sensitive_defensive | -0.09% | -2.46% | -7.08% | 12.90% | -4.77% | -0.750 | -0.127 | -0.148 | -8.32% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | -1.48% | -2.05% | -6.46% | 12.02% | -4.09% | -0.942 | -0.178 | -0.207 | -2.93% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | 0.24% | -0.87% | -4.38% | 4.81% | -0.60% | -0.026 | 0.433 | 0.151 | -2.98% |
| LONG_TREASURY | TLT | rates_and_duration | 0.69% | -0.16% | -4.76% | 10.78% | -1.99% | -0.192 | 0.312 | 0.220 | -6.37% |
| TIPS | TIP | rates_and_duration | 0.18% | -1.19% | -4.04% | 3.20% | -0.36% | -0.612 | 0.385 | 0.098 | -0.76% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | 0.52% | -0.48% | -4.26% | 5.79% | -0.99% | -0.641 | 0.511 | 0.198 | -2.24% |
| HIGH_YIELD_CREDIT | HYG | credit | 0.21% | -0.72% | -3.65% | 2.58% | -0.33% | -0.223 | 0.808 | 0.179 | -0.06% |
| AGGREGATE_BONDS | AGG | rates_and_duration | 0.29% | -0.77% | -4.26% | 4.18% | -0.48% | -1.013 | 0.478 | 0.139 | -1.57% |
| DEVELOPED_EX_US | VEA | international_equity | 0.49% | -0.32% | 1.10% | 15.58% | -1.76% | -0.463 | 0.805 | 1.105 | -0.50% |
| EMERGING_MARKETS | VWO | international_equity | 1.73% | 0.53% | 0.90% | 12.74% | -1.37% | -1.394 | 0.855 | 1.181 | -0.38% |
| EUROPE | VGK | international_equity | -0.36% | -0.82% | -1.00% | 11.10% | -1.13% | -0.762 | 0.729 | 0.755 | -0.98% |
| JAPAN | EWJ | international_equity | 1.05% | 0.55% | 0.96% | 22.42% | -4.27% | -1.406 | 0.751 | 1.298 | -2.67% |
| CHINA | MCHI | international_equity | -0.05% | -2.21% | -3.74% | 13.43% | -4.41% | -1.197 | 0.414 | 0.562 | -16.50% |
| INDIA | INDA | international_equity | 0.36% | -1.15% | -3.77% | 10.27% | -2.34% | -0.650 | 0.561 | 0.554 | -10.42% |
| GOLD | IAU | precious_metals | -0.97% | 0.64% | 7.41% | 24.94% | -1.68% | -0.373 | 0.475 | 0.904 | -14.72% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | -0.27% | -1.82% | 1.03% | 20.27% | -3.81% | -0.314 | -0.165 | -0.264 | -2.59% |
| SEMICONDUCTORS | SMH | technology_and_growth | 4.79% | 0.72% | 7.05% | 39.63% | -7.96% | -0.802 | 0.750 | 2.921 | -14.34% |
| SOFTWARE | IGV | technology_and_growth | 7.68% | 7.14% | 5.78% | 39.25% | -4.17% | -0.706 | 0.466 | 1.293 | -6.32% |
| BROAD_AI_TECH | AIQ | technology_and_growth | 3.60% | 1.28% | 8.05% | 28.89% | -3.59% | -0.471 | 0.829 | 2.359 | -7.98% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | 1.91% | -0.73% | 8.34% | 33.98% | -6.62% | -1.032 | 0.861 | 2.357 | -13.67% |
| CYBERSECURITY | CIBR | technology_and_growth | 8.11% | 6.74% | 0.71% | 39.01% | -9.53% | 0.224 | 0.541 | 1.407 | -1.38% |
| SOLAR | TAN | clean_energy | 2.94% | -1.09% | -0.24% | 36.47% | -9.46% | 0.196 | 0.773 | 2.434 | -32.72% |
| METALS_MINING | XME | materials_and_mining | 4.35% | 6.12% | 13.00% | 39.91% | -3.78% | 0.407 | 0.648 | 1.943 | -7.34% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | -0.22% | -0.58% | -2.43% | 9.68% | -1.34% | -1.230 | 0.685 | 0.550 | -0.59% |
| BIOTECH | XBI | healthcare_and_biotech | 2.47% | 1.85% | 5.92% | 32.95% | -3.64% | -0.239 | 0.303 | 0.706 | -0.78% |
| REGIONAL_BANKS | KRE | financials | -0.55% | -1.60% | -6.47% | 13.22% | -4.62% | -0.939 | 0.150 | 0.205 | -4.59% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | 0.37% | -2.50% | -3.99% | 22.12% | -7.83% | -0.415 | 0.416 | 0.759 | -7.49% |
| CANADA | EWC | international_equity | 0.23% | -0.32% | -0.36% | 9.49% | -1.04% | -0.586 | 0.590 | 0.502 | -0.61% |
| UNITED_KINGDOM | EWU | international_equity | -0.96% | -0.93% | -3.21% | 9.50% | -1.54% | -0.692 | 0.391 | 0.367 | -1.54% |
| AUSTRALIA | EWA | international_equity | 0.17% | 0.10% | -2.34% | 17.00% | -2.83% | 0.076 | 0.580 | 0.713 | -1.05% |
| SOUTH_KOREA | EWY | international_equity | 4.90% | 1.12% | 19.00% | 64.16% | -8.13% | -1.209 | 0.673 | 3.812 | -16.91% |
| TAIWAN | EWT | international_equity | 5.13% | 3.27% | 11.85% | 29.37% | -4.15% | -0.957 | 0.793 | 2.422 | -2.60% |
| BRAZIL | EWZ | international_equity | 1.68% | 3.63% | -8.29% | 22.51% | -8.05% | 0.700 | 0.392 | 0.617 | -13.49% |
| MEXICO | EWW | international_equity | 0.01% | 1.08% | -4.64% | 15.36% | -3.95% | -0.079 | 0.583 | 0.812 | -3.61% |
| SOUTH_AFRICA | EZA | international_equity | 0.32% | 0.43% | 8.97% | 30.55% | -3.77% | -0.497 | 0.667 | 1.510 | -10.38% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | 0.23% | -0.88% | -4.10% | 4.89% | -0.48% | 0.393 | 0.481 | 0.162 | -1.43% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | -0.02% | -1.19% | -4.56% | 2.82% | -0.77% | -0.034 | 0.530 | 0.112 | -1.76% |
| EMERGING_MARKET_BONDS | EMB | credit | 0.30% | -0.63% | -3.99% | 5.23% | -0.76% | -0.411 | 0.718 | 0.283 | -0.90% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | 0.04% | -1.01% | -4.63% | 3.86% | -0.83% | -0.390 | 0.471 | 0.123 | -1.69% |
| SILVER | SLV | precious_metals | 0.92% | 0.69% | 14.56% | 35.32% | -3.58% | -0.174 | 0.558 | 1.785 | -40.56% |
| COPPER | CPER | non_energy_commodities | -0.22% | 0.49% | -1.94% | 19.79% | -4.09% | -0.107 | 0.621 | 1.147 | -2.13% |
| AGRICULTURE | DBA | non_energy_commodities | 1.84% | 0.44% | -1.31% | 10.61% | -1.30% | 0.757 | 0.152 | 0.145 | 0.00% |
| OIL | USO | energy | -1.66% | -4.48% | -0.50% | 46.47% | -11.16% | -0.958 | -0.313 | -1.199 | -15.00% |
| US_DOLLAR | UUP | currencies | 0.21% | -0.72% | -6.34% | 5.56% | -1.90% | -1.490 | -0.384 | -0.145 | -2.03% |
| EURO | FXE | currencies | -0.10% | -1.36% | -2.48% | 4.68% | -0.32% | -0.448 | 0.395 | 0.141 | -2.76% |
| YEN | FXY | currencies | -0.24% | -1.39% | -1.82% | 12.27% | -1.74% | 0.089 | 0.254 | 0.147 | -8.47% |
| BITCOIN_ETF | IBIT | crypto_assets | 1.46% | 8.81% | 9.90% | 38.58% | -3.18% | 1.380 | 0.349 | 1.050 | -36.47% |
| ETHEREUM_ETF | ETHA | crypto_assets | 1.13% | 6.41% | 18.70% | 52.45% | -3.03% | 1.467 | 0.425 | 1.830 | -47.28% |
