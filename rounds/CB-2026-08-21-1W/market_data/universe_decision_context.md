# Full-Universe Horizon-Specific Decision Context

Profile: weekly. All values stop at the requested close and are sorted by frozen option order, not performance.

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
| active_return_dispersion_5s | 4.38% |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_3s | active_return_5s | prior_16s_active_return | volatility_21s | max_drawdown_21s | volume_zscore_5v60 | corr_spy_63s | beta_spy_63s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | 1.96% | -4.08% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.02% | 2.03% | -3.85% | 0.17% | 0.00% | -0.814 | -0.124 | -0.002 | 0.00% |
| SP500 | SPY | diversified_us_equity | -1.30% | 0.00% | 0.00% | 13.71% | -2.40% | -0.915 | 1.000 | 1.000 | -1.96% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | -1.45% | -0.04% | 0.11% | 13.81% | -2.29% | -0.240 | 0.993 | 0.988 | -2.01% |
| NASDAQ100 | QQQ | technology_and_growth | -2.59% | -0.92% | -0.29% | 23.49% | -6.18% | -0.679 | 0.920 | 1.725 | -4.62% |
| LARGE_GROWTH | IWF | technology_and_growth | -2.61% | -1.09% | -0.16% | 21.67% | -5.68% | -0.772 | 0.904 | 1.380 | -5.31% |
| LARGE_VALUE | IWD | diversified_us_equity | -0.18% | 0.99% | 0.44% | 9.83% | -1.00% | -0.309 | 0.706 | 0.580 | -1.00% |
| MID_CAP | IJH | diversified_us_equity | -2.69% | -0.65% | -0.47% | 13.65% | -2.92% | -0.510 | 0.792 | 0.797 | -2.92% |
| SMALL_CAP | IWM | diversified_us_equity | -2.10% | 0.04% | -0.77% | 15.34% | -2.43% | -1.152 | 0.782 | 0.968 | -2.43% |
| SMALL_VALUE | IWN | diversified_us_equity | -1.17% | 0.66% | -1.95% | 11.43% | -1.59% | -1.318 | 0.652 | 0.646 | -1.59% |
| DIVIDEND | SCHD | diversified_us_equity | 1.57% | 3.13% | 0.57% | 11.95% | -1.42% | 0.402 | 0.107 | 0.096 | -0.74% |
| LOW_VOL | SPLV | diversified_us_equity | -0.11% | 1.22% | -4.04% | 9.13% | -2.98% | -0.633 | -0.284 | -0.266 | -2.96% |
| MOMENTUM | MTUM | diversified_us_equity | -5.27% | -1.49% | -3.51% | 34.97% | -9.91% | -0.469 | 0.702 | 1.977 | -11.62% |
| TECHNOLOGY | XLK | technology_and_growth | -3.79% | -2.06% | 1.75% | 32.81% | -7.60% | -1.155 | 0.832 | 2.131 | -7.51% |
| COMMUNICATIONS | XLC | technology_and_growth | -0.13% | 0.30% | -1.01% | 24.51% | -3.50% | -1.344 | 0.401 | 0.571 | -7.29% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | -0.06% | 0.47% | -0.19% | 25.74% | -4.61% | -0.902 | 0.668 | 1.063 | -5.92% |
| CONSUMER_STAPLES | XLP | consumer_defensive | 0.76% | 1.17% | -2.16% | 17.13% | -3.07% | -0.415 | -0.290 | -0.370 | -4.02% |
| HEALTHCARE | XLV | healthcare_and_biotech | 3.20% | 4.35% | 1.54% | 20.14% | -3.09% | -0.436 | -0.138 | -0.199 | -1.87% |
| FINANCIALS | XLF | financials | -1.09% | -0.28% | -0.13% | 11.72% | -2.25% | -0.153 | 0.288 | 0.274 | -2.25% |
| INDUSTRIALS | XLI | industrials_and_defense | -3.52% | -1.28% | -0.20% | 18.62% | -3.61% | -0.862 | 0.657 | 0.887 | -3.61% |
| ENERGY | XLE | energy | 1.87% | 6.37% | -0.93% | 24.53% | -3.87% | -0.925 | -0.322 | -0.551 | 0.00% |
| MATERIALS | XLB | materials_and_mining | 0.34% | 2.17% | -1.14% | 19.22% | -3.65% | -0.933 | 0.429 | 0.598 | -1.54% |
| UTILITIES | XLU | rate_sensitive_defensive | -0.93% | 1.35% | -8.19% | 11.05% | -6.83% | -0.656 | -0.103 | -0.116 | -7.07% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | 0.56% | 1.88% | -3.83% | 14.07% | -4.19% | 0.349 | -0.165 | -0.191 | -2.02% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | 0.17% | 1.64% | -3.52% | 4.86% | -0.65% | -0.238 | 0.468 | 0.161 | -3.22% |
| LONG_TREASURY | TLT | rates_and_duration | 1.22% | 1.66% | -4.70% | 11.74% | -3.04% | 0.710 | 0.347 | 0.241 | -7.26% |
| TIPS | TIP | rates_and_duration | 0.70% | 2.30% | -3.91% | 2.89% | -0.36% | 0.314 | 0.431 | 0.108 | -0.68% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | 0.34% | 1.50% | -3.76% | 5.98% | -0.99% | 0.386 | 0.542 | 0.208 | -2.85% |
| HIGH_YIELD_CREDIT | HYG | credit | -0.06% | 1.68% | -3.25% | 3.01% | -0.36% | -0.254 | 0.823 | 0.184 | -0.29% |
| AGGREGATE_BONDS | AGG | rates_and_duration | 0.25% | 1.76% | -3.62% | 4.23% | -0.56% | -0.491 | 0.513 | 0.146 | -1.91% |
| DEVELOPED_EX_US | VEA | international_equity | -1.15% | 1.01% | 0.25% | 16.26% | -2.18% | -0.449 | 0.803 | 1.116 | -1.15% |
| EMERGING_MARKETS | VWO | international_equity | -0.61% | 1.43% | -1.48% | 14.76% | -3.21% | -0.837 | 0.841 | 1.178 | -1.99% |
| EUROPE | VGK | international_equity | -0.10% | 1.56% | -0.38% | 12.05% | -1.41% | -0.348 | 0.731 | 0.759 | -0.64% |
| JAPAN | EWJ | international_equity | -3.97% | -2.30% | 2.74% | 23.89% | -4.27% | -0.603 | 0.751 | 1.301 | -4.27% |
| CHINA | MCHI | international_equity | 0.82% | 3.97% | -2.49% | 14.37% | -4.41% | -0.697 | 0.398 | 0.548 | -15.57% |
| INDIA | INDA | international_equity | -0.06% | 1.10% | -0.43% | 11.23% | -2.28% | -1.313 | 0.589 | 0.555 | -10.38% |
| GOLD | IAU | precious_metals | 2.43% | 6.06% | 1.19% | 25.86% | -2.56% | -0.069 | 0.475 | 0.893 | -16.19% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | 1.87% | 6.35% | -4.30% | 25.77% | -6.42% | -0.475 | -0.187 | -0.301 | -1.90% |
| SEMICONDUCTORS | SMH | technology_and_growth | -5.29% | -2.53% | -3.70% | 45.78% | -14.09% | -0.632 | 0.750 | 2.932 | -15.89% |
| SOFTWARE | IGV | technology_and_growth | -0.08% | -2.15% | 15.31% | 32.49% | -4.11% | -1.167 | 0.471 | 1.214 | -13.47% |
| BROAD_AI_TECH | AIQ | technology_and_growth | -1.52% | -0.50% | 3.37% | 31.75% | -6.92% | -0.818 | 0.826 | 2.376 | -10.14% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | -5.20% | -2.97% | 5.12% | 36.99% | -8.04% | -1.262 | 0.860 | 2.376 | -14.00% |
| CYBERSECURITY | CIBR | technology_and_growth | -4.44% | -6.60% | 10.33% | 29.15% | -8.56% | -0.064 | 0.552 | 1.332 | -8.56% |
| SOLAR | TAN | clean_energy | -2.34% | -3.26% | -6.40% | 41.59% | -11.24% | -0.841 | 0.758 | 2.497 | -32.73% |
| METALS_MINING | XME | materials_and_mining | -2.88% | 1.47% | 7.30% | 41.83% | -5.72% | -0.045 | 0.651 | 1.965 | -13.59% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | -0.23% | 0.86% | 0.64% | 11.29% | -1.34% | -1.238 | 0.701 | 0.566 | -1.12% |
| BIOTECH | XBI | healthcare_and_biotech | 2.41% | 6.12% | -0.95% | 32.33% | -3.64% | 0.288 | 0.301 | 0.689 | -3.64% |
| REGIONAL_BANKS | KRE | financials | -3.46% | -1.95% | -1.23% | 15.05% | -4.13% | 0.076 | 0.166 | 0.229 | -4.13% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | -5.43% | -2.89% | 3.96% | 27.35% | -6.18% | -0.928 | 0.438 | 0.810 | -6.18% |
| CANADA | EWC | international_equity | -0.66% | 1.43% | 0.68% | 9.90% | -1.04% | 1.071 | 0.590 | 0.495 | -0.74% |
| UNITED_KINGDOM | EWU | international_equity | 0.79% | 2.54% | -1.92% | 10.05% | -1.14% | -0.641 | 0.395 | 0.366 | -0.29% |
| AUSTRALIA | EWA | international_equity | 0.68% | 2.00% | -1.03% | 17.50% | -2.83% | -0.538 | 0.581 | 0.697 | -2.17% |
| SOUTH_KOREA | EWY | international_equity | -3.75% | 1.71% | 0.73% | 73.99% | -17.05% | -0.338 | 0.667 | 3.916 | -18.72% |
| TAIWAN | EWT | international_equity | -3.46% | -1.23% | 1.65% | 39.25% | -12.07% | -1.330 | 0.778 | 2.460 | -6.69% |
| BRAZIL | EWZ | international_equity | 0.50% | 3.06% | -11.86% | 20.20% | -8.05% | -0.298 | 0.381 | 0.579 | -17.41% |
| MEXICO | EWW | international_equity | 0.79% | 2.03% | -5.72% | 16.40% | -3.95% | -0.064 | 0.581 | 0.794 | -5.69% |
| SOUTH_AFRICA | EZA | international_equity | 3.34% | 6.63% | 2.83% | 32.19% | -4.05% | -0.787 | 0.665 | 1.515 | -11.75% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | 0.27% | 1.76% | -3.34% | 5.13% | -0.80% | 0.665 | 0.516 | 0.172 | -1.66% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | -0.09% | 1.31% | -3.54% | 3.76% | -0.74% | 0.741 | 0.543 | 0.121 | -1.69% |
| EMERGING_MARKET_BONDS | EMB | credit | -0.03% | 1.24% | -3.35% | 5.96% | -0.76% | -0.685 | 0.739 | 0.293 | -1.38% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | 0.00% | 1.42% | -3.60% | 3.79% | -0.83% | -0.080 | 0.510 | 0.130 | -1.80% |
| SILVER | SLV | precious_metals | 3.51% | 7.98% | 3.79% | 38.63% | -4.12% | -0.275 | 0.549 | 1.773 | -41.61% |
| COPPER | CPER | non_energy_commodities | -1.94% | 0.71% | -2.55% | 20.24% | -4.09% | 0.029 | 0.632 | 1.153 | -3.67% |
| AGRICULTURE | DBA | non_energy_commodities | 0.85% | 4.72% | -6.24% | 13.81% | -2.87% | -0.078 | 0.136 | 0.130 | -1.22% |
| OIL | USO | energy | 3.26% | 9.57% | -9.13% | 63.69% | -17.64% | -0.807 | -0.328 | -1.255 | -12.04% |
| US_DOLLAR | UUP | currencies | -0.68% | 1.01% | -5.03% | 5.85% | -2.52% | -1.456 | -0.385 | -0.144 | -2.41% |
| EURO | FXE | currencies | 0.88% | 3.28% | -2.98% | 4.98% | -0.36% | -0.319 | 0.401 | 0.144 | -2.53% |
| YEN | FXY | currencies | 0.23% | 2.19% | -1.76% | 12.35% | -1.74% | -0.053 | 0.253 | 0.146 | -8.21% |
| BITCOIN_ETF | IBIT | crypto_assets | 13.12% | 16.79% | -7.99% | 36.07% | -4.58% | 1.453 | 0.330 | 0.953 | -42.21% |
| ETHEREUM_ETF | ETHA | crypto_assets | 21.87% | 25.30% | -6.07% | 56.55% | -4.35% | 2.439 | 0.407 | 1.753 | -52.04% |
