# Full-Universe Horizon-Specific Decision Context

Profile: monthly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: tiingo_eod_history_through_2026-09-25; repository_daily_price_snapshots_2026-09-28_to_2026-10-12_(tiingo_eod_or_yahoo_chart_adjclose); yahoo_chart_reported_volume_2026-09-28_to_2026-10-12
- As-of date requested: 2026-10-12
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | 0.42% |
| spy_return_21s | 2.06% |
| rsp_return_5s | 0.98% |
| rsp_return_21s | -0.41% |
| hyg_return_5s | 0.40% |
| hyg_return_21s | -1.67% |
| tlt_return_5s | 1.22% |
| tlt_return_21s | -3.49% |
| uup_return_5s | 0.48% |
| uup_return_21s | 3.78% |
| uso_return_5s | 4.89% |
| uso_return_21s | -2.50% |
| iau_return_5s | 0.67% |
| iau_return_21s | -4.12% |
| rsp_minus_spy_5s | 0.56% |
| rsp_minus_spy_21s | -2.47% |
| positive_asset_share_5s | 55.07% |
| positive_asset_share_21s | 31.88% |
| active_return_dispersion_5s |  |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_5s | active_return_21s | prior_105s_active_return | volatility_63s | max_drawdown_63s | volume_zscore_20v120 | corr_spy_252s | beta_spy_252s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | -2.06% | -11.68% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.07% | -2.06% | -10.17% | 0.56% | -0.26% | 0.309 | -0.051 | -0.001 | -0.16% |
| SP500 | SPY | diversified_us_equity | 0.42% | 0.00% | 0.00% | 10.89% | -3.36% | -0.484 | 1.000 | 1.000 | -0.13% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | 0.25% | -0.66% | -0.25% | 11.09% | -3.39% | -0.422 | 0.995 | 1.012 | -0.71% |
| NASDAQ100 | QQQ | technology_and_growth | -1.34% | 2.41% | 4.24% | 18.20% | -8.05% | -0.614 | 0.928 | 1.425 | -1.79% |
| LARGE_GROWTH | IWF | technology_and_growth | -0.95% | 2.01% | -3.48% | 17.37% | -7.71% | -0.381 | 0.934 | 1.290 | -1.59% |
| LARGE_VALUE | IWD | diversified_us_equity | 1.71% | -2.06% | 2.92% | 8.81% | -4.06% | -0.301 | 0.806 | 0.702 | -1.46% |
| MID_CAP | IJH | diversified_us_equity | -0.71% | -3.48% | -6.88% | 11.83% | -8.26% | 0.133 | 0.813 | 0.963 | -6.72% |
| SMALL_CAP | IWM | diversified_us_equity | -1.93% | -5.61% | -2.44% | 13.05% | -8.78% | -0.092 | 0.820 | 1.175 | -8.67% |
| SMALL_VALUE | IWN | diversified_us_equity | -1.02% | -5.58% | -1.90% | 10.90% | -7.53% | 0.360 | 0.737 | 0.918 | -6.81% |
| DIVIDEND | SCHD | diversified_us_equity | 1.65% | -3.80% | 0.20% | 11.31% | -6.87% | 0.122 | 0.292 | 0.253 | -4.78% |
| LOW_VOL | SPLV | diversified_us_equity | 2.39% | -3.22% | -11.25% | 9.77% | -9.22% | -0.800 | 0.033 | 0.027 | -6.28% |
| MOMENTUM | MTUM | diversified_us_equity | -2.49% | 0.77% | 3.85% | 26.28% | -11.46% | 0.408 | 0.764 | 1.565 | -8.54% |
| TECHNOLOGY | XLK | technology_and_growth | -2.27% | 2.69% | 17.36% | 25.00% | -9.29% | -0.806 | 0.851 | 1.734 | -2.79% |
| COMMUNICATIONS | XLC | technology_and_growth | -0.14% | -2.77% | -13.35% | 20.72% | -7.06% | 0.312 | 0.548 | 0.678 | -6.35% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | 1.68% | -2.45% | -12.32% | 18.87% | -9.02% | -0.351 | 0.778 | 1.160 | -9.28% |
| CONSUMER_STAPLES | XLP | consumer_defensive | 4.16% | -0.16% | -8.72% | 15.38% | -7.54% | -0.284 | -0.044 | -0.050 | -4.41% |
| HEALTHCARE | XLV | healthcare_and_biotech | 2.76% | 2.35% | 0.56% | 16.51% | -5.87% | -0.560 | 0.227 | 0.275 | -1.73% |
| FINANCIALS | XLF | financials | 2.17% | -5.56% | -0.47% | 12.14% | -8.49% | 0.323 | 0.544 | 0.620 | -5.66% |
| INDUSTRIALS | XLI | industrials_and_defense | -0.56% | -3.66% | -11.64% | 14.84% | -10.23% | -0.248 | 0.703 | 0.939 | -9.07% |
| ENERGY | XLE | energy | 4.03% | -0.11% | 3.19% | 20.74% | -6.15% | -0.162 | -0.177 | -0.300 | 0.00% |
| MATERIALS | XLB | materials_and_mining | -0.12% | -4.58% | -13.69% | 16.13% | -9.14% | -0.013 | 0.532 | 0.731 | -7.46% |
| UTILITIES | XLU | rate_sensitive_defensive | 4.15% | -3.13% | -19.72% | 14.93% | -14.58% | 2.503 | 0.130 | 0.155 | -10.97% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | 3.07% | -4.71% | -9.88% | 13.07% | -11.09% | 0.655 | 0.267 | 0.293 | -8.13% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | 0.57% | -3.80% | -14.73% | 5.07% | -4.58% | 0.651 | 0.310 | 0.115 | -6.59% |
| LONG_TREASURY | TLT | rates_and_duration | 1.22% | -5.55% | -16.66% | 9.93% | -8.05% | 1.856 | 0.268 | 0.193 | -11.75% |
| TIPS | TIP | rates_and_duration | 0.50% | -3.33% | -13.32% | 3.80% | -3.40% | 0.110 | 0.279 | 0.076 | -3.47% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | 0.74% | -3.73% | -14.62% | 5.82% | -4.54% | 0.675 | 0.482 | 0.203 | -5.64% |
| HIGH_YIELD_CREDIT | HYG | credit | 0.40% | -3.73% | -11.24% | 3.35% | -3.25% | 1.825 | 0.763 | 0.230 | -2.76% |
| AGGREGATE_BONDS | AGG | rates_and_duration | 0.56% | -3.43% | -13.59% | 4.31% | -3.62% | 1.081 | 0.407 | 0.124 | -4.43% |
| DEVELOPED_EX_US | VEA | international_equity | -1.66% | -5.59% | -4.56% | 14.63% | -5.09% | -0.410 | 0.803 | 1.092 | -4.97% |
| EMERGING_MARKETS | VWO | international_equity | -1.45% | -2.90% | -6.01% | 14.43% | -4.30% | -0.347 | 0.822 | 1.136 | -2.60% |
| EUROPE | VGK | international_equity | -0.53% | -6.48% | -7.57% | 12.17% | -8.10% | 0.210 | 0.745 | 0.911 | -7.68% |
| JAPAN | EWJ | international_equity | -1.99% | -3.32% | 0.47% | 19.45% | -4.84% | -0.581 | 0.735 | 1.198 | -2.01% |
| CHINA | MCHI | international_equity | -0.25% | -3.59% | -18.73% | 16.45% | -9.99% | -0.731 | 0.576 | 0.878 | -18.98% |
| INDIA | INDA | international_equity | -0.45% | -6.61% | -13.26% | 12.63% | -9.84% | -0.464 | 0.581 | 0.695 | -16.15% |
| GOLD | IAU | precious_metals | 0.67% | -6.18% | -20.09% | 23.93% | -12.19% | -0.614 | 0.333 | 0.750 | -22.87% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | 3.17% | -1.71% | 2.91% | 20.61% | -6.42% | -0.220 | -0.191 | -0.305 | -1.19% |
| SEMICONDUCTORS | SMH | technology_and_growth | -6.77% | 1.89% | 16.56% | 37.28% | -16.01% | -0.785 | 0.770 | 2.361 | -11.65% |
| SOFTWARE | IGV | technology_and_growth | 1.42% | 7.55% | 17.34% | 32.64% | -8.27% | -1.245 | 0.492 | 1.211 | -4.94% |
| BROAD_AI_TECH | AIQ | technology_and_growth | -1.39% | 0.97% | 14.81% | 25.45% | -9.65% | -0.680 | 0.851 | 1.922 | -6.02% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | -3.37% | -1.86% | -11.82% | 28.85% | -10.40% | -0.803 | 0.813 | 2.178 | -15.45% |
| CYBERSECURITY | CIBR | technology_and_growth | 1.69% | 12.14% | 37.84% | 32.70% | -9.53% | 0.524 | 0.497 | 1.120 | -2.00% |
| SOLAR | TAN | clean_energy | -0.44% | -9.84% | -25.80% | 33.42% | -22.94% | -0.681 | 0.654 | 1.934 | -41.19% |
| METALS_MINING | XME | materials_and_mining | -2.70% | -9.72% | -12.76% | 36.16% | -15.75% | -0.892 | 0.600 | 1.778 | -20.96% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | 0.98% | -2.47% | -3.20% | 9.91% | -6.27% | -0.423 | 0.777 | 0.699 | -3.94% |
| BIOTECH | XBI | healthcare_and_biotech | -3.07% | -5.13% | 6.72% | 29.14% | -11.95% | 0.401 | 0.472 | 1.036 | -10.70% |
| REGIONAL_BANKS | KRE | financials | -1.18% | -7.39% | -4.56% | 15.74% | -11.09% | 0.588 | 0.419 | 0.713 | -10.23% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | -0.46% | -7.88% | -17.54% | 20.07% | -19.50% | 0.226 | 0.566 | 1.012 | -18.54% |
| CANADA | EWC | international_equity | 1.14% | -3.92% | -5.39% | 12.78% | -7.50% | -0.061 | 0.673 | 0.761 | -5.09% |
| UNITED_KINGDOM | EWU | international_equity | 1.10% | -4.65% | -10.07% | 11.14% | -7.09% | -0.309 | 0.603 | 0.695 | -5.45% |
| AUSTRALIA | EWA | international_equity | 0.84% | -4.11% | -13.22% | 16.22% | -8.02% | 0.223 | 0.681 | 0.950 | -5.78% |
| SOUTH_KOREA | EWY | international_equity | -11.15% | -11.92% | 21.95% | 55.87% | -18.52% | -0.879 | 0.637 | 2.814 | -22.40% |
| TAIWAN | EWT | international_equity | -3.16% | 0.97% | 30.04% | 31.83% | -12.76% | -0.617 | 0.758 | 1.870 | -3.16% |
| BRAZIL | EWZ | international_equity | 1.30% | 11.95% | -18.82% | 33.40% | -8.05% | 1.648 | 0.460 | 1.004 | 0.00% |
| MEXICO | EWW | international_equity | 1.91% | -4.90% | -15.23% | 17.12% | -10.38% | -0.189 | 0.564 | 0.961 | -8.52% |
| SOUTH_AFRICA | EZA | international_equity | 0.95% | -11.09% | -12.83% | 27.25% | -14.09% | -0.273 | 0.628 | 1.607 | -20.20% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | 0.83% | -3.76% | -13.95% | 5.54% | -4.64% | 4.996 | 0.400 | 0.146 | -4.97% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | 0.04% | -4.01% | -13.95% | 4.56% | -5.72% | 5.001 | 0.361 | 0.095 | -5.44% |
| EMERGING_MARKET_BONDS | EMB | credit | 0.82% | -4.48% | -12.38% | 5.89% | -5.08% | 0.997 | 0.688 | 0.316 | -4.71% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | 0.38% | -2.10% | -12.68% | 3.64% | -2.25% | 0.290 | 0.477 | 0.137 | -2.95% |
| SILVER | SLV | precious_metals | -1.41% | -8.55% | -26.56% | 37.59% | -14.85% | -0.665 | 0.372 | 1.797 | -48.53% |
| COPPER | CPER | non_energy_commodities | 1.93% | 1.64% | -5.18% | 22.90% | -6.80% | -0.503 | 0.577 | 1.276 | -1.93% |
| AGRICULTURE | DBA | non_energy_commodities | -0.07% | -3.75% | -4.25% | 13.15% | -4.61% | -0.356 | 0.064 | 0.056 | -3.56% |
| OIL | USO | energy | 4.89% | -4.56% | 8.89% | 49.12% | -17.64% | -0.481 | -0.352 | -1.344 | -6.69% |
| US_DOLLAR | UUP | currencies | 0.48% | 1.72% | -9.16% | 5.27% | -2.52% | -0.166 | -0.296 | -0.125 | 0.00% |
| EURO | FXE | currencies | -0.58% | -5.82% | -12.75% | 4.76% | -4.39% | -0.259 | 0.278 | 0.116 | -6.80% |
| YEN | FXY | currencies | -0.41% | -5.24% | -8.05% | 9.89% | -3.38% | -0.269 | 0.184 | 0.116 | -5.51% |
| BITCOIN_ETF | IBIT | crypto_assets | -3.50% | 5.00% | -6.44% | 36.92% | -7.14% | -0.087 | 0.499 | 1.743 | -29.21% |
| ETHEREUM_ETF | ETHA | crypto_assets | 178.76% | 195.17% | 0.50% | 397.80% | -8.52% | -0.419 | 0.195 | 3.116 | -6.47% |
