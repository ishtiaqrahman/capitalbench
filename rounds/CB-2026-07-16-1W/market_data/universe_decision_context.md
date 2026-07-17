# Full-Universe Horizon-Specific Decision Context

Profile: weekly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: yahoo_chart_adjusted_close_and_reported_volume
- As-of date requested: 2026-07-16
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | -0.13% |
| spy_return_21s | -0.29% |
| rsp_return_5s | 0.73% |
| rsp_return_21s | 1.42% |
| hyg_return_5s | 0.06% |
| hyg_return_21s | 0.16% |
| tlt_return_5s | -0.33% |
| tlt_return_21s | -1.40% |
| uup_return_5s | -0.07% |
| uup_return_21s | 1.32% |
| uso_return_5s | 9.44% |
| uso_return_21s | -1.58% |
| iau_return_5s | -3.50% |
| iau_return_21s | -7.95% |
| rsp_minus_spy_5s | 0.86% |
| rsp_minus_spy_21s | 1.70% |
| positive_asset_share_5s | 44.93% |
| positive_asset_share_21s | 42.03% |
| active_return_dispersion_5s | 3.28% |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_3s | active_return_5s | prior_16s_active_return | volatility_21s | max_drawdown_21s | volume_zscore_5v60 | corr_spy_63s | beta_spy_63s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | 0.13% | 0.16% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.03% | 0.21% | 0.40% | 0.25% | -0.01% | -0.563 | -0.169 | -0.003 | 0.00% |
| SP500 | SPY | diversified_us_equity | 0.21% | 0.00% | 0.00% | 12.42% | -3.17% | -0.844 | 1.000 | 1.000 | -0.91% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | 0.22% | -0.10% | 0.15% | 11.70% | -2.49% | -0.540 | 0.992 | 0.992 | -0.72% |
| NASDAQ100 | QQQ | technology_and_growth | -0.81% | -2.27% | -2.52% | 26.06% | -5.01% | -0.902 | 0.916 | 1.701 | -5.29% |
| LARGE_GROWTH | IWF | technology_and_growth | -0.32% | -1.57% | -0.70% | 21.92% | -5.03% | -0.438 | 0.887 | 1.275 | -5.80% |
| LARGE_VALUE | IWD | diversified_us_equity | 0.74% | 1.38% | 1.22% | 11.17% | -1.39% | -0.517 | 0.714 | 0.651 | 0.00% |
| MID_CAP | IJH | diversified_us_equity | 1.00% | 0.51% | -0.45% | 12.36% | -3.09% | -0.634 | 0.771 | 0.883 | -1.45% |
| SMALL_CAP | IWM | diversified_us_equity | 0.72% | -0.42% | 1.04% | 12.93% | -2.32% | -1.194 | 0.789 | 1.131 | -1.62% |
| SMALL_VALUE | IWN | diversified_us_equity | 2.00% | 2.26% | 1.17% | 11.05% | -1.83% | -1.042 | 0.673 | 0.813 | 0.00% |
| DIVIDEND | SCHD | diversified_us_equity | 1.47% | 2.55% | -0.19% | 14.25% | -2.36% | -0.224 | 0.098 | 0.090 | 0.00% |
| LOW_VOL | SPLV | diversified_us_equity | 0.69% | 2.04% | 2.10% | 15.78% | -1.89% | -0.401 | -0.283 | -0.292 | 0.00% |
| MOMENTUM | MTUM | diversified_us_equity | -3.57% | -5.41% | -3.57% | 42.70% | -12.11% | 0.957 | 0.770 | 2.124 | -12.11% |
| TECHNOLOGY | XLK | technology_and_growth | -2.07% | -4.09% | -3.09% | 34.12% | -7.61% | -1.226 | 0.841 | 2.144 | -10.33% |
| COMMUNICATIONS | XLC | technology_and_growth | 0.95% | 2.07% | -1.08% | 19.82% | -5.76% | -0.059 | 0.439 | 0.516 | -5.64% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | 1.12% | 0.55% | -1.10% | 19.96% | -4.21% | -0.599 | 0.740 | 1.073 | -5.39% |
| CONSUMER_STAPLES | XLP | consumer_defensive | 1.44% | 3.27% | -1.84% | 20.47% | -3.32% | -1.249 | -0.294 | -0.373 | -3.46% |
| HEALTHCARE | XLV | healthcare_and_biotech | 0.24% | -0.10% | 6.69% | 22.28% | -3.74% | -0.094 | -0.086 | -0.121 | -1.61% |
| FINANCIALS | XLF | financials | 1.21% | 2.31% | 4.22% | 14.34% | -2.08% | 0.022 | 0.165 | 0.167 | 0.00% |
| INDUSTRIALS | XLI | industrials_and_defense | -0.12% | -0.40% | 1.77% | 17.30% | -2.96% | -1.009 | 0.655 | 0.993 | -2.92% |
| ENERGY | XLE | energy | 0.49% | 4.14% | -0.45% | 21.23% | -4.25% | -0.531 | -0.396 | -0.760 | -8.20% |
| MATERIALS | XLB | materials_and_mining | 0.61% | 1.39% | -3.75% | 17.35% | -4.50% | -0.744 | 0.537 | 0.791 | -4.31% |
| UTILITIES | XLU | rate_sensitive_defensive | -0.55% | 0.89% | 1.67% | 15.53% | -3.10% | -1.065 | -0.064 | -0.087 | -3.46% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | 1.70% | 2.91% | -0.67% | 18.80% | -2.75% | -0.686 | -0.061 | -0.078 | 0.00% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | 0.46% | 0.14% | -0.12% | 5.13% | -1.54% | -0.368 | 0.578 | 0.227 | -2.80% |
| LONG_TREASURY | TLT | rates_and_duration | 0.29% | -0.20% | -0.91% | 8.97% | -3.62% | -0.766 | 0.448 | 0.309 | -5.54% |
| TIPS | TIP | rates_and_duration | 0.06% | -0.01% | -0.38% | 4.15% | -0.85% | -0.627 | 0.603 | 0.165 | -1.00% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | 0.50% | -0.06% | -0.67% | 4.89% | -2.16% | 0.579 | 0.595 | 0.249 | -1.96% |
| HIGH_YIELD_CREDIT | HYG | credit | 0.35% | 0.19% | 0.26% | 2.69% | -0.44% | -0.856 | 0.779 | 0.222 | -0.09% |
| AGGREGATE_BONDS | AGG | rates_and_duration | 0.43% | 0.08% | -0.19% | 4.00% | -1.34% | -0.001 | 0.611 | 0.196 | -1.61% |
| DEVELOPED_EX_US | VEA | international_equity | 0.39% | -0.86% | -1.62% | 18.20% | -3.63% | -0.285 | 0.845 | 1.371 | -3.26% |
| EMERGING_MARKETS | VWO | international_equity | 0.09% | -0.96% | -1.95% | 19.60% | -4.34% | 0.407 | 0.872 | 1.376 | -3.92% |
| EUROPE | VGK | international_equity | 1.06% | 0.56% | -0.13% | 13.29% | -2.35% | -1.542 | 0.732 | 1.039 | -1.31% |
| JAPAN | EWJ | international_equity | -0.87% | -1.59% | -0.42% | 24.10% | -5.22% | -0.984 | 0.786 | 1.331 | -5.22% |
| CHINA | MCHI | international_equity | 3.06% | 1.92% | -3.01% | 20.00% | -8.10% | -0.367 | 0.532 | 0.849 | -17.65% |
| INDIA | INDA | international_equity | -0.20% | -0.54% | -0.33% | 13.04% | -2.54% | -0.931 | 0.619 | 0.780 | -11.94% |
| GOLD | IAU | precious_metals | -0.60% | -3.36% | -4.46% | 22.60% | -8.22% | -0.735 | 0.732 | 1.356 | -26.36% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | 0.36% | 3.42% | -2.63% | 21.69% | -6.57% | -0.679 | -0.148 | -0.247 | -10.31% |
| SEMICONDUCTORS | SMH | technology_and_growth | -2.85% | -6.25% | -5.93% | 58.41% | -14.95% | -0.390 | 0.784 | 3.154 | -14.95% |
| SOFTWARE | IGV | technology_and_growth | 1.08% | -0.06% | 1.45% | 26.90% | -8.55% | -1.411 | 0.341 | 0.909 | -20.44% |
| BROAD_AI_TECH | AIQ | technology_and_growth | -3.25% | -6.95% | -3.93% | 39.47% | -11.60% | -0.443 | 0.829 | 2.501 | -15.44% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | -2.12% | -5.13% | -7.26% | 32.45% | -12.29% | -1.111 | 0.850 | 2.495 | -17.86% |
| CYBERSECURITY | CIBR | technology_and_growth | 0.05% | -2.38% | 9.51% | 27.77% | -3.12% | -0.484 | 0.429 | 1.082 | -3.00% |
| SOLAR | TAN | clean_energy | 2.00% | -1.27% | -12.20% | 41.55% | -15.28% | -1.394 | 0.739 | 2.595 | -26.71% |
| METALS_MINING | XME | materials_and_mining | -3.04% | -3.98% | -14.20% | 28.30% | -17.88% | -0.866 | 0.707 | 2.203 | -25.43% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | 0.39% | 0.86% | 0.84% | 10.88% | -1.83% | -0.928 | 0.715 | 0.601 | 0.00% |
| BIOTECH | XBI | healthcare_and_biotech | -2.15% | -7.34% | 20.71% | 29.48% | -7.48% | 0.221 | 0.391 | 0.913 | -7.48% |
| REGIONAL_BANKS | KRE | financials | 3.73% | 4.51% | 4.11% | 19.98% | -3.73% | -0.322 | 0.158 | 0.253 | 0.00% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | -1.77% | -3.51% | 1.09% | 20.53% | -7.93% | -1.096 | 0.489 | 0.988 | -7.93% |
| CANADA | EWC | international_equity | 1.12% | 1.86% | -0.78% | 9.24% | -3.08% | -0.635 | 0.621 | 0.632 | -0.17% |
| UNITED_KINGDOM | EWU | international_equity | 1.32% | 1.34% | 0.59% | 14.09% | -2.28% | -0.439 | 0.506 | 0.669 | -2.13% |
| AUSTRALIA | EWA | international_equity | 0.99% | 1.66% | -1.24% | 13.74% | -4.42% | -0.319 | 0.625 | 0.897 | -4.06% |
| SOUTH_KOREA | EWY | international_equity | -2.77% | -11.45% | -12.47% | 77.64% | -25.47% | 1.050 | 0.763 | 4.580 | -25.47% |
| TAIWAN | EWT | international_equity | -1.69% | -4.52% | -1.08% | 43.18% | -10.19% | 0.499 | 0.790 | 2.500 | -10.19% |
| BRAZIL | EWZ | international_equity | -0.17% | 1.19% | 1.08% | 19.97% | -2.63% | -0.073 | 0.434 | 0.768 | -14.53% |
| MEXICO | EWW | international_equity | 1.44% | 1.45% | -4.37% | 17.84% | -5.37% | -0.574 | 0.631 | 1.002 | -6.04% |
| SOUTH_AFRICA | EZA | international_equity | 0.29% | -0.41% | -6.44% | 22.54% | -8.61% | -0.541 | 0.781 | 2.029 | -21.18% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | 0.54% | 0.07% | -0.23% | 4.68% | -1.45% | -0.150 | 0.610 | 0.229 | -1.54% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | -0.26% | -0.17% | 0.21% | 2.47% | -0.88% | -0.454 | 0.619 | 0.131 | -0.88% |
| EMERGING_MARKET_BONDS | EMB | credit | 0.22% | -0.25% | -0.21% | 4.53% | -1.08% | -0.498 | 0.752 | 0.348 | -0.86% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | 0.15% | 0.01% | -0.13% | 3.43% | -1.20% | -0.569 | 0.576 | 0.194 | -1.40% |
| SILVER | SLV | precious_metals | -3.39% | -6.79% | -14.54% | 43.85% | -20.61% | -0.768 | 0.688 | 2.709 | -52.28% |
| COPPER | CPER | non_energy_commodities | 0.32% | 0.95% | -4.64% | 24.60% | -8.42% | -0.984 | 0.722 | 1.616 | -6.26% |
| AGRICULTURE | DBA | non_energy_commodities | -0.47% | -0.30% | 5.20% | 15.22% | -1.52% | -0.509 | 0.000 | 0.001 | -3.97% |
| OIL | USO | energy | 1.28% | 9.57% | -9.91% | 49.69% | -14.80% | -0.267 | -0.333 | -1.387 | -22.01% |
| US_DOLLAR | UUP | currencies | -0.56% | 0.06% | 1.55% | 5.52% | -0.98% | 0.522 | -0.554 | -0.212 | -0.67% |
| EURO | FXE | currencies | 0.53% | 0.27% | -1.15% | 5.55% | -2.19% | -0.588 | 0.568 | 0.208 | -4.62% |
| YEN | FXY | currencies | -0.02% | 0.08% | -1.17% | 5.25% | -1.42% | -0.237 | 0.249 | 0.126 | -10.18% |
| BITCOIN_ETF | IBIT | crypto_assets | 3.32% | 1.75% | -4.96% | 37.69% | -11.79% | -0.601 | 0.506 | 1.512 | -48.95% |
| ETHEREUM_ETF | ETHA | crypto_assets | 5.68% | 7.26% | -3.99% | 51.58% | -14.68% | 0.098 | 0.598 | 2.477 | -61.38% |
