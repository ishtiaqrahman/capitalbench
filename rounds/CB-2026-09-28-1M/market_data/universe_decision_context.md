# Full-Universe Horizon-Specific Decision Context

Profile: monthly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: tiingo_eod_adjusted_price_and_volume
- As-of date requested: 2026-09-25
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | 1.27% |
| spy_return_21s | 0.94% |
| rsp_return_5s | -0.18% |
| rsp_return_21s | -4.60% |
| hyg_return_5s | -0.85% |
| hyg_return_21s | -2.02% |
| tlt_return_5s | -2.38% |
| tlt_return_21s | -4.41% |
| uup_return_5s | 0.81% |
| uup_return_21s | 2.14% |
| uso_return_5s | -3.57% |
| uso_return_21s | 16.47% |
| iau_return_5s | -1.91% |
| iau_return_21s | -6.61% |
| rsp_minus_spy_5s | -1.45% |
| rsp_minus_spy_21s | -5.53% |
| positive_asset_share_5s | 43.48% |
| positive_asset_share_21s | 34.78% |
| active_return_dispersion_5s |  |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_5s | active_return_21s | prior_105s_active_return | volatility_63s | max_drawdown_63s | volume_zscore_20v120 | corr_spy_252s | beta_spy_252s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | -0.94% | -19.06% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.08% | -0.64% | -17.55% | 0.20% | -0.01% | -0.109 | -0.074 | -0.001 | 0.00% |
| SP500 | SPY | diversified_us_equity | 1.27% | 0.00% | 0.00% | 11.47% | -3.38% | -0.603 | 1.000 | 1.000 | -0.59% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | 1.16% | -0.53% | 0.02% | 11.40% | -3.39% | -0.653 | 0.995 | 1.011 | -1.18% |
| NASDAQ100 | QQQ | technology_and_growth | 3.30% | 3.83% | 5.06% | 20.46% | -10.14% | -0.773 | 0.929 | 1.425 | -0.40% |
| LARGE_GROWTH | IWF | technology_and_growth | 2.43% | 2.85% | -3.65% | 19.31% | -8.15% | -0.554 | 0.934 | 1.288 | -1.78% |
| LARGE_VALUE | IWD | diversified_us_equity | 0.09% | -3.11% | 2.94% | 9.03% | -2.97% | -0.466 | 0.807 | 0.702 | -2.52% |
| MID_CAP | IJH | diversified_us_equity | 0.01% | -5.38% | -4.77% | 11.80% | -7.27% | -0.500 | 0.816 | 0.966 | -6.93% |
| SMALL_CAP | IWM | diversified_us_equity | -0.75% | -6.36% | 2.04% | 13.13% | -7.44% | -0.466 | 0.822 | 1.183 | -7.33% |
| SMALL_VALUE | IWN | diversified_us_equity | -0.97% | -5.39% | -0.13% | 10.63% | -5.91% | -0.556 | 0.741 | 0.927 | -5.75% |
| DIVIDEND | SCHD | diversified_us_equity | -0.61% | -5.43% | -3.68% | 11.62% | -5.24% | 0.142 | 0.299 | 0.258 | -4.92% |
| LOW_VOL | SPLV | diversified_us_equity | -1.57% | -6.79% | -13.61% | 10.77% | -8.45% | -0.749 | 0.031 | 0.026 | -8.20% |
| MOMENTUM | MTUM | diversified_us_equity | 2.87% | 4.04% | 8.70% | 30.53% | -17.42% | 0.280 | 0.764 | 1.562 | -7.55% |
| TECHNOLOGY | XLK | technology_and_growth | 3.64% | 6.53% | 19.10% | 28.07% | -12.57% | -1.016 | 0.852 | 1.739 | -0.75% |
| COMMUNICATIONS | XLC | technology_and_growth | 2.26% | -0.31% | -15.29% | 21.11% | -7.06% | -0.468 | 0.552 | 0.679 | -5.08% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | -0.21% | -6.37% | -11.19% | 19.67% | -8.08% | -0.706 | 0.775 | 1.166 | -10.66% |
| CONSUMER_STAPLES | XLP | consumer_defensive | -0.24% | -5.19% | -11.99% | 15.95% | -5.96% | -0.588 | -0.048 | -0.053 | -7.07% |
| HEALTHCARE | XLV | healthcare_and_biotech | 1.76% | -2.20% | 0.54% | 17.79% | -5.87% | -0.827 | 0.231 | 0.288 | -2.47% |
| FINANCIALS | XLF | financials | -1.48% | -6.48% | 0.13% | 13.38% | -6.55% | -0.252 | 0.538 | 0.612 | -6.02% |
| INDUSTRIALS | XLI | industrials_and_defense | 0.67% | -6.18% | -6.96% | 14.79% | -9.54% | -0.280 | 0.708 | 0.941 | -8.38% |
| ENERGY | XLE | energy | -2.94% | -0.96% | -16.86% | 21.47% | -5.72% | -0.366 | -0.180 | -0.304 | -5.33% |
| MATERIALS | XLB | materials_and_mining | 0.08% | -7.72% | -9.32% | 17.35% | -7.01% | -0.174 | 0.530 | 0.732 | -6.78% |
| UTILITIES | XLU | rate_sensitive_defensive | -3.16% | -9.46% | -22.46% | 14.54% | -14.34% | 0.366 | 0.128 | 0.151 | -15.50% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | -1.47% | -8.00% | -6.18% | 13.43% | -8.92% | -0.161 | 0.262 | 0.285 | -8.92% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | -0.88% | -4.15% | -18.74% | 5.16% | -4.67% | 0.099 | 0.312 | 0.116 | -6.00% |
| LONG_TREASURY | TLT | rates_and_duration | -2.38% | -5.35% | -20.44% | 9.99% | -8.24% | 0.578 | 0.265 | 0.191 | -10.32% |
| TIPS | TIP | rates_and_duration | -0.69% | -3.70% | -17.76% | 3.78% | -3.46% | -0.164 | 0.283 | 0.076 | -3.44% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | -1.42% | -3.87% | -18.12% | 5.92% | -4.83% | -0.188 | 0.482 | 0.202 | -5.06% |
| HIGH_YIELD_CREDIT | HYG | credit | -0.85% | -2.95% | -15.29% | 3.17% | -2.04% | 0.115 | 0.766 | 0.230 | -2.04% |
| AGGREGATE_BONDS | AGG | rates_and_duration | -0.88% | -3.40% | -18.07% | 4.37% | -3.46% | 0.308 | 0.412 | 0.124 | -3.96% |
| DEVELOPED_EX_US | VEA | international_equity | 0.64% | -2.89% | -0.89% | 15.51% | -4.09% | -0.665 | 0.804 | 1.094 | -2.40% |
| EMERGING_MARKETS | VWO | international_equity | 0.25% | -1.57% | -4.15% | 15.05% | -5.24% | -0.623 | 0.823 | 1.128 | -1.90% |
| EUROPE | VGK | international_equity | 0.48% | -5.09% | -1.84% | 12.43% | -5.32% | -0.531 | 0.751 | 0.919 | -4.65% |
| JAPAN | EWJ | international_equity | 0.96% | 1.68% | -3.06% | 20.56% | -6.21% | -0.613 | 0.727 | 1.193 | -0.86% |
| CHINA | MCHI | international_equity | -0.85% | -5.44% | -18.29% | 16.48% | -8.12% | -0.937 | 0.579 | 0.880 | -19.96% |
| INDIA | INDA | international_equity | -0.33% | -4.74% | -12.32% | 12.41% | -6.08% | -0.580 | 0.573 | 0.678 | -13.44% |
| GOLD | IAU | precious_metals | -1.91% | -7.55% | -13.84% | 23.41% | -8.50% | -0.329 | 0.333 | 0.746 | -20.59% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | -0.81% | 6.32% | -12.24% | 21.06% | -6.42% | -0.316 | -0.193 | -0.307 | -2.99% |
| SEMICONDUCTORS | SMH | technology_and_growth | 5.86% | 8.20% | 26.87% | 42.58% | -23.12% | -0.833 | 0.773 | 2.377 | -9.32% |
| SOFTWARE | IGV | technology_and_growth | 1.59% | 2.60% | 9.35% | 32.97% | -8.27% | -1.109 | 0.493 | 1.209 | -9.44% |
| BROAD_AI_TECH | AIQ | technology_and_growth | 2.87% | 3.66% | 16.84% | 29.02% | -14.68% | -0.868 | 0.850 | 1.924 | -5.94% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | 1.82% | 0.77% | -11.60% | 31.40% | -17.14% | -1.028 | 0.807 | 2.182 | -13.49% |
| CYBERSECURITY | CIBR | technology_and_growth | 1.08% | 6.85% | 29.41% | 33.91% | -9.53% | 0.177 | 0.500 | 1.120 | -2.94% |
| SOLAR | TAN | clean_energy | -3.50% | -10.61% | -30.74% | 36.30% | -26.51% | -0.652 | 0.647 | 1.923 | -40.40% |
| METALS_MINING | XME | materials_and_mining | -0.26% | -10.84% | -4.31% | 36.17% | -12.17% | -0.878 | 0.593 | 1.758 | -18.33% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | -0.18% | -5.53% | -2.37% | 10.10% | -5.26% | -0.889 | 0.779 | 0.702 | -4.88% |
| BIOTECH | XBI | healthcare_and_biotech | -1.08% | -8.87% | 16.98% | 29.21% | -10.51% | -0.141 | 0.488 | 1.062 | -8.56% |
| REGIONAL_BANKS | KRE | financials | -1.09% | -4.45% | -2.71% | 16.38% | -9.17% | -0.160 | 0.419 | 0.710 | -7.66% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | -0.01% | -10.38% | -11.60% | 20.97% | -15.88% | -0.090 | 0.568 | 1.018 | -15.46% |
| CANADA | EWC | international_equity | -1.05% | -5.18% | -2.65% | 11.60% | -5.11% | -0.103 | 0.675 | 0.757 | -4.87% |
| UNITED_KINGDOM | EWU | international_equity | 0.11% | -4.09% | -6.97% | 11.94% | -4.66% | -0.345 | 0.609 | 0.707 | -4.19% |
| AUSTRALIA | EWA | international_equity | -1.11% | -6.64% | -6.52% | 16.50% | -6.97% | 0.156 | 0.682 | 0.953 | -6.57% |
| SOUTH_KOREA | EWY | international_equity | 3.24% | 3.53% | 30.27% | 61.52% | -28.57% | -0.926 | 0.639 | 2.810 | -14.61% |
| TAIWAN | EWT | international_equity | 2.81% | 6.95% | 32.71% | 35.16% | -17.68% | -0.850 | 0.757 | 1.860 | -0.74% |
| BRAZIL | EWZ | international_equity | -1.87% | 2.14% | -21.07% | 22.10% | -8.05% | 0.027 | 0.488 | 0.954 | -10.92% |
| MEXICO | EWW | international_equity | 0.00% | -6.37% | -11.70% | 16.36% | -6.86% | -0.655 | 0.556 | 0.948 | -8.39% |
| SOUTH_AFRICA | EZA | international_equity | -2.93% | -8.19% | -4.65% | 26.66% | -9.12% | -0.169 | 0.630 | 1.620 | -16.80% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | -1.04% | -4.05% | -17.76% | 5.45% | -4.34% | 3.316 | 0.408 | 0.147 | -4.43% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | -1.66% | -4.73% | -17.86% | 3.82% | -5.43% | 5.864 | 0.386 | 0.095 | -5.43% |
| EMERGING_MARKET_BONDS | EMB | credit | -1.29% | -3.80% | -14.82% | 5.50% | -3.56% | 0.053 | 0.694 | 0.312 | -3.56% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | -0.23% | -2.45% | -17.79% | 3.89% | -2.69% | -0.013 | 0.480 | 0.138 | -3.02% |
| SILVER | SLV | precious_metals | -2.99% | -6.54% | -17.71% | 37.58% | -10.19% | -0.595 | 0.367 | 1.774 | -44.94% |
| COPPER | CPER | non_energy_commodities | 0.94% | 0.44% | 1.13% | 22.92% | -6.80% | -0.158 | 0.565 | 1.258 | -1.98% |
| AGRICULTURE | DBA | non_energy_commodities | 1.39% | -1.11% | -13.60% | 13.92% | -4.54% | 0.291 | 0.051 | 0.043 | -3.22% |
| OIL | USO | energy | -3.57% | 15.54% | -10.45% | 51.50% | -17.64% | -0.495 | -0.351 | -1.339 | -8.36% |
| US_DOLLAR | UUP | currencies | 0.81% | 1.20% | -18.30% | 5.16% | -2.52% | -0.596 | -0.301 | -0.129 | -0.24% |
| EURO | FXE | currencies | -0.79% | -3.14% | -17.51% | 4.49% | -2.53% | -0.497 | 0.286 | 0.119 | -4.85% |
| YEN | FXY | currencies | -0.31% | 0.37% | -18.85% | 10.20% | -3.38% | 0.368 | 0.184 | 0.121 | -6.75% |
| BITCOIN_ETF | IBIT | crypto_assets | 3.37% | 6.06% | -4.53% | 38.96% | -7.14% | 0.241 | 0.500 | 1.775 | -33.27% |
| ETHEREUM_ETF | ETHA | crypto_assets | 1.96% | 7.96% | 1.58% | 49.12% | -5.32% | 0.764 | 0.522 | 2.609 | -43.25% |
