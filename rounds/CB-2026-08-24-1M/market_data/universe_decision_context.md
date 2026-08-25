# Full-Universe Horizon-Specific Decision Context

Profile: monthly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: tiingo_eod_adjusted_price_and_volume
- As-of date requested: 2026-08-24
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | -1.19% |
| spy_return_21s | 3.32% |
| rsp_return_5s | 0.52% |
| rsp_return_21s | 3.91% |
| hyg_return_5s | 0.11% |
| hyg_return_21s | 1.08% |
| tlt_return_5s | 1.49% |
| tlt_return_21s | -0.43% |
| uup_return_5s | -0.50% |
| uup_return_21s | -2.17% |
| uso_return_5s | 1.47% |
| uso_return_21s | -3.28% |
| iau_return_5s | 5.25% |
| iau_return_21s | 14.74% |
| rsp_minus_spy_5s | 1.71% |
| rsp_minus_spy_21s | 0.59% |
| positive_asset_share_5s | 56.52% |
| positive_asset_share_21s | 79.71% |
| active_return_dispersion_5s |  |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_5s | active_return_21s | prior_105s_active_return | volatility_63s | max_drawdown_63s | volume_zscore_20v120 | corr_spy_252s | beta_spy_252s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | -3.32% | -8.86% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.07% | -3.02% | -7.36% | 0.21% | -0.01% | -0.368 | -0.099 | -0.002 | 0.00% |
| SP500 | SPY | diversified_us_equity | -1.19% | 0.00% | 0.00% | 13.72% | -4.49% | -0.815 | 1.000 | 1.000 | -1.85% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | -1.32% | 0.04% | 0.22% | 13.65% | -4.36% | -0.644 | 0.995 | 1.013 | -1.88% |
| NASDAQ100 | QQQ | technology_and_growth | -3.23% | -0.09% | 5.18% | 25.76% | -11.22% | -0.727 | 0.930 | 1.416 | -5.23% |
| LARGE_GROWTH | IWF | technology_and_growth | -3.23% | -0.44% | -3.63% | 21.05% | -11.36% | -0.885 | 0.936 | 1.283 | -5.92% |
| LARGE_VALUE | IWD | diversified_us_equity | 0.66% | 0.74% | 3.20% | 11.22% | -2.40% | -0.671 | 0.804 | 0.704 | -0.17% |
| MID_CAP | IJH | diversified_us_equity | -2.91% | -2.75% | -1.43% | 13.84% | -3.14% | -0.817 | 0.810 | 0.985 | -3.14% |
| SMALL_CAP | IWM | diversified_us_equity | -2.00% | -0.99% | 3.38% | 16.92% | -3.95% | -1.082 | 0.821 | 1.218 | -2.33% |
| SMALL_VALUE | IWN | diversified_us_equity | -1.06% | -2.13% | 4.09% | 13.55% | -2.75% | -0.676 | 0.735 | 0.963 | -1.48% |
| DIVIDEND | SCHD | diversified_us_equity | 2.68% | 2.45% | -1.54% | 11.88% | -2.95% | 0.344 | 0.291 | 0.251 | 0.00% |
| LOW_VOL | SPLV | diversified_us_equity | 0.54% | -4.67% | -6.44% | 13.03% | -3.75% | -0.518 | 0.022 | 0.018 | -2.33% |
| MOMENTUM | MTUM | diversified_us_equity | -6.67% | -5.21% | 14.06% | 38.70% | -17.99% | 0.418 | 0.768 | 1.561 | -12.93% |
| TECHNOLOGY | XLK | technology_and_growth | -5.40% | -0.95% | 18.41% | 35.19% | -15.86% | -0.970 | 0.854 | 1.728 | -9.05% |
| COMMUNICATIONS | XLC | technology_and_growth | 1.35% | 2.34% | -16.18% | 19.62% | -9.44% | -0.735 | 0.577 | 0.676 | -5.92% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | 1.33% | 4.80% | -13.34% | 21.87% | -10.72% | -0.914 | 0.776 | 1.177 | -4.62% |
| CONSUMER_STAPLES | XLP | consumer_defensive | 3.27% | 0.63% | -13.11% | 17.74% | -3.57% | -0.675 | -0.059 | -0.066 | -1.62% |
| HEALTHCARE | XLV | healthcare_and_biotech | 4.58% | 4.14% | -5.45% | 19.79% | -3.74% | -0.519 | 0.228 | 0.283 | -0.56% |
| FINANCIALS | XLF | financials | 1.11% | 0.07% | 3.09% | 13.34% | -2.25% | -0.820 | 0.542 | 0.617 | -0.07% |
| INDUSTRIALS | XLI | industrials_and_defense | -3.93% | -5.32% | -3.84% | 18.52% | -4.80% | -0.972 | 0.720 | 0.959 | -4.03% |
| ENERGY | XLE | energy | 0.85% | 2.53% | 0.72% | 23.34% | -10.60% | -0.932 | -0.161 | -0.272 | -1.00% |
| MATERIALS | XLB | materials_and_mining | 2.57% | 1.20% | -11.28% | 19.47% | -4.75% | -0.390 | 0.537 | 0.745 | 0.00% |
| UTILITIES | XLU | rate_sensitive_defensive | -2.17% | -9.95% | -8.38% | 16.05% | -7.60% | -0.331 | 0.121 | 0.142 | -8.24% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | 1.12% | -4.67% | -1.88% | 15.85% | -4.19% | -0.385 | 0.251 | 0.275 | -1.48% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | 0.18% | -3.00% | -11.83% | 4.75% | -2.00% | -0.095 | 0.296 | 0.106 | -3.20% |
| LONG_TREASURY | TLT | rates_and_duration | 1.49% | -3.75% | -14.35% | 9.52% | -6.25% | 0.452 | 0.244 | 0.179 | -7.01% |
| TIPS | TIP | rates_and_duration | 0.45% | -2.82% | -9.69% | 3.53% | -1.40% | -0.207 | 0.276 | 0.072 | -0.93% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | 0.45% | -2.94% | -11.97% | 5.25% | -2.89% | -0.393 | 0.483 | 0.200 | -2.74% |
| HIGH_YIELD_CREDIT | HYG | credit | 0.11% | -2.24% | -8.44% | 3.07% | -0.80% | -0.676 | 0.782 | 0.234 | -0.11% |
| AGGREGATE_BONDS | AGG | rates_and_duration | 0.31% | -2.88% | -10.85% | 3.91% | -1.71% | -0.145 | 0.404 | 0.118 | -1.85% |
| DEVELOPED_EX_US | VEA | international_equity | -0.85% | 1.48% | -7.39% | 19.07% | -4.85% | -0.729 | 0.802 | 1.082 | -0.85% |
| EMERGING_MARKETS | VWO | international_equity | -0.70% | 0.43% | -9.19% | 19.28% | -7.05% | -0.699 | 0.811 | 1.109 | -2.07% |
| EUROPE | VGK | international_equity | 0.55% | 1.43% | -8.24% | 14.24% | -3.12% | -0.826 | 0.749 | 0.919 | -0.12% |
| JAPAN | EWJ | international_equity | -3.39% | 0.66% | -8.53% | 23.81% | -7.86% | -0.930 | 0.720 | 1.179 | -3.69% |
| CHINA | MCHI | international_equity | -0.24% | -0.32% | -20.51% | 18.88% | -11.15% | -0.533 | 0.543 | 0.857 | -16.45% |
| INDIA | INDA | international_equity | -0.46% | -0.55% | -17.59% | 12.90% | -4.59% | -0.893 | 0.552 | 0.645 | -10.74% |
| GOLD | IAU | precious_metals | 5.25% | 11.42% | -31.53% | 26.08% | -12.50% | -0.414 | 0.310 | 0.690 | -13.88% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | 1.43% | -0.42% | 13.16% | 22.06% | -13.30% | -0.326 | -0.176 | -0.276 | -2.33% |
| SEMICONDUCTORS | SMH | technology_and_growth | -7.96% | -5.89% | 27.06% | 53.71% | -24.62% | -0.264 | 0.779 | 2.366 | -18.26% |
| SOFTWARE | IGV | technology_and_growth | 0.45% | 13.13% | 5.51% | 35.31% | -21.29% | -1.065 | 0.510 | 1.187 | -13.01% |
| BROAD_AI_TECH | AIQ | technology_and_growth | -2.66% | 4.13% | 10.61% | 39.55% | -20.19% | -0.559 | 0.847 | 1.909 | -11.18% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | -6.62% | 3.53% | -16.27% | 38.18% | -23.82% | -0.704 | 0.801 | 2.188 | -15.29% |
| CYBERSECURITY | CIBR | technology_and_growth | -4.66% | 2.14% | 35.79% | 33.06% | -11.74% | -0.216 | 0.540 | 1.120 | -8.78% |
| SOLAR | TAN | clean_energy | -5.11% | -9.09% | -23.52% | 44.53% | -35.51% | 0.096 | 0.632 | 1.896 | -34.64% |
| METALS_MINING | XME | materials_and_mining | -0.19% | 12.53% | -22.32% | 41.97% | -26.49% | 0.053 | 0.597 | 1.759 | -11.20% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | 0.52% | 0.59% | -2.20% | 10.99% | -2.04% | -0.803 | 0.775 | 0.705 | -0.38% |
| BIOTECH | XBI | healthcare_and_biotech | 2.91% | 5.78% | 9.77% | 31.46% | -10.51% | -0.306 | 0.473 | 1.024 | -3.17% |
| REGIONAL_BANKS | KRE | financials | -3.40% | -4.60% | 2.58% | 18.95% | -4.13% | -0.770 | 0.428 | 0.751 | -4.07% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | -7.09% | -6.13% | -9.19% | 25.51% | -8.58% | -0.440 | 0.567 | 1.019 | -7.83% |
| CANADA | EWC | international_equity | -0.10% | 1.84% | -4.65% | 11.63% | -3.20% | -0.340 | 0.674 | 0.746 | -0.38% |
| UNITED_KINGDOM | EWU | international_equity | 1.95% | 0.64% | -8.82% | 12.72% | -3.40% | -0.511 | 0.605 | 0.702 | 0.00% |
| AUSTRALIA | EWA | international_equity | 1.73% | 1.34% | -9.96% | 16.57% | -4.78% | -0.735 | 0.674 | 0.929 | -1.15% |
| SOUTH_KOREA | EWY | international_equity | -6.19% | 3.23% | 8.12% | 80.27% | -34.21% | 0.027 | 0.636 | 2.753 | -20.78% |
| TAIWAN | EWT | international_equity | -4.15% | 2.11% | 25.07% | 42.85% | -19.83% | -0.729 | 0.760 | 1.843 | -7.35% |
| BRAZIL | EWZ | international_equity | 3.53% | -4.89% | -15.82% | 21.27% | -8.05% | -0.629 | 0.505 | 0.981 | -14.92% |
| MEXICO | EWW | international_equity | 2.99% | -1.07% | -12.62% | 19.33% | -6.47% | -0.311 | 0.545 | 0.935 | -3.63% |
| SOUTH_AFRICA | EZA | international_equity | 4.60% | 13.48% | -28.80% | 31.72% | -11.60% | -0.769 | 0.619 | 1.595 | -10.74% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | 0.28% | -2.74% | -10.73% | 4.56% | -1.85% | 0.078 | 0.399 | 0.138 | -1.65% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | -0.14% | -3.18% | -10.28% | 3.05% | -2.15% | 0.636 | 0.388 | 0.091 | -1.74% |
| EMERGING_MARKET_BONDS | EMB | credit | 0.16% | -2.66% | -9.88% | 5.42% | -1.96% | -0.682 | 0.687 | 0.307 | -1.20% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | 0.06% | -3.32% | -10.34% | 3.47% | -1.45% | -0.537 | 0.470 | 0.130 | -1.74% |
| SILVER | SLV | precious_metals | 4.41% | 14.95% | -43.59% | 44.32% | -27.73% | -0.675 | 0.353 | 1.698 | -41.10% |
| COPPER | CPER | non_energy_commodities | -0.15% | 1.16% | -1.38% | 25.15% | -10.57% | -0.486 | 0.547 | 1.197 | -1.91% |
| AGRICULTURE | DBA | non_energy_commodities | 0.57% | -3.11% | -0.12% | 12.89% | -4.86% | -0.572 | 0.082 | 0.071 | -1.50% |
| OIL | USO | energy | 1.47% | -6.60% | 60.10% | 52.53% | -26.72% | -0.610 | -0.338 | -1.260 | -13.57% |
| US_DOLLAR | UUP | currencies | -0.50% | -5.49% | -3.36% | 5.14% | -2.52% | -0.525 | -0.307 | -0.137 | -2.24% |
| EURO | FXE | currencies | 0.73% | -0.67% | -12.12% | 4.91% | -2.66% | -0.693 | 0.287 | 0.128 | -2.67% |
| YEN | FXY | currencies | 0.19% | -0.47% | -14.53% | 7.91% | -2.95% | 1.432 | 0.185 | 0.118 | -8.25% |
| BITCOIN_ETF | IBIT | crypto_assets | 22.57% | 19.49% | -9.41% | 41.41% | -22.56% | -0.065 | 0.479 | 1.687 | -37.38% |
| ETHEREUM_ETF | ETHA | crypto_assets | 29.58% | 29.58% | -8.93% | 59.16% | -24.84% | 0.193 | 0.506 | 2.638 | -49.00% |
