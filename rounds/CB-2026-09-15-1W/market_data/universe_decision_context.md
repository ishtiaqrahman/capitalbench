# Full-Universe Horizon-Specific Decision Context

Profile: weekly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: tiingo_eod_adjusted_price_and_volume
- As-of date requested: 2026-09-14
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | -1.21% |
| spy_return_21s | -2.19% |
| rsp_return_5s | -1.82% |
| rsp_return_21s | -3.47% |
| hyg_return_5s | -0.80% |
| hyg_return_21s | -1.04% |
| tlt_return_5s | -1.56% |
| tlt_return_21s | -1.63% |
| uup_return_5s | 0.32% |
| uup_return_21s | -0.04% |
| uso_return_5s | 10.36% |
| uso_return_21s | 25.30% |
| iau_return_5s | -3.42% |
| iau_return_21s | -1.52% |
| rsp_minus_spy_5s | -0.61% |
| rsp_minus_spy_21s | -1.28% |
| positive_asset_share_5s | 15.94% |
| positive_asset_share_21s | 20.29% |
| active_return_dispersion_5s | 2.61% |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_3s | active_return_5s | prior_16s_active_return | volatility_21s | max_drawdown_21s | volume_zscore_5v60 | corr_spy_63s | beta_spy_63s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | 1.21% | 0.99% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.04% | 1.26% | 1.23% | 0.17% | 0.00% | 0.105 | 0.024 | 0.000 | 0.00% |
| SP500 | SPY | diversified_us_equity | -0.20% | 0.00% | 0.00% | 8.61% | -2.58% | -0.442 | 1.000 | 1.000 | -2.19% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | -0.23% | -0.12% | -0.20% | 8.95% | -2.88% | 0.021 | 0.992 | 0.977 | -2.50% |
| NASDAQ100 | QQQ | technology_and_growth | -1.00% | -0.15% | -0.80% | 12.58% | -3.52% | -0.860 | 0.905 | 1.664 | -4.85% |
| LARGE_GROWTH | IWF | technology_and_growth | -0.98% | -0.53% | -0.80% | 13.51% | -3.68% | -0.592 | 0.893 | 1.458 | -5.75% |
| LARGE_VALUE | IWD | diversified_us_equity | 0.52% | 0.33% | 0.57% | 9.02% | -2.33% | -0.238 | 0.622 | 0.501 | -1.55% |
| MID_CAP | IJH | diversified_us_equity | -1.03% | -1.51% | -2.29% | 11.57% | -6.20% | -0.319 | 0.767 | 0.781 | -6.20% |
| SMALL_CAP | IWM | diversified_us_equity | -0.94% | -1.53% | -1.48% | 12.59% | -5.70% | 0.239 | 0.733 | 0.822 | -5.63% |
| SMALL_VALUE | IWN | diversified_us_equity | -0.47% | -1.09% | 0.04% | 10.05% | -3.72% | -0.779 | 0.578 | 0.516 | -3.51% |
| DIVIDEND | SCHD | diversified_us_equity | 0.73% | -0.11% | 2.06% | 10.88% | -3.46% | 0.564 | 0.034 | 0.033 | -2.47% |
| LOW_VOL | SPLV | diversified_us_equity | -0.27% | -0.02% | -0.78% | 8.40% | -3.34% | -0.309 | -0.166 | -0.158 | -5.15% |
| MOMENTUM | MTUM | diversified_us_equity | -3.10% | -0.48% | -2.55% | 22.10% | -7.93% | -1.103 | 0.634 | 1.791 | -13.19% |
| TECHNOLOGY | XLK | technology_and_growth | -1.91% | -0.39% | -0.84% | 21.17% | -5.62% | -0.592 | 0.794 | 2.000 | -6.92% |
| COMMUNICATIONS | XLC | technology_and_growth | 3.83% | 3.92% | 0.53% | 16.82% | -2.25% | -0.495 | 0.361 | 0.599 | -3.61% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | 0.35% | -0.58% | -2.00% | 16.54% | -5.59% | -0.388 | 0.655 | 1.112 | -9.01% |
| CONSUMER_STAPLES | XLP | consumer_defensive | 1.65% | 1.02% | -0.66% | 15.24% | -5.03% | 0.244 | -0.158 | -0.219 | -5.03% |
| HEALTHCARE | XLV | healthcare_and_biotech | 0.70% | -0.95% | 2.81% | 20.70% | -5.87% | -0.289 | -0.153 | -0.244 | -4.51% |
| FINANCIALS | XLF | financials | -0.05% | -0.63% | 0.71% | 12.84% | -2.89% | 0.074 | 0.361 | 0.379 | -2.61% |
| INDUSTRIALS | XLI | industrials_and_defense | -1.08% | -1.84% | -4.67% | 13.68% | -8.89% | -0.145 | 0.627 | 0.853 | -8.89% |
| ENERGY | XLE | energy | -1.19% | 1.94% | 5.90% | 15.73% | -2.65% | 0.610 | -0.397 | -0.703 | -1.19% |
| MATERIALS | XLB | materials_and_mining | -1.75% | -2.51% | 1.24% | 15.13% | -5.93% | -0.126 | 0.320 | 0.453 | -5.93% |
| UTILITIES | XLU | rate_sensitive_defensive | -2.61% | -1.72% | -1.19% | 14.05% | -5.62% | -0.181 | -0.048 | -0.057 | -11.21% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | -0.67% | -0.64% | -1.65% | 10.67% | -5.09% | 0.006 | -0.072 | -0.086 | -6.28% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | -1.05% | -0.22% | 0.22% | 4.73% | -2.41% | 0.064 | 0.378 | 0.148 | -5.03% |
| LONG_TREASURY | TLT | rates_and_duration | -0.98% | -0.35% | 0.91% | 10.43% | -2.85% | 0.695 | 0.281 | 0.218 | -8.50% |
| TIPS | TIP | rates_and_duration | -0.92% | 0.13% | 0.81% | 4.00% | -1.69% | 0.284 | 0.254 | 0.075 | -2.25% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | -0.96% | 0.09% | 0.40% | 5.82% | -1.98% | 0.176 | 0.444 | 0.189 | -4.06% |
| HIGH_YIELD_CREDIT | HYG | credit | -0.57% | 0.41% | 0.74% | 2.72% | -1.20% | 0.847 | 0.747 | 0.170 | -1.20% |
| AGGREGATE_BONDS | AGG | rates_and_duration | -0.82% | 0.06% | 0.63% | 4.21% | -1.82% | 0.651 | 0.421 | 0.136 | -3.18% |
| DEVELOPED_EX_US | VEA | international_equity | -1.51% | -1.56% | 1.29% | 13.37% | -2.81% | -0.067 | 0.758 | 1.004 | -2.81% |
| EMERGING_MARKETS | VWO | international_equity | -2.07% | -1.77% | 2.81% | 11.71% | -2.98% | -0.179 | 0.798 | 1.080 | -2.98% |
| EUROPE | VGK | international_equity | -1.09% | -1.53% | 0.30% | 9.76% | -4.25% | -0.815 | 0.697 | 0.689 | -4.25% |
| JAPAN | EWJ | international_equity | 0.60% | 0.50% | 0.80% | 17.09% | -4.27% | -0.475 | 0.714 | 1.285 | -0.99% |
| CHINA | MCHI | international_equity | -0.04% | -1.69% | 1.89% | 12.37% | -5.14% | -0.632 | 0.369 | 0.510 | -18.90% |
| INDIA | INDA | international_equity | -0.49% | -1.76% | 0.85% | 11.94% | -4.22% | -0.224 | 0.546 | 0.577 | -12.41% |
| GOLD | IAU | precious_metals | -2.60% | -2.21% | 2.96% | 27.49% | -8.23% | 0.372 | 0.366 | 0.752 | -20.70% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | 0.92% | 5.26% | 7.97% | 17.35% | -2.57% | -0.206 | -0.322 | -0.579 | -1.35% |
| SEMICONDUCTORS | SMH | technology_and_growth | -5.71% | -3.29% | -2.76% | 34.14% | -8.85% | -0.611 | 0.686 | 2.683 | -19.05% |
| SOFTWARE | IGV | technology_and_growth | 4.72% | 3.19% | -0.62% | 41.87% | -8.27% | -0.842 | 0.450 | 1.269 | -9.45% |
| BROAD_AI_TECH | AIQ | technology_and_growth | -1.00% | -0.11% | 0.52% | 19.40% | -3.59% | -0.677 | 0.804 | 2.155 | -9.51% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | -2.00% | -0.96% | -5.05% | 23.14% | -8.34% | -0.400 | 0.822 | 2.201 | -16.84% |
| CYBERSECURITY | CIBR | technology_and_growth | 5.90% | 6.98% | -6.46% | 44.25% | -9.53% | -0.187 | 0.438 | 1.186 | -2.10% |
| SOLAR | TAN | clean_energy | -3.18% | -2.58% | -7.45% | 24.78% | -11.91% | -0.533 | 0.688 | 2.047 | -37.48% |
| METALS_MINING | XME | materials_and_mining | -7.57% | -5.91% | 3.89% | 37.74% | -10.43% | -0.520 | 0.513 | 1.533 | -17.00% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | 0.17% | -0.61% | -0.69% | 9.92% | -4.31% | -0.438 | 0.643 | 0.551 | -3.48% |
| BIOTECH | XBI | healthcare_and_biotech | -1.12% | -2.58% | 5.42% | 32.51% | -7.87% | -0.449 | 0.215 | 0.512 | -7.05% |
| REGIONAL_BANKS | KRE | financials | 0.90% | -0.33% | -2.20% | 15.24% | -6.81% | -0.424 | 0.201 | 0.281 | -4.90% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | -1.22% | -2.71% | -8.66% | 19.24% | -14.39% | 0.680 | 0.390 | 0.689 | -14.39% |
| CANADA | EWC | international_equity | -0.80% | -1.27% | 0.89% | 13.46% | -3.75% | -0.018 | 0.531 | 0.495 | -3.42% |
| UNITED_KINGDOM | EWU | international_equity | 0.17% | -0.19% | 1.67% | 9.42% | -3.77% | -0.139 | 0.301 | 0.289 | -3.00% |
| AUSTRALIA | EWA | international_equity | -1.89% | -2.66% | 2.64% | 14.61% | -4.50% | 1.497 | 0.520 | 0.647 | -4.50% |
| SOUTH_KOREA | EWY | international_equity | -7.63% | -5.49% | 6.73% | 52.33% | -8.13% | -0.559 | 0.599 | 3.367 | -19.61% |
| TAIWAN | EWT | international_equity | -4.07% | -3.22% | 5.34% | 24.98% | -4.43% | -0.909 | 0.726 | 2.266 | -4.43% |
| BRAZIL | EWZ | international_equity | -0.92% | 0.84% | 13.10% | 22.87% | -2.31% | 0.782 | 0.210 | 0.377 | -8.75% |
| MEXICO | EWW | international_equity | -2.20% | -1.15% | 2.55% | 14.66% | -3.89% | -0.653 | 0.521 | 0.693 | -6.54% |
| SOUTH_AFRICA | EZA | international_equity | -3.95% | -3.19% | 7.39% | 28.43% | -5.54% | -0.257 | 0.604 | 1.359 | -14.29% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | -1.08% | -0.40% | 0.52% | 4.78% | -2.36% | 0.556 | 0.456 | 0.176 | -3.50% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | -0.36% | 0.32% | -0.75% | 4.14% | -2.97% | 5.518 | 0.482 | 0.138 | -3.62% |
| EMERGING_MARKET_BONDS | EMB | credit | -1.01% | -0.11% | 0.49% | 4.91% | -1.83% | 1.550 | 0.676 | 0.274 | -2.47% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | -0.64% | 0.11% | 0.28% | 3.98% | -1.80% | 0.144 | 0.466 | 0.137 | -3.04% |
| SILVER | SLV | precious_metals | -6.39% | -3.77% | 3.84% | 41.55% | -9.45% | -0.117 | 0.452 | 1.546 | -46.17% |
| COPPER | CPER | non_energy_commodities | -6.80% | -3.02% | 1.24% | 26.69% | -6.80% | 2.131 | 0.483 | 0.953 | -6.80% |
| AGRICULTURE | DBA | non_energy_commodities | -0.14% | 1.59% | 5.44% | 12.26% | -2.17% | 0.250 | 0.013 | 0.014 | -1.80% |
| OIL | USO | energy | 4.46% | 11.56% | 14.53% | 38.00% | -6.31% | 0.492 | -0.404 | -1.726 | -1.09% |
| US_DOLLAR | UUP | currencies | 0.68% | 1.53% | 0.63% | 5.32% | -1.06% | -0.480 | -0.313 | -0.135 | -1.50% |
| EURO | FXE | currencies | -0.72% | 0.65% | 1.77% | 4.71% | -1.08% | 0.505 | 0.311 | 0.122 | -3.58% |
| YEN | FXY | currencies | -0.45% | 2.50% | 2.97% | 10.68% | -1.41% | 0.176 | 0.289 | 0.228 | -5.40% |
| BITCOIN_ETF | IBIT | crypto_assets | 1.02% | 0.13% | 27.05% | 45.85% | -5.76% | -0.262 | 0.333 | 1.035 | -37.24% |
| ETHEREUM_ETF | ETHA | crypto_assets | 3.18% | 4.72% | 31.14% | 56.68% | -4.35% | 0.933 | 0.339 | 1.420 | -46.44% |
