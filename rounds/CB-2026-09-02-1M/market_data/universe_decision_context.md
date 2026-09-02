# Full-Universe Horizon-Specific Decision Context

Profile: monthly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: yahoo_chart_adjusted_close_and_reported_volume
- As-of date requested: 2026-09-01
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | -0.54% |
| spy_return_21s | 0.54% |
| rsp_return_5s | -1.96% |
| rsp_return_21s | 1.20% |
| hyg_return_5s | -0.21% |
| hyg_return_21s | 0.55% |
| tlt_return_5s | -0.46% |
| tlt_return_21s | 0.32% |
| uup_return_5s | 0.89% |
| uup_return_21s | 0.14% |
| uso_return_5s | 11.77% |
| uso_return_21s | 15.46% |
| iau_return_5s | -7.00% |
| iau_return_21s | 6.80% |
| rsp_minus_spy_5s | -1.42% |
| rsp_minus_spy_21s | 0.66% |
| positive_asset_share_5s | 24.64% |
| positive_asset_share_21s | 63.77% |
| active_return_dispersion_5s |  |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_5s | active_return_21s | prior_105s_active_return | volatility_63s | max_drawdown_63s | volume_zscore_20v120 | corr_spy_252s | beta_spy_252s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | -0.54% | -11.96% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.05% | -0.27% | -10.46% | 0.20% | -0.01% | -0.581 | -0.106 | -0.002 | 0.00% |
| SP500 | SPY | diversified_us_equity | -0.54% | 0.00% | 0.00% | 13.78% | -4.49% | -1.125 | 1.000 | 1.000 | -2.07% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | -0.50% | 1.35% | -2.73% | 13.75% | -4.36% | -0.657 | 0.995 | 1.012 | -2.38% |
| NASDAQ100 | QQQ | technology_and_growth | -0.43% | 0.54% | 4.69% | 25.71% | -11.22% | -1.137 | 0.930 | 1.424 | -5.06% |
| LARGE_GROWTH | IWF | technology_and_growth | 0.14% | 1.90% | -6.94% | 21.35% | -11.35% | -0.833 | 0.935 | 1.293 | -5.79% |
| LARGE_VALUE | IWD | diversified_us_equity | -0.92% | 1.10% | 0.67% | 11.21% | -2.40% | -0.664 | 0.798 | 0.695 | -1.09% |
| MID_CAP | IJH | diversified_us_equity | -2.10% | -1.43% | -7.06% | 14.12% | -5.17% | -0.744 | 0.804 | 0.974 | -5.17% |
| SMALL_CAP | IWM | diversified_us_equity | -2.48% | -0.76% | -1.12% | 17.09% | -4.76% | -1.205 | 0.818 | 1.202 | -4.76% |
| SMALL_VALUE | IWN | diversified_us_equity | -1.84% | -1.13% | -0.05% | 13.49% | -3.29% | -1.022 | 0.735 | 0.939 | -3.29% |
| DIVIDEND | SCHD | diversified_us_equity | -0.85% | 3.18% | -3.97% | 11.64% | -2.93% | 0.023 | 0.277 | 0.239 | -1.14% |
| LOW_VOL | SPLV | diversified_us_equity | -1.93% | -2.57% | -12.61% | 12.70% | -4.22% | -0.650 | 0.013 | 0.011 | -4.22% |
| MOMENTUM | MTUM | diversified_us_equity | -1.35% | -1.57% | 6.36% | 38.24% | -17.99% | -0.167 | 0.770 | 1.575 | -14.11% |
| TECHNOLOGY | XLK | technology_and_growth | 1.99% | 4.19% | 14.01% | 34.88% | -15.86% | -1.310 | 0.854 | 1.752 | -7.24% |
| COMMUNICATIONS | XLC | technology_and_growth | -1.28% | 1.90% | -19.60% | 19.72% | -8.61% | -1.057 | 0.569 | 0.670 | -7.13% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | -3.14% | -1.83% | -10.98% | 21.48% | -8.09% | -1.228 | 0.766 | 1.162 | -7.61% |
| CONSUMER_STAPLES | XLP | consumer_defensive | -2.52% | -0.31% | -14.88% | 17.22% | -3.58% | -0.990 | -0.069 | -0.077 | -4.09% |
| HEALTHCARE | XLV | healthcare_and_biotech | -2.07% | 5.27% | -7.57% | 19.46% | -3.74% | -0.934 | 0.218 | 0.273 | -2.28% |
| FINANCIALS | XLF | financials | -1.90% | -0.86% | 1.06% | 13.47% | -2.25% | -0.951 | 0.535 | 0.609 | -1.90% |
| INDUSTRIALS | XLI | industrials_and_defense | -3.50% | -4.50% | -10.90% | 19.16% | -7.39% | -0.963 | 0.710 | 0.955 | -7.39% |
| ENERGY | XLE | energy | 4.37% | 9.63% | -6.51% | 22.63% | -9.46% | -0.902 | -0.179 | -0.306 | 0.00% |
| MATERIALS | XLB | materials_and_mining | -2.82% | 2.71% | -16.48% | 19.60% | -4.75% | -0.527 | 0.530 | 0.738 | -2.98% |
| UTILITIES | XLU | rate_sensitive_defensive | -1.53% | -4.58% | -17.08% | 15.53% | -8.77% | -0.335 | 0.114 | 0.135 | -9.63% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | -2.91% | -3.07% | -6.97% | 15.59% | -4.28% | -0.505 | 0.243 | 0.267 | -4.28% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | -0.62% | -0.76% | -14.98% | 4.93% | -2.11% | 0.088 | 0.286 | 0.104 | -3.81% |
| LONG_TREASURY | TLT | rates_and_duration | -0.46% | -0.22% | -18.76% | 9.80% | -6.26% | 0.236 | 0.239 | 0.177 | -7.44% |
| TIPS | TIP | rates_and_duration | -0.41% | -0.58% | -12.92% | 3.66% | -1.40% | -0.420 | 0.257 | 0.067 | -1.34% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | -0.49% | -0.67% | -14.69% | 5.47% | -2.92% | -0.533 | 0.474 | 0.198 | -3.22% |
| HIGH_YIELD_CREDIT | HYG | credit | -0.21% | 0.01% | -10.98% | 3.11% | -0.80% | -0.686 | 0.778 | 0.230 | -0.48% |
| AGGREGATE_BONDS | AGG | rates_and_duration | -0.46% | -0.47% | -13.94% | 4.11% | -1.71% | -0.317 | 0.394 | 0.117 | -2.30% |
| DEVELOPED_EX_US | VEA | international_equity | -1.30% | 1.57% | -8.91% | 18.99% | -4.85% | -0.783 | 0.800 | 1.082 | -2.28% |
| EMERGING_MARKETS | VWO | international_equity | 1.18% | 2.74% | -9.20% | 18.92% | -7.05% | -0.806 | 0.809 | 1.108 | -0.91% |
| EUROPE | VGK | international_equity | -2.04% | -0.40% | -7.45% | 14.38% | -2.65% | -0.876 | 0.746 | 0.916 | -2.65% |
| JAPAN | EWJ | international_equity | 0.40% | 2.52% | -8.98% | 23.72% | -7.86% | -1.017 | 0.719 | 1.177 | -3.30% |
| CHINA | MCHI | international_equity | -0.95% | -3.03% | -15.96% | 18.59% | -11.15% | -0.700 | 0.542 | 0.845 | -17.24% |
| INDIA | INDA | international_equity | 0.47% | -0.98% | -14.22% | 13.32% | -4.59% | -1.034 | 0.553 | 0.653 | -10.33% |
| GOLD | IAU | precious_metals | -7.00% | 6.26% | -36.08% | 27.32% | -11.40% | -0.359 | 0.313 | 0.707 | -19.91% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | 3.14% | 7.94% | 2.36% | 22.20% | -12.58% | -0.402 | -0.181 | -0.287 | 0.00% |
| SEMICONDUCTORS | SMH | technology_and_growth | -0.29% | 0.33% | 21.05% | 53.71% | -24.62% | -0.785 | 0.781 | 2.398 | -18.49% |
| SOFTWARE | IGV | technology_and_growth | 4.25% | 8.45% | 3.87% | 34.36% | -19.05% | -1.089 | 0.504 | 1.222 | -9.84% |
| BROAD_AI_TECH | AIQ | technology_and_growth | 1.22% | 6.54% | 5.68% | 38.50% | -20.19% | -0.815 | 0.847 | 1.922 | -10.09% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | -1.38% | 3.87% | -19.09% | 37.52% | -22.76% | -1.124 | 0.802 | 2.196 | -16.46% |
| CYBERSECURITY | CIBR | technology_and_growth | 3.19% | 4.22% | 33.26% | 32.55% | -11.74% | 0.012 | 0.531 | 1.160 | -5.87% |
| SOLAR | TAN | clean_energy | -3.02% | -5.55% | -24.43% | 42.80% | -35.16% | -0.472 | 0.628 | 1.887 | -36.62% |
| METALS_MINING | XME | materials_and_mining | -1.78% | 14.48% | -29.39% | 41.76% | -26.49% | -0.028 | 0.596 | 1.777 | -12.78% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | -1.96% | 0.66% | -6.01% | 11.32% | -2.33% | -1.030 | 0.769 | 0.697 | -2.33% |
| BIOTECH | XBI | healthcare_and_biotech | -0.47% | 10.61% | 4.32% | 32.32% | -10.51% | -0.285 | 0.468 | 1.025 | -3.63% |
| REGIONAL_BANKS | KRE | financials | -2.86% | -5.07% | 1.60% | 18.66% | -6.81% | -0.816 | 0.416 | 0.716 | -6.81% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | -3.40% | -6.47% | -16.19% | 25.20% | -10.96% | -0.431 | 0.567 | 1.028 | -10.96% |
| CANADA | EWC | international_equity | -2.45% | 1.49% | -9.36% | 12.32% | -3.26% | -0.347 | 0.669 | 0.745 | -3.26% |
| UNITED_KINGDOM | EWU | international_equity | -1.85% | -1.00% | -9.92% | 12.90% | -2.43% | -0.519 | 0.601 | 0.701 | -2.43% |
| AUSTRALIA | EWA | international_equity | -1.26% | 0.62% | -12.55% | 16.90% | -4.78% | -0.626 | 0.670 | 0.926 | -2.46% |
| SOUTH_KOREA | EWY | international_equity | 1.24% | 11.36% | -5.48% | 76.96% | -34.21% | -0.651 | 0.637 | 2.776 | -19.80% |
| TAIWAN | EWT | international_equity | 6.20% | 13.12% | 16.65% | 41.37% | -19.83% | -1.007 | 0.756 | 1.847 | -1.60% |
| BRAZIL | EWZ | international_equity | 3.98% | -0.76% | -16.21% | 21.74% | -8.05% | -0.383 | 0.492 | 0.954 | -11.53% |
| MEXICO | EWW | international_equity | -1.93% | -2.04% | -13.87% | 19.23% | -5.91% | -0.283 | 0.541 | 0.927 | -5.49% |
| SOUTH_AFRICA | EZA | international_equity | -2.51% | 8.76% | -30.59% | 30.79% | -11.18% | -0.760 | 0.618 | 1.595 | -12.91% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | -0.60% | -0.36% | -13.84% | 4.74% | -1.85% | 0.023 | 0.389 | 0.135 | -2.24% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | -0.75% | -1.24% | -13.34% | 3.05% | -2.48% | 0.689 | 0.384 | 0.092 | -2.48% |
| EMERGING_MARKET_BONDS | EMB | credit | -0.37% | -0.27% | -12.64% | 5.46% | -1.96% | -0.713 | 0.681 | 0.304 | -1.56% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | -0.61% | -1.09% | -13.41% | 3.66% | -1.86% | -0.436 | 0.464 | 0.131 | -2.33% |
| SILVER | SLV | precious_metals | -7.06% | 9.87% | -41.71% | 45.17% | -25.89% | -0.630 | 0.357 | 1.737 | -45.15% |
| COPPER | CPER | non_energy_commodities | -2.50% | -1.78% | -3.25% | 25.07% | -10.57% | -0.464 | 0.552 | 1.223 | -4.36% |
| AGRICULTURE | DBA | non_energy_commodities | 4.20% | 6.65% | -6.11% | 13.29% | -3.67% | -0.177 | 0.067 | 0.058 | 0.00% |
| OIL | USO | energy | 11.77% | 14.92% | 23.43% | 52.93% | -26.69% | -0.630 | -0.343 | -1.304 | -7.82% |
| US_DOLLAR | UUP | currencies | 0.89% | -0.40% | -8.89% | 5.17% | -2.52% | -0.916 | -0.293 | -0.128 | -1.36% |
| EURO | FXE | currencies | -0.59% | 0.03% | -12.99% | 4.91% | -2.39% | -0.682 | 0.270 | 0.117 | -3.24% |
| YEN | FXY | currencies | -0.76% | -1.34% | -13.23% | 7.92% | -2.63% | 0.224 | 0.171 | 0.108 | -8.95% |
| BITCOIN_ETF | IBIT | crypto_assets | -2.15% | 20.48% | -18.52% | 39.76% | -12.51% | 0.444 | 0.472 | 1.656 | -38.62% |
| ETHEREUM_ETF | ETHA | crypto_assets | -1.99% | 28.66% | -17.45% | 58.69% | -18.36% | 0.887 | 0.496 | 2.513 | -49.06% |
