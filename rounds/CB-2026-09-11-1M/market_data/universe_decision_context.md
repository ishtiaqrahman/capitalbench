# Full-Universe Horizon-Specific Decision Context

Profile: monthly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: tiingo_eod_adjusted_price_and_volume
- As-of date requested: 2026-09-10
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | -0.96% |
| spy_return_21s | -1.65% |
| rsp_return_5s | -2.48% |
| rsp_return_21s | -3.41% |
| hyg_return_5s | -0.62% |
| hyg_return_21s | -0.58% |
| tlt_return_5s | -1.43% |
| tlt_return_21s | -1.34% |
| uup_return_5s | -0.50% |
| uup_return_21s | -0.39% |
| uso_return_5s | 12.21% |
| uso_return_21s | 24.11% |
| iau_return_5s | -1.55% |
| iau_return_21s | -1.11% |
| rsp_minus_spy_5s | -1.53% |
| rsp_minus_spy_21s | -1.76% |
| positive_asset_share_5s | 21.74% |
| positive_asset_share_21s | 21.74% |
| active_return_dispersion_5s |  |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_5s | active_return_21s | prior_105s_active_return | volatility_63s | max_drawdown_63s | volume_zscore_20v120 | corr_spy_252s | beta_spy_252s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | 1.65% | -14.54% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.08% | 1.94% | -13.03% | 0.20% | -0.01% | -0.600 | -0.097 | -0.001 | 0.00% |
| SP500 | SPY | diversified_us_equity | -0.96% | 0.00% | 0.00% | 12.55% | -3.38% | -1.053 | 1.000 | 1.000 | -2.58% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | -0.97% | -0.29% | 0.38% | 12.41% | -3.29% | -0.671 | 0.995 | 1.012 | -2.88% |
| NASDAQ100 | QQQ | technology_and_growth | -0.08% | 0.29% | 3.96% | 23.38% | -10.96% | -1.050 | 0.928 | 1.420 | -4.92% |
| LARGE_GROWTH | IWF | technology_and_growth | -0.40% | -0.19% | -4.80% | 20.05% | -8.29% | -0.740 | 0.934 | 1.288 | -5.70% |
| LARGE_VALUE | IWD | diversified_us_equity | -1.46% | -0.13% | 4.82% | 10.51% | -2.33% | -0.570 | 0.800 | 0.701 | -2.33% |
| MID_CAP | IJH | diversified_us_equity | -1.66% | -3.38% | -0.24% | 13.30% | -6.11% | -0.705 | 0.811 | 0.979 | -6.11% |
| SMALL_CAP | IWM | diversified_us_equity | -2.15% | -2.76% | 4.99% | 14.99% | -5.70% | -1.034 | 0.820 | 1.205 | -5.70% |
| SMALL_VALUE | IWN | diversified_us_equity | -1.82% | -1.01% | 4.31% | 12.03% | -3.72% | -0.944 | 0.738 | 0.944 | -3.72% |
| DIVIDEND | SCHD | diversified_us_equity | -2.91% | 0.84% | -2.17% | 12.01% | -3.46% | 0.202 | 0.291 | 0.252 | -3.46% |
| LOW_VOL | SPLV | diversified_us_equity | -1.33% | -0.78% | -12.27% | 11.76% | -5.34% | -0.718 | 0.023 | 0.019 | -5.34% |
| MOMENTUM | MTUM | diversified_us_equity | 2.06% | -0.03% | 9.64% | 35.53% | -17.99% | -0.430 | 0.760 | 1.560 | -12.19% |
| TECHNOLOGY | XLK | technology_and_growth | 0.88% | 1.18% | 18.29% | 31.36% | -13.31% | -1.322 | 0.850 | 1.742 | -6.44% |
| COMMUNICATIONS | XLC | technology_and_growth | -0.82% | 1.86% | -18.88% | 19.84% | -7.06% | -1.005 | 0.566 | 0.672 | -6.60% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | -2.52% | -4.45% | -9.65% | 21.28% | -8.09% | -1.081 | 0.766 | 1.163 | -9.73% |
| CONSUMER_STAPLES | XLP | consumer_defensive | -2.85% | -0.24% | -13.16% | 16.72% | -5.03% | -0.757 | -0.059 | -0.066 | -6.52% |
| HEALTHCARE | XLV | healthcare_and_biotech | -4.22% | 0.25% | -3.69% | 19.29% | -5.70% | -0.949 | 0.230 | 0.291 | -5.70% |
| FINANCIALS | XLF | financials | -1.37% | 0.04% | 2.90% | 13.01% | -2.89% | -0.756 | 0.540 | 0.615 | -2.89% |
| INDUSTRIALS | XLI | industrials_and_defense | -1.29% | -6.51% | -4.40% | 17.55% | -8.56% | -0.694 | 0.712 | 0.955 | -8.56% |
| ENERGY | XLE | energy | -0.26% | 8.22% | -6.15% | 21.97% | -8.69% | -0.799 | -0.183 | -0.309 | -0.58% |
| MATERIALS | XLB | materials_and_mining | -4.14% | -3.01% | -6.85% | 18.74% | -5.42% | -0.448 | 0.537 | 0.749 | -5.42% |
| UTILITIES | XLU | rate_sensitive_defensive | -0.35% | -0.89% | -18.78% | 14.45% | -8.77% | -0.347 | 0.120 | 0.142 | -9.73% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | -1.55% | -0.68% | -9.00% | 14.62% | -6.43% | -0.425 | 0.249 | 0.272 | -6.43% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | -1.08% | 0.19% | -16.17% | 4.98% | -3.09% | -0.351 | 0.291 | 0.105 | -4.76% |
| LONG_TREASURY | TLT | rates_and_duration | -1.43% | 0.31% | -18.38% | 9.84% | -6.55% | -0.003 | 0.242 | 0.173 | -8.67% |
| TIPS | TIP | rates_and_duration | -0.50% | 1.13% | -15.01% | 3.58% | -1.58% | -0.400 | 0.264 | 0.068 | -1.78% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | -0.94% | 0.53% | -15.52% | 5.51% | -3.72% | -0.506 | 0.477 | 0.196 | -4.01% |
| HIGH_YIELD_CREDIT | HYG | credit | -0.62% | 1.08% | -12.50% | 3.02% | -1.09% | -0.562 | 0.776 | 0.230 | -1.09% |
| AGGREGATE_BONDS | AGG | rates_and_duration | -0.82% | 0.69% | -15.22% | 4.14% | -2.34% | -0.344 | 0.399 | 0.117 | -3.02% |
| DEVELOPED_EX_US | VEA | international_equity | -0.92% | 0.59% | -3.40% | 17.38% | -4.75% | -0.743 | 0.802 | 1.087 | -2.53% |
| EMERGING_MARKETS | VWO | international_equity | -1.37% | 1.35% | -6.21% | 17.02% | -7.05% | -0.854 | 0.815 | 1.116 | -2.44% |
| EUROPE | VGK | international_equity | -1.69% | -1.47% | -3.33% | 13.46% | -4.05% | -0.879 | 0.748 | 0.917 | -4.05% |
| JAPAN | EWJ | international_equity | 0.42% | 1.82% | -1.64% | 22.38% | -7.86% | -0.801 | 0.727 | 1.184 | -2.06% |
| CHINA | MCHI | international_equity | -3.19% | -3.42% | -18.53% | 16.95% | -8.10% | -0.833 | 0.563 | 0.872 | -19.69% |
| INDIA | INDA | international_equity | -3.72% | -2.30% | -12.88% | 13.13% | -4.79% | -0.966 | 0.559 | 0.663 | -12.99% |
| GOLD | IAU | precious_metals | -1.55% | 0.54% | -30.30% | 25.59% | -8.22% | -0.384 | 0.331 | 0.749 | -19.99% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | 5.19% | 13.60% | -7.68% | 22.09% | -9.47% | -0.508 | -0.183 | -0.292 | 0.00% |
| SEMICONDUCTORS | SMH | technology_and_growth | 1.78% | -0.56% | 28.33% | 48.87% | -24.62% | -0.821 | 0.773 | 2.372 | -16.24% |
| SOFTWARE | IGV | technology_and_growth | -2.15% | -0.97% | 6.69% | 33.11% | -8.55% | -1.030 | 0.509 | 1.248 | -14.07% |
| BROAD_AI_TECH | AIQ | technology_and_growth | 0.00% | 1.46% | 12.06% | 33.64% | -16.56% | -0.831 | 0.848 | 1.924 | -10.06% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | 0.21% | -4.44% | -8.89% | 33.97% | -18.66% | -1.230 | 0.805 | 2.204 | -16.22% |
| CYBERSECURITY | CIBR | technology_and_growth | 0.66% | -4.11% | 37.80% | 31.41% | -9.53% | -0.012 | 0.526 | 1.158 | -7.87% |
| SOLAR | TAN | clean_energy | -0.49% | -9.09% | -19.98% | 38.10% | -25.65% | -0.708 | 0.638 | 1.894 | -36.37% |
| METALS_MINING | XME | materials_and_mining | -3.93% | -0.94% | -11.86% | 37.66% | -19.05% | -0.494 | 0.600 | 1.792 | -13.54% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | -2.48% | -1.76% | -1.36% | 10.94% | -4.31% | -1.054 | 0.774 | 0.705 | -4.31% |
| BIOTECH | XBI | healthcare_and_biotech | -5.17% | 0.86% | 10.65% | 29.56% | -10.51% | -0.332 | 0.485 | 1.057 | -7.51% |
| REGIONAL_BANKS | KRE | financials | -0.58% | -2.25% | 6.90% | 17.43% | -6.81% | -0.650 | 0.416 | 0.718 | -5.29% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | -2.26% | -11.68% | -8.86% | 23.80% | -13.78% | -0.379 | 0.572 | 1.038 | -13.78% |
| CANADA | EWC | international_equity | -1.60% | -0.33% | -5.12% | 11.68% | -3.75% | -0.232 | 0.678 | 0.767 | -3.75% |
| UNITED_KINGDOM | EWU | international_equity | -1.43% | 0.06% | -8.74% | 12.55% | -3.77% | -0.684 | 0.603 | 0.702 | -3.77% |
| AUSTRALIA | EWA | international_equity | -3.16% | -1.25% | -9.80% | 16.12% | -4.44% | -0.338 | 0.676 | 0.940 | -4.44% |
| SOUTH_KOREA | EWY | international_equity | 2.19% | 10.94% | 11.35% | 70.96% | -34.21% | -0.793 | 0.632 | 2.766 | -16.61% |
| TAIWAN | EWT | international_equity | -0.47% | 6.44% | 30.00% | 38.37% | -19.83% | -1.132 | 0.751 | 1.833 | -2.91% |
| BRAZIL | EWZ | international_equity | 1.23% | 15.13% | -23.33% | 22.37% | -8.05% | -0.157 | 0.482 | 0.948 | -6.71% |
| MEXICO | EWW | international_equity | -1.27% | 0.35% | -10.97% | 18.26% | -5.37% | -0.597 | 0.552 | 0.945 | -6.01% |
| SOUTH_AFRICA | EZA | international_equity | -0.64% | 3.04% | -15.96% | 28.70% | -11.18% | -0.567 | 0.633 | 1.630 | -12.98% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | -1.11% | 0.35% | -15.02% | 4.90% | -2.62% | 0.226 | 0.395 | 0.137 | -3.22% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | -1.44% | -1.11% | -14.43% | 3.41% | -3.98% | 1.962 | 0.389 | 0.092 | -3.98% |
| EMERGING_MARKET_BONDS | EMB | credit | -0.79% | 0.59% | -13.19% | 5.34% | -2.27% | -0.459 | 0.687 | 0.306 | -2.27% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | -0.60% | 0.11% | -14.25% | 3.80% | -2.49% | -0.329 | 0.468 | 0.133 | -2.96% |
| SILVER | SLV | precious_metals | -2.66% | -0.14% | -39.39% | 42.97% | -20.61% | -0.630 | 0.367 | 1.789 | -45.55% |
| COPPER | CPER | non_energy_commodities | -1.24% | -1.28% | -3.19% | 24.70% | -8.42% | -0.214 | 0.557 | 1.252 | -4.90% |
| AGRICULTURE | DBA | non_energy_commodities | 0.17% | 7.92% | -11.21% | 13.16% | -2.87% | 0.244 | 0.057 | 0.050 | -0.58% |
| OIL | USO | energy | 12.21% | 25.76% | 3.56% | 53.04% | -23.10% | -0.617 | -0.346 | -1.315 | 0.00% |
| US_DOLLAR | UUP | currencies | -0.50% | 1.26% | -12.40% | 5.27% | -2.52% | -1.132 | -0.297 | -0.130 | -1.99% |
| EURO | FXE | currencies | 0.22% | 2.30% | -14.47% | 4.76% | -2.19% | -0.703 | 0.278 | 0.119 | -3.06% |
| YEN | FXY | currencies | 2.89% | 4.72% | -14.80% | 9.63% | -2.49% | 0.311 | 0.175 | 0.116 | -5.44% |
| BITCOIN_ETF | IBIT | crypto_assets | -0.25% | 23.19% | -24.85% | 38.09% | -11.79% | 0.747 | 0.489 | 1.726 | -38.73% |
| ETHEREUM_ETF | ETHA | crypto_assets | 2.83% | 32.54% | -24.16% | 51.31% | -14.68% | 1.235 | 0.504 | 2.541 | -48.14% |
