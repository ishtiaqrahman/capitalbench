# Full-Universe Horizon-Specific Decision Context

Profile: weekly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: tiingo_eod_adjusted_price_and_volume; yahoo_chart_adjusted_close_and_reported_volume
- As-of date requested: 2026-07-28
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | -0.99% |
| spy_return_21s | 1.63% |
| rsp_return_5s | 2.32% |
| rsp_return_21s | 3.51% |
| hyg_return_5s | -0.29% |
| hyg_return_21s | -0.05% |
| tlt_return_5s | 0.69% |
| tlt_return_21s | -3.21% |
| uup_return_5s | 0.35% |
| uup_return_21s | 0.42% |
| uso_return_5s | -6.49% |
| uso_return_21s | 14.23% |
| iau_return_5s | -1.46% |
| iau_return_21s | -1.12% |
| rsp_minus_spy_5s | 3.31% |
| rsp_minus_spy_21s | 1.88% |
| positive_asset_share_5s | 43.48% |
| positive_asset_share_21s | 50.72% |
| active_return_dispersion_5s | 3.38% |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_3s | active_return_5s | prior_16s_active_return | volatility_21s | max_drawdown_21s | volume_zscore_5v60 | corr_spy_63s | beta_spy_63s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | 0.99% | -2.65% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.05% | 1.07% | -2.43% | 0.23% | -0.01% | -0.664 | -0.186 | -0.003 | 0.00% |
| SP500 | SPY | diversified_us_equity | 0.36% | 0.00% | 0.00% | 11.04% | -2.22% | -0.572 | 1.000 | 1.000 | -2.21% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | 0.36% | 0.06% | -0.65% | 10.42% | -2.15% | -0.765 | 0.992 | 0.990 | -1.95% |
| NASDAQ100 | QQQ | technology_and_growth | -2.38% | -3.73% | -2.30% | 22.85% | -8.27% | -0.164 | 0.909 | 1.715 | -9.37% |
| LARGE_GROWTH | IWF | technology_and_growth | -1.78% | -3.01% | -0.72% | 21.65% | -6.19% | -0.674 | 0.881 | 1.271 | -9.47% |
| LARGE_VALUE | IWD | diversified_us_equity | 2.38% | 2.85% | -0.72% | 9.09% | -1.31% | -0.267 | 0.716 | 0.662 | 0.00% |
| MID_CAP | IJH | diversified_us_equity | 0.77% | 1.40% | -3.30% | 10.84% | -3.09% | -0.898 | 0.786 | 0.882 | -1.40% |
| SMALL_CAP | IWM | diversified_us_equity | 0.44% | -0.08% | -3.74% | 11.05% | -3.09% | -0.735 | 0.778 | 1.104 | -2.36% |
| SMALL_VALUE | IWN | diversified_us_equity | 1.60% | 1.53% | -1.98% | 10.35% | -1.83% | 0.027 | 0.679 | 0.808 | -0.03% |
| DIVIDEND | SCHD | diversified_us_equity | 3.32% | 4.25% | -0.37% | 13.87% | -1.18% | 0.355 | 0.140 | 0.131 | 0.00% |
| LOW_VOL | SPLV | diversified_us_equity | 2.11% | 3.95% | -2.50% | 14.51% | -1.89% | -0.801 | -0.280 | -0.283 | 0.00% |
| MOMENTUM | MTUM | diversified_us_equity | -6.90% | -6.05% | -6.10% | 37.40% | -14.73% | 0.091 | 0.725 | 2.083 | -15.32% |
| TECHNOLOGY | XLK | technology_and_growth | -4.12% | -4.37% | -2.83% | 29.97% | -10.20% | -1.072 | 0.823 | 2.106 | -13.58% |
| COMMUNICATIONS | XLC | technology_and_growth | 4.07% | 0.66% | 0.98% | 22.17% | -7.06% | 0.350 | 0.478 | 0.633 | -8.14% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | 3.42% | -1.09% | -2.21% | 23.58% | -7.90% | 0.040 | 0.728 | 1.171 | -9.31% |
| CONSUMER_STAPLES | XLP | consumer_defensive | 4.63% | 4.56% | -3.41% | 20.33% | -3.03% | 0.110 | -0.260 | -0.341 | -2.06% |
| HEALTHCARE | XLV | healthcare_and_biotech | 3.61% | 5.37% | -2.70% | 20.33% | -3.74% | -0.891 | -0.106 | -0.150 | 0.00% |
| FINANCIALS | XLF | financials | 3.17% | 3.65% | 2.10% | 14.16% | -2.08% | -0.782 | 0.197 | 0.200 | 0.00% |
| INDUSTRIALS | XLI | industrials_and_defense | 0.30% | 3.14% | -4.05% | 13.20% | -4.01% | -0.984 | 0.634 | 0.929 | -1.65% |
| ENERGY | XLE | energy | -3.05% | -0.60% | 6.01% | 20.76% | -3.44% | -0.339 | -0.372 | -0.704 | -7.32% |
| MATERIALS | XLB | materials_and_mining | 4.08% | 5.46% | -5.55% | 19.26% | -3.81% | -0.153 | 0.531 | 0.823 | -1.59% |
| UTILITIES | XLU | rate_sensitive_defensive | -1.45% | 2.33% | -5.42% | 16.46% | -3.10% | -0.818 | -0.070 | -0.093 | -3.36% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | 2.36% | 2.78% | -2.73% | 16.55% | -2.67% | -0.264 | -0.078 | -0.097 | 0.00% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | 0.76% | 1.26% | -4.13% | 4.20% | -2.00% | -0.967 | 0.516 | 0.200 | -2.96% |
| LONG_TREASURY | TLT | rates_and_duration | 1.29% | 1.68% | -6.53% | 7.61% | -4.54% | -0.411 | 0.390 | 0.267 | -5.50% |
| TIPS | TIP | rates_and_duration | 0.16% | 0.79% | -3.34% | 3.00% | -1.33% | -0.059 | 0.545 | 0.149 | -1.28% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | 0.54% | 0.97% | -4.72% | 4.77% | -2.82% | 0.093 | 0.558 | 0.228 | -2.57% |
| HIGH_YIELD_CREDIT | HYG | credit | 0.24% | 0.70% | -2.41% | 2.58% | -0.80% | 0.278 | 0.767 | 0.216 | -0.56% |
| AGGREGATE_BONDS | AGG | rates_and_duration | 0.60% | 1.18% | -3.93% | 3.52% | -1.71% | -0.291 | 0.554 | 0.177 | -1.82% |
| DEVELOPED_EX_US | VEA | international_equity | -0.26% | -0.24% | -2.77% | 15.52% | -3.70% | -0.957 | 0.834 | 1.328 | -3.85% |
| EMERGING_MARKETS | VWO | international_equity | -0.62% | -0.91% | -2.17% | 17.42% | -3.88% | -0.983 | 0.862 | 1.340 | -5.72% |
| EUROPE | VGK | international_equity | 1.59% | 1.52% | -0.78% | 13.84% | -2.53% | -0.513 | 0.730 | 1.012 | -0.82% |
| JAPAN | EWJ | international_equity | -1.39% | -2.15% | -2.71% | 21.18% | -5.71% | -1.002 | 0.779 | 1.345 | -7.36% |
| CHINA | MCHI | international_equity | 1.99% | 1.75% | 4.33% | 19.19% | -2.22% | -1.060 | 0.492 | 0.791 | -17.24% |
| INDIA | INDA | international_equity | 3.67% | 2.22% | -4.22% | 14.05% | -4.51% | 0.723 | 0.565 | 0.691 | -10.69% |
| GOLD | IAU | precious_metals | -0.59% | -0.47% | -2.31% | 21.10% | -4.47% | -0.565 | 0.678 | 1.256 | -25.47% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | -5.54% | -2.35% | 8.57% | 22.72% | -5.54% | -0.333 | -0.122 | -0.206 | -9.78% |
| SEMICONDUCTORS | SMH | technology_and_growth | -8.72% | -8.34% | -7.15% | 48.91% | -19.25% | 1.738 | 0.767 | 3.141 | -20.83% |
| SOFTWARE | IGV | technology_and_growth | 5.37% | 0.95% | 1.46% | 25.94% | -8.11% | 0.053 | 0.326 | 0.840 | -22.07% |
| BROAD_AI_TECH | AIQ | technology_and_growth | -3.52% | -5.17% | -6.05% | 33.78% | -12.76% | -0.662 | 0.811 | 2.445 | -18.39% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | -2.79% | -4.43% | -5.48% | 33.73% | -14.09% | -0.647 | 0.843 | 2.509 | -21.02% |
| CYBERSECURITY | CIBR | technology_and_growth | 1.78% | -0.44% | 3.47% | 27.90% | -7.40% | -0.646 | 0.430 | 1.070 | -5.75% |
| SOLAR | TAN | clean_energy | -7.10% | -7.64% | -8.12% | 39.14% | -16.99% | 0.186 | 0.727 | 2.567 | -33.59% |
| METALS_MINING | XME | materials_and_mining | -1.68% | 0.83% | -8.58% | 30.36% | -9.51% | -0.213 | 0.676 | 2.074 | -23.58% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | 2.72% | 3.31% | -1.48% | 10.23% | -1.46% | -0.793 | 0.714 | 0.611 | 0.00% |
| BIOTECH | XBI | healthcare_and_biotech | -1.61% | -2.06% | -3.21% | 26.22% | -8.83% | -0.529 | 0.357 | 0.838 | -8.83% |
| REGIONAL_BANKS | KRE | financials | 2.18% | 2.06% | -1.57% | 20.09% | -3.73% | -0.733 | 0.200 | 0.312 | -1.45% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | 2.83% | 7.63% | -5.62% | 22.21% | -8.58% | -0.219 | 0.451 | 0.870 | -2.31% |
| CANADA | EWC | international_equity | 1.73% | 2.33% | -0.48% | 9.18% | -1.46% | -0.174 | 0.603 | 0.615 | 0.00% |
| UNITED_KINGDOM | EWU | international_equity | 2.40% | 3.24% | -0.44% | 14.72% | -1.93% | -0.573 | 0.487 | 0.638 | -0.35% |
| AUSTRALIA | EWA | international_equity | 2.91% | 3.22% | -0.11% | 13.55% | -1.63% | -0.655 | 0.616 | 0.884 | -1.73% |
| SOUTH_KOREA | EWY | international_equity | -12.89% | -11.41% | -15.00% | 66.98% | -24.99% | -0.027 | 0.699 | 4.256 | -30.91% |
| TAIWAN | EWT | international_equity | -5.90% | -5.60% | -4.82% | 41.36% | -13.50% | -0.854 | 0.767 | 2.487 | -15.76% |
| BRAZIL | EWZ | international_equity | -0.33% | 2.20% | 0.09% | 20.75% | -2.43% | -0.802 | 0.430 | 0.790 | -12.79% |
| MEXICO | EWW | international_equity | 2.37% | 2.23% | -2.02% | 16.51% | -2.98% | -0.320 | 0.634 | 0.996 | -4.10% |
| SOUTH_AFRICA | EZA | international_equity | 2.56% | 0.51% | -3.80% | 23.05% | -6.50% | 0.395 | 0.771 | 1.957 | -22.44% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | 0.85% | 1.27% | -3.89% | 4.31% | -1.85% | -0.377 | 0.559 | 0.210 | -1.63% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | 0.70% | 0.83% | -3.71% | 3.35% | -2.15% | 3.242 | 0.566 | 0.135 | -1.46% |
| EMERGING_MARKET_BONDS | EMB | credit | 0.70% | 0.79% | -3.44% | 4.55% | -1.96% | -0.250 | 0.735 | 0.327 | -1.27% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | 0.59% | 1.33% | -3.82% | 3.47% | -1.44% | -0.780 | 0.541 | 0.174 | -1.34% |
| SILVER | SLV | precious_metals | -0.69% | -1.61% | -3.02% | 36.79% | -10.19% | -0.969 | 0.645 | 2.511 | -51.04% |
| COPPER | CPER | non_energy_commodities | 0.24% | -2.04% | 3.25% | 21.36% | -3.26% | -0.682 | 0.715 | 1.617 | -5.59% |
| AGRICULTURE | DBA | non_energy_commodities | -1.42% | -0.11% | 2.39% | 16.40% | -2.20% | -0.764 | 0.032 | 0.035 | -3.10% |
| OIL | USO | energy | -13.62% | -5.50% | 19.51% | 58.56% | -13.62% | 0.449 | -0.301 | -1.260 | -21.23% |
| US_DOLLAR | UUP | currencies | 0.07% | 1.34% | -2.58% | 4.42% | -0.88% | -1.147 | -0.532 | -0.200 | -0.07% |
| EURO | FXE | currencies | 0.08% | 0.88% | -2.45% | 3.94% | -0.82% | -0.729 | 0.569 | 0.202 | -5.03% |
| YEN | FXY | currencies | -0.02% | 0.60% | -3.51% | 5.39% | -1.67% | 0.773 | 0.199 | 0.100 | -10.86% |
| BITCOIN_ETF | IBIT | crypto_assets | -1.39% | -3.07% | 8.64% | 31.78% | -4.06% | -0.789 | 0.463 | 1.321 | -49.31% |
| ETHEREUM_ETF | ETHA | crypto_assets | 2.69% | 0.72% | 19.56% | 47.01% | -4.20% | 0.343 | 0.560 | 2.291 | -60.40% |
