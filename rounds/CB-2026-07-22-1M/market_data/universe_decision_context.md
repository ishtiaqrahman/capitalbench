# Full-Universe Horizon-Specific Decision Context

Profile: monthly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: yahoo_chart_adjusted_close_and_reported_volume
- As-of date requested: 2026-07-22
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | -0.98% |
| spy_return_21s | 0.41% |
| rsp_return_5s | -0.13% |
| rsp_return_21s | 1.47% |
| hyg_return_5s | -0.36% |
| hyg_return_21s | -0.06% |
| tlt_return_5s | -0.95% |
| tlt_return_21s | -2.72% |
| uup_return_5s | 0.71% |
| uup_return_21s | 0.32% |
| uso_return_5s | 8.49% |
| uso_return_21s | 16.85% |
| iau_return_5s | 1.85% |
| iau_return_21s | -1.41% |
| rsp_minus_spy_5s | 0.85% |
| rsp_minus_spy_21s | 1.07% |
| positive_asset_share_5s | 37.68% |
| positive_asset_share_21s | 47.83% |
| active_return_dispersion_5s |  |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_5s | active_return_21s | prior_105s_active_return | volatility_63s | max_drawdown_63s | volume_zscore_20v120 | corr_spy_252s | beta_spy_252s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | -0.41% | -10.44% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.07% | -0.10% | -8.96% | 0.21% | -0.01% | -0.155 | -0.118 | -0.002 | 0.00% |
| SP500 | SPY | diversified_us_equity | -0.98% | 0.00% | 0.00% | 12.94% | -4.49% | -0.946 | 1.000 | 1.000 | -1.35% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | -0.95% | -0.10% | -0.04% | 12.90% | -4.36% | -0.855 | 0.995 | 1.014 | -1.18% |
| NASDAQ100 | QQQ | technology_and_growth | -1.73% | -4.82% | 11.20% | 24.40% | -7.03% | -0.900 | 0.932 | 1.388 | -5.37% |
| LARGE_GROWTH | IWF | technology_and_growth | -2.15% | -1.10% | -4.07% | 18.80% | -8.21% | -0.585 | 0.935 | 1.258 | -6.01% |
| LARGE_VALUE | IWD | diversified_us_equity | 0.10% | 1.23% | 3.12% | 11.72% | -2.40% | -0.074 | 0.807 | 0.721 | -0.78% |
| MID_CAP | IJH | diversified_us_equity | 0.08% | -0.91% | 0.19% | 14.53% | -4.25% | -0.978 | 0.799 | 0.997 | -1.84% |
| SMALL_CAP | IWM | diversified_us_equity | -0.67% | -1.88% | 3.59% | 18.36% | -4.81% | -1.136 | 0.815 | 1.251 | -2.22% |
| SMALL_VALUE | IWN | diversified_us_equity | 0.34% | 1.46% | 3.34% | 15.27% | -4.01% | -0.557 | 0.732 | 1.014 | -0.95% |
| DIVIDEND | SCHD | diversified_us_equity | 1.73% | 3.58% | 1.61% | 11.89% | -2.95% | -0.461 | 0.314 | 0.274 | -0.42% |
| LOW_VOL | SPLV | diversified_us_equity | 1.15% | 3.83% | -8.62% | 13.26% | -4.09% | -0.802 | 0.043 | 0.036 | -0.78% |
| MOMENTUM | MTUM | diversified_us_equity | 0.50% | -9.38% | 26.37% | 36.33% | -12.49% | 1.478 | 0.787 | 1.518 | -8.97% |
| TECHNOLOGY | XLK | technology_and_growth | -0.72% | -6.59% | 25.36% | 33.41% | -11.31% | -0.911 | 0.863 | 1.688 | -8.94% |
| COMMUNICATIONS | XLC | technology_and_growth | -3.69% | 1.78% | -15.72% | 15.25% | -10.20% | 0.008 | 0.627 | 0.690 | -8.53% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | -2.55% | -1.21% | -13.57% | 18.43% | -7.02% | -0.378 | 0.796 | 1.178 | -8.07% |
| CONSUMER_STAPLES | XLP | consumer_defensive | 1.09% | 2.27% | -9.40% | 16.41% | -4.95% | -0.871 | -0.058 | -0.063 | -5.07% |
| HEALTHCARE | XLV | healthcare_and_biotech | 0.72% | 5.84% | -13.06% | 18.04% | -3.74% | -0.421 | 0.268 | 0.336 | -3.05% |
| FINANCIALS | XLF | financials | -0.90% | 3.97% | -8.63% | 13.06% | -2.73% | -0.732 | 0.559 | 0.647 | -1.23% |
| INDUSTRIALS | XLI | industrials_and_defense | -0.67% | -2.03% | 1.32% | 19.10% | -4.60% | -1.065 | 0.731 | 0.962 | -3.62% |
| ENERGY | XLE | energy | 4.78% | 9.10% | 4.69% | 24.14% | -13.21% | -0.929 | -0.122 | -0.203 | -4.69% |
| MATERIALS | XLB | materials_and_mining | 0.63% | -1.96% | -2.45% | 19.26% | -6.43% | -0.649 | 0.545 | 0.759 | -4.44% |
| UTILITIES | XLU | rate_sensitive_defensive | 1.57% | 2.30% | -4.95% | 17.75% | -8.00% | -0.744 | 0.132 | 0.157 | -2.48% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | 1.01% | 1.84% | -2.46% | 15.85% | -3.38% | -0.815 | 0.252 | 0.286 | -0.99% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | -0.73% | -1.04% | -10.47% | 4.94% | -2.24% | -0.879 | 0.210 | 0.078 | -3.44% |
| LONG_TREASURY | TLT | rates_and_duration | -0.95% | -3.13% | -9.21% | 8.77% | -4.23% | -0.824 | 0.168 | 0.124 | -6.40% |
| TIPS | TIP | rates_and_duration | -0.28% | -0.51% | -9.47% | 3.54% | -1.18% | -0.617 | 0.230 | 0.063 | -1.18% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | -0.85% | -2.00% | -9.57% | 5.25% | -2.42% | -0.436 | 0.413 | 0.173 | -2.71% |
| HIGH_YIELD_CREDIT | HYG | credit | -0.36% | -0.47% | -9.10% | 3.59% | -1.01% | -0.788 | 0.766 | 0.232 | -0.44% |
| AGGREGATE_BONDS | AGG | rates_and_duration | -0.57% | -1.14% | -9.85% | 4.08% | -1.66% | -0.233 | 0.319 | 0.096 | -2.16% |
| DEVELOPED_EX_US | VEA | international_equity | -0.47% | -3.03% | 2.98% | 20.68% | -4.85% | -0.640 | 0.797 | 1.081 | -2.62% |
| EMERGING_MARKETS | VWO | international_equity | -1.13% | -4.37% | -0.05% | 20.53% | -5.67% | -0.472 | 0.800 | 1.097 | -3.97% |
| EUROPE | VGK | international_equity | -0.03% | 0.55% | -4.66% | 17.81% | -3.86% | -1.041 | 0.738 | 0.932 | -0.98% |
| JAPAN | EWJ | international_equity | -1.40% | -5.34% | 6.01% | 22.01% | -6.74% | -0.760 | 0.707 | 1.176 | -4.93% |
| CHINA | MCHI | international_equity | -1.07% | 0.94% | -24.13% | 21.02% | -15.01% | -0.032 | 0.574 | 0.935 | -18.52% |
| INDIA | INDA | international_equity | -1.03% | -3.81% | -13.94% | 15.21% | -5.64% | -0.740 | 0.514 | 0.610 | -12.79% |
| GOLD | IAU | precious_metals | 1.85% | -1.81% | -22.45% | 23.87% | -16.13% | -0.552 | 0.300 | 0.660 | -23.51% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | 3.73% | 8.46% | 7.00% | 20.84% | -16.55% | 0.138 | -0.117 | -0.176 | -5.82% |
| SEMICONDUCTORS | SMH | technology_and_growth | -0.65% | -12.66% | 60.90% | 52.86% | -16.80% | 0.532 | 0.783 | 2.308 | -12.26% |
| SOFTWARE | IGV | technology_and_growth | -5.24% | 1.55% | -19.41% | 35.04% | -21.29% | -0.599 | 0.510 | 1.162 | -24.41% |
| BROAD_AI_TECH | AIQ | technology_and_growth | -1.60% | -10.76% | 21.26% | 39.55% | -16.31% | 0.064 | 0.849 | 1.874 | -14.26% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | -1.96% | -8.79% | -9.91% | 38.42% | -19.25% | -1.018 | 0.793 | 2.158 | -17.16% |
| CYBERSECURITY | CIBR | technology_and_growth | -4.04% | 6.57% | 9.20% | 32.89% | -11.74% | 0.024 | 0.529 | 1.081 | -5.70% |
| SOLAR | TAN | clean_energy | -3.73% | -12.50% | 8.24% | 45.58% | -28.73% | -0.931 | 0.581 | 1.783 | -27.34% |
| METALS_MINING | XME | materials_and_mining | 0.29% | -10.58% | -18.73% | 41.05% | -26.37% | -0.561 | 0.587 | 1.699 | -22.03% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | -0.13% | 1.07% | -2.67% | 10.71% | -2.04% | -0.780 | 0.777 | 0.722 | -1.10% |
| BIOTECH | XBI | healthcare_and_biotech | -2.63% | 3.88% | 6.09% | 30.69% | -8.12% | 0.103 | 0.480 | 1.016 | -7.41% |
| REGIONAL_BANKS | KRE | financials | -0.24% | 4.61% | -1.68% | 20.58% | -5.29% | -0.621 | 0.445 | 0.808 | -2.98% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | -2.25% | -2.27% | -11.31% | 24.57% | -8.58% | -0.478 | 0.581 | 1.015 | -7.84% |
| CANADA | EWC | international_equity | -0.35% | 2.00% | -4.21% | 13.00% | -3.20% | -0.633 | 0.676 | 0.766 | -0.35% |
| UNITED_KINGDOM | EWU | international_equity | 1.00% | 2.99% | -6.76% | 16.74% | -3.94% | -0.490 | 0.607 | 0.717 | -1.57% |
| AUSTRALIA | EWA | international_equity | 0.21% | 1.04% | -1.41% | 18.11% | -6.84% | -0.787 | 0.672 | 0.919 | -3.29% |
| SOUTH_KOREA | EWY | international_equity | -0.70% | -22.59% | 86.92% | 78.17% | -25.85% | 0.322 | 0.650 | 2.673 | -22.25% |
| TAIWAN | EWT | international_equity | -0.79% | -9.24% | 57.17% | 42.42% | -13.98% | 0.135 | 0.745 | 1.740 | -8.83% |
| BRAZIL | EWZ | international_equity | 2.06% | 6.45% | -7.54% | 23.67% | -17.41% | -1.075 | 0.505 | 0.999 | -11.41% |
| MEXICO | EWW | international_equity | 1.75% | 0.58% | -7.14% | 20.15% | -7.30% | -0.755 | 0.528 | 0.919 | -4.17% |
| SOUTH_AFRICA | EZA | international_equity | -1.19% | -3.72% | -19.80% | 32.34% | -12.47% | -0.568 | 0.621 | 1.579 | -21.13% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | -0.72% | -1.22% | -9.65% | 4.79% | -1.97% | -0.557 | 0.315 | 0.111 | -2.18% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | -0.82% | -1.48% | -9.02% | 2.73% | -1.57% | -0.432 | 0.310 | 0.071 | -1.57% |
| EMERGING_MARKET_BONDS | EMB | credit | -0.67% | -1.35% | -7.52% | 5.73% | -2.10% | -0.692 | 0.658 | 0.292 | -1.38% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | -0.48% | -1.15% | -9.55% | 4.19% | -1.26% | -0.412 | 0.406 | 0.113 | -1.73% |
| SILVER | SLV | precious_metals | 3.28% | -8.88% | -41.45% | 50.51% | -36.50% | -0.666 | 0.349 | 1.691 | -48.94% |
| COPPER | CPER | non_energy_commodities | 1.60% | 0.73% | -1.76% | 29.40% | -10.57% | -0.675 | 0.459 | 1.243 | -3.33% |
| AGRICULTURE | DBA | non_energy_commodities | 0.89% | 5.52% | -5.89% | 13.49% | -8.67% | -0.287 | 0.079 | 0.068 | -1.74% |
| OIL | USO | energy | 8.49% | 16.45% | 46.37% | 50.34% | -32.49% | -0.573 | -0.288 | -1.030 | -13.91% |
| US_DOLLAR | UUP | currencies | 0.71% | -0.09% | -6.22% | 4.86% | -0.98% | -0.199 | -0.274 | -0.130 | -0.28% |
| EURO | FXE | currencies | -0.45% | -0.43% | -12.69% | 4.64% | -3.57% | -0.765 | 0.257 | 0.125 | -4.83% |
| YEN | FXY | currencies | -0.53% | -1.39% | -12.77% | 6.48% | -4.21% | -0.380 | 0.107 | 0.067 | -10.53% |
| BITCOIN_ETF | IBIT | crypto_assets | 1.44% | 1.90% | -38.54% | 38.38% | -28.36% | -0.337 | 0.512 | 1.796 | -47.62% |
| ETHEREUM_ETF | ETHA | crypto_assets | 0.00% | 10.77% | -52.83% | 53.11% | -35.25% | -0.360 | 0.550 | 2.937 | -60.32% |
