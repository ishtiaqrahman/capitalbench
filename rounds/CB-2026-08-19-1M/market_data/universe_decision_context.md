# Full-Universe Horizon-Specific Decision Context

Profile: monthly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: yahoo_chart_adjusted_close_and_reported_volume
- As-of date requested: 2026-08-18
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | -0.40% |
| spy_return_21s | 3.42% |
| rsp_return_5s | -0.41% |
| rsp_return_21s | 2.20% |
| hyg_return_5s | 0.03% |
| hyg_return_21s | 0.30% |
| tlt_return_5s | -0.64% |
| tlt_return_21s | -2.27% |
| uup_return_5s | 0.00% |
| uup_return_21s | -0.88% |
| uso_return_5s | 2.39% |
| uso_return_21s | 4.10% |
| iau_return_5s | -0.57% |
| iau_return_21s | 8.44% |
| rsp_minus_spy_5s | -0.00% |
| rsp_minus_spy_21s | -1.22% |
| positive_asset_share_5s | 39.13% |
| positive_asset_share_21s | 73.91% |
| active_return_dispersion_5s |  |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_5s | active_return_21s | prior_105s_active_return | volatility_63s | max_drawdown_63s | volume_zscore_20v120 | corr_spy_252s | beta_spy_252s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | -3.42% | -9.25% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.08% | -3.12% | -7.76% | 0.21% | -0.01% | -0.375 | -0.107 | -0.002 | 0.00% |
| SP500 | SPY | diversified_us_equity | -0.40% | 0.00% | 0.00% | 13.80% | -4.49% | -0.840 | 1.000 | 1.000 | -1.34% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | -0.42% | 0.07% | 0.06% | 13.74% | -4.36% | -0.717 | 0.995 | 1.012 | -1.37% |
| NASDAQ100 | QQQ | technology_and_growth | -0.13% | -0.34% | 6.78% | 25.88% | -11.22% | -0.738 | 0.931 | 1.420 | -3.73% |
| LARGE_GROWTH | IWF | technology_and_growth | -0.43% | -0.40% | -2.72% | 21.10% | -11.35% | -0.908 | 0.936 | 1.286 | -4.34% |
| LARGE_VALUE | IWD | diversified_us_equity | -0.46% | -0.50% | 3.79% | 11.61% | -2.40% | -0.601 | 0.805 | 0.706 | -0.76% |
| MID_CAP | IJH | diversified_us_equity | -0.68% | -0.33% | -3.76% | 14.27% | -3.09% | -0.843 | 0.808 | 0.980 | -1.82% |
| SMALL_CAP | IWM | diversified_us_equity | -0.25% | -0.71% | 2.34% | 17.54% | -3.95% | -1.091 | 0.819 | 1.213 | -1.59% |
| SMALL_VALUE | IWN | diversified_us_equity | -0.23% | -1.79% | 2.07% | 14.20% | -2.75% | -0.532 | 0.734 | 0.960 | -1.31% |
| DIVIDEND | SCHD | diversified_us_equity | 0.70% | 1.96% | -3.30% | 11.74% | -2.95% | 0.218 | 0.284 | 0.243 | -0.03% |
| LOW_VOL | SPLV | diversified_us_equity | 0.50% | -3.50% | -7.68% | 12.82% | -3.75% | -0.674 | 0.018 | 0.015 | -2.49% |
| MOMENTUM | MTUM | diversified_us_equity | 1.13% | -0.39% | 11.25% | 38.71% | -17.99% | 0.470 | 0.773 | 1.567 | -9.68% |
| TECHNOLOGY | XLK | technology_and_growth | -0.25% | 2.22% | 17.03% | 35.30% | -15.86% | -1.011 | 0.858 | 1.736 | -6.24% |
| COMMUNICATIONS | XLC | technology_and_growth | -0.71% | -3.71% | -11.84% | 19.52% | -9.68% | -0.507 | 0.579 | 0.678 | -7.46% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | -2.42% | -1.89% | -10.09% | 21.92% | -10.72% | -0.771 | 0.777 | 1.171 | -6.18% |
| CONSUMER_STAPLES | XLP | consumer_defensive | 1.05% | -2.57% | -11.83% | 17.17% | -4.95% | -0.757 | -0.068 | -0.075 | -3.72% |
| HEALTHCARE | XLV | healthcare_and_biotech | 1.02% | 3.16% | -7.19% | 18.26% | -3.74% | -0.747 | 0.221 | 0.266 | 0.00% |
| FINANCIALS | XLF | financials | 0.07% | -0.21% | -0.97% | 13.23% | -2.08% | -0.914 | 0.543 | 0.614 | -0.72% |
| INDUSTRIALS | XLI | industrials_and_defense | -1.15% | -0.36% | -6.98% | 18.51% | -4.80% | -1.042 | 0.719 | 0.953 | -1.58% |
| ENERGY | XLE | energy | 4.51% | 6.49% | 0.03% | 24.05% | -13.21% | -0.895 | -0.163 | -0.275 | 0.00% |
| MATERIALS | XLB | materials_and_mining | -2.74% | 0.08% | -13.54% | 19.68% | -4.75% | -0.486 | 0.536 | 0.738 | -2.74% |
| UTILITIES | XLU | rate_sensitive_defensive | 0.89% | -5.46% | -11.06% | 15.58% | -6.83% | -0.450 | 0.125 | 0.145 | -6.54% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | 1.25% | -4.74% | -4.72% | 15.91% | -4.19% | -0.425 | 0.246 | 0.272 | -3.00% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | 0.06% | -4.05% | -11.15% | 4.86% | -2.00% | -0.236 | 0.297 | 0.106 | -3.29% |
| LONG_TREASURY | TLT | rates_and_duration | -0.64% | -5.68% | -14.15% | 9.10% | -6.26% | 0.170 | 0.243 | 0.175 | -8.03% |
| TIPS | TIP | rates_and_duration | 0.12% | -3.64% | -9.52% | 3.42% | -1.40% | -0.363 | 0.281 | 0.072 | -1.15% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | -0.14% | -5.03% | -10.23% | 5.61% | -3.31% | -0.419 | 0.483 | 0.202 | -3.47% |
| HIGH_YIELD_CREDIT | HYG | credit | 0.03% | -3.12% | -8.19% | 3.30% | -0.80% | -0.643 | 0.783 | 0.235 | -0.33% |
| AGGREGATE_BONDS | AGG | rates_and_duration | 0.03% | -4.22% | -9.69% | 4.30% | -1.82% | -0.273 | 0.400 | 0.119 | -2.39% |
| DEVELOPED_EX_US | VEA | international_equity | -0.41% | 1.15% | -7.60% | 19.38% | -4.85% | -0.931 | 0.803 | 1.083 | -1.76% |
| EMERGING_MARKETS | VWO | international_equity | -0.80% | -0.47% | -8.89% | 19.45% | -7.05% | -0.739 | 0.812 | 1.111 | -2.61% |
| EUROPE | VGK | international_equity | -0.81% | 0.98% | -9.17% | 14.84% | -3.12% | -0.796 | 0.747 | 0.918 | -1.13% |
| JAPAN | EWJ | international_equity | -0.95% | 2.05% | -10.29% | 23.79% | -7.86% | -0.998 | 0.721 | 1.182 | -3.15% |
| CHINA | MCHI | international_equity | -1.29% | -1.90% | -19.44% | 18.82% | -11.15% | -0.563 | 0.543 | 0.857 | -16.50% |
| INDIA | INDA | international_equity | -1.42% | -1.71% | -18.11% | 13.50% | -4.59% | -0.603 | 0.547 | 0.643 | -10.69% |
| GOLD | IAU | precious_metals | -0.57% | 5.02% | -27.19% | 24.98% | -12.78% | -0.479 | 0.313 | 0.690 | -19.55% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | 1.62% | 1.30% | 14.62% | 22.33% | -16.24% | -0.371 | -0.175 | -0.274 | -3.75% |
| SEMICONDUCTORS | SMH | technology_and_growth | -0.55% | -1.46% | 27.88% | 54.00% | -24.62% | 0.282 | 0.784 | 2.380 | -14.82% |
| SOFTWARE | IGV | technology_and_growth | -1.89% | 6.24% | 5.62% | 35.44% | -21.29% | -0.848 | 0.510 | 1.190 | -13.42% |
| BROAD_AI_TECH | AIQ | technology_and_growth | -1.06% | 2.31% | 11.51% | 39.72% | -20.19% | -0.493 | 0.850 | 1.918 | -10.85% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | -1.17% | 0.93% | -10.67% | 38.79% | -23.82% | -0.692 | 0.796 | 2.178 | -11.83% |
| CYBERSECURITY | CIBR | technology_and_growth | -2.48% | 2.74% | 31.16% | 32.56% | -11.74% | -0.349 | 0.540 | 1.109 | -4.66% |
| SOLAR | TAN | clean_energy | -5.37% | -14.04% | -13.67% | 45.79% | -35.51% | -0.287 | 0.602 | 1.870 | -32.54% |
| METALS_MINING | XME | materials_and_mining | -3.56% | 12.84% | -24.23% | 41.48% | -26.49% | -0.316 | 0.598 | 1.746 | -14.40% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | -0.41% | -1.22% | -1.27% | 11.25% | -2.04% | -0.884 | 0.774 | 0.702 | -1.34% |
| BIOTECH | XBI | healthcare_and_biotech | 1.29% | 2.66% | 11.98% | 29.15% | -10.51% | -0.636 | 0.476 | 1.000 | -2.54% |
| REGIONAL_BANKS | KRE | financials | 0.05% | -3.21% | -0.41% | 18.98% | -3.73% | -0.888 | 0.433 | 0.758 | -1.39% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | 0.10% | 3.24% | -6.75% | 25.96% | -8.58% | -0.386 | 0.562 | 1.006 | -0.42% |
| CANADA | EWC | international_equity | 0.11% | 1.63% | -3.82% | 11.76% | -3.20% | -0.336 | 0.674 | 0.746 | -1.04% |
| UNITED_KINGDOM | EWU | international_equity | -0.29% | 0.40% | -10.02% | 13.13% | -3.40% | -0.539 | 0.603 | 0.700 | -1.07% |
| AUSTRALIA | EWA | international_equity | -1.14% | -0.60% | -9.58% | 16.69% | -4.78% | -0.835 | 0.663 | 0.910 | -2.63% |
| SOUTH_KOREA | EWY | international_equity | 1.68% | 1.00% | 15.37% | 80.60% | -34.21% | 0.104 | 0.641 | 2.773 | -22.42% |
| TAIWAN | EWT | international_equity | 0.43% | 5.39% | 22.37% | 43.79% | -19.83% | -0.658 | 0.760 | 1.853 | -6.40% |
| BRAZIL | EWZ | international_equity | -0.82% | -8.43% | -14.35% | 21.61% | -8.97% | -0.771 | 0.505 | 0.985 | -18.47% |
| MEXICO | EWW | international_equity | -2.33% | -4.26% | -14.91% | 18.79% | -6.47% | -0.401 | 0.546 | 0.932 | -6.99% |
| SOUTH_AFRICA | EZA | international_equity | -2.17% | 1.85% | -24.14% | 30.73% | -12.74% | -0.592 | 0.623 | 1.579 | -15.97% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | 0.05% | -3.57% | -10.41% | 4.72% | -1.85% | -0.172 | 0.400 | 0.137 | -1.89% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | -0.53% | -4.12% | -9.71% | 3.11% | -2.15% | 1.167 | 0.389 | 0.090 | -1.78% |
| EMERGING_MARKET_BONDS | EMB | credit | -0.20% | -3.75% | -9.42% | 5.50% | -1.96% | -0.650 | 0.687 | 0.306 | -1.41% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | -0.48% | -3.65% | -10.34% | 3.72% | -1.45% | -0.695 | 0.467 | 0.129 | -1.92% |
| SILVER | SLV | precious_metals | -1.90% | 9.25% | -32.44% | 44.08% | -27.95% | -0.532 | 0.356 | 1.712 | -45.61% |
| COPPER | CPER | non_energy_commodities | -2.59% | -1.44% | 0.71% | 25.80% | -10.57% | -0.415 | 0.547 | 1.198 | -4.09% |
| AGRICULTURE | DBA | non_energy_commodities | 1.59% | -3.38% | -0.27% | 13.22% | -7.21% | -0.613 | 0.081 | 0.069 | -2.44% |
| OIL | USO | energy | 2.39% | 0.69% | 56.48% | 53.63% | -32.49% | -0.569 | -0.336 | -1.252 | -14.58% |
| US_DOLLAR | UUP | currencies | 0.00% | -4.30% | -3.75% | 4.82% | -1.85% | -0.487 | -0.311 | -0.138 | -1.61% |
| EURO | FXE | currencies | 0.30% | -1.94% | -12.61% | 4.67% | -2.66% | -0.813 | 0.292 | 0.129 | -3.40% |
| YEN | FXY | currencies | -0.26% | -1.61% | -15.12% | 7.58% | -3.11% | 1.476 | 0.181 | 0.115 | -8.50% |
| BITCOIN_ETF | IBIT | crypto_assets | 1.84% | -4.20% | -13.16% | 35.49% | -24.34% | -0.659 | 0.504 | 1.727 | -48.66% |
| ETHEREUM_ETF | ETHA | crypto_assets | 1.83% | -2.65% | -14.04% | 51.49% | -27.31% | -0.508 | 0.530 | 2.709 | -60.54% |
