# Full-Universe Horizon-Specific Decision Context

Profile: monthly. All values stop at the requested close and are sorted by frozen option order, not performance.

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
| active_return_dispersion_5s |  |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_5s | active_return_21s | prior_105s_active_return | volatility_63s | max_drawdown_63s | volume_zscore_20v120 | corr_spy_252s | beta_spy_252s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | -2.68% | -9.41% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.05% | -2.40% | -7.92% | 0.21% | -0.01% | -0.602 | -0.114 | -0.002 | 0.00% |
| SP500 | SPY | diversified_us_equity | 0.47% | 0.00% | 0.00% | 13.71% | -4.49% | -1.066 | 1.000 | 1.000 | -1.39% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | -0.02% | 0.56% | -0.65% | 13.66% | -4.36% | -0.654 | 0.995 | 1.012 | -1.60% |
| NASDAQ100 | QQQ | technology_and_growth | 1.48% | 1.50% | 3.99% | 25.62% | -11.22% | -1.066 | 0.930 | 1.424 | -3.83% |
| LARGE_GROWTH | IWF | technology_and_growth | 0.26% | 1.82% | -4.89% | 21.29% | -11.35% | -0.847 | 0.934 | 1.292 | -4.62% |
| LARGE_VALUE | IWD | diversified_us_equity | -0.15% | -0.21% | 2.53% | 11.18% | -2.40% | -0.641 | 0.798 | 0.695 | -0.72% |
| MID_CAP | IJH | diversified_us_equity | -1.85% | -2.68% | -3.51% | 13.97% | -4.22% | -0.743 | 0.803 | 0.972 | -4.22% |
| SMALL_CAP | IWM | diversified_us_equity | -2.01% | -2.22% | 2.98% | 16.96% | -3.95% | -1.210 | 0.817 | 1.200 | -3.66% |
| SMALL_VALUE | IWN | diversified_us_equity | -1.34% | -2.68% | 3.57% | 13.42% | -2.60% | -0.881 | 0.733 | 0.937 | -2.48% |
| DIVIDEND | SCHD | diversified_us_equity | -0.91% | 1.56% | -2.63% | 11.65% | -2.93% | 0.071 | 0.274 | 0.237 | -0.91% |
| LOW_VOL | SPLV | diversified_us_equity | -0.64% | -4.71% | -9.81% | 12.97% | -4.03% | -0.615 | 0.010 | 0.008 | -4.03% |
| MOMENTUM | MTUM | diversified_us_equity | -1.58% | -2.15% | 8.93% | 38.17% | -17.99% | -0.090 | 0.770 | 1.574 | -12.99% |
| TECHNOLOGY | XLK | technology_and_growth | 1.74% | 3.45% | 17.54% | 35.12% | -15.86% | -1.302 | 0.854 | 1.751 | -5.80% |
| COMMUNICATIONS | XLC | technology_and_growth | 0.05% | 1.90% | -18.61% | 19.70% | -8.67% | -1.002 | 0.569 | 0.671 | -6.64% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | -1.21% | 1.06% | -12.85% | 21.66% | -9.84% | -1.165 | 0.765 | 1.157 | -5.99% |
| CONSUMER_STAPLES | XLP | consumer_defensive | -1.17% | -3.25% | -13.26% | 17.37% | -3.58% | -0.970 | -0.068 | -0.077 | -4.40% |
| HEALTHCARE | XLV | healthcare_and_biotech | -2.38% | 2.24% | -6.00% | 19.60% | -3.74% | -0.835 | 0.218 | 0.273 | -2.93% |
| FINANCIALS | XLF | financials | -0.88% | -1.33% | 2.54% | 13.30% | -2.25% | -0.966 | 0.531 | 0.605 | -1.03% |
| INDUSTRIALS | XLI | industrials_and_defense | -2.84% | -4.51% | -8.18% | 18.97% | -6.10% | -0.968 | 0.708 | 0.952 | -6.10% |
| ENERGY | XLE | energy | 1.35% | 4.73% | -3.57% | 22.61% | -9.46% | -0.889 | -0.177 | -0.302 | 0.00% |
| MATERIALS | XLB | materials_and_mining | -1.59% | -0.65% | -11.94% | 19.47% | -4.75% | -0.564 | 0.528 | 0.734 | -1.83% |
| UTILITIES | XLU | rate_sensitive_defensive | -1.26% | -8.12% | -14.59% | 16.54% | -8.77% | -0.361 | 0.116 | 0.138 | -10.34% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | -2.69% | -4.81% | -5.20% | 15.61% | -4.19% | -0.521 | 0.240 | 0.264 | -4.13% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | -0.09% | -2.84% | -12.74% | 4.89% | -2.00% | 0.058 | 0.284 | 0.103 | -3.49% |
| LONG_TREASURY | TLT | rates_and_duration | 0.57% | -2.62% | -16.53% | 9.77% | -6.26% | 0.265 | 0.238 | 0.177 | -7.06% |
| TIPS | TIP | rates_and_duration | -0.29% | -2.81% | -10.55% | 3.66% | -1.40% | -0.401 | 0.258 | 0.067 | -1.33% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | 0.27% | -2.44% | -12.33% | 5.39% | -2.89% | -0.547 | 0.472 | 0.197 | -2.71% |
| HIGH_YIELD_CREDIT | HYG | credit | 0.25% | -1.76% | -8.50% | 3.03% | -0.80% | -0.733 | 0.778 | 0.229 | -0.14% |
| AGGREGATE_BONDS | AGG | rates_and_duration | 0.06% | -2.55% | -11.54% | 4.06% | -1.71% | -0.263 | 0.391 | 0.116 | -1.99% |
| DEVELOPED_EX_US | VEA | international_equity | -0.68% | -0.11% | -7.50% | 18.85% | -4.85% | -0.806 | 0.799 | 1.080 | -1.18% |
| EMERGING_MARKETS | VWO | international_equity | 0.12% | 1.32% | -9.14% | 19.00% | -7.05% | -0.757 | 0.811 | 1.113 | -1.18% |
| EUROPE | VGK | international_equity | -1.14% | -1.94% | -6.65% | 14.26% | -2.61% | -0.884 | 0.745 | 0.914 | -1.64% |
| JAPAN | EWJ | international_equity | 0.74% | 0.10% | -7.87% | 23.67% | -7.86% | -1.033 | 0.718 | 1.179 | -2.63% |
| CHINA | MCHI | international_equity | -1.69% | -4.09% | -14.82% | 18.59% | -11.15% | -0.680 | 0.542 | 0.846 | -16.77% |
| INDIA | INDA | international_equity | 0.12% | -2.68% | -14.33% | 13.53% | -4.59% | -1.045 | 0.553 | 0.653 | -10.11% |
| GOLD | IAU | precious_metals | -3.55% | 5.61% | -31.39% | 26.88% | -12.50% | -0.372 | 0.309 | 0.697 | -17.58% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | 0.00% | 3.89% | 7.88% | 21.98% | -12.58% | -0.337 | -0.175 | -0.278 | -1.37% |
| SEMICONDUCTORS | SMH | technology_and_growth | -0.68% | 0.61% | 23.20% | 53.65% | -24.62% | -0.768 | 0.780 | 2.395 | -16.79% |
| SOFTWARE | IGV | technology_and_growth | 7.35% | 13.60% | 4.88% | 34.10% | -21.29% | -1.108 | 0.502 | 1.211 | -6.61% |
| BROAD_AI_TECH | AIQ | technology_and_growth | 1.37% | 6.88% | 7.36% | 38.87% | -20.19% | -0.784 | 0.846 | 1.920 | -8.33% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | -2.45% | 4.80% | -16.32% | 37.56% | -23.31% | -1.035 | 0.801 | 2.194 | -14.82% |
| CYBERSECURITY | CIBR | technology_and_growth | 5.59% | 8.57% | 34.05% | 33.46% | -11.74% | -0.081 | 0.529 | 1.146 | -2.01% |
| SOLAR | TAN | clean_energy | -3.55% | -7.23% | -18.80% | 43.23% | -35.66% | -0.342 | 0.627 | 1.887 | -35.66% |
| METALS_MINING | XME | materials_and_mining | -1.01% | 13.29% | -23.96% | 41.76% | -26.49% | -0.062 | 0.595 | 1.773 | -11.01% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | -1.03% | -0.82% | -3.48% | 11.17% | -2.04% | -1.026 | 0.768 | 0.695 | -1.52% |
| BIOTECH | XBI | healthcare_and_biotech | -1.95% | 4.61% | 9.62% | 32.73% | -10.51% | -0.311 | 0.469 | 1.029 | -4.16% |
| REGIONAL_BANKS | KRE | financials | -1.74% | -5.76% | 5.59% | 18.87% | -5.61% | -0.833 | 0.413 | 0.712 | -5.61% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | -3.79% | -6.79% | -11.58% | 25.50% | -9.82% | -0.459 | 0.566 | 1.026 | -9.82% |
| CANADA | EWC | international_equity | -1.49% | 0.06% | -5.81% | 11.99% | -3.20% | -0.300 | 0.667 | 0.741 | -1.93% |
| UNITED_KINGDOM | EWU | international_equity | -1.16% | -3.32% | -7.98% | 12.92% | -2.39% | -0.517 | 0.600 | 0.701 | -2.07% |
| AUSTRALIA | EWA | international_equity | -0.40% | -2.01% | -8.92% | 16.75% | -4.78% | -0.664 | 0.669 | 0.923 | -1.35% |
| SOUTH_KOREA | EWY | international_equity | 1.41% | 9.51% | -2.91% | 77.55% | -34.21% | -0.605 | 0.636 | 2.771 | -17.49% |
| TAIWAN | EWT | international_equity | 3.58% | 12.25% | 14.81% | 41.84% | -19.83% | -0.979 | 0.761 | 1.859 | -3.14% |
| BRAZIL | EWZ | international_equity | 2.77% | -4.05% | -14.20% | 21.59% | -8.05% | -0.472 | 0.497 | 0.966 | -12.84% |
| MEXICO | EWW | international_equity | -0.85% | -3.19% | -12.74% | 19.08% | -5.91% | -0.274 | 0.539 | 0.925 | -4.16% |
| SOUTH_AFRICA | EZA | international_equity | -2.77% | 7.29% | -29.13% | 31.12% | -11.18% | -0.742 | 0.616 | 1.592 | -11.71% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | -0.02% | -2.52% | -11.45% | 4.69% | -1.85% | 0.072 | 0.386 | 0.134 | -1.87% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | -0.23% | -3.03% | -11.01% | 2.92% | -2.15% | 0.418 | 0.381 | 0.090 | -2.03% |
| EMERGING_MARKET_BONDS | EMB | credit | 0.05% | -2.26% | -10.30% | 5.43% | -1.96% | -0.703 | 0.679 | 0.305 | -1.28% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | -0.21% | -3.12% | -10.98% | 3.63% | -1.53% | -0.477 | 0.462 | 0.130 | -2.00% |
| SILVER | SLV | precious_metals | -3.33% | 12.16% | -45.22% | 44.64% | -25.89% | -0.653 | 0.353 | 1.713 | -43.06% |
| COPPER | CPER | non_energy_commodities | 0.03% | -1.00% | -2.74% | 25.26% | -10.57% | -0.458 | 0.551 | 1.216 | -2.08% |
| AGRICULTURE | DBA | non_energy_commodities | 3.53% | 4.02% | -3.80% | 13.26% | -3.71% | -0.347 | 0.069 | 0.060 | 0.00% |
| OIL | USO | energy | 1.13% | 0.83% | 38.73% | 51.86% | -26.69% | -0.631 | -0.338 | -1.277 | -12.59% |
| US_DOLLAR | UUP | currencies | 0.79% | -2.75% | -5.50% | 5.18% | -2.52% | -0.864 | -0.291 | -0.128 | -1.68% |
| EURO | FXE | currencies | -0.51% | -1.87% | -11.51% | 4.92% | -2.66% | -0.693 | 0.269 | 0.117 | -3.02% |
| YEN | FXY | currencies | -0.54% | -3.01% | -11.54% | 7.90% | -2.81% | 0.396 | 0.170 | 0.108 | -8.64% |
| BITCOIN_ETF | IBIT | crypto_assets | 0.07% | 22.66% | -18.48% | 41.46% | -17.78% | 0.386 | 0.472 | 1.662 | -37.34% |
| ETHEREUM_ETF | ETHA | crypto_assets | 0.32% | 30.37% | -17.87% | 59.33% | -22.30% | 0.822 | 0.496 | 2.512 | -47.69% |
