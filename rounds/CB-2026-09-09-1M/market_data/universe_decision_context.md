# Full-Universe Horizon-Specific Decision Context

Profile: monthly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: yahoo_chart_adjusted_close_and_reported_volume
- As-of date requested: 2026-09-08
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | -0.14% |
| spy_return_21s | -0.94% |
| rsp_return_5s | -1.21% |
| rsp_return_21s | -1.53% |
| hyg_return_5s | -0.32% |
| hyg_return_21s | -0.07% |
| tlt_return_5s | -0.01% |
| tlt_return_21s | -0.30% |
| uup_return_5s | -0.46% |
| uup_return_21s | -0.29% |
| uso_return_5s | 9.22% |
| uso_return_21s | 23.78% |
| iau_return_5s | -2.10% |
| iau_return_21s | 0.33% |
| rsp_minus_spy_5s | -1.07% |
| rsp_minus_spy_21s | -0.58% |
| positive_asset_share_5s | 46.38% |
| positive_asset_share_21s | 37.68% |
| active_return_dispersion_5s |  |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_5s | active_return_21s | prior_105s_active_return | volatility_63s | max_drawdown_63s | volume_zscore_20v120 | corr_spy_252s | beta_spy_252s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | 0.94% | -14.61% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.09% | 1.23% | -13.10% | 0.20% | -0.01% | -0.591 | -0.102 | -0.002 | 0.00% |
| SP500 | SPY | diversified_us_equity | -0.14% | 0.00% | 0.00% | 12.89% | -3.38% | -1.098 | 1.000 | 1.000 | -1.53% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | -0.15% | -0.15% | 0.29% | 12.71% | -3.29% | -0.667 | 0.995 | 1.012 | -1.74% |
| NASDAQ100 | QQQ | technology_and_growth | 0.22% | 0.30% | 4.64% | 23.74% | -10.96% | -1.089 | 0.928 | 1.420 | -3.62% |
| LARGE_GROWTH | IWF | technology_and_growth | 0.25% | -0.32% | -4.26% | 20.38% | -8.29% | -0.760 | 0.933 | 1.288 | -4.38% |
| LARGE_VALUE | IWD | diversified_us_equity | -0.54% | 0.16% | 3.97% | 10.75% | -1.48% | -0.605 | 0.799 | 0.700 | -1.48% |
| MID_CAP | IJH | diversified_us_equity | 0.01% | -2.18% | -1.15% | 13.41% | -5.17% | -0.731 | 0.808 | 0.974 | -4.21% |
| SMALL_CAP | IWM | diversified_us_equity | 0.25% | -1.34% | 4.79% | 14.74% | -4.76% | -1.127 | 0.819 | 1.200 | -3.42% |
| SMALL_VALUE | IWN | diversified_us_equity | 0.43% | -0.28% | 4.00% | 11.82% | -3.29% | -0.974 | 0.735 | 0.940 | -2.05% |
| DIVIDEND | SCHD | diversified_us_equity | -1.38% | 2.45% | -3.52% | 11.85% | -2.93% | 0.141 | 0.285 | 0.247 | -2.27% |
| LOW_VOL | SPLV | diversified_us_equity | -0.19% | -1.05% | -13.21% | 12.06% | -4.22% | -0.712 | 0.018 | 0.015 | -4.21% |
| MOMENTUM | MTUM | diversified_us_equity | 2.77% | 0.74% | 10.75% | 35.63% | -17.99% | -0.386 | 0.760 | 1.560 | -10.58% |
| TECHNOLOGY | XLK | technology_and_growth | 0.73% | 0.89% | 20.21% | 31.82% | -13.31% | -1.368 | 0.850 | 1.743 | -5.10% |
| COMMUNICATIONS | XLC | technology_and_growth | 0.05% | 1.19% | -19.43% | 19.79% | -7.06% | -1.037 | 0.568 | 0.676 | -6.59% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | -2.23% | -3.95% | -9.59% | 21.50% | -8.09% | -1.210 | 0.765 | 1.162 | -8.09% |
| CONSUMER_STAPLES | XLP | consumer_defensive | -1.13% | -0.35% | -14.35% | 17.07% | -3.92% | -0.880 | -0.063 | -0.071 | -5.48% |
| HEALTHCARE | XLV | healthcare_and_biotech | -2.00% | 1.82% | -6.29% | 19.51% | -4.87% | -1.008 | 0.227 | 0.289 | -4.87% |
| FINANCIALS | XLF | financials | -0.71% | 0.42% | 0.83% | 13.07% | -2.25% | -0.843 | 0.540 | 0.615 | -2.15% |
| INDUSTRIALS | XLI | industrials_and_defense | -0.41% | -4.87% | -5.71% | 18.67% | -7.39% | -0.795 | 0.710 | 0.950 | -6.48% |
| ENERGY | XLE | energy | 1.27% | 13.59% | -11.11% | 22.33% | -8.81% | -0.872 | -0.184 | -0.311 | -0.51% |
| MATERIALS | XLB | materials_and_mining | -1.42% | -0.80% | -8.00% | 19.29% | -4.75% | -0.480 | 0.530 | 0.742 | -3.22% |
| UTILITIES | XLU | rate_sensitive_defensive | 2.89% | 0.58% | -20.28% | 14.29% | -8.77% | -0.384 | 0.113 | 0.134 | -7.75% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | -0.48% | -1.46% | -8.33% | 15.01% | -4.96% | -0.449 | 0.243 | 0.266 | -4.59% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | -0.27% | 0.22% | -16.69% | 4.75% | -2.11% | -0.400 | 0.284 | 0.101 | -3.74% |
| LONG_TREASURY | TLT | rates_and_duration | -0.01% | 0.65% | -20.05% | 9.61% | -6.26% | -0.213 | 0.234 | 0.168 | -7.07% |
| TIPS | TIP | rates_and_duration | 0.22% | 0.92% | -15.39% | 3.47% | -1.33% | -0.457 | 0.257 | 0.066 | -1.12% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | -0.27% | 0.36% | -16.56% | 5.28% | -2.92% | -0.602 | 0.475 | 0.193 | -2.98% |
| HIGH_YIELD_CREDIT | HYG | credit | -0.32% | 0.87% | -12.83% | 2.88% | -0.80% | -0.681 | 0.775 | 0.228 | -0.46% |
| AGGREGATE_BONDS | AGG | rates_and_duration | -0.18% | 0.57% | -15.78% | 3.94% | -1.71% | -0.394 | 0.393 | 0.114 | -2.17% |
| DEVELOPED_EX_US | VEA | international_equity | 0.73% | 1.71% | -3.25% | 17.36% | -4.75% | -0.679 | 0.800 | 1.083 | -0.46% |
| EMERGING_MARKETS | VWO | international_equity | 1.17% | 2.20% | -4.79% | 16.87% | -7.05% | -0.758 | 0.814 | 1.113 | -0.34% |
| EUROPE | VGK | international_equity | -0.51% | -0.58% | -3.20% | 13.45% | -2.65% | -0.923 | 0.746 | 0.913 | -2.15% |
| JAPAN | EWJ | international_equity | 2.17% | 2.04% | -0.85% | 22.70% | -7.86% | -0.883 | 0.721 | 1.184 | -0.52% |
| CHINA | MCHI | international_equity | -1.41% | -3.69% | -15.87% | 16.74% | -8.10% | -0.755 | 0.560 | 0.871 | -17.94% |
| INDIA | INDA | international_equity | -1.23% | -1.60% | -13.83% | 12.89% | -4.59% | -1.028 | 0.556 | 0.659 | -11.21% |
| GOLD | IAU | precious_metals | -2.10% | 1.27% | -30.21% | 26.85% | -8.22% | -0.429 | 0.331 | 0.748 | -19.32% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | 3.49% | 12.83% | -8.06% | 21.73% | -10.44% | -0.515 | -0.176 | -0.279 | 0.00% |
| SEMICONDUCTORS | SMH | technology_and_growth | 3.07% | -0.60% | 33.14% | 49.16% | -24.62% | -0.788 | 0.772 | 2.371 | -14.23% |
| SOFTWARE | IGV | technology_and_growth | -6.66% | 0.91% | 2.49% | 33.72% | -11.37% | -1.000 | 0.509 | 1.250 | -12.83% |
| BROAD_AI_TECH | AIQ | technology_and_growth | 0.03% | 2.48% | 12.52% | 34.22% | -16.56% | -0.853 | 0.848 | 1.925 | -8.30% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | 1.27% | -2.03% | -9.53% | 34.70% | -18.66% | -1.301 | 0.803 | 2.201 | -13.75% |
| CYBERSECURITY | CIBR | technology_and_growth | -6.13% | -2.98% | 33.40% | 31.85% | -9.53% | 0.008 | 0.527 | 1.163 | -8.01% |
| SOLAR | TAN | clean_energy | 3.28% | -5.92% | -17.11% | 38.84% | -26.30% | -0.753 | 0.632 | 1.881 | -33.55% |
| METALS_MINING | XME | materials_and_mining | 1.54% | 4.58% | -11.18% | 37.68% | -19.05% | -0.533 | 0.597 | 1.780 | -9.63% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | -1.21% | -0.58% | -2.95% | 11.06% | -2.71% | -1.114 | 0.772 | 0.701 | -2.71% |
| BIOTECH | XBI | healthcare_and_biotech | -0.35% | 3.84% | 9.31% | 29.66% | -10.51% | -0.400 | 0.481 | 1.047 | -4.49% |
| REGIONAL_BANKS | KRE | financials | 1.02% | -1.55% | 4.46% | 17.42% | -6.81% | -0.703 | 0.415 | 0.718 | -4.65% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | -2.11% | -9.91% | -10.85% | 24.17% | -11.79% | -0.450 | 0.570 | 1.033 | -11.72% |
| CANADA | EWC | international_equity | 0.10% | 1.25% | -5.82% | 11.34% | -3.26% | -0.263 | 0.676 | 0.762 | -1.84% |
| UNITED_KINGDOM | EWU | international_equity | -0.04% | 0.35% | -8.03% | 12.48% | -2.43% | -0.754 | 0.601 | 0.699 | -2.11% |
| AUSTRALIA | EWA | international_equity | -0.07% | -0.40% | -7.76% | 15.45% | -4.42% | -0.469 | 0.673 | 0.931 | -1.41% |
| SOUTH_KOREA | EWY | international_equity | 5.00% | 15.29% | 9.44% | 70.74% | -34.21% | -0.765 | 0.631 | 2.760 | -13.36% |
| TAIWAN | EWT | international_equity | 3.25% | 9.14% | 31.08% | 38.44% | -19.83% | -1.090 | 0.751 | 1.830 | -0.57% |
| BRAZIL | EWZ | international_equity | 7.16% | 10.20% | -18.45% | 22.08% | -8.05% | -0.125 | 0.484 | 0.951 | -6.60% |
| MEXICO | EWW | international_equity | -0.07% | -0.15% | -8.15% | 17.97% | -5.37% | -0.561 | 0.550 | 0.942 | -4.22% |
| SOUTH_AFRICA | EZA | international_equity | 1.13% | 3.31% | -15.75% | 28.93% | -11.18% | -0.592 | 0.632 | 1.628 | -10.71% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | -0.25% | 0.51% | -15.60% | 4.62% | -1.85% | 0.118 | 0.389 | 0.133 | -2.12% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | -0.75% | -0.60% | -14.90% | 2.98% | -2.79% | 1.035 | 0.382 | 0.088 | -2.77% |
| EMERGING_MARKET_BONDS | EMB | credit | 0.00% | 0.45% | -13.16% | 5.18% | -1.96% | -0.573 | 0.687 | 0.303 | -1.27% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | -0.08% | 0.03% | -14.59% | 3.60% | -1.90% | -0.377 | 0.465 | 0.130 | -2.08% |
| SILVER | SLV | precious_metals | -1.26% | 4.20% | -41.14% | 42.47% | -20.61% | -0.688 | 0.366 | 1.780 | -43.78% |
| COPPER | CPER | non_energy_commodities | 1.42% | 2.62% | -3.47% | 22.96% | -8.42% | -0.471 | 0.559 | 1.240 | -0.69% |
| AGRICULTURE | DBA | non_energy_commodities | -0.65% | 6.41% | -10.58% | 12.98% | -2.87% | 0.143 | 0.060 | 0.052 | -1.22% |
| OIL | USO | energy | 9.22% | 24.72% | -1.53% | 52.23% | -23.59% | -0.628 | -0.341 | -1.291 | -4.53% |
| US_DOLLAR | UUP | currencies | -0.46% | 0.66% | -12.39% | 5.27% | -2.52% | -1.126 | -0.296 | -0.130 | -2.13% |
| EURO | FXE | currencies | 0.06% | 1.54% | -14.69% | 4.74% | -2.19% | -0.697 | 0.276 | 0.119 | -2.97% |
| YEN | FXY | currencies | 3.78% | 3.21% | -14.52% | 9.57% | -2.49% | 0.271 | 0.174 | 0.115 | -5.19% |
| BITCOIN_ETF | IBIT | crypto_assets | -0.63% | 21.57% | -20.57% | 38.25% | -11.79% | 0.703 | 0.489 | 1.727 | -37.73% |
| ETHEREUM_ETF | ETHA | crypto_assets | 0.00% | 30.32% | -20.47% | 51.67% | -14.68% | 1.071 | 0.504 | 2.548 | -47.69% |
