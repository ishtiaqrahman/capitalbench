# Full-Universe Horizon-Specific Decision Context

Profile: monthly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: yahoo_chart_adjusted_close_and_reported_volume
- As-of date requested: 2026-07-31
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | 1.10% |
| spy_return_21s | 0.17% |
| rsp_return_5s | 0.67% |
| rsp_return_21s | 0.75% |
| hyg_return_5s | 0.32% |
| hyg_return_21s | -0.14% |
| tlt_return_5s | -1.20% |
| tlt_return_21s | -3.82% |
| uup_return_5s | -1.43% |
| uup_return_21s | -1.12% |
| uso_return_5s | -5.50% |
| uso_return_21s | 25.08% |
| iau_return_5s | -0.08% |
| iau_return_21s | 0.28% |
| rsp_minus_spy_5s | -0.42% |
| rsp_minus_spy_21s | 0.58% |
| positive_asset_share_5s | 56.52% |
| positive_asset_share_21s | 46.38% |
| active_return_dispersion_5s |  |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_5s | active_return_21s | prior_105s_active_return | volatility_63s | max_drawdown_63s | volume_zscore_20v120 | corr_spy_252s | beta_spy_252s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | -0.17% | -8.02% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.08% | 0.14% | -6.53% | 0.21% | -0.01% | -0.382 | -0.106 | -0.002 | 0.00% |
| SP500 | SPY | diversified_us_equity | 1.10% | 0.00% | 0.00% | 13.64% | -4.49% | -0.933 | 1.000 | 1.000 | -1.40% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | 0.93% | -0.46% | 0.51% | 13.49% | -4.36% | -0.813 | 0.995 | 1.011 | -1.36% |
| NASDAQ100 | QQQ | technology_and_growth | 0.55% | -5.30% | 7.46% | 25.51% | -11.22% | -0.836 | 0.931 | 1.400 | -7.69% |
| LARGE_GROWTH | IWF | technology_and_growth | 0.57% | -3.99% | -3.02% | 20.07% | -11.35% | -0.792 | 0.936 | 1.270 | -8.03% |
| LARGE_VALUE | IWD | diversified_us_equity | 1.44% | 3.09% | 3.48% | 11.74% | -2.40% | -0.664 | 0.806 | 0.710 | -0.09% |
| MID_CAP | IJH | diversified_us_equity | -0.66% | -1.70% | 2.81% | 14.46% | -4.25% | -0.980 | 0.801 | 0.979 | -2.39% |
| SMALL_CAP | IWM | diversified_us_equity | 0.01% | -2.88% | 6.10% | 18.22% | -4.81% | -1.133 | 0.814 | 1.225 | -3.08% |
| SMALL_VALUE | IWN | diversified_us_equity | -0.08% | -0.38% | 5.90% | 14.96% | -4.01% | -0.688 | 0.730 | 0.983 | -1.31% |
| DIVIDEND | SCHD | diversified_us_equity | 0.54% | 4.92% | 2.21% | 11.83% | -2.95% | -0.113 | 0.294 | 0.254 | -1.24% |
| LOW_VOL | SPLV | diversified_us_equity | -1.24% | 1.33% | -4.05% | 13.37% | -4.09% | -0.856 | 0.030 | 0.025 | -2.23% |
| MOMENTUM | MTUM | diversified_us_equity | -2.22% | -8.86% | 17.88% | 38.95% | -17.99% | 1.417 | 0.775 | 1.535 | -13.22% |
| TECHNOLOGY | XLK | technology_and_growth | -0.30% | -5.70% | 18.67% | 35.12% | -15.86% | -1.000 | 0.859 | 1.704 | -11.43% |
| COMMUNICATIONS | XLC | technology_and_growth | 1.83% | -1.54% | -15.88% | 18.09% | -9.99% | -0.163 | 0.586 | 0.672 | -9.34% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | 6.11% | -1.86% | -10.19% | 21.80% | -10.72% | -0.324 | 0.786 | 1.191 | -6.40% |
| CONSUMER_STAPLES | XLP | consumer_defensive | 1.09% | 1.93% | -5.32% | 17.22% | -4.95% | -0.779 | -0.068 | -0.074 | -4.32% |
| HEALTHCARE | XLV | healthcare_and_biotech | -0.01% | 1.72% | -3.42% | 18.37% | -3.74% | -0.643 | 0.236 | 0.291 | -2.82% |
| FINANCIALS | XLF | financials | 1.12% | 3.77% | -4.84% | 13.66% | -2.42% | -0.754 | 0.559 | 0.640 | -1.15% |
| INDUSTRIALS | XLI | industrials_and_defense | -1.54% | -2.09% | 3.11% | 19.38% | -4.80% | -1.075 | 0.717 | 0.941 | -3.08% |
| ENERGY | XLE | energy | -0.12% | 12.59% | -2.03% | 24.22% | -13.21% | -0.881 | -0.130 | -0.212 | -4.12% |
| MATERIALS | XLB | materials_and_mining | -1.62% | -1.33% | -5.15% | 20.56% | -6.43% | -0.564 | 0.533 | 0.733 | -5.18% |
| UTILITIES | XLU | rate_sensitive_defensive | -4.19% | -1.11% | -3.31% | 16.45% | -8.00% | -0.883 | 0.136 | 0.158 | -5.83% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | -1.92% | 1.84% | 0.43% | 15.98% | -3.38% | -0.851 | 0.238 | 0.262 | -2.04% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | -0.09% | -1.32% | -8.15% | 5.00% | -2.00% | -0.989 | 0.229 | 0.083 | -3.60% |
| LONG_TREASURY | TLT | rates_and_duration | -1.20% | -3.99% | -8.21% | 9.43% | -5.60% | -0.659 | 0.193 | 0.139 | -7.74% |
| TIPS | TIP | rates_and_duration | 0.12% | -0.67% | -7.54% | 3.50% | -1.53% | -0.679 | 0.241 | 0.064 | -1.31% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | 0.02% | -2.21% | -7.81% | 5.31% | -2.83% | -0.364 | 0.432 | 0.177 | -3.10% |
| HIGH_YIELD_CREDIT | HYG | credit | 0.32% | -0.31% | -6.85% | 3.59% | -1.01% | -0.702 | 0.771 | 0.230 | -0.49% |
| AGGREGATE_BONDS | AGG | rates_and_duration | -0.09% | -1.32% | -7.70% | 4.13% | -1.71% | -0.433 | 0.338 | 0.099 | -2.37% |
| DEVELOPED_EX_US | VEA | international_equity | 1.31% | 0.20% | -2.39% | 20.96% | -4.85% | -0.762 | 0.801 | 1.071 | -2.45% |
| EMERGING_MARKETS | VWO | international_equity | 1.64% | -0.96% | -5.16% | 20.67% | -7.05% | -0.587 | 0.805 | 1.097 | -4.07% |
| EUROPE | VGK | international_equity | 2.47% | 3.04% | -6.82% | 17.83% | -3.86% | -0.914 | 0.746 | 0.920 | -0.44% |
| JAPAN | EWJ | international_equity | 1.29% | -0.88% | 0.65% | 23.51% | -7.86% | -0.831 | 0.714 | 1.160 | -4.72% |
| CHINA | MCHI | international_equity | 4.63% | 8.12% | -27.26% | 20.90% | -15.01% | -0.475 | 0.559 | 0.895 | -15.13% |
| INDIA | INDA | international_equity | 3.71% | 1.03% | -12.67% | 15.91% | -5.64% | -0.487 | 0.521 | 0.610 | -9.93% |
| GOLD | IAU | precious_metals | -0.08% | 0.11% | -33.24% | 23.96% | -16.01% | -0.606 | 0.305 | 0.661 | -25.01% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | -2.17% | 11.11% | -2.96% | 22.27% | -16.55% | -0.013 | -0.135 | -0.205 | -7.14% |
| SEMICONDUCTORS | SMH | technology_and_growth | -3.68% | -13.05% | 40.58% | 55.17% | -24.62% | 0.933 | 0.783 | 2.341 | -19.19% |
| SOFTWARE | IGV | technology_and_growth | 7.50% | 1.16% | -6.84% | 33.49% | -21.29% | -0.835 | 0.503 | 1.138 | -19.69% |
| BROAD_AI_TECH | AIQ | technology_and_growth | 1.57% | -7.62% | 11.97% | 40.21% | -20.19% | -0.105 | 0.845 | 1.872 | -16.04% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | 0.93% | -11.95% | -5.96% | 38.37% | -23.82% | -0.941 | 0.798 | 2.146 | -19.99% |
| CYBERSECURITY | CIBR | technology_and_growth | 3.88% | 0.62% | 23.30% | 32.35% | -11.74% | -0.257 | 0.534 | 1.076 | -3.06% |
| SOLAR | TAN | clean_energy | -3.80% | -14.82% | -4.35% | 45.93% | -35.51% | -0.687 | 0.591 | 1.797 | -33.27% |
| METALS_MINING | XME | materials_and_mining | -1.07% | -3.73% | -25.59% | 40.34% | -26.49% | -0.538 | 0.595 | 1.701 | -24.17% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | 0.67% | 0.58% | 0.36% | 10.86% | -2.04% | -0.846 | 0.767 | 0.699 | -1.23% |
| BIOTECH | XBI | healthcare_and_biotech | -2.31% | -6.26% | 15.62% | 30.91% | -10.51% | -0.240 | 0.474 | 0.991 | -10.51% |
| REGIONAL_BANKS | KRE | financials | 0.44% | -0.33% | 3.62% | 19.82% | -5.29% | -0.685 | 0.443 | 0.787 | -2.39% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | -0.20% | -1.89% | -3.12% | 25.49% | -8.58% | -0.404 | 0.564 | 0.983 | -4.43% |
| CANADA | EWC | international_equity | 0.54% | 2.81% | -5.53% | 12.02% | -3.20% | -0.752 | 0.679 | 0.756 | -0.75% |
| UNITED_KINGDOM | EWU | international_equity | 2.50% | 5.21% | -7.68% | 16.37% | -3.94% | -0.544 | 0.609 | 0.706 | -0.55% |
| AUSTRALIA | EWA | international_equity | 2.16% | 5.75% | -9.19% | 18.30% | -6.84% | -0.918 | 0.672 | 0.916 | -1.68% |
| SOUTH_KOREA | EWY | international_equity | -3.60% | -15.48% | 40.97% | 82.65% | -34.21% | 0.598 | 0.640 | 2.695 | -28.33% |
| TAIWAN | EWT | international_equity | -1.49% | -8.82% | 43.33% | 44.26% | -19.83% | 0.148 | 0.745 | 1.779 | -13.43% |
| BRAZIL | EWZ | international_equity | 2.57% | 7.06% | -17.51% | 23.61% | -15.56% | -1.040 | 0.519 | 1.011 | -11.34% |
| MEXICO | EWW | international_equity | 1.80% | 1.88% | -10.66% | 20.60% | -7.30% | -0.886 | 0.540 | 0.923 | -4.05% |
| SOUTH_AFRICA | EZA | international_equity | 4.18% | 1.25% | -27.47% | 32.52% | -14.17% | -0.533 | 0.624 | 1.574 | -20.33% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | -0.20% | -1.34% | -7.78% | 4.91% | -1.93% | -0.427 | 0.333 | 0.115 | -2.42% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | 0.09% | -1.75% | -6.76% | 3.07% | -2.15% | 0.480 | 0.326 | 0.075 | -1.79% |
| EMERGING_MARKET_BONDS | EMB | credit | 0.02% | -1.59% | -6.08% | 5.84% | -2.10% | -0.670 | 0.666 | 0.293 | -1.82% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | -0.06% | -1.21% | -7.48% | 4.17% | -1.44% | -0.557 | 0.422 | 0.116 | -1.80% |
| SILVER | SLV | precious_metals | -0.44% | -2.45% | -57.27% | 50.35% | -36.50% | -0.643 | 0.352 | 1.676 | -50.42% |
| COPPER | CPER | non_energy_commodities | 3.16% | 6.15% | -11.90% | 29.29% | -10.57% | -0.641 | 0.555 | 1.211 | -2.56% |
| AGRICULTURE | DBA | non_energy_commodities | -2.58% | 2.25% | -4.20% | 14.00% | -8.67% | -0.392 | 0.086 | 0.074 | -4.25% |
| OIL | USO | energy | -5.50% | 24.91% | 22.47% | 53.42% | -32.49% | -0.530 | -0.303 | -1.102 | -15.55% |
| US_DOLLAR | UUP | currencies | -1.43% | -1.29% | -0.88% | 5.05% | -1.61% | -0.193 | -0.282 | -0.129 | -1.50% |
| EURO | FXE | currencies | 1.47% | 1.30% | -12.67% | 4.86% | -3.57% | -0.826 | 0.262 | 0.121 | -3.79% |
| YEN | FXY | currencies | 2.89% | 2.01% | -14.02% | 6.78% | -4.58% | 0.687 | 0.140 | 0.090 | -8.21% |
| BITCOIN_ETF | IBIT | crypto_assets | -1.95% | 4.65% | -36.59% | 37.45% | -28.36% | -0.624 | 0.509 | 1.756 | -50.01% |
| ETHEREUM_ETF | ETHA | crypto_assets | 0.21% | 15.25% | -50.28% | 53.20% | -34.41% | -0.425 | 0.551 | 2.882 | -61.55% |
