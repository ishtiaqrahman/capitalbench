# Full-Universe Horizon-Specific Decision Context

Profile: monthly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: tiingo_eod_adjusted_price_and_volume; yahoo_chart_adjusted_close_and_reported_volume
- As-of date requested: 2026-10-27
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | 0.08% |
| spy_return_21s | 0.53% |
| rsp_return_5s | 0.77% |
| rsp_return_21s | 3.71% |
| hyg_return_5s | 1.00% |
| hyg_return_21s | 0.52% |
| tlt_return_5s | 1.87% |
| tlt_return_21s | 4.24% |
| uup_return_5s | 0.76% |
| uup_return_21s | 1.46% |
| uso_return_5s | 2.04% |
| uso_return_21s | 9.25% |
| iau_return_5s | -1.43% |
| iau_return_21s | -1.51% |
| rsp_minus_spy_5s | 0.69% |
| rsp_minus_spy_21s | 3.18% |
| positive_asset_share_5s | 69.57% |
| positive_asset_share_21s | 55.07% |
| active_return_dispersion_5s |  |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_5s | active_return_21s | prior_105s_active_return | volatility_63s | max_drawdown_63s | volume_zscore_20v120 | corr_spy_252s | beta_spy_252s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | -0.53% | -8.12% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.09% | -0.21% | -6.62% | 0.20% | -0.01% | 0.412 | -0.048 | -0.001 | 0.00% |
| SP500 | SPY | diversified_us_equity | 0.08% | 0.00% | 0.00% | 10.73% | -3.06% | -0.722 | 1.000 | 1.000 | -1.21% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | 0.22% | 0.02% | -0.35% | 10.96% | -3.39% | -0.322 | 0.995 | 1.011 | -1.41% |
| NASDAQ100 | QQQ | technology_and_growth | 0.50% | -2.60% | 4.13% | 18.64% | -7.27% | -0.282 | 0.924 | 1.454 | -5.06% |
| LARGE_GROWTH | IWF | technology_and_growth | -0.13% | -2.89% | -2.79% | 17.79% | -7.42% | 0.184 | 0.930 | 1.320 | -5.37% |
| LARGE_VALUE | IWD | diversified_us_equity | 0.31% | 2.85% | 2.75% | 8.18% | -4.06% | 0.131 | 0.784 | 0.677 | -0.21% |
| MID_CAP | IJH | diversified_us_equity | 0.18% | 0.55% | -7.10% | 12.02% | -8.26% | 0.289 | 0.806 | 0.949 | -6.64% |
| SMALL_CAP | IWM | diversified_us_equity | 1.60% | -0.47% | -5.38% | 13.99% | -11.12% | 0.159 | 0.812 | 1.154 | -7.92% |
| SMALL_VALUE | IWN | diversified_us_equity | 1.72% | 0.83% | -4.94% | 11.26% | -8.30% | 0.978 | 0.713 | 0.870 | -5.23% |
| DIVIDEND | SCHD | diversified_us_equity | 1.24% | 5.86% | -1.00% | 11.30% | -6.87% | 0.266 | 0.220 | 0.197 | -0.79% |
| LOW_VOL | SPLV | diversified_us_equity | 1.14% | 5.69% | -11.23% | 10.32% | -8.72% | -0.237 | 0.006 | 0.005 | -2.74% |
| MOMENTUM | MTUM | diversified_us_equity | 1.25% | -5.62% | 6.49% | 24.65% | -11.06% | -0.312 | 0.770 | 1.642 | -13.06% |
| TECHNOLOGY | XLK | technology_and_growth | 2.18% | -3.12% | 15.41% | 25.62% | -9.73% | -0.281 | 0.849 | 1.781 | -6.19% |
| COMMUNICATIONS | XLC | technology_and_growth | -6.00% | -7.36% | -11.51% | 19.80% | -9.73% | 0.465 | 0.531 | 0.682 | -12.96% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | -0.04% | 5.39% | -14.57% | 16.86% | -9.02% | -0.088 | 0.769 | 1.167 | -6.71% |
| CONSUMER_STAPLES | XLP | consumer_defensive | -0.68% | 5.39% | -7.73% | 15.97% | -7.54% | 0.925 | -0.079 | -0.095 | -3.16% |
| HEALTHCARE | XLV | healthcare_and_biotech | -0.36% | 4.10% | 11.92% | 17.22% | -5.87% | -0.234 | 0.187 | 0.240 | -1.17% |
| FINANCIALS | XLF | financials | 0.29% | 2.59% | -2.87% | 12.23% | -8.49% | 0.021 | 0.505 | 0.575 | -4.24% |
| INDUSTRIALS | XLI | industrials_and_defense | 0.67% | -1.04% | -8.90% | 13.87% | -11.50% | -0.020 | 0.700 | 0.946 | -9.73% |
| ENERGY | XLE | energy | 0.35% | 9.31% | 0.91% | 21.64% | -6.15% | -0.221 | -0.239 | -0.416 | -2.05% |
| MATERIALS | XLB | materials_and_mining | 1.07% | 4.14% | -11.07% | 15.12% | -9.14% | 0.015 | 0.505 | 0.703 | -3.08% |
| UTILITIES | XLU | rate_sensitive_defensive | 2.32% | 8.64% | -22.08% | 15.34% | -11.96% | 2.286 | 0.093 | 0.115 | -8.36% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | 0.14% | 2.11% | -12.34% | 12.92% | -10.99% | 2.013 | 0.233 | 0.264 | -6.99% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | 0.94% | 1.57% | -12.51% | 5.64% | -4.24% | 1.039 | 0.321 | 0.125 | -4.52% |
| LONG_TREASURY | TLT | rates_and_duration | 1.87% | 3.72% | -15.33% | 10.72% | -6.89% | 1.148 | 0.293 | 0.220 | -7.34% |
| TIPS | TIP | rates_and_duration | 0.79% | 1.60% | -11.77% | 4.20% | -3.40% | -0.056 | 0.272 | 0.077 | -1.80% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | 1.05% | 1.69% | -12.54% | 6.36% | -3.98% | 0.659 | 0.472 | 0.210 | -3.65% |
| HIGH_YIELD_CREDIT | HYG | credit | 1.00% | -0.01% | -9.21% | 3.62% | -2.93% | 1.171 | 0.746 | 0.226 | -1.94% |
| AGGREGATE_BONDS | AGG | rates_and_duration | 0.86% | 1.35% | -11.27% | 4.74% | -3.28% | 1.230 | 0.409 | 0.131 | -2.64% |
| DEVELOPED_EX_US | VEA | international_equity | 0.14% | -2.53% | -2.02% | 14.19% | -6.19% | -0.234 | 0.808 | 1.118 | -5.06% |
| EMERGING_MARKETS | VWO | international_equity | -2.44% | -5.32% | -5.46% | 14.07% | -7.87% | -0.017 | 0.816 | 1.121 | -7.33% |
| EUROPE | VGK | international_equity | -0.16% | -2.05% | -3.89% | 12.06% | -8.10% | 0.276 | 0.749 | 0.941 | -6.36% |
| JAPAN | EWJ | international_equity | -0.19% | -2.16% | 3.06% | 18.15% | -5.26% | -0.525 | 0.729 | 1.188 | -4.10% |
| CHINA | MCHI | international_equity | -3.69% | -7.11% | -14.94% | 15.32% | -13.93% | -0.417 | 0.541 | 0.795 | -23.75% |
| INDIA | INDA | international_equity | -2.18% | -1.27% | -12.46% | 13.39% | -9.84% | 0.112 | 0.597 | 0.737 | -14.75% |
| GOLD | IAU | precious_metals | -1.43% | -2.04% | -18.48% | 23.86% | -14.37% | -0.563 | 0.363 | 0.809 | -24.85% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | 0.25% | 3.08% | -0.92% | 17.80% | -5.02% | -0.286 | -0.243 | -0.392 | -1.33% |
| SEMICONDUCTORS | SMH | technology_and_growth | 2.13% | -7.53% | 14.03% | 36.84% | -17.44% | -0.210 | 0.768 | 2.420 | -16.58% |
| SOFTWARE | IGV | technology_and_growth | 4.54% | 5.49% | 15.94% | 33.51% | -8.27% | -1.070 | 0.486 | 1.237 | -4.51% |
| BROAD_AI_TECH | AIQ | technology_and_growth | 0.76% | -2.15% | 10.62% | 24.88% | -7.50% | -0.439 | 0.850 | 1.954 | -9.24% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | 2.56% | -4.81% | -12.10% | 29.16% | -14.39% | -0.464 | 0.813 | 2.212 | -18.89% |
| CYBERSECURITY | CIBR | technology_and_growth | 9.21% | 7.32% | 43.42% | 35.07% | -10.16% | 1.318 | 0.487 | 1.145 | -0.32% |
| SOLAR | TAN | clean_energy | 0.65% | -2.81% | -33.49% | 33.00% | -23.63% | -0.240 | 0.649 | 1.934 | -43.16% |
| METALS_MINING | XME | materials_and_mining | 0.15% | -5.20% | -17.95% | 36.40% | -21.89% | -0.639 | 0.616 | 1.809 | -24.24% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | 0.77% | 3.18% | -2.85% | 9.88% | -6.27% | 0.130 | 0.749 | 0.677 | -1.99% |
| BIOTECH | XBI | healthcare_and_biotech | 1.04% | -1.66% | 11.40% | 31.25% | -14.88% | 0.465 | 0.475 | 1.087 | -8.68% |
| REGIONAL_BANKS | KRE | financials | 2.78% | 2.35% | -6.70% | 15.53% | -11.55% | 0.517 | 0.371 | 0.594 | -6.33% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | 0.03% | -1.98% | -11.15% | 17.98% | -20.04% | 0.348 | 0.546 | 0.986 | -18.46% |
| CANADA | EWC | international_equity | 0.30% | 2.82% | -4.84% | 13.10% | -7.50% | -0.085 | 0.666 | 0.766 | -2.54% |
| UNITED_KINGDOM | EWU | international_equity | -1.19% | -0.70% | -5.11% | 11.12% | -7.09% | -0.437 | 0.587 | 0.699 | -4.45% |
| AUSTRALIA | EWA | international_equity | 1.13% | 2.91% | -8.70% | 15.96% | -8.02% | 0.246 | 0.680 | 0.967 | -3.12% |
| SOUTH_KOREA | EWY | international_equity | 2.25% | -14.76% | 10.80% | 52.91% | -22.61% | -0.373 | 0.647 | 2.949 | -28.17% |
| TAIWAN | EWT | international_equity | -0.07% | -6.59% | 22.75% | 28.74% | -11.87% | -0.322 | 0.750 | 1.880 | -9.11% |
| BRAZIL | EWZ | international_equity | -20.12% | -5.80% | -16.02% | 52.50% | -21.57% | 5.197 | 0.326 | 0.891 | -21.22% |
| MEXICO | EWW | international_equity | -0.66% | 3.11% | -11.85% | 16.43% | -10.38% | -0.098 | 0.568 | 0.979 | -6.31% |
| SOUTH_AFRICA | EZA | international_equity | -2.17% | -1.23% | -11.90% | 26.86% | -14.09% | -0.268 | 0.636 | 1.631 | -19.82% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | 1.17% | 2.00% | -12.11% | 5.95% | -4.25% | 0.572 | 0.401 | 0.154 | -2.76% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | 1.49% | 3.00% | -13.08% | 5.26% | -5.28% | 2.598 | 0.350 | 0.101 | -2.64% |
| EMERGING_MARKET_BONDS | EMB | credit | 0.77% | 0.60% | -10.86% | 5.91% | -4.61% | 0.927 | 0.669 | 0.314 | -3.35% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | 0.38% | 0.68% | -9.35% | 3.59% | -2.15% | 0.381 | 0.515 | 0.151 | -2.05% |
| SILVER | SLV | precious_metals | -5.68% | -11.07% | -25.11% | 39.32% | -22.48% | -0.404 | 0.402 | 1.979 | -53.45% |
| COPPER | CPER | non_energy_commodities | 0.75% | 0.40% | 1.37% | 22.55% | -7.14% | -0.500 | 0.563 | 1.243 | -3.33% |
| AGRICULTURE | DBA | non_energy_commodities | -2.73% | -3.54% | -7.08% | 11.59% | -7.09% | -0.492 | 0.066 | 0.058 | -7.09% |
| OIL | USO | energy | 2.04% | 8.72% | -0.66% | 41.52% | -11.44% | -0.589 | -0.400 | -1.557 | -3.33% |
| US_DOLLAR | UUP | currencies | 0.76% | 0.93% | -3.87% | 5.25% | -1.90% | -0.279 | -0.335 | -0.144 | -0.03% |
| EURO | FXE | currencies | -0.83% | -2.42% | -10.69% | 4.77% | -4.45% | -0.229 | 0.324 | 0.137 | -6.86% |
| YEN | FXY | currencies | 0.33% | -0.74% | -6.87% | 10.03% | -3.38% | -0.521 | 0.214 | 0.137 | -3.89% |
| BITCOIN_ETF | IBIT | crypto_assets | -2.16% | -3.73% | 0.99% | 37.62% | -7.73% | -0.452 | 0.499 | 1.763 | -29.99% |
| ETHEREUM_ETF | ETHA | crypto_assets | -3.70% | -12.80% | 7.89% | 46.92% | -16.32% | -0.199 | 0.499 | 2.467 | -44.33% |
