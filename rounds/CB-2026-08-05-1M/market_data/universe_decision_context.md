# Full-Universe Horizon-Specific Decision Context

Profile: monthly. All values stop at the requested close and are sorted by frozen option order, not performance.

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
| active_return_dispersion_5s |  |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_5s | active_return_21s | prior_105s_active_return | volatility_63s | max_drawdown_63s | volume_zscore_20v120 | corr_spy_252s | beta_spy_252s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | -2.95% | -9.02% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.07% | -2.68% | -7.50% | 0.21% | -0.01% | -0.260 | -0.096 | -0.001 | 0.00% |
| SP500 | SPY | diversified_us_equity | 5.53% | 0.00% | 0.00% | 14.23% | -4.49% | -0.825 | 1.000 | 1.000 | -0.20% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | 5.34% | -0.24% | 0.40% | 14.16% | -4.36% | -0.788 | 0.995 | 1.012 | -0.31% |
| NASDAQ100 | QQQ | technology_and_growth | 8.40% | -1.84% | 6.33% | 26.48% | -11.22% | -0.736 | 0.931 | 1.414 | -3.76% |
| LARGE_GROWTH | IWF | technology_and_growth | 8.63% | -0.86% | -3.12% | 21.24% | -11.36% | -0.774 | 0.937 | 1.283 | -3.71% |
| LARGE_VALUE | IWD | diversified_us_equity | 2.65% | 0.43% | 3.40% | 11.73% | -2.40% | -0.638 | 0.803 | 0.701 | -0.19% |
| MID_CAP | IJH | diversified_us_equity | 3.04% | -0.93% | 0.29% | 14.82% | -4.25% | -0.913 | 0.801 | 0.979 | -0.62% |
| SMALL_CAP | IWM | diversified_us_equity | 3.88% | -1.74% | 4.16% | 18.58% | -4.81% | -1.084 | 0.812 | 1.217 | -0.64% |
| SMALL_VALUE | IWN | diversified_us_equity | 1.57% | -0.73% | 3.15% | 15.10% | -4.01% | -0.466 | 0.724 | 0.968 | -0.83% |
| DIVIDEND | SCHD | diversified_us_equity | -0.56% | 0.43% | -0.57% | 11.66% | -2.95% | 0.008 | 0.289 | 0.248 | -0.74% |
| LOW_VOL | SPLV | diversified_us_equity | -1.56% | -3.54% | -4.11% | 13.26% | -3.75% | -0.838 | 0.018 | 0.015 | -2.10% |
| MOMENTUM | MTUM | diversified_us_equity | 9.49% | -3.74% | 13.06% | 39.48% | -17.99% | 1.339 | 0.780 | 1.560 | -10.21% |
| TECHNOLOGY | XLK | technology_and_growth | 11.61% | 0.80% | 17.40% | 36.22% | -15.86% | -0.986 | 0.859 | 1.729 | -6.09% |
| COMMUNICATIONS | XLC | technology_and_growth | 1.24% | -3.09% | -14.17% | 19.15% | -9.98% | -0.241 | 0.585 | 0.678 | -7.13% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | 6.30% | -1.89% | -11.60% | 22.05% | -10.72% | -0.423 | 0.777 | 1.171 | -4.34% |
| CONSUMER_STAPLES | XLP | consumer_defensive | -2.32% | -2.40% | -8.94% | 17.15% | -4.95% | -0.775 | -0.066 | -0.072 | -4.00% |
| HEALTHCARE | XLV | healthcare_and_biotech | -1.25% | -3.12% | -1.40% | 18.42% | -3.74% | -0.594 | 0.223 | 0.270 | -1.85% |
| FINANCIALS | XLF | financials | 2.33% | 0.53% | -3.41% | 13.63% | -2.08% | -0.748 | 0.550 | 0.626 | 0.00% |
| INDUSTRIALS | XLI | industrials_and_defense | 5.49% | -0.78% | -0.50% | 19.67% | -4.80% | -1.021 | 0.721 | 0.951 | -0.03% |
| ENERGY | XLE | energy | -2.28% | 1.93% | -1.83% | 24.50% | -13.22% | -0.896 | -0.150 | -0.246 | -7.74% |
| MATERIALS | XLB | materials_and_mining | 1.74% | -0.76% | -6.59% | 20.71% | -6.43% | -0.620 | 0.532 | 0.733 | -1.03% |
| UTILITIES | XLU | rate_sensitive_defensive | -2.78% | -7.42% | -1.92% | 16.54% | -7.05% | -0.704 | 0.122 | 0.141 | -7.31% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | -1.65% | -2.26% | 2.68% | 15.93% | -3.38% | -0.766 | 0.227 | 0.248 | -1.76% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | 0.49% | -3.03% | -9.33% | 5.05% | -2.00% | -0.953 | 0.284 | 0.100 | -2.89% |
| LONG_TREASURY | TLT | rates_and_duration | 0.58% | -4.39% | -9.73% | 9.39% | -5.60% | -0.511 | 0.226 | 0.162 | -6.52% |
| TIPS | TIP | rates_and_duration | 0.01% | -3.31% | -8.40% | 3.44% | -1.53% | -0.535 | 0.272 | 0.070 | -1.16% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | 0.92% | -3.58% | -9.19% | 5.40% | -2.83% | -0.337 | 0.476 | 0.194 | -2.23% |
| HIGH_YIELD_CREDIT | HYG | credit | 0.84% | -2.77% | -7.74% | 3.60% | -1.01% | -0.650 | 0.779 | 0.233 | -0.04% |
| AGGREGATE_BONDS | AGG | rates_and_duration | 0.51% | -3.12% | -8.86% | 4.18% | -1.71% | -0.225 | 0.394 | 0.114 | -1.69% |
| DEVELOPED_EX_US | VEA | international_equity | 4.93% | -0.73% | -2.19% | 20.85% | -4.85% | -0.925 | 0.803 | 1.075 | -0.06% |
| EMERGING_MARKETS | VWO | international_equity | 5.43% | -1.03% | -5.14% | 20.83% | -7.05% | -0.557 | 0.808 | 1.105 | -2.01% |
| EUROPE | VGK | international_equity | 3.36% | 0.20% | -5.81% | 17.22% | -3.86% | -0.920 | 0.745 | 0.915 | 0.00% |
| JAPAN | EWJ | international_equity | 6.50% | -0.71% | -1.07% | 23.59% | -7.86% | -0.882 | 0.721 | 1.174 | -1.87% |
| CHINA | MCHI | international_equity | 1.71% | 5.22% | -23.67% | 20.85% | -15.02% | -0.548 | 0.546 | 0.868 | -14.80% |
| INDIA | INDA | international_equity | 2.32% | -0.97% | -16.20% | 15.73% | -5.64% | -0.490 | 0.537 | 0.631 | -9.01% |
| GOLD | IAU | precious_metals | 5.01% | 0.25% | -25.85% | 25.16% | -16.01% | -0.560 | 0.311 | 0.679 | -21.38% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | -3.36% | 1.09% | 4.87% | 22.53% | -16.55% | 0.136 | -0.171 | -0.261 | -10.21% |
| SEMICONDUCTORS | SMH | technology_and_growth | 12.99% | -4.97% | 37.20% | 55.95% | -24.62% | 0.754 | 0.785 | 2.364 | -14.83% |
| SOFTWARE | IGV | technology_and_growth | 9.68% | 4.67% | 1.24% | 34.43% | -21.29% | -0.903 | 0.509 | 1.166 | -13.98% |
| BROAD_AI_TECH | AIQ | technology_and_growth | 11.40% | -2.50% | 12.62% | 41.15% | -20.19% | -0.197 | 0.848 | 1.899 | -11.09% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | 11.72% | -4.57% | -10.68% | 40.51% | -23.82% | -0.796 | 0.800 | 2.172 | -14.89% |
| CYBERSECURITY | CIBR | technology_and_growth | 9.89% | 2.86% | 28.78% | 33.21% | -11.74% | -0.331 | 0.541 | 1.104 | -0.38% |
| SOLAR | TAN | clean_energy | 7.53% | -9.41% | -10.42% | 47.13% | -35.51% | -0.384 | 0.603 | 1.859 | -30.65% |
| METALS_MINING | XME | materials_and_mining | 14.70% | 6.27% | -26.66% | 42.30% | -26.49% | -0.507 | 0.598 | 1.731 | -15.68% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | 1.85% | -0.62% | 0.00% | 11.13% | -2.04% | -0.837 | 0.767 | 0.698 | -0.23% |
| BIOTECH | XBI | healthcare_and_biotech | 3.45% | -9.58% | 19.48% | 31.12% | -10.51% | -0.315 | 0.481 | 1.013 | -6.86% |
| REGIONAL_BANKS | KRE | financials | 1.52% | 0.07% | -2.42% | 19.76% | -5.29% | -0.698 | 0.436 | 0.771 | -0.74% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | 6.78% | -0.03% | -4.35% | 25.97% | -8.58% | -0.422 | 0.572 | 1.007 | 0.00% |
| CANADA | EWC | international_equity | 2.51% | 1.19% | -2.10% | 12.15% | -3.20% | -0.595 | 0.666 | 0.741 | 0.00% |
| UNITED_KINGDOM | EWU | international_equity | 0.98% | -0.32% | -6.13% | 16.15% | -3.94% | -0.353 | 0.605 | 0.701 | -0.64% |
| AUSTRALIA | EWA | international_equity | 3.54% | 4.19% | -7.56% | 18.54% | -6.84% | -0.888 | 0.675 | 0.925 | 0.00% |
| SOUTH_KOREA | EWY | international_equity | 17.29% | -9.65% | 36.81% | 82.99% | -34.21% | 0.560 | 0.644 | 2.727 | -22.84% |
| TAIWAN | EWT | international_equity | 13.75% | -3.13% | 39.00% | 44.86% | -19.83% | 0.093 | 0.758 | 1.830 | -8.81% |
| BRAZIL | EWZ | international_equity | 1.80% | 1.29% | -17.08% | 23.31% | -15.56% | -0.952 | 0.507 | 0.987 | -12.64% |
| MEXICO | EWW | international_equity | 1.48% | -0.75% | -12.34% | 19.86% | -7.30% | -0.624 | 0.540 | 0.924 | -4.21% |
| SOUTH_AFRICA | EZA | international_equity | 7.68% | 2.17% | -21.92% | 32.87% | -14.23% | -0.531 | 0.629 | 1.584 | -16.34% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | 0.49% | -3.12% | -8.75% | 5.01% | -1.93% | -0.363 | 0.392 | 0.133 | -1.62% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | 0.32% | -4.01% | -8.04% | 3.13% | -2.15% | 0.515 | 0.370 | 0.085 | -1.36% |
| EMERGING_MARKET_BONDS | EMB | credit | 1.08% | -3.32% | -7.06% | 5.85% | -2.10% | -0.652 | 0.682 | 0.301 | -0.86% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | 0.63% | -2.77% | -8.69% | 4.22% | -1.44% | -0.680 | 0.453 | 0.125 | -1.10% |
| SILVER | SLV | precious_metals | 8.31% | 0.00% | -38.25% | 50.78% | -36.50% | -0.612 | 0.354 | 1.693 | -46.90% |
| COPPER | CPER | non_energy_commodities | 6.52% | 6.30% | -9.26% | 28.95% | -10.57% | -0.562 | 0.558 | 1.215 | 0.00% |
| AGRICULTURE | DBA | non_energy_commodities | 0.51% | -2.66% | -2.02% | 14.10% | -8.67% | -0.408 | 0.076 | 0.065 | -3.83% |
| OIL | USO | energy | -11.16% | 2.52% | 31.58% | 54.46% | -32.49% | -0.536 | -0.333 | -1.224 | -24.90% |
| US_DOLLAR | UUP | currencies | -1.16% | -4.04% | -3.52% | 5.06% | -1.78% | -0.193 | -0.315 | -0.141 | -1.78% |
| EURO | FXE | currencies | 0.92% | -1.66% | -12.16% | 4.89% | -3.57% | -0.904 | 0.299 | 0.134 | -3.63% |
| YEN | FXY | currencies | 3.60% | -0.27% | -13.13% | 7.42% | -4.58% | 1.045 | 0.182 | 0.114 | -7.43% |
| BITCOIN_ETF | IBIT | crypto_assets | 2.06% | -1.32% | -25.53% | 36.69% | -28.36% | -0.631 | 0.503 | 1.735 | -48.46% |
| ETHEREUM_ETF | ETHA | crypto_assets | 1.69% | 4.23% | -31.10% | 53.05% | -34.41% | -0.403 | 0.535 | 2.786 | -60.43% |
