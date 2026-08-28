# Full-Universe Horizon-Specific Decision Context

Profile: monthly. All values stop at the requested close and are sorted by frozen option order, not performance.

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
| active_return_dispersion_5s |  |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_5s | active_return_21s | prior_105s_active_return | volatility_63s | max_drawdown_63s | volume_zscore_20v120 | corr_spy_252s | beta_spy_252s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | -5.71% | -6.39% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.07% | -5.42% | -4.90% | 0.21% | -0.01% | -0.399 | -0.114 | -0.002 | 0.00% |
| SP500 | SPY | diversified_us_equity | 1.11% | 0.00% | 0.00% | 13.69% | -4.49% | -0.983 | 1.000 | 1.000 | -0.87% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | 1.08% | -0.10% | 0.10% | 13.59% | -4.36% | -0.662 | 0.995 | 1.011 | -0.95% |
| NASDAQ100 | QQQ | technology_and_growth | 1.43% | 3.27% | 2.48% | 25.63% | -11.22% | -0.996 | 0.930 | 1.425 | -3.25% |
| LARGE_GROWTH | IWF | technology_and_growth | 1.70% | 2.92% | -5.76% | 21.24% | -11.35% | -0.857 | 0.935 | 1.291 | -3.70% |
| LARGE_VALUE | IWD | diversified_us_equity | 0.55% | -2.48% | 5.09% | 11.16% | -2.40% | -0.664 | 0.798 | 0.695 | -0.46% |
| MID_CAP | IJH | diversified_us_equity | 0.37% | -3.14% | -2.20% | 13.53% | -3.22% | -0.750 | 0.805 | 0.969 | -2.57% |
| SMALL_CAP | IWM | diversified_us_equity | 0.72% | -1.81% | 2.55% | 16.51% | -3.95% | -1.189 | 0.819 | 1.196 | -1.73% |
| SMALL_VALUE | IWN | diversified_us_equity | 0.42% | -4.29% | 4.66% | 13.22% | -2.75% | -0.902 | 0.734 | 0.935 | -1.18% |
| DIVIDEND | SCHD | diversified_us_equity | 0.00% | -2.75% | 2.74% | 11.91% | -2.93% | 0.153 | 0.274 | 0.237 | -1.08% |
| LOW_VOL | SPLV | diversified_us_equity | -0.71% | -8.83% | -4.45% | 13.01% | -3.66% | -0.650 | 0.009 | 0.008 | -3.66% |
| MOMENTUM | MTUM | diversified_us_equity | -0.29% | 1.75% | 4.91% | 38.10% | -17.99% | 0.027 | 0.769 | 1.572 | -11.87% |
| TECHNOLOGY | XLK | technology_and_growth | 3.01% | 7.52% | 12.03% | 35.33% | -15.86% | -1.231 | 0.854 | 1.750 | -4.73% |
| COMMUNICATIONS | XLC | technology_and_growth | 0.66% | -3.97% | -12.02% | 19.76% | -9.44% | -0.979 | 0.569 | 0.671 | -6.68% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | -0.69% | -1.88% | -10.65% | 21.69% | -10.72% | -1.010 | 0.767 | 1.160 | -6.57% |
| CONSUMER_STAPLES | XLP | consumer_defensive | -0.28% | -8.32% | -6.84% | 17.76% | -3.58% | -0.937 | -0.069 | -0.077 | -4.29% |
| HEALTHCARE | XLV | healthcare_and_biotech | -0.47% | -2.50% | 0.12% | 19.86% | -3.74% | -0.739 | 0.216 | 0.270 | -2.33% |
| FINANCIALS | XLF | financials | 1.63% | -3.59% | 2.51% | 13.25% | -2.25% | -0.937 | 0.532 | 0.604 | -0.74% |
| INDUSTRIALS | XLI | industrials_and_defense | -0.54% | -4.50% | -5.88% | 18.51% | -4.80% | -0.980 | 0.710 | 0.948 | -4.13% |
| ENERGY | XLE | energy | -2.29% | 0.50% | 1.62% | 22.68% | -9.46% | -0.903 | -0.174 | -0.295 | -2.29% |
| MATERIALS | XLB | materials_and_mining | 1.55% | -2.83% | -7.97% | 19.37% | -4.75% | -0.495 | 0.527 | 0.732 | -0.82% |
| UTILITIES | XLU | rate_sensitive_defensive | -1.35% | -9.56% | -9.92% | 15.99% | -7.60% | -0.439 | 0.113 | 0.133 | -8.32% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | -0.93% | -8.54% | 0.59% | 15.98% | -4.19% | -0.477 | 0.238 | 0.261 | -2.93% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | 0.25% | -5.30% | -9.37% | 4.79% | -2.00% | 0.063 | 0.283 | 0.102 | -2.98% |
| LONG_TREASURY | TLT | rates_and_duration | 0.96% | -4.97% | -12.88% | 9.67% | -6.26% | 0.329 | 0.236 | 0.175 | -6.37% |
| TIPS | TIP | rates_and_duration | -0.07% | -5.28% | -7.34% | 3.48% | -1.40% | -0.320 | 0.257 | 0.066 | -0.76% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | 0.63% | -4.79% | -9.51% | 5.31% | -2.89% | -0.498 | 0.472 | 0.196 | -2.24% |
| HIGH_YIELD_CREDIT | HYG | credit | 0.39% | -4.42% | -5.93% | 3.03% | -0.80% | -0.728 | 0.777 | 0.229 | -0.06% |
| AGGREGATE_BONDS | AGG | rates_and_duration | 0.35% | -5.07% | -8.39% | 3.97% | -1.71% | -0.269 | 0.391 | 0.115 | -1.57% |
| DEVELOPED_EX_US | VEA | international_equity | 0.80% | 0.77% | -7.64% | 18.80% | -4.85% | -0.809 | 0.799 | 1.079 | -0.50% |
| EMERGING_MARKETS | VWO | international_equity | 1.65% | 1.48% | -8.59% | 18.93% | -7.05% | -0.762 | 0.810 | 1.111 | -0.38% |
| EUROPE | VGK | international_equity | 0.29% | -1.86% | -6.32% | 14.18% | -2.63% | -0.856 | 0.744 | 0.912 | -0.98% |
| JAPAN | EWJ | international_equity | 1.67% | 1.56% | -9.25% | 23.67% | -7.86% | -1.038 | 0.718 | 1.179 | -2.67% |
| CHINA | MCHI | international_equity | -1.10% | -6.02% | -12.80% | 18.58% | -11.15% | -0.571 | 0.536 | 0.844 | -16.50% |
| INDIA | INDA | international_equity | -0.04% | -4.98% | -12.87% | 13.53% | -4.59% | -1.053 | 0.554 | 0.655 | -10.42% |
| GOLD | IAU | precious_metals | 1.75% | 8.21% | -28.63% | 26.09% | -12.50% | -0.366 | 0.308 | 0.689 | -14.72% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | -0.70% | -0.87% | 12.97% | 21.89% | -12.58% | -0.327 | -0.174 | -0.276 | -2.59% |
| SEMICONDUCTORS | SMH | technology_and_growth | 1.84% | 7.93% | 15.99% | 53.35% | -24.62% | -0.657 | 0.781 | 2.390 | -14.34% |
| SOFTWARE | IGV | technology_and_growth | 8.25% | 13.72% | 5.46% | 38.03% | -21.29% | -1.140 | 0.502 | 1.214 | -6.32% |
| BROAD_AI_TECH | AIQ | technology_and_growth | 2.40% | 9.58% | 4.42% | 38.98% | -20.19% | -0.713 | 0.846 | 1.920 | -7.98% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | 0.39% | 7.62% | -18.47% | 37.50% | -23.82% | -0.971 | 0.801 | 2.191 | -13.67% |
| CYBERSECURITY | CIBR | technology_and_growth | 7.85% | 7.81% | 32.99% | 35.63% | -11.74% | -0.102 | 0.529 | 1.146 | -1.38% |
| SOLAR | TAN | clean_energy | 0.02% | -1.39% | -23.58% | 43.11% | -35.51% | -0.270 | 0.627 | 1.876 | -32.72% |
| METALS_MINING | XME | materials_and_mining | 7.24% | 20.34% | -24.99% | 41.04% | -26.49% | -0.051 | 0.596 | 1.764 | -7.34% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | 0.53% | -3.06% | -0.15% | 10.98% | -2.04% | -1.000 | 0.768 | 0.693 | -0.59% |
| BIOTECH | XBI | healthcare_and_biotech | 2.97% | 8.03% | 9.58% | 31.85% | -10.51% | -0.303 | 0.470 | 1.022 | -0.78% |
| REGIONAL_BANKS | KRE | financials | -0.48% | -8.11% | 3.10% | 18.72% | -4.62% | -0.850 | 0.413 | 0.710 | -4.59% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | -1.39% | -6.55% | -8.96% | 25.00% | -8.58% | -0.474 | 0.566 | 1.020 | -7.49% |
| CANADA | EWC | international_equity | 0.79% | -0.70% | -3.95% | 11.65% | -3.20% | -0.312 | 0.668 | 0.739 | -0.61% |
| UNITED_KINGDOM | EWU | international_equity | 0.19% | -4.18% | -6.44% | 12.87% | -2.53% | -0.561 | 0.599 | 0.700 | -1.54% |
| AUSTRALIA | EWA | international_equity | 1.21% | -2.27% | -8.45% | 16.83% | -4.78% | -0.677 | 0.669 | 0.923 | -1.05% |
| SOUTH_KOREA | EWY | international_equity | 2.23% | 20.59% | -10.51% | 77.54% | -34.21% | -0.470 | 0.635 | 2.770 | -16.91% |
| TAIWAN | EWT | international_equity | 4.38% | 15.79% | 11.04% | 41.82% | -19.83% | -0.894 | 0.760 | 1.858 | -2.60% |
| BRAZIL | EWZ | international_equity | 4.75% | -4.89% | -14.81% | 21.57% | -8.05% | -0.486 | 0.498 | 0.969 | -13.49% |
| MEXICO | EWW | international_equity | 2.20% | -3.60% | -11.32% | 19.07% | -5.91% | -0.302 | 0.539 | 0.924 | -3.61% |
| SOUTH_AFRICA | EZA | international_equity | 1.55% | 9.56% | -27.83% | 30.98% | -11.41% | -0.809 | 0.615 | 1.588 | -10.38% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | 0.24% | -5.03% | -8.32% | 4.61% | -1.85% | 0.093 | 0.386 | 0.133 | -1.43% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | -0.08% | -5.80% | -7.98% | 2.89% | -2.15% | 0.426 | 0.380 | 0.089 | -1.76% |
| EMERGING_MARKET_BONDS | EMB | credit | 0.49% | -4.66% | -7.46% | 5.40% | -1.96% | -0.678 | 0.678 | 0.304 | -0.90% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | 0.10% | -5.69% | -7.92% | 3.59% | -1.45% | -0.481 | 0.461 | 0.130 | -1.69% |
| SILVER | SLV | precious_metals | 1.80% | 15.54% | -42.04% | 43.83% | -26.29% | -0.742 | 0.353 | 1.707 | -40.56% |
| COPPER | CPER | non_energy_commodities | 1.60% | -1.46% | -1.98% | 25.29% | -10.57% | -0.518 | 0.550 | 1.216 | -2.13% |
| AGRICULTURE | DBA | non_energy_commodities | 1.55% | -0.87% | -0.86% | 13.11% | -4.86% | -0.454 | 0.075 | 0.065 | 0.00% |
| OIL | USO | energy | -3.37% | -5.17% | 55.71% | 52.51% | -26.69% | -0.619 | -0.337 | -1.272 | -15.00% |
| US_DOLLAR | UUP | currencies | 0.39% | -7.12% | -1.52% | 5.15% | -2.52% | -0.789 | -0.290 | -0.127 | -2.03% |
| EURO | FXE | currencies | -0.24% | -3.89% | -9.04% | 4.90% | -2.66% | -0.699 | 0.268 | 0.116 | -2.76% |
| YEN | FXY | currencies | -0.28% | -3.27% | -11.03% | 7.90% | -2.86% | 0.557 | 0.170 | 0.107 | -8.47% |
| BITCOIN_ETF | IBIT | crypto_assets | 9.93% | 20.10% | -12.30% | 41.24% | -20.03% | 0.223 | 0.474 | 1.663 | -36.47% |
| ETHEREUM_ETF | ETHA | crypto_assets | 7.52% | 26.81% | -13.26% | 58.97% | -22.76% | 0.643 | 0.496 | 2.509 | -47.28% |
