# Full-Universe Horizon-Specific Decision Context

Profile: weekly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: yahoo_chart_adjusted_close_and_reported_volume
- As-of date requested: 2026-08-14
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | 0.40% |
| spy_return_21s | 3.41% |
| rsp_return_5s | 1.22% |
| rsp_return_21s | 3.59% |
| hyg_return_5s | 0.13% |
| hyg_return_21s | 0.37% |
| tlt_return_5s | -0.87% |
| tlt_return_21s | -2.18% |
| uup_return_5s | 0.14% |
| uup_return_21s | -0.81% |
| uso_return_5s | 7.31% |
| uso_return_21s | 6.12% |
| iau_return_5s | 0.73% |
| iau_return_21s | 10.00% |
| rsp_minus_spy_5s | 0.82% |
| rsp_minus_spy_21s | 0.17% |
| positive_asset_share_5s | 65.22% |
| positive_asset_share_21s | 76.81% |
| active_return_dispersion_5s | 2.17% |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_3s | active_return_5s | prior_16s_active_return | volatility_21s | max_drawdown_21s | volume_zscore_5v60 | corr_spy_63s | beta_spy_63s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | -0.40% | -3.00% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.04% | -0.34% | -2.76% | 0.17% | 0.00% | -0.835 | -0.145 | -0.002 | 0.00% |
| SP500 | SPY | diversified_us_equity | 0.75% | 0.00% | 0.00% | 13.68% | -2.83% | -1.289 | 1.000 | 1.000 | -0.20% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | 0.84% | 0.14% | 0.02% | 13.64% | -2.74% | -0.065 | 0.993 | 0.989 | -0.12% |
| NASDAQ100 | QQQ | technology_and_growth | 1.76% | 0.71% | -0.58% | 23.99% | -6.66% | -1.175 | 0.924 | 1.716 | -1.91% |
| LARGE_GROWTH | IWF | technology_and_growth | 1.37% | 0.16% | -0.20% | 21.97% | -6.00% | -0.820 | 0.910 | 1.372 | -2.62% |
| LARGE_VALUE | IWD | diversified_us_equity | 0.25% | -0.01% | 0.24% | 8.67% | -1.31% | -0.470 | 0.723 | 0.588 | -0.05% |
| MID_CAP | IJH | diversified_us_equity | 1.16% | 0.73% | -0.63% | 12.79% | -1.71% | -1.078 | 0.804 | 0.826 | 0.00% |
| SMALL_CAP | IWM | diversified_us_equity | 1.36% | 0.77% | -0.98% | 15.10% | -2.69% | -1.523 | 0.784 | 1.020 | 0.00% |
| SMALL_VALUE | IWN | diversified_us_equity | 1.09% | 0.45% | -2.40% | 11.53% | -1.61% | -1.039 | 0.665 | 0.697 | 0.00% |
| DIVIDEND | SCHD | diversified_us_equity | 0.73% | 1.43% | -0.40% | 10.20% | -1.42% | -0.122 | 0.090 | 0.076 | 0.00% |
| LOW_VOL | SPLV | diversified_us_equity | 0.94% | -0.20% | -3.77% | 9.17% | -2.98% | -0.825 | -0.267 | -0.252 | -2.06% |
| MOMENTUM | MTUM | diversified_us_equity | 2.88% | 2.15% | -1.05% | 34.70% | -9.98% | -0.793 | 0.729 | 2.025 | -8.11% |
| TECHNOLOGY | XLK | technology_and_growth | 2.11% | 0.69% | 2.88% | 32.80% | -7.86% | -1.479 | 0.843 | 2.133 | -4.02% |
| COMMUNICATIONS | XLC | technology_and_growth | 1.51% | 1.13% | -4.25% | 24.45% | -6.45% | -0.960 | 0.401 | 0.556 | -5.39% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | -0.87% | -1.78% | -0.85% | 24.78% | -7.31% | -1.706 | 0.688 | 1.092 | -4.70% |
| CONSUMER_STAPLES | XLP | consumer_defensive | 1.65% | 0.74% | -3.81% | 15.06% | -3.06% | -1.219 | -0.329 | -0.402 | -3.15% |
| HEALTHCARE | XLV | healthcare_and_biotech | -0.38% | 0.62% | -0.60% | 15.23% | -3.09% | -1.437 | -0.164 | -0.214 | -0.64% |
| FINANCIALS | XLF | financials | 0.62% | 0.57% | -1.50% | 10.78% | -1.62% | -1.508 | 0.306 | 0.291 | -0.17% |
| INDUSTRIALS | XLI | industrials_and_defense | 0.44% | 0.32% | -0.21% | 17.14% | -3.57% | -1.938 | 0.675 | 0.905 | 0.00% |
| ENERGY | XLE | energy | 1.61% | 7.27% | -2.16% | 24.25% | -3.87% | -1.005 | -0.357 | -0.627 | -0.33% |
| MATERIALS | XLB | materials_and_mining | -1.31% | -1.00% | 0.87% | 19.34% | -3.65% | -0.459 | 0.470 | 0.685 | -1.31% |
| UTILITIES | XLU | rate_sensitive_defensive | 1.56% | 1.21% | -7.09% | 14.06% | -6.83% | -0.263 | -0.067 | -0.078 | -5.92% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | 2.70% | 0.25% | -1.88% | 15.22% | -4.19% | 0.010 | -0.131 | -0.155 | -1.61% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | 0.18% | -0.54% | -3.25% | 4.55% | -1.05% | -0.177 | 0.516 | 0.187 | -3.17% |
| LONG_TREASURY | TLT | rates_and_duration | -0.18% | -1.27% | -4.33% | 9.59% | -2.69% | 0.031 | 0.417 | 0.281 | -7.60% |
| TIPS | TIP | rates_and_duration | 0.09% | -0.48% | -3.10% | 2.56% | -0.81% | -0.580 | 0.505 | 0.125 | -1.17% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | 0.12% | -0.80% | -3.46% | 5.25% | -1.25% | -0.334 | 0.589 | 0.229 | -2.80% |
| HIGH_YIELD_CREDIT | HYG | credit | 0.25% | -0.27% | -2.76% | 2.92% | -0.71% | -0.794 | 0.811 | 0.200 | -0.10% |
| AGGREGATE_BONDS | AGG | rates_and_duration | 0.16% | -0.52% | -3.20% | 3.81% | -0.88% | -0.189 | 0.561 | 0.167 | -1.92% |
| DEVELOPED_EX_US | VEA | international_equity | 1.22% | 0.55% | 1.08% | 16.15% | -2.18% | -0.468 | 0.822 | 1.155 | 0.00% |
| EMERGING_MARKETS | VWO | international_equity | -0.02% | -0.99% | -0.23% | 16.09% | -3.30% | -0.615 | 0.863 | 1.236 | -1.85% |
| EUROPE | VGK | international_equity | 0.08% | -0.65% | 1.29% | 12.76% | -1.41% | -1.500 | 0.730 | 0.817 | -0.25% |
| JAPAN | EWJ | international_equity | 2.00% | 0.95% | 2.43% | 23.49% | -3.66% | -1.564 | 0.762 | 1.268 | -0.26% |
| CHINA | MCHI | international_equity | -1.78% | -3.83% | 1.49% | 17.92% | -4.41% | -0.208 | 0.432 | 0.602 | -16.91% |
| INDIA | INDA | international_equity | -0.62% | -1.57% | 0.45% | 12.29% | -2.62% | -1.510 | 0.613 | 0.597 | -9.97% |
| GOLD | IAU | precious_metals | 0.12% | 0.34% | 6.20% | 22.49% | -2.56% | -0.811 | 0.534 | 0.963 | -18.99% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | 0.00% | 3.43% | -1.29% | 26.08% | -6.42% | -0.275 | -0.196 | -0.311 | -5.29% |
| SEMICONDUCTORS | SMH | technology_and_growth | 2.60% | 0.48% | -0.58% | 46.45% | -14.09% | -1.003 | 0.771 | 2.992 | -12.12% |
| SOFTWARE | IGV | technology_and_growth | 0.15% | 0.96% | 6.59% | 34.35% | -7.04% | -0.561 | 0.450 | 1.141 | -11.62% |
| BROAD_AI_TECH | AIQ | technology_and_growth | 1.58% | 0.94% | 3.81% | 32.82% | -8.23% | -1.047 | 0.835 | 2.382 | -8.47% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | 1.63% | 1.59% | 5.22% | 36.40% | -8.78% | -1.172 | 0.871 | 2.423 | -9.34% |
| CYBERSECURITY | CIBR | technology_and_growth | -0.32% | 1.39% | 2.11% | 28.59% | -5.77% | 0.129 | 0.545 | 1.298 | -2.54% |
| SOLAR | TAN | clean_energy | -1.39% | -1.88% | -5.64% | 41.46% | -12.00% | -1.159 | 0.743 | 2.457 | -29.70% |
| METALS_MINING | XME | materials_and_mining | -0.59% | 0.81% | 13.92% | 39.15% | -5.72% | -0.828 | 0.674 | 2.031 | -11.75% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | 0.94% | 0.82% | -0.66% | 10.18% | -1.46% | -1.292 | 0.715 | 0.568 | 0.00% |
| BIOTECH | XBI | healthcare_and_biotech | -0.42% | -0.37% | 0.53% | 25.06% | -4.85% | -0.880 | 0.355 | 0.773 | -4.18% |
| REGIONAL_BANKS | KRE | financials | 1.46% | 1.86% | -5.20% | 13.73% | -3.55% | -1.613 | 0.208 | 0.283 | 0.00% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | 0.52% | 0.59% | 5.60% | 21.81% | -3.56% | -1.513 | 0.477 | 0.862 | 0.00% |
| CANADA | EWC | international_equity | 1.17% | 1.12% | 0.21% | 10.69% | -1.40% | -0.693 | 0.611 | 0.522 | 0.00% |
| UNITED_KINGDOM | EWU | international_equity | -0.08% | -1.18% | 0.55% | 11.39% | -1.23% | -0.010 | 0.424 | 0.447 | -0.86% |
| AUSTRALIA | EWA | international_equity | -1.00% | -2.90% | 3.21% | 17.21% | -2.50% | -0.229 | 0.612 | 0.748 | -2.50% |
| SOUTH_KOREA | EWY | international_equity | 7.47% | 7.82% | -1.33% | 69.60% | -17.05% | -0.809 | 0.697 | 3.994 | -18.00% |
| TAIWAN | EWT | international_equity | 3.01% | 3.46% | -0.08% | 42.56% | -12.07% | -1.235 | 0.794 | 2.524 | -4.00% |
| BRAZIL | EWZ | international_equity | -0.15% | -4.39% | -2.97% | 22.17% | -7.86% | 0.312 | 0.428 | 0.685 | -17.92% |
| MEXICO | EWW | international_equity | -1.61% | -3.64% | 0.06% | 16.77% | -3.24% | -0.268 | 0.615 | 0.856 | -6.30% |
| SOUTH_AFRICA | EZA | international_equity | -1.55% | -3.44% | 7.66% | 28.52% | -4.05% | -0.647 | 0.725 | 1.645 | -15.43% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | 0.18% | -0.47% | -3.16% | 4.85% | -0.96% | -0.230 | 0.561 | 0.199 | -1.77% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | -0.07% | -0.47% | -3.37% | 3.60% | -1.28% | -0.080 | 0.570 | 0.131 | -1.32% |
| EMERGING_MARKET_BONDS | EMB | credit | 0.23% | -0.60% | -3.15% | 5.57% | -1.25% | -1.123 | 0.732 | 0.305 | -1.42% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | -0.21% | -0.88% | -2.77% | 3.60% | -0.56% | -0.668 | 0.533 | 0.157 | -1.65% |
| SILVER | SLV | precious_metals | -0.12% | 1.31% | 11.11% | 34.22% | -4.12% | -0.503 | 0.620 | 2.074 | -44.62% |
| COPPER | CPER | non_energy_commodities | -0.52% | -0.12% | 1.83% | 21.29% | -3.26% | -0.654 | 0.660 | 1.285 | -2.06% |
| AGRICULTURE | DBA | non_energy_commodities | 0.65% | 0.14% | -2.89% | 13.18% | -2.87% | -0.947 | 0.152 | 0.148 | -3.34% |
| OIL | USO | energy | -0.79% | 6.91% | -4.11% | 64.71% | -17.64% | -0.549 | -0.356 | -1.379 | -17.23% |
| US_DOLLAR | UUP | currencies | -0.11% | -0.26% | -3.96% | 5.18% | -1.85% | -0.631 | -0.439 | -0.156 | -1.71% |
| EURO | FXE | currencies | 0.25% | -0.30% | -1.87% | 4.30% | -0.62% | -0.423 | 0.462 | 0.158 | -3.44% |
| YEN | FXY | currencies | -0.09% | -1.53% | 0.02% | 11.86% | -1.68% | 0.232 | 0.256 | 0.140 | -8.34% |
| BITCOIN_ETF | IBIT | crypto_assets | -0.86% | -3.58% | -1.88% | 21.33% | -5.42% | -0.871 | 0.454 | 1.170 | -50.02% |
| ETHEREUM_ETF | ETHA | crypto_assets | 0.00% | -2.40% | -0.60% | 30.59% | -4.35% | -0.980 | 0.537 | 2.028 | -61.25% |
