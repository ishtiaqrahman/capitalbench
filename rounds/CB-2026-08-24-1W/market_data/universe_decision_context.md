# Full-Universe Horizon-Specific Decision Context

Profile: weekly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: tiingo_eod_adjusted_price_and_volume
- As-of date requested: 2026-08-24
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | -1.19% |
| spy_return_21s | 3.32% |
| rsp_return_5s | 0.52% |
| rsp_return_21s | 3.91% |
| hyg_return_5s | 0.11% |
| hyg_return_21s | 1.08% |
| tlt_return_5s | 1.49% |
| tlt_return_21s | -0.43% |
| uup_return_5s | -0.50% |
| uup_return_21s | -2.17% |
| uso_return_5s | 1.47% |
| uso_return_21s | -3.28% |
| iau_return_5s | 5.25% |
| iau_return_21s | 14.74% |
| rsp_minus_spy_5s | 1.71% |
| rsp_minus_spy_21s | 0.59% |
| positive_asset_share_5s | 56.52% |
| positive_asset_share_21s | 79.71% |
| active_return_dispersion_5s | 5.38% |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_3s | active_return_5s | prior_16s_active_return | volatility_21s | max_drawdown_21s | volume_zscore_5v60 | corr_spy_63s | beta_spy_63s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | 1.19% | -4.57% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.04% | 1.26% | -4.33% | 0.17% | 0.00% | -0.766 | -0.113 | -0.002 | 0.00% |
| SP500 | SPY | diversified_us_equity | -0.73% | 0.00% | 0.00% | 12.95% | -1.96% | -0.773 | 1.000 | 1.000 | -1.85% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | -0.77% | -0.13% | 0.18% | 13.19% | -2.01% | -0.240 | 0.993 | 0.988 | -1.88% |
| NASDAQ100 | QQQ | technology_and_growth | -1.36% | -2.04% | 2.10% | 22.33% | -3.52% | -0.345 | 0.920 | 1.727 | -5.23% |
| LARGE_GROWTH | IWF | technology_and_growth | -1.33% | -2.04% | 1.75% | 20.69% | -3.68% | -0.536 | 0.904 | 1.387 | -5.92% |
| LARGE_VALUE | IWD | diversified_us_equity | -0.17% | 1.85% | -1.19% | 9.28% | -1.00% | -0.136 | 0.702 | 0.574 | -0.17% |
| MID_CAP | IJH | diversified_us_equity | -1.09% | -1.71% | -0.99% | 13.91% | -3.14% | -0.984 | 0.792 | 0.799 | -3.14% |
| SMALL_CAP | IWM | diversified_us_equity | -1.24% | -0.81% | -0.14% | 15.51% | -2.43% | -0.822 | 0.784 | 0.967 | -2.33% |
| SMALL_VALUE | IWN | diversified_us_equity | -0.69% | 0.13% | -2.29% | 11.25% | -1.59% | -1.178 | 0.653 | 0.644 | -1.48% |
| DIVIDEND | SCHD | diversified_us_equity | 0.34% | 3.87% | -1.56% | 11.11% | -1.42% | 0.303 | 0.100 | 0.086 | 0.00% |
| LOW_VOL | SPLV | diversified_us_equity | 0.23% | 1.73% | -6.44% | 9.25% | -3.41% | 0.054 | -0.297 | -0.282 | -2.33% |
| MOMENTUM | MTUM | diversified_us_equity | -1.73% | -5.48% | 0.55% | 34.35% | -7.60% | -0.577 | 0.701 | 1.978 | -12.93% |
| TECHNOLOGY | XLK | technology_and_growth | -1.95% | -4.21% | 3.64% | 32.79% | -5.62% | -0.953 | 0.831 | 2.130 | -9.05% |
| COMMUNICATIONS | XLC | technology_and_growth | 0.90% | 2.54% | -0.31% | 20.81% | -2.82% | -1.061 | 0.400 | 0.572 | -5.92% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | -0.24% | 2.52% | 2.14% | 19.32% | -2.92% | -0.794 | 0.666 | 1.062 | -4.62% |
| CONSUMER_STAPLES | XLP | consumer_defensive | 1.05% | 4.46% | -3.91% | 17.00% | -3.07% | -0.213 | -0.288 | -0.373 | -1.62% |
| HEALTHCARE | XLV | healthcare_and_biotech | -0.56% | 5.77% | -1.81% | 20.16% | -3.09% | -0.110 | -0.137 | -0.197 | -0.56% |
| FINANCIALS | XLF | financials | 1.29% | 2.30% | -2.31% | 12.35% | -2.25% | -0.486 | 0.278 | 0.270 | -0.07% |
| INDUSTRIALS | XLI | industrials_and_defense | -1.62% | -2.74% | -2.56% | 17.67% | -4.03% | -0.588 | 0.658 | 0.888 | -4.03% |
| ENERGY | XLE | energy | -0.74% | 2.04% | 0.40% | 24.93% | -3.87% | -0.797 | -0.320 | -0.544 | -1.00% |
| MATERIALS | XLB | materials_and_mining | 2.02% | 3.76% | -2.65% | 18.98% | -3.65% | -0.153 | 0.428 | 0.608 | 0.00% |
| UTILITIES | XLU | rate_sensitive_defensive | -1.82% | -0.98% | -9.12% | 13.54% | -7.60% | -0.250 | -0.129 | -0.151 | -8.24% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | 0.76% | 2.31% | -7.00% | 11.76% | -4.19% | -0.377 | -0.169 | -0.195 | -1.48% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | -0.40% | 1.37% | -4.43% | 4.81% | -0.65% | -0.175 | 0.454 | 0.157 | -3.20% |
| LONG_TREASURY | TLT | rates_and_duration | -0.55% | 2.68% | -6.46% | 11.97% | -3.04% | 0.585 | 0.328 | 0.228 | -7.01% |
| TIPS | TIP | rates_and_duration | -0.24% | 1.64% | -4.52% | 3.06% | -0.36% | 0.454 | 0.406 | 0.104 | -0.93% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | -0.37% | 1.64% | -4.64% | 5.90% | -0.99% | 0.215 | 0.528 | 0.202 | -2.74% |
| HIGH_YIELD_CREDIT | HYG | credit | -0.01% | 1.30% | -3.60% | 2.66% | -0.33% | 0.041 | 0.819 | 0.183 | -0.11% |
| AGGREGATE_BONDS | AGG | rates_and_duration | -0.28% | 1.50% | -4.44% | 4.20% | -0.56% | -0.940 | 0.496 | 0.141 | -1.85% |
| DEVELOPED_EX_US | VEA | international_equity | 0.32% | 0.34% | 1.14% | 15.98% | -1.76% | 0.089 | 0.809 | 1.124 | -0.85% |
| EMERGING_MARKETS | VWO | international_equity | -0.12% | 0.50% | -0.09% | 14.31% | -2.25% | -0.822 | 0.842 | 1.183 | -2.07% |
| EUROPE | VGK | international_equity | 0.41% | 1.74% | -0.39% | 10.74% | -1.13% | -0.563 | 0.738 | 0.766 | -0.12% |
| JAPAN | EWJ | international_equity | 0.06% | -2.20% | 3.06% | 23.66% | -4.27% | -0.539 | 0.753 | 1.306 | -3.69% |
| CHINA | MCHI | international_equity | -0.83% | 0.95% | -1.32% | 15.16% | -4.41% | -0.965 | 0.413 | 0.568 | -16.45% |
| INDIA | INDA | international_equity | -0.38% | 0.73% | -1.32% | 10.16% | -2.34% | -1.176 | 0.589 | 0.554 | -10.74% |
| GOLD | IAU | precious_metals | 3.10% | 6.44% | 4.46% | 24.70% | -1.68% | 0.381 | 0.477 | 0.907 | -13.88% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | 0.76% | 2.62% | -3.12% | 25.60% | -5.85% | -0.345 | -0.176 | -0.282 | -2.33% |
| SEMICONDUCTORS | SMH | technology_and_growth | -2.52% | -6.77% | 1.29% | 45.01% | -10.15% | -0.458 | 0.748 | 2.928 | -18.26% |
| SOFTWARE | IGV | technology_and_growth | -0.35% | 1.64% | 11.36% | 31.47% | -4.11% | -1.311 | 0.475 | 1.222 | -13.01% |
| BROAD_AI_TECH | AIQ | technology_and_growth | -1.10% | -1.47% | 5.82% | 30.76% | -3.98% | -0.774 | 0.827 | 2.383 | -11.18% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | -3.32% | -5.43% | 9.87% | 37.01% | -6.62% | -1.086 | 0.859 | 2.388 | -15.29% |
| CYBERSECURITY | CIBR | technology_and_growth | -2.42% | -3.47% | 6.06% | 29.34% | -8.78% | 0.102 | 0.554 | 1.334 | -8.78% |
| SOLAR | TAN | clean_energy | -4.26% | -3.92% | -5.27% | 40.73% | -9.46% | 0.166 | 0.762 | 2.473 | -34.64% |
| METALS_MINING | XME | materials_and_mining | 0.68% | 1.00% | 11.51% | 43.33% | -5.36% | 1.204 | 0.649 | 1.985 | -11.20% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | -0.06% | 1.71% | -1.19% | 11.04% | -1.34% | -1.102 | 0.702 | 0.562 | -0.38% |
| BIOTECH | XBI | healthcare_and_biotech | -3.17% | 4.10% | 1.45% | 32.40% | -3.64% | 0.811 | 0.311 | 0.713 | -3.17% |
| REGIONAL_BANKS | KRE | financials | -0.32% | -2.21% | -2.37% | 14.66% | -4.13% | 0.280 | 0.167 | 0.230 | -4.07% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | -5.18% | -5.90% | 0.04% | 25.63% | -7.83% | -0.421 | 0.438 | 0.814 | -7.83% |
| CANADA | EWC | international_equity | 0.47% | 1.09% | 0.70% | 9.82% | -1.04% | -0.004 | 0.596 | 0.505 | -0.38% |
| UNITED_KINGDOM | EWU | international_equity | 1.09% | 3.14% | -2.60% | 8.58% | -1.07% | -0.689 | 0.402 | 0.373 | 0.00% |
| AUSTRALIA | EWA | international_equity | 0.30% | 2.92% | -1.68% | 17.11% | -2.83% | -0.420 | 0.591 | 0.714 | -1.15% |
| SOUTH_KOREA | EWY | international_equity | -0.45% | -5.00% | 9.02% | 70.71% | -11.51% | -0.446 | 0.673 | 3.935 | -20.78% |
| TAIWAN | EWT | international_equity | -1.31% | -2.96% | 5.42% | 38.12% | -8.77% | -1.191 | 0.780 | 2.437 | -7.35% |
| BRAZIL | EWZ | international_equity | 2.66% | 4.72% | -9.49% | 22.13% | -8.05% | 0.152 | 0.391 | 0.607 | -14.92% |
| MEXICO | EWW | international_equity | 2.68% | 4.18% | -5.28% | 16.70% | -3.95% | 0.291 | 0.580 | 0.816 | -3.63% |
| SOUTH_AFRICA | EZA | international_equity | 1.48% | 5.80% | 7.09% | 29.73% | -3.77% | -0.600 | 0.673 | 1.556 | -10.74% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | -0.28% | 1.47% | -4.26% | 5.03% | -0.80% | 0.738 | 0.500 | 0.166 | -1.65% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | -0.26% | 1.05% | -4.29% | 3.02% | -0.77% | 0.785 | 0.532 | 0.118 | -1.74% |
| EMERGING_MARKET_BONDS | EMB | credit | -0.27% | 1.35% | -4.07% | 5.57% | -0.76% | -0.742 | 0.734 | 0.290 | -1.20% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | -0.13% | 1.25% | -4.63% | 3.68% | -0.83% | 0.133 | 0.505 | 0.128 | -1.74% |
| SILVER | SLV | precious_metals | 3.65% | 5.61% | 8.71% | 36.23% | -3.58% | 0.314 | 0.556 | 1.796 | -41.10% |
| COPPER | CPER | non_energy_commodities | 1.73% | 1.04% | 0.08% | 18.62% | -4.09% | 0.698 | 0.630 | 1.155 | -1.91% |
| AGRICULTURE | DBA | non_energy_commodities | 0.04% | 1.76% | -4.92% | 13.84% | -2.87% | 0.164 | 0.143 | 0.135 | -1.50% |
| OIL | USO | energy | 0.99% | 2.66% | -9.25% | 60.08% | -15.96% | -0.929 | -0.321 | -1.227 | -13.57% |
| US_DOLLAR | UUP | currencies | 0.29% | 0.69% | -6.25% | 5.68% | -2.52% | -1.475 | -0.391 | -0.146 | -2.24% |
| EURO | FXE | currencies | -0.13% | 1.93% | -2.66% | 4.82% | -0.32% | -0.339 | 0.407 | 0.146 | -2.67% |
| YEN | FXY | currencies | -0.65% | 1.38% | -1.91% | 12.23% | -1.74% | -0.255 | 0.257 | 0.148 | -8.25% |
| BITCOIN_ETF | IBIT | crypto_assets | 15.11% | 23.76% | -4.37% | 39.51% | -3.18% | 3.171 | 0.331 | 0.999 | -37.38% |
| ETHEREUM_ETF | ETHA | crypto_assets | 17.51% | 30.77% | -2.00% | 55.40% | -4.35% | 4.344 | 0.416 | 1.792 | -49.00% |
