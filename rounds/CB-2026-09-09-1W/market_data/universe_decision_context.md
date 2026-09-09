# Full-Universe Horizon-Specific Decision Context

Profile: weekly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: yahoo_chart_adjusted_close_and_reported_volume
- As-of date requested: 2026-09-08
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | -0.14% |
| spy_return_21s | -0.94% |
| rsp_return_5s | -1.21% |
| rsp_return_21s | -1.53% |
| hyg_return_5s | -0.32% |
| hyg_return_21s | -0.07% |
| tlt_return_5s | -0.01% |
| tlt_return_21s | -0.30% |
| uup_return_5s | -0.46% |
| uup_return_21s | -0.29% |
| uso_return_5s | 9.22% |
| uso_return_21s | 23.78% |
| iau_return_5s | -2.10% |
| iau_return_21s | 0.33% |
| rsp_minus_spy_5s | -1.07% |
| rsp_minus_spy_21s | -0.58% |
| positive_asset_share_5s | 46.38% |
| positive_asset_share_21s | 37.68% |
| active_return_dispersion_5s | 2.30% |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_3s | active_return_5s | prior_16s_active_return | volatility_21s | max_drawdown_21s | volume_zscore_5v60 | corr_spy_63s | beta_spy_63s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | 0.14% | 0.80% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.07% | 0.23% | 1.00% | 0.15% | 0.00% | 0.070 | -0.005 | -0.000 | 0.00% |
| SP500 | SPY | diversified_us_equity | 0.10% | 0.00% | 0.00% | 8.11% | -2.07% | -0.760 | 1.000 | 1.000 | -1.53% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | 0.19% | -0.00% | -0.15% | 8.44% | -2.38% | -0.367 | 0.992 | 0.979 | -1.74% |
| NASDAQ100 | QQQ | technology_and_growth | 1.29% | 0.37% | -0.06% | 12.53% | -3.52% | -0.827 | 0.912 | 1.680 | -3.62% |
| LARGE_GROWTH | IWF | technology_and_growth | 0.99% | 0.39% | -0.71% | 13.46% | -3.68% | -0.514 | 0.892 | 1.410 | -4.38% |
| LARGE_VALUE | IWD | diversified_us_equity | -0.60% | -0.40% | 0.55% | 8.36% | -1.48% | -0.535 | 0.662 | 0.552 | -1.48% |
| MID_CAP | IJH | diversified_us_equity | 0.33% | 0.16% | -2.33% | 10.68% | -5.17% | -0.680 | 0.776 | 0.807 | -4.21% |
| SMALL_CAP | IWM | diversified_us_equity | 0.22% | 0.39% | -1.73% | 11.90% | -4.76% | -0.531 | 0.753 | 0.861 | -3.42% |
| SMALL_VALUE | IWN | diversified_us_equity | -0.13% | 0.57% | -0.85% | 9.74% | -3.29% | 0.125 | 0.608 | 0.557 | -2.05% |
| DIVIDEND | SCHD | diversified_us_equity | -1.71% | -1.23% | 3.72% | 10.53% | -2.27% | 0.650 | 0.075 | 0.069 | -2.27% |
| LOW_VOL | SPLV | diversified_us_equity | -0.15% | -0.05% | -1.01% | 8.61% | -2.20% | -0.335 | -0.194 | -0.182 | -4.21% |
| MOMENTUM | MTUM | diversified_us_equity | 3.92% | 2.92% | -2.09% | 20.59% | -7.93% | -0.994 | 0.661 | 1.829 | -10.58% |
| TECHNOLOGY | XLK | technology_and_growth | 2.33% | 0.88% | 0.02% | 20.43% | -5.62% | -0.708 | 0.807 | 1.993 | -5.10% |
| COMMUNICATIONS | XLC | technology_and_growth | -0.80% | 0.20% | 0.99% | 16.56% | -2.19% | -0.735 | 0.388 | 0.596 | -6.59% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | -0.76% | -2.09% | -1.93% | 16.07% | -4.90% | -0.657 | 0.682 | 1.138 | -8.09% |
| CONSUMER_STAPLES | XLP | consumer_defensive | -1.77% | -0.99% | 0.64% | 14.64% | -3.92% | -0.184 | -0.213 | -0.282 | -5.48% |
| HEALTHCARE | XLV | healthcare_and_biotech | -3.37% | -1.86% | 3.74% | 20.80% | -4.87% | -0.668 | -0.099 | -0.151 | -4.87% |
| FINANCIALS | XLF | financials | -0.62% | -0.57% | 0.99% | 12.76% | -2.25% | -0.063 | 0.359 | 0.364 | -2.15% |
| INDUSTRIALS | XLI | industrials_and_defense | 0.95% | -0.26% | -4.62% | 11.99% | -7.39% | 0.548 | 0.663 | 0.961 | -6.48% |
| ENERGY | XLE | energy | -0.51% | 1.41% | 12.04% | 21.14% | -2.65% | -0.314 | -0.443 | -0.768 | -0.51% |
| MATERIALS | XLB | materials_and_mining | -1.91% | -1.28% | 0.48% | 14.72% | -3.22% | 0.656 | 0.392 | 0.587 | -3.22% |
| UTILITIES | XLU | rate_sensitive_defensive | 1.83% | 3.03% | -2.36% | 14.05% | -4.69% | 1.021 | -0.076 | -0.085 | -7.75% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | 0.39% | -0.33% | -1.13% | 12.10% | -3.59% | 0.222 | -0.124 | -0.144 | -4.59% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | -0.02% | -0.13% | 0.34% | 4.49% | -1.15% | -0.208 | 0.399 | 0.147 | -3.74% |
| LONG_TREASURY | TLT | rates_and_duration | 0.31% | 0.14% | 0.51% | 10.13% | -1.70% | -0.713 | 0.302 | 0.225 | -7.07% |
| TIPS | TIP | rates_and_duration | 0.18% | 0.36% | 0.56% | 3.51% | -0.77% | -0.487 | 0.310 | 0.084 | -1.12% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | 0.12% | -0.13% | 0.48% | 5.56% | -1.12% | -0.875 | 0.476 | 0.195 | -2.98% |
| HIGH_YIELD_CREDIT | HYG | credit | 0.01% | -0.18% | 1.05% | 2.48% | -0.48% | -0.015 | 0.775 | 0.173 | -0.46% |
| AGGREGATE_BONDS | AGG | rates_and_duration | 0.06% | -0.04% | 0.61% | 3.96% | -0.92% | -0.068 | 0.434 | 0.133 | -2.17% |
| DEVELOPED_EX_US | VEA | international_equity | 1.18% | 0.87% | 0.84% | 11.46% | -2.28% | -0.167 | 0.773 | 1.042 | -0.46% |
| EMERGING_MARKETS | VWO | international_equity | 0.76% | 1.32% | 0.89% | 9.14% | -1.37% | -0.491 | 0.811 | 1.062 | -0.34% |
| EUROPE | VGK | international_equity | 0.25% | -0.37% | -0.21% | 7.96% | -2.65% | -0.465 | 0.716 | 0.748 | -2.15% |
| JAPAN | EWJ | international_equity | 2.00% | 2.31% | -0.25% | 15.79% | -4.27% | -0.569 | 0.735 | 1.295 | -0.52% |
| CHINA | MCHI | international_equity | -1.08% | -1.27% | -2.47% | 14.43% | -5.23% | -0.760 | 0.359 | 0.467 | -17.94% |
| INDIA | INDA | international_equity | -1.76% | -1.09% | -0.53% | 10.48% | -2.54% | -0.225 | 0.536 | 0.536 | -11.21% |
| GOLD | IAU | precious_metals | -0.73% | -1.96% | 3.29% | 27.07% | -7.30% | -0.428 | 0.447 | 0.931 | -19.32% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | 1.26% | 3.63% | 8.92% | 18.38% | -2.57% | -0.079 | -0.297 | -0.500 | 0.00% |
| SEMICONDUCTORS | SMH | technology_and_growth | 4.22% | 3.21% | -3.67% | 30.77% | -8.22% | -0.691 | 0.715 | 2.727 | -14.23% |
| SOFTWARE | IGV | technology_and_growth | -0.73% | -6.51% | 7.90% | 40.33% | -6.94% | -0.442 | 0.467 | 1.222 | -12.83% |
| BROAD_AI_TECH | AIQ | technology_and_growth | 1.97% | 0.17% | 2.30% | 18.58% | -3.59% | -0.746 | 0.817 | 2.171 | -8.30% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | 3.17% | 1.41% | -3.38% | 22.34% | -7.91% | -0.473 | 0.835 | 2.249 | -13.75% |
| CYBERSECURITY | CIBR | technology_and_growth | 0.50% | -5.99% | 3.15% | 40.56% | -9.53% | 0.224 | 0.528 | 1.304 | -8.01% |
| SOLAR | TAN | clean_energy | 3.93% | 3.42% | -9.02% | 24.01% | -11.17% | -0.728 | 0.725 | 2.186 | -33.55% |
| METALS_MINING | XME | materials_and_mining | 0.41% | 1.68% | 2.87% | 34.33% | -5.88% | -0.888 | 0.571 | 1.670 | -9.63% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | -0.86% | -1.07% | 0.49% | 9.31% | -2.71% | -0.801 | 0.668 | 0.574 | -2.71% |
| BIOTECH | XBI | healthcare_and_biotech | -2.08% | -0.21% | 4.06% | 31.90% | -4.49% | -0.775 | 0.266 | 0.613 | -4.49% |
| REGIONAL_BANKS | KRE | financials | 0.09% | 1.16% | -2.67% | 15.64% | -6.81% | -0.220 | 0.199 | 0.269 | -4.65% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | 0.07% | -1.97% | -8.13% | 18.96% | -11.79% | -0.101 | 0.450 | 0.844 | -11.72% |
| CANADA | EWC | international_equity | 0.36% | 0.24% | 1.02% | 12.81% | -3.26% | 0.487 | 0.552 | 0.486 | -1.84% |
| UNITED_KINGDOM | EWU | international_equity | 0.27% | 0.10% | 0.25% | 8.00% | -2.43% | 0.094 | 0.373 | 0.362 | -2.11% |
| AUSTRALIA | EWA | international_equity | -0.10% | 0.08% | -0.48% | 12.82% | -2.83% | 0.530 | 0.532 | 0.639 | -1.41% |
| SOUTH_KOREA | EWY | international_equity | 6.18% | 5.15% | 9.70% | 46.83% | -8.13% | -0.910 | 0.620 | 3.401 | -13.36% |
| TAIWAN | EWT | international_equity | 1.93% | 3.39% | 5.60% | 21.12% | -4.15% | -0.911 | 0.741 | 2.211 | -0.57% |
| BRAZIL | EWZ | international_equity | 1.37% | 7.30% | 2.76% | 25.04% | -4.64% | 2.058 | 0.282 | 0.483 | -6.60% |
| MEXICO | EWW | international_equity | 0.59% | 0.08% | -0.23% | 14.62% | -3.95% | -0.504 | 0.558 | 0.778 | -4.22% |
| SOUTH_AFRICA | EZA | international_equity | 1.87% | 1.28% | 2.02% | 26.77% | -4.10% | 0.037 | 0.651 | 1.461 | -10.71% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | 0.02% | -0.11% | 0.62% | 4.35% | -1.09% | -0.045 | 0.456 | 0.164 | -2.12% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | -0.19% | -0.61% | 0.01% | 2.79% | -1.76% | 3.016 | 0.492 | 0.114 | -2.77% |
| EMERGING_MARKET_BONDS | EMB | credit | 0.22% | 0.15% | 0.31% | 4.67% | -0.92% | 0.880 | 0.699 | 0.281 | -1.27% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | 0.30% | 0.06% | -0.03% | 3.68% | -1.21% | 0.369 | 0.501 | 0.140 | -2.08% |
| SILVER | SLV | precious_metals | 0.51% | -1.12% | 5.38% | 37.80% | -7.73% | -0.723 | 0.499 | 1.643 | -43.78% |
| COPPER | CPER | non_energy_commodities | 2.63% | 1.57% | 1.05% | 18.44% | -4.15% | 0.066 | 0.558 | 0.995 | -0.69% |
| AGRICULTURE | DBA | non_energy_commodities | -0.48% | -0.51% | 6.96% | 11.83% | -2.17% | 1.298 | 0.034 | 0.035 | -1.22% |
| OIL | USO | energy | 3.46% | 9.36% | 14.13% | 39.32% | -6.31% | -0.225 | -0.404 | -1.639 | -4.53% |
| US_DOLLAR | UUP | currencies | -0.64% | -0.32% | 0.98% | 5.23% | -1.13% | -0.459 | -0.335 | -0.137 | -2.13% |
| EURO | FXE | currencies | 0.31% | 0.20% | 1.34% | 4.43% | -0.76% | -0.240 | 0.313 | 0.115 | -2.97% |
| YEN | FXY | currencies | 3.17% | 3.92% | -0.66% | 11.10% | -1.79% | 0.170 | 0.275 | 0.204 | -5.19% |
| BITCOIN_ETF | IBIT | crypto_assets | 1.37% | -0.48% | 22.19% | 46.25% | -4.23% | 0.166 | 0.355 | 1.054 | -37.73% |
| ETHEREUM_ETF | ETHA | crypto_assets | 3.71% | 0.14% | 30.17% | 57.33% | -4.35% | 0.003 | 0.347 | 1.391 | -47.69% |
