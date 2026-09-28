# Full-Universe Horizon-Specific Decision Context

Profile: weekly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: tiingo_eod_adjusted_price_and_volume
- As-of date requested: 2026-09-25
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | 1.27% |
| spy_return_21s | 0.94% |
| rsp_return_5s | -0.18% |
| rsp_return_21s | -4.60% |
| hyg_return_5s | -0.85% |
| hyg_return_21s | -2.02% |
| tlt_return_5s | -2.38% |
| tlt_return_21s | -4.41% |
| uup_return_5s | 0.81% |
| uup_return_21s | 2.14% |
| uso_return_5s | -3.57% |
| uso_return_21s | 16.47% |
| iau_return_5s | -1.91% |
| iau_return_21s | -6.61% |
| rsp_minus_spy_5s | -1.45% |
| rsp_minus_spy_21s | -5.53% |
| positive_asset_share_5s | 43.48% |
| positive_asset_share_21s | 34.78% |
| active_return_dispersion_5s | 1.87% |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_3s | active_return_5s | prior_16s_active_return | volatility_21s | max_drawdown_21s | volume_zscore_5v60 | corr_spy_63s | beta_spy_63s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | -1.27% | 0.33% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.05% | -1.19% | 0.55% | 0.21% | -0.01% | 0.325 | 0.087 | 0.002 | 0.00% |
| SP500 | SPY | diversified_us_equity | -0.26% | 0.00% | 0.00% | 10.75% | -2.47% | -0.100 | 1.000 | 1.000 | -0.59% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | -0.39% | -0.11% | -0.41% | 10.82% | -2.54% | -0.518 | 0.995 | 0.989 | -1.18% |
| NASDAQ100 | QQQ | technology_and_growth | -0.40% | 2.03% | 1.74% | 16.12% | -2.30% | -0.070 | 0.894 | 1.595 | -0.40% |
| LARGE_GROWTH | IWF | technology_and_growth | -0.36% | 1.17% | 1.65% | 15.89% | -2.69% | -0.353 | 0.921 | 1.551 | -1.78% |
| LARGE_VALUE | IWD | diversified_us_equity | -0.29% | -1.18% | -1.93% | 9.03% | -2.97% | -0.202 | 0.594 | 0.467 | -2.52% |
| MID_CAP | IJH | diversified_us_equity | -0.65% | -1.25% | -4.13% | 10.37% | -4.82% | 0.542 | 0.779 | 0.802 | -6.93% |
| SMALL_CAP | IWM | diversified_us_equity | -1.82% | -2.02% | -4.38% | 12.48% | -5.81% | 0.561 | 0.756 | 0.865 | -7.33% |
| SMALL_VALUE | IWN | diversified_us_equity | -1.48% | -2.24% | -3.19% | 10.71% | -4.79% | -0.146 | 0.628 | 0.582 | -5.75% |
| DIVIDEND | SCHD | diversified_us_equity | -0.78% | -1.87% | -3.58% | 9.03% | -4.89% | 0.337 | 0.066 | 0.067 | -4.92% |
| LOW_VOL | SPLV | diversified_us_equity | -0.89% | -2.84% | -4.02% | 6.93% | -6.10% | -0.531 | -0.076 | -0.072 | -8.20% |
| MOMENTUM | MTUM | diversified_us_equity | 0.19% | 1.60% | 2.38% | 19.57% | -3.10% | 3.288 | 0.620 | 1.651 | -7.55% |
| TECHNOLOGY | XLK | technology_and_growth | 0.00% | 2.37% | 4.02% | 21.65% | -2.66% | -0.314 | 0.774 | 1.896 | -0.75% |
| COMMUNICATIONS | XLC | technology_and_growth | -0.50% | 1.00% | -1.27% | 22.24% | -3.70% | 0.389 | 0.394 | 0.725 | -5.08% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | -1.58% | -1.47% | -4.91% | 16.01% | -6.00% | -0.341 | 0.680 | 1.166 | -10.66% |
| CONSUMER_STAPLES | XLP | consumer_defensive | -0.81% | -1.51% | -3.70% | 11.10% | -4.67% | -0.224 | -0.121 | -0.169 | -7.07% |
| HEALTHCARE | XLV | healthcare_and_biotech | 0.48% | 0.49% | -2.64% | 13.63% | -4.71% | -0.579 | -0.043 | -0.067 | -2.47% |
| FINANCIALS | XLF | financials | 0.07% | -2.75% | -3.79% | 13.33% | -6.55% | 1.098 | 0.459 | 0.536 | -6.02% |
| INDUSTRIALS | XLI | industrials_and_defense | 0.09% | -0.60% | -5.55% | 12.85% | -6.45% | 0.707 | 0.633 | 0.817 | -8.38% |
| ENERGY | XLE | energy | 0.42% | -4.21% | 3.34% | 20.34% | -5.72% | 1.315 | -0.386 | -0.722 | -5.33% |
| MATERIALS | XLB | materials_and_mining | -1.44% | -1.19% | -6.53% | 14.28% | -7.01% | -0.084 | 0.269 | 0.408 | -6.78% |
| UTILITIES | XLU | rate_sensitive_defensive | -2.52% | -4.43% | -5.21% | 13.73% | -8.87% | 1.051 | 0.016 | 0.020 | -15.50% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | -2.21% | -2.74% | -5.35% | 11.17% | -7.06% | 0.380 | 0.069 | 0.081 | -8.92% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | -1.27% | -2.15% | -2.02% | 6.01% | -3.54% | 0.770 | 0.495 | 0.223 | -6.00% |
| LONG_TREASURY | TLT | rates_and_duration | -2.97% | -3.64% | -1.76% | 9.85% | -4.41% | 1.120 | 0.431 | 0.376 | -10.32% |
| TIPS | TIP | rates_and_duration | -0.97% | -1.96% | -1.76% | 4.65% | -2.99% | 0.370 | 0.304 | 0.100 | -3.44% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | -1.79% | -2.69% | -1.21% | 6.65% | -2.99% | 0.728 | 0.534 | 0.275 | -5.06% |
| HIGH_YIELD_CREDIT | HYG | credit | -1.03% | -2.12% | -0.85% | 3.74% | -2.02% | 2.612 | 0.711 | 0.196 | -2.04% |
| AGGREGATE_BONDS | AGG | rates_and_duration | -1.17% | -2.14% | -1.27% | 5.01% | -2.64% | 1.181 | 0.508 | 0.194 | -3.96% |
| DEVELOPED_EX_US | VEA | international_equity | -1.20% | -0.62% | -2.25% | 14.98% | -3.43% | -0.402 | 0.761 | 1.030 | -2.40% |
| EMERGING_MARKETS | VWO | international_equity | -1.54% | -1.02% | -0.56% | 13.65% | -3.68% | -0.035 | 0.801 | 1.052 | -1.90% |
| EUROPE | VGK | international_equity | -0.89% | -0.79% | -4.28% | 11.95% | -4.82% | 0.665 | 0.720 | 0.781 | -4.65% |
| JAPAN | EWJ | international_equity | -0.86% | -0.31% | 1.97% | 17.97% | -3.01% | 0.067 | 0.698 | 1.251 | -0.86% |
| CHINA | MCHI | international_equity | -3.00% | -2.12% | -3.36% | 15.27% | -5.29% | -0.626 | 0.351 | 0.505 | -19.96% |
| INDIA | INDA | international_equity | -0.89% | -1.60% | -3.15% | 12.96% | -5.02% | -0.514 | 0.541 | 0.586 | -13.44% |
| GOLD | IAU | precious_metals | -1.67% | -3.18% | -4.47% | 22.45% | -7.30% | -0.193 | 0.311 | 0.635 | -20.59% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | 0.72% | -2.08% | 8.47% | 19.20% | -3.68% | -0.155 | -0.503 | -0.923 | -2.99% |
| SEMICONDUCTORS | SMH | technology_and_growth | -0.15% | 4.59% | 3.43% | 34.96% | -5.71% | -0.523 | 0.670 | 2.487 | -9.32% |
| SOFTWARE | IGV | technology_and_growth | -0.69% | 0.32% | 2.24% | 41.94% | -8.27% | -0.962 | 0.478 | 1.376 | -9.44% |
| BROAD_AI_TECH | AIQ | technology_and_growth | -1.12% | 1.60% | 2.01% | 21.31% | -2.45% | -0.585 | 0.791 | 2.003 | -5.94% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | -1.62% | 0.55% | 0.22% | 22.19% | -4.20% | -0.513 | 0.822 | 2.251 | -13.49% |
| CYBERSECURITY | CIBR | technology_and_growth | -1.58% | -0.18% | 6.96% | 43.55% | -7.19% | 0.194 | 0.465 | 1.375 | -2.94% |
| SOLAR | TAN | clean_energy | -5.25% | -4.77% | -6.07% | 33.03% | -12.61% | -0.312 | 0.707 | 2.239 | -40.40% |
| METALS_MINING | XME | materials_and_mining | -3.22% | -1.52% | -9.34% | 31.60% | -12.17% | -0.647 | 0.525 | 1.656 | -18.33% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | -0.79% | -1.45% | -4.09% | 9.20% | -4.98% | -0.451 | 0.645 | 0.568 | -4.88% |
| BIOTECH | XBI | healthcare_and_biotech | -4.23% | -2.35% | -6.60% | 26.47% | -8.53% | 0.724 | 0.368 | 0.938 | -8.56% |
| REGIONAL_BANKS | KRE | financials | 0.51% | -2.35% | -2.13% | 15.35% | -5.96% | 0.471 | 0.322 | 0.460 | -7.66% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | -0.09% | -1.28% | -9.10% | 13.52% | -9.89% | 0.499 | 0.473 | 0.866 | -15.46% |
| CANADA | EWC | international_equity | -1.93% | -2.31% | -2.90% | 14.19% | -4.85% | 0.833 | 0.568 | 0.574 | -4.87% |
| UNITED_KINGDOM | EWU | international_equity | -0.73% | -1.16% | -2.93% | 10.99% | -3.62% | -0.020 | 0.433 | 0.451 | -4.19% |
| AUSTRALIA | EWA | international_equity | -2.27% | -2.38% | -4.32% | 18.02% | -6.78% | 0.085 | 0.628 | 0.904 | -6.57% |
| SOUTH_KOREA | EWY | international_equity | -2.82% | 1.97% | 1.52% | 46.09% | -7.99% | -0.580 | 0.553 | 2.969 | -14.61% |
| TAIWAN | EWT | international_equity | -0.29% | 1.54% | 5.26% | 27.12% | -4.91% | 0.641 | 0.725 | 2.222 | -0.74% |
| BRAZIL | EWZ | international_equity | -3.76% | -3.13% | 5.37% | 23.15% | -4.64% | 0.690 | 0.316 | 0.609 | -10.92% |
| MEXICO | EWW | international_equity | -1.50% | -1.27% | -5.10% | 16.47% | -6.50% | 0.152 | 0.560 | 0.799 | -8.39% |
| SOUTH_AFRICA | EZA | international_equity | -3.86% | -4.20% | -4.12% | 24.20% | -8.24% | 0.249 | 0.555 | 1.291 | -16.80% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | -1.21% | -2.31% | -1.76% | 6.56% | -3.62% | 12.208 | 0.513 | 0.244 | -4.43% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | -1.54% | -2.93% | -1.84% | 4.63% | -3.79% | 2.575 | 0.497 | 0.166 | -5.43% |
| EMERGING_MARKET_BONDS | EMB | credit | -1.63% | -2.55% | -1.27% | 6.06% | -2.86% | 2.065 | 0.683 | 0.328 | -3.56% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | -0.68% | -1.50% | -0.95% | 4.25% | -1.65% | 1.134 | 0.615 | 0.209 | -3.02% |
| SILVER | SLV | precious_metals | -4.26% | -4.26% | -2.37% | 39.86% | -9.45% | -0.386 | 0.423 | 1.386 | -44.94% |
| COPPER | CPER | non_energy_commodities | -1.98% | -0.32% | 0.75% | 27.93% | -6.80% | 0.508 | 0.472 | 0.944 | -1.98% |
| AGRICULTURE | DBA | non_energy_commodities | -0.04% | 0.12% | -1.21% | 13.88% | -4.54% | -0.309 | 0.061 | 0.073 | -3.22% |
| OIL | USO | energy | 2.95% | -4.84% | 21.11% | 44.81% | -10.98% | 0.540 | -0.556 | -2.499 | -8.36% |
| US_DOLLAR | UUP | currencies | 0.49% | -0.46% | 1.65% | 4.93% | -0.82% | 0.301 | -0.311 | -0.140 | -0.24% |
| EURO | FXE | currencies | -0.47% | -2.06% | -1.09% | 4.02% | -2.35% | 0.254 | 0.276 | 0.108 | -4.85% |
| YEN | FXY | currencies | 0.15% | -1.58% | 1.94% | 11.75% | -3.38% | -0.189 | 0.325 | 0.289 | -6.75% |
| BITCOIN_ETF | IBIT | crypto_assets | -2.58% | 2.10% | 3.84% | 45.91% | -7.14% | 0.032 | 0.336 | 1.143 | -33.27% |
| ETHEREUM_ETF | ETHA | crypto_assets | -2.17% | 0.69% | 7.14% | 48.07% | -5.32% | -0.190 | 0.276 | 1.182 | -43.25% |
