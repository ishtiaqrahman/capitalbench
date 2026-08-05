# Full-Universe Horizon-Specific Decision Context

Profile: monthly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: yahoo_chart_adjusted_close_and_reported_volume
- As-of date requested: 2026-08-04
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | 4.11% |
| spy_return_21s | 2.67% |
| rsp_return_5s | 1.17% |
| rsp_return_21s | 2.43% |
| hyg_return_5s | 0.65% |
| hyg_return_21s | 0.08% |
| tlt_return_5s | -1.29% |
| tlt_return_21s | -2.69% |
| uup_return_5s | -1.47% |
| uup_return_21s | -0.56% |
| uso_return_5s | -3.91% |
| uso_return_21s | 10.95% |
| iau_return_5s | 1.31% |
| iau_return_21s | -2.06% |
| rsp_minus_spy_5s | -2.95% |
| rsp_minus_spy_21s | -0.24% |
| positive_asset_share_5s | 79.71% |
| positive_asset_share_21s | 65.22% |
| active_return_dispersion_5s |  |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_5s | active_return_21s | prior_105s_active_return | volatility_63s | max_drawdown_63s | volume_zscore_20v120 | corr_spy_252s | beta_spy_252s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | -2.67% | -8.61% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.07% | -2.38% | -7.12% | 0.21% | -0.01% | -0.283 | -0.098 | -0.002 | 0.00% |
| SP500 | SPY | diversified_us_equity | 4.11% | 0.00% | 0.00% | 14.29% | -4.49% | -0.864 | 1.000 | 1.000 | 0.00% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | 4.05% | -0.21% | 0.57% | 14.21% | -4.36% | -0.776 | 0.995 | 1.012 | 0.00% |
| NASDAQ100 | QQQ | technology_and_growth | 7.16% | -2.53% | 7.10% | 26.51% | -11.22% | -0.741 | 0.932 | 1.411 | -2.88% |
| LARGE_GROWTH | IWF | technology_and_growth | 6.71% | -1.61% | -3.18% | 21.25% | -11.35% | -0.771 | 0.938 | 1.283 | -3.39% |
| LARGE_VALUE | IWD | diversified_us_equity | 1.82% | 1.13% | 3.70% | 11.84% | -2.40% | -0.645 | 0.804 | 0.700 | 0.00% |
| MID_CAP | IJH | diversified_us_equity | 1.91% | -1.28% | 2.28% | 14.94% | -4.25% | -0.922 | 0.802 | 0.976 | 0.00% |
| SMALL_CAP | IWM | diversified_us_equity | 2.84% | -1.73% | 5.87% | 18.78% | -4.81% | -1.073 | 0.814 | 1.219 | 0.00% |
| SMALL_VALUE | IWN | diversified_us_equity | 1.28% | -0.31% | 5.31% | 15.21% | -4.01% | -0.489 | 0.727 | 0.969 | 0.00% |
| DIVIDEND | SCHD | diversified_us_equity | -0.12% | 2.33% | 0.63% | 11.59% | -2.95% | -0.052 | 0.294 | 0.251 | -0.12% |
| LOW_VOL | SPLV | diversified_us_equity | -2.03% | -2.19% | -4.11% | 13.26% | -3.75% | -0.829 | 0.028 | 0.023 | -2.03% |
| MOMENTUM | MTUM | diversified_us_equity | 7.19% | -5.27% | 16.16% | 39.66% | -17.99% | 1.296 | 0.780 | 1.552 | -9.23% |
| TECHNOLOGY | XLK | technology_and_growth | 9.24% | -0.85% | 18.07% | 36.41% | -15.86% | -0.979 | 0.860 | 1.723 | -5.59% |
| COMMUNICATIONS | XLC | technology_and_growth | 2.16% | -1.01% | -15.98% | 19.06% | -9.99% | -0.258 | 0.591 | 0.684 | -6.15% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | 5.17% | -2.43% | -11.47% | 22.05% | -10.72% | -0.313 | 0.778 | 1.167 | -4.62% |
| CONSUMER_STAPLES | XLP | consumer_defensive | -1.94% | -1.16% | -7.83% | 17.19% | -4.95% | -0.766 | -0.062 | -0.068 | -3.96% |
| HEALTHCARE | XLV | healthcare_and_biotech | -3.09% | -2.58% | -3.69% | 18.30% | -3.74% | -0.675 | 0.233 | 0.281 | -3.09% |
| FINANCIALS | XLF | financials | 0.49% | 0.43% | -3.80% | 13.64% | -2.08% | -0.735 | 0.553 | 0.627 | 0.00% |
| INDUSTRIALS | XLI | industrials_and_defense | 2.14% | -2.22% | 2.74% | 19.71% | -4.80% | -1.008 | 0.721 | 0.947 | 0.00% |
| ENERGY | XLE | energy | 1.65% | 7.48% | -0.99% | 24.16% | -13.21% | -0.890 | -0.154 | -0.250 | -5.78% |
| MATERIALS | XLB | materials_and_mining | -0.65% | -2.63% | -3.06% | 20.85% | -6.43% | -0.613 | 0.538 | 0.737 | -2.23% |
| UTILITIES | XLU | rate_sensitive_defensive | -3.10% | -5.30% | -0.89% | 16.43% | -7.05% | -0.797 | 0.132 | 0.153 | -6.34% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | -1.83% | -0.68% | 1.20% | 15.93% | -3.38% | -0.815 | 0.231 | 0.252 | -1.83% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | 0.01% | -3.32% | -8.32% | 5.06% | -2.00% | -0.961 | 0.286 | 0.100 | -2.96% |
| LONG_TREASURY | TLT | rates_and_duration | -1.29% | -5.36% | -8.03% | 9.45% | -5.60% | -0.529 | 0.229 | 0.163 | -6.72% |
| TIPS | TIP | rates_and_duration | 0.16% | -3.27% | -7.53% | 3.44% | -1.53% | -0.588 | 0.278 | 0.071 | -1.12% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | 0.37% | -4.00% | -8.00% | 5.45% | -2.83% | -0.321 | 0.476 | 0.193 | -2.21% |
| HIGH_YIELD_CREDIT | HYG | credit | 0.65% | -2.59% | -7.25% | 3.61% | -1.01% | -0.644 | 0.780 | 0.233 | 0.00% |
| AGGREGATE_BONDS | AGG | rates_and_duration | 0.08% | -3.34% | -7.99% | 4.19% | -1.71% | -0.336 | 0.394 | 0.113 | -1.74% |
| DEVELOPED_EX_US | VEA | international_equity | 3.76% | -2.21% | 0.32% | 21.06% | -4.85% | -0.776 | 0.804 | 1.073 | -0.23% |
| EMERGING_MARKETS | VWO | international_equity | 4.00% | -2.70% | -2.69% | 20.93% | -7.05% | -0.518 | 0.807 | 1.099 | -1.94% |
| EUROPE | VGK | international_equity | 2.93% | -0.59% | -4.73% | 17.47% | -3.86% | -0.910 | 0.746 | 0.914 | 0.00% |
| JAPAN | EWJ | international_equity | 5.32% | -3.36% | 2.92% | 23.69% | -7.86% | -0.860 | 0.724 | 1.174 | -2.43% |
| CHINA | MCHI | international_equity | 3.09% | 5.16% | -23.61% | 20.86% | -15.01% | -0.511 | 0.550 | 0.872 | -14.69% |
| INDIA | INDA | international_equity | 2.33% | -1.37% | -14.99% | 15.84% | -5.64% | -0.527 | 0.530 | 0.619 | -8.61% |
| GOLD | IAU | precious_metals | 1.31% | -4.72% | -19.19% | 23.74% | -16.01% | -0.603 | 0.317 | 0.682 | -24.50% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | -0.94% | 2.30% | 6.64% | 22.51% | -16.55% | 0.167 | -0.172 | -0.261 | -10.63% |
| SEMICONDUCTORS | SMH | technology_and_growth | 8.71% | -7.40% | 39.52% | 56.20% | -24.62% | 0.791 | 0.785 | 2.350 | -13.93% |
| SOFTWARE | IGV | technology_and_growth | 11.14% | 4.94% | -2.70% | 34.39% | -21.29% | -0.888 | 0.513 | 1.170 | -13.39% |
| BROAD_AI_TECH | AIQ | technology_and_growth | 10.29% | -3.78% | 13.27% | 41.28% | -20.19% | -0.113 | 0.848 | 1.890 | -9.99% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | 9.90% | -6.73% | -2.40% | 40.33% | -23.82% | -0.832 | 0.803 | 2.173 | -13.20% |
| CYBERSECURITY | CIBR | technology_and_growth | 9.70% | 2.75% | 25.25% | 33.23% | -11.74% | -0.350 | 0.544 | 1.104 | 0.00% |
| SOLAR | TAN | clean_energy | 8.70% | -9.92% | -1.44% | 47.26% | -35.51% | -0.492 | 0.601 | 1.833 | -27.81% |
| METALS_MINING | XME | materials_and_mining | 6.33% | -0.99% | -19.06% | 41.73% | -26.49% | -0.575 | 0.604 | 1.732 | -18.74% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | 1.17% | -0.24% | 0.26% | 11.19% | -2.04% | -0.803 | 0.769 | 0.699 | 0.00% |
| BIOTECH | XBI | healthcare_and_biotech | 1.40% | -8.22% | 17.79% | 31.11% | -10.51% | -0.281 | 0.482 | 1.009 | -7.55% |
| REGIONAL_BANKS | KRE | financials | 1.37% | 0.35% | 0.53% | 19.83% | -5.29% | -0.597 | 0.438 | 0.772 | -0.10% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | 2.31% | -2.72% | 0.03% | 25.96% | -8.58% | -0.426 | 0.574 | 1.004 | -0.05% |
| CANADA | EWC | international_equity | 0.27% | 0.67% | -1.67% | 11.93% | -3.20% | -0.633 | 0.674 | 0.747 | 0.00% |
| UNITED_KINGDOM | EWU | international_equity | 1.09% | -0.30% | -5.69% | 16.15% | -3.94% | -0.404 | 0.605 | 0.698 | -0.70% |
| AUSTRALIA | EWA | international_equity | 2.73% | 3.65% | -5.82% | 18.65% | -6.84% | -0.841 | 0.678 | 0.926 | 0.00% |
| SOUTH_KOREA | EWY | international_equity | 13.00% | -12.52% | 48.38% | 83.79% | -34.21% | 0.606 | 0.643 | 2.709 | -21.93% |
| TAIWAN | EWT | international_equity | 8.79% | -7.39% | 46.99% | 45.10% | -19.83% | 0.119 | 0.755 | 1.812 | -8.36% |
| BRAZIL | EWZ | international_equity | 0.11% | 0.68% | -14.48% | 23.59% | -15.56% | -0.978 | 0.507 | 0.983 | -12.69% |
| MEXICO | EWW | international_equity | 0.36% | -1.84% | -5.79% | 20.46% | -7.30% | -0.853 | 0.533 | 0.906 | -3.74% |
| SOUTH_AFRICA | EZA | international_equity | 6.42% | -0.61% | -18.44% | 32.85% | -14.17% | -0.492 | 0.634 | 1.593 | -17.40% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | -0.03% | -3.35% | -7.85% | 5.02% | -1.93% | -0.333 | 0.390 | 0.131 | -1.67% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | 0.04% | -4.08% | -7.35% | 3.13% | -2.15% | 0.460 | 0.367 | 0.083 | -1.42% |
| EMERGING_MARKET_BONDS | EMB | credit | 0.47% | -3.41% | -6.20% | 5.91% | -2.10% | -0.580 | 0.685 | 0.302 | -0.81% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | 0.21% | -2.94% | -7.90% | 4.24% | -1.44% | -0.634 | 0.454 | 0.124 | -1.14% |
| SILVER | SLV | precious_metals | 4.14% | -6.71% | -31.15% | 50.01% | -36.50% | -0.625 | 0.356 | 1.687 | -49.02% |
| COPPER | CPER | non_energy_commodities | 4.72% | 3.41% | -3.15% | 29.03% | -10.57% | -0.587 | 0.558 | 1.206 | -1.13% |
| AGRICULTURE | DBA | non_energy_commodities | -0.65% | -2.23% | -1.24% | 14.11% | -8.67% | -0.478 | 0.077 | 0.066 | -3.72% |
| OIL | USO | energy | -3.91% | 8.28% | 29.92% | 54.61% | -32.49% | -0.518 | -0.335 | -1.228 | -24.31% |
| US_DOLLAR | UUP | currencies | -1.47% | -3.23% | -3.68% | 5.02% | -1.61% | -0.219 | -0.315 | -0.140 | -1.54% |
| EURO | FXE | currencies | 1.28% | -1.83% | -11.28% | 4.87% | -3.57% | -0.911 | 0.299 | 0.133 | -3.82% |
| YEN | FXY | currencies | 3.84% | 0.09% | -12.82% | 7.47% | -4.58% | 1.009 | 0.186 | 0.116 | -7.43% |
| BITCOIN_ETF | IBIT | crypto_assets | 0.69% | -1.92% | -26.93% | 36.88% | -28.36% | -0.639 | 0.505 | 1.731 | -48.95% |
| ETHEREUM_ETF | ETHA | crypto_assets | -2.35% | 1.76% | -31.18% | 52.83% | -34.41% | -0.417 | 0.540 | 2.799 | -61.33% |
