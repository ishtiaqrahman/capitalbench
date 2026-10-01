# Full-Universe Horizon-Specific Decision Context

Profile: monthly. All values stop at the requested close and are sorted by frozen option order, not performance.

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
| active_return_dispersion_5s |  |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_5s | active_return_21s | prior_105s_active_return | volatility_63s | max_drawdown_63s | volume_zscore_20v120 | corr_spy_252s | beta_spy_252s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | 0.33% | -18.25% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.05% | 0.61% | -16.75% | 0.20% | -0.01% | 0.161 | -0.077 | -0.001 | -0.01% |
| SP500 | SPY | diversified_us_equity | -0.67% | 0.00% | 0.00% | 11.06% | -3.38% | -0.513 | 1.000 | 1.000 | -1.72% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | -1.05% | -0.70% | -0.03% | 11.22% | -3.39% | -0.553 | 0.995 | 1.012 | -2.62% |
| NASDAQ100 | QQQ | technology_and_growth | -0.19% | 3.64% | 6.07% | 19.47% | -8.79% | -0.752 | 0.929 | 1.425 | -1.03% |
| LARGE_GROWTH | IWF | technology_and_growth | -0.10% | 2.50% | -3.04% | 18.35% | -7.99% | -0.547 | 0.934 | 1.287 | -2.55% |
| LARGE_VALUE | IWD | diversified_us_equity | -1.39% | -2.81% | 2.37% | 9.19% | -4.06% | -0.394 | 0.807 | 0.703 | -4.06% |
| MID_CAP | IJH | diversified_us_equity | -1.48% | -3.89% | -6.39% | 11.66% | -8.26% | -0.310 | 0.816 | 0.966 | -8.26% |
| SMALL_CAP | IWM | diversified_us_equity | -1.43% | -4.88% | 0.55% | 13.13% | -8.68% | -0.404 | 0.822 | 1.181 | -8.68% |
| SMALL_VALUE | IWN | diversified_us_equity | -1.81% | -4.85% | -0.83% | 10.82% | -7.53% | -0.420 | 0.741 | 0.926 | -7.53% |
| DIVIDEND | SCHD | diversified_us_equity | -2.25% | -5.69% | -3.62% | 11.76% | -6.87% | 0.261 | 0.301 | 0.260 | -6.87% |
| LOW_VOL | SPLV | diversified_us_equity | -1.18% | -5.08% | -15.17% | 10.73% | -9.22% | -0.762 | 0.028 | 0.023 | -9.22% |
| MOMENTUM | MTUM | diversified_us_equity | 0.12% | 6.20% | 7.04% | 28.35% | -13.71% | 0.362 | 0.764 | 1.561 | -7.89% |
| TECHNOLOGY | XLK | technology_and_growth | 0.21% | 5.41% | 22.25% | 26.74% | -10.34% | -0.943 | 0.852 | 1.739 | -1.01% |
| COMMUNICATIONS | XLC | technology_and_growth | -1.41% | 0.21% | -17.44% | 20.58% | -7.06% | -0.110 | 0.553 | 0.682 | -6.75% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | -1.64% | -6.11% | -11.05% | 19.15% | -9.00% | -0.578 | 0.775 | 1.162 | -12.05% |
| CONSUMER_STAPLES | XLP | consumer_defensive | -2.22% | -4.20% | -13.86% | 15.96% | -7.22% | -0.324 | -0.049 | -0.055 | -8.73% |
| HEALTHCARE | XLV | healthcare_and_biotech | -0.23% | -0.54% | -1.42% | 17.81% | -5.87% | -0.682 | 0.226 | 0.281 | -3.77% |
| FINANCIALS | XLF | financials | -2.09% | -6.81% | -0.95% | 13.07% | -8.49% | 0.079 | 0.539 | 0.615 | -8.49% |
| INDUSTRIALS | XLI | industrials_and_defense | -1.83% | -4.07% | -9.70% | 14.55% | -10.23% | -0.278 | 0.707 | 0.942 | -10.23% |
| ENERGY | XLE | energy | -1.39% | -2.93% | -13.10% | 21.37% | -6.15% | -0.284 | -0.178 | -0.299 | -6.15% |
| MATERIALS | XLB | materials_and_mining | -3.14% | -6.82% | -12.41% | 17.11% | -8.84% | -0.243 | 0.529 | 0.729 | -8.84% |
| UTILITIES | XLU | rate_sensitive_defensive | -0.78% | -5.59% | -25.64% | 14.48% | -14.58% | 0.805 | 0.124 | 0.145 | -15.65% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | -2.22% | -6.15% | -9.28% | 12.96% | -10.34% | -0.028 | 0.262 | 0.285 | -10.34% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | -0.98% | -3.02% | -19.44% | 5.15% | -4.50% | 0.233 | 0.316 | 0.118 | -6.72% |
| LONG_TREASURY | TLT | rates_and_duration | -3.33% | -5.05% | -21.20% | 9.88% | -8.33% | 1.073 | 0.271 | 0.196 | -12.06% |
| TIPS | TIP | rates_and_duration | -0.73% | -2.27% | -18.14% | 3.75% | -3.43% | -0.052 | 0.286 | 0.077 | -3.90% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | -1.65% | -3.06% | -18.87% | 5.95% | -5.17% | 0.096 | 0.484 | 0.204 | -6.01% |
| HIGH_YIELD_CREDIT | HYG | credit | -1.14% | -2.40% | -15.43% | 3.27% | -2.86% | 0.799 | 0.765 | 0.230 | -2.86% |
| AGGREGATE_BONDS | AGG | rates_and_duration | -0.91% | -2.28% | -18.45% | 4.40% | -3.51% | 0.531 | 0.414 | 0.126 | -4.55% |
| DEVELOPED_EX_US | VEA | international_equity | -1.13% | -2.60% | -3.86% | 15.41% | -4.09% | -0.625 | 0.804 | 1.094 | -4.07% |
| EMERGING_MARKETS | VWO | international_equity | -1.35% | -1.48% | -6.15% | 14.87% | -5.24% | -0.476 | 0.824 | 1.130 | -3.28% |
| EUROPE | VGK | international_equity | -1.37% | -4.73% | -5.54% | 12.39% | -6.62% | -0.316 | 0.749 | 0.916 | -6.62% |
| JAPAN | EWJ | international_equity | 0.42% | 1.98% | -4.09% | 20.78% | -6.21% | -0.671 | 0.728 | 1.195 | -1.34% |
| CHINA | MCHI | international_equity | -1.84% | -4.29% | -20.20% | 16.42% | -8.48% | -0.848 | 0.583 | 0.880 | -20.61% |
| INDIA | INDA | international_equity | -2.85% | -5.75% | -12.14% | 12.71% | -7.62% | -0.561 | 0.577 | 0.686 | -15.57% |
| GOLD | IAU | precious_metals | -3.01% | -6.37% | -23.29% | 24.72% | -11.69% | -0.347 | 0.336 | 0.761 | -23.11% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | -1.58% | 3.81% | -10.57% | 21.40% | -6.42% | -0.305 | -0.187 | -0.298 | -3.98% |
| SEMICONDUCTORS | SMH | technology_and_growth | 1.26% | 9.74% | 26.94% | 40.02% | -18.73% | -0.811 | 0.774 | 2.378 | -8.96% |
| SOFTWARE | IGV | technology_and_growth | -1.50% | -2.85% | 19.17% | 32.42% | -8.27% | -1.154 | 0.490 | 1.201 | -9.04% |
| BROAD_AI_TECH | AIQ | technology_and_growth | -1.26% | 1.67% | 19.53% | 28.13% | -12.31% | -0.768 | 0.851 | 1.928 | -7.10% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | -2.78% | -0.69% | -9.31% | 29.96% | -16.01% | -0.935 | 0.807 | 2.184 | -15.69% |
| CYBERSECURITY | CIBR | technology_and_growth | -0.88% | 3.27% | 41.67% | 33.08% | -9.53% | 0.122 | 0.496 | 1.111 | -0.88% |
| SOLAR | TAN | clean_energy | -2.40% | -7.24% | -32.86% | 35.88% | -25.61% | -0.711 | 0.649 | 1.932 | -40.52% |
| METALS_MINING | XME | materials_and_mining | -5.49% | -11.95% | -8.80% | 36.26% | -15.75% | -0.853 | 0.597 | 1.773 | -21.93% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | -1.56% | -4.50% | -3.49% | 9.91% | -6.27% | -0.841 | 0.779 | 0.700 | -6.27% |
| BIOTECH | XBI | healthcare_and_biotech | 1.60% | -2.64% | 9.10% | 28.98% | -10.51% | -0.188 | 0.482 | 1.043 | -7.00% |
| REGIONAL_BANKS | KRE | financials | -1.34% | -4.73% | -4.68% | 16.25% | -10.38% | 0.094 | 0.423 | 0.719 | -10.38% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | -3.15% | -8.83% | -13.79% | 20.96% | -18.08% | -0.076 | 0.570 | 1.024 | -18.08% |
| CANADA | EWC | international_equity | -2.13% | -4.64% | -5.60% | 11.85% | -6.80% | -0.044 | 0.677 | 0.761 | -6.80% |
| UNITED_KINGDOM | EWU | international_equity | -1.19% | -3.47% | -10.55% | 12.03% | -5.79% | -0.383 | 0.607 | 0.703 | -5.79% |
| AUSTRALIA | EWA | international_equity | -0.18% | -5.37% | -8.57% | 16.16% | -6.97% | 0.214 | 0.681 | 0.948 | -6.97% |
| SOUTH_KOREA | EWY | international_equity | -1.55% | 1.39% | 28.78% | 59.56% | -24.04% | -0.879 | 0.641 | 2.821 | -16.61% |
| TAIWAN | EWT | international_equity | 0.36% | 4.84% | 34.08% | 33.99% | -16.65% | -0.908 | 0.759 | 1.863 | -2.37% |
| BRAZIL | EWZ | international_equity | -0.32% | 3.72% | -23.50% | 22.66% | -8.05% | 0.023 | 0.485 | 0.950 | -9.88% |
| MEXICO | EWW | international_equity | -3.17% | -7.01% | -14.77% | 16.50% | -8.68% | -0.569 | 0.557 | 0.950 | -11.20% |
| SOUTH_AFRICA | EZA | international_equity | -3.70% | -8.92% | -12.06% | 27.47% | -11.76% | -0.173 | 0.631 | 1.625 | -19.93% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | -1.01% | -3.06% | -18.43% | 5.57% | -4.35% | 4.089 | 0.411 | 0.149 | -5.19% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | -0.92% | -3.21% | -17.90% | 4.34% | -6.26% | 7.394 | 0.372 | 0.096 | -5.50% |
| EMERGING_MARKET_BONDS | EMB | credit | -1.96% | -3.40% | -15.12% | 5.74% | -4.89% | 0.285 | 0.694 | 0.316 | -4.96% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | -0.15% | -0.85% | -18.11% | 3.90% | -2.47% | 0.104 | 0.480 | 0.138 | -3.16% |
| SILVER | SLV | precious_metals | -6.28% | -9.02% | -30.00% | 39.28% | -13.16% | -0.637 | 0.372 | 1.803 | -48.38% |
| COPPER | CPER | non_energy_commodities | -2.04% | -0.22% | -2.07% | 23.14% | -6.80% | -0.176 | 0.569 | 1.264 | -3.98% |
| AGRICULTURE | DBA | non_energy_commodities | -1.44% | -3.69% | -10.93% | 13.83% | -4.58% | -0.139 | 0.055 | 0.047 | -4.58% |
| OIL | USO | energy | -2.13% | 9.28% | -13.18% | 51.96% | -17.64% | -0.488 | -0.348 | -1.329 | -10.01% |
| US_DOLLAR | UUP | currencies | 0.42% | 2.64% | -17.02% | 5.12% | -2.52% | -0.518 | -0.299 | -0.126 | 0.00% |
| EURO | FXE | currencies | -0.51% | -2.11% | -17.39% | 4.41% | -2.94% | -0.457 | 0.284 | 0.117 | -5.39% |
| YEN | FXY | currencies | 0.62% | 1.81% | -19.09% | 10.16% | -3.38% | 0.207 | 0.180 | 0.118 | -6.85% |
| BITCOIN_ETF | IBIT | crypto_assets | -1.13% | 6.31% | -1.98% | 38.41% | -7.14% | 0.074 | 0.500 | 1.758 | -33.60% |
| ETHEREUM_ETF | ETHA | crypto_assets | -0.45% | 7.81% | 0.01% | 48.48% | -5.32% | 0.565 | 0.519 | 2.576 | -43.78% |
