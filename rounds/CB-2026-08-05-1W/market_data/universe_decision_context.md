# Full-Universe Horizon-Specific Decision Context

Profile: weekly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: tiingo_eod_adjusted_price_and_volume; yahoo_adjusted_history_through_2026-08-04_plus_2026-08-05_market_close_quote
- As-of date requested: 2026-08-05
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | 5.53% |
| spy_return_21s | 2.95% |
| rsp_return_5s | 1.85% |
| rsp_return_21s | 2.33% |
| hyg_return_5s | 0.84% |
| hyg_return_21s | 0.18% |
| tlt_return_5s | 0.58% |
| tlt_return_21s | -1.44% |
| uup_return_5s | -1.16% |
| uup_return_21s | -1.09% |
| uso_return_5s | -11.16% |
| uso_return_21s | 5.47% |
| iau_return_5s | 5.01% |
| iau_return_21s | 3.21% |
| rsp_minus_spy_5s | -3.67% |
| rsp_minus_spy_21s | -0.62% |
| positive_asset_share_5s | 85.51% |
| positive_asset_share_21s | 71.01% |
| active_return_dispersion_5s | 4.89% |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_3s | active_return_5s | prior_16s_active_return | volatility_21s | max_drawdown_21s | volume_zscore_5v60 | corr_spy_63s | beta_spy_63s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | -5.53% | 2.44% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.03% | -5.46% | 2.65% | 0.19% | 0.00% | 1.390 | -0.183 | -0.003 | 0.00% |
| SP500 | SPY | diversified_us_equity | 3.05% | 0.00% | 0.00% | 14.22% | -3.38% | 0.591 | 1.000 | 1.000 | -0.20% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | 3.11% | -0.19% | -0.05% | 14.20% | -3.29% | -0.303 | 0.993 | 0.988 | -0.31% |
| NASDAQ100 | QQQ | technology_and_growth | 4.26% | 2.87% | -4.28% | 25.90% | -8.79% | 0.551 | 0.923 | 1.717 | -3.76% |
| LARGE_GROWTH | IWF | technology_and_growth | 4.71% | 3.10% | -3.57% | 24.35% | -7.99% | -0.674 | 0.909 | 1.357 | -3.71% |
| LARGE_VALUE | IWD | diversified_us_equity | 1.71% | -2.88% | 3.16% | 10.09% | -1.31% | -0.310 | 0.725 | 0.597 | -0.19% |
| MID_CAP | IJH | diversified_us_equity | 2.30% | -2.49% | 1.46% | 13.36% | -1.71% | -0.440 | 0.803 | 0.836 | -0.62% |
| SMALL_CAP | IWM | diversified_us_equity | 2.94% | -1.65% | -0.13% | 15.74% | -2.92% | -0.500 | 0.790 | 1.031 | -0.64% |
| SMALL_VALUE | IWN | diversified_us_equity | 1.74% | -3.96% | 3.09% | 12.84% | -1.61% | 0.276 | 0.671 | 0.712 | -0.83% |
| DIVIDEND | SCHD | diversified_us_equity | 0.51% | -6.09% | 6.41% | 13.34% | -1.42% | 1.837 | 0.082 | 0.067 | -0.74% |
| LOW_VOL | SPLV | diversified_us_equity | 0.13% | -7.09% | 3.43% | 12.94% | -2.26% | 0.039 | -0.297 | -0.276 | -2.10% |
| MOMENTUM | MTUM | diversified_us_equity | 3.47% | 3.96% | -6.95% | 38.40% | -12.01% | 0.473 | 0.745 | 2.066 | -10.21% |
| TECHNOLOGY | XLK | technology_and_growth | 6.02% | 6.08% | -4.60% | 35.64% | -10.34% | -0.301 | 0.847 | 2.155 | -6.09% |
| COMMUNICATIONS | XLC | technology_and_growth | 2.43% | -4.29% | 1.08% | 24.85% | -7.06% | 0.199 | 0.410 | 0.552 | -7.13% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | 2.20% | 0.77% | -2.48% | 25.52% | -7.35% | 0.695 | 0.689 | 1.068 | -4.34% |
| CONSUMER_STAPLES | XLP | consumer_defensive | 0.33% | -7.85% | 5.39% | 19.44% | -3.03% | 0.116 | -0.327 | -0.394 | -4.00% |
| HEALTHCARE | XLV | healthcare_and_biotech | 0.99% | -6.78% | 3.54% | 18.20% | -3.74% | 0.782 | -0.183 | -0.237 | -1.85% |
| FINANCIALS | XLF | financials | 1.86% | -3.20% | 3.56% | 13.31% | -1.93% | -0.422 | 0.275 | 0.264 | 0.00% |
| INDUSTRIALS | XLI | industrials_and_defense | 3.62% | -0.04% | -0.70% | 17.59% | -3.57% | 0.186 | 0.681 | 0.941 | -0.03% |
| ENERGY | XLE | energy | -3.76% | -7.81% | 9.78% | 21.35% | -3.87% | -0.669 | -0.371 | -0.638 | -7.74% |
| MATERIALS | XLB | materials_and_mining | 4.38% | -3.79% | 2.89% | 20.87% | -3.65% | 0.753 | 0.486 | 0.708 | -1.03% |
| UTILITIES | XLU | rate_sensitive_defensive | -1.56% | -8.31% | 0.71% | 13.28% | -5.68% | 0.929 | -0.103 | -0.119 | -7.31% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | 0.29% | -7.18% | 4.82% | 14.13% | -2.04% | 1.058 | -0.140 | -0.157 | -1.76% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | 0.73% | -5.04% | 1.88% | 4.17% | -1.05% | -0.279 | 0.528 | 0.187 | -2.89% |
| LONG_TREASURY | TLT | rates_and_duration | 1.32% | -4.94% | 0.43% | 8.66% | -2.72% | 1.755 | 0.433 | 0.286 | -6.52% |
| TIPS | TIP | rates_and_duration | 0.14% | -5.51% | 2.07% | 2.31% | -0.81% | 0.612 | 0.497 | 0.120 | -1.16% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | 0.89% | -4.61% | 0.90% | 4.87% | -1.54% | 0.489 | 0.607 | 0.230 | -2.23% |
| HIGH_YIELD_CREDIT | HYG | credit | 0.54% | -4.69% | 1.79% | 2.95% | -0.73% | 0.094 | 0.790 | 0.200 | -0.04% |
| AGGREGATE_BONDS | AGG | rates_and_duration | 0.70% | -5.02% | 1.77% | 3.69% | -0.89% | 1.309 | 0.575 | 0.169 | -1.69% |
| DEVELOPED_EX_US | VEA | international_equity | 2.45% | -0.60% | -0.14% | 18.05% | -2.87% | -0.560 | 0.822 | 1.204 | -0.06% |
| EMERGING_MARKETS | VWO | international_equity | 2.14% | -0.10% | -0.89% | 17.93% | -4.96% | 0.089 | 0.860 | 1.258 | -2.01% |
| EUROPE | VGK | international_equity | 1.39% | -2.16% | 2.24% | 13.87% | -1.60% | -0.152 | 0.721 | 0.873 | 0.00% |
| JAPAN | EWJ | international_equity | 3.00% | 0.97% | -1.56% | 25.00% | -5.50% | -0.615 | 0.763 | 1.264 | -1.87% |
| CHINA | MCHI | international_equity | 0.38% | -3.82% | 8.79% | 17.23% | -2.22% | 0.068 | 0.431 | 0.631 | -14.80% |
| INDIA | INDA | international_equity | 1.02% | -3.21% | 2.12% | 13.78% | -3.45% | 0.249 | 0.569 | 0.629 | -9.01% |
| GOLD | IAU | precious_metals | 4.83% | -0.52% | 0.72% | 24.73% | -3.50% | 0.309 | 0.560 | 0.990 | -21.38% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | -3.30% | -8.89% | 10.10% | 26.23% | -6.42% | 0.275 | -0.225 | -0.356 | -10.21% |
| SEMICONDUCTORS | SMH | technology_and_growth | 5.40% | 7.46% | -10.84% | 51.17% | -17.48% | -0.304 | 0.786 | 3.090 | -14.83% |
| SOFTWARE | IGV | technology_and_growth | 7.12% | 4.15% | 0.57% | 29.83% | -7.47% | -0.782 | 0.404 | 0.978 | -13.98% |
| BROAD_AI_TECH | AIQ | technology_and_growth | 5.89% | 5.87% | -7.39% | 36.91% | -12.30% | -0.480 | 0.831 | 2.404 | -11.09% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | 6.37% | 6.19% | -9.50% | 37.62% | -12.14% | -0.374 | 0.881 | 2.507 | -14.89% |
| CYBERSECURITY | CIBR | technology_and_growth | 6.25% | 4.36% | -1.27% | 28.92% | -7.40% | -0.298 | 0.492 | 1.149 | -0.38% |
| SOLAR | TAN | clean_energy | 3.93% | 2.00% | -10.57% | 44.76% | -14.55% | 0.671 | 0.743 | 2.461 | -30.65% |
| METALS_MINING | XME | materials_and_mining | 11.20% | 9.17% | -2.33% | 39.89% | -6.55% | 0.422 | 0.688 | 2.046 | -15.68% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | 2.20% | -3.67% | 2.91% | 11.36% | -1.46% | 0.002 | 0.703 | 0.550 | -0.23% |
| BIOTECH | XBI | healthcare_and_biotech | 4.08% | -2.08% | -7.30% | 28.54% | -10.51% | -0.558 | 0.383 | 0.839 | -6.86% |
| REGIONAL_BANKS | KRE | financials | 1.68% | -4.01% | 3.92% | 19.13% | -3.55% | -0.842 | 0.209 | 0.290 | -0.74% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | 5.27% | 1.25% | -1.17% | 25.47% | -6.46% | -0.526 | 0.510 | 0.931 | 0.00% |
| CANADA | EWC | international_equity | 2.34% | -3.02% | 4.03% | 11.11% | -1.46% | 0.564 | 0.601 | 0.513 | 0.00% |
| UNITED_KINGDOM | EWU | international_equity | -0.08% | -4.55% | 4.07% | 12.79% | -1.74% | 0.340 | 0.441 | 0.500 | -0.64% |
| AUSTRALIA | EWA | international_equity | 2.73% | -1.99% | 5.92% | 16.74% | -1.61% | -0.086 | 0.624 | 0.813 | 0.00% |
| SOUTH_KOREA | EWY | international_equity | 7.66% | 11.76% | -18.01% | 77.35% | -21.94% | 0.842 | 0.710 | 4.143 | -22.84% |
| TAIWAN | EWT | international_equity | 5.33% | 8.22% | -9.80% | 45.36% | -15.80% | -0.136 | 0.796 | 2.511 | -8.81% |
| BRAZIL | EWZ | international_equity | -1.47% | -3.72% | 4.84% | 23.19% | -3.14% | -0.333 | 0.412 | 0.675 | -12.64% |
| MEXICO | EWW | international_equity | -0.16% | -4.05% | 3.15% | 16.65% | -2.23% | 1.150 | 0.620 | 0.865 | -4.21% |
| SOUTH_AFRICA | EZA | international_equity | 5.08% | 2.15% | 0.07% | 25.84% | -5.31% | -0.537 | 0.746 | 1.723 | -16.34% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | 0.82% | -5.04% | 1.79% | 4.76% | -1.02% | 0.001 | 0.573 | 0.202 | -1.62% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | 0.44% | -5.21% | 1.07% | 3.42% | -1.85% | 0.439 | 0.566 | 0.124 | -1.36% |
| EMERGING_MARKET_BONDS | EMB | credit | 0.98% | -4.44% | 1.00% | 5.32% | -1.52% | 0.318 | 0.757 | 0.311 | -0.86% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | 0.71% | -4.90% | 2.00% | 3.91% | -0.77% | -0.357 | 0.554 | 0.164 | -1.10% |
| SILVER | SLV | precious_metals | 7.09% | 2.78% | -2.50% | 39.47% | -7.47% | -0.612 | 0.593 | 2.116 | -46.90% |
| COPPER | CPER | non_energy_commodities | 3.26% | 0.99% | 5.01% | 21.59% | -3.26% | -0.414 | 0.672 | 1.366 | 0.00% |
| AGRICULTURE | DBA | non_energy_commodities | 0.44% | -5.02% | 2.22% | 13.16% | -2.69% | -0.332 | 0.107 | 0.106 | -3.83% |
| OIL | USO | energy | -11.06% | -16.69% | 21.16% | 67.67% | -17.64% | -0.505 | -0.378 | -1.447 | -24.90% |
| US_DOLLAR | UUP | currencies | -0.28% | -6.69% | 2.51% | 5.38% | -1.78% | 1.117 | -0.448 | -0.159 | -1.78% |
| EURO | FXE | currencies | 0.17% | -4.61% | 2.81% | 4.37% | -0.81% | -0.415 | 0.473 | 0.163 | -3.63% |
| YEN | FXY | currencies | 0.85% | -1.93% | 1.56% | 11.14% | -1.30% | 5.098 | 0.269 | 0.140 | -7.43% |
| BITCOIN_ETF | IBIT | crypto_assets | 3.09% | -3.47% | 2.03% | 28.90% | -5.39% | -0.221 | 0.447 | 1.153 | -48.46% |
| ETHEREUM_ETF | ETHA | crypto_assets | 2.91% | -3.84% | 7.84% | 40.81% | -4.35% | -0.157 | 0.529 | 1.972 | -60.43% |
