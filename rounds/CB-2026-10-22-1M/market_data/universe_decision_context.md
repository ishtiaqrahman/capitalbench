# Full-Universe Horizon-Specific Decision Context

Profile: monthly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: tiingo_eod_adjusted_price_and_volume; yahoo_chart_adjusted_close_and_reported_volume
- As-of date requested: 2026-10-22
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | -1.01% |
| spy_return_21s | -0.50% |
| rsp_return_5s | 1.50% |
| rsp_return_21s | 3.27% |
| hyg_return_5s | -0.04% |
| hyg_return_21s | -0.84% |
| tlt_return_5s | 2.21% |
| tlt_return_21s | 2.00% |
| uup_return_5s | -0.34% |
| uup_return_21s | 0.87% |
| uso_return_5s | 3.31% |
| uso_return_21s | 9.19% |
| iau_return_5s | -3.58% |
| iau_return_21s | -6.04% |
| rsp_minus_spy_5s | 2.51% |
| rsp_minus_spy_21s | 3.77% |
| positive_asset_share_5s | 50.72% |
| positive_asset_share_21s | 46.38% |
| active_return_dispersion_5s |  |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_5s | active_return_21s | prior_105s_active_return | volatility_63s | max_drawdown_63s | volume_zscore_20v120 | corr_spy_252s | beta_spy_252s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | 0.50% | -8.92% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.07% | 0.80% | -7.43% | 0.20% | -0.01% | 0.455 | -0.041 | -0.001 | 0.00% |
| SP500 | SPY | diversified_us_equity | -1.01% | 0.00% | 0.00% | 11.03% | -3.06% | -0.649 | 1.000 | 1.000 | -1.94% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | -0.93% | -0.13% | -0.49% | 11.24% | -3.39% | -0.230 | 0.995 | 1.011 | -2.20% |
| NASDAQ100 | QQQ | technology_and_growth | -3.23% | -4.46% | 5.10% | 19.01% | -7.27% | -0.293 | 0.925 | 1.455 | -7.27% |
| LARGE_GROWTH | IWF | technology_and_growth | -3.34% | -3.73% | -2.71% | 18.13% | -7.04% | -0.047 | 0.931 | 1.319 | -7.04% |
| LARGE_VALUE | IWD | diversified_us_equity | 1.14% | 3.54% | 2.35% | 8.57% | -4.06% | -0.150 | 0.785 | 0.678 | 0.00% |
| MID_CAP | IJH | diversified_us_equity | -0.31% | 0.19% | -7.83% | 12.31% | -8.26% | 0.551 | 0.805 | 0.953 | -7.18% |
| SMALL_CAP | IWM | diversified_us_equity | 0.58% | -1.36% | -6.09% | 14.16% | -11.12% | 0.210 | 0.813 | 1.161 | -9.08% |
| SMALL_VALUE | IWN | diversified_us_equity | 1.31% | 0.49% | -4.85% | 11.57% | -8.30% | 1.020 | 0.716 | 0.878 | -5.83% |
| DIVIDEND | SCHD | diversified_us_equity | 3.81% | 6.87% | -1.31% | 11.52% | -6.87% | 0.385 | 0.222 | 0.198 | 0.00% |
| LOW_VOL | SPLV | diversified_us_equity | 3.54% | 7.47% | -11.92% | 10.38% | -9.22% | -0.435 | -0.003 | -0.003 | -1.74% |
| MOMENTUM | MTUM | diversified_us_equity | -4.30% | -8.45% | 6.32% | 26.01% | -11.06% | -0.281 | 0.771 | 1.640 | -16.24% |
| TECHNOLOGY | XLK | technology_and_growth | -3.62% | -6.15% | 16.71% | 26.24% | -9.73% | -0.349 | 0.851 | 1.783 | -9.73% |
| COMMUNICATIONS | XLC | technology_and_growth | -4.46% | -4.07% | -12.48% | 19.77% | -6.39% | 0.492 | 0.538 | 0.685 | -9.74% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | 1.41% | 4.44% | -14.55% | 16.78% | -9.02% | -0.094 | 0.766 | 1.155 | -7.07% |
| CONSUMER_STAPLES | XLP | consumer_defensive | 3.82% | 9.67% | -8.84% | 16.05% | -7.54% | 0.783 | -0.087 | -0.103 | 0.00% |
| HEALTHCARE | XLV | healthcare_and_biotech | 2.32% | 7.91% | 7.45% | 17.67% | -5.87% | -0.289 | 0.183 | 0.234 | 0.00% |
| FINANCIALS | XLF | financials | 2.50% | 4.37% | -2.90% | 12.77% | -8.49% | 0.304 | 0.508 | 0.577 | -2.92% |
| INDUSTRIALS | XLI | industrials_and_defense | -0.69% | -1.48% | -10.70% | 14.68% | -10.39% | -0.016 | 0.698 | 0.942 | -10.37% |
| ENERGY | XLE | energy | 1.52% | 8.84% | 1.99% | 21.62% | -6.15% | -0.226 | -0.235 | -0.406 | -0.98% |
| MATERIALS | XLB | materials_and_mining | 2.23% | 3.31% | -11.07% | 15.60% | -9.14% | 0.075 | 0.503 | 0.700 | -3.25% |
| UTILITIES | XLU | rate_sensitive_defensive | 2.93% | 8.35% | -21.49% | 15.62% | -14.58% | 3.443 | 0.094 | 0.116 | -8.31% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | 1.26% | 2.13% | -12.12% | 12.85% | -11.09% | 1.927 | 0.234 | 0.264 | -6.82% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | 0.94% | 1.97% | -12.74% | 5.75% | -4.24% | 0.873 | 0.316 | 0.123 | -4.42% |
| LONG_TREASURY | TLT | rates_and_duration | 2.21% | 2.50% | -14.16% | 11.28% | -7.37% | 1.905 | 0.285 | 0.214 | -7.21% |
| TIPS | TIP | rates_and_duration | 0.99% | 1.95% | -11.77% | 4.24% | -3.40% | 0.126 | 0.265 | 0.075 | -1.78% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | 0.75% | 1.31% | -12.18% | 6.43% | -3.98% | 1.064 | 0.467 | 0.206 | -3.67% |
| HIGH_YIELD_CREDIT | HYG | credit | -0.04% | -0.34% | -9.26% | 3.48% | -2.93% | 2.568 | 0.749 | 0.226 | -2.57% |
| AGGREGATE_BONDS | AGG | rates_and_duration | 0.74% | 1.60% | -11.34% | 4.83% | -3.28% | 1.693 | 0.405 | 0.129 | -2.61% |
| DEVELOPED_EX_US | VEA | international_equity | -0.57% | -2.52% | -2.60% | 14.26% | -5.91% | -0.343 | 0.807 | 1.115 | -5.91% |
| EMERGING_MARKETS | VWO | international_equity | -3.30% | -4.94% | -4.81% | 14.43% | -7.30% | -0.006 | 0.819 | 1.125 | -7.30% |
| EUROPE | VGK | international_equity | -0.47% | -0.87% | -5.50% | 12.02% | -8.10% | 0.236 | 0.747 | 0.936 | -6.62% |
| JAPAN | EWJ | international_equity | -0.87% | -2.02% | 3.13% | 18.46% | -4.75% | -0.401 | 0.727 | 1.184 | -4.75% |
| CHINA | MCHI | international_equity | -5.17% | -7.30% | -15.47% | 16.03% | -13.89% | -0.444 | 0.544 | 0.805 | -23.85% |
| INDIA | INDA | international_equity | -1.23% | -0.93% | -11.68% | 13.54% | -9.84% | -0.114 | 0.581 | 0.717 | -14.34% |
| GOLD | IAU | precious_metals | -3.58% | -5.53% | -17.78% | 23.91% | -13.79% | -0.530 | 0.360 | 0.801 | -25.51% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | 0.96% | 2.59% | 1.00% | 20.00% | -5.85% | -0.258 | -0.236 | -0.381 | -0.45% |
| SEMICONDUCTORS | SMH | technology_and_growth | -6.35% | -12.48% | 15.89% | 38.18% | -17.44% | -0.320 | 0.769 | 2.421 | -21.76% |
| SOFTWARE | IGV | technology_and_growth | -0.80% | 1.07% | 20.45% | 33.95% | -8.27% | -1.070 | 0.492 | 1.251 | -7.12% |
| BROAD_AI_TECH | AIQ | technology_and_growth | -3.15% | -5.44% | 14.40% | 25.52% | -7.50% | -0.529 | 0.852 | 1.962 | -11.50% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | -3.45% | -9.95% | -12.03% | 29.57% | -14.39% | -0.526 | 0.815 | 2.223 | -22.34% |
| CYBERSECURITY | CIBR | technology_and_growth | -0.70% | -0.65% | 47.40% | 34.39% | -10.16% | 1.066 | 0.493 | 1.150 | -6.54% |
| SOLAR | TAN | clean_energy | -3.27% | -7.71% | -32.05% | 34.00% | -22.60% | -0.411 | 0.653 | 1.949 | -44.07% |
| METALS_MINING | XME | materials_and_mining | -4.69% | -11.35% | -15.65% | 36.23% | -21.42% | -0.719 | 0.620 | 1.813 | -27.18% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | 1.50% | 3.77% | -3.75% | 10.27% | -6.27% | 0.068 | 0.750 | 0.677 | -1.68% |
| BIOTECH | XBI | healthcare_and_biotech | 1.24% | -1.79% | 6.58% | 30.70% | -14.88% | 0.543 | 0.474 | 1.081 | -10.56% |
| REGIONAL_BANKS | KRE | financials | 3.81% | 3.39% | -7.22% | 15.97% | -11.55% | 0.618 | 0.374 | 0.600 | -6.55% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | -1.18% | -3.91% | -11.11% | 18.74% | -19.50% | 0.276 | 0.547 | 0.987 | -19.15% |
| CANADA | EWC | international_equity | 1.01% | 2.66% | -5.31% | 13.31% | -7.50% | -0.112 | 0.664 | 0.765 | -2.71% |
| UNITED_KINGDOM | EWU | international_equity | 0.17% | 2.09% | -6.86% | 11.08% | -7.09% | -0.409 | 0.586 | 0.698 | -3.14% |
| AUSTRALIA | EWA | international_equity | 0.56% | 2.65% | -10.67% | 16.18% | -8.02% | 0.253 | 0.680 | 0.965 | -4.80% |
| SOUTH_KOREA | EWY | international_equity | -4.58% | -19.21% | 14.36% | 54.79% | -22.61% | -0.416 | 0.648 | 2.946 | -32.00% |
| TAIWAN | EWT | international_equity | -4.72% | -7.06% | 24.62% | 31.46% | -11.87% | -0.464 | 0.752 | 1.886 | -11.87% |
| BRAZIL | EWZ | international_equity | 0.65% | 12.49% | -14.82% | 33.76% | -8.05% | 2.952 | 0.438 | 0.979 | -3.88% |
| MEXICO | EWW | international_equity | 1.45% | 2.59% | -12.93% | 16.95% | -10.38% | -0.159 | 0.566 | 0.976 | -6.37% |
| SOUTH_AFRICA | EZA | international_equity | -1.77% | -3.38% | -10.87% | 26.83% | -14.09% | -0.162 | 0.634 | 1.627 | -20.03% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | 0.87% | 1.85% | -11.98% | 6.06% | -4.25% | 0.682 | 0.398 | 0.153 | -2.94% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | 0.74% | 1.96% | -12.56% | 5.24% | -5.28% | 4.001 | 0.348 | 0.100 | -3.23% |
| EMERGING_MARKET_BONDS | EMB | credit | 0.03% | 0.11% | -10.24% | 6.02% | -4.61% | 1.497 | 0.671 | 0.314 | -3.43% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | 0.02% | 1.34% | -10.13% | 3.71% | -2.15% | 0.488 | 0.508 | 0.149 | -2.20% |
| SILVER | SLV | precious_metals | -4.97% | -14.66% | -23.87% | 39.48% | -21.40% | -0.403 | 0.401 | 1.969 | -53.28% |
| COPPER | CPER | non_energy_commodities | -2.48% | -4.77% | 0.95% | 22.28% | -7.14% | -0.547 | 0.563 | 1.241 | -7.14% |
| AGRICULTURE | DBA | non_energy_commodities | -1.27% | -1.71% | -4.73% | 12.52% | -5.32% | -0.521 | 0.063 | 0.055 | -5.32% |
| OIL | USO | energy | 3.31% | 9.69% | 1.55% | 47.09% | -15.96% | -0.479 | -0.393 | -1.529 | 0.00% |
| US_DOLLAR | UUP | currencies | -0.34% | 1.37% | -4.86% | 5.32% | -2.52% | -0.240 | -0.337 | -0.145 | -0.79% |
| EURO | FXE | currencies | 0.05% | -0.90% | -11.13% | 4.88% | -4.32% | -0.241 | 0.329 | 0.139 | -6.24% |
| YEN | FXY | currencies | 0.88% | 1.47% | -8.23% | 9.99% | -3.38% | -0.648 | 0.214 | 0.137 | -3.42% |
| BITCOIN_ETF | IBIT | crypto_assets | -1.14% | -3.30% | -0.23% | 37.66% | -7.14% | -0.418 | 0.504 | 1.786 | -29.44% |
| ETHEREUM_ETF | ETHA | crypto_assets | -2.76% | -10.63% | 6.63% | 47.49% | -13.86% | -0.148 | 0.506 | 2.506 | -43.43% |
