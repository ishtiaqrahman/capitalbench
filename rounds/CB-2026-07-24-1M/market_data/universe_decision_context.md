# Full-Universe Horizon-Specific Decision Context

Profile: monthly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: yahoo_chart_adjusted_close_and_reported_volume
- As-of date requested: 2026-07-24
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | -0.59% |
| spy_return_21s | 0.78% |
| rsp_return_5s | 0.09% |
| rsp_return_21s | 1.52% |
| hyg_return_5s | -0.53% |
| hyg_return_21s | -0.32% |
| tlt_return_5s | -1.50% |
| tlt_return_21s | -4.37% |
| uup_return_5s | 0.88% |
| uup_return_21s | 0.18% |
| uso_return_5s | 10.27% |
| uso_return_21s | 28.60% |
| iau_return_5s | 0.97% |
| iau_return_21s | 1.65% |
| rsp_minus_spy_5s | 0.68% |
| rsp_minus_spy_21s | 0.74% |
| positive_asset_share_5s | 49.28% |
| positive_asset_share_21s | 55.07% |
| active_return_dispersion_5s |  |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_5s | active_return_21s | prior_105s_active_return | volatility_63s | max_drawdown_63s | volume_zscore_20v120 | corr_spy_252s | beta_spy_252s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | -0.78% | -6.99% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.07% | -0.46% | -5.50% | 0.21% | -0.01% | -0.199 | -0.108 | -0.002 | 0.00% |
| SP500 | SPY | diversified_us_equity | -0.59% | 0.00% | 0.00% | 13.04% | -4.49% | -0.965 | 1.000 | 1.000 | -2.47% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | -0.60% | -0.17% | 0.03% | 12.98% | -4.36% | -0.845 | 0.995 | 1.013 | -2.27% |
| NASDAQ100 | QQQ | technology_and_growth | -1.60% | -4.49% | 7.76% | 24.63% | -8.20% | -0.963 | 0.932 | 1.392 | -8.20% |
| LARGE_GROWTH | IWF | technology_and_growth | -1.45% | -2.46% | -4.08% | 18.85% | -8.56% | -0.621 | 0.935 | 1.261 | -8.56% |
| LARGE_VALUE | IWD | diversified_us_equity | 0.08% | 2.23% | 3.46% | 11.87% | -2.40% | -0.172 | 0.807 | 0.718 | -0.49% |
| MID_CAP | IJH | diversified_us_equity | 0.30% | -0.76% | 1.22% | 14.54% | -4.25% | -0.995 | 0.800 | 0.990 | -1.74% |
| SMALL_CAP | IWM | diversified_us_equity | -0.98% | -2.64% | 3.44% | 18.37% | -4.81% | -1.171 | 0.814 | 1.242 | -3.09% |
| SMALL_VALUE | IWN | diversified_us_equity | -0.41% | 0.52% | 3.56% | 15.35% | -4.01% | -0.605 | 0.733 | 1.009 | -1.23% |
| DIVIDEND | SCHD | diversified_us_equity | 1.15% | 4.17% | 3.55% | 12.00% | -2.95% | -0.437 | 0.314 | 0.274 | 0.00% |
| LOW_VOL | SPLV | diversified_us_equity | 1.00% | 2.76% | -3.44% | 13.06% | -4.09% | -0.901 | 0.043 | 0.036 | 0.00% |
| MOMENTUM | MTUM | diversified_us_equity | 1.42% | -7.48% | 21.52% | 36.61% | -12.49% | 1.375 | 0.779 | 1.503 | -11.25% |
| TECHNOLOGY | XLK | technology_and_growth | 0.17% | -4.69% | 19.66% | 33.28% | -11.31% | -1.007 | 0.862 | 1.683 | -11.16% |
| COMMUNICATIONS | XLC | technology_and_growth | -3.93% | -1.00% | -14.81% | 16.74% | -10.00% | 0.070 | 0.629 | 0.712 | -10.96% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | -5.22% | -5.69% | -12.77% | 20.54% | -10.72% | -0.326 | 0.795 | 1.206 | -11.78% |
| CONSUMER_STAPLES | XLP | consumer_defensive | -1.24% | -1.14% | -3.06% | 16.47% | -4.95% | -0.924 | -0.046 | -0.050 | -5.35% |
| HEALTHCARE | XLV | healthcare_and_biotech | 0.92% | 5.24% | -9.28% | 18.20% | -3.74% | -0.521 | 0.255 | 0.315 | -1.14% |
| FINANCIALS | XLF | financials | 0.09% | 4.05% | -6.29% | 13.04% | -2.42% | -0.774 | 0.557 | 0.642 | -0.78% |
| INDUSTRIALS | XLI | industrials_and_defense | 1.81% | 0.58% | 2.47% | 19.08% | -4.60% | -1.113 | 0.712 | 0.933 | -1.56% |
| ENERGY | XLE | energy | 3.36% | 10.52% | 4.05% | 24.01% | -13.21% | -0.959 | -0.127 | -0.209 | -4.01% |
| MATERIALS | XLB | materials_and_mining | 1.44% | -0.58% | -2.83% | 19.76% | -6.43% | -0.670 | 0.547 | 0.762 | -3.62% |
| UTILITIES | XLU | rate_sensitive_defensive | 2.48% | 0.87% | 1.07% | 16.94% | -8.00% | -0.839 | 0.133 | 0.156 | -1.72% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | 1.17% | 2.46% | 2.88% | 16.21% | -3.38% | -0.824 | 0.251 | 0.285 | 0.00% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | -0.86% | -2.25% | -6.49% | 4.97% | -2.24% | -0.888 | 0.221 | 0.082 | -3.52% |
| LONG_TREASURY | TLT | rates_and_duration | -1.50% | -5.15% | -5.46% | 8.77% | -4.54% | -0.926 | 0.176 | 0.129 | -6.61% |
| TIPS | TIP | rates_and_duration | -0.71% | -1.48% | -5.95% | 3.54% | -1.44% | -0.644 | 0.246 | 0.067 | -1.43% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | -1.24% | -3.34% | -6.33% | 5.25% | -2.82% | -0.461 | 0.420 | 0.176 | -3.12% |
| HIGH_YIELD_CREDIT | HYG | credit | -0.53% | -1.09% | -6.14% | 3.64% | -1.01% | -0.743 | 0.770 | 0.233 | -0.80% |
| AGGREGATE_BONDS | AGG | rates_and_duration | -0.75% | -2.19% | -6.17% | 4.10% | -1.71% | -0.250 | 0.329 | 0.098 | -2.28% |
| DEVELOPED_EX_US | VEA | international_equity | 0.01% | -1.59% | 1.29% | 20.64% | -4.85% | -0.625 | 0.798 | 1.072 | -3.70% |
| EMERGING_MARKETS | VWO | international_equity | -0.07% | -2.76% | -2.59% | 20.41% | -5.67% | -0.497 | 0.800 | 1.096 | -5.62% |
| EUROPE | VGK | international_equity | -0.20% | 0.90% | -4.41% | 18.02% | -3.86% | -1.017 | 0.740 | 0.928 | -1.73% |
| JAPAN | EWJ | international_equity | 0.80% | -2.29% | 2.74% | 22.06% | -6.74% | -0.789 | 0.714 | 1.156 | -5.94% |
| CHINA | MCHI | international_equity | 0.72% | 2.92% | -24.53% | 20.74% | -15.01% | -0.215 | 0.573 | 0.928 | -18.88% |
| INDIA | INDA | international_equity | -1.82% | -4.02% | -11.18% | 15.31% | -5.64% | -0.701 | 0.517 | 0.614 | -13.15% |
| GOLD | IAU | precious_metals | 0.97% | 0.88% | -25.97% | 23.90% | -16.01% | -0.596 | 0.309 | 0.679 | -24.95% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | 4.06% | 12.98% | 5.00% | 20.76% | -16.55% | 0.118 | -0.122 | -0.183 | -5.08% |
| SEMICONDUCTORS | SMH | technology_and_growth | 0.84% | -10.10% | 46.66% | 53.24% | -16.80% | 0.497 | 0.780 | 2.302 | -16.10% |
| SOFTWARE | IGV | technology_and_growth | -5.19% | 1.32% | -18.08% | 32.99% | -21.29% | -0.663 | 0.512 | 1.167 | -25.29% |
| BROAD_AI_TECH | AIQ | technology_and_growth | -1.23% | -9.31% | 13.87% | 39.32% | -17.34% | -0.160 | 0.845 | 1.867 | -17.34% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | -1.83% | -8.99% | -12.14% | 38.54% | -20.72% | -1.070 | 0.791 | 2.145 | -20.72% |
| CYBERSECURITY | CIBR | technology_and_growth | -4.29% | 4.80% | 11.83% | 32.26% | -11.74% | 0.022 | 0.532 | 1.087 | -6.68% |
| SOLAR | TAN | clean_energy | -4.86% | -12.61% | 0.67% | 44.84% | -30.64% | -1.000 | 0.590 | 1.797 | -30.64% |
| METALS_MINING | XME | materials_and_mining | 3.45% | -5.89% | -24.84% | 39.81% | -26.37% | -0.519 | 0.587 | 1.691 | -23.35% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | 0.09% | 0.74% | -0.76% | 10.84% | -2.04% | -0.842 | 0.778 | 0.718 | -0.69% |
| BIOTECH | XBI | healthcare_and_biotech | -2.45% | -0.26% | 6.91% | 30.46% | -8.40% | -0.135 | 0.476 | 1.004 | -8.40% |
| REGIONAL_BANKS | KRE | financials | -1.25% | 1.60% | 0.02% | 20.54% | -5.29% | -0.617 | 0.447 | 0.809 | -2.81% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | 4.08% | 0.90% | -6.70% | 25.04% | -8.58% | -0.475 | 0.557 | 0.972 | -4.24% |
| CANADA | EWC | international_equity | -0.64% | 2.33% | -2.72% | 13.11% | -3.20% | -0.677 | 0.680 | 0.768 | -0.71% |
| UNITED_KINGDOM | EWU | international_equity | 0.62% | 3.14% | -4.70% | 16.96% | -3.94% | -0.452 | 0.608 | 0.717 | -1.59% |
| AUSTRALIA | EWA | international_equity | -0.10% | 2.13% | -2.44% | 18.33% | -6.84% | -0.894 | 0.674 | 0.920 | -3.76% |
| SOUTH_KOREA | EWY | international_equity | 0.26% | -18.16% | 63.08% | 78.14% | -25.85% | 0.292 | 0.638 | 2.635 | -25.66% |
| TAIWAN | EWT | international_equity | 0.70% | -7.18% | 46.45% | 42.15% | -13.98% | 0.072 | 0.744 | 1.736 | -12.12% |
| BRAZIL | EWZ | international_equity | 1.42% | 4.78% | -11.93% | 23.76% | -15.96% | -1.097 | 0.505 | 0.995 | -13.56% |
| MEXICO | EWW | international_equity | 0.45% | 1.47% | -8.14% | 20.57% | -7.30% | -0.760 | 0.531 | 0.920 | -5.75% |
| SOUTH_AFRICA | EZA | international_equity | -2.07% | -2.56% | -22.89% | 32.90% | -14.17% | -0.391 | 0.625 | 1.597 | -23.52% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | -0.71% | -2.16% | -5.88% | 4.81% | -1.93% | -0.528 | 0.328 | 0.115 | -2.22% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | -0.97% | -2.29% | -5.68% | 3.02% | -2.15% | 0.076 | 0.325 | 0.076 | -1.88% |
| EMERGING_MARKET_BONDS | EMB | credit | -0.93% | -2.37% | -4.69% | 5.76% | -2.10% | -0.684 | 0.663 | 0.295 | -1.84% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | -0.27% | -1.99% | -5.78% | 4.19% | -1.44% | -0.422 | 0.418 | 0.116 | -1.73% |
| SILVER | SLV | precious_metals | 3.56% | 0.79% | -47.56% | 50.34% | -36.50% | -0.686 | 0.354 | 1.712 | -50.20% |
| COPPER | CPER | non_energy_commodities | 1.13% | 4.84% | -5.17% | 29.15% | -10.57% | -0.701 | 0.462 | 1.248 | -5.54% |
| AGRICULTURE | DBA | non_energy_commodities | 1.44% | 5.55% | -3.24% | 13.35% | -8.67% | -0.356 | 0.074 | 0.063 | -1.71% |
| OIL | USO | energy | 10.27% | 27.82% | 41.01% | 51.20% | -32.49% | -0.556 | -0.297 | -1.068 | -10.64% |
| US_DOLLAR | UUP | currencies | 0.88% | -0.60% | -1.91% | 4.90% | -0.98% | -0.281 | -0.279 | -0.131 | 0.00% |
| EURO | FXE | currencies | -0.62% | -0.54% | -10.08% | 4.64% | -3.57% | -0.818 | 0.260 | 0.125 | -5.18% |
| YEN | FXY | currencies | -0.83% | -1.94% | -9.25% | 6.51% | -4.57% | -0.183 | 0.111 | 0.069 | -10.79% |
| BITCOIN_ETF | IBIT | crypto_assets | 0.00% | 6.55% | -40.15% | 36.82% | -28.36% | -0.499 | 0.515 | 1.801 | -49.01% |
| ETHEREUM_ETF | ETHA | crypto_assets | 0.93% | 17.01% | -53.22% | 52.08% | -34.41% | -0.451 | 0.554 | 2.948 | -61.63% |
