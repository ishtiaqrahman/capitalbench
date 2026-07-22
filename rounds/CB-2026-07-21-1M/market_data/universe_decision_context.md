# Full-Universe Horizon-Specific Decision Context

Profile: monthly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: yahoo_chart_adjusted_close_and_reported_volume
- As-of date requested: 2026-07-21
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | -0.47% |
| spy_return_21s | 0.21% |
| rsp_return_5s | -0.32% |
| rsp_return_21s | 1.73% |
| hyg_return_5s | -0.04% |
| hyg_return_21s | 0.01% |
| tlt_return_5s | -0.50% |
| tlt_return_21s | -3.21% |
| uup_return_5s | 0.32% |
| uup_return_21s | 0.64% |
| uso_return_5s | 7.22% |
| uso_return_21s | 12.17% |
| iau_return_5s | 0.72% |
| iau_return_21s | -3.16% |
| rsp_minus_spy_5s | 0.15% |
| rsp_minus_spy_21s | 1.52% |
| positive_asset_share_5s | 34.78% |
| positive_asset_share_21s | 49.28% |
| active_return_dispersion_5s |  |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_5s | active_return_21s | prior_105s_active_return | volatility_63s | max_drawdown_63s | volume_zscore_20v120 | corr_spy_252s | beta_spy_252s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | -0.21% | -8.54% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.05% | 0.08% | -7.05% | 0.21% | -0.01% | -0.112 | -0.117 | -0.002 | 0.00% |
| SP500 | SPY | diversified_us_equity | -0.47% | 0.00% | 0.00% | 13.02% | -4.49% | -0.891 | 1.000 | 1.000 | -1.23% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | -0.46% | -0.06% | 0.03% | 12.99% | -4.36% | -0.842 | 0.995 | 1.014 | -1.03% |
| NASDAQ100 | QQQ | technology_and_growth | -1.49% | -4.37% | 10.83% | 24.38% | -7.03% | -0.807 | 0.932 | 1.388 | -4.88% |
| LARGE_GROWTH | IWF | technology_and_growth | -1.54% | -1.72% | -3.64% | 18.85% | -8.21% | -0.600 | 0.935 | 1.258 | -5.69% |
| LARGE_VALUE | IWD | diversified_us_equity | 0.43% | 1.97% | 2.82% | 11.82% | -2.40% | -0.096 | 0.807 | 0.721 | -0.81% |
| MID_CAP | IJH | diversified_us_equity | 0.20% | -0.29% | 0.15% | 14.59% | -4.25% | -0.981 | 0.798 | 0.997 | -1.80% |
| SMALL_CAP | IWM | diversified_us_equity | 0.69% | 0.12% | 3.15% | 18.38% | -4.81% | -1.112 | 0.815 | 1.250 | -1.30% |
| SMALL_VALUE | IWN | diversified_us_equity | 1.51% | 2.58% | 3.18% | 15.43% | -4.01% | -0.552 | 0.731 | 1.014 | -0.57% |
| DIVIDEND | SCHD | diversified_us_equity | 1.93% | 3.63% | 2.64% | 11.90% | -2.95% | -0.428 | 0.314 | 0.274 | -0.67% |
| LOW_VOL | SPLV | diversified_us_equity | -0.05% | 3.79% | -7.80% | 13.42% | -4.09% | -0.751 | 0.044 | 0.037 | -1.39% |
| MOMENTUM | MTUM | diversified_us_equity | -1.65% | -7.31% | 22.74% | 36.38% | -12.49% | 1.536 | 0.787 | 1.518 | -8.90% |
| TECHNOLOGY | XLK | technology_and_growth | -1.55% | -5.66% | 23.09% | 33.40% | -11.31% | -0.837 | 0.863 | 1.687 | -8.68% |
| COMMUNICATIONS | XLC | technology_and_growth | -1.27% | 0.59% | -13.20% | 15.40% | -10.86% | 0.093 | 0.625 | 0.690 | -7.84% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | -0.89% | -1.97% | -12.55% | 18.44% | -7.02% | -0.343 | 0.796 | 1.178 | -7.38% |
| CONSUMER_STAPLES | XLP | consumer_defensive | 0.77% | 1.41% | -6.52% | 16.46% | -4.95% | -0.803 | -0.057 | -0.062 | -5.43% |
| HEALTHCARE | XLV | healthcare_and_biotech | 1.24% | 7.53% | -12.21% | 18.14% | -3.74% | -0.367 | 0.267 | 0.334 | -2.55% |
| FINANCIALS | XLF | financials | -0.12% | 4.90% | -9.63% | 13.14% | -3.34% | -0.713 | 0.558 | 0.646 | -1.13% |
| INDUSTRIALS | XLI | industrials_and_defense | -0.99% | -1.21% | 0.16% | 19.33% | -4.60% | -0.992 | 0.730 | 0.961 | -3.72% |
| ENERGY | XLE | energy | 2.72% | 9.38% | 4.95% | 24.19% | -13.21% | -0.904 | -0.122 | -0.202 | -5.82% |
| MATERIALS | XLB | materials_and_mining | -1.07% | -3.15% | -1.63% | 19.11% | -6.43% | -0.645 | 0.548 | 0.761 | -5.80% |
| UTILITIES | XLU | rate_sensitive_defensive | -1.69% | 0.79% | -4.66% | 17.53% | -8.00% | -0.708 | 0.136 | 0.160 | -4.62% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | 1.62% | 3.75% | -3.93% | 16.31% | -3.38% | -0.831 | 0.252 | 0.285 | -0.57% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | -0.26% | -0.99% | -8.58% | 5.00% | -2.53% | -0.838 | 0.209 | 0.078 | -3.22% |
| LONG_TREASURY | TLT | rates_and_duration | -0.50% | -3.41% | -7.86% | 8.82% | -4.28% | -0.823 | 0.168 | 0.125 | -6.15% |
| TIPS | TIP | rates_and_duration | -0.12% | -0.62% | -7.45% | 3.55% | -1.16% | -0.589 | 0.230 | 0.063 | -1.08% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | -0.34% | -1.90% | -8.01% | 5.29% | -2.26% | -0.413 | 0.412 | 0.173 | -2.55% |
| HIGH_YIELD_CREDIT | HYG | credit | -0.04% | -0.19% | -7.37% | 3.61% | -1.01% | -0.772 | 0.766 | 0.231 | -0.28% |
| AGGREGATE_BONDS | AGG | rates_and_duration | -0.27% | -1.05% | -8.05% | 4.14% | -1.89% | -0.177 | 0.319 | 0.096 | -2.00% |
| DEVELOPED_EX_US | VEA | international_equity | -0.18% | -2.75% | 3.24% | 21.16% | -4.85% | -0.590 | 0.797 | 1.081 | -2.65% |
| EMERGING_MARKETS | VWO | international_equity | -0.37% | -3.35% | 0.11% | 20.68% | -5.67% | -0.480 | 0.800 | 1.098 | -3.89% |
| EUROPE | VGK | international_equity | 0.52% | 0.35% | -4.22% | 18.36% | -4.16% | -1.011 | 0.739 | 0.932 | -1.34% |
| JAPAN | EWJ | international_equity | -1.22% | -3.86% | 4.69% | 22.56% | -6.74% | -0.663 | 0.707 | 1.176 | -4.36% |
| CHINA | MCHI | international_equity | 1.45% | 2.12% | -23.57% | 21.28% | -15.01% | -0.006 | 0.574 | 0.935 | -17.86% |
| INDIA | INDA | international_equity | 0.10% | -1.82% | -14.72% | 15.31% | -6.57% | -0.734 | 0.514 | 0.609 | -11.77% |
| GOLD | IAU | precious_metals | 0.72% | -3.37% | -16.58% | 24.27% | -17.41% | -0.575 | 0.301 | 0.663 | -24.37% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | 3.34% | 6.76% | 11.64% | 21.05% | -16.55% | 0.141 | -0.116 | -0.175 | -6.66% |
| SEMICONDUCTORS | SMH | technology_and_growth | -2.70% | -11.69% | 56.27% | 52.86% | -16.80% | 0.779 | 0.783 | 2.308 | -12.68% |
| SOFTWARE | IGV | technology_and_growth | -1.93% | 2.86% | -17.90% | 34.46% | -21.29% | -0.583 | 0.511 | 1.159 | -22.03% |
| BROAD_AI_TECH | AIQ | technology_and_growth | -1.55% | -8.89% | 19.09% | 39.44% | -16.31% | 0.809 | 0.849 | 1.873 | -13.03% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | -1.78% | -10.02% | -9.19% | 38.42% | -19.25% | -1.008 | 0.791 | 2.156 | -16.49% |
| CYBERSECURITY | CIBR | technology_and_growth | -4.38% | 7.03% | 9.23% | 32.74% | -11.74% | -0.073 | 0.529 | 1.080 | -4.38% |
| SOLAR | TAN | clean_energy | -2.52% | -11.50% | 8.23% | 45.69% | -28.73% | -0.865 | 0.581 | 1.783 | -27.31% |
| METALS_MINING | XME | materials_and_mining | -2.70% | -13.32% | -14.21% | 40.93% | -26.37% | -0.582 | 0.589 | 1.702 | -23.46% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | -0.32% | 1.52% | -2.60% | 10.80% | -2.04% | -0.728 | 0.776 | 0.722 | -1.07% |
| BIOTECH | XBI | healthcare_and_biotech | -0.61% | 9.69% | 4.78% | 30.59% | -8.12% | 0.160 | 0.480 | 1.014 | -5.95% |
| REGIONAL_BANKS | KRE | financials | 1.31% | 6.35% | -2.22% | 20.78% | -5.29% | -0.547 | 0.445 | 0.807 | -2.49% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | -2.35% | -4.08% | -10.37% | 25.72% | -8.58% | -0.466 | 0.581 | 1.015 | -8.39% |
| CANADA | EWC | international_equity | -0.22% | 1.83% | -3.07% | 13.40% | -3.20% | -0.739 | 0.677 | 0.766 | -0.74% |
| UNITED_KINGDOM | EWU | international_equity | 0.99% | 2.68% | -6.48% | 17.21% | -5.06% | -0.498 | 0.609 | 0.718 | -2.55% |
| AUSTRALIA | EWA | international_equity | -0.10% | 0.21% | -0.23% | 18.45% | -6.84% | -0.803 | 0.673 | 0.920 | -3.89% |
| SOUTH_KOREA | EWY | international_equity | -2.31% | -21.33% | 86.79% | 78.26% | -25.85% | 0.468 | 0.650 | 2.672 | -21.12% |
| TAIWAN | EWT | international_equity | -1.28% | -8.76% | 54.80% | 42.40% | -13.98% | 0.238 | 0.745 | 1.741 | -9.82% |
| BRAZIL | EWZ | international_equity | -1.14% | 5.40% | -5.88% | 22.99% | -18.43% | -1.083 | 0.510 | 1.003 | -13.83% |
| MEXICO | EWW | international_equity | 0.66% | -2.13% | -2.50% | 20.55% | -7.30% | -0.744 | 0.529 | 0.920 | -5.26% |
| SOUTH_AFRICA | EZA | international_equity | -1.84% | -6.89% | -14.83% | 32.98% | -14.54% | -0.503 | 0.621 | 1.581 | -22.00% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | -0.28% | -0.98% | -7.94% | 4.83% | -2.15% | -0.579 | 0.315 | 0.111 | -1.91% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | -0.73% | -1.02% | -7.47% | 2.70% | -1.36% | -0.486 | 0.310 | 0.071 | -1.30% |
| EMERGING_MARKET_BONDS | EMB | credit | -0.20% | -1.19% | -5.78% | 5.78% | -2.10% | -0.670 | 0.658 | 0.291 | -1.08% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | -0.27% | -1.05% | -7.79% | 4.25% | -1.23% | -0.417 | 0.405 | 0.113 | -1.67% |
| SILVER | SLV | precious_metals | -0.17% | -11.01% | -35.09% | 51.23% | -36.50% | -0.673 | 0.350 | 1.694 | -49.73% |
| COPPER | CPER | non_energy_commodities | 2.57% | 1.52% | -0.41% | 29.47% | -10.57% | -0.638 | 0.459 | 1.242 | -2.64% |
| AGRICULTURE | DBA | non_energy_commodities | 1.88% | 5.50% | -4.51% | 13.54% | -8.67% | -0.218 | 0.079 | 0.068 | -2.02% |
| OIL | USO | energy | 7.22% | 11.96% | 51.78% | 51.41% | -32.49% | -0.579 | -0.288 | -1.029 | -15.76% |
| US_DOLLAR | UUP | currencies | 0.32% | 0.43% | -5.37% | 4.95% | -0.98% | -0.137 | -0.274 | -0.130 | -0.18% |
| EURO | FXE | currencies | -0.15% | -0.65% | -9.42% | 4.73% | -3.58% | -0.759 | 0.257 | 0.125 | -4.93% |
| YEN | FXY | currencies | -0.62% | -1.31% | -10.82% | 6.54% | -4.21% | -0.398 | 0.107 | 0.068 | -10.55% |
| BITCOIN_ETF | IBIT | crypto_assets | 2.98% | 5.55% | -42.87% | 38.48% | -28.36% | -0.320 | 0.511 | 1.795 | -47.16% |
| ETHEREUM_ETF | ETHA | crypto_assets | 2.47% | 12.60% | -56.77% | 53.17% | -35.25% | -0.403 | 0.549 | 2.941 | -60.29% |
