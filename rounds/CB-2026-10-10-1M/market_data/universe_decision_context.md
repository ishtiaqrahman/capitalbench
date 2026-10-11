# Full-Universe Horizon-Specific Decision Context

Profile: monthly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: tiingo_eod_history_through_2026-09-25; repository_daily_price_snapshots_2026-09-28_to_2026-10-09_(tiingo_eod_or_yahoo_chart_adjclose); yahoo_chart_reported_volume_2026-09-28_to_2026-10-09
- As-of date requested: 2026-10-09
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | 1.16% |
| spy_return_21s | 2.99% |
| rsp_return_5s | 1.58% |
| rsp_return_21s | 0.31% |
| hyg_return_5s | 0.42% |
| hyg_return_21s | -1.77% |
| tlt_return_5s | 0.65% |
| tlt_return_21s | -3.47% |
| uup_return_5s | 0.45% |
| uup_return_21s | 3.53% |
| uso_return_5s | 0.56% |
| uso_return_21s | -6.43% |
| iau_return_5s | 1.18% |
| iau_return_21s | -2.95% |
| rsp_minus_spy_5s | 0.42% |
| rsp_minus_spy_21s | -2.68% |
| positive_asset_share_5s | 71.01% |
| positive_asset_share_21s | 37.68% |
| active_return_dispersion_5s |  |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_5s | active_return_21s | prior_105s_active_return | volatility_63s | max_drawdown_63s | volume_zscore_20v120 | corr_spy_252s | beta_spy_252s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | -2.99% | -11.82% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.09% | -2.95% | -10.34% | 0.56% | -0.26% | 0.304 | -0.050 | -0.001 | -0.15% |
| SP500 | SPY | diversified_us_equity | 1.16% | 0.00% | 0.00% | 10.91% | -3.36% | -0.427 | 1.000 | 1.000 | -0.07% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | 1.05% | -0.66% | -0.10% | 11.10% | -3.39% | -0.375 | 0.995 | 1.012 | -0.61% |
| NASDAQ100 | QQQ | technology_and_growth | 0.23% | 3.12% | 4.28% | 18.25% | -8.05% | -0.586 | 0.928 | 1.424 | -1.10% |
| LARGE_GROWTH | IWF | technology_and_growth | 0.66% | 2.54% | -2.98% | 17.50% | -7.71% | -0.415 | 0.934 | 1.289 | -0.99% |
| LARGE_VALUE | IWD | diversified_us_equity | 1.67% | -2.54% | 2.73% | 8.85% | -4.06% | -0.313 | 0.807 | 0.703 | -1.89% |
| MID_CAP | IJH | diversified_us_equity | 0.05% | -3.27% | -6.72% | 11.85% | -8.26% | 0.112 | 0.812 | 0.964 | -6.37% |
| SMALL_CAP | IWM | diversified_us_equity | -0.92% | -5.78% | -1.46% | 13.06% | -8.78% | -0.079 | 0.820 | 1.175 | -8.33% |
| SMALL_VALUE | IWN | diversified_us_equity | -0.69% | -6.30% | -1.57% | 10.90% | -7.53% | 0.312 | 0.737 | 0.919 | -6.90% |
| DIVIDEND | SCHD | diversified_us_equity | 0.98% | -5.01% | 0.29% | 11.48% | -6.87% | 0.168 | 0.294 | 0.255 | -5.41% |
| LOW_VOL | SPLV | diversified_us_equity | 1.76% | -4.88% | -11.59% | 9.64% | -9.22% | -0.775 | 0.035 | 0.029 | -7.12% |
| MOMENTUM | MTUM | diversified_us_equity | -0.89% | 2.78% | 3.38% | 26.29% | -11.46% | 0.429 | 0.765 | 1.563 | -7.12% |
| TECHNOLOGY | XLK | technology_and_growth | -0.52% | 4.45% | 18.21% | 24.95% | -9.29% | -0.773 | 0.851 | 1.732 | -1.59% |
| COMMUNICATIONS | XLC | technology_and_growth | 0.05% | -3.68% | -13.71% | 20.63% | -7.06% | 0.230 | 0.550 | 0.680 | -7.25% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | 2.55% | -1.98% | -12.44% | 18.85% | -9.02% | -0.347 | 0.778 | 1.160 | -8.81% |
| CONSUMER_STAPLES | XLP | consumer_defensive | 3.60% | -1.92% | -10.24% | 15.46% | -7.54% | -0.260 | -0.044 | -0.050 | -5.52% |
| HEALTHCARE | XLV | healthcare_and_biotech | 2.79% | 0.51% | 1.13% | 16.99% | -5.87% | -0.512 | 0.228 | 0.276 | -2.40% |
| FINANCIALS | XLF | financials | 2.32% | -6.42% | 0.59% | 12.09% | -8.49% | 0.350 | 0.545 | 0.621 | -6.21% |
| INDUSTRIALS | XLI | industrials_and_defense | -0.41% | -3.49% | -12.14% | 14.84% | -10.23% | -0.205 | 0.703 | 0.941 | -9.01% |
| ENERGY | XLE | energy | 3.60% | -2.15% | 3.03% | 20.60% | -6.15% | -0.080 | -0.174 | -0.295 | -0.69% |
| MATERIALS | XLB | materials_and_mining | 1.17% | -5.16% | -13.76% | 16.13% | -9.14% | 0.050 | 0.532 | 0.733 | -7.48% |
| UTILITIES | XLU | rate_sensitive_defensive | 3.97% | -4.88% | -20.70% | 14.87% | -14.58% | 2.515 | 0.131 | 0.155 | -11.44% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | 1.96% | -5.53% | -10.41% | 12.99% | -11.09% | 0.519 | 0.268 | 0.294 | -8.81% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | 0.39% | -4.94% | -14.47% | 5.11% | -4.58% | 0.626 | 0.311 | 0.115 | -6.62% |
| LONG_TREASURY | TLT | rates_and_duration | 0.65% | -6.46% | -16.61% | 9.94% | -8.05% | 1.811 | 0.268 | 0.193 | -11.83% |
| TIPS | TIP | rates_and_duration | 0.30% | -4.79% | -12.77% | 3.80% | -3.40% | 0.144 | 0.280 | 0.076 | -3.55% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | 0.57% | -4.86% | -14.35% | 5.83% | -4.54% | 0.763 | 0.483 | 0.203 | -5.80% |
| HIGH_YIELD_CREDIT | HYG | credit | 0.42% | -4.76% | -10.98% | 3.38% | -3.25% | 1.815 | 0.763 | 0.231 | -2.83% |
| AGGREGATE_BONDS | AGG | rates_and_duration | 0.36% | -4.51% | -13.46% | 4.36% | -3.62% | 1.038 | 0.408 | 0.124 | -4.50% |
| DEVELOPED_EX_US | VEA | international_equity | -1.10% | -4.93% | -5.09% | 14.78% | -5.09% | -0.361 | 0.803 | 1.093 | -4.42% |
| EMERGING_MARKETS | VWO | international_equity | 0.34% | -3.10% | -6.07% | 14.46% | -4.30% | -0.315 | 0.822 | 1.137 | -2.55% |
| EUROPE | VGK | international_equity | -0.41% | -6.54% | -7.71% | 12.21% | -8.10% | 0.064 | 0.745 | 0.912 | -7.45% |
| JAPAN | EWJ | international_equity | -1.07% | -1.52% | -1.81% | 19.56% | -4.84% | -0.540 | 0.735 | 1.197 | -1.47% |
| CHINA | MCHI | international_equity | 2.56% | -3.47% | -18.87% | 16.61% | -9.99% | -0.725 | 0.577 | 0.879 | -18.36% |
| INDIA | INDA | international_equity | -1.05% | -7.31% | -14.31% | 12.53% | -9.84% | -0.444 | 0.581 | 0.694 | -16.75% |
| GOLD | IAU | precious_metals | 1.18% | -5.94% | -21.07% | 24.02% | -12.19% | -0.460 | 0.334 | 0.753 | -22.35% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | 1.13% | -4.94% | 6.33% | 20.62% | -6.42% | -0.213 | -0.189 | -0.302 | -2.19% |
| SEMICONDUCTORS | SMH | technology_and_growth | -4.32% | 4.69% | 16.43% | 37.37% | -16.01% | -0.742 | 0.770 | 2.359 | -9.80% |
| SOFTWARE | IGV | technology_and_growth | 3.91% | 8.34% | 23.74% | 32.52% | -8.27% | -1.204 | 0.492 | 1.209 | -3.75% |
| BROAD_AI_TECH | AIQ | technology_and_growth | 0.56% | 2.59% | 15.95% | 25.42% | -9.65% | -0.673 | 0.851 | 1.922 | -5.05% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | -0.78% | -0.49% | -10.72% | 28.79% | -10.40% | -0.785 | 0.813 | 2.178 | -14.12% |
| CYBERSECURITY | CIBR | technology_and_growth | 5.06% | 13.83% | 43.34% | 32.90% | -9.53% | 0.667 | 0.497 | 1.118 | 0.00% |
| SOLAR | TAN | clean_energy | -0.68% | -9.99% | -26.65% | 34.42% | -22.94% | -0.682 | 0.649 | 1.926 | -40.82% |
| METALS_MINING | XME | materials_and_mining | 0.58% | -10.27% | -10.68% | 36.32% | -15.75% | -0.824 | 0.599 | 1.775 | -19.83% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | 1.58% | -2.68% | -3.00% | 9.93% | -6.27% | -0.407 | 0.776 | 0.700 | -4.01% |
| BIOTECH | XBI | healthcare_and_biotech | -0.43% | -4.94% | 9.45% | 28.98% | -11.95% | 0.398 | 0.471 | 1.032 | -9.31% |
| REGIONAL_BANKS | KRE | financials | -2.50% | -8.96% | -4.13% | 15.63% | -11.09% | 0.630 | 0.420 | 0.714 | -10.94% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | -0.55% | -8.23% | -16.68% | 20.08% | -19.50% | 0.318 | 0.566 | 1.015 | -18.29% |
| CANADA | EWC | international_equity | 0.53% | -5.08% | -5.10% | 12.79% | -7.50% | -0.043 | 0.674 | 0.764 | -5.76% |
| UNITED_KINGDOM | EWU | international_equity | 0.74% | -5.12% | -10.67% | 11.11% | -7.09% | -0.303 | 0.603 | 0.698 | -5.81% |
| AUSTRALIA | EWA | international_equity | 1.06% | -4.57% | -12.99% | 16.42% | -8.02% | 0.257 | 0.681 | 0.952 | -5.95% |
| SOUTH_KOREA | EWY | international_equity | -7.63% | -6.02% | 19.93% | 56.26% | -18.52% | -0.823 | 0.638 | 2.812 | -19.14% |
| TAIWAN | EWT | international_equity | -1.74% | 1.96% | 29.75% | 31.82% | -12.76% | -0.603 | 0.758 | 1.872 | -3.13% |
| BRAZIL | EWZ | international_equity | 14.01% | 9.92% | -17.63% | 33.53% | -8.05% | 1.567 | 0.460 | 1.005 | 0.00% |
| MEXICO | EWW | international_equity | 1.21% | -7.38% | -15.79% | 17.04% | -10.38% | -0.194 | 0.567 | 0.963 | -10.13% |
| SOUTH_AFRICA | EZA | international_equity | 0.97% | -11.25% | -13.38% | 27.33% | -14.09% | -0.197 | 0.628 | 1.611 | -20.16% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | 0.64% | -4.84% | -13.75% | 5.63% | -4.64% | 5.001 | 0.401 | 0.147 | -5.01% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | 0.12% | -4.59% | -14.37% | 4.56% | -5.72% | 5.265 | 0.362 | 0.095 | -5.52% |
| EMERGING_MARKET_BONDS | EMB | credit | 1.14% | -5.39% | -11.89% | 5.91% | -5.08% | 0.928 | 0.688 | 0.316 | -4.61% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | 0.26% | -2.96% | -12.79% | 3.65% | -2.25% | 0.334 | 0.478 | 0.137 | -2.93% |
| SILVER | SLV | precious_metals | 0.07% | -7.72% | -28.58% | 37.73% | -14.85% | -0.619 | 0.372 | 1.795 | -48.13% |
| COPPER | CPER | non_energy_commodities | 2.00% | 0.26% | -2.98% | 23.06% | -6.80% | -0.459 | 0.576 | 1.274 | -2.70% |
| AGRICULTURE | DBA | non_energy_commodities | 0.43% | -6.37% | -2.78% | 13.15% | -4.61% | -0.312 | 0.066 | 0.057 | -3.93% |
| OIL | USO | energy | 0.56% | -9.42% | 15.07% | 49.14% | -17.64% | -0.448 | -0.351 | -1.338 | -8.44% |
| US_DOLLAR | UUP | currencies | 0.45% | 0.54% | -9.67% | 5.29% | -2.52% | -0.165 | -0.297 | -0.126 | -0.07% |
| EURO | FXE | currencies | -0.43% | -6.50% | -12.52% | 4.77% | -4.07% | -0.318 | 0.279 | 0.117 | -6.46% |
| YEN | FXY | currencies | -0.29% | -5.52% | -8.77% | 9.88% | -3.38% | -0.223 | 0.185 | 0.117 | -5.31% |
| BITCOIN_ETF | IBIT | crypto_assets | -2.47% | 3.58% | -6.72% | 37.56% | -7.14% | -0.026 | 0.500 | 1.746 | -32.28% |
| ETHEREUM_ETF | ETHA | crypto_assets | 178.42% | 198.68% | -2.96% | 397.81% | -8.52% | -0.327 | 0.195 | 3.124 | -8.05% |
