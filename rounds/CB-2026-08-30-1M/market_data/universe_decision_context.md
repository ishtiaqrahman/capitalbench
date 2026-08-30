# Full-Universe Horizon-Specific Decision Context

Profile: monthly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: yahoo_chart_adjusted_close_and_reported_volume
- As-of date requested: 2026-08-28
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | 0.47% |
| spy_return_21s | 3.73% |
| rsp_return_5s | -0.44% |
| rsp_return_21s | 2.47% |
| hyg_return_5s | 0.16% |
| hyg_return_21s | 0.83% |
| tlt_return_5s | 1.01% |
| tlt_return_21s | 0.50% |
| uup_return_5s | 1.00% |
| uup_return_21s | 0.14% |
| uso_return_5s | -3.67% |
| uso_return_21s | 1.74% |
| iau_return_5s | -3.42% |
| iau_return_21s | 8.43% |
| rsp_minus_spy_5s | -0.92% |
| rsp_minus_spy_21s | -1.26% |
| positive_asset_share_5s | 40.58% |
| positive_asset_share_21s | 73.91% |
| active_return_dispersion_5s |  |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_5s | active_return_21s | prior_105s_active_return | volatility_63s | max_drawdown_63s | volume_zscore_20v120 | corr_spy_252s | beta_spy_252s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | -3.73% | -8.69% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.05% | -3.43% | -7.21% | 0.21% | -0.01% | -0.492 | -0.115 | -0.002 | 0.00% |
| SP500 | SPY | diversified_us_equity | 0.47% | 0.00% | 0.00% | 13.70% | -4.49% | -1.028 | 1.000 | 1.000 | -1.10% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | 0.30% | -0.16% | 0.07% | 13.61% | -4.36% | -0.664 | 0.995 | 1.011 | -1.29% |
| NASDAQ100 | QQQ | technology_and_growth | 0.42% | 1.08% | 4.13% | 25.65% | -11.22% | -1.037 | 0.930 | 1.425 | -3.88% |
| LARGE_GROWTH | IWF | technology_and_growth | 0.29% | 0.80% | -4.17% | 21.28% | -11.35% | -0.859 | 0.934 | 1.292 | -4.59% |
| LARGE_VALUE | IWD | diversified_us_equity | 0.40% | -0.69% | 3.25% | 11.16% | -2.40% | -0.669 | 0.797 | 0.694 | -0.17% |
| MID_CAP | IJH | diversified_us_equity | -1.32% | -3.19% | -2.79% | 13.74% | -3.70% | -0.752 | 0.805 | 0.971 | -3.70% |
| SMALL_CAP | IWM | diversified_us_equity | -1.40% | -2.65% | 3.70% | 16.71% | -3.95% | -1.216 | 0.818 | 1.198 | -3.06% |
| SMALL_VALUE | IWN | diversified_us_equity | -0.74% | -3.12% | 4.29% | 13.22% | -2.60% | -0.907 | 0.734 | 0.935 | -1.89% |
| DIVIDEND | SCHD | diversified_us_equity | -0.60% | 0.73% | -1.80% | 11.86% | -2.93% | 0.108 | 0.274 | 0.236 | -0.88% |
| LOW_VOL | SPLV | diversified_us_equity | -0.12% | -5.25% | -9.09% | 12.90% | -3.52% | -0.683 | 0.009 | 0.007 | -3.52% |
| MOMENTUM | MTUM | diversified_us_equity | -1.79% | -3.41% | 9.65% | 38.20% | -17.99% | -0.085 | 0.769 | 1.575 | -13.18% |
| TECHNOLOGY | XLK | technology_and_growth | 1.30% | 1.94% | 18.26% | 35.18% | -15.86% | -1.290 | 0.853 | 1.752 | -6.20% |
| COMMUNICATIONS | XLC | technology_and_growth | 1.43% | 2.28% | -17.89% | 19.91% | -8.67% | -0.994 | 0.564 | 0.668 | -5.36% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | -0.69% | 0.56% | -12.13% | 21.75% | -9.84% | -1.171 | 0.764 | 1.157 | -5.49% |
| CONSUMER_STAPLES | XLP | consumer_defensive | -0.63% | -3.75% | -12.54% | 17.38% | -3.58% | -0.972 | -0.069 | -0.078 | -3.87% |
| HEALTHCARE | XLV | healthcare_and_biotech | -1.98% | 0.94% | -5.75% | 19.75% | -3.74% | -0.790 | 0.217 | 0.271 | -2.57% |
| FINANCIALS | XLF | financials | 1.08% | -1.80% | 3.10% | 13.23% | -2.25% | -0.949 | 0.531 | 0.603 | -0.36% |
| INDUSTRIALS | XLI | industrials_and_defense | -1.73% | -4.43% | -7.46% | 18.60% | -5.02% | -0.957 | 0.710 | 0.949 | -5.02% |
| ENERGY | XLE | energy | -1.51% | 2.58% | -1.80% | 22.54% | -9.46% | -0.899 | -0.175 | -0.297 | -1.68% |
| MATERIALS | XLB | materials_and_mining | -0.67% | -0.75% | -11.22% | 19.35% | -4.75% | -0.549 | 0.527 | 0.732 | -0.91% |
| UTILITIES | XLU | rate_sensitive_defensive | -0.09% | -8.05% | -13.87% | 16.09% | -7.69% | -0.433 | 0.114 | 0.135 | -9.27% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | -1.33% | -5.54% | -3.76% | 15.88% | -4.19% | -0.516 | 0.238 | 0.261 | -3.33% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | 0.03% | -3.77% | -12.02% | 4.85% | -2.00% | 0.056 | 0.284 | 0.103 | -3.37% |
| LONG_TREASURY | TLT | rates_and_duration | 1.01% | -3.23% | -15.81% | 9.69% | -6.26% | 0.260 | 0.237 | 0.176 | -6.65% |
| TIPS | TIP | rates_and_duration | -0.18% | -3.74% | -9.83% | 3.60% | -1.40% | -0.431 | 0.257 | 0.067 | -1.22% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | 0.41% | -3.35% | -11.61% | 5.35% | -2.89% | -0.556 | 0.472 | 0.196 | -2.59% |
| HIGH_YIELD_CREDIT | HYG | credit | 0.16% | -2.90% | -7.78% | 3.05% | -0.80% | -0.736 | 0.778 | 0.229 | -0.23% |
| AGGREGATE_BONDS | AGG | rates_and_duration | 0.14% | -3.51% | -10.82% | 4.03% | -1.71% | -0.287 | 0.391 | 0.115 | -1.91% |
| DEVELOPED_EX_US | VEA | international_equity | -0.49% | -0.96% | -6.78% | 18.83% | -4.85% | -0.824 | 0.799 | 1.080 | -0.99% |
| EMERGING_MARKETS | VWO | international_equity | 0.56% | 0.74% | -8.42% | 18.94% | -7.05% | -0.780 | 0.811 | 1.112 | -0.73% |
| EUROPE | VGK | international_equity | -0.80% | -2.64% | -5.93% | 14.21% | -2.61% | -0.893 | 0.745 | 0.913 | -1.30% |
| JAPAN | EWJ | international_equity | 0.72% | -0.96% | -7.15% | 23.67% | -7.86% | -0.977 | 0.719 | 1.179 | -2.64% |
| CHINA | MCHI | international_equity | -0.77% | -4.22% | -14.10% | 18.61% | -11.15% | -0.679 | 0.540 | 0.845 | -15.99% |
| INDIA | INDA | international_equity | -0.16% | -4.01% | -13.61% | 13.52% | -4.59% | -1.074 | 0.554 | 0.654 | -10.36% |
| GOLD | IAU | precious_metals | -3.42% | 4.71% | -30.67% | 26.82% | -12.50% | -0.326 | 0.309 | 0.695 | -17.48% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | -1.39% | 1.36% | 8.60% | 21.86% | -12.58% | -0.359 | -0.174 | -0.275 | -2.75% |
| SEMICONDUCTORS | SMH | technology_and_growth | -1.30% | -1.09% | 23.92% | 53.80% | -24.62% | -0.745 | 0.779 | 2.396 | -17.31% |
| SOFTWARE | IGV | technology_and_growth | 5.93% | 13.62% | 5.72% | 36.07% | -21.29% | -1.100 | 0.503 | 1.214 | -7.02% |
| BROAD_AI_TECH | AIQ | technology_and_growth | 1.25% | 5.69% | 8.08% | 38.87% | -20.19% | -0.783 | 0.847 | 1.921 | -8.44% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | -2.60% | 3.59% | -15.60% | 37.57% | -23.31% | -1.053 | 0.801 | 2.194 | -14.95% |
| CYBERSECURITY | CIBR | technology_and_growth | 3.91% | 5.76% | 34.77% | 33.77% | -11.74% | -0.091 | 0.529 | 1.149 | -3.56% |
| SOLAR | TAN | clean_energy | -1.36% | -6.12% | -18.08% | 42.69% | -35.51% | -0.378 | 0.629 | 1.882 | -34.19% |
| METALS_MINING | XME | materials_and_mining | -0.50% | 12.84% | -23.24% | 41.58% | -26.49% | -0.027 | 0.595 | 1.771 | -10.55% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | -0.44% | -1.26% | -2.76% | 11.01% | -2.04% | -1.031 | 0.768 | 0.694 | -0.93% |
| BIOTECH | XBI | healthcare_and_biotech | -2.02% | 3.48% | 10.34% | 32.76% | -10.51% | -0.266 | 0.469 | 1.028 | -4.23% |
| REGIONAL_BANKS | KRE | financials | -0.75% | -5.84% | 6.31% | 18.73% | -4.66% | -0.831 | 0.412 | 0.709 | -4.66% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | -1.90% | -5.96% | -10.86% | 25.03% | -8.58% | -0.456 | 0.567 | 1.022 | -8.06% |
| CANADA | EWC | international_equity | -1.01% | -0.48% | -5.09% | 11.79% | -3.20% | -0.312 | 0.668 | 0.739 | -1.45% |
| UNITED_KINGDOM | EWU | international_equity | -0.80% | -4.00% | -7.26% | 12.87% | -2.39% | -0.560 | 0.600 | 0.700 | -1.70% |
| AUSTRALIA | EWA | international_equity | -0.46% | -3.13% | -8.20% | 16.76% | -4.78% | -0.629 | 0.669 | 0.924 | -1.41% |
| SOUTH_KOREA | EWY | international_equity | 1.04% | 8.05% | -2.19% | 77.56% | -34.21% | -0.599 | 0.636 | 2.772 | -17.79% |
| TAIWAN | EWT | international_equity | 3.45% | 11.06% | 15.53% | 41.85% | -19.83% | -1.002 | 0.761 | 1.859 | -3.25% |
| BRAZIL | EWZ | international_equity | 1.40% | -6.41% | -13.48% | 21.57% | -8.05% | -0.465 | 0.499 | 0.969 | -14.00% |
| MEXICO | EWW | international_equity | -1.16% | -4.55% | -12.02% | 19.13% | -5.91% | -0.301 | 0.539 | 0.925 | -4.46% |
| SOUTH_AFRICA | EZA | international_equity | -2.47% | 6.58% | -28.41% | 31.07% | -11.18% | -0.773 | 0.616 | 1.591 | -11.43% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | 0.05% | -3.49% | -10.73% | 4.66% | -1.85% | 0.057 | 0.386 | 0.134 | -1.80% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | -0.11% | -3.97% | -10.29% | 2.89% | -2.15% | 0.397 | 0.381 | 0.089 | -1.92% |
| EMERGING_MARKET_BONDS | EMB | credit | 0.18% | -3.18% | -9.58% | 5.40% | -1.96% | -0.679 | 0.679 | 0.304 | -1.15% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | -0.10% | -4.07% | -10.26% | 3.60% | -1.45% | -0.502 | 0.461 | 0.130 | -1.90% |
| SILVER | SLV | precious_metals | -4.30% | 8.46% | -45.75% | 44.66% | -26.25% | -0.673 | 0.353 | 1.715 | -43.16% |
| COPPER | CPER | non_energy_commodities | -0.80% | -2.89% | -2.02% | 25.32% | -10.57% | -0.477 | 0.551 | 1.218 | -2.89% |
| AGRICULTURE | DBA | non_energy_commodities | 3.07% | 2.49% | -3.08% | 13.07% | -3.71% | -0.288 | 0.071 | 0.062 | 0.00% |
| OIL | USO | energy | -3.67% | -1.99% | 46.86% | 52.44% | -26.69% | -0.623 | -0.337 | -1.271 | -15.21% |
| US_DOLLAR | UUP | currencies | 1.00% | -3.59% | -4.78% | 5.26% | -2.52% | -0.855 | -0.291 | -0.128 | -1.47% |
| EURO | FXE | currencies | -0.76% | -3.17% | -10.79% | 5.00% | -2.66% | -0.700 | 0.269 | 0.117 | -3.27% |
| YEN | FXY | currencies | -0.78% | -4.30% | -10.82% | 7.94% | -2.81% | 0.480 | 0.171 | 0.108 | -8.87% |
| BITCOIN_ETF | IBIT | crypto_assets | 0.50% | 15.89% | -10.01% | 41.75% | -20.03% | 0.363 | 0.474 | 1.667 | -38.42% |
| ETHEREUM_ETF | ETHA | crypto_assets | 0.71% | 22.87% | -8.76% | 59.28% | -22.76% | 0.812 | 0.496 | 2.514 | -48.67% |
