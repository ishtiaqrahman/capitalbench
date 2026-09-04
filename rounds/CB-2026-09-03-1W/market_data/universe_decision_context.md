# Full-Universe Horizon-Specific Decision Context

Profile: weekly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: tiingo_eod_adjusted_price_and_volume
- As-of date requested: 2026-09-03
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | 0.27% |
| spy_return_21s | 0.44% |
| rsp_return_5s | -0.63% |
| rsp_return_21s | 0.15% |
| hyg_return_5s | -0.28% |
| hyg_return_21s | 0.16% |
| tlt_return_5s | -0.90% |
| tlt_return_21s | -0.74% |
| uup_return_5s | -0.04% |
| uup_return_21s | -0.28% |
| uso_return_5s | 9.29% |
| uso_return_21s | 23.69% |
| iau_return_5s | -2.91% |
| iau_return_21s | 5.32% |
| rsp_minus_spy_5s | -0.90% |
| rsp_minus_spy_21s | -0.29% |
| positive_asset_share_5s | 40.58% |
| positive_asset_share_21s | 55.07% |
| active_return_dispersion_5s | 2.20% |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_3s | active_return_5s | prior_16s_active_return | volatility_21s | max_drawdown_21s | volume_zscore_5v60 | corr_spy_63s | beta_spy_63s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | -0.27% | -0.17% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.04% | -0.19% | 0.05% | 0.16% | 0.00% | 0.424 | -0.110 | -0.002 | 0.00% |
| SP500 | SPY | diversified_us_equity | 0.80% | 0.00% | 0.00% | 8.10% | -2.07% | -0.838 | 1.000 | 1.000 | -0.61% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | 0.74% | -0.19% | 0.09% | 8.56% | -2.38% | -0.588 | 0.993 | 0.988 | -0.88% |
| NASDAQ100 | QQQ | technology_and_growth | 0.13% | -0.75% | 0.36% | 13.26% | -3.52% | -0.779 | 0.926 | 1.726 | -3.71% |
| LARGE_GROWTH | IWF | technology_and_growth | 0.59% | -0.64% | -0.17% | 13.86% | -3.68% | -0.382 | 0.905 | 1.397 | -4.06% |
| LARGE_VALUE | IWD | diversified_us_equity | 0.96% | 0.43% | 0.40% | 7.69% | -1.09% | -0.387 | 0.705 | 0.572 | 0.00% |
| MID_CAP | IJH | diversified_us_equity | 0.53% | -1.44% | -0.62% | 11.72% | -5.17% | -0.693 | 0.798 | 0.804 | -3.71% |
| SMALL_CAP | IWM | diversified_us_equity | 0.43% | -1.81% | -0.16% | 12.59% | -4.76% | -0.338 | 0.794 | 0.943 | -3.24% |
| SMALL_VALUE | IWN | diversified_us_equity | 0.87% | -0.72% | -0.32% | 9.79% | -3.29% | -0.009 | 0.670 | 0.626 | -1.63% |
| DIVIDEND | SCHD | diversified_us_equity | 0.54% | 0.45% | 3.37% | 9.09% | -1.14% | -0.108 | 0.109 | 0.091 | -0.37% |
| LOW_VOL | SPLV | diversified_us_equity | 0.74% | -0.11% | -1.57% | 8.32% | -2.20% | -0.244 | -0.275 | -0.250 | -3.32% |
| MOMENTUM | MTUM | diversified_us_equity | -0.31% | -1.85% | -2.03% | 19.03% | -7.93% | -1.165 | 0.718 | 1.954 | -13.27% |
| TECHNOLOGY | XLK | technology_and_growth | -0.28% | -1.67% | 1.28% | 20.89% | -5.62% | -0.864 | 0.842 | 2.113 | -6.06% |
| COMMUNICATIONS | XLC | technology_and_growth | 1.72% | 1.50% | 0.32% | 15.86% | -2.19% | -0.892 | 0.397 | 0.568 | -5.03% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | -0.11% | 0.23% | -2.50% | 16.46% | -4.40% | -0.977 | 0.688 | 1.077 | -6.10% |
| CONSUMER_STAPLES | XLP | consumer_defensive | 0.33% | -0.06% | -0.46% | 14.23% | -2.82% | -0.824 | -0.284 | -0.354 | -4.08% |
| HEALTHCARE | XLV | healthcare_and_biotech | 1.59% | 0.71% | 4.35% | 18.13% | -2.93% | -1.043 | -0.150 | -0.201 | -1.38% |
| FINANCIALS | XLF | financials | 1.47% | 0.91% | -0.38% | 11.57% | -2.25% | -0.477 | 0.308 | 0.281 | 0.00% |
| INDUSTRIALS | XLI | industrials_and_defense | -0.33% | -2.64% | -4.22% | 12.02% | -7.39% | 0.924 | 0.657 | 0.890 | -6.41% |
| ENERGY | XLE | energy | 1.03% | 3.47% | 8.52% | 21.55% | -2.65% | -0.538 | -0.335 | -0.546 | -0.74% |
| MATERIALS | XLB | materials_and_mining | -0.13% | -1.41% | 0.95% | 15.41% | -2.98% | 0.883 | 0.417 | 0.596 | -1.96% |
| UTILITIES | XLU | rate_sensitive_defensive | 1.89% | -0.62% | -1.27% | 13.98% | -4.69% | 1.755 | -0.113 | -0.120 | -8.65% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | 0.32% | -1.19% | -1.36% | 12.32% | -3.59% | 0.559 | -0.158 | -0.175 | -3.83% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | -0.14% | -0.93% | -0.26% | 4.75% | -1.15% | 0.097 | 0.440 | 0.154 | -3.62% |
| LONG_TREASURY | TLT | rates_and_duration | -0.16% | -1.16% | -0.01% | 10.36% | -1.99% | 0.005 | 0.317 | 0.222 | -7.21% |
| TIPS | TIP | rates_and_duration | 0.17% | -0.68% | 0.24% | 3.59% | -0.77% | -0.026 | 0.382 | 0.099 | -1.16% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | -0.25% | -1.00% | -0.18% | 5.72% | -1.12% | -0.352 | 0.517 | 0.202 | -2.96% |
| HIGH_YIELD_CREDIT | HYG | credit | -0.21% | -0.55% | 0.27% | 2.56% | -0.48% | 0.471 | 0.802 | 0.177 | -0.34% |
| AGGREGATE_BONDS | AGG | rates_and_duration | -0.13% | -0.82% | -0.05% | 4.11% | -0.92% | 0.527 | 0.483 | 0.141 | -2.11% |
| DEVELOPED_EX_US | VEA | international_equity | 0.71% | -0.24% | 1.31% | 11.89% | -2.28% | -0.613 | 0.811 | 1.112 | -0.47% |
| EMERGING_MARKETS | VWO | international_equity | 0.78% | -0.30% | 1.50% | 9.16% | -1.37% | -0.747 | 0.850 | 1.135 | -0.41% |
| EUROPE | VGK | international_equity | 0.09% | -0.85% | 0.30% | 8.31% | -2.65% | -0.268 | 0.744 | 0.753 | -1.56% |
| JAPAN | EWJ | international_equity | 2.11% | 1.88% | 0.54% | 16.86% | -4.27% | 0.335 | 0.766 | 1.328 | -0.58% |
| CHINA | MCHI | international_equity | -0.64% | -1.23% | -2.15% | 13.54% | -4.50% | -0.662 | 0.420 | 0.516 | -17.30% |
| INDIA | INDA | international_equity | 0.44% | 0.52% | -1.72% | 9.17% | -2.02% | -0.462 | 0.565 | 0.522 | -9.71% |
| GOLD | IAU | precious_metals | 0.47% | -3.18% | 8.31% | 27.08% | -7.30% | -0.193 | 0.492 | 0.979 | -17.20% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | 2.36% | 3.37% | 8.31% | 18.09% | -2.57% | 0.020 | -0.181 | -0.288 | 0.00% |
| SEMICONDUCTORS | SMH | technology_and_growth | -0.72% | -3.83% | 0.41% | 29.82% | -8.22% | -0.968 | 0.763 | 2.926 | -17.39% |
| SOFTWARE | IGV | technology_and_growth | -2.76% | -3.32% | 8.72% | 40.99% | -6.25% | -0.516 | 0.505 | 1.250 | -9.19% |
| BROAD_AI_TECH | AIQ | technology_and_growth | 0.00% | -0.64% | 3.33% | 20.26% | -3.59% | -0.861 | 0.844 | 2.342 | -8.33% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | 0.25% | -1.36% | 1.27% | 25.66% | -7.91% | -0.921 | 0.872 | 2.358 | -14.61% |
| CYBERSECURITY | CIBR | technology_and_growth | -4.82% | -5.70% | 3.13% | 41.05% | -9.53% | 0.557 | 0.569 | 1.360 | -6.73% |
| SOLAR | TAN | clean_energy | 0.32% | -4.33% | -3.15% | 24.77% | -11.17% | -0.563 | 0.794 | 2.413 | -35.45% |
| METALS_MINING | XME | materials_and_mining | 0.21% | -4.02% | 9.73% | 38.40% | -5.88% | -0.785 | 0.644 | 1.895 | -10.82% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | 0.30% | -0.90% | 0.61% | 9.00% | -2.33% | -0.817 | 0.692 | 0.559 | -1.22% |
| BIOTECH | XBI | healthcare_and_biotech | 1.16% | -2.56% | 9.78% | 32.05% | -4.23% | -0.403 | 0.327 | 0.721 | -3.05% |
| REGIONAL_BANKS | KRE | financials | 1.78% | 0.43% | -4.04% | 15.33% | -6.81% | -0.056 | 0.170 | 0.211 | -3.93% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | -1.04% | -3.80% | -7.31% | 19.14% | -11.79% | 0.079 | 0.436 | 0.763 | -10.76% |
| CANADA | EWC | international_equity | 1.69% | 0.07% | 2.26% | 12.49% | -3.26% | -0.234 | 0.614 | 0.536 | -0.27% |
| UNITED_KINGDOM | EWU | international_equity | 0.64% | -0.17% | 0.37% | 8.18% | -2.43% | 0.341 | 0.403 | 0.367 | -1.44% |
| AUSTRALIA | EWA | international_equity | 1.17% | 0.60% | -0.27% | 12.79% | -2.83% | 0.694 | 0.601 | 0.730 | -0.20% |
| SOUTH_KOREA | EWY | international_equity | -0.17% | -1.14% | 7.52% | 46.27% | -8.13% | -1.172 | 0.687 | 3.799 | -17.63% |
| TAIWAN | EWT | international_equity | 1.94% | 1.11% | 6.64% | 20.34% | -4.15% | -0.847 | 0.784 | 2.338 | -1.26% |
| BRAZIL | EWZ | international_equity | 5.83% | 6.36% | -1.14% | 25.14% | -6.67% | 1.446 | 0.349 | 0.563 | -7.75% |
| MEXICO | EWW | international_equity | 0.33% | -0.51% | 0.44% | 15.12% | -3.95% | -0.323 | 0.609 | 0.832 | -3.86% |
| SOUTH_AFRICA | EZA | international_equity | 1.87% | 0.09% | 6.88% | 29.99% | -4.10% | 0.360 | 0.693 | 1.533 | -10.12% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | -0.11% | -0.82% | 0.02% | 4.58% | -1.09% | 0.146 | 0.491 | 0.167 | -1.98% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | -0.77% | -1.31% | -0.58% | 3.02% | -1.76% | 1.920 | 0.503 | 0.109 | -2.79% |
| EMERGING_MARKET_BONDS | EMB | credit | 0.10% | -0.55% | -0.21% | 4.86% | -0.92% | 0.548 | 0.725 | 0.282 | -1.18% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | -0.06% | -0.64% | -0.77% | 3.73% | -1.29% | 0.408 | 0.491 | 0.128 | -2.07% |
| SILVER | SLV | precious_metals | 0.70% | -3.81% | 11.78% | 38.50% | -7.73% | 0.056 | 0.565 | 1.848 | -42.66% |
| COPPER | CPER | non_energy_commodities | -0.23% | -0.44% | -2.30% | 19.12% | -4.36% | -0.345 | 0.635 | 1.118 | -2.30% |
| AGRICULTURE | DBA | non_energy_commodities | -0.78% | 0.67% | 4.14% | 11.54% | -1.36% | 2.649 | 0.105 | 0.099 | -1.36% |
| OIL | USO | energy | 6.28% | 9.02% | 13.00% | 40.03% | -6.31% | -0.511 | -0.323 | -1.219 | -7.11% |
| US_DOLLAR | UUP | currencies | -0.39% | -0.30% | -0.42% | 5.40% | -1.13% | -0.496 | -0.403 | -0.156 | -2.06% |
| EURO | FXE | currencies | 0.11% | -0.43% | 0.73% | 4.68% | -0.76% | -0.427 | 0.400 | 0.145 | -2.92% |
| YEN | FXY | currencies | 2.58% | 2.11% | -1.29% | 10.11% | -1.79% | 0.305 | 0.302 | 0.198 | -6.29% |
| BITCOIN_ETF | IBIT | crypto_assets | 3.76% | 2.07% | 23.10% | 43.82% | -3.38% | 0.363 | 0.408 | 1.187 | -34.98% |
| ETHEREUM_ETF | ETHA | crypto_assets | 1.60% | 0.53% | 30.15% | 56.05% | -4.35% | 0.182 | 0.446 | 1.870 | -46.86% |
