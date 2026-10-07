# Full-Universe Horizon-Specific Decision Context

Profile: weekly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: tiingo_eod_history_through_2026-09-25; repository_daily_price_snapshots_2026-09-28_to_2026-10-06_(tiingo_eod_or_yahoo_chart_adjclose); yahoo_chart_reported_volume_2026-09-28_to_2026-10-06
- As-of date requested: 2026-10-06
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | 1.95% |
| spy_return_21s | 1.41% |
| rsp_return_5s | 1.35% |
| rsp_return_21s | -2.68% |
| hyg_return_5s | -0.12% |
| hyg_return_21s | -2.39% |
| tlt_return_5s | -1.21% |
| tlt_return_21s | -6.00% |
| uup_return_5s | 0.52% |
| uup_return_21s | 2.92% |
| uso_return_5s | 1.09% |
| uso_return_21s | 2.08% |
| iau_return_5s | -0.19% |
| iau_return_21s | -6.02% |
| rsp_minus_spy_5s | -0.60% |
| rsp_minus_spy_21s | -4.09% |
| positive_asset_share_5s | 62.32% |
| positive_asset_share_21s | 31.88% |
| active_return_dispersion_5s | 24.11% |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_3s | active_return_5s | prior_16s_active_return | volatility_21s | max_drawdown_21s | volume_zscore_5v60 | corr_spy_63s | beta_spy_63s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | -1.95% | 0.53% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.04% | -2.17% | 0.75% | 0.94% | -0.26% | 0.957 | 0.049 | 0.003 | -0.22% |
| SP500 | SPY | diversified_us_equity | 1.98% | 0.00% | 0.00% | 10.41% | -2.10% | 0.359 | 1.000 | 1.000 | 0.00% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | 1.96% | -0.01% | -0.65% | 10.71% | -2.23% | 1.068 | 0.995 | 1.010 | -0.46% |
| NASDAQ100 | QQQ | technology_and_growth | 2.38% | 1.00% | 3.27% | 15.10% | -2.01% | -0.534 | 0.905 | 1.531 | 0.00% |
| LARGE_GROWTH | IWF | technology_and_growth | 2.75% | 1.16% | 2.15% | 14.03% | -2.31% | 0.156 | 0.929 | 1.501 | 0.00% |
| LARGE_VALUE | IWD | diversified_us_equity | 1.41% | -0.84% | -2.47% | 8.71% | -3.41% | 0.643 | 0.710 | 0.562 | -2.59% |
| MID_CAP | IJH | diversified_us_equity | 1.79% | 0.30% | -3.76% | 10.46% | -4.85% | 1.508 | 0.789 | 0.831 | -5.65% |
| SMALL_CAP | IWM | diversified_us_equity | 0.83% | -1.11% | -4.96% | 11.33% | -5.87% | 1.086 | 0.782 | 0.932 | -7.54% |
| SMALL_VALUE | IWN | diversified_us_equity | 0.86% | -1.30% | -5.15% | 9.81% | -6.37% | 1.592 | 0.666 | 0.651 | -6.24% |
| DIVIDEND | SCHD | diversified_us_equity | 0.58% | -1.95% | -4.32% | 9.19% | -5.77% | -0.159 | 0.195 | 0.195 | -5.96% |
| LOW_VOL | SPLV | diversified_us_equity | 1.57% | -1.19% | -4.03% | 7.50% | -5.47% | 0.424 | 0.038 | 0.033 | -7.65% |
| MOMENTUM | MTUM | diversified_us_equity | 1.11% | 0.42% | 4.70% | 17.58% | -3.10% | -0.295 | 0.608 | 1.467 | -5.83% |
| TECHNOLOGY | XLK | technology_and_growth | 2.12% | 1.91% | 4.50% | 17.30% | -2.20% | 0.358 | 0.786 | 1.811 | 0.00% |
| COMMUNICATIONS | XLC | technology_and_growth | 1.56% | -1.79% | 0.35% | 21.02% | -4.19% | 0.817 | 0.424 | 0.787 | -6.18% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | 2.67% | 0.41% | -4.27% | 14.57% | -5.10% | 0.098 | 0.674 | 1.160 | -9.73% |
| CONSUMER_STAPLES | XLP | consumer_defensive | 1.83% | -2.01% | -2.06% | 11.84% | -4.40% | 0.240 | -0.021 | -0.030 | -7.37% |
| HEALTHCARE | XLV | healthcare_and_biotech | 0.54% | -4.08% | 0.49% | 13.89% | -3.55% | 0.101 | 0.017 | 0.025 | -4.53% |
| FINANCIALS | XLF | financials | 1.03% | -1.95% | -6.18% | 11.90% | -7.77% | 0.339 | 0.558 | 0.607 | -7.45% |
| INDUSTRIALS | XLI | industrials_and_defense | 1.74% | -0.50% | -2.71% | 12.93% | -4.47% | 0.156 | 0.616 | 0.797 | -7.76% |
| ENERGY | XLE | energy | 1.67% | 1.64% | -2.82% | 19.75% | -6.15% | 0.067 | -0.317 | -0.596 | -2.72% |
| MATERIALS | XLB | materials_and_mining | 2.45% | -0.67% | -5.41% | 13.87% | -7.01% | 1.915 | 0.393 | 0.570 | -6.92% |
| UTILITIES | XLU | rate_sensitive_defensive | 3.73% | 1.70% | -6.61% | 17.87% | -9.00% | 5.390 | 0.137 | 0.185 | -11.97% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | 1.03% | -2.53% | -4.58% | 11.00% | -6.65% | 2.233 | 0.219 | 0.241 | -9.93% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | -0.20% | -2.31% | -2.50% | 6.09% | -3.61% | 0.860 | 0.527 | 0.243 | -6.91% |
| LONG_TREASURY | TLT | rates_and_duration | -0.55% | -3.16% | -4.31% | 10.07% | -6.20% | 1.630 | 0.472 | 0.417 | -12.62% |
| TIPS | TIP | rates_and_duration | -0.12% | -1.78% | -2.24% | 4.83% | -2.87% | 0.584 | 0.307 | 0.105 | -3.77% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | 0.11% | -2.21% | -2.38% | 6.84% | -3.46% | 1.507 | 0.573 | 0.302 | -6.05% |
| HIGH_YIELD_CREDIT | HYG | credit | 0.48% | -2.06% | -1.74% | 4.24% | -2.85% | 1.727 | 0.693 | 0.213 | -2.78% |
| AGGREGATE_BONDS | AGG | rates_and_duration | -0.06% | -2.20% | -1.94% | 5.09% | -2.96% | 2.265 | 0.541 | 0.213 | -4.73% |
| DEVELOPED_EX_US | VEA | international_equity | 1.28% | -2.05% | -2.73% | 14.71% | -4.58% | 0.752 | 0.774 | 1.046 | -3.39% |
| EMERGING_MARKETS | VWO | international_equity | 2.69% | -0.27% | -2.25% | 15.21% | -3.74% | 0.064 | 0.811 | 1.056 | -1.15% |
| EUROPE | VGK | international_equity | 1.28% | -3.39% | -3.47% | 13.19% | -6.58% | 1.340 | 0.712 | 0.774 | -6.86% |
| JAPAN | EWJ | international_equity | 1.99% | 0.96% | -1.27% | 17.97% | -3.01% | 0.587 | 0.711 | 1.280 | 0.00% |
| CHINA | MCHI | international_equity | 0.21% | -1.72% | -4.59% | 17.11% | -6.68% | 0.121 | 0.328 | 0.473 | -20.15% |
| INDIA | INDA | international_equity | 0.80% | -2.40% | -5.42% | 13.63% | -7.11% | -0.238 | 0.607 | 0.670 | -15.48% |
| GOLD | IAU | precious_metals | -0.13% | -2.14% | -5.31% | 20.70% | -7.06% | -0.626 | 0.371 | 0.812 | -22.84% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | -0.51% | -0.01% | 0.95% | 19.74% | -5.02% | 0.092 | -0.496 | -0.956 | -3.18% |
| SEMICONDUCTORS | SMH | technology_and_growth | 2.38% | 2.27% | 7.57% | 29.72% | -5.71% | -0.666 | 0.673 | 2.319 | -5.44% |
| SOFTWARE | IGV | technology_and_growth | 2.71% | 3.70% | 1.15% | 25.14% | -3.22% | -0.884 | 0.475 | 1.386 | -5.04% |
| BROAD_AI_TECH | AIQ | technology_and_growth | 2.10% | 1.13% | 1.67% | 19.22% | -3.01% | -0.139 | 0.817 | 1.942 | -4.40% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | 4.75% | 2.98% | -0.31% | 22.08% | -4.15% | 0.872 | 0.826 | 2.150 | -11.56% |
| CYBERSECURITY | CIBR | technology_and_growth | 4.19% | 4.09% | 8.34% | 27.61% | -2.94% | 1.551 | 0.412 | 1.228 | 0.00% |
| SOLAR | TAN | clean_energy | 3.09% | 0.29% | -9.06% | 34.01% | -12.48% | -0.481 | 0.686 | 2.164 | -39.94% |
| METALS_MINING | XME | materials_and_mining | 3.79% | 2.23% | -11.82% | 28.35% | -13.61% | -0.675 | 0.589 | 1.907 | -18.40% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | 1.59% | -0.60% | -3.45% | 9.62% | -4.66% | 1.223 | 0.670 | 0.592 | -4.33% |
| BIOTECH | XBI | healthcare_and_biotech | -2.34% | -5.72% | -3.74% | 27.38% | -7.88% | 0.773 | 0.328 | 0.871 | -11.00% |
| REGIONAL_BANKS | KRE | financials | 0.17% | -1.60% | -6.16% | 13.43% | -7.22% | 0.880 | 0.371 | 0.522 | -9.57% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | 0.11% | -2.45% | -6.59% | 13.17% | -8.15% | 0.401 | 0.464 | 0.827 | -17.66% |
| CANADA | EWC | international_equity | 1.54% | -1.52% | -4.48% | 11.37% | -6.06% | -0.082 | 0.647 | 0.694 | -5.52% |
| UNITED_KINGDOM | EWU | international_equity | 1.05% | -2.97% | -3.05% | 11.92% | -5.56% | 0.192 | 0.475 | 0.467 | -6.11% |
| AUSTRALIA | EWA | international_equity | 2.00% | -1.31% | -5.62% | 17.69% | -7.41% | 0.857 | 0.644 | 0.941 | -6.18% |
| SOUTH_KOREA | EWY | international_equity | 0.16% | -2.32% | -0.41% | 45.68% | -7.99% | -0.617 | 0.556 | 2.927 | -14.96% |
| TAIWAN | EWT | international_equity | 4.28% | 1.12% | 2.25% | 28.01% | -4.91% | -0.354 | 0.732 | 2.149 | -0.33% |
| BRAZIL | EWZ | international_equity | 15.78% | 15.96% | -3.14% | 48.31% | -6.22% | 7.493 | 0.310 | 0.948 | 0.00% |
| MEXICO | EWW | international_equity | 4.19% | -1.06% | -5.45% | 19.51% | -9.00% | 0.265 | 0.576 | 0.889 | -9.20% |
| SOUTH_AFRICA | EZA | international_equity | 1.27% | -3.78% | -8.95% | 24.40% | -12.26% | -0.609 | 0.576 | 1.409 | -20.33% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | -0.21% | -2.13% | -2.91% | 6.89% | -3.91% | 0.458 | 0.532 | 0.267 | -5.47% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | -0.32% | -1.21% | -3.07% | 6.16% | -3.60% | 2.154 | 0.418 | 0.166 | -5.57% |
| EMERGING_MARKET_BONDS | EMB | credit | 0.76% | -2.31% | -2.85% | 7.39% | -4.58% | 1.845 | 0.685 | 0.371 | -4.84% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | 0.13% | -1.97% | -0.71% | 4.04% | -1.39% | 2.484 | 0.641 | 0.220 | -3.20% |
| SILVER | SLV | precious_metals | 0.78% | -2.00% | -6.72% | 37.73% | -10.24% | -0.403 | 0.458 | 1.569 | -47.49% |
| COPPER | CPER | non_energy_commodities | 1.32% | -1.70% | 0.48% | 27.53% | -6.80% | -0.312 | 0.487 | 1.007 | -3.38% |
| AGRICULTURE | DBA | non_energy_commodities | 2.56% | 0.18% | -1.55% | 13.64% | -4.06% | -0.216 | 0.111 | 0.129 | -2.17% |
| OIL | USO | energy | -3.41% | -0.86% | 1.51% | 46.07% | -11.44% | -0.590 | -0.577 | -2.706 | -10.47% |
| US_DOLLAR | UUP | currencies | -0.21% | -1.43% | 2.92% | 4.61% | -0.36% | 0.953 | -0.304 | -0.144 | -0.31% |
| EURO | FXE | currencies | 0.25% | -2.66% | -1.79% | 4.43% | -3.48% | 1.541 | 0.248 | 0.105 | -5.96% |
| YEN | FXY | currencies | -0.07% | -2.53% | -0.15% | 8.72% | -3.38% | -0.673 | 0.387 | 0.349 | -5.39% |
| BITCOIN_ETF | IBIT | crypto_assets | 1.11% | 0.50% | 5.17% | 37.70% | -4.84% | -0.417 | 0.359 | 1.213 | -31.98% |
| ETHEREUM_ETF | ETHA | crypto_assets | 198.92% | 198.30% | 10.03% | 685.45% | -5.32% | -1.390 | 0.118 | 4.238 | 0.00% |
