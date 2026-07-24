# Full-Universe Horizon-Specific Decision Context

Profile: weekly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: yahoo_chart_adjusted_close_and_reported_volume
- As-of date requested: 2026-07-23
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | -1.67% |
| spy_return_21s | 0.63% |
| rsp_return_5s | -1.46% |
| rsp_return_21s | 1.45% |
| hyg_return_5s | -0.71% |
| hyg_return_21s | -0.34% |
| tlt_return_5s | -1.24% |
| tlt_return_21s | -3.16% |
| uup_return_5s | 0.78% |
| uup_return_21s | 0.39% |
| uso_return_5s | 16.92% |
| uso_return_21s | 25.37% |
| iau_return_5s | 1.80% |
| iau_return_21s | -1.53% |
| rsp_minus_spy_5s | 0.21% |
| rsp_minus_spy_21s | 0.82% |
| positive_asset_share_5s | 30.43% |
| positive_asset_share_21s | 49.28% |
| active_return_dispersion_5s | 3.25% |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_3s | active_return_5s | prior_16s_active_return | volatility_21s | max_drawdown_21s | volume_zscore_5v60 | corr_spy_63s | beta_spy_63s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | 1.67% | -2.34% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.02% | 1.73% | -2.10% | 0.23% | -0.01% | -0.368 | -0.184 | -0.003 | 0.00% |
| SP500 | SPY | diversified_us_equity | -0.53% | 0.00% | 0.00% | 11.37% | -2.22% | -0.394 | 1.000 | 1.000 | -2.57% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | -0.43% | 0.08% | -0.15% | 10.43% | -2.15% | -0.796 | 0.992 | 0.988 | -2.30% |
| NASDAQ100 | QQQ | technology_and_growth | -0.59% | -0.31% | -3.42% | 23.11% | -6.03% | -0.477 | 0.921 | 1.729 | -7.16% |
| LARGE_GROWTH | IWF | technology_and_growth | -0.74% | -0.48% | -1.18% | 22.05% | -4.49% | 0.621 | 0.889 | 1.288 | -7.82% |
| LARGE_VALUE | IWD | diversified_us_equity | -0.32% | 0.36% | 1.20% | 9.76% | -1.31% | 0.194 | 0.713 | 0.644 | -1.31% |
| MID_CAP | IJH | diversified_us_equity | 0.69% | 0.96% | -1.42% | 11.43% | -3.09% | -0.615 | 0.783 | 0.871 | -2.15% |
| SMALL_CAP | IWM | diversified_us_equity | -0.08% | 0.49% | -2.25% | 11.36% | -2.78% | -0.542 | 0.780 | 1.096 | -2.78% |
| SMALL_VALUE | IWN | diversified_us_equity | -0.12% | 0.06% | 0.71% | 10.36% | -1.83% | -0.838 | 0.675 | 0.793 | -1.61% |
| DIVIDEND | SCHD | diversified_us_equity | 0.15% | 0.94% | 1.67% | 12.64% | -1.18% | -0.343 | 0.104 | 0.095 | -0.73% |
| LOW_VOL | SPLV | diversified_us_equity | 0.35% | 1.10% | 1.34% | 14.37% | -1.89% | -1.158 | -0.308 | -0.312 | -0.57% |
| MOMENTUM | MTUM | diversified_us_equity | 3.75% | 5.15% | -10.33% | 39.48% | -11.88% | 0.224 | 0.756 | 2.094 | -9.05% |
| TECHNOLOGY | XLK | technology_and_growth | 1.56% | 2.19% | -5.96% | 29.82% | -7.84% | -1.093 | 0.842 | 2.142 | -9.86% |
| COMMUNICATIONS | XLC | technology_and_growth | -4.89% | -4.78% | 2.68% | 21.05% | -7.06% | 0.146 | 0.467 | 0.594 | -11.73% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | -5.10% | -5.64% | 0.81% | 23.40% | -7.90% | 0.382 | 0.743 | 1.169 | -12.31% |
| CONSUMER_STAPLES | XLP | consumer_defensive | -1.94% | -1.36% | 0.16% | 18.71% | -3.03% | -0.759 | -0.290 | -0.369 | -6.39% |
| HEALTHCARE | XLV | healthcare_and_biotech | 1.38% | 1.45% | 3.98% | 21.76% | -3.74% | -1.375 | -0.131 | -0.182 | -1.82% |
| FINANCIALS | XLF | financials | -0.37% | 0.05% | 2.99% | 13.69% | -2.08% | -0.515 | 0.189 | 0.189 | -1.62% |
| INDUSTRIALS | XLI | industrials_and_defense | 2.14% | 2.66% | -1.21% | 16.57% | -4.01% | -0.862 | 0.594 | 0.880 | -1.95% |
| ENERGY | XLE | energy | 2.49% | 5.81% | 2.36% | 19.48% | -3.03% | -0.780 | -0.382 | -0.702 | -4.40% |
| MATERIALS | XLB | materials_and_mining | 0.52% | 0.49% | -2.30% | 17.61% | -3.81% | -0.436 | 0.542 | 0.804 | -5.44% |
| UTILITIES | XLU | rate_sensitive_defensive | 2.78% | 3.25% | -1.45% | 16.47% | -3.10% | -0.628 | -0.086 | -0.117 | -1.93% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | -0.62% | 0.55% | -0.50% | 15.34% | -2.67% | -0.888 | -0.099 | -0.120 | -1.12% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | -0.74% | 0.74% | -2.43% | 4.64% | -2.00% | -0.870 | 0.526 | 0.200 | -3.70% |
| LONG_TREASURY | TLT | rates_and_duration | -0.86% | 0.44% | -4.28% | 8.54% | -4.54% | -0.506 | 0.396 | 0.266 | -6.70% |
| TIPS | TIP | rates_and_duration | -0.52% | 1.23% | -2.22% | 3.34% | -1.24% | -0.237 | 0.542 | 0.147 | -1.44% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | -0.83% | 0.52% | -3.28% | 4.84% | -2.80% | 0.016 | 0.562 | 0.227 | -3.09% |
| HIGH_YIELD_CREDIT | HYG | credit | -0.56% | 0.96% | -1.96% | 2.48% | -0.80% | -0.137 | 0.772 | 0.216 | -0.80% |
| AGGREGATE_BONDS | AGG | rates_and_duration | -0.62% | 0.87% | -2.59% | 3.74% | -1.71% | -0.593 | 0.564 | 0.177 | -2.40% |
| DEVELOPED_EX_US | VEA | international_equity | 0.79% | 1.31% | -2.54% | 16.26% | -3.70% | -0.702 | 0.839 | 1.330 | -3.61% |
| EMERGING_MARKETS | VWO | international_equity | 0.29% | 0.41% | -3.21% | 17.06% | -3.71% | -0.565 | 0.869 | 1.369 | -5.13% |
| EUROPE | VGK | international_equity | 0.16% | 0.59% | -0.47% | 14.34% | -2.53% | -0.604 | 0.732 | 1.011 | -2.38% |
| JAPAN | EWJ | international_equity | 0.74% | 0.79% | -3.24% | 20.56% | -5.08% | -0.312 | 0.795 | 1.346 | -6.05% |
| CHINA | MCHI | international_equity | -1.35% | 0.21% | 2.16% | 19.75% | -2.57% | -0.476 | 0.505 | 0.811 | -18.85% |
| INDIA | INDA | international_equity | -1.89% | -0.51% | -3.11% | 12.22% | -4.51% | 0.134 | 0.590 | 0.694 | -13.85% |
| GOLD | IAU | precious_metals | 1.06% | 3.48% | -5.61% | 23.58% | -4.47% | -0.050 | 0.688 | 1.259 | -25.03% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | 3.91% | 8.16% | 2.48% | 21.24% | -2.47% | 3.745 | -0.136 | -0.217 | -4.49% |
| SEMICONDUCTORS | SMH | technology_and_growth | 3.82% | 3.65% | -10.88% | 49.36% | -15.15% | -0.293 | 0.787 | 3.178 | -13.27% |
| SOFTWARE | IGV | technology_and_growth | -6.32% | -5.37% | 4.97% | 27.98% | -8.11% | -0.956 | 0.344 | 0.921 | -26.04% |
| BROAD_AI_TECH | AIQ | technology_and_growth | 0.32% | 1.70% | -8.71% | 33.36% | -10.53% | -0.571 | 0.828 | 2.496 | -15.41% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | 0.19% | 0.58% | -8.84% | 32.93% | -12.16% | -0.911 | 0.852 | 2.503 | -18.75% |
| CYBERSECURITY | CIBR | technology_and_growth | -4.43% | -2.87% | 6.88% | 28.62% | -7.40% | -0.016 | 0.435 | 1.104 | -7.40% |
| SOLAR | TAN | clean_energy | 0.30% | -0.78% | -9.82% | 35.20% | -10.92% | -1.403 | 0.732 | 2.512 | -28.51% |
| METALS_MINING | XME | materials_and_mining | 5.56% | 5.89% | -13.08% | 31.69% | -11.87% | 0.015 | 0.680 | 2.094 | -22.28% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | -0.24% | 0.21% | 0.62% | 9.81% | -1.46% | -0.900 | 0.720 | 0.592 | -1.46% |
| BIOTECH | XBI | healthcare_and_biotech | 0.85% | 1.82% | 1.04% | 28.39% | -8.12% | -0.355 | 0.355 | 0.833 | -7.34% |
| REGIONAL_BANKS | KRE | financials | -0.98% | -1.88% | 4.23% | 19.83% | -3.73% | -0.079 | 0.168 | 0.264 | -3.55% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | 3.91% | 4.85% | -4.47% | 21.51% | -8.58% | -0.731 | 0.433 | 0.828 | -5.00% |
| CANADA | EWC | international_equity | 0.34% | 0.71% | 0.65% | 9.32% | -1.46% | 0.151 | 0.606 | 0.607 | -1.13% |
| UNITED_KINGDOM | EWU | international_equity | 0.67% | 1.10% | 0.74% | 14.46% | -1.93% | -0.601 | 0.491 | 0.635 | -2.69% |
| AUSTRALIA | EWA | international_equity | -0.11% | 1.18% | -0.16% | 12.51% | -1.63% | -0.633 | 0.617 | 0.863 | -4.53% |
| SOUTH_KOREA | EWY | international_equity | 6.75% | 8.10% | -17.34% | 65.53% | -20.71% | 0.198 | 0.726 | 4.299 | -20.68% |
| TAIWAN | EWT | international_equity | 4.07% | 1.35% | -7.16% | 39.42% | -11.67% | 0.536 | 0.793 | 2.562 | -10.48% |
| BRAZIL | EWZ | international_equity | 1.94% | 4.05% | 1.12% | 21.06% | -2.22% | -0.932 | 0.431 | 0.784 | -12.50% |
| MEXICO | EWW | international_equity | -0.12% | 1.38% | -1.68% | 18.26% | -2.98% | -0.731 | 0.637 | 1.004 | -6.31% |
| SOUTH_AFRICA | EZA | international_equity | -1.95% | -2.32% | -3.89% | 24.54% | -6.50% | 0.338 | 0.778 | 1.980 | -24.32% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | -0.74% | 0.73% | -2.60% | 4.25% | -1.85% | -0.675 | 0.572 | 0.210 | -2.46% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | -1.07% | 0.39% | -2.67% | 3.01% | -2.15% | 0.539 | 0.584 | 0.132 | -2.15% |
| EMERGING_MARKET_BONDS | EMB | credit | -0.88% | 0.56% | -2.62% | 4.37% | -1.96% | -0.786 | 0.742 | 0.331 | -1.96% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | -0.23% | 1.15% | -2.98% | 3.31% | -1.44% | -0.717 | 0.548 | 0.176 | -1.92% |
| SILVER | SLV | precious_metals | 2.12% | 4.98% | -11.92% | 44.01% | -10.19% | -0.886 | 0.652 | 2.520 | -50.70% |
| COPPER | CPER | non_energy_commodities | -0.47% | 2.14% | -0.35% | 23.89% | -3.26% | -0.479 | 0.718 | 1.613 | -5.81% |
| AGRICULTURE | DBA | non_energy_commodities | 0.79% | 4.03% | 1.39% | 14.61% | -1.52% | -0.947 | 0.018 | 0.019 | -1.71% |
| OIL | USO | energy | 11.14% | 18.59% | 4.89% | 50.70% | -7.18% | -0.143 | -0.329 | -1.301 | -8.81% |
| US_DOLLAR | UUP | currencies | 0.60% | 2.45% | -2.72% | 4.56% | -0.98% | -0.959 | -0.538 | -0.202 | 0.00% |
| EURO | FXE | currencies | -0.32% | 1.16% | -1.76% | 4.06% | -0.74% | -0.719 | 0.577 | 0.205 | -5.11% |
| YEN | FXY | currencies | -0.80% | 0.89% | -2.95% | 5.40% | -1.65% | 0.762 | 0.205 | 0.102 | -10.88% |
| BITCOIN_ETF | IBIT | crypto_assets | -0.65% | 2.38% | 0.72% | 34.66% | -5.72% | -0.294 | 0.469 | 1.323 | -48.59% |
| ETHEREUM_ETF | ETHA | crypto_assets | -1.54% | 1.53% | 10.52% | 48.87% | -6.23% | 0.527 | 0.574 | 2.303 | -61.44% |
