# Full-Universe Horizon-Specific Decision Context

Profile: weekly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: yahoo_chart_adjusted_close_and_reported_volume
- As-of date requested: 2026-07-24
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | -0.59% |
| spy_return_21s | 0.78% |
| rsp_return_5s | 0.09% |
| rsp_return_21s | 1.52% |
| hyg_return_5s | -0.53% |
| hyg_return_21s | -0.32% |
| tlt_return_5s | -1.50% |
| tlt_return_21s | -4.37% |
| uup_return_5s | 0.88% |
| uup_return_21s | 0.18% |
| uso_return_5s | 10.27% |
| uso_return_21s | 28.60% |
| iau_return_5s | 0.97% |
| iau_return_21s | 1.65% |
| rsp_minus_spy_5s | 0.68% |
| rsp_minus_spy_21s | 0.74% |
| positive_asset_share_5s | 49.28% |
| positive_asset_share_21s | 55.07% |
| active_return_dispersion_5s | 2.28% |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_3s | active_return_5s | prior_16s_active_return | volatility_21s | max_drawdown_21s | volume_zscore_5v60 | corr_spy_63s | beta_spy_63s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | 0.59% | -1.37% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.05% | 0.65% | -1.12% | 0.24% | -0.01% | -0.948 | -0.176 | -0.003 | 0.00% |
| SP500 | SPY | diversified_us_equity | -1.25% | 0.00% | 0.00% | 11.37% | -2.22% | -0.659 | 1.000 | 1.000 | -2.47% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | -1.26% | -0.02% | -0.16% | 10.43% | -2.15% | -0.915 | 0.992 | 0.988 | -2.27% |
| NASDAQ100 | QQQ | technology_and_growth | -3.49% | -1.01% | -3.52% | 23.34% | -7.08% | -0.657 | 0.916 | 1.730 | -8.20% |
| LARGE_GROWTH | IWF | technology_and_growth | -3.03% | -0.86% | -1.61% | 22.20% | -5.25% | 0.194 | 0.886 | 1.281 | -8.56% |
| LARGE_VALUE | IWD | diversified_us_equity | 0.32% | 0.67% | 1.55% | 10.07% | -1.31% | 0.194 | 0.715 | 0.650 | -0.49% |
| MID_CAP | IJH | diversified_us_equity | 0.07% | 0.89% | -1.66% | 11.33% | -3.09% | -0.722 | 0.784 | 0.874 | -1.74% |
| SMALL_CAP | IWM | diversified_us_equity | -1.81% | -0.39% | -2.26% | 11.23% | -3.09% | -0.815 | 0.779 | 1.097 | -3.09% |
| SMALL_VALUE | IWN | diversified_us_equity | -0.67% | 0.17% | 0.34% | 10.32% | -1.83% | -0.563 | 0.677 | 0.797 | -1.23% |
| DIVIDEND | SCHD | diversified_us_equity | 1.43% | 1.74% | 2.38% | 13.40% | -1.18% | -0.493 | 0.119 | 0.110 | 0.00% |
| LOW_VOL | SPLV | diversified_us_equity | 1.93% | 1.58% | 1.15% | 14.64% | -1.89% | -1.175 | -0.296 | -0.297 | 0.00% |
| MOMENTUM | MTUM | diversified_us_equity | -2.57% | 2.01% | -9.39% | 40.22% | -11.88% | -0.305 | 0.748 | 2.099 | -11.25% |
| TECHNOLOGY | XLK | technology_and_growth | -2.71% | 0.75% | -5.45% | 30.12% | -7.84% | -1.296 | 0.836 | 2.134 | -11.16% |
| COMMUNICATIONS | XLC | technology_and_growth | -3.39% | -3.34% | 2.49% | 21.17% | -7.06% | -0.031 | 0.463 | 0.595 | -10.96% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | -4.75% | -4.64% | -1.05% | 23.07% | -7.90% | 0.173 | 0.740 | 1.166 | -11.78% |
| CONSUMER_STAPLES | XLP | consumer_defensive | 0.08% | -0.66% | -0.48% | 18.88% | -3.03% | -1.222 | -0.279 | -0.352 | -5.35% |
| HEALTHCARE | XLV | healthcare_and_biotech | 1.45% | 1.51% | 3.68% | 21.74% | -3.74% | -1.493 | -0.133 | -0.186 | -1.14% |
| FINANCIALS | XLF | financials | 0.36% | 0.68% | 3.36% | 13.78% | -2.08% | -0.795 | 0.181 | 0.181 | -0.78% |
| INDUSTRIALS | XLI | industrials_and_defense | 2.24% | 2.40% | -1.81% | 16.17% | -4.01% | -1.125 | 0.617 | 0.903 | -1.56% |
| ENERGY | XLE | energy | 1.91% | 3.95% | 6.30% | 18.00% | -2.37% | -0.702 | -0.379 | -0.698 | -4.01% |
| MATERIALS | XLB | materials_and_mining | 2.32% | 2.03% | -2.60% | 18.80% | -3.81% | -0.231 | 0.534 | 0.809 | -3.62% |
| UTILITIES | XLU | rate_sensitive_defensive | 3.05% | 3.07% | -2.18% | 16.13% | -3.10% | -0.833 | -0.068 | -0.089 | -1.72% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | 1.66% | 1.75% | 0.67% | 17.04% | -2.67% | -0.765 | -0.086 | -0.107 | 0.00% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | -0.30% | -0.28% | -1.98% | 4.00% | -2.00% | -1.075 | 0.523 | 0.199 | -3.52% |
| LONG_TREASURY | TLT | rates_and_duration | -0.49% | -0.92% | -4.29% | 6.60% | -4.54% | -0.697 | 0.394 | 0.265 | -6.61% |
| TIPS | TIP | rates_and_duration | -0.35% | -0.12% | -1.36% | 3.01% | -1.24% | -0.363 | 0.553 | 0.150 | -1.43% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | -0.58% | -0.65% | -2.72% | 4.41% | -2.82% | 0.075 | 0.559 | 0.225 | -3.12% |
| HIGH_YIELD_CREDIT | HYG | credit | -0.53% | 0.06% | -1.16% | 2.48% | -0.80% | -0.114 | 0.770 | 0.215 | -0.80% |
| AGGREGATE_BONDS | AGG | rates_and_duration | -0.29% | -0.17% | -2.04% | 3.27% | -1.71% | -0.631 | 0.561 | 0.176 | -2.28% |
| DEVELOPED_EX_US | VEA | international_equity | -1.08% | 0.60% | -2.20% | 16.24% | -3.70% | -0.831 | 0.838 | 1.326 | -3.70% |
| EMERGING_MARKETS | VWO | international_equity | -1.80% | 0.52% | -3.29% | 17.01% | -3.78% | -0.866 | 0.869 | 1.360 | -5.62% |
| EUROPE | VGK | international_equity | -0.39% | 0.38% | 0.52% | 14.45% | -2.53% | -0.292 | 0.729 | 1.008 | -1.73% |
| JAPAN | EWJ | international_equity | -1.65% | 1.38% | -3.66% | 20.57% | -5.08% | -0.811 | 0.794 | 1.343 | -5.94% |
| CHINA | MCHI | international_equity | -1.24% | 1.30% | 1.58% | 19.50% | -2.22% | -0.439 | 0.501 | 0.797 | -18.88% |
| INDIA | INDA | international_equity | -1.56% | -1.23% | -2.82% | 11.84% | -4.51% | 0.308 | 0.584 | 0.686 | -13.15% |
| GOLD | IAU | precious_metals | -0.77% | 1.55% | -0.69% | 20.97% | -4.47% | -0.279 | 0.686 | 1.258 | -24.95% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | 1.70% | 4.64% | 7.94% | 18.75% | -2.05% | -0.296 | -0.128 | -0.203 | -5.08% |
| SEMICONDUCTORS | SMH | technology_and_growth | -3.92% | 1.42% | -11.45% | 50.44% | -15.15% | -0.498 | 0.784 | 3.200 | -16.10% |
| SOFTWARE | IGV | technology_and_growth | -4.18% | -4.61% | 6.32% | 27.76% | -8.11% | -0.804 | 0.341 | 0.862 | -25.29% |
| BROAD_AI_TECH | AIQ | technology_and_growth | -4.95% | -0.64% | -8.77% | 34.02% | -11.63% | -0.785 | 0.821 | 2.476 | -17.34% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | -5.07% | -1.24% | -7.88% | 33.40% | -13.77% | -0.916 | 0.845 | 2.496 | -20.72% |
| CYBERSECURITY | CIBR | technology_and_growth | -2.41% | -3.70% | 8.94% | 28.57% | -7.40% | -0.140 | 0.432 | 1.068 | -6.68% |
| SOLAR | TAN | clean_energy | -4.58% | -4.27% | -8.70% | 36.25% | -13.31% | -1.355 | 0.743 | 2.554 | -30.64% |
| METALS_MINING | XME | materials_and_mining | 0.14% | 4.03% | -9.64% | 30.06% | -10.12% | -0.306 | 0.678 | 2.069 | -23.35% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | 0.38% | 0.68% | 0.05% | 9.87% | -1.46% | -1.257 | 0.715 | 0.594 | -0.69% |
| BIOTECH | XBI | healthcare_and_biotech | -2.60% | -1.86% | 1.67% | 28.09% | -8.40% | -0.701 | 0.348 | 0.812 | -8.40% |
| REGIONAL_BANKS | KRE | financials | -0.33% | -0.67% | 2.31% | 19.62% | -3.73% | -0.281 | 0.175 | 0.276 | -2.81% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | 4.53% | 4.66% | -3.68% | 21.67% | -8.58% | -0.510 | 0.433 | 0.831 | -4.24% |
| CANADA | EWC | international_equity | 0.03% | -0.05% | 2.40% | 8.97% | -1.46% | 0.021 | 0.604 | 0.608 | -0.71% |
| UNITED_KINGDOM | EWU | international_equity | 0.98% | 1.20% | 1.91% | 14.80% | -1.93% | -0.643 | 0.485 | 0.630 | -1.59% |
| AUSTRALIA | EWA | international_equity | 0.14% | 0.48% | 1.64% | 12.62% | -1.63% | -0.697 | 0.613 | 0.862 | -3.76% |
| SOUTH_KOREA | EWY | international_equity | -5.75% | 0.84% | -18.97% | 67.57% | -20.71% | -0.275 | 0.714 | 4.276 | -25.66% |
| TAIWAN | EWT | international_equity | -2.56% | 1.29% | -8.43% | 39.81% | -11.67% | -0.129 | 0.788 | 2.546 | -12.12% |
| BRAZIL | EWZ | international_equity | 0.31% | 2.01% | 2.71% | 21.32% | -2.43% | -0.911 | 0.426 | 0.775 | -13.56% |
| MEXICO | EWW | international_equity | -0.51% | 1.04% | 0.42% | 17.74% | -2.98% | -0.636 | 0.634 | 1.000 | -5.75% |
| SOUTH_AFRICA | EZA | international_equity | -1.94% | -1.48% | -1.08% | 23.20% | -6.50% | 0.717 | 0.777 | 1.961 | -23.52% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | -0.32% | -0.13% | -2.04% | 4.02% | -1.85% | -0.559 | 0.566 | 0.209 | -2.22% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | -0.58% | -0.38% | -1.92% | 3.12% | -2.15% | 2.240 | 0.577 | 0.133 | -1.88% |
| EMERGING_MARKET_BONDS | EMB | credit | -0.78% | -0.35% | -2.04% | 4.19% | -1.96% | -0.630 | 0.742 | 0.327 | -1.84% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | -0.06% | 0.32% | -2.32% | 3.25% | -1.44% | -0.816 | 0.543 | 0.175 | -1.73% |
| SILVER | SLV | precious_metals | -0.92% | 4.15% | -3.30% | 36.55% | -10.19% | -0.962 | 0.649 | 2.507 | -50.20% |
| COPPER | CPER | non_energy_commodities | -2.99% | 1.72% | 3.06% | 21.55% | -3.26% | -0.606 | 0.717 | 1.602 | -5.54% |
| AGRICULTURE | DBA | non_energy_commodities | 0.32% | 2.02% | 3.45% | 14.56% | -1.52% | -1.021 | 0.029 | 0.029 | -1.71% |
| OIL | USO | energy | 6.08% | 10.86% | 15.25% | 47.91% | -5.53% | 0.079 | -0.322 | -1.266 | -10.64% |
| US_DOLLAR | UUP | currencies | 0.35% | 1.47% | -2.07% | 4.46% | -0.98% | -0.943 | -0.536 | -0.201 | 0.00% |
| EURO | FXE | currencies | -0.27% | -0.04% | -0.50% | 3.97% | -0.81% | -0.723 | 0.576 | 0.205 | -5.18% |
| YEN | FXY | currencies | -0.32% | -0.25% | -1.71% | 5.40% | -1.65% | 0.505 | 0.204 | 0.102 | -10.79% |
| BITCOIN_ETF | IBIT | crypto_assets | -3.50% | 0.59% | 5.95% | 31.26% | -3.50% | -0.580 | 0.466 | 1.315 | -49.01% |
| ETHEREUM_ETF | ETHA | crypto_assets | -3.37% | 1.52% | 15.32% | 44.99% | -4.20% | 0.188 | 0.571 | 2.279 | -61.63% |
