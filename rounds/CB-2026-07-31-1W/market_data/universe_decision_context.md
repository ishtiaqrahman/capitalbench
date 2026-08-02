# Full-Universe Horizon-Specific Decision Context

Profile: weekly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: yahoo_chart_adjusted_close_and_reported_volume
- As-of date requested: 2026-07-31
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | 1.10% |
| spy_return_21s | 0.17% |
| rsp_return_5s | 0.67% |
| rsp_return_21s | 0.75% |
| hyg_return_5s | 0.32% |
| hyg_return_21s | -0.14% |
| tlt_return_5s | -1.20% |
| tlt_return_21s | -3.82% |
| uup_return_5s | -1.43% |
| uup_return_21s | -1.12% |
| uso_return_5s | -5.50% |
| uso_return_21s | 25.08% |
| iau_return_5s | -0.08% |
| iau_return_21s | 0.28% |
| rsp_minus_spy_5s | -0.42% |
| rsp_minus_spy_21s | 0.58% |
| positive_asset_share_5s | 56.52% |
| positive_asset_share_21s | 46.38% |
| active_return_dispersion_5s | 2.29% |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_3s | active_return_5s | prior_16s_active_return | volatility_21s | max_drawdown_21s | volume_zscore_5v60 | corr_spy_63s | beta_spy_63s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | -1.10% | 0.92% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.05% | -1.02% | 1.15% | 0.23% | -0.01% | 0.005 | -0.159 | -0.002 | 0.00% |
| SP500 | SPY | diversified_us_equity | 0.83% | 0.00% | 0.00% | 12.38% | -3.38% | 0.389 | 1.000 | 1.000 | -1.40% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | 0.61% | -0.16% | -0.29% | 11.98% | -3.29% | -0.280 | 0.993 | 0.982 | -1.36% |
| NASDAQ100 | QQQ | technology_and_growth | 1.85% | -0.55% | -4.73% | 23.86% | -8.79% | 0.797 | 0.917 | 1.715 | -7.69% |
| LARGE_GROWTH | IWF | technology_and_growth | 1.58% | -0.53% | -3.45% | 22.52% | -7.99% | -0.685 | 0.896 | 1.319 | -8.03% |
| LARGE_VALUE | IWD | diversified_us_equity | -0.09% | 0.35% | 2.70% | 9.90% | -1.31% | -0.230 | 0.715 | 0.615 | -0.09% |
| MID_CAP | IJH | diversified_us_equity | -1.00% | -1.76% | 0.04% | 11.96% | -2.24% | -0.459 | 0.789 | 0.836 | -2.39% |
| SMALL_CAP | IWM | diversified_us_equity | -0.74% | -1.09% | -1.81% | 13.25% | -3.59% | -0.191 | 0.776 | 1.037 | -3.08% |
| SMALL_VALUE | IWN | diversified_us_equity | -1.28% | -1.18% | 0.79% | 11.13% | -1.83% | 0.334 | 0.660 | 0.724 | -1.31% |
| DIVIDEND | SCHD | diversified_us_equity | -1.24% | -0.56% | 5.44% | 14.29% | -1.42% | 2.527 | 0.058 | 0.050 | -1.24% |
| LOW_VOL | SPLV | diversified_us_equity | -2.23% | -2.34% | 3.70% | 15.29% | -2.23% | -0.161 | -0.308 | -0.302 | -2.23% |
| MOMENTUM | MTUM | diversified_us_equity | 2.49% | -3.32% | -5.70% | 38.99% | -13.71% | 0.879 | 0.744 | 2.126 | -13.22% |
| TECHNOLOGY | XLK | technology_and_growth | 2.49% | -1.40% | -4.33% | 33.44% | -10.34% | -0.170 | 0.839 | 2.161 | -11.43% |
| COMMUNICATIONS | XLC | technology_and_growth | -1.30% | 0.73% | -2.22% | 22.48% | -7.06% | 0.217 | 0.364 | 0.483 | -9.34% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | 3.21% | 5.01% | -6.43% | 25.04% | -7.90% | 0.045 | 0.702 | 1.122 | -6.40% |
| CONSUMER_STAPLES | XLP | consumer_defensive | -2.31% | -0.00% | 1.91% | 21.12% | -3.03% | 1.221 | -0.338 | -0.427 | -4.32% |
| HEALTHCARE | XLV | healthcare_and_biotech | -2.82% | -1.11% | 2.82% | 20.97% | -3.74% | 0.149 | -0.167 | -0.225 | -2.82% |
| FINANCIALS | XLF | financials | -1.15% | 0.02% | 3.71% | 14.08% | -2.08% | 0.025 | 0.246 | 0.247 | -1.15% |
| INDUSTRIALS | XLI | industrials_and_defense | -1.45% | -2.64% | 0.53% | 16.63% | -4.80% | -0.273 | 0.654 | 0.929 | -3.08% |
| ENERGY | XLE | energy | 3.44% | -1.21% | 13.81% | 20.34% | -3.44% | -0.721 | -0.375 | -0.667 | -4.12% |
| MATERIALS | XLB | materials_and_mining | -3.65% | -2.72% | 1.39% | 20.32% | -3.81% | 0.361 | 0.473 | 0.712 | -5.18% |
| UTILITIES | XLU | rate_sensitive_defensive | -2.57% | -5.29% | 4.31% | 15.97% | -4.19% | 0.010 | -0.098 | -0.119 | -5.83% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | -2.04% | -3.01% | 4.92% | 15.66% | -2.04% | 0.426 | -0.142 | -0.167 | -2.04% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | -0.65% | -1.18% | -0.15% | 4.10% | -1.41% | -0.640 | 0.509 | 0.187 | -3.60% |
| LONG_TREASURY | TLT | rates_and_duration | -2.36% | -2.30% | -1.74% | 8.48% | -3.82% | 1.580 | 0.419 | 0.290 | -7.74% |
| TIPS | TIP | rates_and_duration | -0.03% | -0.98% | 0.30% | 2.54% | -1.01% | 0.451 | 0.487 | 0.125 | -1.31% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | -0.54% | -1.08% | -1.14% | 4.75% | -2.25% | 0.930 | 0.584 | 0.228 | -3.10% |
| HIGH_YIELD_CREDIT | HYG | credit | 0.08% | -0.78% | 0.46% | 2.77% | -0.80% | 0.283 | 0.776 | 0.205 | -0.49% |
| AGGREGATE_BONDS | AGG | rates_and_duration | -0.56% | -1.19% | -0.14% | 3.58% | -1.34% | 0.238 | 0.554 | 0.168 | -2.37% |
| DEVELOPED_EX_US | VEA | international_equity | 1.47% | 0.21% | -0.01% | 18.81% | -4.09% | -0.211 | 0.828 | 1.272 | -2.45% |
| EMERGING_MARKETS | VWO | international_equity | 1.75% | 0.55% | -1.48% | 19.33% | -5.24% | -0.505 | 0.867 | 1.314 | -4.07% |
| EUROPE | VGK | international_equity | 1.52% | 1.37% | 1.65% | 15.43% | -2.53% | -0.332 | 0.727 | 0.951 | -0.44% |
| JAPAN | EWJ | international_equity | 2.85% | 0.20% | -1.06% | 26.67% | -6.21% | -0.337 | 0.765 | 1.318 | -4.72% |
| CHINA | MCHI | international_equity | 2.55% | 3.54% | 4.41% | 19.35% | -2.22% | -0.070 | 0.440 | 0.674 | -15.13% |
| INDIA | INDA | international_equity | 0.85% | 2.61% | -1.50% | 14.23% | -4.51% | 0.649 | 0.565 | 0.659 | -9.93% |
| GOLD | IAU | precious_metals | 0.62% | -1.17% | 1.27% | 21.96% | -4.47% | -0.693 | 0.628 | 1.103 | -25.01% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | 2.93% | -3.27% | 14.67% | 24.23% | -5.54% | -0.191 | -0.178 | -0.291 | -7.14% |
| SEMICONDUCTORS | SMH | technology_and_growth | 2.06% | -4.78% | -8.64% | 51.01% | -18.73% | 2.432 | 0.789 | 3.189 | -19.19% |
| SOFTWARE | IGV | technology_and_growth | 3.05% | 6.41% | -4.83% | 23.55% | -8.11% | 0.057 | 0.325 | 0.797 | -19.69% |
| BROAD_AI_TECH | AIQ | technology_and_growth | 2.88% | 0.47% | -7.96% | 36.20% | -12.31% | 0.187 | 0.818 | 2.412 | -16.04% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | 1.30% | -0.17% | -11.68% | 33.76% | -16.01% | -0.054 | 0.861 | 2.422 | -19.99% |
| CYBERSECURITY | CIBR | technology_and_growth | 2.86% | 2.78% | -2.06% | 25.41% | -7.40% | -0.750 | 0.450 | 1.067 | -3.06% |
| SOLAR | TAN | clean_energy | 0.47% | -4.90% | -10.36% | 41.36% | -17.51% | 1.090 | 0.730 | 2.457 | -33.27% |
| METALS_MINING | XME | materials_and_mining | -0.78% | -2.17% | -1.59% | 35.79% | -8.01% | -0.132 | 0.689 | 2.038 | -24.17% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | -1.23% | -0.42% | 0.99% | 9.98% | -1.46% | 0.406 | 0.675 | 0.537 | -1.23% |
| BIOTECH | XBI | healthcare_and_biotech | -1.85% | -3.40% | -2.96% | 28.55% | -10.51% | -0.255 | 0.346 | 0.783 | -10.51% |
| REGIONAL_BANKS | KRE | financials | -0.95% | -0.66% | 0.33% | 19.32% | -3.73% | -0.650 | 0.190 | 0.276 | -2.39% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | -2.17% | -1.30% | -0.61% | 25.13% | -8.58% | -0.066 | 0.478 | 0.893 | -4.43% |
| CANADA | EWC | international_equity | -0.75% | -0.55% | 3.34% | 10.35% | -1.46% | -0.514 | 0.610 | 0.537 | -0.75% |
| UNITED_KINGDOM | EWU | international_equity | 1.23% | 1.40% | 3.72% | 15.42% | -1.93% | -0.365 | 0.470 | 0.564 | -0.55% |
| AUSTRALIA | EWA | international_equity | 0.07% | 1.06% | 4.60% | 15.93% | -1.61% | -0.193 | 0.609 | 0.816 | -1.68% |
| SOUTH_KOREA | EWY | international_equity | 3.73% | -4.69% | -11.24% | 77.14% | -24.04% | 1.999 | 0.707 | 4.282 | -28.33% |
| TAIWAN | EWT | international_equity | 2.77% | -2.59% | -6.35% | 46.31% | -16.65% | 0.232 | 0.792 | 2.570 | -13.43% |
| BRAZIL | EWZ | international_equity | 1.66% | 1.48% | 5.45% | 23.31% | -3.14% | -0.595 | 0.471 | 0.815 | -11.34% |
| MEXICO | EWW | international_equity | 0.04% | 0.71% | 1.15% | 18.15% | -2.98% | -0.337 | 0.648 | 0.978 | -4.05% |
| SOUTH_AFRICA | EZA | international_equity | 2.65% | 3.08% | -1.73% | 25.68% | -6.50% | -0.680 | 0.750 | 1.789 | -20.33% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | -0.80% | -1.30% | -0.05% | 4.47% | -1.48% | 0.751 | 0.552 | 0.199 | -2.42% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | -0.34% | -1.01% | -0.75% | 3.34% | -2.15% | 0.852 | 0.551 | 0.124 | -1.79% |
| EMERGING_MARKET_BONDS | EMB | credit | -0.56% | -1.08% | -0.52% | 4.85% | -1.89% | -0.049 | 0.741 | 0.317 | -1.82% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | -0.46% | -1.16% | -0.06% | 3.74% | -1.16% | -0.638 | 0.533 | 0.163 | -1.80% |
| SILVER | SLV | precious_metals | 1.28% | -1.53% | -0.93% | 38.85% | -10.19% | -0.722 | 0.611 | 2.255 | -50.42% |
| COPPER | CPER | non_energy_commodities | 3.21% | 2.06% | 3.98% | 21.85% | -3.26% | -0.563 | 0.699 | 1.501 | -2.56% |
| AGRICULTURE | DBA | non_energy_commodities | -1.19% | -3.68% | 6.05% | 16.40% | -2.69% | -0.536 | 0.097 | 0.100 | -4.25% |
| OIL | USO | energy | 7.20% | -6.60% | 33.28% | 61.57% | -13.62% | -0.230 | -0.337 | -1.319 | -15.55% |
| US_DOLLAR | UUP | currencies | -1.43% | -2.53% | 1.23% | 5.72% | -1.61% | 0.506 | -0.465 | -0.172 | -1.50% |
| EURO | FXE | currencies | 1.31% | 0.37% | 0.92% | 4.62% | -0.81% | -0.479 | 0.500 | 0.178 | -3.79% |
| YEN | FXY | currencies | 2.96% | 1.79% | 0.22% | 10.49% | -1.67% | 3.226 | 0.249 | 0.124 | -8.21% |
| BITCOIN_ETF | IBIT | crypto_assets | -1.38% | -3.05% | 7.83% | 31.98% | -5.39% | -0.388 | 0.437 | 1.199 | -50.01% |
| ETHEREUM_ETF | ETHA | crypto_assets | -2.90% | -0.88% | 16.09% | 47.27% | -4.35% | 0.407 | 0.546 | 2.129 | -61.55% |
