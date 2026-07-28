# Full-Universe Horizon-Specific Decision Context

Profile: weekly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: yahoo_chart_adjusted_close_and_reported_volume; yahoo_chart_history_with_tiingo_eod_frozen_entry_close
- As-of date requested: 2026-07-27
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | -0.40% |
| spy_return_21s | 0.65% |
| rsp_return_5s | 1.30% |
| rsp_return_21s | 1.62% |
| hyg_return_5s | -0.51% |
| hyg_return_21s | -0.30% |
| tlt_return_5s | -0.17% |
| tlt_return_21s | -3.77% |
| uup_return_5s | 0.74% |
| uup_return_21s | 0.42% |
| uso_return_5s | -0.60% |
| uso_return_21s | 14.13% |
| iau_return_5s | 1.90% |
| iau_return_21s | 1.41% |
| rsp_minus_spy_5s | 1.70% |
| rsp_minus_spy_21s | 0.97% |
| positive_asset_share_5s | 53.62% |
| positive_asset_share_21s | 50.72% |
| active_return_dispersion_5s | 1.76% |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_3s | active_return_5s | prior_16s_active_return | volatility_21s | max_drawdown_21s | volume_zscore_5v60 | corr_spy_63s | beta_spy_63s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | 0.40% | -1.06% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.04% | 0.47% | -0.81% | 0.24% | -0.01% | -0.801 | -0.186 | -0.003 | 0.00% |
| SP500 | SPY | diversified_us_equity | -1.11% | 0.00% | 0.00% | 11.37% | -2.22% | -0.804 | 1.000 | 1.000 | -2.45% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | -1.00% | 0.11% | -0.15% | 10.43% | -2.15% | -0.929 | 0.992 | 0.990 | -2.17% |
| NASDAQ100 | QQQ | technology_and_growth | -3.29% | -1.60% | -3.90% | 23.07% | -7.37% | -0.446 | 0.915 | 1.720 | -8.48% |
| LARGE_GROWTH | IWF | technology_and_growth | -3.13% | -1.55% | 0.10% | 21.79% | -5.67% | -0.658 | 0.884 | 1.274 | -8.96% |
| LARGE_VALUE | IWD | diversified_us_equity | 0.90% | 1.53% | -0.02% | 9.13% | -1.31% | -0.349 | 0.718 | 0.659 | 0.00% |
| MID_CAP | IJH | diversified_us_equity | 0.41% | 1.83% | -3.06% | 10.89% | -3.09% | -0.960 | 0.786 | 0.882 | -1.44% |
| SMALL_CAP | IWM | diversified_us_equity | -0.30% | 0.61% | -3.27% | 11.10% | -3.09% | -0.851 | 0.779 | 1.104 | -2.51% |
| SMALL_VALUE | IWN | diversified_us_equity | 0.05% | 1.00% | -0.72% | 10.11% | -1.83% | -0.541 | 0.680 | 0.805 | -0.90% |
| DIVIDEND | SCHD | diversified_us_equity | 1.61% | 2.48% | 1.41% | 13.29% | -1.18% | -0.244 | 0.136 | 0.125 | 0.00% |
| LOW_VOL | SPLV | diversified_us_equity | 1.34% | 1.89% | 0.72% | 14.64% | -1.89% | -0.966 | -0.287 | -0.288 | 0.00% |
| MOMENTUM | MTUM | diversified_us_equity | -3.79% | 0.30% | -11.87% | 38.12% | -11.88% | -0.206 | 0.743 | 2.098 | -12.42% |
| TECHNOLOGY | XLK | technology_and_growth | -3.31% | -0.40% | -5.86% | 29.99% | -8.51% | -1.224 | 0.833 | 2.116 | -11.96% |
| COMMUNICATIONS | XLC | technology_and_growth | -1.41% | -2.43% | 3.88% | 21.35% | -7.06% | 0.220 | 0.485 | 0.625 | -9.82% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | -2.79% | -2.89% | 0.05% | 23.18% | -7.90% | 0.081 | 0.730 | 1.163 | -10.63% |
| CONSUMER_STAPLES | XLP | consumer_defensive | 1.16% | 0.99% | 0.04% | 19.42% | -3.03% | -0.958 | -0.273 | -0.352 | -3.97% |
| HEALTHCARE | XLV | healthcare_and_biotech | 2.49% | 3.01% | 1.27% | 21.32% | -3.74% | -1.360 | -0.117 | -0.161 | -0.63% |
| FINANCIALS | XLF | financials | 1.48% | 1.90% | 3.78% | 13.77% | -2.08% | -1.019 | 0.196 | 0.197 | 0.00% |
| INDUSTRIALS | XLI | industrials_and_defense | 2.43% | 3.26% | -4.32% | 14.30% | -4.01% | -1.077 | 0.636 | 0.931 | -1.27% |
| ENERGY | XLE | energy | -1.42% | 1.13% | 6.06% | 20.07% | -2.37% | -0.534 | -0.371 | -0.699 | -6.04% |
| MATERIALS | XLB | materials_and_mining | 1.12% | 3.12% | -4.55% | 18.21% | -3.81% | -0.353 | 0.534 | 0.815 | -3.37% |
| UTILITIES | XLU | rate_sensitive_defensive | -0.54% | 2.05% | -3.05% | 16.67% | -3.10% | -0.869 | -0.069 | -0.091 | -3.01% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | 1.67% | 1.58% | 0.37% | 17.16% | -2.67% | -0.616 | -0.081 | -0.101 | -0.41% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | 0.19% | 0.13% | -2.05% | 4.15% | -2.00% | -1.051 | 0.514 | 0.198 | -3.26% |
| LONG_TREASURY | TLT | rates_and_duration | 0.37% | 0.24% | -4.67% | 7.16% | -4.54% | -0.749 | 0.386 | 0.264 | -6.05% |
| TIPS | TIP | rates_and_duration | -0.35% | -0.21% | -1.42% | 2.93% | -1.33% | -0.305 | 0.547 | 0.148 | -1.53% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | -0.15% | -0.19% | -2.86% | 4.56% | -2.82% | 0.164 | 0.555 | 0.226 | -2.86% |
| HIGH_YIELD_CREDIT | HYG | credit | -0.31% | -0.11% | -0.85% | 2.49% | -0.80% | 0.095 | 0.768 | 0.215 | -0.75% |
| AGGREGATE_BONDS | AGG | rates_and_duration | 0.11% | 0.14% | -2.04% | 3.41% | -1.71% | -0.457 | 0.553 | 0.175 | -2.05% |
| DEVELOPED_EX_US | VEA | international_equity | -0.70% | 1.52% | -3.77% | 15.66% | -3.70% | -1.070 | 0.837 | 1.331 | -3.30% |
| EMERGING_MARKETS | VWO | international_equity | -0.99% | 0.92% | -2.54% | 17.23% | -3.78% | -0.909 | 0.866 | 1.343 | -4.92% |
| EUROPE | VGK | international_equity | -0.28% | 1.72% | -1.22% | 14.14% | -2.53% | -0.415 | 0.727 | 1.009 | -1.26% |
| JAPAN | EWJ | international_equity | -0.74% | 1.60% | -4.23% | 20.36% | -5.08% | -0.891 | 0.796 | 1.355 | -5.63% |
| CHINA | MCHI | international_equity | 1.29% | 0.74% | 5.44% | 19.48% | -2.22% | -0.945 | 0.487 | 0.787 | -17.47% |
| INDIA | INDA | international_equity | 1.39% | 1.10% | -2.84% | 13.61% | -4.51% | 0.360 | 0.565 | 0.686 | -11.58% |
| GOLD | IAU | precious_metals | -1.17% | 2.30% | -1.54% | 20.86% | -4.47% | -0.648 | 0.682 | 1.260 | -24.41% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | -2.64% | 0.17% | 6.82% | 22.58% | -3.99% | -0.324 | -0.117 | -0.197 | -8.30% |
| SEMICONDUCTORS | SMH | technology_and_growth | -6.54% | -1.44% | -13.32% | 49.31% | -16.37% | 1.153 | 0.779 | 3.158 | -17.99% |
| SOFTWARE | IGV | technology_and_growth | 2.12% | -1.82% | 8.64% | 29.11% | -8.11% | -0.412 | 0.325 | 0.837 | -22.81% |
| BROAD_AI_TECH | AIQ | technology_and_growth | -3.06% | -1.02% | -8.91% | 33.68% | -11.63% | -0.835 | 0.818 | 2.455 | -16.88% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | -3.58% | -1.10% | -6.88% | 33.63% | -13.77% | -0.856 | 0.846 | 2.517 | -20.13% |
| CYBERSECURITY | CIBR | technology_and_growth | -0.26% | -2.53% | 8.66% | 28.59% | -7.40% | -0.257 | 0.431 | 1.072 | -5.94% |
| SOLAR | TAN | clean_energy | -4.02% | -1.74% | -10.01% | 36.46% | -13.31% | -0.768 | 0.748 | 2.590 | -30.26% |
| METALS_MINING | XME | materials_and_mining | -0.38% | 5.90% | -11.18% | 30.01% | -10.12% | -0.298 | 0.677 | 2.086 | -22.32% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | 1.17% | 1.70% | -0.74% | 9.95% | -1.46% | -1.277 | 0.721 | 0.606 | 0.00% |
| BIOTECH | XBI | healthcare_and_biotech | -1.00% | 0.17% | -1.49% | 27.74% | -8.40% | -0.619 | 0.359 | 0.841 | -8.33% |
| REGIONAL_BANKS | KRE | financials | -0.11% | -0.08% | 0.44% | 19.34% | -3.73% | -0.563 | 0.198 | 0.310 | -3.08% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | 5.54% | 6.79% | -4.48% | 22.23% | -8.58% | -0.395 | 0.451 | 0.869 | -2.74% |
| CANADA | EWC | international_equity | 0.19% | 1.72% | 0.67% | 8.95% | -1.46% |  | 0.604 | 0.612 | -0.17% |
| UNITED_KINGDOM | EWU | international_equity | 0.28% | 2.52% | 0.05% | 14.55% | -1.93% | -0.668 | 0.483 | 0.631 | -1.30% |
| AUSTRALIA | EWA | international_equity | 0.07% | 1.67% | 1.05% | 12.70% | -1.63% | -0.886 | 0.620 | 0.878 | -3.22% |
| SOUTH_KOREA | EWY | international_equity | -5.42% | -0.62% | -21.62% | 65.33% | -21.37% | -0.278 | 0.712 | 4.288 | -26.46% |
| TAIWAN | EWT | international_equity | -3.81% | 2.35% | -9.61% | 39.78% | -11.67% | -0.766 | 0.787 | 2.503 | -12.30% |
| BRAZIL | EWZ | international_equity | -2.05% | 1.50% | 2.74% | 21.17% | -2.43% | -0.877 | 0.429 | 0.788 | -13.22% |
| MEXICO | EWW | international_equity | -0.22% | 2.34% | -1.64% | 16.52% | -2.98% | -0.523 | 0.622 | 0.991 | -4.39% |
| SOUTH_AFRICA | EZA | international_equity | -1.65% | 0.91% | -3.50% | 23.05% | -6.50% | 0.587 | 0.771 | 1.959 | -22.43% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | 0.24% | 0.19% | -2.13% | 4.11% | -1.85% | -0.383 | 0.558 | 0.208 | -1.95% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | -0.08% | -0.16% | -1.89% | 3.24% | -2.15% | 2.743 | 0.568 | 0.134 | -1.65% |
| EMERGING_MARKET_BONDS | EMB | credit | -0.14% | -0.03% | -1.88% | 4.43% | -1.96% | -0.548 | 0.733 | 0.326 | -1.51% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | 0.25% | 0.61% | -2.22% | 3.42% | -1.44% | -0.845 | 0.535 | 0.174 | -1.49% |
| SILVER | SLV | precious_metals | -1.84% | 4.23% | -3.70% | 36.42% | -10.19% | -0.951 | 0.649 | 2.519 | -49.88% |
| COPPER | CPER | non_energy_commodities | -1.22% | 1.32% | 2.83% | 21.01% | -3.26% | -0.605 | 0.720 | 1.623 | -4.51% |
| AGRICULTURE | DBA | non_energy_commodities | -2.16% | -1.02% | 3.03% | 16.39% | -2.20% | -0.895 | 0.031 | 0.033 | -3.86% |
| OIL | USO | energy | -5.26% | -0.19% | 13.76% | 58.63% | -10.56% | 0.244 | -0.298 | -1.241 | -18.44% |
| US_DOLLAR | UUP | currencies | 0.53% | 1.14% | -1.38% | 4.42% | -0.88% | -1.071 | -0.531 | -0.200 | 0.00% |
| EURO | FXE | currencies | -0.36% | 0.01% | -0.58% | 3.93% | -0.81% | -0.737 | 0.569 | 0.201 | -5.18% |
| YEN | FXY | currencies | -0.39% | -0.39% | -1.47% | 5.40% | -1.65% | 0.794 | 0.198 | 0.100 | -10.84% |
| BITCOIN_ETF | IBIT | crypto_assets | -1.53% | 0.08% | 8.99% | 30.95% | -3.50% | -0.620 | 0.465 | 1.326 | -48.42% |
| ETHEREUM_ETF | ETHA | crypto_assets | 1.31% | 3.06% | 21.00% | 46.14% | -4.20% | 0.393 | 0.560 | 2.294 | -59.80% |
