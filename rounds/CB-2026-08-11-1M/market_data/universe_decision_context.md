# Full-Universe Horizon-Specific Decision Context

Profile: monthly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: yahoo_chart_adjusted_close_and_reported_volume
- As-of date requested: 2026-08-10
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | 2.03% |
| spy_return_21s | 2.39% |
| rsp_return_5s | 1.43% |
| rsp_return_21s | 2.76% |
| hyg_return_5s | 0.21% |
| hyg_return_21s | 0.20% |
| tlt_return_5s | -0.16% |
| tlt_return_21s | -2.46% |
| uup_return_5s | -0.11% |
| uup_return_21s | -0.88% |
| uso_return_5s | 3.11% |
| uso_return_21s | 15.84% |
| iau_return_5s | 8.30% |
| iau_return_21s | 6.80% |
| rsp_minus_spy_5s | -0.59% |
| rsp_minus_spy_21s | 0.37% |
| positive_asset_share_5s | 78.26% |
| positive_asset_share_21s | 68.12% |
| active_return_dispersion_5s |  |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_5s | active_return_21s | prior_105s_active_return | volatility_63s | max_drawdown_63s | volume_zscore_20v120 | corr_spy_252s | beta_spy_252s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | -2.39% | -9.90% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.07% | -2.12% | -8.38% | 0.21% | -0.01% | -0.234 | -0.102 | -0.002 | 0.00% |
| SP500 | SPY | diversified_us_equity | 2.03% | 0.00% | 0.00% | 13.94% | -4.49% | -0.791 | 1.000 | 1.000 | -0.03% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | 2.08% | 0.00% | 0.07% | 13.89% | -4.36% | -0.781 | 0.995 | 1.013 | -0.04% |
| NASDAQ100 | QQQ | technology_and_growth | 2.97% | -3.03% | 9.39% | 25.88% | -11.22% | -0.703 | 0.931 | 1.416 | -3.28% |
| LARGE_GROWTH | IWF | technology_and_growth | 2.73% | -2.22% | -1.18% | 21.04% | -11.35% | -0.750 | 0.937 | 1.281 | -3.49% |
| LARGE_VALUE | IWD | diversified_us_equity | 1.60% | 2.25% | 0.79% | 11.29% | -2.40% | -0.638 | 0.805 | 0.704 | 0.00% |
| MID_CAP | IJH | diversified_us_equity | 1.88% | 0.08% | -3.89% | 14.38% | -3.43% | -0.884 | 0.804 | 0.987 | -0.32% |
| SMALL_CAP | IWM | diversified_us_equity | 1.27% | -1.05% | 2.25% | 18.21% | -4.32% | -1.030 | 0.816 | 1.227 | -0.57% |
| SMALL_VALUE | IWN | diversified_us_equity | -0.07% | -0.43% | 0.62% | 14.71% | -3.50% | -0.385 | 0.728 | 0.976 | -1.18% |
| DIVIDEND | SCHD | diversified_us_equity | 1.88% | 3.13% | -5.24% | 11.73% | -2.95% | 0.195 | 0.294 | 0.253 | 0.00% |
| LOW_VOL | SPLV | diversified_us_equity | -0.67% | -2.40% | -7.64% | 13.20% | -3.75% | -0.768 | 0.017 | 0.014 | -2.91% |
| MOMENTUM | MTUM | diversified_us_equity | 1.84% | -6.89% | 17.29% | 38.63% | -17.99% | 1.271 | 0.779 | 1.560 | -10.98% |
| TECHNOLOGY | XLK | technology_and_growth | 4.65% | -2.10% | 22.06% | 35.42% | -15.86% | -0.956 | 0.859 | 1.731 | -5.89% |
| COMMUNICATIONS | XLC | technology_and_growth | 0.44% | -2.22% | -12.90% | 18.94% | -9.78% | -0.377 | 0.582 | 0.675 | -6.33% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | 1.24% | -0.32% | -10.13% | 22.05% | -10.72% | -0.498 | 0.778 | 1.172 | -3.51% |
| CONSUMER_STAPLES | XLP | consumer_defensive | 0.11% | -1.41% | -13.03% | 17.14% | -4.95% | -0.777 | -0.071 | -0.078 | -4.43% |
| HEALTHCARE | XLV | healthcare_and_biotech | 3.82% | 2.33% | -7.04% | 18.49% | -3.74% | -0.579 | 0.228 | 0.276 | 0.00% |
| FINANCIALS | XLF | financials | 0.75% | 1.37% | -6.33% | 13.53% | -2.08% | -0.736 | 0.548 | 0.622 | -0.33% |
| INDUSTRIALS | XLI | industrials_and_defense | 0.79% | -0.92% | -4.29% | 18.79% | -4.80% | -0.978 | 0.721 | 0.955 | -0.97% |
| ENERGY | XLE | energy | 2.36% | 6.86% | -5.03% | 24.78% | -13.21% | -0.881 | -0.150 | -0.252 | -3.11% |
| MATERIALS | XLB | materials_and_mining | 4.25% | 2.11% | -10.29% | 20.32% | -6.16% | -0.530 | 0.541 | 0.748 | -0.01% |
| UTILITIES | XLU | rate_sensitive_defensive | -2.77% | -7.42% | -3.74% | 16.26% | -6.83% | -0.535 | 0.126 | 0.146 | -8.42% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | -1.73% | -2.51% | -2.39% | 15.99% | -3.50% | -0.700 | 0.234 | 0.257 | -3.50% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | -0.06% | -2.98% | -10.85% | 5.03% | -2.00% | -0.300 | 0.286 | 0.102 | -3.46% |
| LONG_TREASURY | TLT | rates_and_duration | -0.16% | -4.86% | -11.59% | 9.37% | -5.60% | -0.060 | 0.234 | 0.169 | -7.58% |
| TIPS | TIP | rates_and_duration | 0.00% | -2.84% | -9.59% | 3.42% | -1.53% | -0.471 | 0.275 | 0.071 | -1.29% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | -0.14% | -3.36% | -10.86% | 5.33% | -2.83% | -0.362 | 0.477 | 0.196 | -2.94% |
| HIGH_YIELD_CREDIT | HYG | credit | 0.21% | -2.20% | -8.79% | 3.44% | -0.99% | -0.624 | 0.779 | 0.234 | -0.16% |
| AGGREGATE_BONDS | AGG | rates_and_duration | -0.02% | -2.91% | -10.31% | 4.15% | -1.71% | -0.271 | 0.396 | 0.115 | -2.16% |
| DEVELOPED_EX_US | VEA | international_equity | 2.06% | -0.27% | -3.79% | 19.73% | -4.85% | -0.930 | 0.805 | 1.081 | -0.54% |
| EMERGING_MARKETS | VWO | international_equity | 2.15% | -1.66% | -5.18% | 20.26% | -7.05% | -0.690 | 0.811 | 1.111 | -1.49% |
| EUROPE | VGK | international_equity | 1.46% | 1.77% | -7.97% | 15.74% | -3.12% | -0.839 | 0.748 | 0.921 | -0.37% |
| JAPAN | EWJ | international_equity | 3.38% | -0.81% | -3.56% | 23.15% | -7.86% | -0.900 | 0.721 | 1.178 | -0.95% |
| CHINA | MCHI | international_equity | 1.84% | 4.76% | -23.17% | 20.33% | -15.01% | -0.527 | 0.548 | 0.873 | -13.41% |
| INDIA | INDA | international_equity | -0.04% | -0.69% | -17.37% | 15.39% | -5.28% | -0.507 | 0.541 | 0.637 | -9.31% |
| GOLD | IAU | precious_metals | 8.30% | 4.40% | -27.03% | 24.88% | -16.01% | -0.509 | 0.314 | 0.689 | -18.77% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | 3.36% | 6.06% | 5.39% | 23.03% | -16.55% | 0.232 | -0.172 | -0.268 | -5.71% |
| SEMICONDUCTORS | SMH | technology_and_growth | 4.39% | -9.21% | 42.23% | 54.38% | -24.62% | 0.680 | 0.787 | 2.376 | -14.87% |
| SOFTWARE | IGV | technology_and_growth | 7.79% | 11.24% | 2.19% | 34.84% | -21.29% | -0.899 | 0.507 | 1.173 | -10.83% |
| BROAD_AI_TECH | AIQ | technology_and_growth | 4.85% | -2.28% | 16.78% | 40.20% | -20.19% | -0.271 | 0.848 | 1.907 | -9.45% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | 7.81% | 0.75% | -8.93% | 38.96% | -23.82% | -0.647 | 0.802 | 2.193 | -11.08% |
| CYBERSECURITY | CIBR | technology_and_growth | 7.12% | 7.10% | 27.33% | 32.41% | -11.74% | -0.409 | 0.538 | 1.098 | 0.00% |
| SOLAR | TAN | clean_energy | 1.21% | -8.04% | -14.71% | 46.96% | -35.51% | -0.269 | 0.606 | 1.878 | -29.85% |
| METALS_MINING | XME | materials_and_mining | 13.99% | 10.96% | -25.14% | 42.31% | -26.49% | -0.330 | 0.606 | 1.766 | -11.45% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | 1.43% | 0.37% | -3.08% | 11.08% | -2.04% | -0.801 | 0.770 | 0.703 | -0.00% |
| BIOTECH | XBI | healthcare_and_biotech | 7.28% | -3.02% | 16.94% | 30.18% | -10.51% | -0.432 | 0.485 | 1.023 | -3.80% |
| REGIONAL_BANKS | KRE | financials | -1.34% | -1.05% | -6.82% | 19.71% | -4.12% | -0.683 | 0.439 | 0.778 | -2.43% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | 2.05% | 2.65% | -7.56% | 25.06% | -8.58% | -0.377 | 0.573 | 1.011 | -0.46% |
| CANADA | EWC | international_equity | 3.10% | 2.46% | -2.78% | 12.08% | -3.20% | -0.548 | 0.670 | 0.741 | 0.00% |
| UNITED_KINGDOM | EWU | international_equity | 0.54% | 1.66% | -9.11% | 14.73% | -3.40% | -0.572 | 0.606 | 0.705 | -0.39% |
| AUSTRALIA | EWA | international_equity | 2.21% | 3.23% | -7.70% | 17.13% | -5.17% | -0.848 | 0.676 | 0.929 | -1.18% |
| SOUTH_KOREA | EWY | international_equity | 1.80% | -13.51% | 37.26% | 81.08% | -34.21% | 0.391 | 0.645 | 2.745 | -25.58% |
| TAIWAN | EWT | international_equity | 4.29% | -6.17% | 41.70% | 44.59% | -19.83% | -0.146 | 0.762 | 1.840 | -8.38% |
| BRAZIL | EWZ | international_equity | -3.38% | -4.45% | -13.32% | 22.76% | -13.88% | -0.978 | 0.505 | 0.984 | -14.87% |
| MEXICO | EWW | international_equity | 0.50% | 0.37% | -14.79% | 19.38% | -7.30% | -0.560 | 0.547 | 0.934 | -3.90% |
| SOUTH_AFRICA | EZA | international_equity | 8.39% | 6.87% | -22.67% | 31.40% | -13.92% | -0.552 | 0.630 | 1.599 | -12.67% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | 0.22% | -2.88% | -10.05% | 4.97% | -1.93% | -0.290 | 0.394 | 0.135 | -2.06% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | 0.38% | -3.21% | -9.19% | 3.16% | -2.15% | 0.780 | 0.378 | 0.087 | -1.33% |
| EMERGING_MARKET_BONDS | EMB | credit | 0.09% | -3.16% | -8.45% | 5.67% | -1.98% | -0.701 | 0.683 | 0.304 | -1.20% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | -0.10% | -2.75% | -9.73% | 4.15% | -1.44% | -0.713 | 0.456 | 0.127 | -1.51% |
| SILVER | SLV | precious_metals | 13.25% | 7.73% | -33.03% | 49.50% | -36.50% | -0.564 | 0.357 | 1.710 | -43.74% |
| COPPER | CPER | non_energy_commodities | 1.36% | 3.37% | -5.07% | 28.21% | -10.57% | -0.503 | 0.550 | 1.201 | -1.64% |
| AGRICULTURE | DBA | non_energy_commodities | 0.11% | -2.21% | -2.13% | 13.98% | -8.67% | -0.542 | 0.082 | 0.071 | -3.17% |
| OIL | USO | energy | 3.11% | 13.45% | 31.29% | 54.90% | -32.49% | -0.550 | -0.333 | -1.239 | -17.68% |
| US_DOLLAR | UUP | currencies | -0.11% | -3.28% | -4.79% | 5.02% | -1.85% | -0.219 | -0.315 | -0.141 | -1.61% |
| EURO | FXE | currencies | 0.30% | -1.17% | -13.08% | 4.80% | -3.57% | -0.880 | 0.298 | 0.133 | -3.69% |
| YEN | FXY | currencies | -1.50% | -0.84% | -12.90% | 7.65% | -4.44% | 1.306 | 0.181 | 0.115 | -8.28% |
| BITCOIN_ETF | IBIT | crypto_assets | 0.19% | -2.39% | -18.59% | 36.74% | -28.36% | -0.595 | 0.504 | 1.737 | -49.18% |
| ETHEREUM_ETF | ETHA | crypto_assets | 0.21% | 2.11% | -22.66% | 52.97% | -33.56% | -0.314 | 0.536 | 2.781 | -61.36% |
