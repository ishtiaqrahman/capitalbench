# Full-Universe Horizon-Specific Decision Context

Profile: weekly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: tiingo_eod_adjusted_price_and_volume
- As-of date requested: 2026-08-06
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | 3.62% |
| spy_return_21s | 3.11% |
| rsp_return_5s | 1.49% |
| rsp_return_21s | 3.01% |
| hyg_return_5s | 0.47% |
| hyg_return_21s | 0.23% |
| tlt_return_5s | 0.06% |
| tlt_return_21s | -1.79% |
| uup_return_5s | 0.18% |
| uup_return_21s | -0.60% |
| uso_return_5s | -6.75% |
| uso_return_21s | 5.94% |
| iau_return_5s | 3.32% |
| iau_return_21s | 4.08% |
| rsp_minus_spy_5s | -2.14% |
| rsp_minus_spy_21s | -0.10% |
| positive_asset_share_5s | 78.26% |
| positive_asset_share_21s | 72.46% |
| active_return_dispersion_5s | 2.77% |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_3s | active_return_5s | prior_16s_active_return | volatility_21s | max_drawdown_21s | volume_zscore_5v60 | corr_spy_63s | beta_spy_63s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | -3.62% | 0.50% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.03% | -3.54% | 0.72% | 0.18% | 0.00% | 1.200 | -0.147 | -0.002 | 0.00% |
| SP500 | SPY | diversified_us_equity | 1.44% | 0.00% | 0.00% | 14.17% | -3.38% | 0.157 | 1.000 | 1.000 | -0.36% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | 1.40% | -0.13% | -0.04% | 14.12% | -3.29% | -0.249 | 0.993 | 0.988 | -0.46% |
| NASDAQ100 | QQQ | technology_and_growth | 2.08% | 0.93% | -3.42% | 25.93% | -8.79% | 0.007 | 0.921 | 1.723 | -4.12% |
| LARGE_GROWTH | IWF | technology_and_growth | 2.18% | 1.55% | -3.09% | 24.38% | -7.99% | -0.703 | 0.907 | 1.360 | -4.01% |
| LARGE_VALUE | IWD | diversified_us_equity | 0.74% | -1.46% | 2.74% | 9.15% | -1.31% | -0.353 | 0.717 | 0.594 | -0.20% |
| MID_CAP | IJH | diversified_us_equity | 0.84% | -1.76% | 1.33% | 12.88% | -1.71% | -0.451 | 0.795 | 0.818 | -0.94% |
| SMALL_CAP | IWM | diversified_us_equity | 0.69% | -1.69% | 0.19% | 15.48% | -2.92% | -0.662 | 0.784 | 1.031 | -1.15% |
| SMALL_VALUE | IWN | diversified_us_equity | -0.28% | -2.70% | 2.39% | 12.28% | -1.61% | 0.189 | 0.660 | 0.702 | -1.38% |
| DIVIDEND | SCHD | diversified_us_equity | 0.42% | -2.75% | 3.81% | 13.04% | -1.42% | 0.930 | 0.090 | 0.075 | -0.56% |
| LOW_VOL | SPLV | diversified_us_equity | 0.07% | -3.78% | 1.37% | 11.97% | -2.26% | -0.143 | -0.286 | -0.270 | -2.19% |
| MOMENTUM | MTUM | diversified_us_equity | 2.12% | -0.48% | -4.61% | 38.34% | -12.01% | 0.258 | 0.739 | 2.067 | -10.73% |
| TECHNOLOGY | XLK | technology_and_growth | 4.09% | 1.84% | -2.63% | 35.48% | -10.34% | -0.700 | 0.844 | 2.163 | -6.39% |
| COMMUNICATIONS | XLC | technology_and_growth | -0.14% | 0.69% | -2.13% | 24.32% | -7.06% | -0.398 | 0.390 | 0.527 | -6.87% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | -0.09% | 1.46% | -2.03% | 24.71% | -7.31% | 0.422 | 0.682 | 1.065 | -4.78% |
| CONSUMER_STAPLES | XLP | consumer_defensive | 0.29% | -4.04% | 1.78% | 19.35% | -3.03% | -0.405 | -0.335 | -0.411 | -4.25% |
| HEALTHCARE | XLV | healthcare_and_biotech | 1.36% | -3.05% | 1.25% | 17.58% | -3.09% | 0.554 | -0.183 | -0.241 | -1.68% |
| FINANCIALS | XLF | financials | 0.75% | -2.20% | 4.19% | 11.11% | -1.62% | -0.542 | 0.274 | 0.267 | -0.33% |
| INDUSTRIALS | XLI | industrials_and_defense | 0.87% | -0.05% | -0.63% | 17.42% | -3.57% | -0.023 | 0.667 | 0.911 | -0.88% |
| ENERGY | XLE | energy | -1.07% | -4.98% | 6.54% | 21.13% | -3.87% | -0.593 | -0.335 | -0.556 | -6.37% |
| MATERIALS | XLB | materials_and_mining | 2.27% | -2.60% | 3.45% | 18.78% | -3.65% | 0.639 | 0.472 | 0.691 | -1.91% |
| UTILITIES | XLU | rate_sensitive_defensive | -2.21% | -6.49% | -1.05% | 13.23% | -6.29% | 1.061 | -0.072 | -0.084 | -7.90% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | -0.82% | -4.70% | 3.10% | 13.18% | -2.61% | 0.821 | -0.169 | -0.191 | -2.61% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | 0.14% | -3.56% | 0.18% | 4.33% | -1.05% | -0.200 | 0.509 | 0.182 | -3.26% |
| LONG_TREASURY | TLT | rates_and_duration | 0.40% | -3.56% | -1.35% | 8.82% | -2.69% | 1.335 | 0.416 | 0.277 | -7.06% |
| TIPS | TIP | rates_and_duration | 0.01% | -3.70% | 0.21% | 2.31% | -0.81% | 0.550 | 0.498 | 0.123 | -1.28% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | 0.24% | -3.24% | -0.67% | 4.97% | -1.38% | 0.500 | 0.592 | 0.226 | -2.58% |
| HIGH_YIELD_CREDIT | HYG | credit | 0.19% | -3.15% | 0.26% | 2.93% | -0.73% | -0.001 | 0.784 | 0.199 | -0.11% |
| AGGREGATE_BONDS | AGG | rates_and_duration | 0.17% | -3.47% | 0.07% | 3.77% | -0.88% | 1.419 | 0.557 | 0.164 | -1.97% |
| DEVELOPED_EX_US | VEA | international_equity | 1.52% | -2.17% | 1.56% | 17.93% | -2.87% | -0.567 | 0.816 | 1.175 | -0.37% |
| EMERGING_MARKETS | VWO | international_equity | 1.52% | -0.58% | -1.16% | 17.88% | -4.96% | -0.234 | 0.854 | 1.238 | -2.09% |
| EUROPE | VGK | international_equity | 0.99% | -2.70% | 3.68% | 13.29% | -1.60% | -0.020 | 0.711 | 0.832 | -0.02% |
| JAPAN | EWJ | international_equity | 2.41% | -1.63% | 1.31% | 24.88% | -5.50% | -1.018 | 0.753 | 1.237 | -1.88% |
| CHINA | MCHI | international_equity | 0.01% | -2.89% | 5.51% | 16.19% | -2.22% | -0.103 | 0.404 | 0.582 | -14.96% |
| INDIA | INDA | international_equity | -0.08% | -2.78% | 2.66% | 12.84% | -3.39% | -0.444 | 0.552 | 0.605 | -9.35% |
| GOLD | IAU | precious_metals | 4.83% | -0.30% | 1.23% | 24.48% | -3.50% | 0.586 | 0.539 | 0.937 | -21.36% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | -0.12% | -5.17% | 5.79% | 25.97% | -6.42% | 0.547 | -0.190 | -0.298 | -8.88% |
| SEMICONDUCTORS | SMH | technology_and_growth | 4.77% | 2.42% | -8.63% | 50.65% | -17.48% | -0.621 | 0.778 | 3.058 | -14.57% |
| SOFTWARE | IGV | technology_and_growth | 2.05% | 2.93% | 1.40% | 29.94% | -7.28% | -0.829 | 0.421 | 1.041 | -15.58% |
| BROAD_AI_TECH | AIQ | technology_and_growth | 2.28% | 1.93% | -5.70% | 36.89% | -12.30% | -0.599 | 0.827 | 2.405 | -11.68% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | 3.86% | 4.47% | -7.44% | 37.66% | -12.14% | -0.285 | 0.875 | 2.447 | -14.34% |
| CYBERSECURITY | CIBR | technology_and_growth | 2.64% | 3.45% | -1.29% | 29.23% | -7.40% | -0.247 | 0.521 | 1.238 | -1.58% |
| SOLAR | TAN | clean_energy | 0.02% | -0.79% | -7.44% | 44.63% | -14.55% | 0.649 | 0.757 | 2.547 | -30.68% |
| METALS_MINING | XME | materials_and_mining | 7.02% | 4.71% | 0.42% | 40.27% | -6.55% | 0.434 | 0.676 | 1.999 | -16.87% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | 0.68% | -2.14% | 2.00% | 10.62% | -1.46% | -0.532 | 0.696 | 0.553 | -0.75% |
| BIOTECH | XBI | healthcare_and_biotech | 4.88% | -1.62% | -6.56% | 28.87% | -10.51% | -0.388 | 0.361 | 0.790 | -5.95% |
| REGIONAL_BANKS | KRE | financials | -0.74% | -2.85% | 3.99% | 17.58% | -3.55% | -0.539 | 0.198 | 0.280 | -1.84% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | 1.59% | 1.36% | -0.13% | 24.29% | -4.32% | -0.442 | 0.488 | 0.874 | -0.91% |
| CANADA | EWC | international_equity | 1.76% | -2.10% | 3.64% | 10.73% | -1.46% | 0.651 | 0.593 | 0.510 | -0.13% |
| UNITED_KINGDOM | EWU | international_equity | 0.15% | -4.40% | 5.21% | 11.65% | -1.23% | 0.369 | 0.415 | 0.463 | -0.78% |
| AUSTRALIA | EWA | international_equity | 2.59% | -2.48% | 6.54% | 16.72% | -1.61% | -0.209 | 0.607 | 0.756 | 0.00% |
| SOUTH_KOREA | EWY | international_equity | 2.42% | -1.82% | -11.27% | 77.83% | -21.94% | 0.014 | 0.706 | 4.166 | -25.13% |
| TAIWAN | EWT | international_equity | 4.08% | 4.87% | -9.03% | 44.82% | -15.80% | -0.277 | 0.796 | 2.539 | -8.56% |
| BRAZIL | EWZ | international_equity | -1.67% | -5.59% | 6.66% | 23.28% | -3.14% | -0.262 | 0.411 | 0.685 | -13.37% |
| MEXICO | EWW | international_equity | 0.10% | -4.25% | 3.71% | 16.54% | -2.23% | 1.363 | 0.602 | 0.826 | -4.28% |
| SOUTH_AFRICA | EZA | international_equity | 3.96% | 0.70% | 2.76% | 25.14% | -5.31% | -0.603 | 0.743 | 1.614 | -16.30% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | 0.31% | -3.56% | 0.07% | 4.89% | -1.01% | -0.011 | 0.555 | 0.196 | -1.96% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | 0.20% | -3.45% | -0.58% | 3.31% | -1.64% | 0.577 | 0.556 | 0.124 | -1.51% |
| EMERGING_MARKET_BONDS | EMB | credit | 0.21% | -3.02% | -0.55% | 5.35% | -1.52% | 0.223 | 0.747 | 0.302 | -1.09% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | 0.10% | -3.35% | 0.60% | 3.71% | -0.77% | -0.330 | 0.534 | 0.156 | -1.31% |
| SILVER | SLV | precious_metals | 6.46% | 0.77% | 1.77% | 37.84% | -6.93% | -0.665 | 0.574 | 2.009 | -47.11% |
| COPPER | CPER | non_energy_commodities | 2.83% | -0.01% | 6.62% | 21.22% | -3.26% | -0.312 | 0.659 | 1.330 | -0.22% |
| AGRICULTURE | DBA | non_energy_commodities | -1.30% | -3.80% | -0.01% | 13.37% | -2.87% | -0.552 | 0.141 | 0.141 | -4.52% |
| OIL | USO | energy | -2.66% | -10.38% | 14.11% | 67.91% | -17.64% | -0.350 | -0.350 | -1.330 | -22.29% |
| US_DOLLAR | UUP | currencies | 0.07% | -3.45% | -0.28% | 5.55% | -1.78% | 0.156 | -0.425 | -0.150 | -1.43% |
| EURO | FXE | currencies | 0.10% | -3.70% | 1.47% | 4.51% | -0.82% | -0.467 | 0.453 | 0.156 | -3.88% |
| YEN | FXY | currencies | -1.04% | -3.08% | 2.48% | 11.22% | -1.30% | 0.947 | 0.239 | 0.124 | -7.85% |
| BITCOIN_ETF | IBIT | crypto_assets | 0.91% | -4.20% | 4.67% | 27.44% | -5.39% | -0.278 | 0.454 | 1.189 | -48.81% |
| ETHEREUM_ETF | ETHA | crypto_assets | 2.06% | -4.38% | 11.18% | 39.16% | -4.35% | -0.148 | 0.544 | 2.059 | -60.64% |
