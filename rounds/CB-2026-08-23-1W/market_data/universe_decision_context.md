# Full-Universe Horizon-Specific Decision Context

Profile: weekly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: yahoo_chart_adjusted_close_and_reported_volume
- As-of date requested: 2026-08-21
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | -1.37% |
| spy_return_21s | 3.73% |
| rsp_return_5s | -0.49% |
| rsp_return_21s | 4.60% |
| hyg_return_5s | -0.13% |
| hyg_return_21s | 0.97% |
| tlt_return_5s | 0.01% |
| tlt_return_21s | -0.95% |
| uup_return_5s | -0.75% |
| uup_return_21s | -2.31% |
| uso_return_5s | 6.35% |
| uso_return_21s | -3.48% |
| iau_return_5s | 5.48% |
| iau_return_21s | 13.97% |
| rsp_minus_spy_5s | 0.87% |
| rsp_minus_spy_21s | 0.87% |
| positive_asset_share_5s | 39.13% |
| positive_asset_share_21s | 82.61% |
| active_return_dispersion_5s | 5.20% |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_3s | active_return_5s | prior_16s_active_return | volatility_21s | max_drawdown_21s | volume_zscore_5v60 | corr_spy_63s | beta_spy_63s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | 1.37% | -5.17% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.04% | 1.44% | -4.93% | 0.18% | 0.00% | -0.715 | -0.111 | -0.002 | 0.00% |
| SP500 | SPY | diversified_us_equity | -0.23% | 0.00% | 0.00% | 12.85% | -1.96% | -0.770 | 1.000 | 1.000 | -1.56% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | -0.21% | -0.09% | 0.08% | 13.09% | -2.01% | -0.103 | 0.993 | 0.988 | -1.58% |
| NASDAQ100 | QQQ | technology_and_growth | -0.57% | -1.04% | 0.48% | 22.41% | -4.37% | -0.511 | 0.920 | 1.723 | -4.28% |
| LARGE_GROWTH | IWF | technology_and_growth | -0.55% | -0.95% | 0.48% | 20.48% | -3.83% | -0.563 | 0.905 | 1.381 | -4.87% |
| LARGE_VALUE | IWD | diversified_us_equity | 0.22% | 0.87% | -0.14% | 9.52% | -1.00% | -0.249 | 0.707 | 0.580 | -0.57% |
| MID_CAP | IJH | diversified_us_equity | -0.61% | -1.05% | -0.90% | 13.68% | -2.92% | -0.495 | 0.793 | 0.799 | -2.42% |
| SMALL_CAP | IWM | diversified_us_equity | -0.09% | -0.31% | -0.72% | 15.34% | -2.43% | -0.820 | 0.784 | 0.968 | -1.68% |
| SMALL_VALUE | IWN | diversified_us_equity | 0.16% | 0.22% | -2.06% | 11.21% | -1.59% | -1.306 | 0.653 | 0.646 | -1.15% |
| DIVIDEND | SCHD | diversified_us_equity | 1.74% | 3.08% | 0.07% | 11.89% | -1.42% | 0.346 | 0.111 | 0.100 | 0.00% |
| LOW_VOL | SPLV | diversified_us_equity | -0.95% | -0.01% | -5.17% | 9.20% | -3.41% | -0.509 | -0.288 | -0.270 | -3.41% |
| MOMENTUM | MTUM | diversified_us_equity | -2.13% | -2.43% | -4.14% | 34.97% | -9.83% | -0.563 | 0.700 | 1.970 | -11.60% |
| TECHNOLOGY | XLK | technology_and_growth | -1.24% | -2.16% | 1.31% | 32.56% | -6.66% | -1.004 | 0.831 | 2.124 | -7.41% |
| COMMUNICATIONS | XLC | technology_and_growth | 0.83% | -0.00% | 2.01% | 20.82% | -2.82% | -1.122 | 0.403 | 0.575 | -6.69% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | 1.43% | 1.22% | 3.51% | 19.32% | -2.92% | -0.628 | 0.669 | 1.067 | -4.84% |
| CONSUMER_STAPLES | XLP | consumer_defensive | 0.48% | 1.25% | -1.71% | 16.46% | -3.07% | -0.151 | -0.283 | -0.360 | -3.26% |
| HEALTHCARE | XLV | healthcare_and_biotech | 2.88% | 5.70% | -1.50% | 20.16% | -3.09% | -0.044 | -0.133 | -0.192 | -0.60% |
| FINANCIALS | XLF | financials | -0.62% | 0.20% | -1.00% | 11.94% | -2.25% | -0.157 | 0.292 | 0.280 | -1.34% |
| INDUSTRIALS | XLI | industrials_and_defense | -1.81% | -1.99% | -2.66% | 17.60% | -3.61% | -0.610 | 0.658 | 0.887 | -3.36% |
| ENERGY | XLE | energy | -0.06% | 4.16% | -0.91% | 24.60% | -3.87% | -0.793 | -0.323 | -0.548 | -0.17% |
| MATERIALS | XLB | materials_and_mining | 3.40% | 3.27% | -0.70% | 19.87% | -3.65% | -0.504 | 0.430 | 0.610 | 0.00% |
| UTILITIES | XLU | rate_sensitive_defensive | -2.84% | -2.11% | -9.24% | 12.76% | -7.60% | -0.419 | -0.117 | -0.136 | -9.19% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | 1.01% | 0.95% | -4.46% | 14.06% | -4.19% | 0.270 | -0.165 | -0.191 | -2.02% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | -0.12% | 1.13% | -4.62% | 4.81% | -0.65% | -0.229 | 0.461 | 0.159 | -3.40% |
| LONG_TREASURY | TLT | rates_and_duration | 0.48% | 1.38% | -6.13% | 11.75% | -3.04% | 0.599 | 0.342 | 0.237 | -7.59% |
| TIPS | TIP | rates_and_duration | 0.10% | 1.50% | -4.90% | 3.04% | -0.36% | 0.408 | 0.410 | 0.105 | -1.04% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | 0.08% | 1.18% | -4.87% | 5.84% | -0.99% | 0.252 | 0.539 | 0.206 | -2.98% |
| HIGH_YIELD_CREDIT | HYG | credit | 0.10% | 1.24% | -4.08% | 2.65% | -0.33% | 0.013 | 0.823 | 0.184 | -0.23% |
| AGGREGATE_BONDS | AGG | rates_and_duration | 0.00% | 1.23% | -4.68% | 4.17% | -0.56% | -0.564 | 0.506 | 0.144 | -2.05% |
| DEVELOPED_EX_US | VEA | international_equity | 1.42% | 1.15% | 0.28% | 15.82% | -1.76% | -0.113 | 0.804 | 1.117 | -0.37% |
| EMERGING_MARKETS | VWO | international_equity | 1.36% | 1.93% | -1.71% | 14.10% | -2.25% | -0.832 | 0.842 | 1.180 | -1.29% |
| EUROPE | VGK | international_equity | 1.28% | 1.75% | -0.00% | 10.77% | -1.13% | -0.207 | 0.732 | 0.761 | 0.00% |
| JAPAN | EWJ | international_equity | -0.20% | -1.72% | 2.64% | 23.58% | -4.27% | -0.557 | 0.752 | 1.304 | -3.34% |
| CHINA | MCHI | international_equity | 1.38% | 3.25% | -2.77% | 14.22% | -4.41% | -0.728 | 0.404 | 0.553 | -15.34% |
| INDIA | INDA | international_equity | 0.53% | 1.09% | -0.66% | 10.09% | -2.28% | -1.246 | 0.589 | 0.555 | -10.22% |
| GOLD | IAU | precious_metals | 6.22% | 6.85% | 2.88% | 24.77% | -1.68% | 0.251 | 0.477 | 0.907 | -14.55% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | 2.47% | 5.50% | -6.00% | 25.43% | -6.42% | -0.433 | -0.184 | -0.294 | -1.37% |
| SEMICONDUCTORS | SMH | technology_and_growth | -1.64% | -3.29% | -3.85% | 45.65% | -13.09% | -0.465 | 0.748 | 2.921 | -16.22% |
| SOFTWARE | IGV | technology_and_growth | 1.38% | 0.69% | 14.33% | 30.91% | -4.11% | -1.123 | 0.475 | 1.224 | -12.23% |
| BROAD_AI_TECH | AIQ | technology_and_growth | 1.44% | 0.17% | 3.04% | 31.24% | -5.65% | -0.792 | 0.826 | 2.371 | -9.57% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | -0.96% | -2.32% | 6.42% | 36.43% | -6.24% | -1.147 | 0.861 | 2.383 | -12.68% |
| CYBERSECURITY | CIBR | technology_and_growth | -2.66% | -3.40% | 8.37% | 28.48% | -8.56% | 0.402 | 0.553 | 1.337 | -7.19% |
| SOLAR | TAN | clean_energy | -1.10% | -3.73% | -6.83% | 41.37% | -9.78% | 0.255 | 0.762 | 2.477 | -33.29% |
| METALS_MINING | XME | materials_and_mining | 5.03% | 3.25% | 8.37% | 43.42% | -5.42% | 0.737 | 0.649 | 1.985 | -10.09% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | 0.86% | 0.87% | -0.05% | 11.22% | -1.34% | -1.087 | 0.702 | 0.568 | -0.49% |
| BIOTECH | XBI | healthcare_and_biotech | 3.51% | 6.65% | -1.77% | 32.52% | -3.64% | 0.616 | 0.303 | 0.694 | -2.25% |
| REGIONAL_BANKS | KRE | financials | -2.59% | -2.57% | -1.47% | 14.94% | -4.13% | 0.414 | 0.166 | 0.229 | -3.94% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | -5.88% | -4.90% | 1.12% | 25.18% | -6.27% | -0.777 | 0.437 | 0.807 | -6.27% |
| CANADA | EWC | international_equity | 1.27% | 1.58% | 0.63% | 9.56% | -1.04% | 1.202 | 0.591 | 0.499 | 0.00% |
| UNITED_KINGDOM | EWU | international_equity | 1.62% | 2.78% | -1.83% | 9.18% | -1.07% | -0.606 | 0.397 | 0.370 | 0.00% |
| AUSTRALIA | EWA | international_equity | 1.79% | 3.02% | -1.10% | 17.13% | -2.83% | -0.560 | 0.581 | 0.704 | -0.89% |
| SOUTH_KOREA | EWY | international_equity | 4.88% | 0.59% | -1.79% | 73.73% | -17.05% | -0.359 | 0.667 | 3.897 | -18.64% |
| TAIWAN | EWT | international_equity | -0.09% | -1.22% | 2.07% | 38.60% | -10.45% | -1.234 | 0.780 | 2.446 | -6.48% |
| BRAZIL | EWZ | international_equity | 4.04% | 4.70% | -11.36% | 22.44% | -8.05% | -0.085 | 0.380 | 0.597 | -15.18% |
| MEXICO | EWW | international_equity | 3.92% | 4.53% | -5.16% | 16.71% | -3.95% | 0.147 | 0.578 | 0.814 | -3.34% |
| SOUTH_AFRICA | EZA | international_equity | 8.06% | 8.74% | 6.58% | 28.44% | -3.77% | -0.642 | 0.664 | 1.534 | -9.19% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | 0.04% | 1.28% | -4.46% | 5.06% | -0.80% | 0.791 | 0.509 | 0.169 | -1.85% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | -0.03% | 0.88% | -4.33% | 3.16% | -0.77% | 0.915 | 0.537 | 0.119 | -1.81% |
| EMERGING_MARKET_BONDS | EMB | credit | 0.08% | 1.02% | -4.18% | 5.57% | -0.76% | -0.574 | 0.738 | 0.292 | -1.33% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | 0.13% | 1.22% | -4.90% | 3.73% | -0.83% | -0.001 | 0.509 | 0.129 | -1.80% |
| SILVER | SLV | precious_metals | 9.19% | 8.62% | 7.16% | 35.73% | -3.58% | 0.088 | 0.550 | 1.780 | -40.61% |
| COPPER | CPER | non_energy_commodities | 2.07% | 1.32% | -0.54% | 18.62% | -4.09% | 0.453 | 0.633 | 1.162 | -2.11% |
| AGRICULTURE | DBA | non_energy_commodities | 1.03% | 3.35% | -6.83% | 13.84% | -2.87% | 0.127 | 0.141 | 0.132 | -1.43% |
| OIL | USO | energy | 3.05% | 7.72% | -14.41% | 60.16% | -17.64% | -0.814 | -0.327 | -1.248 | -11.98% |
| US_DOLLAR | UUP | currencies | -0.85% | 0.62% | -6.75% | 5.60% | -2.52% | -1.628 | -0.385 | -0.144 | -2.45% |
| EURO | FXE | currencies | 0.90% | 2.31% | -3.41% | 4.78% | -0.32% | -0.332 | 0.402 | 0.144 | -2.53% |
| YEN | FXY | currencies | 0.38% | 1.58% | -2.37% | 12.21% | -1.74% | -0.219 | 0.254 | 0.146 | -8.15% |
| BITCOIN_ETF | IBIT | crypto_assets | 19.34% | 23.96% | -7.95% | 39.75% | -3.18% | 2.528 | 0.330 | 0.997 | -38.73% |
| ETHEREUM_ETF | ETHA | crypto_assets | 26.32% | 30.00% | -4.67% | 55.68% | -4.35% | 3.490 | 0.410 | 1.778 | -50.15% |
