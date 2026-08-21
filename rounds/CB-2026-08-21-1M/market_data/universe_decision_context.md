# Full-Universe Horizon-Specific Decision Context

Profile: monthly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: yahoo_chart_adjusted_close_and_reported_volume
- As-of date requested: 2026-08-20
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | -1.96% |
| spy_return_21s | 2.03% |
| rsp_return_5s | -1.10% |
| rsp_return_21s | 3.56% |
| hyg_return_5s | -0.29% |
| hyg_return_21s | 0.54% |
| tlt_return_5s | -0.30% |
| tlt_return_21s | -0.92% |
| uup_return_5s | -0.96% |
| uup_return_21s | -1.90% |
| uso_return_5s | 7.61% |
| uso_return_21s | 2.17% |
| iau_return_5s | 4.10% |
| iau_return_21s | 9.58% |
| rsp_minus_spy_5s | 0.86% |
| rsp_minus_spy_21s | 1.53% |
| positive_asset_share_5s | 31.88% |
| positive_asset_share_21s | 79.71% |
| active_return_dispersion_5s |  |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_5s | active_return_21s | prior_105s_active_return | volatility_63s | max_drawdown_63s | volume_zscore_20v120 | corr_spy_252s | beta_spy_252s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | -2.03% | -9.77% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.07% | -1.74% | -8.27% | 0.21% | -0.01% | -0.371 | -0.100 | -0.002 | 0.00% |
| SP500 | SPY | diversified_us_equity | -1.96% | 0.00% | 0.00% | 13.71% | -4.49% | -0.818 | 1.000 | 1.000 | -1.96% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | -2.01% | 0.06% | -0.05% | 13.64% | -4.36% | -0.678 | 0.995 | 1.012 | -2.01% |
| NASDAQ100 | QQQ | technology_and_growth | -2.89% | -1.24% | 7.38% | 25.69% | -11.22% | -0.702 | 0.930 | 1.415 | -4.62% |
| LARGE_GROWTH | IWF | technology_and_growth | -3.06% | -1.29% | -2.28% | 20.92% | -11.35% | -0.908 | 0.936 | 1.281 | -5.31% |
| LARGE_VALUE | IWD | diversified_us_equity | -0.98% | 1.46% | 1.51% | 11.25% | -2.40% | -0.683 | 0.805 | 0.705 | -1.00% |
| MID_CAP | IJH | diversified_us_equity | -2.61% | -1.13% | -3.64% | 13.80% | -3.09% | -0.825 | 0.810 | 0.983 | -2.92% |
| SMALL_CAP | IWM | diversified_us_equity | -1.92% | -0.71% | 1.72% | 16.97% | -3.95% | -1.102 | 0.820 | 1.215 | -2.43% |
| SMALL_VALUE | IWN | diversified_us_equity | -1.31% | -1.24% | 1.81% | 13.59% | -2.75% | -0.579 | 0.735 | 0.963 | -1.59% |
| DIVIDEND | SCHD | diversified_us_equity | 1.16% | 3.83% | -3.84% | 12.28% | -2.95% | 0.341 | 0.290 | 0.250 | -0.74% |
| LOW_VOL | SPLV | diversified_us_equity | -0.75% | -2.74% | -7.99% | 12.85% | -3.75% | -0.574 | 0.026 | 0.022 | -2.96% |
| MOMENTUM | MTUM | diversified_us_equity | -3.46% | -4.94% | 14.53% | 38.63% | -17.99% | 0.504 | 0.768 | 1.559 | -11.62% |
| TECHNOLOGY | XLK | technology_and_growth | -4.02% | -0.46% | 19.11% | 35.09% | -15.86% | -0.972 | 0.855 | 1.726 | -7.51% |
| COMMUNICATIONS | XLC | technology_and_growth | -1.66% | -0.68% | -14.38% | 19.52% | -9.44% | -0.676 | 0.579 | 0.678 | -7.29% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | -1.49% | 0.30% | -11.29% | 21.80% | -10.72% | -0.869 | 0.777 | 1.179 | -5.92% |
| CONSUMER_STAPLES | XLP | consumer_defensive | -0.79% | -0.92% | -12.31% | 17.49% | -4.31% | -0.686 | -0.056 | -0.062 | -4.02% |
| HEALTHCARE | XLV | healthcare_and_biotech | 2.38% | 6.10% | -7.53% | 19.78% | -3.74% | -0.542 | 0.226 | 0.281 | -1.87% |
| FINANCIALS | XLF | financials | -2.25% | -0.43% | -1.36% | 13.07% | -2.25% | -0.830 | 0.545 | 0.617 | -2.25% |
| INDUSTRIALS | XLI | industrials_and_defense | -3.24% | -1.52% | -7.82% | 18.50% | -4.80% | -0.991 | 0.720 | 0.958 | -3.61% |
| ENERGY | XLE | energy | 4.41% | 5.65% | -1.01% | 23.41% | -11.05% | -0.914 | -0.164 | -0.276 | 0.00% |
| MATERIALS | XLB | materials_and_mining | 0.21% | 1.12% | -12.79% | 19.08% | -4.75% | -0.477 | 0.537 | 0.740 | -1.54% |
| UTILITIES | XLU | rate_sensitive_defensive | -0.61% | -6.74% | -8.83% | 15.50% | -6.83% | -0.420 | 0.130 | 0.151 | -7.07% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | -0.09% | -1.88% | -3.96% | 15.82% | -4.19% | -0.398 | 0.253 | 0.277 | -2.02% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | -0.32% | -1.80% | -12.32% | 4.72% | -2.00% | -0.126 | 0.300 | 0.108 | -3.22% |
| LONG_TREASURY | TLT | rates_and_duration | -0.30% | -2.95% | -14.92% | 9.51% | -6.26% | 0.368 | 0.249 | 0.182 | -7.26% |
| TIPS | TIP | rates_and_duration | 0.34% | -1.53% | -10.32% | 3.45% | -1.40% | -0.263 | 0.281 | 0.073 | -0.68% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | -0.46% | -2.17% | -12.45% | 5.25% | -2.89% | -0.352 | 0.487 | 0.202 | -2.85% |
| HIGH_YIELD_CREDIT | HYG | credit | -0.29% | -1.50% | -9.07% | 3.06% | -0.80% | -0.658 | 0.783 | 0.235 | -0.29% |
| AGGREGATE_BONDS | AGG | rates_and_duration | -0.20% | -1.78% | -11.43% | 3.89% | -1.71% | -0.159 | 0.408 | 0.120 | -1.91% |
| DEVELOPED_EX_US | VEA | international_equity | -0.95% | 1.30% | -6.59% | 19.04% | -4.85% | -0.816 | 0.801 | 1.080 | -1.15% |
| EMERGING_MARKETS | VWO | international_equity | -0.53% | 0.03% | -7.53% | 19.18% | -7.05% | -0.675 | 0.811 | 1.107 | -1.99% |
| EUROPE | VGK | international_equity | -0.40% | 1.25% | -7.99% | 14.23% | -3.12% | -0.786 | 0.748 | 0.918 | -0.64% |
| JAPAN | EWJ | international_equity | -4.27% | 0.22% | -8.14% | 23.74% | -7.86% | -0.944 | 0.720 | 1.180 | -4.27% |
| CHINA | MCHI | international_equity | 2.00% | 1.59% | -20.96% | 18.90% | -11.15% | -0.501 | 0.541 | 0.852 | -15.57% |
| INDIA | INDA | international_equity | -0.86% | 0.73% | -17.58% | 12.91% | -4.59% | -0.731 | 0.551 | 0.643 | -10.38% |
| GOLD | IAU | precious_metals | 4.10% | 7.54% | -27.23% | 25.80% | -12.55% | -0.440 | 0.310 | 0.687 | -16.19% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | 4.39% | 2.12% | 12.80% | 22.02% | -14.33% | -0.363 | -0.181 | -0.282 | -1.90% |
| SEMICONDUCTORS | SMH | technology_and_growth | -4.49% | -6.17% | 33.30% | 53.57% | -24.62% | 0.312 | 0.780 | 2.364 | -15.89% |
| SOFTWARE | IGV | technology_and_growth | -4.11% | 12.45% | -0.90% | 35.35% | -21.29% | -0.924 | 0.509 | 1.183 | -13.47% |
| BROAD_AI_TECH | AIQ | technology_and_growth | -2.46% | 2.77% | 11.94% | 39.44% | -20.19% | -0.496 | 0.847 | 1.906 | -10.14% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | -4.93% | 1.78% | -15.69% | 37.85% | -23.82% | -0.666 | 0.802 | 2.179 | -14.00% |
| CYBERSECURITY | CIBR | technology_and_growth | -8.56% | 2.58% | 26.11% | 33.09% | -11.74% | -0.410 | 0.540 | 1.114 | -8.56% |
| SOLAR | TAN | clean_energy | -5.22% | -9.46% | -17.98% | 45.15% | -35.51% | -0.090 | 0.632 | 1.903 | -32.73% |
| METALS_MINING | XME | materials_and_mining | -0.49% | 8.79% | -21.38% | 41.38% | -26.49% | -0.260 | 0.597 | 1.747 | -13.59% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | -1.10% | 1.53% | -4.21% | 11.08% | -2.04% | -0.808 | 0.775 | 0.705 | -1.12% |
| BIOTECH | XBI | healthcare_and_biotech | 4.16% | 5.38% | 10.36% | 31.38% | -10.51% | -0.336 | 0.471 | 1.016 | -3.64% |
| REGIONAL_BANKS | KRE | financials | -3.91% | -3.21% | -2.04% | 18.94% | -4.13% | -0.819 | 0.428 | 0.750 | -4.13% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | -4.86% | 0.76% | -14.73% | 25.33% | -8.58% | -0.402 | 0.565 | 1.013 | -6.18% |
| CANADA | EWC | international_equity | -0.53% | 2.17% | -4.82% | 11.50% | -3.20% | -0.386 | 0.672 | 0.742 | -0.74% |
| UNITED_KINGDOM | EWU | international_equity | 0.58% | 0.72% | -9.28% | 12.73% | -3.40% | -0.525 | 0.603 | 0.699 | -0.29% |
| AUSTRALIA | EWA | international_equity | 0.03% | 1.05% | -10.13% | 16.46% | -4.78% | -0.777 | 0.672 | 0.923 | -2.17% |
| SOUTH_KOREA | EWY | international_equity | -0.26% | 2.50% | 16.27% | 80.53% | -34.21% | 0.105 | 0.636 | 2.748 | -18.72% |
| TAIWAN | EWT | international_equity | -3.19% | 0.32% | 30.15% | 43.37% | -19.83% | -0.677 | 0.760 | 1.846 | -6.69% |
| BRAZIL | EWZ | international_equity | 1.10% | -8.80% | -14.03% | 20.85% | -8.97% | -0.723 | 0.503 | 0.974 | -17.41% |
| MEXICO | EWW | international_equity | 0.07% | -3.61% | -12.40% | 18.73% | -6.47% | -0.392 | 0.544 | 0.928 | -5.69% |
| SOUTH_AFRICA | EZA | international_equity | 4.66% | 9.86% | -23.97% | 31.22% | -11.54% | -0.726 | 0.619 | 1.585 | -11.75% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | -0.20% | -1.50% | -11.33% | 4.56% | -1.85% | 0.062 | 0.402 | 0.139 | -1.66% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | -0.65% | -2.15% | -10.84% | 3.05% | -2.15% | 1.020 | 0.392 | 0.092 | -1.69% |
| EMERGING_MARKET_BONDS | EMB | credit | -0.72% | -2.04% | -10.16% | 5.43% | -1.96% | -0.659 | 0.689 | 0.309 | -1.38% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | -0.54% | -2.10% | -10.97% | 3.50% | -1.45% | -0.592 | 0.471 | 0.131 | -1.80% |
| SILVER | SLV | precious_metals | 6.02% | 12.32% | -33.84% | 44.30% | -27.73% | -0.495 | 0.351 | 1.688 | -41.61% |
| COPPER | CPER | non_energy_commodities | -1.25% | -1.78% | 0.66% | 25.00% | -10.57% | -0.540 | 0.546 | 1.192 | -3.67% |
| AGRICULTURE | DBA | non_energy_commodities | 2.75% | -1.50% | -0.78% | 13.16% | -6.19% | -0.577 | 0.081 | 0.070 | -1.22% |
| OIL | USO | energy | 7.61% | 0.14% | 52.41% | 52.50% | -28.42% | -0.589 | -0.340 | -1.268 | -12.04% |
| US_DOLLAR | UUP | currencies | -0.96% | -3.93% | -4.87% | 5.13% | -2.52% | -0.498 | -0.307 | -0.138 | -2.41% |
| EURO | FXE | currencies | 1.32% | 0.39% | -12.49% | 4.91% | -2.66% | -0.733 | 0.288 | 0.128 | -2.53% |
| YEN | FXY | currencies | 0.23% | 0.51% | -14.86% | 7.91% | -3.08% | 1.498 | 0.186 | 0.119 | -8.21% |
| BITCOIN_ETF | IBIT | crypto_assets | 14.83% | 8.31% | -11.69% | 39.64% | -24.34% | -0.340 | 0.482 | 1.681 | -42.21% |
| ETHEREUM_ETF | ETHA | crypto_assets | 23.33% | 18.84% | -11.13% | 59.08% | -27.31% | -0.090 | 0.504 | 2.631 | -52.04% |
