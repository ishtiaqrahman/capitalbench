# Full-Universe Horizon-Specific Decision Context

Profile: monthly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: tiingo_eod_adjusted_price_and_volume
- As-of date requested: 2026-09-18
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | -0.09% |
| spy_return_21s | -0.71% |
| rsp_return_5s | -1.20% |
| rsp_return_21s | -4.40% |
| hyg_return_5s | -0.09% |
| hyg_return_21s | -0.94% |
| tlt_return_5s | 0.47% |
| tlt_return_21s | -1.76% |
| uup_return_5s | 1.14% |
| uup_return_21s | 1.83% |
| uso_return_5s | -0.70% |
| uso_return_21s | 17.50% |
| iau_return_5s | 0.64% |
| iau_return_21s | -3.08% |
| rsp_minus_spy_5s | -1.11% |
| rsp_minus_spy_21s | -3.69% |
| positive_asset_share_5s | 34.78% |
| positive_asset_share_21s | 31.88% |
| active_return_dispersion_5s |  |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_5s | active_return_21s | prior_105s_active_return | volatility_63s | max_drawdown_63s | volume_zscore_20v120 | corr_spy_252s | beta_spy_252s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | 0.71% | -17.18% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.05% | 1.00% | -15.67% | 0.19% | -0.01% | -0.347 | -0.078 | -0.001 | 0.00% |
| SP500 | SPY | diversified_us_equity | -0.09% | 0.00% | 0.00% | 11.47% | -3.38% | -0.812 | 1.000 | 1.000 | -1.84% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | -0.23% | -0.49% | 0.29% | 11.27% | -3.39% | -0.681 | 0.995 | 1.012 | -2.31% |
| NASDAQ100 | QQQ | technology_and_growth | 0.92% | 1.46% | 3.85% | 20.88% | -10.55% | -0.945 | 0.929 | 1.421 | -3.21% |
| LARGE_GROWTH | IWF | technology_and_growth | 0.89% | 1.28% | -4.39% | 19.26% | -8.15% | -0.595 | 0.934 | 1.287 | -4.12% |
| LARGE_VALUE | IWD | diversified_us_equity | -1.16% | -1.66% | 4.15% | 9.63% | -2.81% | -0.525 | 0.804 | 0.702 | -2.60% |
| MID_CAP | IJH | diversified_us_equity | -1.66% | -4.27% | -2.51% | 12.09% | -7.18% | -0.573 | 0.814 | 0.974 | -6.95% |
| SMALL_CAP | IWM | diversified_us_equity | -1.40% | -4.88% | 4.95% | 12.95% | -6.69% | -0.718 | 0.820 | 1.193 | -6.63% |
| SMALL_VALUE | IWN | diversified_us_equity | -1.47% | -3.34% | 4.09% | 10.43% | -4.83% | -0.697 | 0.737 | 0.933 | -4.83% |
| DIVIDEND | SCHD | diversified_us_equity | -1.29% | -3.31% | -0.58% | 11.59% | -4.35% | 0.090 | 0.291 | 0.252 | -4.35% |
| LOW_VOL | SPLV | diversified_us_equity | -1.64% | -3.58% | -12.66% | 11.33% | -6.74% | -0.735 | 0.025 | 0.020 | -6.74% |
| MOMENTUM | MTUM | diversified_us_equity | 1.04% | 2.14% | 6.86% | 33.40% | -17.99% | -0.700 | 0.764 | 1.568 | -10.13% |
| TECHNOLOGY | XLK | technology_and_growth | 1.03% | 3.96% | 15.80% | 29.03% | -13.31% | -1.119 | 0.852 | 1.746 | -4.23% |
| COMMUNICATIONS | XLC | technology_and_growth | -1.59% | 0.25% | -18.22% | 19.88% | -7.06% | -0.786 | 0.550 | 0.655 | -7.18% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | -1.71% | -5.66% | -8.65% | 20.08% | -8.08% | -0.874 | 0.770 | 1.162 | -10.48% |
| CONSUMER_STAPLES | XLP | consumer_defensive | -0.70% | -3.61% | -10.27% | 16.42% | -5.32% | -0.670 | -0.055 | -0.061 | -6.85% |
| HEALTHCARE | XLV | healthcare_and_biotech | 1.83% | -3.44% | 3.67% | 19.01% | -5.87% | -0.932 | 0.225 | 0.282 | -4.15% |
| FINANCIALS | XLF | financials | -2.43% | -2.11% | 1.16% | 12.76% | -4.61% | -0.596 | 0.542 | 0.613 | -4.61% |
| INDUSTRIALS | XLI | industrials_and_defense | -1.52% | -5.99% | -5.70% | 16.29% | -9.54% | -0.475 | 0.711 | 0.951 | -8.99% |
| ENERGY | XLE | energy | -1.27% | 1.86% | -8.61% | 21.05% | -3.87% | -0.549 | -0.173 | -0.294 | -2.46% |
| MATERIALS | XLB | materials_and_mining | -1.88% | -4.10% | -6.27% | 17.34% | -6.86% | -0.311 | 0.536 | 0.743 | -6.86% |
| UTILITIES | XLU | rate_sensitive_defensive | -3.04% | -5.92% | -21.33% | 14.61% | -11.21% | -0.081 | 0.123 | 0.146 | -12.74% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | -2.05% | -4.76% | -8.21% | 13.86% | -7.56% | -0.425 | 0.250 | 0.272 | -7.56% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | -0.23% | -1.70% | -18.00% | 4.80% | -3.57% | -0.165 | 0.292 | 0.105 | -5.16% |
| LONG_TREASURY | TLT | rates_and_duration | 0.47% | -1.04% | -20.44% | 9.68% | -6.63% | 0.124 | 0.243 | 0.174 | -8.13% |
| TIPS | TIP | rates_and_duration | -0.54% | -1.37% | -17.11% | 3.50% | -2.57% | -0.363 | 0.255 | 0.067 | -2.76% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | 0.36% | -0.63% | -17.65% | 5.40% | -3.79% | -0.444 | 0.473 | 0.194 | -3.69% |
| HIGH_YIELD_CREDIT | HYG | credit | -0.09% | -0.23% | -14.63% | 2.76% | -1.39% | -0.331 | 0.772 | 0.229 | -1.20% |
| AGGREGATE_BONDS | AGG | rates_and_duration | -0.02% | -0.85% | -17.18% | 4.06% | -2.58% | -0.156 | 0.399 | 0.117 | -3.11% |
| DEVELOPED_EX_US | VEA | international_equity | -1.56% | -1.03% | -2.87% | 16.17% | -4.75% | -0.694 | 0.802 | 1.087 | -3.03% |
| EMERGING_MARKETS | VWO | international_equity | -0.37% | 0.85% | -5.89% | 15.62% | -7.05% | -0.798 | 0.817 | 1.116 | -2.14% |
| EUROPE | VGK | international_equity | -1.76% | -3.40% | -2.67% | 12.26% | -5.11% | -0.728 | 0.747 | 0.913 | -5.11% |
| JAPAN | EWJ | international_equity | -1.58% | 3.05% | -3.85% | 21.51% | -7.86% | -0.786 | 0.726 | 1.185 | -1.58% |
| CHINA | MCHI | international_equity | 0.21% | -3.48% | -19.04% | 16.35% | -8.12% | -0.955 | 0.565 | 0.862 | -19.28% |
| INDIA | INDA | international_equity | -1.13% | -2.36% | -12.93% | 12.74% | -6.08% | -0.616 | 0.567 | 0.674 | -13.15% |
| GOLD | IAU | precious_metals | 0.64% | -2.36% | -20.08% | 24.36% | -8.48% | -0.375 | 0.336 | 0.758 | -19.04% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | -0.66% | 7.97% | -10.73% | 22.02% | -6.42% | -0.404 | -0.187 | -0.298 | -2.19% |
| SEMICONDUCTORS | SMH | technology_and_growth | 0.79% | 2.87% | 24.85% | 44.97% | -24.62% | -0.878 | 0.770 | 2.379 | -14.34% |
| SOFTWARE | IGV | technology_and_growth | 2.79% | 2.21% | 4.57% | 33.92% | -8.27% | -1.068 | 0.496 | 1.225 | -11.39% |
| BROAD_AI_TECH | AIQ | technology_and_growth | 0.23% | 2.52% | 11.90% | 30.56% | -16.56% | -0.805 | 0.850 | 1.924 | -8.57% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | 0.69% | -2.31% | -11.26% | 31.77% | -17.73% | -1.146 | 0.806 | 2.195 | -15.03% |
| CYBERSECURITY | CIBR | technology_and_growth | 5.79% | 5.24% | 29.67% | 33.20% | -9.53% | 0.174 | 0.503 | 1.128 | -2.28% |
| SOLAR | TAN | clean_energy | -3.16% | -8.82% | -28.56% | 35.76% | -26.98% | -0.483 | 0.643 | 1.917 | -38.24% |
| METALS_MINING | XME | materials_and_mining | -4.36% | -6.45% | -5.72% | 37.01% | -16.55% | -0.603 | 0.597 | 1.775 | -18.12% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | -1.20% | -3.69% | -1.38% | 10.17% | -4.71% | -0.935 | 0.776 | 0.702 | -4.70% |
| BIOTECH | XBI | healthcare_and_biotech | 0.33% | -6.85% | 21.55% | 29.19% | -10.51% | -0.336 | 0.487 | 1.061 | -7.57% |
| REGIONAL_BANKS | KRE | financials | -1.56% | -2.29% | 2.88% | 16.65% | -6.81% | -0.483 | 0.417 | 0.717 | -6.65% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | -2.25% | -12.31% | -8.82% | 20.92% | -15.45% | -0.200 | 0.567 | 1.022 | -15.45% |
| CANADA | EWC | international_equity | -0.59% | -1.89% | -2.36% | 11.05% | -4.44% | -0.408 | 0.679 | 0.763 | -3.86% |
| UNITED_KINGDOM | EWU | international_equity | -1.40% | -1.96% | -7.96% | 11.75% | -4.29% | -0.562 | 0.602 | 0.702 | -4.29% |
| AUSTRALIA | EWA | international_equity | -1.78% | -3.36% | -9.63% | 15.88% | -6.38% | -0.007 | 0.677 | 0.944 | -5.52% |
| SOUTH_KOREA | EWY | international_equity | -3.93% | 4.66% | 12.20% | 65.95% | -34.21% | -0.966 | 0.635 | 2.792 | -17.29% |
| TAIWAN | EWT | international_equity | 0.66% | 7.34% | 27.95% | 36.28% | -19.83% | -1.088 | 0.751 | 1.841 | -0.48% |
| BRAZIL | EWZ | international_equity | -1.75% | 10.23% | -22.42% | 21.71% | -8.05% | -0.098 | 0.478 | 0.937 | -9.23% |
| MEXICO | EWW | international_equity | -2.71% | -1.68% | -11.56% | 17.16% | -6.37% | -0.668 | 0.553 | 0.946 | -8.39% |
| SOUTH_AFRICA | EZA | international_equity | -2.30% | -1.85% | -6.63% | 26.74% | -9.45% | -0.373 | 0.634 | 1.631 | -14.29% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | -0.10% | -1.37% | -17.01% | 4.84% | -2.89% | 0.251 | 0.392 | 0.137 | -3.42% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | -0.28% | -1.67% | -16.94% | 3.52% | -3.98% | 3.697 | 0.395 | 0.094 | -3.83% |
| EMERGING_MARKET_BONDS | EMB | credit | 0.04% | -0.67% | -14.45% | 4.97% | -2.71% | -0.280 | 0.687 | 0.304 | -2.30% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | 0.13% | -0.48% | -16.81% | 3.67% | -2.69% | -0.278 | 0.469 | 0.133 | -2.79% |
| SILVER | SLV | precious_metals | 3.11% | 0.58% | -25.81% | 40.85% | -15.33% | -0.570 | 0.370 | 1.795 | -43.25% |
| COPPER | CPER | non_energy_commodities | 2.68% | 2.85% | -0.37% | 24.53% | -6.80% | -0.277 | 0.556 | 1.249 | -2.00% |
| AGRICULTURE | DBA | non_energy_commodities | -2.70% | 0.22% | -12.29% | 13.70% | -4.54% | 0.467 | 0.028 | 0.024 | -4.54% |
| OIL | USO | energy | -0.70% | 18.21% | -5.63% | 51.55% | -17.64% | -0.587 | -0.345 | -1.312 | -4.97% |
| US_DOLLAR | UUP | currencies | 1.14% | 2.54% | -16.09% | 5.05% | -2.52% | -0.948 | -0.300 | -0.130 | -0.73% |
| EURO | FXE | currencies | -0.95% | -0.87% | -16.00% | 4.48% | -1.73% | -0.588 | 0.283 | 0.120 | -4.09% |
| YEN | FXY | currencies | -2.01% | 1.51% | -17.59% | 9.83% | -2.22% | 0.437 | 0.183 | 0.121 | -6.46% |
| BITCOIN_ETF | IBIT | crypto_assets | 5.14% | 19.38% | -19.79% | 38.83% | -8.79% | 0.565 | 0.485 | 1.720 | -35.45% |
| ETHEREUM_ETF | ETHA | crypto_assets | 3.97% | 26.15% | -18.91% | 50.45% | -10.11% | 1.190 | 0.508 | 2.564 | -44.34% |
