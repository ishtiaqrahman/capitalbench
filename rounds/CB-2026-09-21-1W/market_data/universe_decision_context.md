# Full-Universe Horizon-Specific Decision Context

Profile: weekly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: tiingo_eod_adjusted_price_and_volume
- As-of date requested: 2026-09-18
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | -0.09% |
| spy_return_21s | -0.71% |
| rsp_return_5s | -1.20% |
| rsp_return_21s | -4.40% |
| hyg_return_5s | -0.09% |
| hyg_return_21s | -0.94% |
| tlt_return_5s | 0.47% |
| tlt_return_21s | -1.76% |
| uup_return_5s | 1.14% |
| uup_return_21s | 1.83% |
| uso_return_5s | -0.70% |
| uso_return_21s | 17.50% |
| iau_return_5s | 0.64% |
| iau_return_21s | -3.08% |
| rsp_minus_spy_5s | -1.11% |
| rsp_minus_spy_21s | -3.69% |
| positive_asset_share_5s | 34.78% |
| positive_asset_share_21s | 31.88% |
| active_return_dispersion_5s | 1.88% |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_3s | active_return_5s | prior_16s_active_return | volatility_21s | max_drawdown_21s | volume_zscore_5v60 | corr_spy_63s | beta_spy_63s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | 0.09% | 0.62% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.04% | 0.15% | 0.85% | 0.17% | 0.00% | 0.279 | 0.038 | 0.001 | 0.00% |
| SP500 | SPY | diversified_us_equity | 0.82% | 0.00% | 0.00% | 9.41% | -2.47% | 0.491 | 1.000 | 1.000 | -1.84% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | 0.69% | -0.14% | -0.35% | 9.59% | -2.54% | -0.574 | 0.991 | 0.973 | -2.31% |
| NASDAQ100 | QQQ | technology_and_growth | 2.40% | 1.01% | 0.45% | 13.21% | -2.30% | -0.098 | 0.898 | 1.635 | -3.21% |
| LARGE_GROWTH | IWF | technology_and_growth | 2.32% | 0.99% | 0.29% | 14.04% | -2.69% | 0.350 | 0.881 | 1.481 | -4.12% |
| LARGE_VALUE | IWD | diversified_us_equity | -0.71% | -1.06% | -0.61% | 9.18% | -2.81% | -0.321 | 0.578 | 0.485 | -2.60% |
| MID_CAP | IJH | diversified_us_equity | -0.34% | -1.57% | -2.75% | 10.87% | -5.21% | 0.514 | 0.767 | 0.808 | -6.95% |
| SMALL_CAP | IWM | diversified_us_equity | -0.36% | -1.31% | -3.63% | 11.93% | -5.65% | 0.895 | 0.722 | 0.815 | -6.63% |
| SMALL_VALUE | IWN | diversified_us_equity | -0.96% | -1.38% | -2.00% | 9.85% | -4.06% | -0.137 | 0.572 | 0.520 | -4.83% |
| DIVIDEND | SCHD | diversified_us_equity | -1.89% | -1.20% | -2.14% | 9.60% | -4.35% | -0.202 | 0.022 | 0.023 | -4.35% |
| LOW_VOL | SPLV | diversified_us_equity | -1.14% | -1.55% | -2.08% | 8.33% | -4.51% | -0.993 | -0.185 | -0.183 | -6.74% |
| MOMENTUM | MTUM | diversified_us_equity | 3.38% | 1.14% | 1.00% | 19.24% | -3.10% | -1.093 | 0.628 | 1.828 | -10.13% |
| TECHNOLOGY | XLK | technology_and_growth | 3.19% | 1.12% | 2.81% | 20.68% | -2.66% | -0.356 | 0.785 | 1.986 | -4.23% |
| COMMUNICATIONS | XLC | technology_and_growth | -2.82% | -1.50% | 1.77% | 16.72% | -3.70% | -0.284 | 0.313 | 0.543 | -7.18% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | 0.14% | -1.62% | -4.13% | 15.96% | -7.09% | 0.089 | 0.627 | 1.097 | -10.48% |
| CONSUMER_STAPLES | XLP | consumer_defensive | -1.11% | -0.60% | -3.03% | 13.38% | -5.32% | -0.037 | -0.192 | -0.276 | -6.85% |
| HEALTHCARE | XLV | healthcare_and_biotech | 0.44% | 1.93% | -5.25% | 15.23% | -5.87% | -0.372 | -0.152 | -0.252 | -4.15% |
| FINANCIALS | XLF | financials | -1.74% | -2.33% | 0.22% | 13.30% | -4.61% | 0.759 | 0.422 | 0.469 | -4.61% |
| INDUSTRIALS | XLI | industrials_and_defense | 0.53% | -1.43% | -4.64% | 13.20% | -7.28% | 0.653 | 0.629 | 0.894 | -8.99% |
| ENERGY | XLE | energy | -2.46% | -1.18% | 3.07% | 18.93% | -2.88% | 1.651 | -0.316 | -0.581 | -2.46% |
| MATERIALS | XLB | materials_and_mining | -1.46% | -1.79% | -2.37% | 14.87% | -6.86% | -0.423 | 0.311 | 0.471 | -6.86% |
| UTILITIES | XLU | rate_sensitive_defensive | -0.53% | -2.95% | -3.08% | 15.21% | -6.63% | 0.584 | -0.083 | -0.106 | -12.74% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | -1.25% | -1.96% | -2.87% | 10.03% | -6.24% | 0.070 | -0.103 | -0.124 | -7.56% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | -0.02% | -0.14% | -1.57% | 4.96% | -2.62% | 0.368 | 0.371 | 0.155 | -5.16% |
| LONG_TREASURY | TLT | rates_and_duration | 0.67% | 0.56% | -1.60% | 8.92% | -2.93% | 0.969 | 0.341 | 0.288 | -8.13% |
| TIPS | TIP | rates_and_duration | -0.49% | -0.45% | -0.93% | 3.91% | -2.20% | 0.330 | 0.182 | 0.056 | -2.76% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | 0.40% | 0.46% | -1.08% | 5.73% | -2.00% | 0.516 | 0.458 | 0.216 | -3.69% |
| HIGH_YIELD_CREDIT | HYG | credit | 0.19% | 0.00% | -0.23% | 3.08% | -1.39% | 1.296 | 0.727 | 0.175 | -1.20% |
| AGGREGATE_BONDS | AGG | rates_and_duration | 0.11% | 0.07% | -0.92% | 4.35% | -1.90% | 0.696 | 0.414 | 0.147 | -3.11% |
| DEVELOPED_EX_US | VEA | international_equity | 0.04% | -1.46% | 0.43% | 12.94% | -3.43% | -0.457 | 0.764 | 1.077 | -3.03% |
| EMERGING_MARKETS | VWO | international_equity | 1.53% | -0.28% | 1.14% | 11.59% | -3.68% | -0.486 | 0.782 | 1.065 | -2.14% |
| EUROPE | VGK | international_equity | -0.59% | -1.67% | -1.78% | 10.24% | -5.11% | 1.166 | 0.713 | 0.763 | -5.11% |
| JAPAN | EWJ | international_equity | 0.08% | -1.49% | 4.61% | 14.43% | -1.87% | -0.673 | 0.718 | 1.346 | -1.58% |
| CHINA | MCHI | international_equity | 0.30% | 0.30% | -3.77% | 12.68% | -6.02% | -0.917 | 0.343 | 0.489 | -19.28% |
| INDIA | INDA | international_equity | 0.90% | -1.04% | -1.34% | 13.83% | -5.51% | 0.687 | 0.511 | 0.567 | -13.15% |
| GOLD | IAU | precious_metals | 1.79% | 0.73% | -3.07% | 23.68% | -8.48% | 0.000 | 0.332 | 0.705 | -19.04% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | -2.19% | -0.56% | 8.59% | 18.87% | -2.57% | -0.138 | -0.347 | -0.667 | -2.19% |
| SEMICONDUCTORS | SMH | technology_and_growth | 5.70% | 0.88% | 1.98% | 33.25% | -5.71% | -0.513 | 0.682 | 2.675 | -14.34% |
| SOFTWARE | IGV | technology_and_growth | -1.14% | 2.88% | -0.63% | 41.05% | -8.27% | -0.814 | 0.423 | 1.252 | -11.39% |
| BROAD_AI_TECH | AIQ | technology_and_growth | 1.86% | 0.33% | 2.19% | 19.09% | -2.45% | -0.475 | 0.796 | 2.121 | -8.57% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | 2.73% | 0.79% | -3.07% | 23.63% | -5.60% | -0.921 | 0.818 | 2.266 | -15.03% |
| CYBERSECURITY | CIBR | technology_and_growth | -1.12% | 5.89% | -0.57% | 43.02% | -7.19% | 1.027 | 0.432 | 1.250 | -2.28% |
| SOLAR | TAN | clean_energy | 1.26% | -3.07% | -5.96% | 28.72% | -11.59% | 0.126 | 0.707 | 2.204 | -38.24% |
| METALS_MINING | XME | materials_and_mining | -0.69% | -4.26% | -2.32% | 34.89% | -11.64% | -0.493 | 0.559 | 1.804 | -18.12% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | -0.78% | -1.11% | -2.62% | 9.18% | -4.43% | -0.417 | 0.619 | 0.548 | -4.70% |
| BIOTECH | XBI | healthcare_and_biotech | 1.75% | 0.43% | -7.25% | 26.89% | -9.15% | 0.118 | 0.266 | 0.676 | -7.57% |
| REGIONAL_BANKS | KRE | financials | -1.76% | -1.46% | -0.85% | 13.92% | -3.36% | 0.915 | 0.235 | 0.341 | -6.65% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | -0.07% | -2.15% | -10.41% | 17.12% | -13.02% | 2.044 | 0.439 | 0.800 | -15.45% |
| CANADA | EWC | international_equity | -0.12% | -0.50% | -1.40% | 13.65% | -4.44% | -0.217 | 0.550 | 0.530 | -3.86% |
| UNITED_KINGDOM | EWU | international_equity | -1.11% | -1.30% | -0.68% | 11.00% | -4.29% | -0.286 | 0.389 | 0.399 | -4.29% |
| AUSTRALIA | EWA | international_equity | -0.48% | -1.68% | -1.72% | 17.28% | -6.38% | 1.350 | 0.625 | 0.866 | -5.52% |
| SOUTH_KOREA | EWY | international_equity | 2.73% | -3.83% | 8.81% | 43.51% | -7.99% | -0.793 | 0.573 | 3.295 | -17.29% |
| TAIWAN | EWT | international_equity | 4.66% | 0.75% | 6.55% | 23.73% | -4.91% | -1.007 | 0.725 | 2.293 | -0.48% |
| BRAZIL | EWZ | international_equity | -0.69% | -1.66% | 12.09% | 22.81% | -2.93% | -0.167 | 0.247 | 0.468 | -9.23% |
| MEXICO | EWW | international_equity | -0.93% | -2.61% | 0.94% | 17.43% | -6.37% | -0.152 | 0.553 | 0.827 | -8.39% |
| SOUTH_AFRICA | EZA | international_equity | -0.62% | -2.20% | 0.35% | 23.85% | -6.84% | 0.158 | 0.576 | 1.343 | -14.29% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | 0.05% | -0.01% | -1.36% | 5.20% | -2.36% | 0.612 | 0.436 | 0.184 | -3.42% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | 0.01% | -0.19% | -1.48% | 4.17% | -2.53% | 1.968 | 0.480 | 0.148 | -3.83% |
| EMERGING_MARKET_BONDS | EMB | credit | 0.42% | 0.14% | -0.81% | 5.10% | -2.08% | 0.590 | 0.654 | 0.283 | -2.30% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | 0.38% | 0.22% | -0.70% | 3.92% | -1.92% | 0.147 | 0.501 | 0.160 | -2.79% |
| SILVER | SLV | precious_metals | 4.17% | 3.21% | -2.53% | 38.35% | -9.45% | -0.268 | 0.436 | 1.554 | -43.25% |
| COPPER | CPER | non_energy_commodities | 4.03% | 2.77% | 0.09% | 27.90% | -6.80% | -0.240 | 0.485 | 1.037 | -2.00% |
| AGRICULTURE | DBA | non_energy_commodities | -2.53% | -2.60% | 2.88% | 12.74% | -4.54% | 0.672 | 0.017 | 0.020 | -4.54% |
| OIL | USO | energy | -4.97% | -0.60% | 18.95% | 42.17% | -6.31% | -0.001 | -0.432 | -1.943 | -4.97% |
| US_DOLLAR | UUP | currencies | 0.60% | 1.23% | 1.30% | 4.48% | -0.82% | -0.058 | -0.344 | -0.152 | -0.73% |
| EURO | FXE | currencies | -0.47% | -0.86% | -0.02% | 3.73% | -1.73% | 0.290 | 0.308 | 0.120 | -4.09% |
| YEN | FXY | currencies | -1.10% | -1.92% | 3.48% | 11.00% | -2.04% | 0.143 | 0.333 | 0.285 | -6.46% |
| BITCOIN_ETF | IBIT | crypto_assets | 6.75% | 5.23% | 13.49% | 48.72% | -7.14% | 0.436 | 0.287 | 0.972 | -35.45% |
| ETHEREUM_ETF | ETHA | crypto_assets | 9.45% | 4.06% | 21.28% | 57.48% | -5.32% | 1.056 | 0.263 | 1.158 | -44.34% |
