# Full-Universe Horizon-Specific Decision Context

Profile: weekly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: yahoo_chart_adjusted_close_and_reported_volume
- As-of date requested: 2026-07-22
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | -0.98% |
| spy_return_21s | 0.41% |
| rsp_return_5s | -0.13% |
| rsp_return_21s | 1.47% |
| hyg_return_5s | -0.36% |
| hyg_return_21s | -0.06% |
| tlt_return_5s | -0.95% |
| tlt_return_21s | -2.72% |
| uup_return_5s | 0.71% |
| uup_return_21s | 0.32% |
| uso_return_5s | 8.49% |
| uso_return_21s | 16.85% |
| iau_return_5s | 1.85% |
| iau_return_21s | -1.41% |
| rsp_minus_spy_5s | 0.85% |
| rsp_minus_spy_21s | 1.07% |
| positive_asset_share_5s | 37.68% |
| positive_asset_share_21s | 47.83% |
| active_return_dispersion_5s | 1.98% |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_3s | active_return_5s | prior_16s_active_return | volatility_21s | max_drawdown_21s | volume_zscore_5v60 | corr_spy_63s | beta_spy_63s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | 0.98% | -1.40% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.03% | 1.05% | -1.16% | 0.23% | -0.01% | -0.270 | -0.234 | -0.004 | 0.00% |
| SP500 | SPY | diversified_us_equity | 0.55% | 0.00% | 0.00% | 11.70% | -2.07% | -0.521 | 1.000 | 1.000 | -1.35% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | 0.51% | 0.03% | -0.13% | 10.82% | -1.73% | -0.822 | 0.992 | 0.990 | -1.18% |
| NASDAQ100 | QQQ | technology_and_growth | 1.44% | -0.75% | -4.14% | 24.88% | -5.78% | -0.539 | 0.920 | 1.736 | -5.37% |
| LARGE_GROWTH | IWF | technology_and_growth | 1.29% | -1.17% | 0.09% | 21.73% | -3.86% | 0.904 | 0.887 | 1.289 | -6.01% |
| LARGE_VALUE | IWD | diversified_us_equity | -0.21% | 1.08% | 0.14% | 10.34% | -1.06% | 0.158 | 0.705 | 0.639 | -0.78% |
| MID_CAP | IJH | diversified_us_equity | 0.20% | 1.06% | -1.98% | 11.93% | -3.09% | -0.711 | 0.771 | 0.867 | -1.84% |
| SMALL_CAP | IWM | diversified_us_equity | -0.09% | 0.31% | -2.21% | 11.65% | -2.71% | -0.654 | 0.783 | 1.112 | -2.22% |
| SMALL_VALUE | IWN | diversified_us_equity | -0.13% | 1.32% | 0.11% | 10.07% | -1.83% | -0.749 | 0.670 | 0.791 | -0.95% |
| DIVIDEND | SCHD | diversified_us_equity | -0.03% | 2.71% | 0.82% | 12.55% | -1.18% | 0.004 | 0.091 | 0.084 | -0.42% |
| LOW_VOL | SPLV | diversified_us_equity | -0.30% | 2.13% | 1.64% | 14.94% | -1.89% | -1.043 | -0.318 | -0.326 | -0.78% |
| MOMENTUM | MTUM | diversified_us_equity | 4.02% | 1.48% | -10.83% | 42.16% | -12.49% | 0.732 | 0.769 | 2.159 | -8.97% |
| TECHNOLOGY | XLK | technology_and_growth | 2.67% | 0.26% | -6.90% | 32.80% | -8.62% | -1.016 | 0.849 | 2.192 | -8.94% |
| COMMUNICATIONS | XLC | technology_and_growth | -1.31% | -2.71% | 4.70% | 17.00% | -3.69% | -0.485 | 0.438 | 0.516 | -8.53% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | -1.23% | -1.57% | 0.39% | 17.42% | -3.45% | -0.205 | 0.737 | 1.051 | -8.07% |
| CONSUMER_STAPLES | XLP | consumer_defensive | -0.95% | 2.07% | 0.17% | 19.12% | -2.11% | -0.613 | -0.328 | -0.417 | -5.07% |
| HEALTHCARE | XLV | healthcare_and_biotech | -1.03% | 1.70% | 4.08% | 21.85% | -3.74% | -0.924 | -0.106 | -0.148 | -3.05% |
| FINANCIALS | XLF | financials | -0.37% | 0.08% | 3.93% | 13.55% | -2.08% | -0.428 | 0.169 | 0.170 | -1.23% |
| INDUSTRIALS | XLI | industrials_and_defense | -0.31% | 0.31% | -2.36% | 17.01% | -4.01% | -1.113 | 0.639 | 0.944 | -3.62% |
| ENERGY | XLE | energy | 2.64% | 5.76% | 3.11% | 19.51% | -3.03% | -0.982 | -0.368 | -0.686 | -4.69% |
| MATERIALS | XLB | materials_and_mining | 0.57% | 1.61% | -3.57% | 17.95% | -3.81% | -0.663 | 0.531 | 0.791 | -4.44% |
| UTILITIES | XLU | rate_sensitive_defensive | 1.68% | 2.55% | -0.28% | 16.56% | -3.10% | -0.542 | -0.079 | -0.109 | -2.48% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | -0.90% | 1.99% | -0.17% | 16.04% | -2.67% | -0.943 | -0.120 | -0.147 | -0.99% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | -0.79% | 0.26% | -1.30% | 4.60% | -1.74% | -0.871 | 0.521 | 0.199 | -3.44% |
| LONG_TREASURY | TLT | rates_and_duration | -1.28% | 0.03% | -3.19% | 8.56% | -4.23% | -0.703 | 0.395 | 0.268 | -6.40% |
| TIPS | TIP | rates_and_duration | -0.46% | 0.70% | -1.23% | 3.22% | -0.98% | -0.526 | 0.535 | 0.146 | -1.18% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | -0.83% | 0.13% | -2.16% | 4.79% | -2.42% | -0.015 | 0.556 | 0.225 | -2.71% |
| HIGH_YIELD_CREDIT | HYG | credit | -0.16% | 0.62% | -1.10% | 2.16% | -0.44% | -0.735 | 0.764 | 0.212 | -0.44% |
| AGGREGATE_BONDS | AGG | rates_and_duration | -0.63% | 0.41% | -1.56% | 3.70% | -1.47% | -0.562 | 0.560 | 0.177 | -2.16% |
| DEVELOPED_EX_US | VEA | international_equity | 1.13% | 0.51% | -3.57% | 19.14% | -4.37% | -0.780 | 0.839 | 1.341 | -2.62% |
| EMERGING_MARKETS | VWO | international_equity | 1.68% | -0.15% | -4.27% | 19.62% | -5.55% | -0.513 | 0.870 | 1.381 | -3.97% |
| EUROPE | VGK | international_equity | 0.56% | 0.95% | -0.41% | 14.12% | -2.53% | -1.001 | 0.719 | 0.991 | -0.98% |
| JAPAN | EWJ | international_equity | 1.88% | -0.42% | -4.98% | 25.13% | -6.74% | -0.440 | 0.792 | 1.347 | -4.93% |
| CHINA | MCHI | international_equity | 1.17% | -0.09% | 1.04% | 21.02% | -4.50% | -0.326 | 0.509 | 0.827 | -18.52% |
| INDIA | INDA | international_equity | -1.41% | -0.05% | -3.80% | 12.85% | -3.41% | -0.644 | 0.579 | 0.681 | -12.79% |
| GOLD | IAU | precious_metals | 2.90% | 2.83% | -4.60% | 23.46% | -5.08% | 0.052 | 0.685 | 1.263 | -23.51% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | 3.25% | 4.71% | 3.55% | 21.71% | -3.55% | 3.705 | -0.096 | -0.154 | -5.82% |
| SEMICONDUCTORS | SMH | technology_and_growth | 5.46% | 0.33% | -13.08% | 54.55% | -16.80% | -0.011 | 0.795 | 3.247 | -12.26% |
| SOFTWARE | IGV | technology_and_growth | -4.07% | -4.26% | 6.19% | 26.86% | -6.09% | -1.134 | 0.341 | 0.924 | -24.41% |
| BROAD_AI_TECH | AIQ | technology_and_growth | 2.45% | -0.62% | -10.30% | 37.94% | -12.51% | -0.372 | 0.834 | 2.550 | -14.26% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | 2.58% | -0.98% | -7.95% | 33.62% | -12.16% | -0.886 | 0.856 | 2.542 | -17.16% |
| CYBERSECURITY | CIBR | technology_and_growth | -3.28% | -3.06% | 10.07% | 27.71% | -5.70% | -0.093 | 0.423 | 1.075 | -5.70% |
| SOLAR | TAN | clean_energy | -0.33% | -2.75% | -10.09% | 37.30% | -13.78% | -1.407 | 0.741 | 2.613 | -27.34% |
| METALS_MINING | XME | materials_and_mining | 5.24% | 1.27% | -11.83% | 33.84% | -15.17% | -0.227 | 0.701 | 2.225 | -22.03% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | -0.31% | 0.85% | 0.20% | 9.80% | -1.30% | -0.892 | 0.709 | 0.587 | -1.10% |
| BIOTECH | XBI | healthcare_and_biotech | -1.39% | -1.65% | 5.70% | 28.47% | -8.12% | -0.087 | 0.362 | 0.858 | -7.41% |
| REGIONAL_BANKS | KRE | financials | -1.42% | 0.74% | 3.86% | 20.23% | -3.73% | 0.156 | 0.145 | 0.230 | -2.98% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | 0.16% | -1.27% | -1.01% | 18.51% | -8.58% | -0.803 | 0.473 | 0.899 | -7.84% |
| CANADA | EWC | international_equity | -0.29% | 0.63% | 1.36% | 8.95% | -1.46% | 0.213 | 0.597 | 0.600 | -0.35% |
| UNITED_KINGDOM | EWU | international_equity | 0.64% | 1.99% | 0.96% | 13.80% | -1.93% | -0.643 | 0.479 | 0.620 | -1.57% |
| AUSTRALIA | EWA | international_equity | 0.38% | 1.19% | -0.17% | 12.84% | -2.64% | -0.445 | 0.598 | 0.837 | -3.29% |
| SOUTH_KOREA | EWY | international_equity | 4.85% | 0.28% | -23.03% | 76.61% | -25.79% | 0.336 | 0.757 | 4.576 | -22.25% |
| TAIWAN | EWT | international_equity | 4.47% | 0.19% | -9.51% | 43.40% | -13.98% | 0.628 | 0.797 | 2.614 | -8.83% |
| BRAZIL | EWZ | international_equity | 3.95% | 3.04% | 3.30% | 20.47% | -2.22% | -0.864 | 0.414 | 0.758 | -11.41% |
| MEXICO | EWW | international_equity | 2.13% | 2.73% | -2.15% | 17.41% | -2.98% | -0.781 | 0.619 | 0.964 | -4.17% |
| SOUTH_AFRICA | EZA | international_equity | 0.99% | -0.21% | -3.55% | 21.23% | -5.39% | -0.347 | 0.764 | 1.910 | -21.13% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | -0.67% | 0.26% | -1.49% | 4.19% | -1.57% | -0.685 | 0.570 | 0.211 | -2.18% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | -0.66% | 0.16% | -1.65% | 2.37% | -1.57% | -0.275 | 0.561 | 0.118 | -1.57% |
| EMERGING_MARKET_BONDS | EMB | credit | -0.46% | 0.31% | -1.68% | 3.95% | -1.38% | -1.114 | 0.734 | 0.325 | -1.38% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | -0.27% | 0.50% | -1.67% | 3.41% | -1.26% | -0.655 | 0.547 | 0.177 | -1.73% |
| SILVER | SLV | precious_metals | 6.18% | 4.26% | -12.77% | 46.24% | -14.46% | -0.757 | 0.652 | 2.546 | -48.94% |
| COPPER | CPER | non_energy_commodities | 3.51% | 2.59% | -1.86% | 26.00% | -6.44% | -0.721 | 0.715 | 1.625 | -3.33% |
| AGRICULTURE | DBA | non_energy_commodities | 1.40% | 1.87% | 3.59% | 14.68% | -1.52% | -0.952 | 0.013 | 0.014 | -1.74% |
| OIL | USO | energy | 6.23% | 9.47% | 6.31% | 48.18% | -8.36% | -0.580 | -0.289 | -1.126 | -13.91% |
| US_DOLLAR | UUP | currencies | 0.42% | 1.69% | -1.79% | 4.50% | -0.98% | -0.563 | -0.522 | -0.196 | -0.28% |
| EURO | FXE | currencies | -0.27% | 0.53% | -0.97% | 4.16% | -0.63% | -0.672 | 0.553 | 0.198 | -4.83% |
| YEN | FXY | currencies | -0.50% | 0.45% | -1.86% | 5.28% | -1.28% | 0.027 | 0.191 | 0.096 | -10.53% |
| BITCOIN_ETF | IBIT | crypto_assets | 2.72% | 2.42% | -0.55% | 36.03% | -8.79% | -0.476 | 0.480 | 1.423 | -47.62% |
| ETHEREUM_ETF | ETHA | crypto_assets | 4.39% | 0.98% | 9.78% | 50.22% | -10.11% | 0.401 | 0.579 | 2.379 | -60.32% |
