# Full-Universe Horizon-Specific Decision Context

Profile: monthly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: tiingo_eod_adjusted_price_and_volume
- As-of date requested: 2026-08-25
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | -0.20% |
| spy_return_21s | 3.63% |
| rsp_return_5s | 0.90% |
| rsp_return_21s | 3.06% |
| hyg_return_5s | 0.49% |
| hyg_return_21s | 1.31% |
| tlt_return_5s | 2.22% |
| tlt_return_21s | 0.07% |
| uup_return_5s | -0.71% |
| uup_return_21s | -2.31% |
| uso_return_5s | -3.45% |
| uso_return_21s | 1.11% |
| iau_return_5s | 7.40% |
| iau_return_21s | 14.30% |
| rsp_minus_spy_5s | 1.10% |
| rsp_minus_spy_21s | -0.57% |
| positive_asset_share_5s | 68.12% |
| positive_asset_share_21s | 88.41% |
| active_return_dispersion_5s |  |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_5s | active_return_21s | prior_105s_active_return | volatility_63s | max_drawdown_63s | volume_zscore_20v120 | corr_spy_252s | beta_spy_252s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | -3.63% | -8.10% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.07% | -3.33% | -6.61% | 0.21% | -0.01% | -0.381 | -0.111 | -0.002 | 0.00% |
| SP500 | SPY | diversified_us_equity | -0.20% | 0.00% | 0.00% | 13.68% | -4.49% | -0.841 | 1.000 | 1.000 | -1.54% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | -0.23% | -0.08% | 0.21% | 13.59% | -4.36% | -0.630 | 0.995 | 1.011 | -1.60% |
| NASDAQ100 | QQQ | technology_and_growth | -0.95% | 0.56% | 4.38% | 25.53% | -11.22% | -0.793 | 0.930 | 1.422 | -4.64% |
| LARGE_GROWTH | IWF | technology_and_growth | -1.01% | 0.38% | -4.42% | 21.06% | -11.36% | -0.869 | 0.935 | 1.286 | -5.31% |
| LARGE_VALUE | IWD | diversified_us_equity | 0.60% | -0.21% | 3.97% | 11.13% | -2.40% | -0.655 | 0.801 | 0.699 | -0.19% |
| MID_CAP | IJH | diversified_us_equity | -1.42% | -3.44% | -1.31% | 13.51% | -3.22% | -0.711 | 0.808 | 0.973 | -3.22% |
| SMALL_CAP | IWM | diversified_us_equity | -0.33% | -1.47% | 3.59% | 16.54% | -3.95% | -1.090 | 0.820 | 1.200 | -1.92% |
| SMALL_VALUE | IWN | diversified_us_equity | 0.08% | -2.51% | 4.33% | 13.21% | -2.75% | -0.756 | 0.735 | 0.938 | -1.23% |
| DIVIDEND | SCHD | diversified_us_equity | 1.74% | 1.40% | -0.71% | 11.84% | -2.93% | 0.340 | 0.279 | 0.241 | -0.28% |
| LOW_VOL | SPLV | diversified_us_equity | -0.33% | -5.49% | -5.98% | 13.06% | -3.48% | -0.533 | 0.017 | 0.014 | -2.81% |
| MOMENTUM | MTUM | diversified_us_equity | -3.02% | -3.61% | 12.04% | 38.09% | -17.99% | 0.243 | 0.770 | 1.575 | -12.40% |
| TECHNOLOGY | XLK | technology_and_growth | -2.09% | 0.64% | 16.42% | 34.85% | -15.86% | -0.997 | 0.855 | 1.740 | -8.20% |
| COMMUNICATIONS | XLC | technology_and_growth | 2.44% | 1.50% | -14.88% | 19.69% | -9.44% | -0.777 | 0.573 | 0.673 | -5.20% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | 1.37% | 2.79% | -12.78% | 21.87% | -10.72% | -0.924 | 0.772 | 1.165 | -4.90% |
| CONSUMER_STAPLES | XLP | consumer_defensive | 1.10% | -2.27% | -11.78% | 17.65% | -3.57% | -0.791 | -0.060 | -0.068 | -2.66% |
| HEALTHCARE | XLV | healthcare_and_biotech | 3.28% | 3.65% | -3.72% | 19.65% | -3.74% | -0.601 | 0.224 | 0.280 | -0.22% |
| FINANCIALS | XLF | financials | 0.81% | -1.11% | 4.43% | 13.32% | -2.25% | -0.841 | 0.536 | 0.610 | 0.00% |
| INDUSTRIALS | XLI | industrials_and_defense | -2.82% | -6.25% | -4.04% | 18.32% | -4.80% | -0.946 | 0.717 | 0.956 | -4.35% |
| ENERGY | XLE | energy | -2.54% | 2.71% | -0.74% | 22.89% | -9.47% | -0.920 | -0.174 | -0.295 | -2.65% |
| MATERIALS | XLB | materials_and_mining | 3.48% | 0.63% | -11.01% | 19.30% | -4.75% | -0.412 | 0.531 | 0.737 | 0.00% |
| UTILITIES | XLU | rate_sensitive_defensive | -1.61% | -8.82% | -10.03% | 16.06% | -7.60% | -0.333 | 0.118 | 0.140 | -8.05% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | 1.64% | -4.50% | -1.85% | 15.84% | -4.19% | -0.421 | 0.242 | 0.265 | -1.41% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | 0.62% | -3.04% | -10.79% | 4.79% | -2.00% | -0.035 | 0.287 | 0.103 | -2.68% |
| LONG_TREASURY | TLT | rates_and_duration | 2.22% | -3.56% | -13.19% | 9.73% | -6.25% | 0.490 | 0.238 | 0.176 | -5.99% |
| TIPS | TIP | rates_and_duration | 0.58% | -2.66% | -9.05% | 3.52% | -1.40% | -0.278 | 0.261 | 0.067 | -0.57% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | 0.96% | -2.87% | -10.93% | 5.35% | -2.89% | -0.358 | 0.474 | 0.197 | -2.12% |
| HIGH_YIELD_CREDIT | HYG | credit | 0.49% | -2.32% | -7.56% | 3.04% | -0.80% | -0.679 | 0.779 | 0.231 | 0.00% |
| AGGREGATE_BONDS | AGG | rates_and_duration | 0.68% | -2.95% | -9.85% | 3.98% | -1.71% | -0.238 | 0.393 | 0.116 | -1.39% |
| DEVELOPED_EX_US | VEA | international_equity | 1.93% | 1.79% | -6.62% | 18.81% | -4.85% | -0.725 | 0.800 | 1.083 | 0.00% |
| EMERGING_MARKETS | VWO | international_equity | 1.68% | 0.51% | -8.75% | 18.94% | -7.05% | -0.699 | 0.809 | 1.110 | -0.98% |
| EUROPE | VGK | international_equity | 1.79% | 1.27% | -7.26% | 14.12% | -3.12% | -0.779 | 0.746 | 0.918 | 0.00% |
| JAPAN | EWJ | international_equity | 0.27% | 0.87% | -7.26% | 23.71% | -7.86% | -0.960 | 0.718 | 1.181 | -2.88% |
| CHINA | MCHI | international_equity | 0.40% | -2.04% | -17.72% | 18.78% | -11.15% | -0.520 | 0.537 | 0.845 | -16.16% |
| INDIA | INDA | international_equity | 1.72% | -0.89% | -15.28% | 13.35% | -4.59% | -0.909 | 0.553 | 0.655 | -9.15% |
| GOLD | IAU | precious_metals | 7.40% | 10.67% | -29.11% | 26.09% | -12.50% | -0.404 | 0.309 | 0.690 | -13.60% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | -0.16% | 1.16% | 9.86% | 22.07% | -12.58% | -0.331 | -0.179 | -0.283 | -3.91% |
| SEMICONDUCTORS | SMH | technology_and_growth | -2.45% | -2.30% | 22.77% | 53.04% | -24.62% | -0.407 | 0.780 | 2.381 | -16.91% |
| SOFTWARE | IGV | technology_and_growth | -0.11% | 8.41% | 7.86% | 35.34% | -21.29% | -1.143 | 0.508 | 1.189 | -13.52% |
| BROAD_AI_TECH | AIQ | technology_and_growth | 0.88% | 4.57% | 9.70% | 38.88% | -20.19% | -0.500 | 0.846 | 1.914 | -10.06% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | -3.20% | 3.22% | -16.03% | 37.84% | -23.82% | -0.742 | 0.800 | 2.188 | -14.66% |
| CYBERSECURITY | CIBR | technology_and_growth | -5.11% | 0.14% | 36.97% | 33.12% | -11.74% | -0.170 | 0.538 | 1.122 | -9.53% |
| SOLAR | TAN | clean_energy | -2.05% | -8.88% | -22.92% | 43.47% | -35.51% | -0.154 | 0.626 | 1.872 | -33.92% |
| METALS_MINING | XME | materials_and_mining | 6.43% | 13.66% | -21.61% | 41.19% | -26.49% | 0.053 | 0.594 | 1.756 | -8.89% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | 0.90% | -0.57% | -1.48% | 10.97% | -2.04% | -0.852 | 0.771 | 0.697 | -0.45% |
| BIOTECH | XBI | healthcare_and_biotech | 5.61% | 8.66% | 8.60% | 31.84% | -10.51% | -0.288 | 0.473 | 1.033 | -0.27% |
| REGIONAL_BANKS | KRE | financials | -3.28% | -5.20% | 3.14% | 18.84% | -4.62% | -0.782 | 0.415 | 0.716 | -4.62% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | -7.08% | -7.57% | -7.64% | 25.27% | -8.58% | -0.442 | 0.569 | 1.030 | -7.47% |
| CANADA | EWC | international_equity | 1.72% | 1.84% | -3.69% | 11.71% | -3.20% | -0.321 | 0.670 | 0.744 | 0.00% |
| UNITED_KINGDOM | EWU | international_equity | 2.55% | 0.64% | -7.95% | 12.70% | -3.40% | -0.525 | 0.604 | 0.703 | 0.00% |
| AUSTRALIA | EWA | international_equity | 2.77% | 1.74% | -9.08% | 16.70% | -4.78% | -0.722 | 0.671 | 0.930 | 0.00% |
| SOUTH_KOREA | EWY | international_equity | 5.94% | 8.13% | 3.42% | 77.94% | -34.21% | -0.076 | 0.635 | 2.768 | -17.81% |
| TAIWAN | EWT | international_equity | 0.97% | 4.13% | 21.06% | 41.64% | -19.83% | -0.800 | 0.760 | 1.855 | -5.50% |
| BRAZIL | EWZ | international_equity | 6.47% | -3.60% | -16.35% | 21.65% | -8.05% | -0.521 | 0.497 | 0.966 | -13.20% |
| MEXICO | EWW | international_equity | 4.55% | -1.92% | -11.47% | 19.21% | -6.47% | -0.301 | 0.541 | 0.931 | -2.76% |
| SOUTH_AFRICA | EZA | international_equity | 8.06% | 13.44% | -28.29% | 31.04% | -11.60% | -0.760 | 0.615 | 1.589 | -9.26% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | 0.74% | -2.83% | -9.68% | 4.64% | -1.85% | 0.334 | 0.389 | 0.135 | -1.16% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | 0.20% | -3.57% | -9.47% | 2.93% | -2.15% | 0.580 | 0.382 | 0.090 | -1.58% |
| EMERGING_MARKET_BONDS | EMB | credit | 0.78% | -2.75% | -8.73% | 5.45% | -1.96% | -0.699 | 0.681 | 0.306 | -0.65% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | 0.67% | -3.40% | -9.37% | 3.53% | -1.45% | -0.527 | 0.467 | 0.131 | -1.26% |
| SILVER | SLV | precious_metals | 8.50% | 14.11% | -41.17% | 44.12% | -27.73% | -0.684 | 0.352 | 1.704 | -40.98% |
| COPPER | CPER | non_energy_commodities | 4.03% | 1.50% | -1.30% | 25.37% | -10.57% | -0.462 | 0.551 | 1.216 | -0.22% |
| AGRICULTURE | DBA | non_energy_commodities | 0.89% | -1.24% | -1.91% | 12.87% | -4.86% | -0.581 | 0.072 | 0.061 | -1.57% |
| OIL | USO | energy | -3.45% | -2.51% | 46.38% | 53.03% | -26.69% | -0.614 | -0.341 | -1.287 | -17.53% |
| US_DOLLAR | UUP | currencies | -0.71% | -5.94% | -2.60% | 5.14% | -2.52% | -0.536 | -0.294 | -0.130 | -2.31% |
| EURO | FXE | currencies | 0.90% | -0.83% | -11.24% | 4.90% | -2.66% | -0.680 | 0.273 | 0.120 | -2.53% |
| YEN | FXY | currencies | 0.26% | -0.74% | -13.14% | 7.91% | -2.86% | 1.420 | 0.173 | 0.110 | -8.26% |
| BITCOIN_ETF | IBIT | crypto_assets | 22.19% | 17.99% | -7.44% | 41.41% | -22.56% | 0.017 | 0.474 | 1.672 | -37.27% |
| ETHEREUM_ETF | ETHA | crypto_assets | 28.81% | 22.82% | -3.25% | 59.18% | -24.84% | 0.288 | 0.496 | 2.540 | -48.03% |
