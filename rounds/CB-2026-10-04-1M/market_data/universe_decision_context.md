# Full-Universe Horizon-Specific Decision Context

Profile: monthly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: tiingo_eod_history_through_2026-09-25; repository_daily_price_snapshots_2026-09-28_to_2026-10-02_(tiingo_eod_or_yahoo_chart_adjclose); yahoo_chart_reported_volume_2026-09-28_to_2026-10-02
- As-of date requested: 2026-10-02
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | -0.22% |
| spy_return_21s | 0.83% |
| rsp_return_5s | -0.65% |
| rsp_return_21s | -3.70% |
| hyg_return_5s | -1.22% |
| hyg_return_21s | -2.78% |
| tlt_return_5s | -2.32% |
| tlt_return_21s | -5.45% |
| uup_return_5s | 0.94% |
| uup_return_21s | 2.56% |
| uso_return_5s | -0.65% |
| uso_return_21s | 4.41% |
| iau_return_5s | -3.36% |
| iau_return_21s | -5.57% |
| rsp_minus_spy_5s | -0.43% |
| rsp_minus_spy_21s | -4.53% |
| positive_asset_share_5s | 26.09% |
| positive_asset_share_21s | 31.88% |
| active_return_dispersion_5s |  |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_5s | active_return_21s | prior_105s_active_return | volatility_63s | max_drawdown_63s | volume_zscore_20v120 | corr_spy_252s | beta_spy_252s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | -0.83% | -16.97% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | -0.21% | -0.80% | -15.49% | 0.56% | -0.26% | 0.328 | -0.051 | -0.001 | -0.24% |
| SP500 | SPY | diversified_us_equity | -0.22% | 0.00% | 0.00% | 11.02% | -3.38% | -0.434 | 1.000 | 1.000 | -0.81% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | -0.47% | -0.54% | -0.23% | 11.21% | -3.39% | -0.379 | 0.995 | 1.012 | -1.64% |
| NASDAQ100 | QQQ | technology_and_growth | 0.68% | 4.96% | 4.41% | 19.03% | -8.79% | -0.660 | 0.929 | 1.426 | 0.00% |
| LARGE_GROWTH | IWF | technology_and_growth | 0.65% | 3.58% | -3.57% | 17.97% | -7.99% | -0.560 | 0.934 | 1.288 | -1.15% |
| LARGE_VALUE | IWD | diversified_us_equity | -1.01% | -3.47% | 2.69% | 8.92% | -4.06% | -0.328 | 0.807 | 0.703 | -3.50% |
| MID_CAP | IJH | diversified_us_equity | 0.55% | -2.82% | -6.53% | 11.98% | -8.26% | -0.121 | 0.816 | 0.968 | -6.42% |
| SMALL_CAP | IWM | diversified_us_equity | -0.16% | -4.83% | 0.31% | 13.24% | -8.68% | -0.266 | 0.823 | 1.182 | -7.48% |
| SMALL_VALUE | IWN | diversified_us_equity | -0.54% | -5.25% | -0.50% | 11.03% | -7.53% | -0.238 | 0.742 | 0.927 | -6.26% |
| DIVIDEND | SCHD | diversified_us_equity | -1.48% | -6.63% | -1.49% | 11.26% | -6.87% | 0.310 | 0.299 | 0.258 | -6.33% |
| LOW_VOL | SPLV | diversified_us_equity | -0.58% | -5.70% | -15.01% | 9.86% | -9.22% | -0.704 | 0.030 | 0.024 | -8.73% |
| MOMENTUM | MTUM | diversified_us_equity | 1.38% | 8.08% | 3.98% | 27.37% | -12.01% | 0.383 | 0.764 | 1.561 | -6.28% |
| TECHNOLOGY | XLK | technology_and_growth | 1.80% | 8.12% | 18.20% | 26.07% | -10.34% | -0.860 | 0.852 | 1.738 | 0.00% |
| COMMUNICATIONS | XLC | technology_and_growth | -2.34% | -2.39% | -16.06% | 20.65% | -7.06% | 0.011 | 0.556 | 0.684 | -7.30% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | -0.47% | -4.82% | -10.55% | 19.18% | -9.02% | -0.425 | 0.777 | 1.164 | -11.08% |
| CONSUMER_STAPLES | XLP | consumer_defensive | -1.86% | -6.06% | -11.79% | 15.29% | -7.54% | -0.257 | -0.049 | -0.054 | -8.80% |
| HEALTHCARE | XLV | healthcare_and_biotech | -2.65% | -4.38% | 1.35% | 17.12% | -5.87% | -0.601 | 0.223 | 0.270 | -5.05% |
| FINANCIALS | XLF | financials | -2.46% | -7.74% | -0.15% | 12.52% | -8.49% | 0.150 | 0.543 | 0.617 | -8.34% |
| INDUSTRIALS | XLI | industrials_and_defense | -0.28% | -2.21% | -11.21% | 14.67% | -10.23% | -0.315 | 0.708 | 0.943 | -8.63% |
| ENERGY | XLE | energy | 1.26% | -3.75% | -6.31% | 21.60% | -6.15% | -0.191 | -0.175 | -0.295 | -4.14% |
| MATERIALS | XLB | materials_and_mining | -1.89% | -8.13% | -11.54% | 16.70% | -9.14% | -0.062 | 0.532 | 0.731 | -8.54% |
| UTILITIES | XLU | rate_sensitive_defensive | 0.81% | -6.80% | -24.30% | 13.69% | -14.58% | 1.428 | 0.124 | 0.145 | -14.81% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | -1.80% | -6.73% | -10.96% | 12.69% | -10.85% | 0.057 | 0.262 | 0.285 | -10.56% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | -1.06% | -4.23% | -18.54% | 5.15% | -4.78% | 0.392 | 0.312 | 0.116 | -6.99% |
| LONG_TREASURY | TLT | rates_and_duration | -2.32% | -6.29% | -20.72% | 9.88% | -8.61% | 1.533 | 0.270 | 0.194 | -12.40% |
| TIPS | TIP | rates_and_duration | -0.41% | -3.41% | -17.23% | 3.77% | -3.43% | 0.026 | 0.282 | 0.076 | -3.83% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | -1.34% | -4.18% | -18.50% | 5.93% | -5.49% | 0.413 | 0.482 | 0.203 | -6.33% |
| HIGH_YIELD_CREDIT | HYG | credit | -1.22% | -3.62% | -14.99% | 3.30% | -3.25% | 1.280 | 0.760 | 0.229 | -3.24% |
| AGGREGATE_BONDS | AGG | rates_and_duration | -0.91% | -3.51% | -17.71% | 4.39% | -3.80% | 0.708 | 0.410 | 0.124 | -4.84% |
| DEVELOPED_EX_US | VEA | international_equity | -0.99% | -2.60% | -4.08% | 15.32% | -4.62% | -0.455 | 0.804 | 1.094 | -3.37% |
| EMERGING_MARKETS | VWO | international_equity | -1.00% | -2.64% | -3.92% | 14.58% | -5.24% | -0.398 | 0.824 | 1.130 | -2.88% |
| EUROPE | VGK | international_equity | -2.54% | -5.63% | -6.18% | 12.30% | -8.03% | -0.237 | 0.746 | 0.914 | -7.07% |
| JAPAN | EWJ | international_equity | 1.01% | 2.16% | -3.76% | 20.52% | -6.21% | -0.591 | 0.730 | 1.200 | 0.00% |
| CHINA | MCHI | international_equity | -2.62% | -6.89% | -18.65% | 16.00% | -9.99% | -0.848 | 0.575 | 0.870 | -22.06% |
| INDIA | INDA | international_equity | -2.80% | -7.74% | -9.85% | 12.61% | -8.25% | -0.504 | 0.576 | 0.685 | -15.86% |
| GOLD | IAU | precious_metals | -3.36% | -6.41% | -23.10% | 24.36% | -11.69% | -0.372 | 0.334 | 0.755 | -23.25% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | -0.31% | 1.16% | -8.18% | 21.46% | -6.42% | -0.254 | -0.187 | -0.298 | -3.28% |
| SEMICONDUCTORS | SMH | technology_and_growth | 3.96% | 13.72% | 23.35% | 39.05% | -17.48% | -0.775 | 0.774 | 2.377 | -5.73% |
| SOFTWARE | IGV | technology_and_growth | 2.28% | 4.01% | 11.78% | 32.48% | -8.27% | -1.163 | 0.490 | 1.202 | -7.37% |
| BROAD_AI_TECH | AIQ | technology_and_growth | 0.39% | 4.16% | 16.48% | 26.88% | -12.31% | -0.706 | 0.851 | 1.927 | -5.57% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | 0.05% | 2.69% | -12.32% | 29.97% | -15.79% | -0.845 | 0.808 | 2.186 | -13.45% |
| CYBERSECURITY | CIBR | technology_and_growth | 3.71% | 11.10% | 28.88% | 32.77% | -9.53% | 0.183 | 0.496 | 1.112 | 0.00% |
| SOLAR | TAN | clean_energy | -0.02% | -7.65% | -30.79% | 35.81% | -25.27% | -0.701 | 0.650 | 1.932 | -40.42% |
| METALS_MINING | XME | materials_and_mining | -2.39% | -12.26% | -9.06% | 36.32% | -15.75% | -0.807 | 0.598 | 1.772 | -20.29% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | -0.65% | -4.53% | -3.32% | 9.88% | -6.27% | -0.667 | 0.779 | 0.699 | -5.50% |
| BIOTECH | XBI | healthcare_and_biotech | -0.39% | -7.45% | 11.39% | 28.81% | -10.51% | -0.049 | 0.478 | 1.036 | -8.92% |
| REGIONAL_BANKS | KRE | financials | -1.08% | -4.95% | -3.83% | 16.21% | -10.38% | 0.293 | 0.426 | 0.725 | -8.65% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | -2.82% | -7.70% | -16.24% | 20.43% | -18.08% | 0.162 | 0.569 | 1.019 | -17.84% |
| CANADA | EWC | international_equity | -1.46% | -5.00% | -5.69% | 11.91% | -6.96% | 0.006 | 0.678 | 0.762 | -6.26% |
| UNITED_KINGDOM | EWU | international_equity | -2.41% | -5.07% | -11.16% | 11.19% | -7.09% | -0.375 | 0.604 | 0.700 | -6.50% |
| AUSTRALIA | EWA | international_equity | -0.39% | -6.53% | -8.59% | 16.17% | -8.02% | 0.269 | 0.680 | 0.949 | -6.93% |
| SOUTH_KOREA | EWY | international_equity | 2.51% | 6.44% | 28.60% | 58.71% | -24.04% | -0.783 | 0.642 | 2.826 | -12.46% |
| TAIWAN | EWT | international_equity | 1.35% | 5.47% | 37.66% | 34.21% | -16.65% | -0.778 | 0.759 | 1.869 | 0.00% |
| BRAZIL | EWZ | international_equity | 3.72% | -0.57% | -16.70% | 23.14% | -8.05% | 0.188 | 0.489 | 0.962 | -7.61% |
| MEXICO | EWW | international_equity | -3.07% | -7.57% | -15.36% | 17.12% | -10.38% | -0.479 | 0.560 | 0.956 | -11.20% |
| SOUTH_AFRICA | EZA | international_equity | -4.95% | -10.55% | -11.88% | 27.35% | -13.31% | -0.286 | 0.629 | 1.620 | -20.92% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | -1.24% | -4.39% | -17.68% | 5.57% | -4.67% | 4.460 | 0.405 | 0.147 | -5.61% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | -0.21% | -3.96% | -17.77% | 4.39% | -6.26% | 7.786 | 0.363 | 0.094 | -5.63% |
| EMERGING_MARKET_BONDS | EMB | credit | -2.21% | -5.09% | -14.61% | 5.81% | -5.62% | 0.681 | 0.688 | 0.314 | -5.69% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | -0.17% | -1.66% | -17.26% | 3.92% | -2.48% | 0.150 | 0.480 | 0.138 | -3.18% |
| SILVER | SLV | precious_metals | -5.85% | -8.17% | -27.18% | 38.76% | -13.16% | -0.590 | 0.371 | 1.796 | -48.16% |
| COPPER | CPER | non_energy_commodities | -2.68% | -0.86% | -1.95% | 23.02% | -6.80% | -0.146 | 0.569 | 1.262 | -4.61% |
| AGRICULTURE | DBA | non_energy_commodities | -1.16% | -4.46% | -9.20% | 12.48% | -4.61% | -0.303 | 0.057 | 0.049 | -4.34% |
| OIL | USO | energy | -0.65% | 3.57% | -14.63% | 52.40% | -17.64% | -0.454 | -0.348 | -1.329 | -8.95% |
| US_DOLLAR | UUP | currencies | 0.94% | 1.72% | -15.86% | 5.19% | -2.52% | -0.345 | -0.297 | -0.127 | -0.24% |
| EURO | FXE | currencies | -1.26% | -3.72% | -16.13% | 4.62% | -3.77% | -0.400 | 0.280 | 0.117 | -6.05% |
| YEN | FXY | currencies | -0.39% | -0.25% | -16.64% | 9.97% | -3.38% | 0.078 | 0.178 | 0.117 | -7.04% |
| BITCOIN_ETF | IBIT | crypto_assets | 0.34% | 8.16% | -1.64% | 37.77% | -7.14% | -0.008 | 0.498 | 1.750 | -33.05% |
| ETHEREUM_ETF | ETHA | crypto_assets | -0.98% | 10.58% | -1.48% | 46.80% | -5.32% | 0.536 | 0.518 | 2.562 | -43.81% |
