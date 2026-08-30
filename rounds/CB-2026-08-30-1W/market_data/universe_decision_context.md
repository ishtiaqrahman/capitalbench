# Full-Universe Horizon-Specific Decision Context

Profile: weekly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: yahoo_chart_adjusted_close_and_reported_volume
- As-of date requested: 2026-08-28
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | 0.47% |
| spy_return_21s | 3.73% |
| rsp_return_5s | -0.44% |
| rsp_return_21s | 2.47% |
| hyg_return_5s | 0.16% |
| hyg_return_21s | 0.83% |
| tlt_return_5s | 1.01% |
| tlt_return_21s | 0.50% |
| uup_return_5s | 1.00% |
| uup_return_21s | 0.14% |
| uso_return_5s | -3.67% |
| uso_return_21s | 1.74% |
| iau_return_5s | -3.42% |
| iau_return_21s | 8.43% |
| rsp_minus_spy_5s | -0.92% |
| rsp_minus_spy_21s | -1.26% |
| positive_asset_share_5s | 40.58% |
| positive_asset_share_21s | 73.91% |
| active_return_dispersion_5s | 1.62% |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_3s | active_return_5s | prior_16s_active_return | volatility_21s | max_drawdown_21s | volume_zscore_5v60 | corr_spy_63s | beta_spy_63s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | -0.47% | -3.24% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.03% | -0.42% | -3.00% | 0.17% | 0.00% | -0.819 | -0.141 | -0.002 | 0.00% |
| SP500 | SPY | diversified_us_equity | 0.45% | 0.00% | 0.00% | 10.37% | -1.96% | -1.327 | 1.000 | 1.000 | -1.10% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | 0.32% | -0.18% | 0.03% | 10.85% | -2.01% | -0.739 | 0.993 | 0.986 | -1.29% |
| NASDAQ100 | QQQ | technology_and_growth | 0.80% | -0.05% | 1.13% | 17.97% | -3.52% | -0.964 | 0.921 | 1.724 | -3.88% |
| LARGE_GROWTH | IWF | technology_and_growth | 0.76% | -0.18% | 0.98% | 17.44% | -3.68% | -0.598 | 0.902 | 1.402 | -4.59% |
| LARGE_VALUE | IWD | diversified_us_equity | 0.02% | -0.07% | -0.62% | 7.89% | -1.00% | -0.333 | 0.687 | 0.560 | -0.17% |
| MID_CAP | IJH | diversified_us_equity | -0.50% | -1.79% | -1.36% | 13.00% | -3.70% | 0.036 | 0.783 | 0.786 | -3.70% |
| SMALL_CAP | IWM | diversified_us_equity | -1.16% | -1.88% | -0.72% | 14.38% | -3.06% | -1.303 | 0.784 | 0.957 | -3.06% |
| SMALL_VALUE | IWN | diversified_us_equity | -0.67% | -1.22% | -1.88% | 10.40% | -1.89% | -0.801 | 0.658 | 0.635 | -1.89% |
| DIVIDEND | SCHD | diversified_us_equity | -0.60% | -1.07% | 1.85% | 9.59% | -1.08% | 0.549 | 0.095 | 0.083 | -0.88% |
| LOW_VOL | SPLV | diversified_us_equity | -0.74% | -0.59% | -4.64% | 7.64% | -1.53% | -0.926 | -0.298 | -0.280 | -3.52% |
| MOMENTUM | MTUM | diversified_us_equity | -0.89% | -2.26% | -1.10% | 23.37% | -6.94% | -0.966 | 0.697 | 1.945 | -13.18% |
| TECHNOLOGY | XLK | technology_and_growth | 2.17% | 0.82% | 1.07% | 26.63% | -5.62% | -0.944 | 0.831 | 2.134 | -6.20% |
| COMMUNICATIONS | XLC | technology_and_growth | -0.17% | 0.95% | 1.28% | 18.06% | -2.19% | -1.147 | 0.382 | 0.556 | -5.36% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | -0.63% | -1.16% | 1.77% | 19.38% | -3.32% | -1.432 | 0.656 | 1.042 | -5.49% |
| CONSUMER_STAPLES | XLP | consumer_defensive | -1.24% | -1.10% | -2.63% | 14.25% | -2.71% | -1.067 | -0.292 | -0.370 | -3.87% |
| HEALTHCARE | XLV | healthcare_and_biotech | -2.36% | -2.46% | 3.55% | 18.56% | -2.57% | -1.543 | -0.142 | -0.204 | -2.57% |
| FINANCIALS | XLF | financials | -0.36% | 0.60% | -2.40% | 9.77% | -2.25% | -1.043 | 0.275 | 0.266 | -0.36% |
| INDUSTRIALS | XLI | industrials_and_defense | -0.71% | -2.20% | -2.20% | 14.38% | -5.02% | -0.182 | 0.640 | 0.869 | -5.02% |
| ENERGY | XLE | energy | 1.00% | -1.98% | 4.70% | 23.16% | -3.76% | -0.772 | -0.316 | -0.519 | -1.68% |
| MATERIALS | XLB | materials_and_mining | -0.75% | -1.15% | 0.44% | 17.76% | -2.74% | -0.547 | 0.411 | 0.580 | -0.91% |
| UTILITIES | XLU | rate_sensitive_defensive | -1.34% | -0.57% | -7.47% | 13.18% | -4.32% | -0.849 | -0.120 | -0.141 | -9.27% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | -1.94% | -1.81% | -3.73% | 11.11% | -2.69% | -0.973 | -0.173 | -0.200 | -3.33% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | -0.71% | -0.44% | -3.32% | 5.03% | -0.71% | 0.083 | 0.432 | 0.153 | -3.37% |
| LONG_TREASURY | TLT | rates_and_duration | -0.71% | 0.54% | -3.75% | 10.84% | -1.99% | -0.005 | 0.313 | 0.222 | -6.65% |
| TIPS | TIP | rates_and_duration | -0.65% | -0.65% | -3.08% | 3.61% | -0.65% | -0.597 | 0.382 | 0.100 | -1.22% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | -0.48% | -0.07% | -3.27% | 5.93% | -0.99% | -0.594 | 0.511 | 0.199 | -2.59% |
| HIGH_YIELD_CREDIT | HYG | credit | -0.23% | -0.31% | -2.58% | 2.55% | -0.33% | -0.311 | 0.806 | 0.180 | -0.23% |
| AGGREGATE_BONDS | AGG | rates_and_duration | -0.53% | -0.33% | -3.17% | 4.38% | -0.53% | -0.718 | 0.477 | 0.140 | -1.91% |
| DEVELOPED_EX_US | VEA | international_equity | -0.99% | -0.96% | 0.04% | 12.01% | -1.76% | -0.655 | 0.805 | 1.107 | -0.99% |
| EMERGING_MARKETS | VWO | international_equity | 0.25% | 0.09% | 0.64% | 10.91% | -1.37% | -1.258 | 0.856 | 1.183 | -0.73% |
| EUROPE | VGK | international_equity | -1.30% | -1.27% | -1.34% | 7.76% | -1.30% | -0.761 | 0.730 | 0.758 | -1.30% |
| JAPAN | EWJ | international_equity | 0.25% | 0.25% | -1.21% | 16.86% | -4.27% | -0.633 | 0.750 | 1.297 | -2.64% |
| CHINA | MCHI | international_equity | 0.20% | -1.25% | -2.95% | 13.31% | -4.41% | -1.045 | 0.410 | 0.557 | -15.99% |
| INDIA | INDA | international_equity | -1.33% | -0.64% | -3.36% | 9.55% | -2.34% | -0.510 | 0.562 | 0.555 | -10.36% |
| GOLD | IAU | precious_metals | -4.49% | -3.90% | 9.04% | 27.98% | -4.49% | -0.164 | 0.469 | 0.918 | -17.48% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | 1.21% | -1.87% | 3.33% | 20.20% | -3.76% | -0.288 | -0.163 | -0.259 | -2.75% |
| SEMICONDUCTORS | SMH | technology_and_growth | -0.49% | -1.78% | 0.75% | 35.06% | -7.96% | -0.907 | 0.749 | 2.940 | -17.31% |
| SOFTWARE | IGV | technology_and_growth | 7.51% | 5.46% | 7.54% | 39.65% | -4.17% | -0.525 | 0.482 | 1.270 | -7.02% |
| BROAD_AI_TECH | AIQ | technology_and_growth | 1.81% | 0.77% | 4.84% | 24.88% | -3.59% | -0.469 | 0.829 | 2.353 | -8.44% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | -0.34% | -3.07% | 6.94% | 32.33% | -6.62% | -1.136 | 0.862 | 2.366 | -14.95% |
| CYBERSECURITY | CIBR | technology_and_growth | 6.60% | 3.44% | 2.13% | 40.11% | -9.53% | -0.165 | 0.565 | 1.393 | -3.56% |
| SOLAR | TAN | clean_energy | -0.41% | -1.83% | -4.28% | 33.81% | -9.46% | -0.776 | 0.778 | 2.426 | -34.19% |
| METALS_MINING | XME | materials_and_mining | -1.82% | -0.98% | 13.92% | 41.11% | -3.78% | -0.325 | 0.648 | 1.966 | -10.55% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | -0.49% | -0.92% | -0.32% | 9.76% | -1.34% | -1.181 | 0.685 | 0.551 | -0.93% |
| BIOTECH | XBI | healthcare_and_biotech | -3.97% | -2.50% | 6.18% | 35.20% | -4.23% | -0.270 | 0.304 | 0.726 | -4.23% |
| REGIONAL_BANKS | KRE | financials | -0.04% | -1.22% | -4.61% | 13.19% | -4.66% | -0.989 | 0.151 | 0.207 | -4.66% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | -0.63% | -2.38% | -3.57% | 22.00% | -8.06% | -0.281 | 0.417 | 0.762 | -8.06% |
| CANADA | EWC | international_equity | -1.45% | -1.48% | 1.06% | 9.92% | -1.45% | -0.550 | 0.587 | 0.506 | -1.45% |
| UNITED_KINGDOM | EWU | international_equity | -1.70% | -1.27% | -2.71% | 7.65% | -1.70% | -0.665 | 0.393 | 0.370 | -1.70% |
| AUSTRALIA | EWA | international_equity | -1.41% | -0.94% | -2.17% | 14.92% | -2.83% | 0.451 | 0.581 | 0.711 | -1.41% |
| SOUTH_KOREA | EWY | international_equity | 0.03% | 0.57% | 7.39% | 51.64% | -8.13% | -1.161 | 0.674 | 3.816 | -17.79% |
| TAIWAN | EWT | international_equity | 2.37% | 2.98% | 7.72% | 25.58% | -4.15% | -0.842 | 0.793 | 2.424 | -3.25% |
| BRAZIL | EWZ | international_equity | -0.92% | 0.92% | -7.26% | 19.88% | -8.05% | 0.641 | 0.395 | 0.623 | -14.00% |
| MEXICO | EWW | international_equity | -1.76% | -1.64% | -2.89% | 14.00% | -3.95% | -0.314 | 0.586 | 0.818 | -4.46% |
| SOUTH_AFRICA | EZA | international_equity | -2.47% | -2.94% | 9.86% | 29.70% | -3.77% | -0.502 | 0.670 | 1.518 | -11.43% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | -0.64% | -0.42% | -3.05% | 5.09% | -0.64% | 0.335 | 0.480 | 0.164 | -1.80% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | -0.34% | -0.59% | -3.37% | 2.87% | -0.89% | -0.193 | 0.531 | 0.112 | -1.92% |
| EMERGING_MARKET_BONDS | EMB | credit | -0.51% | -0.29% | -2.87% | 5.28% | -0.76% | -0.156 | 0.718 | 0.283 | -1.15% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | -0.65% | -0.58% | -3.47% | 3.89% | -0.83% | -0.397 | 0.471 | 0.124 | -1.90% |
| SILVER | SLV | precious_metals | -3.69% | -4.78% | 13.99% | 38.69% | -4.38% | 0.162 | 0.554 | 1.808 | -43.16% |
| COPPER | CPER | non_energy_commodities | -2.67% | -1.27% | -1.59% | 18.05% | -4.09% | -0.345 | 0.624 | 1.153 | -2.89% |
| AGRICULTURE | DBA | non_energy_commodities | 3.22% | 2.60% | -0.18% | 11.17% | -1.30% | 1.474 | 0.151 | 0.144 | 0.00% |
| OIL | USO | energy | 2.81% | -4.14% | 2.38% | 46.18% | -11.06% | -1.032 | -0.311 | -1.190 | -15.21% |
| US_DOLLAR | UUP | currencies | 0.86% | 0.53% | -4.09% | 4.90% | -1.13% | -1.223 | -0.383 | -0.147 | -1.47% |
| EURO | FXE | currencies | -0.76% | -1.23% | -1.91% | 4.52% | -0.76% | -0.519 | 0.393 | 0.144 | -3.27% |
| YEN | FXY | currencies | -0.66% | -1.25% | -3.03% | 8.51% | -2.14% | 0.399 | 0.257 | 0.149 | -8.87% |
| BITCOIN_ETF | IBIT | crypto_assets | -1.83% | 0.03% | 15.78% | 41.07% | -3.18% | 0.866 | 0.350 | 1.068 | -38.42% |
| ETHEREUM_ETF | ETHA | crypto_assets | -1.24% | 0.24% | 22.47% | 54.24% | -3.03% | 1.172 | 0.427 | 1.848 | -48.67% |
