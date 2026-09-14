# Full-Universe Horizon-Specific Decision Context

Profile: weekly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: tiingo_eod_adjusted_price_and_volume
- As-of date requested: 2026-09-11
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | -1.15% |
| spy_return_21s | -1.06% |
| rsp_return_5s | -2.35% |
| rsp_return_21s | -2.81% |
| hyg_return_5s | -0.77% |
| hyg_return_21s | -0.73% |
| tlt_return_5s | -1.46% |
| tlt_return_21s | -1.13% |
| uup_return_5s | 0.21% |
| uup_return_21s | -0.46% |
| uso_return_5s | 9.02% |
| uso_return_21s | 21.68% |
| iau_return_5s | -2.84% |
| iau_return_21s | -1.53% |
| rsp_minus_spy_5s | -1.21% |
| rsp_minus_spy_21s | -1.75% |
| positive_asset_share_5s | 20.29% |
| positive_asset_share_21s | 23.19% |
| active_return_dispersion_5s | 2.24% |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_3s | active_return_5s | prior_16s_active_return | volatility_21s | max_drawdown_21s | volume_zscore_5v60 | corr_spy_63s | beta_spy_63s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | 1.15% | -0.09% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.04% | 1.24% | 0.12% | 0.17% | 0.00% | -0.186 | 0.027 | 0.000 | 0.00% |
| SP500 | SPY | diversified_us_equity | -0.22% | 0.00% | 0.00% | 8.94% | -2.58% | -0.614 | 1.000 | 1.000 | -1.75% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | -0.34% | -0.06% | -0.32% | 9.25% | -2.88% | -0.122 | 0.992 | 0.977 | -2.08% |
| NASDAQ100 | QQQ | technology_and_growth | -0.48% | 0.76% | -0.92% | 13.12% | -3.52% | -0.913 | 0.904 | 1.662 | -4.09% |
| LARGE_GROWTH | IWF | technology_and_growth | -0.61% | 0.21% | -0.88% | 13.86% | -3.68% | -0.683 | 0.889 | 1.447 | -4.97% |
| LARGE_VALUE | IWD | diversified_us_equity | 0.02% | -0.32% | 0.54% | 9.14% | -2.33% | -0.293 | 0.624 | 0.510 | -1.47% |
| MID_CAP | IJH | diversified_us_equity | -1.22% | -0.58% | -3.05% | 11.64% | -6.11% | -0.549 | 0.767 | 0.779 | -5.38% |
| SMALL_CAP | IWM | diversified_us_equity | -1.96% | -0.99% | -2.57% | 12.71% | -5.70% | -0.173 | 0.735 | 0.830 | -5.31% |
| SMALL_VALUE | IWN | diversified_us_equity | -1.38% | -0.65% | -1.07% | 10.22% | -3.72% | -0.562 | 0.580 | 0.529 | -3.40% |
| DIVIDEND | SCHD | diversified_us_equity | -0.84% | -1.59% | 2.31% | 10.78% | -3.46% | 0.678 | 0.053 | 0.052 | -3.10% |
| LOW_VOL | SPLV | diversified_us_equity | -1.02% | -0.78% | -0.67% | 8.71% | -3.34% | -0.427 | -0.152 | -0.146 | -5.18% |
| MOMENTUM | MTUM | diversified_us_equity | -0.53% | 3.69% | -4.95% | 20.76% | -7.93% | -1.186 | 0.633 | 1.783 | -11.06% |
| TECHNOLOGY | XLK | technology_and_growth | -0.11% | 2.06% | -1.62% | 20.65% | -5.62% | -0.809 | 0.793 | 1.987 | -5.21% |
| COMMUNICATIONS | XLC | technology_and_growth | 0.97% | 0.46% | 2.73% | 16.62% | -2.25% | -0.658 | 0.383 | 0.622 | -5.68% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | -0.90% | -1.86% | -1.30% | 16.72% | -5.59% | -0.419 | 0.657 | 1.116 | -8.92% |
| CONSUMER_STAPLES | XLP | consumer_defensive | -0.76% | -1.06% | 0.12% | 15.06% | -5.03% | 0.190 | -0.141 | -0.193 | -6.20% |
| HEALTHCARE | XLV | healthcare_and_biotech | -1.06% | -3.41% | 2.77% | 20.02% | -5.87% | -0.547 | -0.146 | -0.230 | -5.87% |
| FINANCIALS | XLF | financials | -0.09% | -1.09% | 1.02% | 13.01% | -2.89% | -0.228 | 0.365 | 0.388 | -2.24% |
| INDUSTRIALS | XLI | industrials_and_defense | -1.18% | -0.11% | -6.18% | 13.24% | -8.56% | -0.349 | 0.626 | 0.843 | -7.58% |
| ENERGY | XLE | energy | 0.57% | 1.95% | 5.79% | 15.14% | -2.65% | -0.040 | -0.403 | -0.711 | -0.26% |
| MATERIALS | XLB | materials_and_mining | -1.91% | -2.03% | -0.01% | 14.95% | -5.42% | -0.156 | 0.323 | 0.466 | -5.07% |
| UTILITIES | XLU | rate_sensitive_defensive | -2.44% | -0.34% | -1.94% | 13.65% | -4.69% | -0.369 | -0.050 | -0.059 | -10.00% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | -1.09% | -0.73% | -0.63% | 11.90% | -5.09% | -0.296 | -0.067 | -0.081 | -5.63% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | -1.25% | -0.23% | -0.46% | 5.00% | -2.32% | -0.121 | 0.372 | 0.145 | -4.94% |
| LONG_TREASURY | TLT | rates_and_duration | -1.62% | -0.31% | 0.25% | 10.67% | -2.85% | 0.413 | 0.281 | 0.217 | -8.56% |
| TIPS | TIP | rates_and_duration | -1.13% | 0.06% | -0.01% | 4.12% | -1.67% | -0.055 | 0.256 | 0.076 | -2.23% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | -1.10% | 0.03% | -0.25% | 6.06% | -1.97% | -0.165 | 0.445 | 0.190 | -4.04% |
| HIGH_YIELD_CREDIT | HYG | credit | -0.66% | 0.38% | -0.04% | 2.88% | -1.11% | 0.401 | 0.744 | 0.169 | -1.11% |
| AGGREGATE_BONDS | AGG | rates_and_duration | -0.95% | 0.15% | -0.23% | 4.37% | -1.73% | 0.095 | 0.414 | 0.134 | -3.09% |
| DEVELOPED_EX_US | VEA | international_equity | -1.03% | 0.13% | 0.10% | 12.69% | -2.53% | -0.163 | 0.758 | 0.989 | -1.49% |
| EMERGING_MARKETS | VWO | international_equity | -1.44% | 0.10% | 0.87% | 10.91% | -2.44% | -0.348 | 0.799 | 1.073 | -1.77% |
| EUROPE | VGK | international_equity | -1.28% | -0.73% | -0.64% | 9.45% | -4.05% | -1.041 | 0.694 | 0.679 | -3.40% |
| JAPAN | EWJ | international_equity | 0.61% | 1.82% | 0.02% | 16.90% | -4.27% | -0.601 | 0.712 | 1.276 | 0.00% |
| CHINA | MCHI | international_equity | -1.84% | -1.44% | -1.38% | 12.60% | -5.14% | -0.729 | 0.384 | 0.533 | -19.44% |
| INDIA | INDA | international_equity | -1.06% | -1.56% | -0.15% | 11.95% | -4.22% | -0.308 | 0.548 | 0.588 | -12.15% |
| GOLD | IAU | precious_metals | -0.29% | -1.69% | 1.26% | 27.50% | -7.40% | -0.219 | 0.359 | 0.732 | -19.55% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | 2.54% | 4.82% | 6.14% | 18.16% | -2.57% | -0.253 | -0.331 | -0.600 | -1.30% |
| SEMICONDUCTORS | SMH | technology_and_growth | -0.91% | 4.03% | -5.60% | 30.36% | -8.22% | -0.661 | 0.687 | 2.646 | -15.01% |
| SOFTWARE | IGV | technology_and_growth | -1.11% | -3.93% | 3.67% | 39.42% | -8.27% | -0.879 | 0.491 | 1.329 | -13.80% |
| BROAD_AI_TECH | AIQ | technology_and_growth | -0.53% | 0.65% | 0.74% | 19.80% | -3.59% | -0.674 | 0.802 | 2.146 | -8.78% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | -2.17% | -0.03% | -4.83% | 23.22% | -7.91% | -0.258 | 0.815 | 2.177 | -15.62% |
| CYBERSECURITY | CIBR | technology_and_growth | 0.41% | 0.18% | -5.14% | 39.12% | -9.53% | -0.867 | 0.496 | 1.260 | -7.63% |
| SOLAR | TAN | clean_energy | -4.03% | -0.05% | -8.90% | 24.42% | -10.69% | -0.618 | 0.688 | 2.049 | -36.22% |
| METALS_MINING | XME | materials_and_mining | -5.27% | -2.86% | 1.27% | 36.54% | -7.62% | -0.804 | 0.512 | 1.518 | -14.40% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | -0.86% | -1.21% | -0.55% | 10.39% | -4.31% | -0.622 | 0.648 | 0.563 | -3.55% |
| BIOTECH | XBI | healthcare_and_biotech | -3.54% | -3.83% | 3.04% | 32.82% | -7.87% | -0.667 | 0.222 | 0.528 | -7.87% |
| REGIONAL_BANKS | KRE | financials | -0.55% | -0.15% | -3.33% | 15.33% | -6.81% | -0.551 | 0.214 | 0.303 | -5.17% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | -2.02% | -1.94% | -10.28% | 19.20% | -13.78% | 0.190 | 0.377 | 0.665 | -13.51% |
| CANADA | EWC | international_equity | -1.48% | -1.88% | 1.05% | 13.65% | -3.75% | 0.585 | 0.533 | 0.498 | -3.29% |
| UNITED_KINGDOM | EWU | international_equity | -0.85% | -0.37% | 0.55% | 9.45% | -3.77% | -0.243 | 0.305 | 0.294 | -2.94% |
| AUSTRALIA | EWA | international_equity | -2.43% | -2.47% | 1.52% | 14.52% | -4.44% | 1.029 | 0.521 | 0.648 | -3.81% |
| SOUTH_KOREA | EWY | international_equity | -0.63% | 5.67% | 2.58% | 46.68% | -8.13% | -0.689 | 0.592 | 3.269 | -13.91% |
| TAIWAN | EWT | international_equity | -0.56% | 1.86% | 3.63% | 22.16% | -4.15% | -0.993 | 0.723 | 2.221 | -1.13% |
| BRAZIL | EWZ | international_equity | -1.09% | 1.31% | 12.52% | 22.16% | -1.40% | 0.896 | 0.206 | 0.367 | -7.61% |
| MEXICO | EWW | international_equity | -1.68% | -0.92% | 0.58% | 15.14% | -3.34% | -0.821 | 0.522 | 0.704 | -5.84% |
| SOUTH_AFRICA | EZA | international_equity | -1.68% | -1.25% | 5.02% | 27.68% | -4.10% | -0.504 | 0.603 | 1.337 | -12.27% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | -1.24% | -0.23% | -0.29% | 4.98% | -2.19% | 0.309 | 0.447 | 0.173 | -3.33% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | -0.82% | 0.35% | -1.68% | 4.26% | -2.97% | 5.033 | 0.483 | 0.139 | -3.56% |
| EMERGING_MARKET_BONDS | EMB | credit | -1.08% | -0.03% | -0.17% | 5.24% | -1.71% | 1.076 | 0.676 | 0.274 | -2.34% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | -0.84% | 0.28% | -0.71% | 4.09% | -1.72% | -0.070 | 0.469 | 0.138 | -2.91% |
| SILVER | SLV | precious_metals | -2.11% | -2.86% | 2.43% | 41.18% | -8.40% | -0.194 | 0.449 | 1.528 | -44.96% |
| COPPER | CPER | non_energy_commodities | -3.43% | -0.68% | -0.36% | 25.53% | -4.90% | 1.654 | 0.482 | 0.942 | -4.56% |
| AGRICULTURE | DBA | non_energy_commodities | -0.69% | 0.60% | 4.40% | 12.75% | -2.17% | 0.140 | 0.008 | 0.008 | -1.90% |
| OIL | USO | energy | 6.07% | 10.16% | 11.53% | 39.29% | -6.31% | 0.180 | -0.408 | -1.756 | -2.20% |
| US_DOLLAR | UUP | currencies | 0.29% | 1.36% | -0.76% | 5.16% | -1.13% | -0.487 | -0.305 | -0.131 | -1.85% |
| EURO | FXE | currencies | -0.21% | 0.90% | 0.88% | 4.43% | -0.76% | 0.277 | 0.299 | 0.116 | -3.17% |
| YEN | FXY | currencies | 0.20% | 2.52% | 2.26% | 10.49% | -1.41% | 0.147 | 0.275 | 0.217 | -5.00% |
| BITCOIN_ETF | IBIT | crypto_assets | -1.40% | -4.42% | 29.06% | 45.81% | -5.76% | -0.206 | 0.341 | 1.056 | -38.60% |
| ETHEREUM_ETF | ETHA | crypto_assets | 2.35% | 1.88% | 34.23% | 56.56% | -4.35% | 0.868 | 0.331 | 1.389 | -46.47% |
