# Full-Universe Horizon-Specific Decision Context

Profile: weekly. All values stop at the requested close and are sorted by frozen option order, not performance.

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
| active_return_dispersion_5s | 3.98% |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_3s | active_return_5s | prior_16s_active_return | volatility_21s | max_drawdown_21s | volume_zscore_5v60 | corr_spy_63s | beta_spy_63s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | 2.40% | -0.87% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.03% | 2.47% | -0.64% | 0.23% | -0.01% | -0.654 | -0.176 | -0.003 | 0.00% |
| SP500 | SPY | diversified_us_equity | -1.28% | 0.00% | 0.00% | 10.86% | -3.38% | -0.009 | 1.000 | 1.000 | -3.72% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | -1.20% | 0.11% | -0.39% | 10.65% | -3.29% | -0.326 | 0.993 | 0.989 | -3.45% |
| NASDAQ100 | QQQ | technology_and_growth | -3.29% | -3.78% | -3.45% | 21.48% | -10.14% | 0.356 | 0.910 | 1.689 | -11.22% |
| LARGE_GROWTH | IWF | technology_and_growth | -3.06% | -3.28% | -1.73% | 20.57% | -8.15% | -0.786 | 0.886 | 1.271 | -11.35% |
| LARGE_VALUE | IWD | diversified_us_equity | 0.52% | 3.21% | 1.10% | 9.95% | -1.31% | -0.276 | 0.727 | 0.665 | -1.00% |
| MID_CAP | IJH | diversified_us_equity | -1.37% | 1.13% | -1.96% | 12.21% | -3.09% | -0.434 | 0.798 | 0.888 | -3.09% |
| SMALL_CAP | IWM | diversified_us_equity | -0.89% | 0.62% | -2.60% | 12.26% | -3.95% | -0.286 | 0.786 | 1.094 | -3.95% |
| SMALL_VALUE | IWN | diversified_us_equity | 0.08% | 2.20% | -0.52% | 11.12% | -1.83% | 0.554 | 0.687 | 0.804 | -1.15% |
| DIVIDEND | SCHD | diversified_us_equity | 1.62% | 5.23% | 2.17% | 13.69% | -1.11% | 1.170 | 0.155 | 0.141 | -0.18% |
| LOW_VOL | SPLV | diversified_us_equity | 0.45% | 4.16% | 0.13% | 14.66% | -1.89% | -0.423 | -0.241 | -0.237 | -0.55% |
| MOMENTUM | MTUM | diversified_us_equity | -7.60% | -7.50% | -7.34% | 36.02% | -17.42% | 0.389 | 0.733 | 2.073 | -17.99% |
| TECHNOLOGY | XLK | technology_and_growth | -5.29% | -5.20% | -3.64% | 29.46% | -12.57% | -0.613 | 0.827 | 2.076 | -15.86% |
| COMMUNICATIONS | XLC | technology_and_growth | 3.02% | 2.69% | 0.36% | 21.56% | -7.06% | 0.657 | 0.467 | 0.603 | -8.27% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | 2.01% | 0.29% | -3.51% | 21.89% | -7.90% | 0.067 | 0.720 | 1.128 | -10.01% |
| CONSUMER_STAPLES | XLP | consumer_defensive | 3.84% | 5.93% | -0.85% | 20.24% | -3.03% | 0.685 | -0.254 | -0.322 | -1.72% |
| HEALTHCARE | XLV | healthcare_and_biotech | 2.26% | 6.67% | -1.68% | 20.53% | -3.74% | -0.427 | -0.080 | -0.111 | -0.61% |
| FINANCIALS | XLF | financials | 0.66% | 3.53% | 3.47% | 15.69% | -2.08% | -0.192 | 0.247 | 0.253 | -1.60% |
| INDUSTRIALS | XLI | industrials_and_defense | -3.28% | 1.18% | -3.00% | 16.96% | -4.80% | -0.347 | 0.657 | 0.988 | -4.80% |
| ENERGY | XLE | energy | -1.63% | 1.47% | 9.62% | 21.21% | -3.44% | -0.229 | -0.386 | -0.715 | -5.57% |
| MATERIALS | XLB | materials_and_mining | 0.94% | 4.21% | -0.55% | 18.55% | -3.81% | 0.035 | 0.537 | 0.814 | -2.71% |
| UTILITIES | XLU | rate_sensitive_defensive | -2.98% | 0.18% | -1.06% | 17.02% | -2.98% | -0.583 | -0.029 | -0.038 | -4.65% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | 0.02% | 4.51% | -0.66% | 16.32% | -1.98% | -0.026 | -0.061 | -0.073 | -0.11% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | 0.15% | 2.48% | -2.60% | 4.36% | -2.00% | -0.802 | 0.532 | 0.203 | -3.37% |
| LONG_TREASURY | TLT | rates_and_duration | -0.48% | 1.69% | -5.10% | 9.14% | -4.91% | 0.310 | 0.442 | 0.315 | -7.06% |
| TIPS | TIP | rates_and_duration | 0.25% | 2.40% | -1.85% | 2.94% | -1.33% | -0.066 | 0.512 | 0.137 | -1.18% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | -0.01% | 1.98% | -3.29% | 4.92% | -2.83% | 0.751 | 0.584 | 0.237 | -3.12% |
| HIGH_YIELD_CREDIT | HYG | credit | 0.01% | 2.05% | -1.02% | 2.55% | -0.80% | 0.889 | 0.767 | 0.211 | -0.79% |
| AGGREGATE_BONDS | AGG | rates_and_duration | 0.09% | 2.37% | -2.34% | 3.68% | -1.71% | -0.321 | 0.573 | 0.181 | -2.19% |
| DEVELOPED_EX_US | VEA | international_equity | -1.09% | 0.22% | -1.47% | 15.65% | -4.09% | -0.547 | 0.828 | 1.289 | -4.75% |
| EMERGING_MARKETS | VWO | international_equity | -1.52% | -0.81% | -1.49% | 17.56% | -5.24% | -0.875 | 0.861 | 1.314 | -7.05% |
| EUROPE | VGK | international_equity | 0.51% | 2.14% | 0.29% | 13.50% | -2.53% | -0.501 | 0.720 | 0.971 | -1.23% |
| JAPAN | EWJ | international_equity | -2.04% | -0.68% | -1.96% | 21.11% | -6.21% | -0.767 | 0.770 | 1.295 | -7.86% |
| CHINA | MCHI | international_equity | 3.26% | 5.20% | 4.61% | 19.41% | -2.22% | -0.796 | 0.442 | 0.697 | -16.24% |
| INDIA | INDA | international_equity | 2.39% | 4.37% | -2.82% | 13.87% | -4.51% | 1.016 | 0.560 | 0.667 | -11.07% |
| GOLD | IAU | precious_metals | -0.25% | 0.28% | 1.99% | 20.61% | -4.47% | -0.829 | 0.640 | 1.147 | -25.14% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | -2.12% | 1.05% | 11.57% | 24.37% | -5.54% | -0.297 | -0.174 | -0.298 | -7.09% |
| SEMICONDUCTORS | SMH | technology_and_growth | -10.15% | -11.69% | -8.00% | 48.70% | -23.12% | 2.453 | 0.775 | 3.120 | -24.62% |
| SOFTWARE | IGV | technology_and_growth | 4.99% | 6.16% | -1.83% | 25.25% | -8.11% | 0.002 | 0.307 | 0.771 | -21.57% |
| BROAD_AI_TECH | AIQ | technology_and_growth | -3.45% | -4.52% | -7.22% | 33.37% | -14.68% | 0.006 | 0.809 | 2.382 | -20.19% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | -3.91% | -5.64% | -8.07% | 31.67% | -17.14% | -0.187 | 0.847 | 2.474 | -23.82% |
| CYBERSECURITY | CIBR | technology_and_growth | 0.44% | 1.80% | 0.07% | 25.01% | -7.40% | -0.865 | 0.429 | 1.039 | -6.27% |
| SOLAR | TAN | clean_energy | -7.02% | -8.84% | -7.60% | 39.17% | -19.39% | 0.420 | 0.727 | 2.511 | -35.51% |
| METALS_MINING | XME | materials_and_mining | -4.09% | -3.32% | -3.70% | 32.55% | -8.74% | -0.244 | 0.686 | 2.067 | -26.49% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | 1.01% | 3.83% | -1.03% | 9.99% | -1.46% | -0.164 | 0.723 | 0.609 | -0.90% |
| BIOTECH | XBI | healthcare_and_biotech | -1.71% | -0.36% | -4.78% | 25.38% | -9.96% | -0.313 | 0.363 | 0.828 | -9.96% |
| REGIONAL_BANKS | KRE | financials | 0.59% | 3.17% | 0.27% | 20.21% | -3.73% | -0.236 | 0.219 | 0.334 | -2.23% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | -1.62% | 4.63% | -4.22% | 25.45% | -8.58% | 0.254 | 0.490 | 0.960 | -5.79% |
| CANADA | EWC | international_equity | 0.37% | 2.42% | 2.25% | 9.64% | -1.46% | -0.550 | 0.611 | 0.607 | -0.92% |
| UNITED_KINGDOM | EWU | international_equity | 1.42% | 3.80% | 1.50% | 14.53% | -1.93% | -0.438 | 0.470 | 0.598 | -0.19% |
| AUSTRALIA | EWA | international_equity | 1.36% | 3.27% | 1.80% | 13.89% | -1.63% | -0.464 | 0.614 | 0.860 | -2.45% |
| SOUTH_KOREA | EWY | international_equity | -11.51% | -12.98% | -14.57% | 67.94% | -28.57% | 0.823 | 0.702 | 4.194 | -34.21% |
| TAIWAN | EWT | international_equity | -8.77% | -9.67% | -4.75% | 42.26% | -17.68% | -0.370 | 0.782 | 2.537 | -19.83% |
| BRAZIL | EWZ | international_equity | -0.73% | -0.74% | 5.13% | 21.61% | -3.14% | -0.809 | 0.443 | 0.799 | -14.19% |
| MEXICO | EWW | international_equity | 0.16% | 0.92% | -0.09% | 17.13% | -2.98% | -0.194 | 0.643 | 0.990 | -5.60% |
| SOUTH_AFRICA | EZA | international_equity | 1.65% | 0.97% | -1.56% | 22.92% | -6.50% | 0.385 | 0.743 | 1.827 | -22.25% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | 0.13% | 2.49% | -2.43% | 4.54% | -1.85% | 0.552 | 0.581 | 0.216 | -2.10% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | 0.21% | 2.30% | -2.30% | 3.34% | -2.15% | 3.769 | 0.575 | 0.134 | -1.67% |
| EMERGING_MARKET_BONDS | EMB | credit | -0.08% | 1.84% | -2.24% | 4.84% | -1.96% | 0.122 | 0.750 | 0.334 | -1.93% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | 0.02% | 2.42% | -2.12% | 3.65% | -1.44% | -0.769 | 0.558 | 0.178 | -1.71% |
| SILVER | SLV | precious_metals | -1.56% | -1.59% | 1.49% | 36.62% | -10.19% | -0.821 | 0.618 | 2.329 | -50.98% |
| COPPER | CPER | non_energy_commodities | 0.00% | 0.11% | 4.56% | 21.31% | -3.26% | -0.339 | 0.692 | 1.511 | -5.54% |
| AGRICULTURE | DBA | non_energy_commodities | -2.66% | -0.22% | 5.62% | 16.59% | -2.66% | -0.760 | 0.091 | 0.097 | -4.32% |
| OIL | USO | energy | -5.40% | 0.60% | 22.11% | 62.87% | -13.62% | 0.560 | -0.338 | -1.420 | -15.46% |
| US_DOLLAR | UUP | currencies | -0.56% | 2.30% | -0.58% | 4.72% | -0.88% | -0.853 | -0.436 | -0.164 | -0.63% |
| EURO | FXE | currencies | 0.71% | 2.75% | -0.91% | 4.23% | -0.81% | -0.625 | 0.476 | 0.170 | -4.50% |
| YEN | FXY | currencies | 0.16% | 2.22% | -1.62% | 5.48% | -1.67% | 0.734 | 0.170 | 0.083 | -10.65% |
| BITCOIN_ETF | IBIT | crypto_assets | -0.96% | -1.19% | 8.38% | 31.78% | -4.43% | -0.628 | 0.451 | 1.252 | -49.50% |
| ETHEREUM_ETF | ETHA | crypto_assets | 1.42% | 0.47% | 17.76% | 47.34% | -4.20% | 0.289 | 0.561 | 2.237 | -61.08% |
