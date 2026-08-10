# Full-Universe Horizon-Specific Decision Context

Profile: weekly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: yahoo_chart_adjusted_close_and_reported_volume
- As-of date requested: 2026-08-07
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | 3.51% |
| spy_return_21s | 2.87% |
| rsp_return_5s | 2.36% |
| rsp_return_21s | 3.09% |
| hyg_return_5s | 0.65% |
| hyg_return_21s | 0.31% |
| tlt_return_5s | 1.03% |
| tlt_return_21s | -1.65% |
| uup_return_5s | -0.35% |
| uup_return_21s | -1.02% |
| uso_return_5s | -8.66% |
| uso_return_21s | 8.23% |
| iau_return_5s | 7.23% |
| iau_return_21s | 5.38% |
| rsp_minus_spy_5s | -1.15% |
| rsp_minus_spy_21s | 0.22% |
| positive_asset_share_5s | 88.41% |
| positive_asset_share_21s | 72.46% |
| active_return_dispersion_5s | 3.68% |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_3s | active_return_5s | prior_16s_active_return | volatility_21s | max_drawdown_21s | volume_zscore_5v60 | corr_spy_63s | beta_spy_63s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | -3.51% | 0.62% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.07% | -3.43% | 0.86% | 0.19% | 0.00% | 0.727 | -0.128 | -0.002 | 0.00% |
| SP500 | SPY | diversified_us_equity | 0.25% | 0.00% | 0.00% | 14.05% | -3.38% | -0.151 | 1.000 | 1.000 | 0.00% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | 0.25% | 0.17% | -0.25% | 14.03% | -3.29% | -0.472 | 0.993 | 0.988 | 0.00% |
| NASDAQ100 | QQQ | technology_and_growth | -0.11% | 1.58% | -4.26% | 25.59% | -8.79% | -0.297 | 0.922 | 1.729 | -2.99% |
| LARGE_GROWTH | IWF | technology_and_growth | 0.24% | 1.80% | -3.42% | 24.20% | -7.99% | -0.923 | 0.910 | 1.367 | -3.15% |
| LARGE_VALUE | IWD | diversified_us_equity | 0.36% | -1.23% | 2.83% | 9.18% | -1.31% | -0.457 | 0.724 | 0.587 | 0.00% |
| MID_CAP | IJH | diversified_us_equity | 0.40% | -0.16% | 0.05% | 12.95% | -1.71% | -0.483 | 0.799 | 0.819 | 0.00% |
| SMALL_CAP | IWM | diversified_us_equity | -0.05% | 0.05% | -1.41% | 15.32% | -2.92% | -0.972 | 0.790 | 1.026 | -0.05% |
| SMALL_VALUE | IWN | diversified_us_equity | -0.64% | -1.58% | 1.42% | 12.23% | -1.61% | 0.133 | 0.664 | 0.696 | -0.64% |
| DIVIDEND | SCHD | diversified_us_equity | 0.15% | -2.23% | 4.37% | 13.00% | -1.42% | 0.619 | 0.091 | 0.076 | 0.00% |
| LOW_VOL | SPLV | diversified_us_equity | -0.24% | -3.54% | 1.78% | 11.84% | -2.26% | 0.040 | -0.291 | -0.274 | -2.26% |
| MOMENTUM | MTUM | diversified_us_equity | -1.29% | -0.26% | -6.11% | 37.63% | -12.01% | -0.054 | 0.738 | 2.050 | -10.40% |
| TECHNOLOGY | XLK | technology_and_growth | 0.57% | 3.69% | -4.77% | 35.02% | -10.34% | -0.823 | 0.845 | 2.169 | -5.05% |
| COMMUNICATIONS | XLC | technology_and_growth | -0.71% | -0.73% | -1.43% | 24.12% | -7.06% | -0.563 | 0.391 | 0.528 | -6.82% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | 1.33% | -0.26% | -0.03% | 24.81% | -7.31% | -0.370 | 0.685 | 1.079 | -3.36% |
| CONSUMER_STAPLES | XLP | consumer_defensive | -0.29% | -3.43% | 2.85% | 18.62% | -3.03% | -0.749 | -0.337 | -0.413 | -4.24% |
| HEALTHCARE | XLV | healthcare_and_biotech | 2.21% | -1.59% | 0.86% | 17.72% | -3.09% | 0.429 | -0.183 | -0.240 | -0.94% |
| FINANCIALS | XLF | financials | -0.48% | -2.35% | 3.14% | 10.90% | -1.62% | -0.862 | 0.262 | 0.254 | -0.69% |
| INDUSTRIALS | XLI | industrials_and_defense | -0.65% | -0.54% | -0.08% | 17.40% | -3.57% | -0.153 | 0.668 | 0.896 | -0.65% |
| ENERGY | XLE | energy | -1.74% | -6.95% | 9.25% | 20.88% | -3.87% | -0.631 | -0.355 | -0.583 | -7.43% |
| MATERIALS | XLB | materials_and_mining | 1.65% | 1.31% | 0.96% | 19.18% | -3.65% | 0.278 | 0.475 | 0.688 | -0.61% |
| UTILITIES | XLU | rate_sensitive_defensive | -1.13% | -5.18% | -1.11% | 13.42% | -6.29% | 0.964 | -0.076 | -0.088 | -7.41% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | -0.42% | -3.71% | 2.52% | 13.21% | -2.61% | 0.445 | -0.172 | -0.194 | -2.24% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | -0.09% | -2.93% | -0.19% | 4.35% | -1.05% | 3.239 | 0.510 | 0.182 | -3.04% |
| LONG_TREASURY | TLT | rates_and_duration | -0.07% | -2.49% | -2.03% | 8.88% | -2.69% | 2.271 | 0.416 | 0.276 | -6.79% |
| TIPS | TIP | rates_and_duration | 0.03% | -3.29% | 0.17% | 2.42% | -0.81% | -0.030 | 0.501 | 0.124 | -1.09% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | -0.20% | -2.79% | -0.73% | 5.02% | -1.38% | -0.007 | 0.593 | 0.224 | -2.40% |
| HIGH_YIELD_CREDIT | HYG | credit | 0.08% | -2.86% | 0.28% | 2.97% | -0.73% | -0.355 | 0.793 | 0.197 | 0.00% |
| AGGREGATE_BONDS | AGG | rates_and_duration | -0.06% | -2.93% | -0.20% | 3.79% | -0.88% | 0.899 | 0.558 | 0.164 | -1.80% |
| DEVELOPED_EX_US | VEA | international_equity | 0.93% | -0.30% | 0.47% | 18.17% | -2.87% | -0.668 | 0.821 | 1.168 | 0.00% |
| EMERGING_MARKETS | VWO | international_equity | 0.70% | -0.58% | -0.62% | 18.02% | -4.96% | -0.364 | 0.855 | 1.237 | -1.26% |
| EUROPE | VGK | international_equity | 0.83% | -1.29% | 3.09% | 13.47% | -1.60% | -0.301 | 0.727 | 0.820 | 0.00% |
| JAPAN | EWJ | international_equity | 2.42% | 1.37% | -0.59% | 25.38% | -5.50% | -1.103 | 0.753 | 1.246 | -0.07% |
| CHINA | MCHI | international_equity | 0.86% | -2.13% | 5.53% | 16.45% | -2.22% | -0.672 | 0.407 | 0.590 | -13.96% |
| INDIA | INDA | international_equity | -0.32% | -2.37% | 2.21% | 12.71% | -3.39% | -0.503 | 0.553 | 0.606 | -8.90% |
| GOLD | IAU | precious_metals | 6.51% | 3.72% | -1.11% | 25.38% | -3.50% | 0.789 | 0.544 | 0.963 | -19.58% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | 2.07% | -5.28% | 7.57% | 25.48% | -6.42% | 0.394 | -0.188 | -0.294 | -8.78% |
| SEMICONDUCTORS | SMH | technology_and_growth | 1.21% | 4.29% | -10.43% | 50.35% | -17.48% | -0.944 | 0.778 | 3.054 | -12.89% |
| SOFTWARE | IGV | technology_and_growth | 0.68% | 5.06% | 1.37% | 31.39% | -7.28% | -0.886 | 0.445 | 1.098 | -12.80% |
| BROAD_AI_TECH | AIQ | technology_and_growth | 0.35% | 4.06% | -7.12% | 37.07% | -12.30% | -0.787 | 0.828 | 2.418 | -9.68% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | 2.42% | 7.60% | -7.10% | 39.82% | -12.14% | -0.150 | 0.872 | 2.462 | -11.10% |
| CYBERSECURITY | CIBR | technology_and_growth | -0.09% | 3.04% | -1.96% | 28.10% | -7.40% | -0.349 | 0.551 | 1.276 | -0.09% |
| SOLAR | TAN | clean_energy | -1.16% | 3.42% | -9.60% | 45.59% | -14.55% | 0.348 | 0.757 | 2.566 | -28.65% |
| METALS_MINING | XME | materials_and_mining | 7.31% | 11.48% | -1.89% | 43.09% | -6.55% | 0.846 | 0.673 | 2.025 | -12.81% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | -0.06% | -1.15% | 1.33% | 10.67% | -1.46% | -0.784 | 0.698 | 0.552 | -0.06% |
| BIOTECH | XBI | healthcare_and_biotech | 3.61% | 3.54% | -9.89% | 29.57% | -10.51% | -0.357 | 0.362 | 0.780 | -4.21% |
| REGIONAL_BANKS | KRE | financials | -2.09% | -3.31% | 2.51% | 16.70% | -3.55% | -0.647 | 0.188 | 0.264 | -2.19% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | 0.04% | 1.12% | 0.64% | 24.27% | -4.32% | -0.406 | 0.485 | 0.868 | -0.61% |
| CANADA | EWC | international_equity | 2.17% | -0.30% | 2.35% | 10.93% | -1.46% | 0.517 | 0.594 | 0.512 | 0.00% |
| UNITED_KINGDOM | EWU | international_equity | 0.62% | -3.04% | 4.93% | 11.71% | -1.23% | 0.402 | 0.424 | 0.447 | -0.08% |
| AUSTRALIA | EWA | international_equity | 0.96% | 0.14% | 4.67% | 16.80% | -1.61% | -0.359 | 0.616 | 0.744 | 0.00% |
| SOUTH_KOREA | EWY | international_equity | -2.95% | 2.21% | -14.34% | 77.85% | -21.94% | -0.473 | 0.705 | 4.145 | -24.23% |
| TAIWAN | EWT | international_equity | 0.86% | 3.26% | -7.47% | 44.81% | -15.80% | -0.884 | 0.796 | 2.536 | -7.57% |
| BRAZIL | EWZ | international_equity | -2.08% | -7.09% | 5.46% | 23.26% | -3.57% | -0.355 | 0.398 | 0.649 | -14.51% |
| MEXICO | EWW | international_equity | 0.60% | -2.59% | 4.08% | 16.68% | -2.23% | 1.301 | 0.607 | 0.837 | -3.16% |
| SOUTH_AFRICA | EZA | international_equity | 5.59% | 5.97% | 1.16% | 28.37% | -5.31% | -0.542 | 0.733 | 1.646 | -12.77% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | -0.03% | -2.76% | -0.34% | 4.97% | -1.01% | -0.253 | 0.557 | 0.197 | -1.69% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | 0.17% | -2.96% | -0.59% | 3.47% | -1.64% | 0.527 | 0.561 | 0.126 | -1.25% |
| EMERGING_MARKET_BONDS | EMB | credit | 0.02% | -2.46% | -0.73% | 5.44% | -1.52% | -0.132 | 0.749 | 0.301 | -0.79% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | -0.04% | -2.88% | 0.10% | 3.48% | -0.77% | -0.342 | 0.534 | 0.156 | -1.18% |
| SILVER | SLV | precious_metals | 6.80% | 6.31% | -2.67% | 38.22% | -6.93% | -0.472 | 0.587 | 2.058 | -45.55% |
| COPPER | CPER | non_energy_commodities | -0.60% | -2.65% | 5.42% | 22.38% | -3.26% | -0.090 | 0.636 | 1.297 | -2.33% |
| AGRICULTURE | DBA | non_energy_commodities | -0.14% | -3.11% | -0.10% | 13.56% | -2.87% | -0.522 | 0.142 | 0.141 | -3.86% |
| OIL | USO | energy | 1.90% | -12.17% | 19.12% | 67.04% | -17.64% | -0.341 | -0.349 | -1.326 | -22.87% |
| US_DOLLAR | UUP | currencies | -0.32% | -3.87% | -0.05% | 5.72% | -1.85% | -0.142 | -0.428 | -0.154 | -1.85% |
| EURO | FXE | currencies | 0.29% | -3.25% | 1.64% | 4.63% | -0.81% | -0.373 | 0.457 | 0.159 | -3.54% |
| YEN | FXY | currencies | 0.15% | -2.51% | 2.71% | 11.34% | -1.30% | 0.710 | 0.245 | 0.129 | -7.29% |
| BITCOIN_ETF | IBIT | crypto_assets | 1.13% | -0.26% | 0.15% | 27.04% | -5.39% | -0.532 | 0.454 | 1.187 | -48.38% |
| ETHEREUM_ETF | ETHA | crypto_assets | 2.26% | -0.67% | 7.29% | 39.16% | -4.35% | -0.325 | 0.542 | 2.045 | -60.45% |
