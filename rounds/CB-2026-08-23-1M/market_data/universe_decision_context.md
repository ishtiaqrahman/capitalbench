# Full-Universe Horizon-Specific Decision Context

Profile: monthly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: yahoo_chart_adjusted_close_and_reported_volume
- As-of date requested: 2026-08-21
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | -1.37% |
| spy_return_21s | 3.73% |
| rsp_return_5s | -0.49% |
| rsp_return_21s | 4.60% |
| hyg_return_5s | -0.13% |
| hyg_return_21s | 0.97% |
| tlt_return_5s | 0.01% |
| tlt_return_21s | -0.95% |
| uup_return_5s | -0.75% |
| uup_return_21s | -2.31% |
| uso_return_5s | 6.35% |
| uso_return_21s | -3.48% |
| iau_return_5s | 5.48% |
| iau_return_21s | 13.97% |
| rsp_minus_spy_5s | 0.87% |
| rsp_minus_spy_21s | 0.87% |
| positive_asset_share_5s | 39.13% |
| positive_asset_share_21s | 82.61% |
| active_return_dispersion_5s |  |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_5s | active_return_21s | prior_105s_active_return | volatility_63s | max_drawdown_63s | volume_zscore_20v120 | corr_spy_252s | beta_spy_252s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | -3.73% | -7.64% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.08% | -3.41% | -6.17% | 0.21% | -0.01% | -0.344 | -0.097 | -0.001 | 0.00% |
| SP500 | SPY | diversified_us_equity | -1.37% | 0.00% | 0.00% | 13.72% | -4.49% | -0.814 | 1.000 | 1.000 | -1.56% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | -1.46% | -0.02% | 0.18% | 13.65% | -4.36% | -0.661 | 0.995 | 1.013 | -1.58% |
| NASDAQ100 | QQQ | technology_and_growth | -2.41% | -0.63% | 6.29% | 25.69% | -11.22% | -0.717 | 0.930 | 1.414 | -4.28% |
| LARGE_GROWTH | IWF | technology_and_growth | -2.31% | -0.53% | -2.94% | 20.95% | -11.35% | -0.894 | 0.936 | 1.281 | -4.87% |
| LARGE_VALUE | IWD | diversified_us_equity | -0.50% | 0.78% | 2.40% | 11.26% | -2.40% | -0.670 | 0.806 | 0.706 | -0.57% |
| MID_CAP | IJH | diversified_us_equity | -2.42% | -1.98% | -2.50% | 13.83% | -3.09% | -0.825 | 0.810 | 0.983 | -2.42% |
| SMALL_CAP | IWM | diversified_us_equity | -1.68% | -1.04% | 3.20% | 16.94% | -3.95% | -1.077 | 0.820 | 1.216 | -1.68% |
| SMALL_VALUE | IWN | diversified_us_equity | -1.15% | -1.81% | 2.85% | 13.58% | -2.75% | -0.642 | 0.735 | 0.962 | -1.15% |
| DIVIDEND | SCHD | diversified_us_equity | 1.71% | 3.31% | -2.16% | 12.34% | -2.95% | 0.342 | 0.291 | 0.252 | 0.00% |
| LOW_VOL | SPLV | diversified_us_equity | -1.38% | -5.11% | -5.96% | 12.89% | -3.75% | -0.581 | 0.027 | 0.022 | -3.41% |
| MOMENTUM | MTUM | diversified_us_equity | -3.80% | -6.54% | 15.84% | 38.59% | -17.99% | 0.474 | 0.768 | 1.559 | -11.60% |
| TECHNOLOGY | XLK | technology_and_growth | -3.53% | -1.01% | 19.34% | 35.06% | -15.86% | -0.969 | 0.854 | 1.724 | -7.41% |
| COMMUNICATIONS | XLC | technology_and_growth | -1.37% | 1.98% | -16.89% | 19.57% | -9.44% | -0.689 | 0.579 | 0.678 | -6.69% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | -0.15% | 4.78% | -14.67% | 21.88% | -10.72% | -0.886 | 0.777 | 1.179 | -4.84% |
| CONSUMER_STAPLES | XLP | consumer_defensive | -0.12% | -0.39% | -11.77% | 17.43% | -3.58% | -0.663 | -0.053 | -0.059 | -3.26% |
| HEALTHCARE | XLV | healthcare_and_biotech | 4.33% | 4.43% | -3.81% | 19.87% | -3.74% | -0.502 | 0.228 | 0.284 | -0.60% |
| FINANCIALS | XLF | financials | -1.17% | -0.78% | -0.36% | 13.16% | -2.25% | -0.838 | 0.547 | 0.620 | -1.34% |
| INDUSTRIALS | XLI | industrials_and_defense | -3.36% | -4.66% | -4.44% | 18.50% | -4.80% | -0.975 | 0.720 | 0.958 | -3.36% |
| ENERGY | XLE | energy | 2.79% | 3.44% | 2.05% | 23.28% | -10.59% | -0.918 | -0.163 | -0.275 | -0.17% |
| MATERIALS | XLB | materials_and_mining | 1.90% | 2.73% | -11.90% | 19.49% | -4.75% | -0.445 | 0.537 | 0.744 | 0.00% |
| UTILITIES | XLU | rate_sensitive_defensive | -3.48% | -11.13% | -6.60% | 15.98% | -7.60% | -0.369 | 0.125 | 0.147 | -9.19% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | -0.42% | -3.44% | -2.85% | 15.82% | -4.19% | -0.396 | 0.254 | 0.278 | -2.02% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | -0.24% | -3.42% | -10.45% | 4.73% | -2.00% | -0.126 | 0.299 | 0.108 | -3.40% |
| LONG_TREASURY | TLT | rates_and_duration | 0.01% | -4.68% | -12.87% | 9.50% | -6.26% | 0.422 | 0.248 | 0.182 | -7.59% |
| TIPS | TIP | rates_and_duration | 0.13% | -3.33% | -8.39% | 3.52% | -1.40% | -0.239 | 0.277 | 0.072 | -1.04% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | -0.19% | -3.62% | -10.62% | 5.24% | -2.89% | -0.358 | 0.487 | 0.202 | -2.98% |
| HIGH_YIELD_CREDIT | HYG | credit | -0.13% | -2.76% | -7.38% | 3.06% | -0.80% | -0.663 | 0.783 | 0.235 | -0.23% |
| AGGREGATE_BONDS | AGG | rates_and_duration | -0.13% | -3.37% | -9.56% | 3.90% | -1.71% | -0.144 | 0.407 | 0.120 | -2.05% |
| DEVELOPED_EX_US | VEA | international_equity | -0.22% | 1.49% | -6.57% | 19.05% | -4.85% | -0.781 | 0.802 | 1.082 | -0.37% |
| EMERGING_MARKETS | VWO | international_equity | 0.57% | 0.31% | -8.26% | 19.23% | -7.05% | -0.686 | 0.811 | 1.108 | -1.29% |
| EUROPE | VGK | international_equity | 0.38% | 1.84% | -8.27% | 14.26% | -3.12% | -0.810 | 0.749 | 0.921 | 0.00% |
| JAPAN | EWJ | international_equity | -3.09% | 0.75% | -7.50% | 23.80% | -7.86% | -0.944 | 0.720 | 1.181 | -3.34% |
| CHINA | MCHI | international_equity | 1.89% | 0.60% | -19.62% | 18.76% | -11.15% | -0.511 | 0.542 | 0.854 | -15.34% |
| INDIA | INDA | international_equity | -0.28% | 0.49% | -18.48% | 12.91% | -4.59% | -0.794 | 0.552 | 0.644 | -10.22% |
| GOLD | IAU | precious_metals | 5.48% | 10.24% | -28.28% | 26.09% | -12.50% | -0.462 | 0.312 | 0.692 | -14.55% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | 4.13% | -0.46% | 15.72% | 22.01% | -13.82% | -0.356 | -0.179 | -0.280 | -1.37% |
| SEMICONDUCTORS | SMH | technology_and_growth | -4.66% | -7.13% | 32.15% | 53.57% | -24.62% | 0.158 | 0.779 | 2.360 | -16.22% |
| SOFTWARE | IGV | technology_and_growth | -0.68% | 14.95% | 0.20% | 35.37% | -21.29% | -0.947 | 0.510 | 1.186 | -12.23% |
| BROAD_AI_TECH | AIQ | technology_and_growth | -1.20% | 3.18% | 11.31% | 39.39% | -20.19% | -0.543 | 0.847 | 1.905 | -9.57% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | -3.69% | 3.74% | -14.14% | 37.99% | -23.82% | -0.668 | 0.802 | 2.180 | -12.68% |
| CYBERSECURITY | CIBR | technology_and_growth | -4.77% | 4.40% | 29.99% | 33.18% | -11.74% | -0.261 | 0.540 | 1.117 | -7.19% |
| SOLAR | TAN | clean_energy | -5.10% | -10.41% | -19.22% | 44.62% | -35.51% | 0.216 | 0.632 | 1.901 | -33.29% |
| METALS_MINING | XME | materials_and_mining | 1.88% | 11.94% | -19.69% | 41.98% | -26.49% | -0.055 | 0.596 | 1.753 | -10.09% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | -0.49% | 0.87% | -2.96% | 11.11% | -2.04% | -0.808 | 0.776 | 0.706 | -0.49% |
| BIOTECH | XBI | healthcare_and_biotech | 5.29% | 5.14% | 14.48% | 31.44% | -10.51% | -0.279 | 0.472 | 1.019 | -2.25% |
| REGIONAL_BANKS | KRE | financials | -3.94% | -4.12% | -1.90% | 18.94% | -4.13% | -0.787 | 0.428 | 0.751 | -3.94% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | -6.27% | -4.10% | -9.73% | 25.33% | -8.58% | -0.433 | 0.566 | 1.014 | -6.27% |
| CANADA | EWC | international_equity | 0.21% | 2.29% | -4.25% | 11.60% | -3.20% | -0.379 | 0.673 | 0.744 | 0.00% |
| UNITED_KINGDOM | EWU | international_equity | 1.41% | 1.07% | -9.04% | 12.77% | -3.40% | -0.528 | 0.606 | 0.703 | 0.00% |
| AUSTRALIA | EWA | international_equity | 1.65% | 2.06% | -10.37% | 16.64% | -4.78% | -0.765 | 0.672 | 0.926 | -0.89% |
| SOUTH_KOREA | EWY | international_equity | -0.78% | -1.15% | 14.90% | 80.23% | -34.21% | 0.052 | 0.635 | 2.746 | -18.64% |
| TAIWAN | EWT | international_equity | -2.59% | 0.74% | 26.59% | 43.06% | -19.83% | -0.699 | 0.760 | 1.841 | -6.48% |
| BRAZIL | EWZ | international_equity | 3.33% | -6.80% | -14.89% | 21.53% | -8.97% | -0.660 | 0.505 | 0.981 | -15.18% |
| MEXICO | EWW | international_equity | 3.16% | -0.56% | -13.95% | 19.32% | -6.47% | -0.352 | 0.543 | 0.932 | -3.34% |
| SOUTH_AFRICA | EZA | international_equity | 7.37% | 16.26% | -27.70% | 31.70% | -11.54% | -0.784 | 0.619 | 1.592 | -9.19% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | -0.09% | -3.10% | -9.54% | 4.56% | -1.85% | 0.075 | 0.402 | 0.139 | -1.85% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | -0.49% | -3.38% | -9.36% | 3.05% | -2.15% | 0.646 | 0.390 | 0.091 | -1.81% |
| EMERGING_MARKET_BONDS | EMB | credit | -0.35% | -3.09% | -8.72% | 5.43% | -1.96% | -0.679 | 0.688 | 0.308 | -1.33% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | -0.15% | -3.61% | -9.12% | 3.49% | -1.45% | -0.570 | 0.472 | 0.131 | -1.80% |
| SILVER | SLV | precious_metals | 7.25% | 16.75% | -39.69% | 44.39% | -27.73% | -0.652 | 0.352 | 1.694 | -40.61% |
| COPPER | CPER | non_energy_commodities | -0.05% | 0.85% | -1.92% | 25.20% | -10.57% | -0.538 | 0.546 | 1.196 | -2.11% |
| AGRICULTURE | DBA | non_energy_commodities | 1.98% | -3.45% | 0.85% | 12.90% | -4.96% | -0.550 | 0.081 | 0.070 | -1.43% |
| OIL | USO | energy | 6.35% | -7.21% | 64.89% | 52.45% | -27.55% | -0.598 | -0.339 | -1.265 | -11.98% |
| US_DOLLAR | UUP | currencies | -0.75% | -6.04% | -2.21% | 5.13% | -2.52% | -0.506 | -0.308 | -0.138 | -2.45% |
| EURO | FXE | currencies | 0.95% | -1.01% | -10.79% | 4.91% | -2.66% | -0.699 | 0.288 | 0.129 | -2.53% |
| YEN | FXY | currencies | 0.21% | -0.71% | -13.16% | 7.91% | -3.06% | 1.567 | 0.187 | 0.119 | -8.15% |
| BITCOIN_ETF | IBIT | crypto_assets | 22.59% | 15.45% | -12.25% | 41.47% | -24.34% | -0.195 | 0.482 | 1.696 | -38.73% |
| ETHEREUM_ETF | ETHA | crypto_assets | 28.63% | 25.54% | -12.88% | 59.55% | -27.31% | 0.082 | 0.509 | 2.650 | -50.15% |
