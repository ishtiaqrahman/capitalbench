# Full-Universe Horizon-Specific Decision Context

Profile: weekly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: tiingo_eod_history_through_2026-09-25; repository_daily_price_snapshots_2026-09-28_to_2026-09-30_(tiingo_eod_or_yahoo_chart_adjclose); yahoo_chart_reported_volume_2026-09-28_to_2026-09-30
- As-of date requested: 2026-09-30
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | -0.67% |
| spy_return_21s | -0.33% |
| rsp_return_5s | -1.56% |
| rsp_return_21s | -4.83% |
| hyg_return_5s | -1.14% |
| hyg_return_21s | -2.73% |
| tlt_return_5s | -3.33% |
| tlt_return_21s | -5.38% |
| uup_return_5s | 0.42% |
| uup_return_21s | 2.31% |
| uso_return_5s | -2.13% |
| uso_return_21s | 8.95% |
| iau_return_5s | -3.01% |
| iau_return_21s | -6.70% |
| rsp_minus_spy_5s | -0.88% |
| rsp_minus_spy_21s | -4.50% |
| positive_asset_share_5s | 13.04% |
| positive_asset_share_21s | 26.09% |
| active_return_dispersion_5s | 1.34% |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_3s | active_return_5s | prior_16s_active_return | volatility_21s | max_drawdown_21s | volume_zscore_5v60 | corr_spy_63s | beta_spy_63s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | 0.67% | -0.35% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.02% | 0.73% | -0.12% | 0.23% | -0.01% | 1.915 | 0.135 | 0.002 | -0.01% |
| SP500 | SPY | diversified_us_equity | -1.13% | 0.00% | 0.00% | 10.81% | -2.47% | -0.012 | 1.000 | 1.000 | -1.72% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | -1.46% | -0.38% | -0.33% | 11.12% | -2.54% | 0.533 | 0.995 | 1.009 | -2.62% |
| NASDAQ100 | QQQ | technology_and_growth | -0.64% | 0.48% | 3.17% | 15.92% | -2.01% | -0.473 | 0.889 | 1.565 | -1.03% |
| LARGE_GROWTH | IWF | technology_and_growth | -0.78% | 0.57% | 1.93% | 14.75% | -2.33% | -0.450 | 0.915 | 1.518 | -2.55% |
| LARGE_VALUE | IWD | diversified_us_equity | -1.59% | -0.71% | -2.13% | 9.14% | -4.06% | 0.098 | 0.653 | 0.543 | -4.06% |
| MID_CAP | IJH | diversified_us_equity | -1.42% | -0.80% | -3.13% | 9.98% | -4.85% | 1.421 | 0.792 | 0.835 | -8.26% |
| SMALL_CAP | IWM | diversified_us_equity | -1.45% | -0.75% | -4.18% | 11.75% | -5.87% | 0.656 | 0.796 | 0.944 | -8.68% |
| SMALL_VALUE | IWN | diversified_us_equity | -1.89% | -1.14% | -3.78% | 10.75% | -6.37% | 0.736 | 0.670 | 0.655 | -7.53% |
| DIVIDEND | SCHD | diversified_us_equity | -2.05% | -1.58% | -4.20% | 9.23% | -6.53% | 0.406 | 0.145 | 0.154 | -6.87% |
| LOW_VOL | SPLV | diversified_us_equity | -1.11% | -0.50% | -4.63% | 6.90% | -6.10% | -0.777 | -0.037 | -0.036 | -9.22% |
| MOMENTUM | MTUM | diversified_us_equity | -0.36% | 0.80% | 5.39% | 19.03% | -3.10% | -0.302 | 0.604 | 1.549 | -7.89% |
| TECHNOLOGY | XLK | technology_and_growth | -0.26% | 0.88% | 4.51% | 18.52% | -2.20% | -0.353 | 0.770 | 1.862 | -1.01% |
| COMMUNICATIONS | XLC | technology_and_growth | -1.76% | -0.74% | 0.96% | 21.61% | -3.70% | 0.865 | 0.419 | 0.780 | -6.75% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | -1.56% | -0.96% | -5.24% | 15.49% | -6.44% | -0.286 | 0.669 | 1.158 | -12.05% |
| CONSUMER_STAPLES | XLP | consumer_defensive | -1.78% | -1.55% | -2.71% | 11.19% | -5.14% | 0.483 | -0.080 | -0.115 | -8.73% |
| HEALTHCARE | XLV | healthcare_and_biotech | -1.34% | 0.45% | -0.99% | 13.90% | -4.56% | -0.171 | -0.021 | -0.033 | -3.77% |
| FINANCIALS | XLF | financials | -2.63% | -1.42% | -5.51% | 13.67% | -8.49% | 0.946 | 0.530 | 0.626 | -8.49% |
| INDUSTRIALS | XLI | industrials_and_defense | -2.02% | -1.16% | -2.96% | 12.91% | -4.47% | 0.501 | 0.621 | 0.817 | -10.23% |
| ENERGY | XLE | energy | -0.87% | -0.72% | -2.24% | 18.98% | -6.15% | 0.549 | -0.362 | -0.700 | -6.15% |
| MATERIALS | XLB | materials_and_mining | -2.21% | -2.47% | -4.48% | 14.22% | -7.60% | 0.129 | 0.358 | 0.554 | -8.84% |
| UTILITIES | XLU | rate_sensitive_defensive | -0.18% | -0.11% | -5.52% | 14.28% | -9.00% | 4.029 | 0.045 | 0.059 | -15.65% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | -1.56% | -1.55% | -4.70% | 11.16% | -6.78% | 1.284 | 0.157 | 0.184 | -10.34% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | -0.77% | -0.30% | -2.75% | 6.08% | -3.35% | 0.907 | 0.551 | 0.256 | -6.72% |
| LONG_TREASURY | TLT | rates_and_duration | -1.94% | -2.66% | -2.47% | 10.20% | -5.39% | 2.631 | 0.492 | 0.440 | -12.06% |
| TIPS | TIP | rates_and_duration | -0.48% | -0.06% | -2.23% | 4.65% | -2.84% | 1.010 | 0.335 | 0.113 | -3.90% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | -1.00% | -0.97% | -2.12% | 6.91% | -3.39% | 3.005 | 0.579 | 0.312 | -6.01% |
| HIGH_YIELD_CREDIT | HYG | credit | -0.83% | -0.46% | -1.95% | 3.83% | -2.73% | 6.008 | 0.719 | 0.212 | -2.86% |
| AGGREGATE_BONDS | AGG | rates_and_duration | -0.61% | -0.24% | -2.06% | 5.12% | -2.61% | 2.020 | 0.561 | 0.223 | -4.55% |
| DEVELOPED_EX_US | VEA | international_equity | -1.71% | -0.46% | -2.16% | 15.27% | -4.03% | -0.281 | 0.784 | 1.092 | -4.07% |
| EMERGING_MARKETS | VWO | international_equity | -1.41% | -0.67% | -0.82% | 13.70% | -3.68% | 0.463 | 0.804 | 1.081 | -3.28% |
| EUROPE | VGK | international_equity | -2.06% | -0.70% | -4.09% | 12.47% | -5.15% | 2.272 | 0.704 | 0.789 | -6.62% |
| JAPAN | EWJ | international_equity | -0.48% | 1.10% | 0.87% | 18.78% | -3.01% | 0.476 | 0.720 | 1.352 | -1.34% |
| CHINA | MCHI | international_equity | -0.82% | -1.17% | -3.18% | 15.00% | -5.12% | -0.189 | 0.351 | 0.521 | -20.61% |
| INDIA | INDA | international_equity | -2.47% | -2.18% | -3.67% | 13.71% | -6.58% | -0.383 | 0.610 | 0.701 | -15.57% |
| GOLD | IAU | precious_metals | -3.17% | -2.33% | -4.16% | 24.28% | -7.85% | -0.182 | 0.387 | 0.866 | -23.11% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | -1.03% | -0.91% | 4.80% | 19.79% | -5.02% | 0.028 | -0.483 | -0.934 | -3.98% |
| SEMICONDUCTORS | SMH | technology_and_growth | 0.40% | 1.94% | 7.70% | 31.23% | -5.71% | -0.715 | 0.660 | 2.389 | -8.96% |
| SOFTWARE | IGV | technology_and_growth | 0.44% | -0.82% | -2.06% | 31.97% | -7.98% | -0.887 | 0.483 | 1.416 | -9.04% |
| BROAD_AI_TECH | AIQ | technology_and_growth | -1.23% | -0.58% | 2.28% | 21.07% | -3.01% | -0.396 | 0.804 | 2.045 | -7.10% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | -2.55% | -2.11% | 1.46% | 22.24% | -4.15% | -0.639 | 0.809 | 2.191 | -15.69% |
| CYBERSECURITY | CIBR | technology_and_growth | 2.12% | -0.21% | 3.51% | 33.59% | -6.60% | -0.206 | 0.420 | 1.255 | -0.88% |
| SOLAR | TAN | clean_energy | -0.20% | -1.72% | -5.64% | 32.38% | -12.48% | -0.572 | 0.696 | 2.258 | -40.52% |
| METALS_MINING | XME | materials_and_mining | -4.40% | -4.82% | -7.52% | 29.37% | -13.61% | -0.458 | 0.585 | 1.917 | -21.93% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | -1.46% | -0.88% | -3.67% | 9.39% | -5.11% | -0.056 | 0.637 | 0.571 | -6.27% |
| BIOTECH | XBI | healthcare_and_biotech | 1.71% | 2.27% | -4.84% | 24.48% | -6.86% | 0.199 | 0.333 | 0.871 | -7.00% |
| REGIONAL_BANKS | KRE | financials | -2.95% | -0.66% | -4.12% | 15.98% | -7.22% | 1.150 | 0.390 | 0.573 | -10.38% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | -3.10% | -2.48% | -6.56% | 13.97% | -9.16% | 0.192 | 0.472 | 0.893 | -18.08% |
| CANADA | EWC | international_equity | -2.03% | -1.45% | -3.24% | 14.37% | -6.55% | -0.131 | 0.632 | 0.678 | -6.80% |
| UNITED_KINGDOM | EWU | international_equity | -1.67% | -0.51% | -2.99% | 11.36% | -4.42% | -0.268 | 0.422 | 0.458 | -5.79% |
| AUSTRALIA | EWA | international_equity | -0.42% | 0.50% | -5.88% | 18.08% | -6.78% | 0.526 | 0.638 | 0.933 | -6.97% |
| SOUTH_KOREA | EWY | international_equity | -2.35% | -0.87% | 2.30% | 47.41% | -7.99% | -0.735 | 0.582 | 3.135 | -16.61% |
| TAIWAN | EWT | international_equity | -1.64% | 1.03% | 3.79% | 26.75% | -4.91% | -0.786 | 0.715 | 2.197 | -2.37% |
| BRAZIL | EWZ | international_equity | 1.17% | 0.35% | 3.37% | 24.62% | -6.22% | 0.493 | 0.343 | 0.703 | -9.88% |
| MEXICO | EWW | international_equity | -3.07% | -2.50% | -4.65% | 16.98% | -7.64% | 0.096 | 0.588 | 0.877 | -11.20% |
| SOUTH_AFRICA | EZA | international_equity | -3.76% | -3.03% | -6.11% | 26.23% | -10.92% | 0.159 | 0.586 | 1.454 | -19.93% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | -0.80% | -0.33% | -2.75% | 6.90% | -3.49% | 0.553 | 0.563 | 0.283 | -5.19% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | -0.07% | -0.25% | -2.99% | 5.98% | -4.32% | 3.626 | 0.446 | 0.175 | -5.50% |
| EMERGING_MARKET_BONDS | EMB | credit | -1.45% | -1.29% | -2.14% | 6.72% | -3.84% | 2.771 | 0.710 | 0.368 | -4.96% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | -0.15% | 0.53% | -1.38% | 4.26% | -1.29% | 1.586 | 0.646 | 0.228 | -3.16% |
| SILVER | SLV | precious_metals | -6.24% | -5.60% | -3.62% | 41.18% | -10.24% | 0.129 | 0.474 | 1.682 | -48.38% |
| COPPER | CPER | non_energy_commodities | -2.04% | -1.37% | 1.18% | 28.95% | -6.80% | -0.412 | 0.508 | 1.062 | -3.98% |
| AGRICULTURE | DBA | non_energy_commodities | -1.40% | -0.76% | -2.97% | 12.90% | -4.58% | -0.274 | 0.134 | 0.168 | -4.58% |
| OIL | USO | energy | -1.80% | -1.46% | 10.97% | 47.24% | -11.44% | 0.535 | -0.577 | -2.710 | -10.01% |
| US_DOLLAR | UUP | currencies | 0.52% | 1.09% | 1.54% | 4.54% | -0.82% | -0.191 | -0.309 | -0.143 | 0.00% |
| EURO | FXE | currencies | -0.57% | 0.16% | -2.28% | 3.56% | -2.59% | -0.324 | 0.263 | 0.105 | -5.39% |
| YEN | FXY | currencies | -0.10% | 1.30% | 0.51% | 11.61% | -3.38% | -0.553 | 0.363 | 0.334 | -6.85% |
| BITCOIN_ETF | IBIT | crypto_assets | -0.48% | -0.45% | 6.84% | 43.86% | -7.14% | -0.538 | 0.384 | 1.335 | -33.60% |
| ETHEREUM_ETF | ETHA | crypto_assets | -0.94% | 0.23% | 7.61% | 46.84% | -5.32% | -0.676 | 0.302 | 1.322 | -43.78% |
