# Full-Universe Horizon-Specific Decision Context

Profile: monthly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: tiingo_eod_adjusted_price_and_volume
- As-of date requested: 2026-09-14
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | -1.21% |
| spy_return_21s | -2.19% |
| rsp_return_5s | -1.82% |
| rsp_return_21s | -3.47% |
| hyg_return_5s | -0.80% |
| hyg_return_21s | -1.04% |
| tlt_return_5s | -1.56% |
| tlt_return_21s | -1.63% |
| uup_return_5s | 0.32% |
| uup_return_21s | -0.04% |
| uso_return_5s | 10.36% |
| uso_return_21s | 25.30% |
| iau_return_5s | -3.42% |
| iau_return_21s | -1.52% |
| rsp_minus_spy_5s | -0.61% |
| rsp_minus_spy_21s | -1.28% |
| positive_asset_share_5s | 15.94% |
| positive_asset_share_21s | 20.29% |
| active_return_dispersion_5s |  |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_5s | active_return_21s | prior_105s_active_return | volatility_63s | max_drawdown_63s | volume_zscore_20v120 | corr_spy_252s | beta_spy_252s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | 2.19% | -18.08% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.05% | 2.48% | -16.60% | 0.20% | -0.01% | -0.439 | -0.086 | -0.001 | 0.00% |
| SP500 | SPY | diversified_us_equity | -1.21% | 0.00% | 0.00% | 12.21% | -3.38% | -0.970 | 1.000 | 1.000 | -2.19% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | -1.33% | -0.32% | 0.47% | 12.03% | -3.29% | -0.620 | 0.995 | 1.012 | -2.50% |
| NASDAQ100 | QQQ | technology_and_growth | -1.36% | -0.94% | 5.51% | 22.47% | -10.96% | -0.992 | 0.929 | 1.422 | -4.85% |
| LARGE_GROWTH | IWF | technology_and_growth | -1.74% | -1.32% | -3.20% | 19.94% | -8.29% | -0.697 | 0.934 | 1.289 | -5.75% |
| LARGE_VALUE | IWD | diversified_us_equity | -0.88% | 0.90% | 3.23% | 9.83% | -2.33% | -0.520 | 0.802 | 0.700 | -1.55% |
| MID_CAP | IJH | diversified_us_equity | -2.72% | -3.72% | -0.30% | 12.43% | -6.20% | -0.643 | 0.812 | 0.977 | -6.20% |
| SMALL_CAP | IWM | diversified_us_equity | -2.74% | -2.95% | 5.51% | 13.69% | -5.70% | -0.902 | 0.820 | 1.198 | -5.63% |
| SMALL_VALUE | IWN | diversified_us_equity | -2.30% | -1.04% | 4.18% | 10.90% | -3.72% | -0.907 | 0.736 | 0.937 | -3.51% |
| DIVIDEND | SCHD | diversified_us_equity | -1.32% | 1.92% | -4.46% | 11.87% | -3.46% | 0.231 | 0.286 | 0.248 | -2.47% |
| LOW_VOL | SPLV | diversified_us_equity | -1.23% | -0.80% | -15.22% | 11.64% | -5.34% | -0.638 | 0.017 | 0.014 | -5.15% |
| MOMENTUM | MTUM | diversified_us_equity | -1.69% | -2.98% | 11.99% | 34.51% | -17.99% | -0.485 | 0.764 | 1.569 | -13.19% |
| TECHNOLOGY | XLK | technology_and_growth | -1.60% | -1.22% | 21.71% | 30.77% | -13.31% | -1.205 | 0.852 | 1.748 | -6.92% |
| COMMUNICATIONS | XLC | technology_and_growth | 2.71% | 4.42% | -19.17% | 20.28% | -7.06% | -0.977 | 0.555 | 0.663 | -3.61% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | -1.79% | -2.54% | -10.81% | 20.75% | -8.09% | -1.020 | 0.768 | 1.158 | -9.01% |
| CONSUMER_STAPLES | XLP | consumer_defensive | -0.19% | 0.35% | -15.31% | 16.87% | -5.03% | -0.689 | -0.063 | -0.071 | -5.03% |
| HEALTHCARE | XLV | healthcare_and_biotech | -2.16% | 1.81% | -4.71% | 19.42% | -5.87% | -0.851 | 0.221 | 0.279 | -4.51% |
| FINANCIALS | XLF | financials | -1.84% | 0.07% | 2.11% | 12.80% | -2.89% | -0.668 | 0.540 | 0.612 | -2.61% |
| INDUSTRIALS | XLI | industrials_and_defense | -3.05% | -6.35% | -4.65% | 16.63% | -8.89% | -0.605 | 0.713 | 0.958 | -8.89% |
| ENERGY | XLE | energy | 0.73% | 7.87% | -10.81% | 21.63% | -7.58% | -0.695 | -0.181 | -0.305 | -1.19% |
| MATERIALS | XLB | materials_and_mining | -3.72% | -1.29% | -10.87% | 17.25% | -5.93% | -0.387 | 0.535 | 0.743 | -5.93% |
| UTILITIES | XLU | rate_sensitive_defensive | -2.92% | -2.86% | -23.05% | 14.49% | -9.66% | -0.299 | 0.118 | 0.140 | -11.21% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | -1.84% | -2.25% | -9.64% | 14.65% | -6.43% | -0.403 | 0.248 | 0.271 | -6.28% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | -1.43% | -0.00% | -18.83% | 4.76% | -3.35% | -0.295 | 0.286 | 0.103 | -5.03% |
| LONG_TREASURY | TLT | rates_and_duration | -1.56% | 0.55% | -20.78% | 9.45% | -6.55% | 0.040 | 0.238 | 0.169 | -8.50% |
| TIPS | TIP | rates_and_duration | -1.08% | 0.93% | -17.98% | 3.61% | -2.06% | -0.294 | 0.250 | 0.065 | -2.25% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | -1.12% | 0.49% | -17.63% | 5.21% | -3.77% | -0.479 | 0.473 | 0.193 | -4.06% |
| HIGH_YIELD_CREDIT | HYG | credit | -0.80% | 1.15% | -14.82% | 2.78% | -1.20% | -0.483 | 0.773 | 0.229 | -1.20% |
| AGGREGATE_BONDS | AGG | rates_and_duration | -1.14% | 0.68% | -17.93% | 3.96% | -2.50% | -0.260 | 0.395 | 0.115 | -3.18% |
| DEVELOPED_EX_US | VEA | international_equity | -2.77% | -0.29% | -2.04% | 16.17% | -4.75% | -0.658 | 0.802 | 1.090 | -2.81% |
| EMERGING_MARKETS | VWO | international_equity | -2.98% | 0.98% | -6.25% | 16.53% | -7.05% | -0.795 | 0.814 | 1.115 | -2.98% |
| EUROPE | VGK | international_equity | -2.74% | -1.22% | -3.56% | 12.08% | -4.25% | -0.823 | 0.749 | 0.917 | -4.25% |
| JAPAN | EWJ | international_equity | -0.71% | 1.28% | 0.68% | 21.98% | -7.86% | -0.736 | 0.727 | 1.190 | -0.99% |
| CHINA | MCHI | international_equity | -2.90% | 0.16% | -23.27% | 16.89% | -8.10% | -0.875 | 0.560 | 0.858 | -18.90% |
| INDIA | INDA | international_equity | -2.97% | -0.92% | -14.08% | 12.92% | -4.79% | -0.869 | 0.562 | 0.666 | -12.41% |
| GOLD | IAU | precious_metals | -3.42% | 0.67% | -31.43% | 25.08% | -8.23% | -0.280 | 0.334 | 0.756 | -20.70% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | 4.05% | 13.50% | -14.34% | 22.00% | -7.50% | -0.472 | -0.185 | -0.294 | -1.35% |
| SEMICONDUCTORS | SMH | technology_and_growth | -4.50% | -5.90% | 34.02% | 47.79% | -24.62% | -0.785 | 0.771 | 2.385 | -19.05% |
| SOFTWARE | IGV | technology_and_growth | 1.98% | 2.52% | 8.18% | 34.43% | -8.55% | -1.101 | 0.496 | 1.229 | -9.45% |
| BROAD_AI_TECH | AIQ | technology_and_growth | -1.32% | 0.41% | 15.57% | 32.73% | -16.56% | -0.816 | 0.849 | 1.926 | -9.51% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | -2.17% | -5.89% | -7.14% | 32.70% | -18.66% | -1.192 | 0.804 | 2.201 | -16.84% |
| CYBERSECURITY | CIBR | technology_and_growth | 5.77% | 0.08% | 39.20% | 33.10% | -9.53% | 0.046 | 0.505 | 1.134 | -2.10% |
| SOLAR | TAN | clean_energy | -3.79% | -9.73% | -23.33% | 36.34% | -26.67% | -0.688 | 0.640 | 1.900 | -37.48% |
| METALS_MINING | XME | materials_and_mining | -7.12% | -2.24% | -12.22% | 36.50% | -19.05% | -0.435 | 0.596 | 1.786 | -17.00% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | -1.82% | -1.28% | -2.05% | 10.47% | -4.31% | -1.014 | 0.774 | 0.701 | -3.48% |
| BIOTECH | XBI | healthcare_and_biotech | -3.79% | 2.66% | 10.80% | 29.09% | -10.51% | -0.288 | 0.481 | 1.045 | -7.05% |
| REGIONAL_BANKS | KRE | financials | -1.54% | -2.50% | 6.54% | 17.09% | -6.81% | -0.524 | 0.414 | 0.715 | -4.90% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | -3.92% | -11.00% | -9.06% | 21.55% | -14.39% | -0.324 | 0.573 | 1.037 | -14.39% |
| CANADA | EWC | international_equity | -2.48% | -0.39% | -4.70% | 11.40% | -3.75% | -0.164 | 0.677 | 0.764 | -3.42% |
| UNITED_KINGDOM | EWU | international_equity | -1.40% | 1.46% | -10.08% | 11.73% | -3.77% | -0.630 | 0.603 | 0.701 | -3.00% |
| AUSTRALIA | EWA | international_equity | -3.87% | -0.10% | -10.28% | 15.19% | -4.50% | -0.236 | 0.675 | 0.938 | -4.50% |
| SOUTH_KOREA | EWY | international_equity | -6.70% | 0.84% | 25.80% | 68.71% | -34.21% | -0.761 | 0.632 | 2.790 | -19.61% |
| TAIWAN | EWT | international_equity | -4.43% | 1.92% | 35.51% | 38.14% | -19.83% | -1.079 | 0.752 | 1.847 | -4.43% |
| BRAZIL | EWZ | international_equity | -0.37% | 13.88% | -22.02% | 21.88% | -8.05% | -0.154 | 0.478 | 0.941 | -8.75% |
| MEXICO | EWW | international_equity | -2.36% | 1.35% | -11.06% | 16.25% | -5.37% | -0.619 | 0.549 | 0.937 | -6.54% |
| SOUTH_AFRICA | EZA | international_equity | -4.40% | 3.91% | -14.84% | 27.47% | -11.18% | -0.504 | 0.633 | 1.631 | -14.29% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | -1.61% | 0.12% | -17.79% | 4.71% | -2.89% | 0.358 | 0.392 | 0.135 | -3.50% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | -0.88% | -0.42% | -17.76% | 3.50% | -3.98% | 2.846 | 0.391 | 0.092 | -3.62% |
| EMERGING_MARKET_BONDS | EMB | credit | -1.32% | 0.37% | -14.81% | 4.95% | -2.47% | -0.362 | 0.686 | 0.303 | -2.47% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | -1.10% | 0.39% | -17.08% | 3.58% | -2.57% | -0.242 | 0.469 | 0.133 | -3.04% |
| SILVER | SLV | precious_metals | -4.98% | -0.08% | -38.07% | 41.77% | -20.61% | -0.591 | 0.368 | 1.794 | -46.17% |
| COPPER | CPER | non_energy_commodities | -4.23% | -1.80% | -3.63% | 24.11% | -8.42% | -0.204 | 0.556 | 1.251 | -6.80% |
| AGRICULTURE | DBA | non_energy_commodities | 0.38% | 7.04% | -14.83% | 13.46% | -2.87% | 0.349 | 0.045 | 0.039 | -1.80% |
| OIL | USO | energy | 10.36% | 27.48% | -13.79% | 52.21% | -17.67% | -0.604 | -0.347 | -1.317 | -1.09% |
| US_DOLLAR | UUP | currencies | 0.32% | 2.15% | -17.04% | 5.27% | -2.52% | -1.096 | -0.295 | -0.129 | -1.50% |
| EURO | FXE | currencies | -0.56% | 2.41% | -16.79% | 4.81% | -2.19% | -0.614 | 0.276 | 0.118 | -3.58% |
| YEN | FXY | currencies | 1.30% | 5.49% | -18.10% | 9.66% | -2.22% | 0.307 | 0.178 | 0.118 | -5.40% |
| BITCOIN_ETF | IBIT | crypto_assets | -1.08% | 26.88% | -29.20% | 37.96% | -11.79% | 0.902 | 0.485 | 1.710 | -37.24% |
| ETHEREUM_ETF | ETHA | crypto_assets | 3.51% | 36.90% | -28.53% | 51.17% | -14.68% | 1.681 | 0.504 | 2.539 | -46.44% |
