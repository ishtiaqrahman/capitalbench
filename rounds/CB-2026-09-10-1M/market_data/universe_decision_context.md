# Full-Universe Horizon-Specific Decision Context

Profile: monthly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: tiingo_eod_adjusted_price_and_volume
- As-of date requested: 2026-09-09
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | 0.08% |
| spy_return_21s | -1.38% |
| rsp_return_5s | -1.36% |
| rsp_return_21s | -2.53% |
| hyg_return_5s | -0.15% |
| hyg_return_21s | -0.08% |
| tlt_return_5s | -0.17% |
| tlt_return_21s | -0.02% |
| uup_return_5s | -0.82% |
| uup_return_21s | -0.57% |
| uso_return_5s | 6.36% |
| uso_return_21s | 19.10% |
| iau_return_5s | 1.65% |
| iau_return_21s | 0.22% |
| rsp_minus_spy_5s | -1.44% |
| rsp_minus_spy_21s | -1.16% |
| positive_asset_share_5s | 53.62% |
| positive_asset_share_21s | 36.23% |
| active_return_dispersion_5s |  |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_5s | active_return_21s | prior_105s_active_return | volatility_63s | max_drawdown_63s | volume_zscore_20v120 | corr_spy_252s | beta_spy_252s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | 1.38% | -14.76% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.08% | 1.66% | -13.26% | 0.20% | -0.01% | -0.584 | -0.099 | -0.001 | 0.00% |
| SP500 | SPY | diversified_us_equity | 0.08% | 0.00% | 0.00% | 12.91% | -3.38% | -1.087 | 1.000 | 1.000 | -1.99% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | 0.10% | -0.22% | 0.36% | 12.76% | -3.29% | -0.695 | 0.995 | 1.012 | -2.27% |
| NASDAQ100 | QQQ | technology_and_growth | 1.23% | 0.74% | 4.13% | 23.63% | -10.96% | -1.075 | 0.928 | 1.419 | -3.89% |
| LARGE_GROWTH | IWF | technology_and_growth | 1.03% | -0.00% | -4.53% | 20.33% | -8.29% | -0.756 | 0.934 | 1.287 | -4.82% |
| LARGE_VALUE | IWD | diversified_us_equity | -0.74% | -0.27% | 4.51% | 10.83% | -2.05% | -0.567 | 0.800 | 0.702 | -2.05% |
| MID_CAP | IJH | diversified_us_equity | -0.05% | -2.47% | -1.14% | 13.49% | -5.22% | -0.714 | 0.808 | 0.977 | -5.22% |
| SMALL_CAP | IWM | diversified_us_equity | 0.02% | -1.74% | 4.13% | 15.00% | -4.76% | -1.091 | 0.819 | 1.203 | -4.74% |
| SMALL_VALUE | IWN | diversified_us_equity | 0.25% | -0.32% | 3.38% | 12.01% | -3.29% | -0.953 | 0.736 | 0.942 | -3.06% |
| DIVIDEND | SCHD | diversified_us_equity | -2.07% | 1.08% | -2.30% | 12.03% | -3.18% | 0.177 | 0.289 | 0.251 | -3.18% |
| LOW_VOL | SPLV | diversified_us_equity | -0.70% | -0.66% | -13.17% | 11.73% | -4.89% | -0.789 | 0.021 | 0.017 | -4.89% |
| MOMENTUM | MTUM | diversified_us_equity | 4.31% | 2.02% | 9.26% | 35.57% | -17.99% | -0.413 | 0.760 | 1.556 | -10.41% |
| TECHNOLOGY | XLK | technology_and_growth | 2.30% | 2.21% | 18.87% | 31.58% | -13.31% | -1.342 | 0.849 | 1.740 | -5.10% |
| COMMUNICATIONS | XLC | technology_and_growth | -0.05% | 0.48% | -18.94% | 19.82% | -7.06% | -0.995 | 0.569 | 0.677 | -7.16% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | -1.86% | -4.65% | -9.77% | 21.65% | -8.09% | -1.122 | 0.766 | 1.164 | -9.32% |
| CONSUMER_STAPLES | XLP | consumer_defensive | -2.58% | -0.86% | -14.41% | 17.06% | -5.03% | -0.814 | -0.059 | -0.066 | -6.57% |
| HEALTHCARE | XLV | healthcare_and_biotech | -2.96% | 0.27% | -3.84% | 19.41% | -5.18% | -0.973 | 0.228 | 0.290 | -5.18% |
| FINANCIALS | XLF | financials | -0.24% | 0.08% | 1.71% | 13.03% | -2.56% | -0.798 | 0.540 | 0.616 | -2.56% |
| INDUSTRIALS | XLI | industrials_and_defense | -0.54% | -5.56% | -5.62% | 18.77% | -7.89% | -0.761 | 0.711 | 0.954 | -7.89% |
| ENERGY | XLE | energy | 0.83% | 9.90% | -5.05% | 22.06% | -8.69% | -0.849 | -0.185 | -0.312 | 0.00% |
| MATERIALS | XLB | materials_and_mining | -1.31% | -1.99% | -7.28% | 19.16% | -4.75% | -0.460 | 0.531 | 0.744 | -4.25% |
| UTILITIES | XLU | rate_sensitive_defensive | 0.89% | 0.93% | -20.89% | 14.32% | -8.77% | -0.390 | 0.117 | 0.139 | -8.84% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | -1.43% | -0.85% | -9.72% | 14.54% | -5.65% | -0.431 | 0.246 | 0.270 | -5.65% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | -0.22% | 0.80% | -16.96% | 4.74% | -2.33% | -0.393 | 0.286 | 0.102 | -4.02% |
| LONG_TREASURY | TLT | rates_and_duration | -0.17% | 1.36% | -20.00% | 9.59% | -6.25% | -0.144 | 0.236 | 0.168 | -7.59% |
| TIPS | TIP | rates_and_duration | -0.01% | 1.32% | -15.41% | 3.48% | -1.33% | -0.453 | 0.259 | 0.066 | -1.35% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | 0.09% | 1.18% | -16.58% | 5.24% | -2.92% | -0.557 | 0.475 | 0.193 | -3.13% |
| HIGH_YIELD_CREDIT | HYG | credit | -0.15% | 1.29% | -12.99% | 2.90% | -0.80% | -0.635 | 0.776 | 0.229 | -0.63% |
| AGGREGATE_BONDS | AGG | rates_and_duration | -0.09% | 1.15% | -15.97% | 3.94% | -1.71% | -0.440 | 0.395 | 0.114 | -2.39% |
| DEVELOPED_EX_US | VEA | international_equity | 0.98% | 1.82% | -4.10% | 17.46% | -4.75% | -0.736 | 0.801 | 1.084 | -1.31% |
| EMERGING_MARKETS | VWO | international_equity | 0.31% | 2.27% | -5.95% | 16.92% | -7.05% | -0.801 | 0.814 | 1.113 | -0.93% |
| EUROPE | VGK | international_equity | -0.56% | -0.85% | -3.79% | 13.63% | -3.20% | -0.894 | 0.747 | 0.915 | -3.20% |
| JAPAN | EWJ | international_equity | 1.87% | 2.36% | -3.08% | 22.68% | -7.86% | -0.829 | 0.724 | 1.183 | -1.49% |
| CHINA | MCHI | international_equity | -1.97% | -4.93% | -17.14% | 16.84% | -8.10% | -0.804 | 0.562 | 0.872 | -18.87% |
| INDIA | INDA | international_equity | -1.84% | -1.56% | -14.34% | 12.95% | -4.59% | -0.980 | 0.557 | 0.660 | -11.97% |
| GOLD | IAU | precious_metals | 1.65% | 1.59% | -30.44% | 26.70% | -8.22% | -0.419 | 0.329 | 0.743 | -18.59% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | 2.89% | 11.30% | -6.31% | 21.68% | -9.47% | -0.513 | -0.179 | -0.284 | 0.00% |
| SEMICONDUCTORS | SMH | technology_and_growth | 5.33% | 2.23% | 28.55% | 49.10% | -24.62% | -0.801 | 0.772 | 2.367 | -14.15% |
| SOFTWARE | IGV | technology_and_growth | -4.10% | -1.65% | 7.86% | 33.24% | -8.79% | -0.982 | 0.509 | 1.249 | -13.53% |
| BROAD_AI_TECH | AIQ | technology_and_growth | 1.67% | 2.32% | 13.10% | 33.98% | -16.56% | -0.838 | 0.848 | 1.923 | -8.60% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | 1.56% | -3.21% | -8.95% | 34.59% | -18.66% | -1.305 | 0.804 | 2.204 | -15.15% |
| CYBERSECURITY | CIBR | technology_and_growth | -1.79% | -4.71% | 38.57% | 31.53% | -9.53% | -0.024 | 0.526 | 1.158 | -7.55% |
| SOLAR | TAN | clean_energy | 1.88% | -6.57% | -20.30% | 38.86% | -25.65% | -0.728 | 0.634 | 1.890 | -35.43% |
| METALS_MINING | XME | materials_and_mining | 2.95% | 2.78% | -11.63% | 37.46% | -19.05% | -0.488 | 0.598 | 1.779 | -10.21% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | -1.36% | -1.16% | -2.19% | 11.16% | -3.65% | -1.105 | 0.772 | 0.704 | -3.65% |
| BIOTECH | XBI | healthcare_and_biotech | -2.46% | 2.23% | 9.37% | 29.65% | -10.51% | -0.413 | 0.483 | 1.053 | -6.00% |
| REGIONAL_BANKS | KRE | financials | 1.14% | -2.02% | 4.07% | 17.43% | -6.81% | -0.668 | 0.416 | 0.721 | -5.75% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | -2.67% | -11.24% | -9.86% | 24.26% | -13.33% | -0.413 | 0.571 | 1.038 | -13.33% |
| CANADA | EWC | international_equity | 0.64% | 0.55% | -5.79% | 11.48% | -3.26% | -0.249 | 0.677 | 0.764 | -2.63% |
| UNITED_KINGDOM | EWU | international_equity | -0.75% | 0.01% | -8.77% | 12.67% | -3.16% | -0.700 | 0.602 | 0.701 | -3.16% |
| AUSTRALIA | EWA | international_equity | -0.20% | -0.06% | -9.49% | 15.66% | -4.42% | -0.432 | 0.674 | 0.934 | -2.66% |
| SOUTH_KOREA | EWY | international_equity | 8.52% | 18.33% | 10.43% | 70.71% | -34.21% | -0.775 | 0.631 | 2.755 | -12.97% |
| TAIWAN | EWT | international_equity | 1.84% | 10.75% | 30.30% | 38.44% | -19.83% | -1.103 | 0.751 | 1.827 | -0.37% |
| BRAZIL | EWZ | international_equity | 4.10% | 9.56% | -20.10% | 22.30% | -8.05% | -0.164 | 0.486 | 0.955 | -7.90% |
| MEXICO | EWW | international_equity | 1.11% | 0.82% | -10.35% | 17.97% | -5.37% | -0.585 | 0.550 | 0.941 | -4.44% |
| SOUTH_AFRICA | EZA | international_equity | 2.55% | 3.64% | -17.27% | 28.89% | -11.18% | -0.592 | 0.632 | 1.623 | -10.76% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | -0.21% | 0.99% | -15.88% | 4.64% | -1.85% | 0.102 | 0.392 | 0.133 | -2.44% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | -0.81% | -0.59% | -14.94% | 3.13% | -3.27% | 1.380 | 0.387 | 0.089 | -3.27% |
| EMERGING_MARKET_BONDS | EMB | credit | 0.09% | 1.11% | -13.73% | 5.13% | -1.96% | -0.546 | 0.688 | 0.303 | -1.47% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | -0.08% | 0.46% | -14.99% | 3.65% | -1.94% | -0.352 | 0.466 | 0.131 | -2.42% |
| SILVER | SLV | precious_metals | 4.83% | 3.58% | -40.58% | 41.86% | -20.61% | -0.654 | 0.364 | 1.770 | -42.50% |
| COPPER | CPER | non_energy_commodities | 5.07% | 3.54% | -3.40% | 23.06% | -8.42% | -0.398 | 0.557 | 1.235 | 0.00% |
| AGRICULTURE | DBA | non_energy_commodities | -1.66% | 5.62% | -10.22% | 13.02% | -2.87% | 0.204 | 0.062 | 0.053 | -1.66% |
| OIL | USO | energy | 6.36% | 20.47% | 4.19% | 52.10% | -23.10% | -0.632 | -0.343 | -1.297 | -1.95% |
| US_DOLLAR | UUP | currencies | -0.82% | 0.81% | -12.25% | 5.26% | -2.52% | -1.112 | -0.295 | -0.129 | -2.17% |
| EURO | FXE | currencies | 0.37% | 2.22% | -15.06% | 4.74% | -2.19% | -0.692 | 0.275 | 0.118 | -2.88% |
| YEN | FXY | currencies | 4.37% | 4.98% | -15.67% | 9.57% | -2.49% | 0.311 | 0.173 | 0.114 | -4.97% |
| BITCOIN_ETF | IBIT | crypto_assets | 1.21% | 23.62% | -23.53% | 37.94% | -11.79% | 0.726 | 0.489 | 1.724 | -37.87% |
| ETHEREUM_ETF | ETHA | crypto_assets | 1.92% | 32.78% | -22.94% | 51.49% | -14.68% | 1.169 | 0.504 | 2.547 | -48.09% |
