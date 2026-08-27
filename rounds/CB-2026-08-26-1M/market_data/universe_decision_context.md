# Full-Universe Horizon-Specific Decision Context

Profile: monthly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: tiingo_eod_adjusted_price_and_volume
- As-of date requested: 2026-08-26
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | -0.39% |
| spy_return_21s | 3.40% |
| rsp_return_5s | 0.02% |
| rsp_return_21s | 2.03% |
| hyg_return_5s | 0.24% |
| hyg_return_21s | 1.09% |
| tlt_return_5s | 0.34% |
| tlt_return_21s | -0.72% |
| uup_return_5s | 0.50% |
| uup_return_21s | -1.96% |
| uso_return_5s | -2.72% |
| uso_return_21s | 5.69% |
| iau_return_5s | 1.80% |
| iau_return_21s | 14.10% |
| rsp_minus_spy_5s | 0.41% |
| rsp_minus_spy_21s | -1.37% |
| positive_asset_share_5s | 52.17% |
| positive_asset_share_21s | 81.16% |
| active_return_dispersion_5s |  |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_5s | active_return_21s | prior_105s_active_return | volatility_63s | max_drawdown_63s | volume_zscore_20v120 | corr_spy_252s | beta_spy_252s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | -3.40% | -7.45% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.07% | -3.11% | -5.96% | 0.21% | -0.01% | -0.364 | -0.112 | -0.002 | 0.00% |
| SP500 | SPY | diversified_us_equity | -0.39% | 0.00% | 0.00% | 13.68% | -4.49% | -0.919 | 1.000 | 1.000 | -1.52% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | -0.46% | -0.06% | 0.27% | 13.59% | -4.36% | -0.675 | 0.995 | 1.011 | -1.58% |
| NASDAQ100 | QQQ | technology_and_growth | -0.66% | 1.91% | 2.34% | 25.54% | -11.22% | -0.889 | 0.930 | 1.423 | -4.56% |
| LARGE_GROWTH | IWF | technology_and_growth | -0.75% | 1.12% | -5.66% | 21.06% | -11.36% | -0.867 | 0.936 | 1.288 | -5.37% |
| LARGE_VALUE | IWD | diversified_us_equity | -0.12% | -0.86% | 5.32% | 11.12% | -2.40% | -0.658 | 0.801 | 0.697 | -0.12% |
| MID_CAP | IJH | diversified_us_equity | -0.55% | -2.63% | -1.02% | 13.53% | -3.22% | -0.754 | 0.807 | 0.972 | -2.61% |
| SMALL_CAP | IWM | diversified_us_equity | -0.92% | -1.51% | 3.89% | 16.54% | -3.95% | -1.170 | 0.820 | 1.199 | -2.02% |
| SMALL_VALUE | IWN | diversified_us_equity | -0.56% | -3.30% | 5.45% | 13.22% | -2.75% | -0.860 | 0.734 | 0.937 | -1.36% |
| DIVIDEND | SCHD | diversified_us_equity | -0.11% | 0.02% | 1.87% | 11.81% | -2.93% | 0.265 | 0.277 | 0.239 | -0.45% |
| LOW_VOL | SPLV | diversified_us_equity | 0.05% | -5.90% | -4.16% | 13.04% | -3.41% | -0.601 | 0.013 | 0.011 | -2.50% |
| MOMENTUM | MTUM | diversified_us_equity | -0.61% | 0.59% | 6.79% | 38.11% | -17.99% | 0.118 | 0.770 | 1.576 | -11.94% |
| TECHNOLOGY | XLK | technology_and_growth | -0.44% | 3.46% | 12.47% | 34.86% | -15.86% | -1.115 | 0.855 | 1.742 | -7.64% |
| COMMUNICATIONS | XLC | technology_and_growth | 1.16% | -0.72% | -12.77% | 19.67% | -9.44% | -0.842 | 0.573 | 0.675 | -5.67% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | -1.21% | 0.76% | -11.01% | 21.61% | -10.72% | -0.977 | 0.772 | 1.166 | -5.54% |
| CONSUMER_STAPLES | XLP | consumer_defensive | -0.31% | -4.31% | -8.41% | 17.53% | -3.57% | -0.850 | -0.066 | -0.073 | -2.94% |
| HEALTHCARE | XLV | healthcare_and_biotech | -1.22% | 0.35% | -0.58% | 19.81% | -3.74% | -0.672 | 0.221 | 0.276 | -1.22% |
| FINANCIALS | XLF | financials | 1.36% | -2.26% | 4.55% | 13.17% | -2.25% | -0.925 | 0.535 | 0.609 | -0.09% |
| INDUSTRIALS | XLI | industrials_and_defense | -0.88% | -4.58% | -2.99% | 18.43% | -4.80% | -0.965 | 0.715 | 0.954 | -3.31% |
| ENERGY | XLE | energy | -1.81% | 5.04% | -1.10% | 22.67% | -9.47% | -0.934 | -0.174 | -0.295 | -2.07% |
| MATERIALS | XLB | materials_and_mining | 2.19% | -0.86% | -8.01% | 19.29% | -4.75% | -0.476 | 0.531 | 0.737 | 0.00% |
| UTILITIES | XLU | rate_sensitive_defensive | -1.16% | -7.82% | -10.06% | 16.07% | -7.60% | -0.398 | 0.115 | 0.136 | -7.63% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | 0.22% | -5.40% | 0.09% | 15.88% | -4.19% | -0.454 | 0.241 | 0.264 | -2.00% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | -0.06% | -3.32% | -9.77% | 4.81% | -2.00% | -0.029 | 0.285 | 0.103 | -2.88% |
| LONG_TREASURY | TLT | rates_and_duration | 0.34% | -4.12% | -11.99% | 9.72% | -6.25% | 0.408 | 0.237 | 0.176 | -6.18% |
| TIPS | TIP | rates_and_duration | 0.00% | -2.81% | -8.24% | 3.52% | -1.40% | -0.286 | 0.259 | 0.067 | -0.69% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | 0.20% | -3.02% | -9.96% | 5.35% | -2.89% | -0.459 | 0.473 | 0.196 | -2.19% |
| HIGH_YIELD_CREDIT | HYG | credit | 0.24% | -2.31% | -6.86% | 3.04% | -0.80% | -0.745 | 0.779 | 0.230 | -0.03% |
| AGGREGATE_BONDS | AGG | rates_and_duration | 0.04% | -3.12% | -8.92% | 3.99% | -1.71% | -0.230 | 0.392 | 0.115 | -1.54% |
| DEVELOPED_EX_US | VEA | international_equity | 0.85% | 2.13% | -7.70% | 18.80% | -4.85% | -0.771 | 0.800 | 1.081 | -0.46% |
| EMERGING_MARKETS | VWO | international_equity | 1.03% | 1.65% | -9.49% | 18.94% | -7.05% | -0.709 | 0.809 | 1.110 | -0.95% |
| EUROPE | VGK | international_equity | 0.51% | 0.48% | -7.02% | 14.17% | -2.94% | -0.794 | 0.746 | 0.915 | -0.53% |
| JAPAN | EWJ | international_equity | 0.69% | 2.83% | -9.76% | 23.67% | -7.86% | -0.991 | 0.718 | 1.179 | -3.09% |
| CHINA | MCHI | international_equity | -0.52% | -2.14% | -17.18% | 18.64% | -11.15% | -0.541 | 0.537 | 0.847 | -16.19% |
| INDIA | INDA | international_equity | 0.42% | -2.65% | -13.82% | 13.50% | -4.59% | -0.959 | 0.552 | 0.655 | -10.02% |
| GOLD | IAU | precious_metals | 1.80% | 10.69% | -29.39% | 26.16% | -12.50% | -0.389 | 0.308 | 0.691 | -14.97% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | -0.82% | 3.16% | 8.52% | 21.78% | -12.58% | -0.323 | -0.178 | -0.282 | -3.86% |
| SEMICONDUCTORS | SMH | technology_and_growth | -0.92% | 1.54% | 16.82% | 53.00% | -24.62% | -0.572 | 0.780 | 2.384 | -16.91% |
| SOFTWARE | IGV | technology_and_growth | -0.41% | 8.16% | 6.09% | 35.27% | -21.29% | -1.169 | 0.507 | 1.188 | -13.06% |
| BROAD_AI_TECH | AIQ | technology_and_growth | 0.13% | 6.78% | 5.78% | 38.88% | -20.19% | -0.684 | 0.846 | 1.916 | -10.08% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | -2.92% | 4.29% | -16.46% | 37.84% | -23.82% | -0.916 | 0.800 | 2.192 | -14.94% |
| CYBERSECURITY | CIBR | technology_and_growth | -1.97% | 1.50% | 35.29% | 32.60% | -11.74% | -0.198 | 0.537 | 1.121 | -8.36% |
| SOLAR | TAN | clean_energy | -3.35% | -4.06% | -24.67% | 43.12% | -35.51% | -0.186 | 0.626 | 1.873 | -34.02% |
| METALS_MINING | XME | materials_and_mining | 2.77% | 15.20% | -22.44% | 41.21% | -26.49% | 0.019 | 0.595 | 1.760 | -9.36% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | 0.02% | -1.37% | 0.35% | 10.96% | -2.04% | -0.916 | 0.771 | 0.696 | -0.30% |
| BIOTECH | XBI | healthcare_and_biotech | -0.68% | 9.02% | 9.42% | 31.87% | -10.51% | -0.282 | 0.471 | 1.027 | -0.68% |
| REGIONAL_BANKS | KRE | financials | -0.56% | -6.28% | 3.72% | 18.71% | -4.62% | -0.884 | 0.415 | 0.715 | -4.30% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | -3.97% | -6.91% | -5.76% | 25.31% | -8.58% | -0.457 | 0.569 | 1.030 | -6.65% |
| CANADA | EWC | international_equity | 0.65% | 0.59% | -3.06% | 11.69% | -3.20% | -0.325 | 0.669 | 0.742 | -0.65% |
| UNITED_KINGDOM | EWU | international_equity | 0.60% | -1.23% | -7.76% | 12.87% | -3.01% | -0.561 | 0.601 | 0.702 | -1.07% |
| AUSTRALIA | EWA | international_equity | 0.60% | -0.57% | -8.86% | 16.82% | -4.78% | -0.692 | 0.670 | 0.926 | -0.92% |
| SOUTH_KOREA | EWY | international_equity | 2.72% | 14.91% | -5.73% | 77.91% | -34.21% | -0.274 | 0.634 | 2.768 | -18.26% |
| TAIWAN | EWT | international_equity | 1.61% | 9.84% | 14.47% | 41.65% | -19.83% | -0.863 | 0.760 | 1.854 | -4.61% |
| BRAZIL | EWZ | international_equity | 4.26% | -4.32% | -15.52% | 21.57% | -8.05% | -0.496 | 0.498 | 0.969 | -13.58% |
| MEXICO | EWW | international_equity | 3.21% | -2.40% | -10.62% | 19.14% | -6.47% | -0.305 | 0.540 | 0.927 | -3.13% |
| SOUTH_AFRICA | EZA | international_equity | 1.98% | 12.25% | -28.60% | 31.01% | -11.48% | -0.833 | 0.615 | 1.589 | -10.30% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | 0.01% | -3.13% | -8.69% | 4.65% | -1.85% | 0.080 | 0.388 | 0.134 | -1.36% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | -0.22% | -3.65% | -8.67% | 2.90% | -2.15% | 0.421 | 0.382 | 0.090 | -1.70% |
| EMERGING_MARKET_BONDS | EMB | credit | 0.21% | -2.84% | -7.93% | 5.41% | -1.96% | -0.713 | 0.681 | 0.305 | -0.72% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | 0.08% | -3.60% | -8.45% | 3.58% | -1.45% | -0.509 | 0.465 | 0.131 | -1.53% |
| SILVER | SLV | precious_metals | 2.63% | 15.73% | -42.86% | 43.73% | -26.29% | -0.699 | 0.352 | 1.703 | -41.68% |
| COPPER | CPER | non_energy_commodities | 1.70% | 1.11% | -3.24% | 25.45% | -10.57% | -0.510 | 0.551 | 1.219 | -1.93% |
| AGRICULTURE | DBA | non_energy_commodities | 1.06% | -0.71% | -0.87% | 13.04% | -4.86% | -0.511 | 0.071 | 0.061 | -0.49% |
| OIL | USO | energy | -2.72% | 2.29% | 43.67% | 52.35% | -26.69% | -0.619 | -0.340 | -1.285 | -16.74% |
| US_DOLLAR | UUP | currencies | 0.50% | -5.36% | -1.91% | 5.17% | -2.52% | -0.620 | -0.291 | -0.128 | -2.03% |
| EURO | FXE | currencies | -0.17% | -0.96% | -10.70% | 4.91% | -2.66% | -0.693 | 0.270 | 0.117 | -2.71% |
| YEN | FXY | currencies | -0.81% | -0.64% | -12.15% | 7.90% | -2.86% | 1.643 | 0.171 | 0.108 | -8.39% |
| BITCOIN_ETF | IBIT | crypto_assets | 14.65% | 19.62% | -15.33% | 41.34% | -21.58% | 0.047 | 0.473 | 1.659 | -37.64% |
| ETHEREUM_ETF | ETHA | crypto_assets | 17.44% | 25.31% | -15.04% | 59.13% | -24.18% | 0.361 | 0.496 | 2.517 | -47.89% |
