# Full-Universe Horizon-Specific Decision Context

Profile: weekly. All values stop at the requested close and are sorted by frozen option order, not performance.

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
| rsp_return_21s | 3.47% |
| hyg_return_5s | 0.03% |
| hyg_return_21s | 0.15% |
| tlt_return_5s | -0.64% |
| tlt_return_21s | -2.27% |
| uup_return_5s | 0.00% |
| uup_return_21s | -0.88% |
| uso_return_5s | 2.39% |
| uso_return_21s | 4.10% |
| iau_return_5s | -0.57% |
| iau_return_21s | 8.44% |
| rsp_minus_spy_5s | -0.00% |
| rsp_minus_spy_21s | 0.05% |
| positive_asset_share_5s | 39.13% |
| positive_asset_share_21s | 71.01% |
| active_return_dispersion_5s | 1.45% |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_3s | active_return_5s | prior_16s_active_return | volatility_21s | max_drawdown_21s | volume_zscore_5v60 | corr_spy_63s | beta_spy_63s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | 0.40% | -3.84% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.05% | 0.48% | -3.61% | 0.17% | 0.00% | -0.795 | -0.139 | -0.002 | 0.00% |
| SP500 | SPY | diversified_us_equity | -1.34% | 0.00% | 0.00% | 13.53% | -2.52% | -1.224 | 1.000 | 1.000 | -1.34% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | -1.37% | -0.02% | 0.10% | 13.60% | -2.44% | -0.511 | 0.993 | 0.989 | -1.37% |
| NASDAQ100 | QQQ | technology_and_growth | -1.99% | 0.27% | -0.62% | 24.20% | -6.66% | -0.857 | 0.923 | 1.732 | -3.73% |
| LARGE_GROWTH | IWF | technology_and_growth | -2.06% | -0.03% | -3.82% | 23.24% | -7.71% | -0.875 | 0.899 | 1.364 | -4.34% |
| LARGE_VALUE | IWD | diversified_us_equity | -0.76% | -0.06% | 0.60% | 8.63% | -1.00% | -0.473 | 0.711 | 0.571 | -0.76% |
| MID_CAP | IJH | diversified_us_equity | -1.50% | -0.28% | -1.49% | 14.05% | -1.82% | -0.611 | 0.796 | 0.841 | -1.82% |
| SMALL_CAP | IWM | diversified_us_equity | -1.08% | 0.15% | -0.87% | 15.60% | -2.69% | -1.439 | 0.781 | 0.993 | -1.59% |
| SMALL_VALUE | IWN | diversified_us_equity | -1.02% | 0.17% | -1.97% | 11.43% | -1.38% | -1.371 | 0.657 | 0.676 | -1.31% |
| DIVIDEND | SCHD | diversified_us_equity | 0.23% | 1.10% | 0.80% | 10.24% | -1.42% | -0.117 | 0.083 | 0.070 | -0.03% |
| LOW_VOL | SPLV | diversified_us_equity | -0.26% | 0.91% | -4.41% | 9.44% | -2.98% | -1.104 | -0.292 | -0.271 | -2.49% |
| MOMENTUM | MTUM | diversified_us_equity | -1.34% | 1.53% | -5.22% | 38.41% | -9.83% | -0.606 | 0.673 | 1.894 | -9.68% |
| TECHNOLOGY | XLK | technology_and_growth | -2.70% | 0.15% | 2.07% | 33.88% | -7.86% | -1.311 | 0.842 | 2.154 | -6.24% |
| COMMUNICATIONS | XLC | technology_and_growth | -1.84% | -0.31% | -5.06% | 27.80% | -6.45% | -0.939 | 0.415 | 0.620 | -7.46% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | -1.76% | -2.01% | 0.20% | 24.36% | -5.32% | -1.316 | 0.680 | 1.081 | -6.18% |
| CONSUMER_STAPLES | XLP | consumer_defensive | -0.49% | 1.45% | -4.04% | 16.30% | -3.07% | -0.797 | -0.332 | -0.413 | -3.72% |
| HEALTHCARE | XLV | healthcare_and_biotech | 0.80% | 1.43% | 1.66% | 15.11% | -3.09% | -1.316 | -0.203 | -0.269 | 0.00% |
| FINANCIALS | XLF | financials | -0.72% | 0.47% | -0.70% | 10.84% | -1.60% | -0.800 | 0.306 | 0.293 | -0.72% |
| INDUSTRIALS | XLI | industrials_and_defense | -1.19% | -0.74% | 0.42% | 17.73% | -3.57% | -1.601 | 0.667 | 0.895 | -1.58% |
| ENERGY | XLE | energy | 4.29% | 4.92% | 1.32% | 24.68% | -3.87% | -1.150 | -0.349 | -0.608 | 0.00% |
| MATERIALS | XLB | materials_and_mining | -1.01% | -2.34% | 2.58% | 19.19% | -3.65% | -0.943 | 0.452 | 0.645 | -2.74% |
| UTILITIES | XLU | rate_sensitive_defensive | -0.05% | 1.30% | -6.75% | 13.89% | -6.83% | -0.661 | -0.117 | -0.132 | -6.54% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | -1.09% | 1.65% | -6.38% | 13.81% | -4.19% | 0.539 | -0.149 | -0.171 | -3.00% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | -0.40% | 0.47% | -4.21% | 4.46% | -0.74% | -0.266 | 0.487 | 0.169 | -3.29% |
| LONG_TREASURY | TLT | rates_and_duration | -1.13% | -0.24% | -5.47% | 9.68% | -3.04% | -0.036 | 0.378 | 0.249 | -8.03% |
| TIPS | TIP | rates_and_duration | -0.13% | 0.53% | -4.18% | 2.51% | -0.61% | -0.565 | 0.467 | 0.116 | -1.15% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | -0.67% | 0.26% | -4.49% | 5.28% | -0.99% | -0.132 | 0.565 | 0.217 | -3.05% |
| HIGH_YIELD_CREDIT | HYG | credit | -0.33% | 0.43% | -3.72% | 3.31% | -0.71% | -0.707 | 0.820 | 0.209 | -0.33% |
| AGGREGATE_BONDS | AGG | rates_and_duration | -0.35% | 0.43% | -4.13% | 3.80% | -0.62% | -0.293 | 0.534 | 0.154 | -2.05% |
| DEVELOPED_EX_US | VEA | international_equity | -1.56% | -0.01% | 1.16% | 17.16% | -2.18% | -1.023 | 0.816 | 1.145 | -1.76% |
| EMERGING_MARKETS | VWO | international_equity | -1.16% | -0.39% | -0.06% | 15.56% | -3.30% | -0.662 | 0.853 | 1.203 | -2.61% |
| EUROPE | VGK | international_equity | -0.90% | -0.41% | 1.42% | 12.37% | -1.41% | -0.995 | 0.740 | 0.796 | -1.13% |
| JAPAN | EWJ | international_equity | -3.15% | -0.54% | 2.63% | 25.18% | -3.66% | -1.277 | 0.757 | 1.305 | -3.15% |
| CHINA | MCHI | international_equity | 0.88% | -0.89% | -0.99% | 14.52% | -4.41% | -0.385 | 0.394 | 0.538 | -16.50% |
| INDIA | INDA | international_equity | -1.20% | -1.01% | -0.66% | 12.12% | -2.36% | -1.345 | 0.610 | 0.597 | -10.69% |
| GOLD | IAU | precious_metals | -0.09% | -0.17% | 5.23% | 23.63% | -2.56% | -0.773 | 0.515 | 0.932 | -19.55% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | 2.42% | 2.02% | -0.79% | 26.02% | -6.42% | -0.442 | -0.205 | -0.332 | -3.75% |
| SEMICONDUCTORS | SMH | technology_and_growth | -3.28% | -0.15% | -1.31% | 48.23% | -14.09% | -0.698 | 0.763 | 2.987 | -14.82% |
| SOFTWARE | IGV | technology_and_growth | -4.06% | -1.48% | 7.93% | 35.14% | -6.32% | -0.392 | 0.476 | 1.221 | -13.42% |
| BROAD_AI_TECH | AIQ | technology_and_growth | -3.23% | -0.66% | 3.03% | 33.84% | -8.23% | -0.820 | 0.834 | 2.400 | -10.85% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | -2.54% | -0.77% | 1.74% | 38.53% | -9.84% | -1.287 | 0.852 | 2.367 | -11.83% |
| CYBERSECURITY | CIBR | technology_and_growth | -4.66% | -2.08% | 4.35% | 29.11% | -5.02% | 0.189 | 0.559 | 1.340 | -4.66% |
| SOLAR | TAN | clean_energy | -4.96% | -4.97% | -3.82% | 41.84% | -11.28% | -0.848 | 0.767 | 2.545 | -32.54% |
| METALS_MINING | XME | materials_and_mining | -1.42% | -3.16% | 16.72% | 41.78% | -5.72% | -0.877 | 0.662 | 1.989 | -14.40% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | -1.32% | -0.00% | 0.06% | 10.32% | -1.34% | -1.439 | 0.712 | 0.569 | -1.34% |
| BIOTECH | XBI | healthcare_and_biotech | 2.07% | 1.69% | 0.89% | 23.50% | -4.85% | -0.960 | 0.319 | 0.674 | -2.54% |
| REGIONAL_BANKS | KRE | financials | -1.16% | 0.46% | -3.68% | 13.28% | -2.33% | -1.123 | 0.206 | 0.285 | -1.39% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | 0.99% | 0.51% | 6.03% | 21.84% | -3.56% | -1.493 | 0.455 | 0.796 | -0.42% |
| CANADA | EWC | international_equity | -0.84% | 0.52% | -0.44% | 10.51% | -1.46% | 0.611 | 0.589 | 0.500 | -1.04% |
| UNITED_KINGDOM | EWU | international_equity | -0.21% | 0.11% | 0.28% | 10.44% | -1.14% | -0.718 | 0.422 | 0.401 | -1.07% |
| AUSTRALIA | EWA | international_equity | -0.44% | -0.73% | 1.18% | 16.94% | -2.83% | -0.546 | 0.593 | 0.710 | -2.63% |
| SOUTH_KOREA | EWY | international_equity | -4.80% | 2.08% | -1.15% | 76.41% | -17.05% | -0.256 | 0.682 | 3.985 | -22.42% |
| TAIWAN | EWT | international_equity | -2.89% | 0.84% | 2.95% | 44.10% | -12.07% | -1.317 | 0.795 | 2.557 | -6.40% |
| BRAZIL | EWZ | international_equity | -0.21% | -0.42% | -8.06% | 22.05% | -8.05% | -0.171 | 0.413 | 0.647 | -18.47% |
| MEXICO | EWW | international_equity | -1.31% | -1.93% | -2.30% | 16.90% | -3.95% | 0.157 | 0.604 | 0.823 | -6.99% |
| SOUTH_AFRICA | EZA | international_equity | -0.34% | -1.77% | 3.77% | 26.12% | -5.19% | -0.768 | 0.709 | 1.561 | -15.97% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | -0.44% | 0.46% | -4.69% | 5.52% | -1.18% | -0.194 | 0.528 | 0.196 | -2.25% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | -0.74% | -0.13% | -4.18% | 4.24% | -1.24% | 0.459 | 0.551 | 0.132 | -1.78% |
| EMERGING_MARKET_BONDS | EMB | credit | -0.76% | 0.20% | -3.97% | 5.56% | -0.89% | -1.077 | 0.749 | 0.299 | -1.41% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | -0.67% | -0.08% | -3.59% | 3.57% | -0.83% | -0.597 | 0.525 | 0.141 | -1.92% |
| SILVER | SLV | precious_metals | -1.24% | -1.49% | 11.01% | 37.61% | -4.12% | -0.701 | 0.600 | 1.916 | -45.61% |
| COPPER | CPER | non_energy_commodities | -1.68% | -2.18% | 0.85% | 22.69% | -4.09% | 0.004 | 0.650 | 1.216 | -4.09% |
| AGRICULTURE | DBA | non_energy_commodities | 1.48% | 2.00% | -5.37% | 13.51% | -2.87% | -0.428 | 0.109 | 0.105 | -2.44% |
| OIL | USO | energy | 4.50% | 2.79% | -2.16% | 64.02% | -17.64% | -0.869 | -0.345 | -1.339 | -14.58% |
| US_DOLLAR | UUP | currencies | -0.14% | 0.40% | -4.72% | 5.15% | -1.85% | -1.406 | -0.420 | -0.147 | -1.61% |
| EURO | FXE | currencies | 0.41% | 0.70% | -2.67% | 4.19% | -0.40% | -0.422 | 0.443 | 0.150 | -3.40% |
| YEN | FXY | currencies | -0.09% | 0.14% | -1.76% | 11.86% | -1.74% | -0.170 | 0.243 | 0.134 | -8.50% |
| BITCOIN_ETF | IBIT | crypto_assets | 2.01% | 2.24% | -6.41% | 22.22% | -5.42% | -0.861 | 0.416 | 1.069 | -48.66% |
| ETHEREUM_ETF | ETHA | crypto_assets | 1.48% | 2.24% | -4.88% | 28.66% | -4.35% | -0.746 | 0.518 | 1.933 | -60.54% |
