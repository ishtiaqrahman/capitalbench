# Full-Universe Horizon-Specific Decision Context

Profile: monthly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: yahoo_chart_adjusted_close_and_reported_volume
- As-of date requested: 2026-07-17
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | -1.54% |
| spy_return_21s | -0.68% |
| rsp_return_5s | -0.43% |
| rsp_return_21s | 0.96% |
| hyg_return_5s | -0.08% |
| hyg_return_21s | -0.01% |
| tlt_return_5s | 0.06% |
| tlt_return_21s | -1.58% |
| uup_return_5s | -0.21% |
| uup_return_21s | 1.43% |
| uso_return_5s | 14.04% |
| uso_return_21s | 7.35% |
| iau_return_5s | -2.28% |
| iau_return_21s | -7.36% |
| rsp_minus_spy_5s | 1.11% |
| rsp_minus_spy_21s | 1.64% |
| positive_asset_share_5s | 43.48% |
| positive_asset_share_21s | 37.68% |
| active_return_dispersion_5s |  |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_5s | active_return_21s | prior_105s_active_return | volatility_63s | max_drawdown_63s | volume_zscore_20v120 | corr_spy_252s | beta_spy_252s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | 0.68% | -8.98% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.05% | 1.01% | -7.51% | 0.21% | -0.01% | -0.042 | -0.117 | -0.002 | 0.00% |
| SP500 | SPY | diversified_us_equity | -1.54% | 0.00% | 0.00% | 13.13% | -4.49% | -0.772 | 1.000 | 1.000 | -1.89% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | -1.52% | 0.06% | -0.03% | 13.11% | -4.36% | -0.809 | 0.995 | 1.014 | -1.68% |
| NASDAQ100 | QQQ | technology_and_growth | -4.16% | -3.94% | 8.97% | 24.27% | -7.03% | -0.689 | 0.932 | 1.385 | -6.71% |
| LARGE_GROWTH | IWF | technology_and_growth | -3.69% | -2.54% | -3.85% | 18.86% | -8.21% | -0.649 | 0.936 | 1.256 | -7.21% |
| LARGE_VALUE | IWD | diversified_us_equity | 0.48% | 2.77% | 3.08% | 11.88% | -2.40% | -0.185 | 0.808 | 0.723 | -0.57% |
| MID_CAP | IJH | diversified_us_equity | -0.17% | 0.17% | 0.91% | 14.89% | -4.25% | -0.926 | 0.798 | 0.996 | -2.04% |
| SMALL_CAP | IWM | diversified_us_equity | -0.66% | 1.35% | 2.46% | 18.61% | -4.81% | -1.003 | 0.814 | 1.250 | -2.13% |
| SMALL_VALUE | IWN | diversified_us_equity | 1.08% | 3.52% | 3.34% | 15.77% | -4.01% | -0.456 | 0.731 | 1.015 | -0.82% |
| DIVIDEND | SCHD | diversified_us_equity | 1.57% | 2.66% | 3.98% | 11.92% | -2.95% | -0.315 | 0.315 | 0.276 | -0.39% |
| LOW_VOL | SPLV | diversified_us_equity | 0.96% | 3.66% | -5.81% | 13.40% | -4.16% | -0.707 | 0.047 | 0.039 | -0.48% |
| MOMENTUM | MTUM | diversified_us_equity | -6.12% | -6.67% | 18.77% | 35.70% | -12.49% | 1.605 | 0.789 | 1.505 | -12.49% |
| TECHNOLOGY | XLK | technology_and_growth | -5.48% | -5.02% | 20.02% | 33.07% | -11.31% | -0.747 | 0.863 | 1.680 | -11.31% |
| COMMUNICATIONS | XLC | technology_and_growth | -0.89% | -0.55% | -12.38% | 15.36% | -11.12% | 0.359 | 0.631 | 0.697 | -7.32% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | -1.54% | -1.67% | -11.89% | 19.02% | -7.02% | -0.287 | 0.795 | 1.178 | -6.92% |
| CONSUMER_STAPLES | XLP | consumer_defensive | 1.27% | 0.91% | -4.31% | 16.49% | -4.95% | -0.745 | -0.051 | -0.055 | -4.16% |
| HEALTHCARE | XLV | healthcare_and_biotech | 0.16% | 6.48% | -11.70% | 18.26% | -4.01% | -0.220 | 0.261 | 0.327 | -2.04% |
| FINANCIALS | XLF | financials | 0.99% | 4.56% | -8.10% | 13.17% | -3.34% | -0.678 | 0.560 | 0.650 | -0.86% |
| INDUSTRIALS | XLI | industrials_and_defense | -1.38% | 0.68% | 0.81% | 19.60% | -4.60% | -0.909 | 0.731 | 0.964 | -3.31% |
| ENERGY | XLE | energy | 4.72% | 5.63% | 6.96% | 24.79% | -13.21% | -0.821 | -0.123 | -0.204 | -7.14% |
| MATERIALS | XLB | materials_and_mining | -0.71% | -3.11% | -0.36% | 19.07% | -6.43% | -0.593 | 0.549 | 0.763 | -4.99% |
| UTILITIES | XLU | rate_sensitive_defensive | -0.53% | 1.57% | -3.88% | 17.61% | -8.00% | -0.486 | 0.135 | 0.160 | -4.09% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | 2.18% | 2.28% | 0.71% | 16.56% | -3.38% | -0.770 | 0.251 | 0.285 | -0.09% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | 0.22% | 0.29% | -9.44% | 5.07% | -2.62% | -0.765 | 0.211 | 0.078 | -2.68% |
| LONG_TREASURY | TLT | rates_and_duration | 0.06% | -0.89% | -9.56% | 8.89% | -4.30% | -0.731 | 0.168 | 0.125 | -5.19% |
| TIPS | TIP | rates_and_duration | 0.13% | 0.29% | -7.90% | 3.55% | -1.16% | -0.483 | 0.233 | 0.064 | -0.72% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | 0.09% | -0.40% | -8.83% | 5.34% | -2.27% | -0.332 | 0.417 | 0.174 | -1.90% |
| HIGH_YIELD_CREDIT | HYG | credit | -0.08% | 0.67% | -7.73% | 3.69% | -1.10% | -0.682 | 0.768 | 0.232 | -0.28% |
| AGGREGATE_BONDS | AGG | rates_and_duration | 0.12% | 0.24% | -8.72% | 4.16% | -1.90% | -0.194 | 0.322 | 0.097 | -1.54% |
| DEVELOPED_EX_US | VEA | international_equity | -1.82% | -2.43% | 2.69% | 21.03% | -4.85% | -0.598 | 0.796 | 1.075 | -3.72% |
| EMERGING_MARKETS | VWO | international_equity | -3.42% | -3.06% | -1.71% | 20.72% | -5.67% | -0.360 | 0.799 | 1.095 | -5.55% |
| EUROPE | VGK | international_equity | 0.02% | 0.45% | -3.98% | 18.35% | -4.41% | -1.014 | 0.738 | 0.928 | -1.53% |
| JAPAN | EWJ | international_equity | -4.29% | -3.17% | 2.30% | 22.14% | -6.68% | -0.653 | 0.706 | 1.169 | -6.68% |
| CHINA | MCHI | international_equity | -0.34% | -1.50% | -23.24% | 20.92% | -15.01% | -0.086 | 0.580 | 0.942 | -19.46% |
| INDIA | INDA | international_equity | -0.79% | -0.33% | -16.19% | 16.34% | -7.94% | -0.697 | 0.511 | 0.606 | -11.54% |
| GOLD | IAU | precious_metals | -2.28% | -6.68% | -15.55% | 24.10% | -18.11% | -0.542 | 0.297 | 0.654 | -25.67% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | 4.93% | 4.16% | 11.12% | 21.83% | -16.55% | 0.142 | -0.119 | -0.180 | -8.78% |
| SEMICONDUCTORS | SMH | technology_and_growth | -8.92% | -8.97% | 49.64% | 52.32% | -16.80% | 0.864 | 0.783 | 2.296 | -16.80% |
| SOFTWARE | IGV | technology_and_growth | 0.42% | 2.25% | -18.56% | 34.48% | -21.29% | -0.427 | 0.516 | 1.172 | -21.20% |
| BROAD_AI_TECH | AIQ | technology_and_growth | -7.47% | -8.51% | 14.66% | 39.03% | -16.31% | 0.862 | 0.850 | 1.866 | -16.31% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | -6.33% | -11.56% | -8.74% | 38.00% | -19.25% | -0.951 | 0.790 | 2.157 | -19.25% |
| CYBERSECURITY | CIBR | technology_and_growth | 0.52% | 9.33% | 8.70% | 32.46% | -11.74% | -0.028 | 0.534 | 1.091 | -2.50% |
| SOLAR | TAN | clean_energy | -1.93% | -10.34% | 8.67% | 45.38% | -28.15% | -0.721 | 0.580 | 1.775 | -27.09% |
| METALS_MINING | XME | materials_and_mining | -5.15% | -16.84% | -11.88% | 40.31% | -25.91% | -0.488 | 0.587 | 1.694 | -25.91% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | -0.43% | 1.64% | -1.74% | 11.01% | -2.04% | -0.681 | 0.777 | 0.725 | -0.79% |
| BIOTECH | XBI | healthcare_and_biotech | -3.00% | 14.77% | -2.27% | 30.26% | -8.57% | 0.427 | 0.477 | 1.005 | -6.10% |
| REGIONAL_BANKS | KRE | financials | 2.23% | 7.10% | -0.13% | 21.06% | -5.29% | -0.482 | 0.446 | 0.813 | -1.58% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | -3.48% | -2.99% | -8.70% | 25.81% | -8.11% | -0.412 | 0.581 | 1.018 | -8.00% |
| CANADA | EWC | international_equity | 1.36% | 1.26% | -1.36% | 13.16% | -3.20% | -0.750 | 0.678 | 0.764 | -0.07% |
| UNITED_KINGDOM | EWU | international_equity | 0.73% | 1.61% | -4.80% | 17.09% | -5.55% | -0.485 | 0.607 | 0.714 | -2.19% |
| AUSTRALIA | EWA | international_equity | 1.05% | -0.11% | 1.74% | 18.48% | -7.12% | -0.799 | 0.672 | 0.919 | -3.65% |
| SOUTH_KOREA | EWY | international_equity | -11.43% | -20.38% | 78.82% | 77.68% | -25.85% | 0.447 | 0.648 | 2.650 | -25.85% |
| TAIWAN | EWT | international_equity | -8.34% | -5.54% | 47.07% | 41.46% | -12.73% | 0.147 | 0.747 | 1.723 | -12.73% |
| BRAZIL | EWZ | international_equity | -1.95% | 3.07% | -4.23% | 22.93% | -18.76% | -0.997 | 0.508 | 1.009 | -14.77% |
| MEXICO | EWW | international_equity | 0.33% | -3.00% | -1.15% | 20.51% | -7.30% | -0.661 | 0.527 | 0.918 | -6.17% |
| SOUTH_AFRICA | EZA | international_equity | -2.29% | -7.66% | -14.24% | 33.64% | -15.34% | -0.523 | 0.618 | 1.576 | -21.90% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | 0.06% | 0.07% | -8.42% | 4.85% | -2.24% | -0.532 | 0.318 | 0.111 | -1.52% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | -0.40% | 0.40% | -8.21% | 2.74% | -1.36% | -0.448 | 0.313 | 0.072 | -0.92% |
| EMERGING_MARKET_BONDS | EMB | credit | -0.48% | -0.08% | -6.45% | 5.96% | -2.10% | -0.641 | 0.658 | 0.292 | -0.92% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | -0.31% | 0.08% | -8.42% | 4.35% | -1.34% | -0.399 | 0.404 | 0.113 | -1.47% |
| SILVER | SLV | precious_metals | -5.88% | -19.21% | -34.02% | 51.05% | -36.50% | -0.676 | 0.347 | 1.681 | -51.91% |
| COPPER | CPER | non_energy_commodities | -0.18% | -3.44% | -3.52% | 28.92% | -10.57% | -0.627 | 0.456 | 1.231 | -6.60% |
| AGRICULTURE | DBA | non_energy_commodities | 0.25% | 5.11% | -4.48% | 13.56% | -8.67% | -0.087 | 0.075 | 0.064 | -3.10% |
| OIL | USO | energy | 14.04% | 8.04% | 50.04% | 54.26% | -32.49% | -0.582 | -0.291 | -1.037 | -18.96% |
| US_DOLLAR | UUP | currencies | -0.21% | 2.12% | -6.79% | 4.93% | -0.98% | -0.058 | -0.273 | -0.130 | -0.70% |
| EURO | FXE | currencies | 0.29% | -0.66% | -8.97% | 4.72% | -3.58% | -0.733 | 0.255 | 0.125 | -4.58% |
| YEN | FXY | currencies | -0.41% | -0.51% | -10.35% | 6.55% | -3.85% | -0.203 | 0.107 | 0.068 | -10.09% |
| BITCOIN_ETF | IBIT | crypto_assets | 0.33% | -1.52% | -41.94% | 38.63% | -28.36% | -0.299 | 0.511 | 1.791 | -49.01% |
| ETHEREUM_ETF | ETHA | crypto_assets | 2.81% | 3.42% | -56.07% | 53.66% | -36.13% | -0.438 | 0.548 | 2.944 | -61.98% |
