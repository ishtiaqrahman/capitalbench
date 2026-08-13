# Full-Universe Horizon-Specific Decision Context

Profile: weekly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: yahoo_chart_adjusted_close_and_reported_volume
- As-of date requested: 2026-08-12
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | 0.35% |
| spy_return_21s | 2.75% |
| rsp_return_5s | 0.61% |
| rsp_return_21s | 3.57% |
| hyg_return_5s | 0.11% |
| hyg_return_21s | 0.36% |
| tlt_return_5s | -1.07% |
| tlt_return_21s | -1.95% |
| uup_return_5s | 0.39% |
| uup_return_21s | -0.67% |
| uso_return_5s | 10.81% |
| uso_return_21s | 5.93% |
| iau_return_5s | 3.92% |
| iau_return_21s | 8.80% |
| rsp_minus_spy_5s | 0.26% |
| rsp_minus_spy_21s | 0.83% |
| positive_asset_share_5s | 59.42% |
| positive_asset_share_21s | 72.46% |
| active_return_dispersion_5s | 2.44% |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_3s | active_return_5s | prior_16s_active_return | volatility_21s | max_drawdown_21s | volume_zscore_5v60 | corr_spy_63s | beta_spy_63s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | -0.35% | -2.39% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.03% | -0.26% | -2.18% | 0.17% | 0.00% | -0.658 | -0.132 | -0.002 | 0.00% |
| SP500 | SPY | diversified_us_equity | -0.10% | 0.00% | 0.00% | 13.73% | -3.36% | -1.110 | 1.000 | 1.000 | -0.10% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | 0.01% | 0.22% | -0.10% | 13.71% | -3.22% | 0.053 | 0.993 | 0.989 | 0.00% |
| NASDAQ100 | QQQ | technology_and_growth | 0.09% | 0.54% | -2.72% | 24.53% | -8.05% | -1.086 | 0.923 | 1.711 | -2.90% |
| LARGE_GROWTH | IWF | technology_and_growth | -0.14% | 0.08% | -1.91% | 23.79% | -7.99% | -0.849 | 0.898 | 1.351 | -3.29% |
| LARGE_VALUE | IWD | diversified_us_equity | 0.08% | 0.29% | 1.37% | 9.84% | -1.31% | -0.480 | 0.727 | 0.603 | -0.21% |
| MID_CAP | IJH | diversified_us_equity | 0.35% | 1.03% | -0.63% | 12.90% | -1.71% | -0.961 | 0.787 | 0.817 | 0.00% |
| SMALL_CAP | IWM | diversified_us_equity | 0.38% | 0.63% | -0.60% | 15.09% | -2.69% | -1.380 | 0.787 | 1.021 | 0.00% |
| SMALL_VALUE | IWN | diversified_us_equity | 0.18% | 0.03% | 0.11% | 12.47% | -1.61% | -0.897 | 0.660 | 0.691 | -0.46% |
| DIVIDEND | SCHD | diversified_us_equity | 1.06% | 1.49% | 2.08% | 12.23% | -1.42% | 0.050 | 0.083 | 0.070 | -0.03% |
| LOW_VOL | SPLV | diversified_us_equity | -0.51% | -1.02% | -1.10% | 11.86% | -2.98% | -0.322 | -0.284 | -0.270 | -2.76% |
| MOMENTUM | MTUM | diversified_us_equity | 1.75% | 1.18% | -5.45% | 37.23% | -11.46% | -0.741 | 0.731 | 2.024 | -8.83% |
| TECHNOLOGY | XLK | technology_and_growth | 0.47% | 1.24% | -1.14% | 34.12% | -9.29% | -1.360 | 0.844 | 2.135 | -4.60% |
| COMMUNICATIONS | XLC | technology_and_growth | -0.88% | -0.89% | -2.91% | 24.19% | -7.06% | -1.203 | 0.400 | 0.541 | -7.64% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | -1.64% | -0.98% | -1.19% | 29.61% | -7.31% | -1.643 | 0.675 | 1.159 | -4.95% |
| CONSUMER_STAPLES | XLP | consumer_defensive | -0.05% | -0.64% | -0.10% | 17.56% | -3.06% | -1.519 | -0.335 | -0.405 | -4.29% |
| HEALTHCARE | XLV | healthcare_and_biotech | 1.67% | 2.26% | 1.32% | 16.51% | -3.09% | -1.076 | -0.165 | -0.215 | 0.00% |
| FINANCIALS | XLF | financials | 0.56% | -0.49% | 0.85% | 10.80% | -1.62% | -1.686 | 0.284 | 0.274 | -0.14% |
| INDUSTRIALS | XLI | industrials_and_defense | 0.38% | -0.60% | 0.50% | 19.11% | -3.57% | -1.715 | 0.652 | 0.907 | -0.28% |
| ENERGY | XLE | energy | 6.14% | 6.14% | -1.76% | 24.39% | -3.87% | -1.015 | -0.347 | -0.605 | -1.74% |
| MATERIALS | XLB | materials_and_mining | -0.53% | -0.46% | 1.05% | 17.87% | -2.54% | -0.184 | 0.455 | 0.658 | -1.24% |
| UTILITIES | XLU | rate_sensitive_defensive | 0.53% | 0.06% | -6.83% | 14.19% | -6.83% | 0.166 | -0.071 | -0.083 | -6.92% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | -1.09% | -1.92% | -0.77% | 14.31% | -4.19% | -0.170 | -0.159 | -0.184 | -3.30% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | -0.23% | -0.73% | -2.02% | 4.63% | -1.05% | 3.424 | 0.513 | 0.186 | -3.26% |
| LONG_TREASURY | TLT | rates_and_duration | -0.79% | -1.42% | -3.28% | 9.11% | -2.69% | 1.741 | 0.406 | 0.269 | -7.52% |
| TIPS | TIP | rates_and_duration | -0.15% | -0.43% | -2.60% | 2.40% | -0.81% | -0.547 | 0.489 | 0.119 | -1.24% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | -0.40% | -0.93% | -3.29% | 5.77% | -1.62% | -0.300 | 0.577 | 0.230 | -3.22% |
| HIGH_YIELD_CREDIT | HYG | credit | 0.00% | -0.24% | -2.14% | 3.37% | -0.73% | -1.015 | 0.793 | 0.202 | 0.00% |
| AGGREGATE_BONDS | AGG | rates_and_duration | -0.17% | -0.64% | -2.87% | 4.41% | -0.98% | -0.248 | 0.536 | 0.166 | -2.31% |
| DEVELOPED_EX_US | VEA | international_equity | 0.56% | 0.96% | 0.09% | 16.81% | -2.64% | 0.075 | 0.818 | 1.151 | 0.00% |
| EMERGING_MARKETS | VWO | international_equity | -0.10% | 0.32% | -0.81% | 16.65% | -4.30% | -0.615 | 0.863 | 1.238 | -1.36% |
| EUROPE | VGK | international_equity | -0.38% | 0.08% | 1.50% | 11.66% | -1.60% | -0.794 | 0.698 | 0.770 | -0.38% |
| JAPAN | EWJ | international_equity | 0.92% | 2.41% | -1.04% | 24.51% | -4.84% | -1.370 | 0.743 | 1.242 | 0.00% |
| CHINA | MCHI | international_equity | -2.63% | -2.01% | 2.83% | 18.21% | -3.25% | -0.430 | 0.404 | 0.603 | -16.22% |
| INDIA | INDA | international_equity | -0.83% | -1.07% | 0.85% | 12.18% | -2.62% | -1.358 | 0.622 | 0.611 | -9.66% |
| GOLD | IAU | precious_metals | 1.59% | 3.57% | 2.31% | 23.12% | -2.56% | -0.149 | 0.539 | 0.964 | -18.30% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | 4.17% | 5.48% | -2.97% | 26.11% | -6.42% | 0.021 | -0.195 | -0.309 | -4.97% |
| SEMICONDUCTORS | SMH | technology_and_growth | 0.37% | 2.31% | -7.49% | 48.61% | -16.01% | -1.071 | 0.772 | 2.998 | -12.57% |
| SOFTWARE | IGV | technology_and_growth | 0.38% | 1.40% | 5.81% | 31.92% | -7.28% | -0.925 | 0.442 | 1.103 | -12.47% |
| BROAD_AI_TECH | AIQ | technology_and_growth | 0.66% | 1.91% | -4.09% | 38.14% | -11.76% | -1.075 | 0.839 | 2.445 | -9.08% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | 0.84% | 4.98% | -2.29% | 38.22% | -10.40% | -0.608 | 0.871 | 2.418 | -10.35% |
| CYBERSECURITY | CIBR | technology_and_growth | 2.60% | 2.54% | 0.61% | 26.08% | -7.40% | -0.470 | 0.538 | 1.247 | -0.21% |
| SOLAR | TAN | clean_energy | -0.80% | 1.72% | -9.39% | 42.74% | -14.55% | -0.827 | 0.746 | 2.500 | -29.22% |
| METALS_MINING | XME | materials_and_mining | 0.91% | 4.00% | 6.02% | 44.23% | -6.55% | -0.075 | 0.591 | 1.814 | -12.02% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | 0.45% | 0.26% | 0.55% | 10.46% | -1.46% | -1.268 | 0.698 | 0.554 | 0.00% |
| BIOTECH | XBI | healthcare_and_biotech | 1.28% | 3.82% | -3.96% | 26.33% | -5.90% | -0.611 | 0.362 | 0.783 | -2.98% |
| REGIONAL_BANKS | KRE | financials | 1.54% | -0.30% | 0.73% | 17.11% | -3.55% | -1.184 | 0.195 | 0.270 | -0.69% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | 0.35% | -0.61% | 2.89% | 26.48% | -4.32% | -1.089 | 0.470 | 0.872 | -0.26% |
| CANADA | EWC | international_equity | 0.77% | 1.28% | 0.31% | 10.78% | -1.46% | -0.574 | 0.592 | 0.513 | 0.00% |
| UNITED_KINGDOM | EWU | international_equity | -0.56% | -0.35% | 1.83% | 10.80% | -1.23% | 0.144 | 0.378 | 0.396 | -0.64% |
| AUSTRALIA | EWA | international_equity | -1.71% | -1.18% | 2.59% | 17.18% | -1.71% | -0.325 | 0.613 | 0.749 | -1.71% |
| SOUTH_KOREA | EWY | international_equity | 5.89% | 3.63% | -6.82% | 72.76% | -18.52% | -0.811 | 0.698 | 4.025 | -19.77% |
| TAIWAN | EWT | international_equity | 3.00% | 4.05% | -2.57% | 44.53% | -12.76% | -1.199 | 0.796 | 2.589 | -4.80% |
| BRAZIL | EWZ | international_equity | -4.19% | -6.58% | -2.17% | 22.51% | -7.61% | 0.135 | 0.395 | 0.665 | -18.09% |
| MEXICO | EWW | international_equity | -1.37% | -0.65% | -0.60% | 15.95% | -2.23% | -0.283 | 0.607 | 0.845 | -4.49% |
| SOUTH_AFRICA | EZA | international_equity | -1.90% | 1.86% | 3.25% | 25.52% | -5.31% | -0.729 | 0.730 | 1.605 | -14.43% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | -0.09% | -0.51% | -2.90% | 5.81% | -1.18% | -0.387 | 0.526 | 0.199 | -2.14% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | 0.04% | -0.20% | -3.13% | 4.02% | -1.58% | 0.226 | 0.554 | 0.133 | -1.21% |
| EMERGING_MARKET_BONDS | EMB | credit | -0.31% | -0.59% | -2.37% | 5.13% | -1.25% | -1.119 | 0.744 | 0.300 | -1.10% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | -0.27% | -0.70% | -2.45% | 3.32% | -0.77% | -0.660 | 0.511 | 0.149 | -1.69% |
| SILVER | SLV | precious_metals | 2.71% | 4.98% | 3.07% | 37.42% | -5.23% | -0.284 | 0.597 | 2.029 | -44.07% |
| COPPER | CPER | non_energy_commodities | 0.30% | -2.38% | 3.60% | 21.99% | -3.26% | -0.516 | 0.654 | 1.272 | -2.03% |
| AGRICULTURE | DBA | non_energy_commodities | 0.80% | 0.41% | -2.39% | 14.37% | -2.87% | -1.041 | 0.142 | 0.141 | -3.10% |
| OIL | USO | energy | 7.90% | 10.46% | -6.79% | 64.64% | -17.64% | -0.506 | -0.349 | -1.344 | -16.78% |
| US_DOLLAR | UUP | currencies | 0.46% | 0.04% | -3.45% | 5.52% | -1.85% | -0.380 | -0.415 | -0.148 | -1.40% |
| EURO | FXE | currencies | -0.32% | -0.59% | -1.17% | 4.45% | -0.81% | -0.389 | 0.443 | 0.152 | -3.85% |
| YEN | FXY | currencies | -1.24% | -1.43% | 0.60% | 11.88% | -1.68% | 0.372 | 0.255 | 0.140 | -8.44% |
| BITCOIN_ETF | IBIT | crypto_assets | -2.47% | -2.66% | -1.95% | 21.69% | -5.39% | -0.688 | 0.456 | 1.185 | -49.66% |
| ETHEREUM_ETF | ETHA | crypto_assets | -2.14% | -2.56% | -0.27% | 33.09% | -4.35% | -0.690 | 0.537 | 2.029 | -61.30% |
