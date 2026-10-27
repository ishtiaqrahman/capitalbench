# Full-Universe Horizon-Specific Decision Context

Profile: weekly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: tiingo_eod_adjusted_price_and_volume; yahoo_chart_adjusted_close_and_reported_volume
- As-of date requested: 2026-10-27
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | 0.08% |
| spy_return_21s | 0.53% |
| rsp_return_5s | 0.77% |
| rsp_return_21s | 3.71% |
| hyg_return_5s | 1.00% |
| hyg_return_21s | 0.52% |
| tlt_return_5s | 1.87% |
| tlt_return_21s | 4.24% |
| uup_return_5s | 0.76% |
| uup_return_21s | 1.46% |
| uso_return_5s | 2.04% |
| uso_return_21s | 9.25% |
| iau_return_5s | -1.43% |
| iau_return_21s | -1.51% |
| rsp_minus_spy_5s | 0.69% |
| rsp_minus_spy_21s | 3.18% |
| positive_asset_share_5s | 69.57% |
| positive_asset_share_21s | 55.07% |
| active_return_dispersion_5s | 3.22% |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_3s | active_return_5s | prior_16s_active_return | volatility_21s | max_drawdown_21s | volume_zscore_5v60 | corr_spy_63s | beta_spy_63s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | -0.08% | -0.45% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.07% | 0.01% | -0.22% | 0.23% | -0.01% | 1.073 | 0.192 | 0.004 | 0.00% |
| SP500 | SPY | diversified_us_equity | 0.75% | 0.00% | 0.00% | 9.74% | -2.45% | -0.630 | 1.000 | 1.000 | -1.21% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | 0.81% | 0.14% | -0.12% | 10.04% | -2.49% | -0.360 | 0.996 | 1.017 | -1.41% |
| NASDAQ100 | QQQ | technology_and_growth | 2.38% | 0.43% | -3.02% | 18.93% | -7.27% | 0.234 | 0.917 | 1.594 | -5.06% |
| LARGE_GROWTH | IWF | technology_and_growth | 1.80% | -0.21% | -2.68% | 18.47% | -7.42% | 1.129 | 0.938 | 1.556 | -5.37% |
| LARGE_VALUE | IWD | diversified_us_equity | -0.21% | 0.24% | 2.61% | 6.68% | -0.85% | 3.919 | 0.699 | 0.533 | -0.21% |
| MID_CAP | IJH | diversified_us_equity | 0.58% | 0.10% | 0.45% | 12.64% | -2.34% | -0.109 | 0.787 | 0.881 | -6.64% |
| SMALL_CAP | IWM | diversified_us_equity | 1.27% | 1.52% | -1.96% | 14.82% | -4.57% | -0.443 | 0.753 | 0.981 | -7.92% |
| SMALL_VALUE | IWN | diversified_us_equity | 0.64% | 1.65% | -0.81% | 12.53% | -2.61% | 0.309 | 0.584 | 0.613 | -5.23% |
| DIVIDEND | SCHD | diversified_us_equity | -0.79% | 1.16% | 4.64% | 12.68% | -1.45% | 0.037 | 0.035 | 0.037 | -0.79% |
| LOW_VOL | SPLV | diversified_us_equity | -1.02% | 1.06% | 4.57% | 12.77% | -1.03% | 0.805 | -0.059 | -0.057 | -2.74% |
| MOMENTUM | MTUM | diversified_us_equity | 3.80% | 1.17% | -6.71% | 23.77% | -11.06% | -0.196 | 0.706 | 1.623 | -13.06% |
| TECHNOLOGY | XLK | technology_and_growth | 3.92% | 2.10% | -5.12% | 24.56% | -9.73% | 0.450 | 0.822 | 1.964 | -6.19% |
| COMMUNICATIONS | XLC | technology_and_growth | -3.57% | -6.08% | -1.34% | 16.31% | -7.88% | 1.219 | 0.366 | 0.675 | -12.96% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | 0.38% | -0.12% | 5.51% | 14.24% | -2.10% | 0.107 | 0.660 | 1.038 | -6.71% |
| CONSUMER_STAPLES | XLP | consumer_defensive | -3.16% | -0.76% | 6.20% | 19.97% | -3.16% | 1.436 | -0.192 | -0.286 | -3.16% |
| HEALTHCARE | XLV | healthcare_and_biotech | -1.17% | -0.44% | 4.55% | 18.90% | -2.97% | -0.051 | -0.004 | -0.006 | -1.17% |
| FINANCIALS | XLF | financials | -1.36% | 0.21% | 2.37% | 12.20% | -1.46% | -0.585 | 0.425 | 0.484 | -4.24% |
| INDUSTRIALS | XLI | industrials_and_defense | 0.71% | 0.59% | -1.62% | 14.41% | -4.06% | 0.332 | 0.676 | 0.875 | -9.73% |
| ENERGY | XLE | energy | 0.95% | 0.27% | 9.00% | 21.83% | -2.05% | 0.550 | -0.292 | -0.590 | -2.05% |
| MATERIALS | XLB | materials_and_mining | 0.17% | 0.99% | 3.11% | 12.03% | -1.88% | -0.648 | 0.310 | 0.437 | -3.08% |
| UTILITIES | XLU | rate_sensitive_defensive | -0.05% | 2.24% | 6.25% | 16.61% | -2.01% | -0.164 | 0.058 | 0.083 | -8.36% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | -0.19% | 0.06% | 2.04% | 15.02% | -1.89% | 1.582 | 0.234 | 0.281 | -6.99% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | -0.11% | 0.86% | 0.70% | 5.23% | -0.43% | 1.237 | 0.280 | 0.147 | -4.52% |
| LONG_TREASURY | TLT | rates_and_duration | -0.13% | 1.79% | 1.88% | 10.54% | -1.53% | -0.179 | 0.222 | 0.222 | -7.34% |
| TIPS | TIP | rates_and_duration | -0.02% | 0.71% | 0.89% | 3.62% | -0.32% | -0.398 | 0.128 | 0.050 | -1.80% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | 0.02% | 0.97% | 0.72% | 5.72% | -0.60% | 0.097 | 0.375 | 0.222 | -3.65% |
| HIGH_YIELD_CREDIT | HYG | credit | 0.65% | 0.92% | -0.92% | 3.78% | -0.62% | 0.102 | 0.666 | 0.225 | -1.94% |
| AGGREGATE_BONDS | AGG | rates_and_duration | -0.03% | 0.78% | 0.56% | 4.23% | -0.31% | -0.320 | 0.321 | 0.142 | -2.64% |
| DEVELOPED_EX_US | VEA | international_equity | 0.90% | 0.06% | -2.59% | 11.03% | -3.17% | -0.278 | 0.774 | 1.024 | -5.06% |
| EMERGING_MARKETS | VWO | international_equity | -0.04% | -2.52% | -2.86% | 14.74% | -6.80% | 0.411 | 0.790 | 1.036 | -7.33% |
| EUROPE | VGK | international_equity | 0.28% | -0.24% | -1.81% | 12.90% | -3.34% | -0.060 | 0.668 | 0.751 | -6.36% |
| JAPAN | EWJ | international_equity | 0.69% | -0.27% | -1.90% | 12.38% | -5.26% | -0.039 | 0.725 | 1.227 | -4.10% |
| CHINA | MCHI | international_equity | 0.12% | -3.77% | -3.46% | 17.34% | -6.76% | -0.099 | 0.448 | 0.639 | -23.75% |
| INDIA | INDA | international_equity | -1.31% | -2.26% | 1.02% | 15.74% | -3.25% | 0.570 | 0.554 | 0.692 | -14.75% |
| GOLD | IAU | precious_metals | 0.89% | -1.51% | -0.53% | 17.68% | -4.72% | -0.201 | 0.409 | 0.910 | -24.85% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | 0.25% | 0.17% | 2.91% | 14.26% | -1.58% | -0.455 | -0.492 | -0.816 | -1.33% |
| SEMICONDUCTORS | SMH | technology_and_growth | 6.62% | 2.05% | -9.39% | 36.92% | -17.44% | 0.539 | 0.710 | 2.437 | -16.58% |
| SOFTWARE | IGV | technology_and_growth | 2.81% | 4.46% | 0.97% | 27.91% | -7.39% | -0.544 | 0.577 | 1.804 | -4.51% |
| BROAD_AI_TECH | AIQ | technology_and_growth | 2.56% | 0.68% | -2.81% | 23.39% | -7.50% | 0.375 | 0.898 | 2.083 | -9.24% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | 4.44% | 2.48% | -7.12% | 29.34% | -12.19% | -0.076 | 0.855 | 2.323 | -18.89% |
| CYBERSECURITY | CIBR | technology_and_growth | 6.65% | 9.13% | -1.70% | 32.20% | -10.16% | 0.623 | 0.500 | 1.635 | -0.32% |
| SOLAR | TAN | clean_energy | 1.62% | 0.57% | -3.36% | 29.72% | -8.20% | 0.045 | 0.730 | 2.246 | -43.16% |
| METALS_MINING | XME | materials_and_mining | 4.05% | 0.07% | -5.26% | 32.82% | -11.30% | -0.084 | 0.605 | 2.054 | -24.24% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | -0.32% | 0.69% | 2.47% | 9.73% | -0.82% | 0.648 | 0.636 | 0.586 | -1.99% |
| BIOTECH | XBI | healthcare_and_biotech | 2.11% | 0.96% | -2.60% | 33.00% | -8.47% | -0.368 | 0.394 | 1.148 | -8.68% |
| REGIONAL_BANKS | KRE | financials | 0.23% | 2.70% | -0.35% | 17.35% | -3.16% | 0.384 | 0.223 | 0.322 | -6.33% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | 0.85% | -0.05% | -1.94% | 16.06% | -3.38% | 0.688 | 0.470 | 0.788 | -18.46% |
| CANADA | EWC | international_equity | 0.18% | 0.22% | 2.60% | 14.18% | -2.10% | -0.068 | 0.583 | 0.712 | -2.54% |
| UNITED_KINGDOM | EWU | international_equity | -1.36% | -1.27% | 0.59% | 12.97% | -2.92% | -0.737 | 0.360 | 0.373 | -4.45% |
| AUSTRALIA | EWA | international_equity | 1.76% | 1.05% | 1.83% | 11.91% | -1.79% | 0.005 | 0.663 | 0.987 | -3.12% |
| SOUTH_KOREA | EWY | international_equity | 5.64% | 2.17% | -16.57% | 44.01% | -22.32% | -0.304 | 0.635 | 3.130 | -28.17% |
| TAIWAN | EWT | international_equity | 3.13% | -0.15% | -6.44% | 28.14% | -11.87% | -0.096 | 0.748 | 2.004 | -9.11% |
| BRAZIL | EWZ | international_equity | -18.04% | -20.20% | 18.14% | 86.35% | -21.57% | 3.398 | 0.068 | 0.332 | -21.22% |
| MEXICO | EWW | international_equity | 0.07% | -0.74% | 3.88% | 16.77% | -3.59% | 0.017 | 0.471 | 0.722 | -6.31% |
| SOUTH_AFRICA | EZA | international_equity | 0.25% | -2.25% | 1.06% | 21.12% | -3.95% | 0.421 | 0.553 | 1.384 | -19.82% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | 0.19% | 1.09% | 0.89% | 5.09% | -0.51% | 0.106 | 0.336 | 0.187 | -2.76% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | 0.61% | 1.41% | 1.56% | 6.04% | -0.81% | -0.072 | 0.258 | 0.127 | -2.64% |
| EMERGING_MARKET_BONDS | EMB | credit | 0.08% | 0.69% | -0.09% | 5.31% | -0.83% | -0.222 | 0.555 | 0.306 | -3.35% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | 0.15% | 0.30% | 0.37% | 2.19% | -0.38% | -0.185 | 0.479 | 0.161 | -2.05% |
| SILVER | SLV | precious_metals | -0.36% | -5.76% | -5.60% | 36.15% | -12.29% | -0.072 | 0.529 | 1.939 | -53.45% |
| COPPER | CPER | non_energy_commodities | 4.11% | 0.68% | -0.27% | 18.18% | -5.32% | -0.107 | 0.488 | 1.025 | -3.33% |
| AGRICULTURE | DBA | non_energy_commodities | -1.86% | -2.81% | -0.73% | 9.32% | -5.03% | 0.276 | 0.072 | 0.078 | -7.09% |
| OIL | USO | energy | 0.84% | 1.96% | 6.62% | 33.78% | -4.44% | -0.108 | -0.578 | -2.236 | -3.33% |
| US_DOLLAR | UUP | currencies | 0.76% | 0.68% | 0.25% | 5.04% | -0.79% | -0.525 | -0.297 | -0.145 | -0.03% |
| EURO | FXE | currencies | -0.67% | -0.91% | -1.52% | 5.11% | -1.89% | -0.733 | 0.284 | 0.127 | -6.86% |
| YEN | FXY | currencies | -0.58% | 0.25% | -0.98% | 4.59% | -0.84% | -0.017 | 0.307 | 0.287 | -3.89% |
| BITCOIN_ETF | IBIT | crypto_assets | -0.78% | -2.24% | -1.51% | 24.12% | -6.88% | -0.510 | 0.374 | 1.311 | -29.99% |
| ETHEREUM_ETF | ETHA | crypto_assets | -1.58% | -3.78% | -9.35% | 34.98% | -14.60% | -0.846 | 0.269 | 1.178 | -44.33% |
