# Full-Universe Horizon-Specific Decision Context

Profile: monthly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: tiingo_eod_adjusted_price_and_volume
- As-of date requested: 2026-07-28
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | -0.99% |
| spy_return_21s | 1.63% |
| rsp_return_5s | 2.32% |
| rsp_return_21s | 3.51% |
| hyg_return_5s | -0.29% |
| hyg_return_21s | -0.05% |
| tlt_return_5s | 0.69% |
| tlt_return_21s | -3.21% |
| uup_return_5s | 0.35% |
| uup_return_21s | 0.42% |
| uso_return_5s | -6.49% |
| uso_return_21s | 14.23% |
| iau_return_5s | -1.46% |
| iau_return_21s | -1.12% |
| rsp_minus_spy_5s | 3.31% |
| rsp_minus_spy_21s | 1.88% |
| positive_asset_share_5s | 43.48% |
| positive_asset_share_21s | 50.72% |
| active_return_dispersion_5s |  |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_5s | active_return_21s | prior_105s_active_return | volatility_63s | max_drawdown_63s | volume_zscore_20v120 | corr_spy_252s | beta_spy_252s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | -1.63% | -5.79% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.08% | -1.34% | -4.30% | 0.21% | -0.01% | -0.212 | -0.112 | -0.002 | 0.00% |
| SP500 | SPY | diversified_us_equity | -0.99% | 0.00% | 0.00% | 12.96% | -4.49% | -1.031 | 1.000 | 1.000 | -2.21% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | -0.94% | -0.59% | 0.75% | 12.93% | -4.36% | -0.850 | 0.995 | 1.013 | -1.95% |
| NASDAQ100 | QQQ | technology_and_growth | -4.72% | -6.02% | 7.43% | 24.44% | -9.37% | -0.948 | 0.929 | 1.392 | -9.37% |
| LARGE_GROWTH | IWF | technology_and_growth | -4.00% | -3.78% | -4.56% | 18.71% | -9.47% | -0.713 | 0.934 | 1.260 | -9.47% |
| LARGE_VALUE | IWD | diversified_us_equity | 1.86% | 2.19% | 5.77% | 12.00% | -2.40% | -0.493 | 0.805 | 0.719 | 0.00% |
| MID_CAP | IJH | diversified_us_equity | 0.41% | -1.88% | 4.23% | 14.55% | -4.25% | -1.017 | 0.801 | 0.989 | -1.40% |
| SMALL_CAP | IWM | diversified_us_equity | -1.07% | -3.78% | 8.25% | 18.38% | -4.81% | -1.252 | 0.815 | 1.241 | -2.36% |
| SMALL_VALUE | IWN | diversified_us_equity | 0.54% | -0.42% | 8.54% | 15.42% | -4.01% | -0.652 | 0.736 | 1.010 | -0.03% |
| DIVIDEND | SCHD | diversified_us_equity | 3.26% | 3.98% | 5.99% | 12.14% | -2.95% | -0.424 | 0.313 | 0.275 | 0.00% |
| LOW_VOL | SPLV | diversified_us_equity | 2.96% | 1.48% | -1.14% | 13.08% | -4.09% | -0.929 | 0.044 | 0.037 | 0.00% |
| MOMENTUM | MTUM | diversified_us_equity | -7.05% | -11.89% | 21.23% | 37.23% | -15.32% | 1.425 | 0.769 | 1.500 | -15.32% |
| TECHNOLOGY | XLK | technology_and_growth | -5.36% | -7.16% | 18.48% | 33.17% | -13.58% | -1.045 | 0.857 | 1.682 | -13.58% |
| COMMUNICATIONS | XLC | technology_and_growth | -0.33% | 1.66% | -15.11% | 17.17% | -9.98% | -0.020 | 0.626 | 0.716 | -8.14% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | -2.08% | -3.28% | -11.92% | 20.85% | -10.72% | -0.396 | 0.794 | 1.205 | -9.31% |
| CONSUMER_STAPLES | XLP | consumer_defensive | 3.57% | 1.15% | -2.17% | 16.98% | -4.95% | -0.808 | -0.044 | -0.049 | -2.06% |
| HEALTHCARE | XLV | healthcare_and_biotech | 4.37% | 2.69% | -3.52% | 18.36% | -3.74% | -0.629 | 0.253 | 0.316 | 0.00% |
| FINANCIALS | XLF | financials | 2.66% | 5.89% | -4.63% | 13.17% | -2.42% | -0.731 | 0.554 | 0.642 | 0.00% |
| INDUSTRIALS | XLI | industrials_and_defense | 2.14% | -0.92% | 5.01% | 19.00% | -4.60% | -1.155 | 0.711 | 0.931 | -1.65% |
| ENERGY | XLE | energy | -1.59% | 5.30% | 5.08% | 24.57% | -13.22% | -0.891 | -0.126 | -0.209 | -7.32% |
| MATERIALS | XLB | materials_and_mining | 4.47% | -0.19% | -1.82% | 20.10% | -6.43% | -0.659 | 0.546 | 0.762 | -1.59% |
| UTILITIES | XLU | rate_sensitive_defensive | 1.34% | -3.10% | 3.41% | 17.16% | -8.00% | -0.852 | 0.131 | 0.156 | -3.36% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | 1.79% | 0.07% | 5.65% | 16.15% | -3.38% | -0.809 | 0.252 | 0.286 | 0.00% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | 0.27% | -2.85% | -5.29% | 5.01% | -2.02% | -0.926 | 0.220 | 0.081 | -2.96% |
| LONG_TREASURY | TLT | rates_and_duration | 0.69% | -4.84% | -5.04% | 8.89% | -4.54% | -0.871 | 0.174 | 0.128 | -5.50% |
| TIPS | TIP | rates_and_duration | -0.20% | -2.53% | -4.75% | 3.55% | -1.53% | -0.693 | 0.245 | 0.067 | -1.28% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | -0.02% | -3.72% | -5.20% | 5.30% | -2.82% | -0.515 | 0.419 | 0.175 | -2.57% |
| HIGH_YIELD_CREDIT | HYG | credit | -0.29% | -1.68% | -4.97% | 3.65% | -1.01% | -0.744 | 0.770 | 0.233 | -0.56% |
| AGGREGATE_BONDS | AGG | rates_and_duration | 0.18% | -2.73% | -5.07% | 4.14% | -1.71% | -0.229 | 0.328 | 0.098 | -1.82% |
| DEVELOPED_EX_US | VEA | international_equity | -1.23% | -2.99% | 1.73% | 20.65% | -4.85% | -0.677 | 0.798 | 1.072 | -3.85% |
| EMERGING_MARKETS | VWO | international_equity | -1.90% | -3.06% | -2.78% | 20.15% | -5.72% | -0.484 | 0.798 | 1.096 | -5.72% |
| EUROPE | VGK | international_equity | 0.53% | 0.78% | -4.39% | 17.97% | -3.86% | -0.991 | 0.742 | 0.928 | -0.82% |
| JAPAN | EWJ | international_equity | -3.14% | -4.83% | 4.44% | 22.38% | -7.36% | -0.807 | 0.713 | 1.157 | -7.36% |
| CHINA | MCHI | international_equity | 0.76% | 6.16% | -24.70% | 20.85% | -15.02% | -0.282 | 0.572 | 0.929 | -17.24% |
| INDIA | INDA | international_equity | 1.23% | -1.99% | -9.45% | 15.85% | -5.64% | -0.644 | 0.515 | 0.616 | -10.69% |
| GOLD | IAU | precious_metals | -1.46% | -2.75% | -25.36% | 24.03% | -16.01% | -0.594 | 0.309 | 0.680 | -25.47% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | -3.34% | 5.87% | 4.26% | 22.00% | -16.55% | 0.156 | -0.119 | -0.182 | -9.78% |
| SEMICONDUCTORS | SMH | technology_and_growth | -9.33% | -15.04% | 47.56% | 53.07% | -20.83% | 0.966 | 0.774 | 2.301 | -20.83% |
| SOFTWARE | IGV | technology_and_growth | -0.04% | 2.43% | -16.52% | 33.45% | -21.29% | -0.638 | 0.508 | 1.167 | -22.07% |
| BROAD_AI_TECH | AIQ | technology_and_growth | -6.16% | -10.99% | 14.65% | 39.08% | -18.39% | -0.270 | 0.842 | 1.865 | -18.39% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | -5.42% | -9.73% | -8.85% | 38.58% | -21.02% | -1.082 | 0.791 | 2.142 | -21.02% |
| CYBERSECURITY | CIBR | technology_and_growth | -1.44% | 2.96% | 12.92% | 32.25% | -11.74% | -0.243 | 0.532 | 1.087 | -5.75% |
| SOLAR | TAN | clean_energy | -8.63% | -15.26% | -2.64% | 45.77% | -33.59% | -0.744 | 0.584 | 1.793 | -33.59% |
| METALS_MINING | XME | materials_and_mining | -0.16% | -7.71% | -20.08% | 39.76% | -26.37% | -0.472 | 0.586 | 1.688 | -23.58% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | 2.32% | 1.88% | 0.62% | 11.09% | -2.04% | -0.903 | 0.775 | 0.718 | 0.00% |
| BIOTECH | XBI | healthcare_and_biotech | -3.06% | -5.23% | 15.84% | 30.41% | -8.83% | -0.227 | 0.476 | 1.003 | -8.83% |
| REGIONAL_BANKS | KRE | financials | 1.07% | 0.53% | 6.14% | 20.25% | -5.29% | -0.657 | 0.449 | 0.812 | -1.45% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | 6.63% | 1.83% | -4.20% | 24.97% | -8.58% | -0.437 | 0.555 | 0.971 | -2.31% |
| CANADA | EWC | international_equity | 1.34% | 1.90% | -1.52% | 13.22% | -3.20% | -0.672 | 0.680 | 0.769 | 0.00% |
| UNITED_KINGDOM | EWU | international_equity | 2.25% | 2.87% | -4.51% | 16.96% | -3.94% | -0.498 | 0.609 | 0.719 | -0.35% |
| AUSTRALIA | EWA | international_equity | 2.23% | 3.20% | -3.09% | 18.59% | -6.84% | -0.885 | 0.674 | 0.923 | -1.73% |
| SOUTH_KOREA | EWY | international_equity | -12.41% | -24.86% | 62.36% | 78.98% | -30.91% | 0.375 | 0.632 | 2.631 | -30.91% |
| TAIWAN | EWT | international_equity | -6.59% | -10.25% | 41.20% | 42.02% | -15.76% | 0.006 | 0.735 | 1.733 | -15.76% |
| BRAZIL | EWZ | international_equity | 1.21% | 2.35% | -10.19% | 23.81% | -15.56% | -1.091 | 0.507 | 0.998 | -12.79% |
| MEXICO | EWW | international_equity | 1.24% | 0.24% | -6.09% | 20.36% | -7.30% | -0.913 | 0.530 | 0.920 | -4.10% |
| SOUTH_AFRICA | EZA | international_equity | -0.48% | -3.26% | -22.64% | 32.89% | -14.23% | -0.557 | 0.627 | 1.600 | -22.44% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | 0.28% | -2.60% | -4.90% | 4.86% | -1.93% | -0.632 | 0.327 | 0.114 | -1.63% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | -0.16% | -2.85% | -4.52% | 3.08% | -2.15% | 0.270 | 0.324 | 0.076 | -1.46% |
| EMERGING_MARKET_BONDS | EMB | credit | -0.20% | -2.62% | -3.89% | 5.78% | -2.10% | -0.667 | 0.662 | 0.294 | -1.27% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | 0.33% | -2.47% | -4.69% | 4.18% | -1.44% | -0.533 | 0.417 | 0.115 | -1.34% |
| SILVER | SLV | precious_metals | -2.60% | -4.59% | -51.62% | 50.49% | -36.50% | -0.670 | 0.355 | 1.715 | -51.04% |
| COPPER | CPER | non_energy_commodities | -3.04% | 1.05% | -3.63% | 29.32% | -10.57% | -0.700 | 0.462 | 1.250 | -5.59% |
| AGRICULTURE | DBA | non_energy_commodities | -1.10% | 2.25% | -1.76% | 14.12% | -8.67% | -0.418 | 0.075 | 0.066 | -3.10% |
| OIL | USO | energy | -6.49% | 12.60% | 37.75% | 54.33% | -32.49% | -0.547 | -0.290 | -1.066 | -21.23% |
| US_DOLLAR | UUP | currencies | 0.35% | -1.21% | 0.48% | 4.87% | -0.98% | -0.319 | -0.280 | -0.131 | -0.07% |
| EURO | FXE | currencies | -0.11% | -1.54% | -9.73% | 4.61% | -3.56% | -0.815 | 0.261 | 0.126 | -5.03% |
| YEN | FXY | currencies | -0.39% | -2.88% | -10.79% | 6.50% | -4.58% | -0.055 | 0.112 | 0.070 | -10.86% |
| BITCOIN_ETF | IBIT | crypto_assets | -4.06% | 5.14% | -37.62% | 37.01% | -28.36% | -0.569 | 0.516 | 1.804 | -49.31% |
| ETHEREUM_ETF | ETHA | crypto_assets | -0.28% | 20.24% | -51.50% | 53.06% | -34.41% | -0.398 | 0.555 | 2.954 | -60.40% |
