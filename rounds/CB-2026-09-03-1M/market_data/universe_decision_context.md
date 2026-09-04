# Full-Universe Horizon-Specific Decision Context

Profile: monthly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: tiingo_eod_adjusted_price_and_volume
- As-of date requested: 2026-09-03
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | 0.27% |
| spy_return_21s | 0.44% |
| rsp_return_5s | -0.63% |
| rsp_return_21s | 0.15% |
| hyg_return_5s | -0.28% |
| hyg_return_21s | 0.16% |
| tlt_return_5s | -0.90% |
| tlt_return_21s | -0.74% |
| uup_return_5s | -0.04% |
| uup_return_21s | -0.28% |
| uso_return_5s | 9.29% |
| uso_return_21s | 23.69% |
| iau_return_5s | -2.91% |
| iau_return_21s | 5.32% |
| rsp_minus_spy_5s | -0.90% |
| rsp_minus_spy_21s | -0.29% |
| positive_asset_share_5s | 40.58% |
| positive_asset_share_21s | 55.07% |
| active_return_dispersion_5s |  |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_5s | active_return_21s | prior_105s_active_return | volatility_63s | max_drawdown_63s | volume_zscore_20v120 | corr_spy_252s | beta_spy_252s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | -0.44% | -13.59% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.08% | -0.14% | -12.10% | 0.20% | -0.01% | -0.581 | -0.100 | -0.002 | 0.00% |
| SP500 | SPY | diversified_us_equity | 0.27% | 0.00% | 0.00% | 13.86% | -4.18% | -1.118 | 1.000 | 1.000 | -0.61% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | 0.08% | -0.10% | 0.09% | 13.79% | -4.11% | -0.666 | 0.995 | 1.012 | -0.88% |
| NASDAQ100 | QQQ | technology_and_growth | -0.48% | -0.39% | 4.49% | 25.82% | -10.96% | -1.141 | 0.929 | 1.423 | -3.71% |
| LARGE_GROWTH | IWF | technology_and_growth | -0.37% | -0.81% | -4.01% | 21.40% | -10.00% | -0.792 | 0.934 | 1.290 | -4.06% |
| LARGE_VALUE | IWD | diversified_us_equity | 0.70% | 0.83% | 3.33% | 11.25% | -2.40% | -0.643 | 0.800 | 0.698 | 0.00% |
| MID_CAP | IJH | diversified_us_equity | -1.17% | -2.06% | -2.84% | 13.96% | -5.17% | -0.745 | 0.808 | 0.977 | -3.71% |
| SMALL_CAP | IWM | diversified_us_equity | -1.54% | -1.97% | 3.64% | 16.47% | -4.76% | -1.149 | 0.819 | 1.202 | -3.24% |
| SMALL_VALUE | IWN | diversified_us_equity | -0.45% | -1.04% | 2.97% | 12.95% | -3.29% | -0.994 | 0.736 | 0.941 | -1.63% |
| DIVIDEND | SCHD | diversified_us_equity | 0.72% | 3.84% | -4.21% | 11.62% | -2.93% | -0.014 | 0.281 | 0.241 | -0.37% |
| LOW_VOL | SPLV | diversified_us_equity | 0.16% | -1.68% | -12.47% | 12.61% | -4.22% | -0.669 | 0.016 | 0.014 | -3.32% |
| MOMENTUM | MTUM | diversified_us_equity | -1.58% | -3.85% | 12.14% | 37.72% | -17.99% | -0.364 | 0.769 | 1.573 | -13.27% |
| TECHNOLOGY | XLK | technology_and_growth | -1.40% | -0.41% | 19.35% | 34.78% | -13.67% | -1.392 | 0.852 | 1.746 | -6.06% |
| COMMUNICATIONS | XLC | technology_and_growth | 1.77% | 1.82% | -19.43% | 19.82% | -7.06% | -1.091 | 0.567 | 0.673 | -5.03% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | 0.50% | -2.28% | -11.39% | 21.69% | -8.09% | -1.310 | 0.765 | 1.163 | -6.10% |
| CONSUMER_STAPLES | XLP | consumer_defensive | 0.21% | -0.52% | -12.42% | 17.28% | -3.57% | -1.009 | -0.068 | -0.076 | -4.08% |
| HEALTHCARE | XLV | healthcare_and_biotech | 0.98% | 5.10% | -6.02% | 18.61% | -3.74% | -1.071 | 0.221 | 0.276 | -1.38% |
| FINANCIALS | XLF | financials | 1.17% | 0.53% | 0.60% | 12.65% | -2.25% | -0.936 | 0.538 | 0.616 | 0.00% |
| INDUSTRIALS | XLI | industrials_and_defense | -2.37% | -6.77% | -4.72% | 18.78% | -7.39% | -0.865 | 0.713 | 0.954 | -6.41% |
| ENERGY | XLE | energy | 3.74% | 12.32% | -10.74% | 22.61% | -9.47% | -0.893 | -0.179 | -0.303 | -0.74% |
| MATERIALS | XLB | materials_and_mining | -1.15% | -0.48% | -9.18% | 19.77% | -4.75% | -0.475 | 0.527 | 0.736 | -1.96% |
| UTILITIES | XLU | rate_sensitive_defensive | -0.35% | -1.88% | -19.26% | 14.79% | -8.77% | -0.367 | 0.116 | 0.138 | -8.65% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | -0.92% | -2.54% | -7.69% | 15.30% | -4.96% | -0.472 | 0.241 | 0.264 | -3.83% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | -0.66% | -1.19% | -15.28% | 4.86% | -2.11% | 0.181 | 0.282 | 0.102 | -3.62% |
| LONG_TREASURY | TLT | rates_and_duration | -0.90% | -1.18% | -18.29% | 9.70% | -6.25% | 0.180 | 0.230 | 0.168 | -7.21% |
| TIPS | TIP | rates_and_duration | -0.41% | -0.44% | -14.09% | 3.60% | -1.33% | -0.482 | 0.254 | 0.066 | -1.16% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | -0.74% | -1.18% | -15.11% | 5.42% | -2.92% | -0.590 | 0.471 | 0.195 | -2.96% |
| HIGH_YIELD_CREDIT | HYG | credit | -0.28% | -0.28% | -11.81% | 3.06% | -0.80% | -0.690 | 0.776 | 0.229 | -0.34% |
| AGGREGATE_BONDS | AGG | rates_and_duration | -0.55% | -0.87% | -14.45% | 4.05% | -1.71% | -0.416 | 0.390 | 0.114 | -2.11% |
| DEVELOPED_EX_US | VEA | international_equity | 0.03% | 1.07% | -2.85% | 19.01% | -4.75% | -0.773 | 0.800 | 1.083 | -0.47% |
| EMERGING_MARKETS | VWO | international_equity | -0.03% | 1.19% | -4.05% | 18.51% | -7.05% | -0.853 | 0.809 | 1.108 | -0.41% |
| EUROPE | VGK | international_equity | -0.59% | -0.56% | -3.34% | 14.03% | -2.65% | -0.924 | 0.745 | 0.911 | -1.56% |
| JAPAN | EWJ | international_equity | 2.15% | 2.44% | -2.21% | 24.02% | -7.86% | -0.878 | 0.722 | 1.185 | -0.58% |
| CHINA | MCHI | international_equity | -0.97% | -3.37% | -13.24% | 17.00% | -8.82% | -0.723 | 0.549 | 0.855 | -17.30% |
| INDIA | INDA | international_equity | 0.79% | -1.21% | -13.71% | 12.79% | -4.59% | -1.088 | 0.554 | 0.653 | -9.71% |
| GOLD | IAU | precious_metals | -2.91% | 4.88% | -29.99% | 27.56% | -11.25% | -0.421 | 0.324 | 0.733 | -17.20% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | 3.64% | 11.99% | -6.12% | 22.08% | -11.60% | -0.495 | -0.175 | -0.277 | 0.00% |
| SEMICONDUCTORS | SMH | technology_and_growth | -3.56% | -3.44% | 30.51% | 53.15% | -24.62% | -0.841 | 0.777 | 2.382 | -17.39% |
| SOFTWARE | IGV | technology_and_growth | -3.05% | 5.13% | 2.06% | 34.29% | -15.28% | -1.081 | 0.503 | 1.231 | -9.19% |
| BROAD_AI_TECH | AIQ | technology_and_growth | -0.37% | 2.67% | 12.01% | 38.45% | -17.76% | -0.877 | 0.847 | 1.923 | -8.33% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | -1.09% | -0.10% | -12.34% | 37.48% | -21.48% | -1.278 | 0.804 | 2.201 | -14.61% |
| CYBERSECURITY | CIBR | technology_and_growth | -5.43% | -2.75% | 35.10% | 33.10% | -9.53% | 0.106 | 0.523 | 1.154 | -6.73% |
| SOLAR | TAN | clean_energy | -4.06% | -7.36% | -18.80% | 42.11% | -33.48% | -0.735 | 0.629 | 1.885 | -35.45% |
| METALS_MINING | XME | materials_and_mining | -3.76% | 5.33% | -14.30% | 40.75% | -24.10% | -0.345 | 0.595 | 1.775 | -10.82% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | -0.63% | -0.29% | -3.13% | 11.20% | -2.33% | -1.088 | 0.772 | 0.698 | -1.22% |
| BIOTECH | XBI | healthcare_and_biotech | -2.29% | 6.99% | 10.02% | 30.53% | -10.51% | -0.336 | 0.474 | 1.033 | -3.05% |
| REGIONAL_BANKS | KRE | financials | 0.70% | -3.63% | 3.88% | 17.17% | -6.81% | -0.771 | 0.417 | 0.723 | -3.93% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | -3.53% | -10.86% | -8.35% | 24.23% | -11.79% | -0.464 | 0.570 | 1.032 | -10.76% |
| CANADA | EWC | international_equity | 0.34% | 2.34% | -6.29% | 12.09% | -3.26% | -0.435 | 0.675 | 0.757 | -0.27% |
| UNITED_KINGDOM | EWU | international_equity | 0.10% | 0.20% | -7.47% | 12.62% | -2.43% | -0.580 | 0.600 | 0.697 | -1.44% |
| AUSTRALIA | EWA | international_equity | 0.86% | 0.32% | -6.75% | 16.84% | -4.42% | -0.499 | 0.673 | 0.931 | -0.20% |
| SOUTH_KOREA | EWY | international_equity | -0.87% | 6.31% | 20.93% | 76.64% | -34.21% | -0.787 | 0.635 | 2.768 | -17.63% |
| TAIWAN | EWT | international_equity | 1.38% | 7.85% | 30.87% | 41.31% | -19.83% | -1.121 | 0.752 | 1.831 | -1.26% |
| BRAZIL | EWZ | international_equity | 6.63% | 5.15% | -13.33% | 22.37% | -8.05% | -0.246 | 0.486 | 0.954 | -7.75% |
| MEXICO | EWW | international_equity | -0.25% | -0.07% | -10.18% | 18.93% | -5.37% | -0.551 | 0.548 | 0.938 | -3.86% |
| SOUTH_AFRICA | EZA | international_equity | 0.36% | 7.00% | -18.01% | 30.63% | -11.18% | -0.603 | 0.622 | 1.608 | -10.12% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | -0.56% | -0.80% | -14.22% | 4.70% | -1.85% | 0.137 | 0.386 | 0.133 | -1.98% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | -1.04% | -1.89% | -13.94% | 3.00% | -2.79% | 0.775 | 0.370 | 0.088 | -2.79% |
| EMERGING_MARKET_BONDS | EMB | credit | -0.28% | -0.76% | -12.66% | 5.38% | -1.96% | -0.659 | 0.680 | 0.303 | -1.18% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | -0.38% | -1.42% | -13.63% | 3.60% | -1.90% | -0.386 | 0.463 | 0.130 | -2.07% |
| SILVER | SLV | precious_metals | -3.54% | 7.55% | -38.09% | 45.35% | -24.77% | -0.653 | 0.363 | 1.763 | -42.66% |
| COPPER | CPER | non_energy_commodities | -0.18% | -2.74% | 1.22% | 24.41% | -8.61% | -0.543 | 0.560 | 1.241 | -2.30% |
| AGRICULTURE | DBA | non_energy_commodities | 0.94% | 4.85% | -8.97% | 12.99% | -2.87% | 0.079 | 0.061 | 0.053 | -1.36% |
| OIL | USO | energy | 9.29% | 23.25% | 5.69% | 52.34% | -24.48% | -0.631 | -0.339 | -1.281 | -7.11% |
| US_DOLLAR | UUP | currencies | -0.04% | -0.72% | -11.37% | 5.36% | -2.52% | -1.003 | -0.293 | -0.129 | -2.06% |
| EURO | FXE | currencies | -0.16% | 0.29% | -13.72% | 5.02% | -2.22% | -0.695 | 0.270 | 0.117 | -2.92% |
| YEN | FXY | currencies | 2.38% | 0.80% | -13.85% | 9.07% | -2.49% | 0.372 | 0.180 | 0.117 | -6.29% |
| BITCOIN_ETF | IBIT | crypto_assets | 2.34% | 25.72% | -22.63% | 40.36% | -11.79% | 0.626 | 0.481 | 1.699 | -34.98% |
| ETHEREUM_ETF | ETHA | crypto_assets | 0.79% | 30.91% | -21.94% | 58.17% | -14.68% | 0.972 | 0.498 | 2.520 | -46.86% |
