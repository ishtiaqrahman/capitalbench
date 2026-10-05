# Full-Universe Horizon-Specific Decision Context

Profile: weekly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: tiingo_eod_history_through_2026-09-25; repository_daily_price_snapshots_2026-09-28_to_2026-10-02_(tiingo_eod_or_yahoo_chart_adjclose); yahoo_chart_reported_volume_2026-09-28_to_2026-10-02
- As-of date requested: 2026-10-02
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | -0.22% |
| spy_return_21s | 0.83% |
| rsp_return_5s | -0.65% |
| rsp_return_21s | -3.70% |
| hyg_return_5s | -1.22% |
| hyg_return_21s | -2.78% |
| tlt_return_5s | -2.32% |
| tlt_return_21s | -5.45% |
| uup_return_5s | 0.94% |
| uup_return_21s | 2.56% |
| uso_return_5s | -0.65% |
| uso_return_21s | 4.41% |
| iau_return_5s | -3.36% |
| iau_return_21s | -5.57% |
| rsp_minus_spy_5s | -0.43% |
| rsp_minus_spy_21s | -4.53% |
| positive_asset_share_5s | 26.09% |
| positive_asset_share_21s | 31.88% |
| active_return_dispersion_5s | 1.81% |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_3s | active_return_5s | prior_16s_active_return | volatility_21s | max_drawdown_21s | volume_zscore_5v60 | corr_spy_63s | beta_spy_63s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | 0.22% | -1.06% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | -0.24% | 0.01% | -0.82% | 0.95% | -0.26% | 3.086 | 0.046 | 0.002 | -0.24% |
| SP500 | SPY | diversified_us_equity | 0.71% | 0.00% | 0.00% | 10.74% | -2.47% | 0.284 | 1.000 | 1.000 | -0.81% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | 0.73% | -0.25% | -0.29% | 11.02% | -2.54% | 1.446 | 0.995 | 1.012 | -1.64% |
| NASDAQ100 | QQQ | technology_and_growth | 1.58% | 0.90% | 4.02% | 15.29% | -2.01% | -0.207 | 0.898 | 1.551 | 0.00% |
| LARGE_GROWTH | IWF | technology_and_growth | 1.41% | 0.87% | 2.68% | 14.25% | -2.33% | -0.305 | 0.923 | 1.504 | -1.15% |
| LARGE_VALUE | IWD | diversified_us_equity | 0.16% | -0.79% | -2.70% | 9.17% | -4.06% | 0.621 | 0.692 | 0.560 | -3.50% |
| MID_CAP | IJH | diversified_us_equity | 1.41% | 0.77% | -3.58% | 10.72% | -4.85% | 2.286 | 0.785 | 0.853 | -6.42% |
| SMALL_CAP | IWM | diversified_us_equity | 0.90% | 0.06% | -4.90% | 11.10% | -5.87% | 1.193 | 0.798 | 0.959 | -7.48% |
| SMALL_VALUE | IWN | diversified_us_equity | 0.64% | -0.32% | -4.95% | 9.94% | -6.37% | 2.079 | 0.676 | 0.677 | -6.26% |
| DIVIDEND | SCHD | diversified_us_equity | -0.40% | -1.25% | -5.44% | 9.19% | -6.53% | 0.361 | 0.180 | 0.183 | -6.33% |
| LOW_VOL | SPLV | diversified_us_equity | -0.42% | -0.35% | -5.37% | 7.25% | -6.10% | 0.274 | 0.006 | 0.006 | -8.73% |
| MOMENTUM | MTUM | diversified_us_equity | 1.88% | 1.60% | 6.38% | 18.36% | -3.10% | -0.255 | 0.610 | 1.514 | -6.28% |
| TECHNOLOGY | XLK | technology_and_growth | 2.73% | 2.03% | 5.96% | 17.61% | -2.20% | 0.303 | 0.778 | 1.841 | 0.00% |
| COMMUNICATIONS | XLC | technology_and_growth | -1.03% | -2.12% | -0.26% | 21.22% | -4.19% | 1.287 | 0.413 | 0.773 | -7.30% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | 0.82% | -0.25% | -4.59% | 15.31% | -6.37% | 0.150 | 0.671 | 1.168 | -11.08% |
| CONSUMER_STAPLES | XLP | consumer_defensive | -1.61% | -1.64% | -4.48% | 10.98% | -5.46% | 0.715 | -0.051 | -0.071 | -8.80% |
| HEALTHCARE | XLV | healthcare_and_biotech | -2.67% | -2.43% | -1.98% | 13.99% | -4.56% | 0.028 | 0.004 | 0.005 | -5.05% |
| FINANCIALS | XLF | financials | -0.96% | -2.24% | -5.62% | 13.08% | -8.49% | 1.306 | 0.542 | 0.616 | -8.34% |
| INDUSTRIALS | XLI | industrials_and_defense | 0.48% | -0.06% | -2.16% | 13.18% | -4.47% | 0.432 | 0.618 | 0.823 | -8.63% |
| ENERGY | XLE | energy | 2.08% | 1.48% | -5.18% | 19.66% | -6.15% | 0.361 | -0.349 | -0.684 | -4.14% |
| MATERIALS | XLB | materials_and_mining | -0.49% | -1.67% | -6.58% | 12.41% | -7.91% | 1.391 | 0.386 | 0.585 | -8.54% |
| UTILITIES | XLU | rate_sensitive_defensive | 0.30% | 1.03% | -7.78% | 14.20% | -9.00% | 6.886 | 0.091 | 0.112 | -14.81% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | -1.28% | -1.58% | -5.23% | 11.32% | -7.30% | 2.225 | 0.193 | 0.222 | -10.56% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | -0.45% | -0.83% | -3.42% | 6.02% | -3.50% | 0.920 | 0.537 | 0.251 | -6.99% |
| LONG_TREASURY | TLT | rates_and_duration | -0.96% | -2.10% | -4.27% | 10.13% | -5.75% | 2.688 | 0.489 | 0.438 | -12.40% |
| TIPS | TIP | rates_and_duration | 0.10% | -0.19% | -3.23% | 4.80% | -2.84% | 1.106 | 0.316 | 0.108 | -3.83% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | -0.57% | -1.12% | -3.09% | 6.72% | -3.48% | 3.119 | 0.575 | 0.309 | -6.33% |
| HIGH_YIELD_CREDIT | HYG | credit | -0.58% | -1.00% | -2.64% | 3.88% | -2.92% | 6.130 | 0.695 | 0.208 | -3.24% |
| AGGREGATE_BONDS | AGG | rates_and_duration | -0.37% | -0.69% | -2.84% | 5.03% | -2.84% | 2.581 | 0.551 | 0.220 | -4.84% |
| DEVELOPED_EX_US | VEA | international_equity | -0.07% | -0.77% | -1.85% | 15.53% | -4.58% | 0.534 | 0.784 | 1.089 | -3.37% |
| EMERGING_MARKETS | VWO | international_equity | -0.10% | -0.78% | -1.88% | 14.12% | -3.74% | 0.522 | 0.800 | 1.057 | -2.88% |
| EUROPE | VGK | international_equity | -1.67% | -2.32% | -3.37% | 13.62% | -6.58% | 1.716 | 0.720 | 0.803 | -7.07% |
| JAPAN | EWJ | international_equity | 2.50% | 1.23% | 0.91% | 19.11% | -3.01% | 0.861 | 0.717 | 1.335 | 0.00% |
| CHINA | MCHI | international_equity | -1.65% | -2.40% | -4.58% | 15.68% | -6.68% | -0.146 | 0.288 | 0.418 | -22.06% |
| INDIA | INDA | international_equity | -0.89% | -2.58% | -5.28% | 13.41% | -7.22% | -0.207 | 0.610 | 0.697 | -15.86% |
| GOLD | IAU | precious_metals | -0.73% | -3.14% | -3.35% | 21.88% | -7.85% | -0.323 | 0.381 | 0.842 | -23.25% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | 1.83% | -0.09% | 1.25% | 19.14% | -5.02% | 0.135 | -0.508 | -0.988 | -3.28% |
| SEMICONDUCTORS | SMH | technology_and_growth | 3.91% | 4.19% | 9.13% | 30.43% | -5.71% | -0.602 | 0.671 | 2.377 | -5.73% |
| SOFTWARE | IGV | technology_and_growth | 3.05% | 2.50% | 1.45% | 28.47% | -5.38% | -0.725 | 0.476 | 1.402 | -7.37% |
| BROAD_AI_TECH | AIQ | technology_and_growth | 1.81% | 0.62% | 3.52% | 20.01% | -3.01% | -0.111 | 0.811 | 1.977 | -5.57% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | 2.69% | 0.27% | 2.42% | 22.81% | -4.15% | 0.163 | 0.812 | 2.209 | -13.45% |
| CYBERSECURITY | CIBR | technology_and_growth | 2.68% | 3.94% | 6.87% | 27.88% | -2.94% | 0.720 | 0.409 | 1.215 | 0.00% |
| SOLAR | TAN | clean_energy | 1.43% | 0.20% | -7.85% | 33.70% | -12.48% | -0.593 | 0.691 | 2.245 | -40.42% |
| METALS_MINING | XME | materials_and_mining | 1.77% | -2.17% | -10.32% | 26.99% | -13.61% | -0.397 | 0.590 | 1.945 | -20.29% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | 0.11% | -0.43% | -4.12% | 9.34% | -5.11% | 0.893 | 0.656 | 0.588 | -5.50% |
| BIOTECH | XBI | healthcare_and_biotech | -1.52% | -0.17% | -7.31% | 24.62% | -6.86% | -0.001 | 0.335 | 0.876 | -8.92% |
| REGIONAL_BANKS | KRE | financials | 1.36% | -0.85% | -4.13% | 14.21% | -7.22% | 1.689 | 0.394 | 0.580 | -8.65% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | -0.72% | -2.59% | -5.23% | 13.83% | -8.21% | 0.635 | 0.476 | 0.882 | -17.84% |
| CANADA | EWC | international_equity | -0.36% | -1.24% | -3.80% | 13.42% | -6.71% | -0.061 | 0.635 | 0.686 | -6.26% |
| UNITED_KINGDOM | EWU | international_equity | -1.43% | -2.19% | -2.93% | 12.41% | -5.73% | 0.088 | 0.475 | 0.482 | -6.50% |
| AUSTRALIA | EWA | international_equity | -0.18% | -0.17% | -6.39% | 18.07% | -7.84% | 1.016 | 0.645 | 0.946 | -6.93% |
| SOUTH_KOREA | EWY | international_equity | 2.55% | 2.73% | 3.59% | 47.31% | -7.99% | -0.634 | 0.577 | 3.071 | -12.46% |
| TAIWAN | EWT | international_equity | 1.95% | 1.57% | 3.83% | 28.22% | -4.91% | -0.469 | 0.714 | 2.216 | 0.00% |
| BRAZIL | EWZ | international_equity | 4.72% | 3.94% | -4.39% | 21.66% | -6.22% | 1.807 | 0.351 | 0.736 | -7.61% |
| MEXICO | EWW | international_equity | -1.33% | -2.85% | -4.84% | 18.75% | -9.35% | 0.424 | 0.571 | 0.887 | -11.20% |
| SOUTH_AFRICA | EZA | international_equity | -2.56% | -4.73% | -6.07% | 26.37% | -12.48% | -0.062 | 0.586 | 1.453 | -20.92% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | -0.34% | -1.02% | -3.40% | 6.83% | -3.77% | 0.559 | 0.540 | 0.273 | -5.61% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | 0.68% | 0.01% | -3.99% | 6.09% | -3.78% | 3.476 | 0.423 | 0.168 | -5.63% |
| EMERGING_MARKET_BONDS | EMB | credit | -1.25% | -1.99% | -3.15% | 6.84% | -4.58% | 2.612 | 0.688 | 0.362 | -5.69% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | 0.00% | 0.05% | -1.72% | 4.22% | -1.39% | 1.580 | 0.654 | 0.233 | -3.18% |
| SILVER | SLV | precious_metals | -1.33% | -5.63% | -2.63% | 38.87% | -10.24% | 0.145 | 0.468 | 1.647 | -48.16% |
| COPPER | CPER | non_energy_commodities | -1.03% | -2.46% | 1.67% | 27.53% | -6.80% | -0.297 | 0.492 | 1.027 | -4.61% |
| AGRICULTURE | DBA | non_energy_commodities | -0.14% | -0.93% | -3.55% | 12.57% | -4.06% | -0.275 | 0.079 | 0.089 | -4.34% |
| OIL | USO | energy | 2.80% | -0.43% | 4.03% | 45.23% | -11.44% | 0.237 | -0.582 | -2.767 | -8.95% |
| US_DOLLAR | UUP | currencies | 0.49% | 1.17% | 0.54% | 4.96% | -0.67% | 0.757 | -0.315 | -0.148 | -0.24% |
| EURO | FXE | currencies | -0.80% | -1.04% | -2.70% | 4.47% | -3.41% | -0.012 | 0.253 | 0.106 | -6.05% |
| YEN | FXY | currencies | -0.34% | -0.17% | -0.07% | 11.26% | -3.38% | -0.662 | 0.399 | 0.361 | -7.04% |
| BITCOIN_ETF | IBIT | crypto_assets | 0.85% | 0.56% | 7.57% | 43.23% | -7.14% | -0.478 | 0.365 | 1.252 | -33.05% |
| ETHEREUM_ETF | ETHA | crypto_assets | -0.84% | -0.76% | 11.46% | 45.75% | -5.32% | -0.623 | 0.279 | 1.186 | -43.81% |
