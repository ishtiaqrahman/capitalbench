# Full-Universe Horizon-Specific Decision Context

Profile: monthly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: tiingo_eod_adjusted_price_and_volume
- As-of date requested: 2026-08-06
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | 3.62% |
| spy_return_21s | 3.11% |
| rsp_return_5s | 1.49% |
| rsp_return_21s | 3.01% |
| hyg_return_5s | 0.47% |
| hyg_return_21s | 0.23% |
| tlt_return_5s | 0.06% |
| tlt_return_21s | -1.79% |
| uup_return_5s | 0.18% |
| uup_return_21s | -0.60% |
| uso_return_5s | -6.75% |
| uso_return_21s | 5.94% |
| iau_return_5s | 3.32% |
| iau_return_21s | 4.08% |
| rsp_minus_spy_5s | -2.14% |
| rsp_minus_spy_21s | -0.10% |
| positive_asset_share_5s | 78.26% |
| positive_asset_share_21s | 72.46% |
| active_return_dispersion_5s |  |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_5s | active_return_21s | prior_105s_active_return | volatility_63s | max_drawdown_63s | volume_zscore_20v120 | corr_spy_252s | beta_spy_252s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | -3.11% | -9.21% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.08% | -2.81% | -7.72% | 0.21% | -0.01% | -0.246 | -0.101 | -0.002 | 0.00% |
| SP500 | SPY | diversified_us_equity | 3.62% | 0.00% | 0.00% | 14.00% | -4.49% | -0.812 | 1.000 | 1.000 | -0.36% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | 3.49% | -0.17% | 0.32% | 13.93% | -4.36% | -0.852 | 0.995 | 1.012 | -0.46% |
| NASDAQ100 | QQQ | technology_and_growth | 4.55% | -2.66% | 8.52% | 26.19% | -11.22% | -0.719 | 0.931 | 1.415 | -4.12% |
| LARGE_GROWTH | IWF | technology_and_growth | 5.17% | -1.71% | -1.69% | 21.00% | -11.36% | -0.762 | 0.937 | 1.283 | -4.01% |
| LARGE_VALUE | IWD | diversified_us_equity | 2.16% | 1.35% | 1.69% | 11.60% | -2.40% | -0.636 | 0.803 | 0.702 | -0.20% |
| MID_CAP | IJH | diversified_us_equity | 1.86% | -0.40% | -1.78% | 14.41% | -4.25% | -0.896 | 0.802 | 0.980 | -0.94% |
| SMALL_CAP | IWM | diversified_us_equity | 1.93% | -1.48% | 3.91% | 18.40% | -4.81% | -1.062 | 0.814 | 1.221 | -1.15% |
| SMALL_VALUE | IWN | diversified_us_equity | 0.92% | -0.28% | 1.53% | 14.89% | -4.01% | -0.455 | 0.727 | 0.973 | -1.38% |
| DIVIDEND | SCHD | diversified_us_equity | 0.87% | 1.10% | -3.20% | 11.65% | -2.95% | 0.072 | 0.291 | 0.250 | -0.56% |
| LOW_VOL | SPLV | diversified_us_equity | -0.16% | -2.39% | -6.51% | 13.22% | -3.75% | -0.775 | 0.017 | 0.014 | -2.19% |
| MOMENTUM | MTUM | diversified_us_equity | 3.15% | -5.23% | 18.49% | 39.14% | -17.99% | 1.304 | 0.780 | 1.562 | -10.73% |
| TECHNOLOGY | XLK | technology_and_growth | 5.46% | -0.94% | 22.44% | 35.89% | -15.86% | -0.974 | 0.859 | 1.729 | -6.39% |
| COMMUNICATIONS | XLC | technology_and_growth | 4.32% | -1.54% | -14.95% | 18.91% | -9.98% | -0.293 | 0.584 | 0.676 | -6.87% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | 5.08% | -0.68% | -12.82% | 21.85% | -10.72% | -0.471 | 0.778 | 1.174 | -4.78% |
| CONSUMER_STAPLES | XLP | consumer_defensive | -0.42% | -2.25% | -10.97% | 17.16% | -4.95% | -0.787 | -0.066 | -0.073 | -4.25% |
| HEALTHCARE | XLV | healthcare_and_biotech | 0.57% | -1.78% | -4.30% | 18.42% | -3.74% | -0.587 | 0.222 | 0.269 | -1.68% |
| FINANCIALS | XLF | financials | 1.42% | 2.06% | -6.46% | 13.66% | -2.08% | -0.725 | 0.550 | 0.626 | -0.33% |
| INDUSTRIALS | XLI | industrials_and_defense | 3.57% | -0.70% | -2.14% | 19.12% | -4.80% | -1.001 | 0.720 | 0.953 | -0.88% |
| ENERGY | XLE | energy | -1.36% | 1.50% | -2.53% | 23.24% | -13.22% | -0.867 | -0.151 | -0.248 | -6.37% |
| MATERIALS | XLB | materials_and_mining | 1.03% | 0.90% | -11.75% | 20.52% | -6.43% | -0.624 | 0.535 | 0.738 | -1.91% |
| UTILITIES | XLU | rate_sensitive_defensive | -2.87% | -7.47% | -2.51% | 16.35% | -6.29% | -0.654 | 0.119 | 0.138 | -7.90% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | -1.08% | -1.61% | -1.08% | 15.83% | -3.38% | -0.716 | 0.229 | 0.251 | -2.61% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | 0.06% | -3.37% | -9.70% | 5.00% | -2.00% | -0.919 | 0.284 | 0.101 | -3.26% |
| LONG_TREASURY | TLT | rates_and_duration | 0.06% | -4.89% | -9.89% | 9.32% | -5.60% | -0.463 | 0.229 | 0.165 | -7.06% |
| TIPS | TIP | rates_and_duration | -0.08% | -3.47% | -8.59% | 3.45% | -1.53% | -0.493 | 0.271 | 0.070 | -1.28% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | 0.38% | -3.90% | -9.45% | 5.34% | -2.83% | -0.308 | 0.477 | 0.195 | -2.58% |
| HIGH_YIELD_CREDIT | HYG | credit | 0.47% | -2.87% | -7.93% | 3.56% | -1.01% | -0.627 | 0.779 | 0.233 | -0.11% |
| AGGREGATE_BONDS | AGG | rates_and_duration | 0.15% | -3.38% | -9.17% | 4.12% | -1.71% | -0.211 | 0.395 | 0.114 | -1.97% |
| DEVELOPED_EX_US | VEA | international_equity | 1.45% | -0.58% | -3.17% | 20.16% | -4.85% | -0.930 | 0.804 | 1.078 | -0.37% |
| EMERGING_MARKETS | VWO | international_equity | 3.04% | -1.77% | -4.19% | 20.29% | -7.05% | -0.598 | 0.809 | 1.108 | -2.09% |
| EUROPE | VGK | international_equity | 0.92% | 1.03% | -7.14% | 16.39% | -3.86% | -0.827 | 0.745 | 0.917 | -0.02% |
| JAPAN | EWJ | international_equity | 1.99% | -0.29% | -2.87% | 23.00% | -7.86% | -0.911 | 0.721 | 1.174 | -1.88% |
| CHINA | MCHI | international_equity | 0.73% | 2.67% | -21.00% | 20.16% | -15.02% | -0.536 | 0.548 | 0.873 | -14.96% |
| INDIA | INDA | international_equity | 0.85% | -0.09% | -18.17% | 15.35% | -5.64% | -0.514 | 0.537 | 0.633 | -9.35% |
| GOLD | IAU | precious_metals | 3.32% | 0.97% | -26.62% | 24.33% | -16.01% | -0.546 | 0.311 | 0.680 | -21.36% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | -1.54% | 0.56% | 6.53% | 21.98% | -16.55% | 0.180 | -0.174 | -0.267 | -8.88% |
| SEMICONDUCTORS | SMH | technology_and_growth | 6.05% | -6.74% | 46.02% | 55.03% | -24.62% | 0.712 | 0.785 | 2.363 | -14.57% |
| SOFTWARE | IGV | technology_and_growth | 6.55% | 4.40% | 1.12% | 34.66% | -21.29% | -0.897 | 0.509 | 1.170 | -15.58% |
| BROAD_AI_TECH | AIQ | technology_and_growth | 5.55% | -4.10% | 17.50% | 40.70% | -20.19% | -0.237 | 0.848 | 1.901 | -11.68% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | 8.09% | -3.60% | -5.53% | 39.14% | -23.82% | -0.723 | 0.801 | 2.177 | -14.34% |
| CYBERSECURITY | CIBR | technology_and_growth | 7.08% | 2.05% | 28.92% | 33.26% | -11.74% | -0.468 | 0.540 | 1.103 | -1.58% |
| SOLAR | TAN | clean_energy | 2.83% | -8.45% | -16.02% | 47.13% | -35.51% | -0.303 | 0.602 | 1.859 | -30.68% |
| METALS_MINING | XME | materials_and_mining | 8.33% | 5.14% | -25.29% | 41.38% | -26.49% | -0.437 | 0.602 | 1.745 | -16.87% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | 1.49% | -0.10% | -2.41% | 11.13% | -2.04% | -0.833 | 0.767 | 0.699 | -0.75% |
| BIOTECH | XBI | healthcare_and_biotech | 2.01% | -8.30% | 20.99% | 30.68% | -10.51% | -0.281 | 0.481 | 1.013 | -5.95% |
| REGIONAL_BANKS | KRE | financials | 0.78% | 1.19% | -6.67% | 19.83% | -5.29% | -0.677 | 0.437 | 0.775 | -1.84% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | 4.98% | 1.22% | -3.97% | 25.09% | -8.58% | -0.378 | 0.572 | 1.009 | -0.91% |
| CANADA | EWC | international_equity | 1.52% | 1.60% | -3.33% | 12.05% | -3.20% | -0.563 | 0.670 | 0.745 | -0.13% |
| UNITED_KINGDOM | EWU | international_equity | -0.78% | 0.79% | -8.97% | 15.61% | -3.94% | -0.664 | 0.605 | 0.703 | -0.78% |
| AUSTRALIA | EWA | international_equity | 1.14% | 4.15% | -8.61% | 17.43% | -6.84% | -0.882 | 0.677 | 0.928 | 0.00% |
| SOUTH_KOREA | EWY | international_equity | 1.81% | -13.29% | 42.73% | 82.62% | -34.21% | 0.541 | 0.645 | 2.738 | -25.13% |
| TAIWAN | EWT | international_equity | 8.49% | -4.95% | 43.25% | 44.67% | -19.83% | 0.071 | 0.759 | 1.833 | -8.56% |
| BRAZIL | EWZ | international_equity | -1.97% | 0.96% | -15.27% | 23.32% | -15.56% | -0.924 | 0.508 | 0.991 | -13.37% |
| MEXICO | EWW | international_equity | -0.62% | -0.54% | -11.04% | 19.19% | -7.30% | -0.590 | 0.545 | 0.931 | -4.28% |
| SOUTH_AFRICA | EZA | international_equity | 4.32% | 3.58% | -22.67% | 30.40% | -14.23% | -0.540 | 0.630 | 1.588 | -16.30% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | 0.07% | -3.47% | -9.05% | 4.94% | -1.93% | -0.326 | 0.393 | 0.134 | -1.96% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | 0.18% | -4.01% | -8.53% | 3.11% | -2.15% | 0.597 | 0.372 | 0.085 | -1.51% |
| EMERGING_MARKET_BONDS | EMB | credit | 0.61% | -3.55% | -7.45% | 5.65% | -2.10% | -0.646 | 0.683 | 0.302 | -1.09% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | 0.27% | -2.73% | -9.42% | 4.10% | -1.44% | -0.723 | 0.454 | 0.125 | -1.31% |
| SILVER | SLV | precious_metals | 4.39% | 2.61% | -42.49% | 48.97% | -36.50% | -0.597 | 0.356 | 1.700 | -47.11% |
| COPPER | CPER | non_energy_commodities | 3.61% | 6.85% | -7.06% | 28.25% | -10.57% | -0.547 | 0.556 | 1.210 | -0.22% |
| AGRICULTURE | DBA | non_energy_commodities | -0.18% | -3.79% | -1.78% | 14.00% | -8.67% | -0.419 | 0.080 | 0.069 | -4.52% |
| OIL | USO | energy | -6.75% | 2.83% | 34.87% | 53.20% | -32.49% | -0.531 | -0.335 | -1.237 | -22.29% |
| US_DOLLAR | UUP | currencies | 0.18% | -3.71% | -4.21% | 4.96% | -1.78% | -0.196 | -0.316 | -0.142 | -1.43% |
| EURO | FXE | currencies | -0.08% | -2.22% | -12.11% | 4.81% | -3.57% | -0.934 | 0.300 | 0.135 | -3.88% |
| YEN | FXY | currencies | 0.54% | -0.57% | -12.84% | 7.26% | -4.58% | 1.112 | 0.181 | 0.114 | -7.85% |
| BITCOIN_ETF | IBIT | crypto_assets | -0.57% | 0.47% | -24.46% | 36.69% | -28.36% | -0.614 | 0.503 | 1.736 | -48.81% |
| ETHEREUM_ETF | ETHA | crypto_assets | -0.76% | 6.73% | -28.97% | 53.03% | -33.75% | -0.349 | 0.534 | 2.783 | -60.64% |
