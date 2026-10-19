# Full-Universe Horizon-Specific Decision Context

Profile: monthly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: yahoo_chart_adjusted_close_and_reported_volume
- As-of date requested: 2026-10-16
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | -1.97% |
| spy_return_21s | 0.33% |
| rsp_return_5s | 0.49% |
| rsp_return_21s | 0.74% |
| hyg_return_5s | -0.48% |
| hyg_return_21s | -1.93% |
| tlt_return_5s | 2.65% |
| tlt_return_21s | -1.72% |
| uup_return_5s | -0.34% |
| uup_return_21s | 1.90% |
| uso_return_5s | 9.15% |
| uso_return_21s | 4.15% |
| iau_return_5s | -0.67% |
| iau_return_21s | -4.10% |
| rsp_minus_spy_5s | 2.46% |
| rsp_minus_spy_21s | 0.41% |
| positive_asset_share_5s | 49.28% |
| positive_asset_share_21s | 30.43% |
| active_return_dispersion_5s |  |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_5s | active_return_21s | prior_105s_active_return | volatility_63s | max_drawdown_63s | volume_zscore_20v120 | corr_spy_252s | beta_spy_252s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | -0.33% | -7.66% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.07% | -0.00% | -6.19% | 0.20% | -0.01% | 0.396 | -0.041 | -0.001 | 0.00% |
| SP500 | SPY | diversified_us_equity | -1.97% | 0.00% | 0.00% | 11.10% | -3.06% | -0.544 | 1.000 | 1.000 | -2.03% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | -2.06% | -0.42% | -0.28% | 11.29% | -3.39% | -0.310 | 0.995 | 1.012 | -2.42% |
| NASDAQ100 | QQQ | technology_and_growth | -5.52% | -1.22% | 2.95% | 18.79% | -6.66% | -0.399 | 0.926 | 1.440 | -6.56% |
| LARGE_GROWTH | IWF | technology_and_growth | -5.03% | -1.19% | -4.60% | 17.84% | -6.00% | -0.205 | 0.932 | 1.305 | -5.97% |
| LARGE_VALUE | IWD | diversified_us_equity | 0.88% | 0.83% | 4.40% | 8.61% | -4.07% | -0.210 | 0.795 | 0.691 | -1.03% |
| MID_CAP | IJH | diversified_us_equity | -1.47% | -1.51% | -6.68% | 12.26% | -8.26% | 0.270 | 0.807 | 0.958 | -7.75% |
| SMALL_CAP | IWM | diversified_us_equity | -3.05% | -5.59% | -3.65% | 14.15% | -11.13% | 0.131 | 0.817 | 1.178 | -11.13% |
| SMALL_VALUE | IWN | diversified_us_equity | -1.01% | -4.02% | -1.88% | 11.15% | -8.30% | 0.535 | 0.731 | 0.908 | -7.84% |
| DIVIDEND | SCHD | diversified_us_equity | 3.96% | 1.83% | 2.35% | 10.86% | -6.87% | 0.376 | 0.254 | 0.223 | -1.66% |
| LOW_VOL | SPLV | diversified_us_equity | 3.24% | 1.81% | -8.92% | 9.18% | -9.22% | -0.556 | 0.029 | 0.024 | -4.11% |
| MOMENTUM | MTUM | diversified_us_equity | -8.38% | -4.56% | 4.22% | 26.45% | -9.98% | 0.545 | 0.767 | 1.614 | -14.91% |
| TECHNOLOGY | XLK | technology_and_growth | -7.70% | -2.66% | 14.32% | 25.92% | -9.17% | -0.527 | 0.848 | 1.759 | -9.17% |
| COMMUNICATIONS | XLC | technology_and_growth | -0.05% | -1.82% | -13.09% | 20.86% | -4.89% | 0.504 | 0.544 | 0.692 | -7.29% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | -0.35% | 0.85% | -14.97% | 18.89% | -9.02% | -0.240 | 0.768 | 1.159 | -9.12% |
| CONSUMER_STAPLES | XLP | consumer_defensive | 5.02% | 5.30% | -5.71% | 15.11% | -7.54% | 0.177 | -0.059 | -0.069 | -0.78% |
| HEALTHCARE | XLV | healthcare_and_biotech | 3.45% | 4.75% | 6.28% | 17.08% | -5.87% | -0.380 | 0.199 | 0.252 | -0.27% |
| FINANCIALS | XLF | financials | 1.44% | -0.63% | -0.71% | 12.33% | -8.49% | 0.517 | 0.526 | 0.606 | -4.86% |
| INDUSTRIALS | XLI | industrials_and_defense | -0.88% | -0.81% | -10.02% | 14.93% | -10.23% | -0.137 | 0.699 | 0.945 | -9.81% |
| ENERGY | XLE | energy | 4.86% | 6.13% | 10.38% | 21.57% | -6.16% | -0.225 | -0.231 | -0.400 | 0.00% |
| MATERIALS | XLB | materials_and_mining | 3.01% | 0.54% | -9.55% | 16.36% | -9.14% | 0.103 | 0.512 | 0.715 | -4.69% |
| UTILITIES | XLU | rate_sensitive_defensive | 1.93% | 1.66% | -16.77% | 15.05% | -14.59% | 2.879 | 0.114 | 0.138 | -9.72% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | 1.32% | -1.32% | -10.28% | 12.74% | -11.08% | 1.140 | 0.255 | 0.285 | -7.60% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | 1.14% | -0.90% | -10.92% | 5.32% | -4.24% | 0.804 | 0.342 | 0.130 | -5.24% |
| LONG_TREASURY | TLT | rates_and_duration | 2.65% | -2.05% | -11.92% | 10.40% | -7.37% | 1.989 | 0.309 | 0.227 | -9.13% |
| TIPS | TIP | rates_and_duration | 1.07% | -0.49% | -9.60% | 3.94% | -3.40% | 0.140 | 0.287 | 0.080 | -2.51% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | 0.97% | -1.58% | -10.20% | 6.02% | -3.98% | 0.820 | 0.497 | 0.215 | -4.48% |
| HIGH_YIELD_CREDIT | HYG | credit | -0.48% | -2.26% | -7.56% | 3.51% | -2.93% | 2.515 | 0.759 | 0.230 | -2.87% |
| AGGREGATE_BONDS | AGG | rates_and_duration | 0.84% | -0.97% | -9.54% | 4.51% | -3.28% | 1.405 | 0.433 | 0.135 | -3.36% |
| DEVELOPED_EX_US | VEA | international_equity | -1.22% | -3.78% | -3.50% | 14.56% | -5.85% | -0.300 | 0.802 | 1.108 | -5.59% |
| EMERGING_MARKETS | VWO | international_equity | -2.89% | -3.29% | -6.31% | 14.28% | -5.37% | -0.091 | 0.815 | 1.114 | -5.37% |
| EUROPE | VGK | international_equity | 1.46% | -2.42% | -5.96% | 12.25% | -8.10% | 0.244 | 0.743 | 0.930 | -6.10% |
| JAPAN | EWJ | international_equity | -3.05% | -3.43% | 1.49% | 19.16% | -4.47% | -0.434 | 0.726 | 1.186 | -4.47% |
| CHINA | MCHI | international_equity | -2.57% | -3.12% | -18.24% | 15.19% | -10.06% | -0.556 | 0.546 | 0.803 | -20.46% |
| INDIA | INDA | international_equity | 3.54% | -1.06% | -14.04% | 13.78% | -9.84% | -0.304 | 0.588 | 0.725 | -13.80% |
| GOLD | IAU | precious_metals | -0.67% | -4.43% | -18.23% | 23.99% | -12.19% | -0.527 | 0.344 | 0.790 | -22.87% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | 2.29% | 1.70% | 9.38% | 20.38% | -6.42% | -0.275 | -0.230 | -0.373 | 0.00% |
| SEMICONDUCTORS | SMH | technology_and_growth | -10.53% | -4.05% | 13.12% | 37.69% | -14.85% | -0.456 | 0.764 | 2.374 | -19.30% |
| SOFTWARE | IGV | technology_and_growth | -7.39% | -1.70% | 16.69% | 34.87% | -8.27% | -1.129 | 0.492 | 1.250 | -10.86% |
| BROAD_AI_TECH | AIQ | technology_and_growth | -6.88% | -3.98% | 11.32% | 26.00% | -8.23% | -0.561 | 0.848 | 1.942 | -11.58% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | -9.12% | -8.72% | -13.29% | 29.66% | -13.97% | -0.643 | 0.811 | 2.209 | -21.96% |
| CYBERSECURITY | CIBR | technology_and_growth | -10.16% | -3.12% | 45.39% | 34.49% | -10.16% | 0.977 | 0.496 | 1.155 | -10.16% |
| SOLAR | TAN | clean_energy | -4.34% | -10.06% | -23.57% | 33.99% | -22.13% | -0.495 | 0.647 | 1.933 | -43.39% |
| METALS_MINING | XME | materials_and_mining | -5.11% | -9.62% | -12.94% | 36.08% | -18.76% | -0.769 | 0.603 | 1.803 | -23.92% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | 0.49% | 0.41% | -2.26% | 10.02% | -6.27% | -0.159 | 0.766 | 0.692 | -3.54% |
| BIOTECH | XBI | healthcare_and_biotech | -6.15% | -9.14% | 6.57% | 29.98% | -14.88% | 0.476 | 0.477 | 1.080 | -14.88% |
| REGIONAL_BANKS | KRE | financials | 1.16% | -3.82% | -3.69% | 14.59% | -11.55% | 0.552 | 0.398 | 0.667 | -9.91% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | 1.17% | -2.58% | -15.28% | 19.97% | -19.50% | 0.146 | 0.551 | 1.000 | -17.34% |
| CANADA | EWC | international_equity | 2.63% | -0.05% | -3.95% | 13.21% | -7.50% | 0.065 | 0.661 | 0.765 | -3.29% |
| UNITED_KINGDOM | EWU | international_equity | 3.20% | -0.21% | -6.86% | 11.30% | -7.09% | -0.294 | 0.595 | 0.705 | -2.79% |
| AUSTRALIA | EWA | international_equity | 0.38% | -1.71% | -9.88% | 16.28% | -8.02% | 0.189 | 0.677 | 0.962 | -5.59% |
| SOUTH_KOREA | EWY | international_equity | -15.12% | -17.85% | 12.07% | 56.11% | -21.90% | -0.497 | 0.640 | 2.900 | -31.37% |
| TAIWAN | EWT | international_equity | -7.04% | -4.29% | 25.28% | 31.82% | -12.07% | -0.251 | 0.748 | 1.854 | -9.95% |
| BRAZIL | EWZ | international_equity | -3.93% | 10.50% | -15.10% | 33.84% | -8.05% | 2.361 | 0.441 | 0.982 | -3.93% |
| MEXICO | EWW | international_equity | 4.16% | 0.54% | -12.79% | 17.73% | -10.38% | -0.116 | 0.550 | 0.955 | -6.39% |
| SOUTH_AFRICA | EZA | international_equity | 2.32% | -5.30% | -13.59% | 27.72% | -14.09% | -0.297 | 0.617 | 1.604 | -18.25% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | 0.81% | -1.33% | -9.84% | 5.76% | -4.25% | 5.914 | 0.422 | 0.159 | -3.85% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | 1.26% | -0.84% | -10.28% | 5.17% | -5.28% | 5.086 | 0.372 | 0.105 | -4.07% |
| EMERGING_MARKET_BONDS | EMB | credit | 0.38% | -2.14% | -8.68% | 5.98% | -4.61% | 1.441 | 0.686 | 0.320 | -3.77% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | 0.32% | -0.05% | -9.01% | 3.67% | -2.15% | 0.597 | 0.515 | 0.151 | -2.38% |
| SILVER | SLV | precious_metals | -5.97% | -12.98% | -27.57% | 39.48% | -19.99% | -0.500 | 0.387 | 1.916 | -51.22% |
| COPPER | CPER | non_energy_commodities | -2.01% | -0.74% | -1.31% | 22.96% | -6.80% | -0.419 | 0.558 | 1.229 | -4.66% |
| AGRICULTURE | DBA | non_energy_commodities | -0.35% | -1.00% | -2.09% | 12.48% | -4.61% | -0.656 | 0.058 | 0.051 | -4.27% |
| OIL | USO | energy | 9.15% | 3.82% | 26.18% | 48.83% | -17.64% | -0.444 | -0.388 | -1.509 | -0.06% |
| US_DOLLAR | UUP | currencies | -0.34% | 1.57% | -3.94% | 5.33% | -2.52% | -0.087 | -0.330 | -0.142 | -0.72% |
| EURO | FXE | currencies | 0.37% | -2.29% | -9.85% | 4.86% | -4.32% | -0.199 | 0.316 | 0.134 | -6.04% |
| YEN | FXY | currencies | 0.17% | -1.63% | -6.16% | 9.88% | -3.38% | -0.515 | 0.222 | 0.141 | -5.15% |
| BITCOIN_ETF | IBIT | crypto_assets | -0.86% | 6.25% | -9.12% | 37.10% | -7.14% | -0.305 | 0.502 | 1.783 | -29.30% |
| ETHEREUM_ETF | ETHA | crypto_assets | -2.64% | -1.96% | -7.17% | 46.66% | -12.85% | -0.024 | 0.505 | 2.502 | -42.77% |
