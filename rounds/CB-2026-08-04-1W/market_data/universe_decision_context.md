# Full-Universe Horizon-Specific Decision Context

Profile: weekly. All values stop at the requested close and are sorted by frozen option order, not performance.

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
| active_return_dispersion_5s | 3.80% |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_3s | active_return_5s | prior_16s_active_return | volatility_21s | max_drawdown_21s | volume_zscore_5v60 | corr_spy_63s | beta_spy_63s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | -4.11% | 1.39% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.05% | -4.04% | 1.61% | 0.19% | 0.00% | 1.083 | -0.186 | -0.003 | 0.00% |
| SP500 | SPY | diversified_us_equity | 4.00% | 0.00% | 0.00% | 14.34% | -3.38% | 0.860 | 1.000 | 1.000 | 0.00% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | 3.97% | -0.06% | -0.14% | 14.32% | -3.29% | 0.005 | 0.994 | 0.988 | 0.00% |
| NASDAQ100 | QQQ | technology_and_growth | 5.90% | 3.05% | -5.16% | 26.54% | -8.79% | 0.923 | 0.924 | 1.714 | -2.88% |
| LARGE_GROWTH | IWF | technology_and_growth | 5.85% | 2.60% | -3.91% | 24.83% | -7.99% | -0.626 | 0.908 | 1.350 | -3.39% |
| LARGE_VALUE | IWD | diversified_us_equity | 2.36% | -2.29% | 3.33% | 10.00% | -1.31% | -0.303 | 0.727 | 0.603 | 0.00% |
| MID_CAP | IJH | diversified_us_equity | 2.83% | -2.21% | 0.88% | 13.95% | -2.21% | 0.047 | 0.805 | 0.841 | 0.00% |
| SMALL_CAP | IWM | diversified_us_equity | 3.12% | -1.27% | -0.46% | 15.91% | -3.46% | -0.032 | 0.791 | 1.040 | 0.00% |
| SMALL_VALUE | IWN | diversified_us_equity | 2.34% | -2.84% | 2.46% | 12.73% | -1.83% | 0.725 | 0.676 | 0.719 | 0.00% |
| DIVIDEND | SCHD | diversified_us_equity | 1.32% | -4.23% | 6.50% | 13.27% | -1.42% | 2.392 | 0.084 | 0.068 | -0.12% |
| LOW_VOL | SPLV | diversified_us_equity | 0.01% | -6.14% | 3.94% | 13.40% | -2.26% | 0.094 | -0.297 | -0.276 | -2.03% |
| MOMENTUM | MTUM | diversified_us_equity | 4.88% | 3.08% | -7.75% | 39.53% | -12.01% | 0.650 | 0.747 | 2.074 | -9.23% |
| TECHNOLOGY | XLK | technology_and_growth | 6.36% | 5.13% | -5.41% | 36.69% | -10.34% | -0.001 | 0.848 | 2.161 | -5.59% |
| COMMUNICATIONS | XLC | technology_and_growth | 5.12% | -1.95% | 0.90% | 24.67% | -7.06% | 0.302 | 0.402 | 0.537 | -6.15% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | 5.25% | 1.05% | -3.30% | 25.58% | -7.84% | 0.565 | 0.690 | 1.065 | -4.62% |
| CONSUMER_STAPLES | XLP | consumer_defensive | -0.12% | -6.05% | 4.91% | 19.67% | -3.03% | 0.560 | -0.319 | -0.384 | -3.96% |
| HEALTHCARE | XLV | healthcare_and_biotech | -0.87% | -7.20% | 4.66% | 18.45% | -3.74% | 0.544 | -0.176 | -0.226 | -3.09% |
| FINANCIALS | XLF | financials | 1.54% | -3.63% | 3.99% | 13.35% | -2.08% | -0.038 | 0.271 | 0.259 | 0.00% |
| INDUSTRIALS | XLI | industrials_and_defense | 4.49% | -1.97% | -0.27% | 18.69% | -4.80% | 0.657 | 0.683 | 0.942 | 0.00% |
| ENERGY | XLE | energy | -0.75% | -2.46% | 9.74% | 21.45% | -3.44% | -0.677 | -0.381 | -0.644 | -5.78% |
| MATERIALS | XLB | materials_and_mining | 0.70% | -4.76% | 2.08% | 20.74% | -3.75% | 0.822 | 0.502 | 0.733 | -2.23% |
| UTILITIES | XLU | rate_sensitive_defensive | -1.23% | -7.21% | 1.87% | 13.46% | -4.71% | 0.798 | -0.107 | -0.123 | -6.34% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | -0.29% | -5.94% | 5.27% | 14.85% | -2.04% | 1.008 | -0.138 | -0.154 | -1.83% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | 0.39% | -4.10% | 0.73% | 4.52% | -1.41% | -0.295 | 0.532 | 0.188 | -2.96% |
| LONG_TREASURY | TLT | rates_and_duration | 0.43% | -5.40% | -0.03% | 9.23% | -3.74% | 2.201 | 0.443 | 0.293 | -6.72% |
| TIPS | TIP | rates_and_duration | 0.09% | -3.95% | 0.62% | 2.50% | -1.01% | 0.613 | 0.491 | 0.118 | -1.12% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | 0.76% | -3.75% | -0.31% | 5.43% | -2.25% | 1.056 | 0.612 | 0.233 | -2.21% |
| HIGH_YIELD_CREDIT | HYG | credit | 0.59% | -3.46% | 0.82% | 2.99% | -0.80% | 0.677 | 0.791 | 0.200 | 0.00% |
| AGGREGATE_BONDS | AGG | rates_and_duration | 0.39% | -4.03% | 0.64% | 3.99% | -1.34% | 0.514 | 0.580 | 0.170 | -1.74% |
| DEVELOPED_EX_US | VEA | international_equity | 1.59% | -0.35% | -1.80% | 18.93% | -4.09% | -0.214 | 0.825 | 1.216 | -0.23% |
| EMERGING_MARKETS | VWO | international_equity | 3.20% | -0.11% | -2.49% | 19.32% | -5.24% | -0.004 | 0.862 | 1.263 | -1.94% |
| EUROPE | VGK | international_equity | 0.93% | -1.19% | 0.56% | 14.46% | -2.53% | -0.056 | 0.724 | 0.886 | 0.00% |
| JAPAN | EWJ | international_equity | 1.41% | 1.21% | -4.32% | 26.29% | -6.21% | -0.377 | 0.768 | 1.274 | -2.43% |
| CHINA | MCHI | international_equity | 1.06% | -1.03% | 5.98% | 17.39% | -2.22% | 0.060 | 0.428 | 0.625 | -14.69% |
| INDIA | INDA | international_equity | 1.67% | -1.78% | 0.38% | 14.29% | -4.51% | 0.368 | 0.573 | 0.635 | -8.61% |
| GOLD | IAU | precious_metals | -0.79% | -2.80% | -1.93% | 20.50% | -4.47% | -0.185 | 0.615 | 1.022 | -24.50% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | -3.43% | -5.05% | 7.35% | 26.53% | -6.42% | 0.212 | -0.225 | -0.355 | -10.63% |
| SEMICONDUCTORS | SMH | technology_and_growth | 6.83% | 4.59% | -10.97% | 52.69% | -17.48% | 0.192 | 0.788 | 3.098 | -13.93% |
| SOFTWARE | IGV | technology_and_growth | 9.31% | 7.02% | -1.79% | 29.84% | -8.11% | -0.694 | 0.398 | 0.958 | -13.39% |
| BROAD_AI_TECH | AIQ | technology_and_growth | 7.57% | 6.18% | -8.95% | 37.95% | -12.31% | 0.173 | 0.833 | 2.407 | -9.99% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | 9.52% | 5.78% | -11.31% | 40.03% | -15.79% | 0.052 | 0.874 | 2.469 | -13.20% |
| CYBERSECURITY | CIBR | technology_and_growth | 8.80% | 5.59% | -2.52% | 29.06% | -7.40% | -0.307 | 0.494 | 1.149 | 0.00% |
| SOLAR | TAN | clean_energy | 7.08% | 4.58% | -13.28% | 45.67% | -17.14% | 0.381 | 0.748 | 2.476 | -27.81% |
| METALS_MINING | XME | materials_and_mining | 5.89% | 2.22% | -2.99% | 40.11% | -8.01% | -0.090 | 0.711 | 2.078 | -18.74% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | 2.25% | -2.95% | 2.64% | 11.32% | -1.46% | 0.317 | 0.705 | 0.552 | 0.00% |
| BIOTECH | XBI | healthcare_and_biotech | 0.28% | -2.71% | -5.47% | 29.35% | -10.51% | -0.572 | 0.384 | 0.835 | -7.55% |
| REGIONAL_BANKS | KRE | financials | 2.56% | -2.75% | 3.01% | 19.14% | -3.55% | -0.343 | 0.215 | 0.298 | -0.10% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | 5.26% | -1.80% | -0.93% | 26.71% | -8.58% | -0.394 | 0.511 | 0.929 | -0.05% |
| CANADA | EWC | international_equity | 0.35% | -3.85% | 4.45% | 10.44% | -1.46% | 0.414 | 0.612 | 0.511 | 0.00% |
| UNITED_KINGDOM | EWU | international_equity | -0.70% | -3.03% | 2.66% | 12.83% | -1.93% | 0.114 | 0.438 | 0.496 | -0.70% |
| AUSTRALIA | EWA | international_equity | 1.01% | -1.38% | 4.88% | 17.11% | -1.61% | -0.014 | 0.628 | 0.820 | 0.00% |
| SOUTH_KOREA | EWY | international_equity | 6.16% | 8.89% | -18.84% | 78.72% | -24.04% | 1.810 | 0.713 | 4.184 | -21.93% |
| TAIWAN | EWT | international_equity | 8.73% | 4.68% | -11.03% | 48.62% | -16.65% | 0.171 | 0.798 | 2.520 | -8.36% |
| BRAZIL | EWZ | international_equity | -1.20% | -4.00% | 4.62% | 23.45% | -3.14% | -0.363 | 0.421 | 0.696 | -12.69% |
| MEXICO | EWW | international_equity | -0.06% | -3.75% | 1.84% | 17.85% | -2.98% | -0.095 | 0.621 | 0.889 | -3.74% |
| SOUTH_AFRICA | EZA | international_equity | 2.89% | 2.31% | -2.71% | 26.28% | -6.50% | -0.380 | 0.754 | 1.733 | -17.40% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | 0.37% | -4.15% | 0.74% | 5.01% | -1.48% | 1.201 | 0.577 | 0.203 | -1.67% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | 0.27% | -4.07% | -0.07% | 3.51% | -2.15% | 0.547 | 0.570 | 0.125 | -1.42% |
| EMERGING_MARKET_BONDS | EMB | credit | 0.89% | -3.64% | 0.18% | 5.51% | -1.89% | 0.508 | 0.759 | 0.314 | -0.81% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | 0.44% | -3.90% | 0.91% | 4.17% | -1.06% | -0.522 | 0.556 | 0.165 | -1.14% |
| SILVER | SLV | precious_metals | 0.64% | 0.03% | -6.47% | 38.08% | -10.19% | -0.654 | 0.609 | 2.130 | -49.02% |
| COPPER | CPER | non_energy_commodities | 2.03% | 0.61% | 2.68% | 21.71% | -3.26% | -0.345 | 0.685 | 1.392 | -1.13% |
| AGRICULTURE | DBA | non_energy_commodities | 0.66% | -4.76% | 2.48% | 13.15% | -2.69% | -0.772 | 0.110 | 0.109 | -3.72% |
| OIL | USO | energy | -9.18% | -8.02% | 16.85% | 68.94% | -17.00% | -0.366 | -0.384 | -1.466 | -24.31% |
| US_DOLLAR | UUP | currencies | 0.07% | -5.58% | 2.31% | 5.45% | -1.61% | 1.161 | -0.453 | -0.159 | -1.54% |
| EURO | FXE | currencies | -0.02% | -2.84% | 0.95% | 4.46% | -0.81% | -0.384 | 0.477 | 0.163 | -3.82% |
| YEN | FXY | currencies | 0.99% | -0.27% | 0.34% | 11.13% | -1.30% | 5.086 | 0.255 | 0.133 | -7.43% |
| BITCOIN_ETF | IBIT | crypto_assets | -0.84% | -3.42% | 1.44% | 28.73% | -5.39% | -0.185 | 0.458 | 1.183 | -48.95% |
| ETHEREUM_ETF | ETHA | crypto_assets | -2.48% | -6.46% | 8.32% | 40.22% | -4.35% | -0.114 | 0.538 | 1.988 | -61.33% |
