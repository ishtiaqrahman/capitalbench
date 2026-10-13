# Full-Universe Horizon-Specific Decision Context

Profile: weekly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: tiingo_eod_history_through_2026-09-25; repository_daily_price_snapshots_2026-09-28_to_2026-10-12_(tiingo_eod_or_yahoo_chart_adjclose); yahoo_chart_reported_volume_2026-09-28_to_2026-10-12
- As-of date requested: 2026-10-12
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | 0.42% |
| spy_return_21s | 2.06% |
| rsp_return_5s | 0.98% |
| rsp_return_21s | -0.41% |
| hyg_return_5s | 0.40% |
| hyg_return_21s | -1.67% |
| tlt_return_5s | 1.22% |
| tlt_return_21s | -3.49% |
| uup_return_5s | 0.48% |
| uup_return_21s | 3.78% |
| uso_return_5s | 4.89% |
| uso_return_21s | -2.50% |
| iau_return_5s | 0.67% |
| iau_return_21s | -4.12% |
| rsp_minus_spy_5s | 0.56% |
| rsp_minus_spy_21s | -2.47% |
| positive_asset_share_5s | 55.07% |
| positive_asset_share_21s | 31.88% |
| active_return_dispersion_5s | 21.66% |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_3s | active_return_5s | prior_16s_active_return | volatility_21s | max_drawdown_21s | volume_zscore_5v60 | corr_spy_63s | beta_spy_63s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | -0.42% | -1.63% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.04% | -0.36% | -1.70% | 0.94% | -0.26% | -0.539 | 0.049 | 0.003 | -0.16% |
| SP500 | SPY | diversified_us_equity | 0.11% | 0.00% | 0.00% | 9.72% | -1.41% | -1.371 | 1.000 | 1.000 | -0.13% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | 0.14% | -0.17% | -0.49% | 10.09% | -1.84% | -0.544 | 0.995 | 1.012 | -0.71% |
| NASDAQ100 | QQQ | technology_and_growth | -1.54% | -1.77% | 4.26% | 15.60% | -1.79% | -0.602 | 0.901 | 1.504 | -1.79% |
| LARGE_GROWTH | IWF | technology_and_growth | -1.27% | -1.37% | 3.44% | 14.48% | -1.61% | -0.157 | 0.929 | 1.481 | -1.59% |
| LARGE_VALUE | IWD | diversified_us_equity | 1.54% | 1.29% | -3.31% | 8.16% | -2.64% | -0.325 | 0.723 | 0.585 | -1.46% |
| MID_CAP | IJH | diversified_us_equity | 0.55% | -1.13% | -2.35% | 10.74% | -3.05% | -0.189 | 0.759 | 0.824 | -6.72% |
| SMALL_CAP | IWM | diversified_us_equity | 0.07% | -2.36% | -3.28% | 10.91% | -3.67% | 0.472 | 0.773 | 0.926 | -8.67% |
| SMALL_VALUE | IWN | diversified_us_equity | 0.51% | -1.44% | -4.16% | 9.68% | -4.27% | 2.051 | 0.645 | 0.645 | -6.81% |
| DIVIDEND | SCHD | diversified_us_equity | 1.87% | 1.23% | -4.97% | 10.43% | -4.51% | -0.853 | 0.193 | 0.201 | -4.78% |
| LOW_VOL | SPLV | diversified_us_equity | 2.20% | 1.97% | -5.10% | 9.25% | -4.30% | -0.867 | 0.063 | 0.056 | -6.28% |
| MOMENTUM | MTUM | diversified_us_equity | -2.27% | -2.91% | 3.83% | 17.72% | -2.88% | -0.389 | 0.594 | 1.433 | -8.54% |
| TECHNOLOGY | XLK | technology_and_growth | -2.50% | -2.70% | 5.56% | 18.37% | -2.79% | -0.448 | 0.774 | 1.776 | -2.79% |
| COMMUNICATIONS | XLC | technology_and_growth | 0.17% | -0.57% | -2.20% | 21.59% | -4.19% | 0.228 | 0.385 | 0.733 | -6.35% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | 0.82% | 1.25% | -3.67% | 13.85% | -3.46% | -0.350 | 0.661 | 1.144 | -9.28% |
| CONSUMER_STAPLES | XLP | consumer_defensive | 3.32% | 3.74% | -3.80% | 13.84% | -4.22% | -0.009 | -0.012 | -0.016 | -4.41% |
| HEALTHCARE | XLV | healthcare_and_biotech | 1.88% | 2.34% | -0.03% | 12.29% | -2.97% | -0.160 | 0.060 | 0.092 | -1.73% |
| FINANCIALS | XLF | financials | 2.42% | 1.75% | -7.19% | 12.55% | -6.40% | -0.082 | 0.551 | 0.614 | -5.66% |
| INDUSTRIALS | XLI | industrials_and_defense | 0.78% | -0.98% | -2.68% | 13.40% | -2.87% | -0.409 | 0.590 | 0.804 | -9.07% |
| ENERGY | XLE | energy | 4.18% | 3.61% | -3.63% | 22.36% | -6.15% | 0.084 | -0.287 | -0.546 | 0.00% |
| MATERIALS | XLB | materials_and_mining | 0.94% | -0.54% | -4.03% | 13.80% | -4.29% | -0.478 | 0.378 | 0.559 | -7.46% |
| UTILITIES | XLU | rate_sensitive_defensive | 1.17% | 3.73% | -6.64% | 17.32% | -6.72% | 0.785 | 0.166 | 0.228 | -10.97% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | 3.33% | 2.65% | -7.18% | 13.44% | -5.79% | 1.704 | 0.240 | 0.288 | -8.13% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | 0.36% | 0.15% | -3.93% | 5.91% | -2.55% | 0.051 | 0.480 | 0.223 | -6.59% |
| LONG_TREASURY | TLT | rates_and_duration | 1.17% | 0.80% | -6.28% | 10.35% | -5.73% | -0.186 | 0.429 | 0.391 | -11.75% |
| TIPS | TIP | rates_and_duration | 0.25% | 0.08% | -3.39% | 4.67% | -1.76% | -0.246 | 0.260 | 0.091 | -3.47% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | 0.47% | 0.31% | -4.02% | 6.53% | -3.17% | -0.574 | 0.539 | 0.288 | -5.64% |
| HIGH_YIELD_CREDIT | HYG | credit | 0.14% | -0.02% | -3.69% | 4.14% | -2.31% | 0.033 | 0.686 | 0.211 | -2.76% |
| AGGREGATE_BONDS | AGG | rates_and_duration | 0.37% | 0.14% | -3.56% | 4.97% | -2.28% | 0.586 | 0.494 | 0.195 | -4.43% |
| DEVELOPED_EX_US | VEA | international_equity | -0.44% | -2.08% | -3.53% | 14.24% | -3.92% | 0.151 | 0.771 | 1.034 | -4.97% |
| EMERGING_MARKETS | VWO | international_equity | -0.20% | -1.87% | -1.01% | 15.70% | -3.45% | -0.012 | 0.803 | 1.064 | -2.60% |
| EUROPE | VGK | international_equity | 0.30% | -0.96% | -5.54% | 13.05% | -4.86% | 0.743 | 0.706 | 0.788 | -7.68% |
| JAPAN | EWJ | international_equity | -1.02% | -2.42% | -0.88% | 16.67% | -3.01% | -0.491 | 0.702 | 1.253 | -2.01% |
| CHINA | MCHI | international_equity | 0.99% | -0.67% | -2.91% | 18.20% | -5.55% | -0.145 | 0.325 | 0.491 | -18.98% |
| INDIA | INDA | international_equity | 0.54% | -0.87% | -5.75% | 13.68% | -6.20% | -0.194 | 0.588 | 0.682 | -16.15% |
| GOLD | IAU | precious_metals | 1.66% | 0.25% | -6.39% | 20.76% | -6.29% | -0.724 | 0.348 | 0.764 | -22.87% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | 2.32% | 2.75% | -4.36% | 16.70% | -5.02% | -0.308 | -0.475 | -0.898 | -1.19% |
| SEMICONDUCTORS | SMH | technology_and_growth | -5.45% | -7.19% | 9.87% | 31.73% | -6.77% | -0.259 | 0.652 | 2.232 | -11.65% |
| SOFTWARE | IGV | technology_and_growth | 1.31% | 1.00% | 6.45% | 26.14% | -2.66% | -1.054 | 0.497 | 1.489 | -4.94% |
| BROAD_AI_TECH | AIQ | technology_and_growth | -1.12% | -1.81% | 2.86% | 19.85% | -3.01% | -0.453 | 0.821 | 1.917 | -6.02% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | -2.71% | -3.79% | 2.06% | 23.22% | -4.40% | -0.084 | 0.827 | 2.190 | -15.45% |
| CYBERSECURITY | CIBR | technology_and_growth | 1.15% | 1.27% | 10.67% | 31.50% | -2.94% | 0.441 | 0.430 | 1.292 | -2.00% |
| SOLAR | TAN | clean_energy | -0.11% | -0.86% | -9.01% | 32.08% | -8.80% | -0.437 | 0.683 | 2.095 | -41.19% |
| METALS_MINING | XME | materials_and_mining | 0.01% | -3.12% | -6.73% | 28.16% | -8.80% | -1.083 | 0.583 | 1.935 | -20.96% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | 1.23% | 0.56% | -3.01% | 8.63% | -2.89% | 0.670 | 0.659 | 0.599 | -3.94% |
| BIOTECH | XBI | healthcare_and_biotech | 0.78% | -3.49% | -1.64% | 29.17% | -7.77% | 1.401 | 0.345 | 0.923 | -10.70% |
| REGIONAL_BANKS | KRE | financials | 0.97% | -1.60% | -5.83% | 14.60% | -6.51% | 0.276 | 0.325 | 0.469 | -10.23% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | 1.19% | -0.88% | -7.01% | 14.51% | -6.93% | 0.214 | 0.450 | 0.829 | -18.54% |
| CANADA | EWC | international_equity | 2.61% | 0.72% | -4.60% | 13.72% | -4.64% | 0.031 | 0.612 | 0.718 | -5.09% |
| UNITED_KINGDOM | EWU | international_equity | 1.68% | 0.68% | -5.28% | 11.94% | -4.30% | -0.373 | 0.466 | 0.476 | -5.45% |
| AUSTRALIA | EWA | international_equity | 1.56% | 0.42% | -4.50% | 17.17% | -4.37% | -0.272 | 0.648 | 0.965 | -5.78% |
| SOUTH_KOREA | EWY | international_equity | -7.39% | -11.57% | -0.18% | 45.93% | -11.69% | -0.563 | 0.549 | 2.813 | -22.40% |
| TAIWAN | EWT | international_equity | -1.69% | -3.58% | 4.76% | 27.75% | -3.95% | -0.091 | 0.730 | 2.132 | -3.16% |
| BRAZIL | EWZ | international_equity | 2.76% | 0.88% | 10.91% | 48.10% | -5.36% | 0.836 | 0.293 | 0.898 | 0.00% |
| MEXICO | EWW | international_equity | 1.76% | 1.48% | -6.29% | 20.48% | -7.44% | -0.048 | 0.574 | 0.902 | -8.52% |
| SOUTH_AFRICA | EZA | international_equity | 2.38% | 0.53% | -11.52% | 25.30% | -11.14% | -0.452 | 0.562 | 1.405 | -20.20% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | 0.68% | 0.41% | -4.14% | 6.94% | -2.96% | 0.057 | 0.483 | 0.246 | -4.97% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | 0.64% | -0.38% | -3.62% | 5.77% | -2.80% | 1.601 | 0.406 | 0.170 | -5.44% |
| EMERGING_MARKET_BONDS | EMB | credit | 0.33% | 0.40% | -4.84% | 7.24% | -3.88% | 0.667 | 0.663 | 0.358 | -4.71% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | 0.30% | -0.04% | -2.06% | 3.52% | -0.99% | 0.168 | 0.599 | 0.200 | -2.95% |
| SILVER | SLV | precious_metals | 0.98% | -1.84% | -6.77% | 34.49% | -11.99% | -0.336 | 0.445 | 1.534 | -48.53% |
| COPPER | CPER | non_energy_commodities | 2.06% | 1.51% | 0.11% | 21.85% | -4.76% | -0.520 | 0.486 | 1.021 | -1.93% |
| AGRICULTURE | DBA | non_energy_commodities | -0.18% | -0.49% | -3.26% | 12.55% | -2.87% | -0.216 | 0.117 | 0.141 | -3.56% |
| OIL | USO | energy | 4.95% | 4.47% | -8.67% | 40.11% | -11.44% | -1.075 | -0.557 | -2.510 | -6.69% |
| US_DOLLAR | UUP | currencies | 0.31% | 0.06% | 1.65% | 4.65% | -0.31% | -0.316 | -0.278 | -0.134 | 0.00% |
| EURO | FXE | currencies | -0.33% | -1.00% | -4.83% | 4.69% | -3.76% | 0.700 | 0.230 | 0.100 | -6.80% |
| YEN | FXY | currencies | -0.36% | -0.84% | -4.41% | 6.06% | -3.35% | -0.795 | 0.365 | 0.331 | -5.51% |
| BITCOIN_ETF | IBIT | crypto_assets | -0.74% | -3.92% | 9.31% | 38.77% | -5.61% | -0.471 | 0.342 | 1.161 | -29.21% |
| ETHEREUM_ETF | ETHA | crypto_assets | -1.98% | 178.33% | 5.00% | 687.49% | -8.52% | -0.979 | 0.122 | 4.472 | -6.47% |
