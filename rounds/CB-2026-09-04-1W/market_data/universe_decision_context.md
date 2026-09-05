# Full-Universe Horizon-Specific Decision Context

Profile: weekly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: yahoo_chart_adjusted_close_and_reported_volume
- As-of date requested: 2026-09-04
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | 0.11% |
| spy_return_21s | 0.21% |
| rsp_return_5s | -0.77% |
| rsp_return_21s | 0.19% |
| hyg_return_5s | -0.18% |
| hyg_return_21s | 0.17% |
| tlt_return_5s | -0.43% |
| tlt_return_21s | 0.01% |
| uup_return_5s | -0.35% |
| uup_return_21s | -0.39% |
| uso_return_5s | 9.45% |
| uso_return_21s | 19.42% |
| iau_return_5s | -0.51% |
| iau_return_21s | 4.41% |
| rsp_minus_spy_5s | -0.87% |
| rsp_minus_spy_21s | -0.02% |
| positive_asset_share_5s | 53.62% |
| positive_asset_share_21s | 59.42% |
| active_return_dispersion_5s | 2.03% |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_3s | active_return_5s | prior_16s_active_return | volatility_21s | max_drawdown_21s | volume_zscore_5v60 | corr_spy_63s | beta_spy_63s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | -0.11% | -0.10% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.07% | -0.02% | 0.12% | 0.17% | 0.00% | 0.472 | -0.009 | -0.000 | 0.00% |
| SP500 | SPY | diversified_us_equity | 1.10% | 0.00% | 0.00% | 8.20% | -2.07% | -0.851 | 1.000 | 1.000 | -0.99% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | 1.22% | -0.01% | -0.03% | 8.62% | -2.38% | -0.617 | 0.992 | 0.979 | -1.19% |
| NASDAQ100 | QQQ | technology_and_growth | 1.60% | 0.24% | 0.15% | 13.20% | -3.52% | -0.787 | 0.911 | 1.699 | -3.54% |
| LARGE_GROWTH | IWF | technology_and_growth | 1.82% | 0.43% | -0.71% | 13.82% | -3.68% | -0.381 | 0.893 | 1.418 | -4.08% |
| LARGE_VALUE | IWD | diversified_us_equity | 0.66% | -0.38% | 0.76% | 8.10% | -1.09% | -0.403 | 0.658 | 0.543 | -0.67% |
| MID_CAP | IJH | diversified_us_equity | 1.68% | 0.01% | -1.39% | 11.70% | -5.17% | -0.644 | 0.773 | 0.805 | -3.58% |
| SMALL_CAP | IWM | diversified_us_equity | 1.87% | -0.02% | -0.94% | 12.54% | -4.76% | -0.446 | 0.749 | 0.864 | -2.98% |
| SMALL_VALUE | IWN | diversified_us_equity | 2.13% | 0.55% | -0.41% | 9.70% | -3.29% | 0.209 | 0.601 | 0.551 | -1.24% |
| DIVIDEND | SCHD | diversified_us_equity | -0.03% | -0.40% | 3.46% | 9.73% | -1.16% | 0.057 | 0.055 | 0.050 | -1.16% |
| LOW_VOL | SPLV | diversified_us_equity | 0.27% | -0.56% | -1.46% | 8.59% | -2.20% | -0.091 | -0.200 | -0.193 | -3.96% |
| MOMENTUM | MTUM | diversified_us_equity | 2.81% | 1.61% | -2.85% | 20.13% | -7.93% | -1.110 | 0.668 | 1.875 | -11.69% |
| TECHNOLOGY | XLK | technology_and_growth | 1.98% | 0.75% | 0.09% | 20.99% | -5.62% | -0.884 | 0.809 | 2.023 | -5.40% |
| COMMUNICATIONS | XLC | technology_and_growth | 1.04% | -0.96% | 1.53% | 16.47% | -2.19% | -0.955 | 0.383 | 0.592 | -6.16% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | 0.28% | -2.07% | -0.86% | 16.98% | -4.40% | -0.899 | 0.680 | 1.138 | -7.35% |
| CONSUMER_STAPLES | XLP | consumer_defensive | -0.79% | -1.13% | 0.30% | 14.47% | -3.28% | -0.598 | -0.223 | -0.297 | -4.85% |
| HEALTHCARE | XLV | healthcare_and_biotech | -0.13% | 0.06% | 3.98% | 18.69% | -2.93% | -0.925 | -0.133 | -0.195 | -2.41% |
| FINANCIALS | XLF | financials | 1.57% | -0.11% | 0.40% | 11.86% | -2.25% | -0.415 | 0.341 | 0.340 | -0.79% |
| INDUSTRIALS | XLI | industrials_and_defense | 1.47% | -1.16% | -4.23% | 12.09% | -7.39% | 0.669 | 0.660 | 0.960 | -6.03% |
| ENERGY | XLE | energy | -1.10% | 2.09% | 7.67% | 21.84% | -2.65% | -0.331 | -0.435 | -0.757 | -1.60% |
| MATERIALS | XLB | materials_and_mining | 0.71% | -1.50% | 1.83% | 15.13% | -2.98% | 0.682 | 0.378 | 0.571 | -2.29% |
| UTILITIES | XLU | rate_sensitive_defensive | 1.22% | 0.71% | -1.60% | 13.83% | -4.69% | 1.697 | -0.069 | -0.079 | -8.53% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | -0.25% | -1.35% | -0.84% | 12.22% | -3.59% | 0.582 | -0.128 | -0.152 | -4.52% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | 0.16% | -0.40% | -0.21% | 4.58% | -1.15% | -0.057 | 0.396 | 0.147 | -3.65% |
| LONG_TREASURY | TLT | rates_and_duration | 0.42% | -0.54% | 0.33% | 10.18% | -1.70% | -0.336 | 0.299 | 0.225 | -7.05% |
| TIPS | TIP | rates_and_duration | 0.15% | -0.08% | -0.04% | 3.57% | -0.77% | -0.176 | 0.315 | 0.085 | -1.19% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | 0.25% | -0.51% | -0.11% | 5.61% | -1.12% | -0.505 | 0.478 | 0.197 | -2.98% |
| HIGH_YIELD_CREDIT | HYG | credit | 0.08% | -0.29% | 0.25% | 2.56% | -0.48% | 0.225 | 0.774 | 0.174 | -0.41% |
| AGGREGATE_BONDS | AGG | rates_and_duration | 0.24% | -0.27% | -0.04% | 4.00% | -0.92% | 0.364 | 0.431 | 0.132 | -2.06% |
| DEVELOPED_EX_US | VEA | international_equity | 2.29% | 0.85% | 1.20% | 11.86% | -2.28% | -0.562 | 0.771 | 1.047 | -0.04% |
| EMERGING_MARKETS | VWO | international_equity | 1.25% | 0.96% | 1.28% | 9.41% | -1.37% | -0.741 | 0.811 | 1.067 | 0.00% |
| EUROPE | VGK | international_equity | 1.12% | -0.37% | 0.06% | 8.31% | -2.65% | -0.339 | 0.714 | 0.745 | -1.56% |
| JAPAN | EWJ | international_equity | 3.21% | 2.40% | 0.65% | 16.87% | -4.27% | -0.309 | 0.733 | 1.304 | -0.19% |
| CHINA | MCHI | international_equity | 0.92% | -0.69% | -1.32% | 14.09% | -4.50% | -0.769 | 0.343 | 0.440 | -16.48% |
| INDIA | INDA | international_equity | 0.67% | 0.60% | -1.22% | 9.10% | -2.03% | -0.391 | 0.529 | 0.513 | -9.73% |
| GOLD | IAU | precious_metals | 2.51% | -0.62% | 4.84% | 27.34% | -7.30% | -0.497 | 0.440 | 0.913 | -17.90% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | -0.21% | 3.26% | 6.63% | 18.08% | -2.57% | -0.013 | -0.285 | -0.481 | -0.42% |
| SEMICONDUCTORS | SMH | technology_and_growth | 4.00% | 2.40% | -3.32% | 31.28% | -8.22% | -0.852 | 0.714 | 2.789 | -15.23% |
| SOFTWARE | IGV | technology_and_growth | -1.52% | -4.61% | 10.04% | 41.24% | -6.25% | -0.611 | 0.460 | 1.201 | -11.21% |
| BROAD_AI_TECH | AIQ | technology_and_growth | 2.00% | 0.05% | 3.56% | 20.05% | -3.59% | -0.780 | 0.812 | 2.201 | -8.30% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | 1.75% | -0.17% | -0.82% | 25.61% | -7.91% | -0.614 | 0.849 | 2.299 | -15.00% |
| CYBERSECURITY | CIBR | technology_and_growth | -1.67% | -4.14% | 2.15% | 40.93% | -9.53% | 0.370 | 0.524 | 1.301 | -7.45% |
| SOLAR | TAN | clean_energy | 2.52% | -1.36% | -5.18% | 24.99% | -11.17% | -0.631 | 0.749 | 2.245 | -35.02% |
| METALS_MINING | XME | materials_and_mining | 2.46% | -0.21% | 7.50% | 37.90% | -5.88% | -0.982 | 0.580 | 1.701 | -10.64% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | 0.65% | -0.87% | 0.86% | 8.97% | -2.33% | -0.849 | 0.664 | 0.561 | -1.69% |
| BIOTECH | XBI | healthcare_and_biotech | 0.25% | 0.77% | 5.00% | 32.05% | -4.23% | -0.862 | 0.258 | 0.593 | -3.39% |
| REGIONAL_BANKS | KRE | financials | 3.65% | 1.20% | -2.97% | 15.10% | -6.81% | -0.077 | 0.187 | 0.251 | -3.41% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | 0.07% | -3.21% | -6.97% | 19.12% | -11.79% | 0.004 | 0.442 | 0.834 | -10.90% |
| CANADA | EWC | international_equity | 2.38% | 0.39% | 1.59% | 12.79% | -3.26% | 0.525 | 0.546 | 0.475 | -0.96% |
| UNITED_KINGDOM | EWU | international_equity | 0.83% | -0.03% | 0.41% | 8.19% | -2.43% | 0.306 | 0.368 | 0.356 | -1.62% |
| AUSTRALIA | EWA | international_equity | 1.85% | 0.66% | -0.63% | 12.91% | -2.83% | 0.402 | 0.527 | 0.630 | -0.66% |
| SOUTH_KOREA | EWY | international_equity | 7.43% | 4.70% | 9.69% | 46.86% | -8.13% | -1.021 | 0.619 | 3.460 | -13.84% |
| TAIWAN | EWT | international_equity | 2.22% | 3.86% | 5.70% | 20.96% | -4.15% | -0.820 | 0.739 | 2.227 | 0.00% |
| BRAZIL | EWZ | international_equity | 3.53% | 6.39% | -0.83% | 25.08% | -5.89% | 1.427 | 0.299 | 0.510 | -8.41% |
| MEXICO | EWW | international_equity | 1.28% | 0.09% | -0.30% | 15.21% | -3.95% | -0.362 | 0.559 | 0.783 | -4.27% |
| SOUTH_AFRICA | EZA | international_equity | 3.02% | 1.19% | 5.64% | 30.05% | -4.10% | 0.278 | 0.650 | 1.465 | -10.28% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | 0.34% | -0.23% | 0.07% | 4.42% | -1.09% | 0.103 | 0.451 | 0.162 | -1.92% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | -0.29% | -0.97% | -0.52% | 3.02% | -1.76% | 2.443 | 0.496 | 0.115 | -2.76% |
| EMERGING_MARKET_BONDS | EMB | credit | 0.40% | -0.11% | -0.17% | 4.80% | -0.92% | 0.332 | 0.696 | 0.281 | -1.16% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | 0.38% | -0.17% | -0.71% | 3.71% | -1.21% | 0.463 | 0.495 | 0.139 | -1.96% |
| SILVER | SLV | precious_metals | 3.28% | -0.44% | 7.36% | 38.81% | -7.73% | -0.587 | 0.498 | 1.647 | -43.35% |
| COPPER | CPER | non_energy_commodities | 2.25% | 0.60% | -2.78% | 19.12% | -4.15% | -0.512 | 0.578 | 1.031 | -2.20% |
| AGRICULTURE | DBA | non_energy_commodities | -2.17% | -1.27% | 6.31% | 11.65% | -2.17% | 1.719 | 0.046 | 0.046 | -2.17% |
| OIL | USO | energy | 0.68% | 9.34% | 9.01% | 39.20% | -6.31% | -0.373 | -0.396 | -1.607 | -7.19% |
| US_DOLLAR | UUP | currencies | -0.46% | -0.46% | -0.14% | 5.32% | -1.13% | -0.413 | -0.351 | -0.143 | -1.82% |
| EURO | FXE | currencies | 0.21% | 0.13% | 0.54% | 4.58% | -0.76% | -0.265 | 0.317 | 0.117 | -3.04% |
| YEN | FXY | currencies | 2.57% | 2.37% | -1.21% | 10.05% | -1.79% | 0.036 | 0.321 | 0.228 | -6.61% |
| BITCOIN_ETF | IBIT | crypto_assets | 3.36% | 2.92% | 20.20% | 45.12% | -3.38% | 0.145 | 0.343 | 1.047 | -36.55% |
| ETHEREUM_ETF | ETHA | crypto_assets | 1.59% | 0.71% | 27.47% | 57.39% | -4.35% | -0.100 | 0.345 | 1.433 | -48.25% |
