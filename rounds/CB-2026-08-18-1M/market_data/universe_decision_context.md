# Full-Universe Horizon-Specific Decision Context

Profile: monthly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: yahoo_chart_adjusted_close_and_reported_volume
- As-of date requested: 2026-08-17
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | -0.05% |
| spy_return_21s | 3.95% |
| rsp_return_5s | 0.26% |
| rsp_return_21s | 3.48% |
| hyg_return_5s | 0.16% |
| hyg_return_21s | 0.23% |
| tlt_return_5s | -0.87% |
| tlt_return_21s | -3.36% |
| uup_return_5s | -0.14% |
| uup_return_21s | -0.81% |
| uso_return_5s | 3.47% |
| uso_return_21s | 5.11% |
| iau_return_5s | 0.73% |
| iau_return_21s | 10.08% |
| rsp_minus_spy_5s | 0.31% |
| rsp_minus_spy_21s | -0.48% |
| positive_asset_share_5s | 59.42% |
| positive_asset_share_21s | 72.46% |
| active_return_dispersion_5s |  |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_5s | active_return_21s | prior_105s_active_return | volatility_63s | max_drawdown_63s | volume_zscore_20v120 | corr_spy_252s | beta_spy_252s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | -3.95% | -9.61% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.08% | -3.65% | -8.12% | 0.21% | -0.01% | -0.404 | -0.111 | -0.002 | 0.00% |
| SP500 | SPY | diversified_us_equity | -0.05% | 0.00% | 0.00% | 13.72% | -4.49% | -0.871 | 1.000 | 1.000 | -0.67% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | 0.13% | 0.17% | 0.07% | 13.63% | -4.36% | -0.769 | 0.995 | 1.012 | -0.56% |
| NASDAQ100 | QQQ | technology_and_growth | 1.25% | 1.01% | 6.19% | 25.66% | -11.22% | -0.781 | 0.931 | 1.417 | -2.08% |
| LARGE_GROWTH | IWF | technology_and_growth | 0.73% | 0.82% | -2.63% | 20.85% | -11.35% | -0.910 | 0.937 | 1.283 | -2.78% |
| LARGE_VALUE | IWD | diversified_us_equity | -0.65% | -0.18% | 1.15% | 11.60% | -2.40% | -0.597 | 0.805 | 0.709 | -0.80% |
| MID_CAP | IJH | diversified_us_equity | 1.21% | -0.06% | -3.06% | 13.85% | -3.09% | -0.855 | 0.808 | 0.977 | -0.24% |
| SMALL_CAP | IWM | diversified_us_equity | 1.36% | -0.55% | 2.68% | 17.38% | -3.95% | -1.102 | 0.819 | 1.212 | -0.34% |
| SMALL_VALUE | IWN | diversified_us_equity | 0.97% | -0.83% | 0.44% | 14.35% | -2.75% | -0.448 | 0.726 | 0.973 | -0.43% |
| DIVIDEND | SCHD | diversified_us_equity | 0.29% | 0.24% | -3.78% | 11.83% | -2.95% | 0.158 | 0.288 | 0.246 | -0.67% |
| LOW_VOL | SPLV | diversified_us_equity | 0.05% | -3.99% | -7.63% | 13.24% | -3.75% | -0.735 | 0.023 | 0.019 | -2.86% |
| MOMENTUM | MTUM | diversified_us_equity | 4.80% | -3.23% | 16.01% | 38.72% | -17.99% | 0.787 | 0.752 | 1.514 | -6.71% |
| TECHNOLOGY | XLK | technology_and_growth | 2.15% | 4.44% | 16.52% | 34.99% | -15.86% | -1.027 | 0.858 | 1.731 | -3.87% |
| COMMUNICATIONS | XLC | technology_and_growth | -0.90% | -6.21% | -11.92% | 20.71% | -9.78% | -0.454 | 0.577 | 0.694 | -7.18% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | -2.44% | -4.17% | -9.85% | 23.90% | -10.72% | -0.750 | 0.771 | 1.198 | -5.86% |
| CONSUMER_STAPLES | XLP | consumer_defensive | -0.32% | -4.55% | -13.23% | 17.29% | -4.95% | -0.793 | -0.064 | -0.070 | -4.74% |
| HEALTHCARE | XLV | healthcare_and_biotech | -0.83% | -0.25% | -6.56% | 18.06% | -3.74% | -0.777 | 0.224 | 0.270 | -0.83% |
| FINANCIALS | XLF | financials | -0.40% | -1.61% | 0.26% | 13.39% | -2.08% | -0.922 | 0.546 | 0.619 | -1.17% |
| INDUSTRIALS | XLI | industrials_and_defense | 0.93% | -0.10% | -6.05% | 18.25% | -4.80% | -1.056 | 0.718 | 0.950 | -0.10% |
| ENERGY | XLE | energy | 3.99% | 4.54% | -2.02% | 24.10% | -13.21% | -0.924 | -0.159 | -0.268 | 0.00% |
| MATERIALS | XLB | materials_and_mining | -1.77% | -0.57% | -14.04% | 19.60% | -4.75% | -0.484 | 0.534 | 0.736 | -1.88% |
| UTILITIES | XLU | rate_sensitive_defensive | 2.43% | -6.14% | -11.16% | 15.56% | -6.83% | -0.489 | 0.124 | 0.144 | -6.20% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | 0.97% | -3.35% | -3.88% | 16.46% | -4.19% | -0.510 | 0.248 | 0.276 | -2.56% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | 0.09% | -4.68% | -11.50% | 4.80% | -2.00% | -0.271 | 0.295 | 0.105 | -3.38% |
| LONG_TREASURY | TLT | rates_and_duration | -0.87% | -7.32% | -13.63% | 9.06% | -6.26% | 0.117 | 0.247 | 0.178 | -8.38% |
| TIPS | TIP | rates_and_duration | -0.08% | -4.61% | -9.82% | 3.39% | -1.40% | -0.377 | 0.287 | 0.074 | -1.38% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | -0.25% | -5.26% | -11.39% | 5.31% | -2.89% | -0.426 | 0.487 | 0.201 | -3.18% |
| HIGH_YIELD_CREDIT | HYG | credit | 0.16% | -3.72% | -8.40% | 3.54% | -0.80% | -0.628 | 0.783 | 0.238 | -0.23% |
| AGGREGATE_BONDS | AGG | rates_and_duration | 0.01% | -4.72% | -10.42% | 4.30% | -1.82% | -0.265 | 0.401 | 0.119 | -2.49% |
| DEVELOPED_EX_US | VEA | international_equity | 1.64% | 1.77% | -7.53% | 19.04% | -4.85% | -0.957 | 0.802 | 1.077 | 0.00% |
| EMERGING_MARKETS | VWO | international_equity | 0.10% | -2.42% | -7.83% | 19.56% | -7.05% | -0.720 | 0.802 | 1.094 | -1.39% |
| EUROPE | VGK | international_equity | -0.17% | 0.35% | -8.82% | 15.11% | -3.12% | -0.901 | 0.740 | 0.905 | -0.54% |
| JAPAN | EWJ | international_equity | 2.21% | 4.53% | -12.66% | 23.03% | -7.86% | -0.988 | 0.717 | 1.169 | -0.30% |
| CHINA | MCHI | international_equity | -3.28% | 0.03% | -21.29% | 18.84% | -11.15% | -0.580 | 0.542 | 0.857 | -16.25% |
| INDIA | INDA | international_equity | -1.12% | -2.58% | -17.13% | 13.49% | -4.59% | -0.613 | 0.545 | 0.642 | -10.33% |
| GOLD | IAU | precious_metals | 0.73% | 6.13% | -29.92% | 24.77% | -12.78% | -0.488 | 0.310 | 0.683 | -18.17% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | 2.13% | 3.42% | 10.17% | 22.62% | -16.24% | -0.349 | -0.181 | -0.285 | -3.70% |
| SEMICONDUCTORS | SMH | technology_and_growth | 4.33% | 2.79% | 26.89% | 53.47% | -24.62% | 0.226 | 0.784 | 2.372 | -11.19% |
| SOFTWARE | IGV | technology_and_growth | -2.88% | 5.95% | 2.53% | 35.49% | -21.29% | -0.841 | 0.510 | 1.192 | -13.40% |
| BROAD_AI_TECH | AIQ | technology_and_growth | 0.77% | 5.08% | 9.10% | 39.45% | -20.19% | -0.548 | 0.849 | 1.912 | -8.75% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | 2.02% | 8.39% | -14.31% | 37.89% | -23.82% | -0.678 | 0.800 | 2.185 | -9.28% |
| CYBERSECURITY | CIBR | technology_and_growth | -2.79% | 2.47% | 31.91% | 33.09% | -11.74% | -0.358 | 0.541 | 1.119 | -4.32% |
| SOLAR | TAN | clean_energy | -1.81% | -9.48% | -16.55% | 46.12% | -35.51% | -0.171 | 0.606 | 1.881 | -31.12% |
| METALS_MINING | XME | materials_and_mining | 0.48% | 16.13% | -26.03% | 40.97% | -26.49% | -0.335 | 0.596 | 1.736 | -11.03% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | 0.26% | -0.48% | -3.57% | 11.00% | -2.04% | -0.859 | 0.773 | 0.700 | -0.89% |
| BIOTECH | XBI | healthcare_and_biotech | 0.95% | -0.54% | 16.07% | 29.65% | -10.51% | -0.610 | 0.476 | 1.001 | -2.89% |
| REGIONAL_BANKS | KRE | financials | 1.79% | -4.63% | 1.89% | 19.09% | -3.73% | -0.883 | 0.432 | 0.757 | -0.69% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | 0.03% | 2.82% | -8.59% | 25.96% | -8.58% | -0.378 | 0.565 | 1.010 | -0.80% |
| CANADA | EWC | international_equity | 1.11% | 1.12% | -4.78% | 11.83% | -3.20% | -0.447 | 0.664 | 0.732 | -0.08% |
| UNITED_KINGDOM | EWU | international_equity | -0.68% | -1.35% | -8.84% | 13.87% | -3.40% | -0.539 | 0.605 | 0.703 | -1.07% |
| AUSTRALIA | EWA | international_equity | -1.66% | -1.03% | -7.95% | 16.75% | -4.78% | -0.831 | 0.667 | 0.915 | -2.83% |
| SOUTH_KOREA | EWY | international_equity | 13.47% | 9.93% | 11.72% | 78.93% | -34.21% | 0.044 | 0.640 | 2.743 | -15.56% |
| TAIWAN | EWT | international_equity | 5.50% | 6.80% | 23.63% | 43.24% | -19.83% | -0.631 | 0.760 | 1.844 | -3.34% |
| BRAZIL | EWZ | international_equity | -3.47% | -7.53% | -16.16% | 21.78% | -8.97% | -0.814 | 0.502 | 0.982 | -17.82% |
| MEXICO | EWW | international_equity | -2.63% | -4.22% | -15.55% | 18.85% | -6.47% | -0.500 | 0.545 | 0.931 | -6.42% |
| SOUTH_AFRICA | EZA | international_equity | -2.21% | 5.40% | -25.00% | 30.34% | -11.54% | -0.527 | 0.624 | 1.588 | -14.60% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | 0.14% | -4.61% | -10.14% | 5.18% | -2.02% | -0.367 | 0.394 | 0.138 | -2.28% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | -0.27% | -4.64% | -9.83% | 3.09% | -2.15% | 1.027 | 0.386 | 0.090 | -1.60% |
| EMERGING_MARKET_BONDS | EMB | credit | -0.15% | -4.39% | -9.40% | 5.50% | -1.96% | -0.680 | 0.688 | 0.307 | -1.35% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | -0.29% | -4.29% | -10.29% | 3.75% | -1.44% | -0.720 | 0.466 | 0.130 | -1.80% |
| SILVER | SLV | precious_metals | 0.27% | 13.36% | -36.77% | 43.67% | -27.95% | -0.543 | 0.354 | 1.700 | -43.59% |
| COPPER | CPER | non_energy_commodities | -0.12% | 0.17% | -3.52% | 26.00% | -10.57% | -0.484 | 0.540 | 1.170 | -1.76% |
| AGRICULTURE | DBA | non_energy_commodities | 1.15% | -2.88% | -1.66% | 13.46% | -7.21% | -0.654 | 0.074 | 0.064 | -2.05% |
| OIL | USO | energy | 3.47% | 1.15% | 53.03% | 53.65% | -32.49% | -0.566 | -0.335 | -1.252 | -14.82% |
| US_DOLLAR | UUP | currencies | -0.14% | -4.76% | -3.98% | 4.85% | -1.85% | -0.472 | -0.308 | -0.137 | -1.75% |
| EURO | FXE | currencies | 0.33% | -2.69% | -12.93% | 4.70% | -2.66% | -0.841 | 0.289 | 0.128 | -3.38% |
| YEN | FXY | currencies | -0.16% | -2.15% | -15.72% | 7.58% | -3.20% | 1.479 | 0.179 | 0.114 | -8.42% |
| BITCOIN_ETF | IBIT | crypto_assets | 0.52% | -3.76% | -16.33% | 35.84% | -25.73% | -0.637 | 0.506 | 1.737 | -48.91% |
| ETHEREUM_ETF | ETHA | crypto_assets | 1.84% | -0.43% | -19.52% | 52.24% | -29.95% | -0.497 | 0.532 | 2.725 | -60.64% |
