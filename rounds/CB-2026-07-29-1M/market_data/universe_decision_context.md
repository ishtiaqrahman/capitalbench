# Full-Universe Horizon-Specific Decision Context

Profile: monthly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: yahoo_chart_adjusted_close_and_reported_volume
- As-of date requested: 2026-07-29
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | -2.40% |
| spy_return_21s | -1.56% |
| rsp_return_5s | 1.42% |
| rsp_return_21s | 1.26% |
| hyg_return_5s | -0.35% |
| hyg_return_21s | -0.50% |
| tlt_return_5s | -0.71% |
| tlt_return_21s | -4.91% |
| uup_return_5s | -0.11% |
| uup_return_21s | 0.18% |
| uso_return_5s | -1.80% |
| uso_return_21s | 20.76% |
| iau_return_5s | -2.12% |
| iau_return_21s | 0.68% |
| rsp_minus_spy_5s | 3.83% |
| rsp_minus_spy_21s | 2.82% |
| positive_asset_share_5s | 33.33% |
| positive_asset_share_21s | 44.93% |
| active_return_dispersion_5s |  |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_5s | active_return_21s | prior_105s_active_return | volatility_63s | max_drawdown_63s | volume_zscore_20v120 | corr_spy_252s | beta_spy_252s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | 1.56% | -7.11% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.07% | 1.85% | -5.61% | 0.21% | -0.01% | -0.334 | -0.108 | -0.002 | 0.00% |
| SP500 | SPY | diversified_us_equity | -2.40% | 0.00% | 0.00% | 13.31% | -4.49% | -0.998 | 1.000 | 1.000 | -3.72% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | -2.29% | -0.27% | 0.48% | 13.26% | -4.36% | -0.844 | 0.995 | 1.012 | -3.45% |
| NASDAQ100 | QQQ | technology_and_growth | -6.18% | -7.05% | 7.89% | 24.71% | -11.22% | -0.909 | 0.930 | 1.391 | -11.22% |
| LARGE_GROWTH | IWF | technology_and_growth | -5.68% | -4.94% | -4.09% | 19.10% | -11.35% | -0.721 | 0.935 | 1.261 | -11.35% |
| LARGE_VALUE | IWD | diversified_us_equity | 0.81% | 4.35% | 4.45% | 12.19% | -2.40% | -0.573 | 0.808 | 0.718 | -1.00% |
| MID_CAP | IJH | diversified_us_equity | -1.27% | -0.79% | 3.36% | 14.83% | -4.25% | -0.983 | 0.804 | 0.991 | -3.09% |
| SMALL_CAP | IWM | diversified_us_equity | -1.78% | -1.92% | 6.29% | 18.54% | -4.81% | -1.199 | 0.817 | 1.239 | -3.95% |
| SMALL_VALUE | IWN | diversified_us_equity | -0.20% | 1.70% | 6.71% | 15.58% | -4.01% | -0.700 | 0.737 | 1.006 | -1.15% |
| DIVIDEND | SCHD | diversified_us_equity | 2.83% | 7.51% | 3.40% | 12.12% | -2.95% | -0.335 | 0.314 | 0.273 | -0.18% |
| LOW_VOL | SPLV | diversified_us_equity | 1.76% | 4.33% | -2.90% | 13.10% | -4.09% | -0.919 | 0.050 | 0.042 | -0.55% |
| MOMENTUM | MTUM | diversified_us_equity | -9.91% | -14.18% | 22.27% | 37.64% | -17.99% | 1.409 | 0.772 | 1.508 | -17.99% |
| TECHNOLOGY | XLK | technology_and_growth | -7.60% | -8.60% | 18.43% | 33.43% | -15.86% | -1.012 | 0.860 | 1.683 | -15.86% |
| COMMUNICATIONS | XLC | technology_and_growth | 0.28% | 3.07% | -14.29% | 17.17% | -9.99% | 0.029 | 0.622 | 0.706 | -8.27% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | -2.11% | -3.15% | -11.27% | 20.86% | -10.72% | -0.338 | 0.792 | 1.194 | -10.01% |
| CONSUMER_STAPLES | XLP | consumer_defensive | 3.53% | 5.10% | -4.38% | 16.91% | -4.95% | -0.787 | -0.047 | -0.052 | -1.72% |
| HEALTHCARE | XLV | healthcare_and_biotech | 4.27% | 4.98% | -2.82% | 18.45% | -3.74% | -0.620 | 0.257 | 0.318 | -0.61% |
| FINANCIALS | XLF | financials | 1.12% | 7.07% | -4.87% | 13.64% | -2.42% | -0.660 | 0.561 | 0.648 | -1.60% |
| INDUSTRIALS | XLI | industrials_and_defense | -1.22% | -1.78% | 4.20% | 20.02% | -4.80% | -1.101 | 0.716 | 0.949 | -4.80% |
| ENERGY | XLE | energy | -0.93% | 11.02% | 2.25% | 24.63% | -13.21% | -0.862 | -0.135 | -0.222 | -5.57% |
| MATERIALS | XLB | materials_and_mining | 1.81% | 3.69% | -4.92% | 20.18% | -6.43% | -0.596 | 0.550 | 0.761 | -2.71% |
| UTILITIES | XLU | rate_sensitive_defensive | -2.22% | -0.85% | 0.28% | 17.36% | -8.00% | -0.818 | 0.141 | 0.166 | -4.65% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | 2.11% | 3.87% | 3.48% | 16.06% | -3.38% | -0.855 | 0.252 | 0.282 | -0.11% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | 0.08% | -0.11% | -6.46% | 5.07% | -2.00% | -0.950 | 0.228 | 0.084 | -3.37% |
| LONG_TREASURY | TLT | rates_and_duration | -0.71% | -3.35% | -5.62% | 9.47% | -4.91% | -0.829 | 0.192 | 0.142 | -7.06% |
| TIPS | TIP | rates_and_duration | 0.00% | 0.58% | -5.89% | 3.56% | -1.53% | -0.800 | 0.240 | 0.065 | -1.18% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | -0.42% | -1.27% | -6.22% | 5.41% | -2.83% | -0.476 | 0.427 | 0.178 | -3.12% |
| HIGH_YIELD_CREDIT | HYG | credit | -0.35% | 1.05% | -6.04% | 3.67% | -1.01% | -0.712 | 0.770 | 0.232 | -0.79% |
| AGGREGATE_BONDS | AGG | rates_and_duration | -0.03% | 0.06% | -6.28% | 4.20% | -1.71% | -0.423 | 0.336 | 0.101 | -2.19% |
| DEVELOPED_EX_US | VEA | international_equity | -2.18% | -1.22% | -0.77% | 20.71% | -4.85% | -0.755 | 0.801 | 1.065 | -4.75% |
| EMERGING_MARKETS | VWO | international_equity | -3.21% | -2.26% | -4.32% | 20.30% | -7.05% | -0.538 | 0.801 | 1.093 | -7.05% |
| EUROPE | VGK | international_equity | -0.26% | 2.45% | -6.24% | 17.96% | -3.86% | -0.981 | 0.744 | 0.918 | -1.23% |
| JAPAN | EWJ | international_equity | -3.08% | -2.58% | 2.07% | 22.41% | -7.86% | -0.772 | 0.713 | 1.144 | -7.86% |
| CHINA | MCHI | international_equity | 2.80% | 9.98% | -26.33% | 20.98% | -15.01% | -0.352 | 0.559 | 0.902 | -16.24% |
| INDIA | INDA | international_equity | 1.97% | 1.54% | -11.97% | 15.86% | -5.64% | -0.582 | 0.515 | 0.610 | -11.07% |
| GOLD | IAU | precious_metals | -2.12% | 2.23% | -29.63% | 23.85% | -16.01% | -0.597 | 0.305 | 0.666 | -25.14% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | -1.35% | 12.48% | 1.23% | 22.79% | -16.55% | 0.077 | -0.134 | -0.207 | -7.09% |
| SEMICONDUCTORS | SMH | technology_and_growth | -14.09% | -18.66% | 48.07% | 53.62% | -24.62% | 1.108 | 0.779 | 2.315 | -24.62% |
| SOFTWARE | IGV | technology_and_growth | 3.76% | 4.32% | -15.14% | 33.44% | -21.29% | -0.676 | 0.501 | 1.142 | -21.57% |
| BROAD_AI_TECH | AIQ | technology_and_growth | -6.92% | -11.27% | 13.81% | 39.20% | -20.19% | -0.099 | 0.843 | 1.859 | -20.19% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | -8.04% | -13.11% | -8.42% | 38.90% | -23.82% | -0.983 | 0.793 | 2.144 | -23.82% |
| CYBERSECURITY | CIBR | technology_and_growth | -0.60% | 1.89% | 16.08% | 32.25% | -11.74% | -0.225 | 0.531 | 1.076 | -6.27% |
| SOLAR | TAN | clean_energy | -11.24% | -15.66% | -4.36% | 45.97% | -35.51% | -0.778 | 0.588 | 1.794 | -35.51% |
| METALS_MINING | XME | materials_and_mining | -5.72% | -6.84% | -24.00% | 40.13% | -26.49% | -0.385 | 0.592 | 1.699 | -26.49% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | 1.42% | 2.82% | 0.86% | 11.21% | -2.04% | -0.863 | 0.777 | 0.716 | -0.90% |
| BIOTECH | XBI | healthcare_and_biotech | -2.76% | -5.01% | 16.18% | 30.37% | -9.96% | -0.230 | 0.479 | 1.001 | -9.96% |
| REGIONAL_BANKS | KRE | financials | 0.77% | 3.47% | 3.68% | 20.33% | -5.29% | -0.577 | 0.450 | 0.808 | -2.23% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | 2.23% | 0.36% | -6.08% | 26.08% | -8.58% | -0.416 | 0.564 | 0.991 | -5.79% |
| CANADA | EWC | international_equity | 0.02% | 4.69% | -4.30% | 13.22% | -3.20% | -0.691 | 0.682 | 0.766 | -0.92% |
| UNITED_KINGDOM | EWU | international_equity | 1.40% | 5.35% | -6.44% | 16.96% | -3.94% | -0.461 | 0.606 | 0.706 | -0.19% |
| AUSTRALIA | EWA | international_equity | 0.87% | 5.11% | -6.17% | 18.64% | -6.84% | -0.884 | 0.674 | 0.915 | -2.45% |
| SOUTH_KOREA | EWY | international_equity | -15.38% | -25.42% | 53.85% | 79.51% | -34.21% | 0.507 | 0.637 | 2.639 | -34.21% |
| TAIWAN | EWT | international_equity | -12.07% | -13.93% | 41.22% | 43.18% | -19.83% | 0.060 | 0.740 | 1.755 | -19.83% |
| BRAZIL | EWZ | international_equity | -3.14% | 4.22% | -15.06% | 23.99% | -15.56% | -1.055 | 0.511 | 0.998 | -14.19% |
| MEXICO | EWW | international_equity | -1.49% | 0.83% | -7.91% | 20.50% | -7.30% | -0.882 | 0.535 | 0.922 | -5.60% |
| SOUTH_AFRICA | EZA | international_equity | -1.43% | -0.56% | -25.09% | 32.74% | -14.17% | -0.509 | 0.622 | 1.574 | -22.25% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | 0.09% | 0.08% | -6.17% | 4.96% | -1.93% | -0.453 | 0.336 | 0.117 | -2.10% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | -0.10% | 0.02% | -5.79% | 3.10% | -2.15% | 0.377 | 0.330 | 0.077 | -1.67% |
| EMERGING_MARKET_BONDS | EMB | credit | -0.56% | -0.37% | -4.86% | 5.93% | -2.10% | -0.673 | 0.667 | 0.296 | -1.93% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | 0.02% | 0.32% | -5.96% | 4.25% | -1.44% | -0.561 | 0.424 | 0.117 | -1.71% |
| SILVER | SLV | precious_metals | -3.99% | -0.17% | -55.25% | 50.20% | -36.50% | -0.657 | 0.352 | 1.689 | -50.98% |
| COPPER | CPER | non_energy_commodities | -2.29% | 4.57% | -5.33% | 29.05% | -10.57% | -0.663 | 0.460 | 1.228 | -5.54% |
| AGRICULTURE | DBA | non_energy_commodities | -2.62% | 5.25% | -4.52% | 14.06% | -8.67% | -0.429 | 0.089 | 0.078 | -4.32% |
| OIL | USO | energy | -1.80% | 22.32% | 34.42% | 55.85% | -32.49% | -0.539 | -0.304 | -1.117 | -15.46% |
| US_DOLLAR | UUP | currencies | -0.11% | 1.73% | 0.07% | 5.01% | -0.98% | -0.289 | -0.267 | -0.123 | -0.63% |
| EURO | FXE | currencies | 0.35% | 1.86% | -11.90% | 4.76% | -3.57% | -0.824 | 0.251 | 0.118 | -4.50% |
| YEN | FXY | currencies | -0.18% | 0.62% | -13.24% | 6.52% | -4.58% | -0.058 | 0.107 | 0.066 | -10.65% |
| BITCOIN_ETF | IBIT | crypto_assets | -3.59% | 6.88% | -39.60% | 37.00% | -28.36% | -0.606 | 0.513 | 1.778 | -49.50% |
| ETHEREUM_ETF | ETHA | crypto_assets | -1.93% | 17.90% | -53.50% | 53.11% | -34.41% | -0.374 | 0.555 | 2.925 | -61.08% |
