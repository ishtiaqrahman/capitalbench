# Full-Universe Horizon-Specific Decision Context

Profile: monthly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: yahoo_chart_adjusted_close_and_reported_volume
- As-of date requested: 2026-07-16
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | -0.13% |
| spy_return_21s | -0.29% |
| rsp_return_5s | 0.73% |
| rsp_return_21s | 1.42% |
| hyg_return_5s | 0.06% |
| hyg_return_21s | 0.16% |
| tlt_return_5s | -0.33% |
| tlt_return_21s | -1.40% |
| uup_return_5s | -0.07% |
| uup_return_21s | 1.32% |
| uso_return_5s | 9.44% |
| uso_return_21s | -1.58% |
| iau_return_5s | -3.50% |
| iau_return_21s | -7.95% |
| rsp_minus_spy_5s | 0.86% |
| rsp_minus_spy_21s | 1.70% |
| positive_asset_share_5s | 44.93% |
| positive_asset_share_21s | 42.03% |
| active_return_dispersion_5s |  |

## Option Decision Context

| option_id | symbol | economic_exposure_cluster | return_5s | active_return_21s | prior_105s_active_return | volatility_63s | max_drawdown_63s | volume_zscore_20v120 | corr_spy_252s | beta_spy_252s | distance_52w_high |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | capital_preservation | 0.00% | 0.29% | -9.10% | 0.00% | 0.00% | 0.000 |  | 0.000 |  |
| SHORT_TREASURY | BIL | capital_preservation | 0.08% | 0.60% | -7.62% | 0.21% | -0.01% | -0.120 | -0.113 | -0.002 | 0.00% |
| SP500 | SPY | diversified_us_equity | -0.13% | 0.00% | 0.00% | 12.94% | -4.49% | -0.721 | 1.000 | 1.000 | -0.91% |
| TOTAL_US_MARKET | VTI | diversified_us_equity | -0.23% | 0.05% | 0.06% | 12.93% | -4.36% | -0.768 | 0.995 | 1.014 | -0.72% |
| NASDAQ100 | QQQ | technology_and_growth | -2.40% | -4.72% | 9.86% | 24.05% | -7.03% | -0.690 | 0.932 | 1.383 | -5.29% |
| LARGE_GROWTH | IWF | technology_and_growth | -1.70% | -2.25% | -4.37% | 18.60% | -8.21% | -0.603 | 0.935 | 1.254 | -5.80% |
| LARGE_VALUE | IWD | diversified_us_equity | 1.25% | 2.62% | 3.76% | 11.80% | -2.40% | -0.015 | 0.808 | 0.724 | 0.00% |
| MID_CAP | IJH | diversified_us_equity | 0.38% | 0.07% | 1.24% | 14.83% | -4.25% | -0.892 | 0.798 | 0.999 | -1.45% |
| SMALL_CAP | IWM | diversified_us_equity | -0.56% | 0.61% | 4.11% | 18.56% | -4.81% | -0.948 | 0.815 | 1.255 | -1.62% |
| SMALL_VALUE | IWN | diversified_us_equity | 2.13% | 3.45% | 4.88% | 15.64% | -4.01% | -0.395 | 0.730 | 1.016 | 0.00% |
| DIVIDEND | SCHD | diversified_us_equity | 2.42% | 2.35% | 5.88% | 11.90% | -2.95% | -0.285 | 0.313 | 0.274 | 0.00% |
| LOW_VOL | SPLV | diversified_us_equity | 1.91% | 4.18% | -5.26% | 13.37% | -4.16% | -0.631 | 0.044 | 0.037 | 0.00% |
| MOMENTUM | MTUM | diversified_us_equity | -5.54% | -8.77% | 20.02% | 35.67% | -12.11% | 1.498 | 0.790 | 1.512 | -12.11% |
| TECHNOLOGY | XLK | technology_and_growth | -4.22% | -7.04% | 22.00% | 33.01% | -10.89% | -0.719 | 0.863 | 1.684 | -10.33% |
| COMMUNICATIONS | XLC | technology_and_growth | 1.94% | 0.96% | -12.81% | 15.22% | -11.12% | 0.418 | 0.628 | 0.690 | -5.64% |
| CONSUMER_DISCRETIONARY | XLY | consumer_cyclical | 0.42% | -0.55% | -13.45% | 18.77% | -7.02% | -0.305 | 0.794 | 1.175 | -5.39% |
| CONSUMER_STAPLES | XLP | consumer_defensive | 3.14% | 1.37% | -3.12% | 16.42% | -4.95% | -0.712 | -0.055 | -0.060 | -3.46% |
| HEALTHCARE | XLV | healthcare_and_biotech | -0.23% | 6.58% | -11.15% | 18.32% | -4.01% | -0.192 | 0.260 | 0.328 | -1.61% |
| FINANCIALS | XLF | financials | 2.18% | 6.62% | -9.83% | 13.04% | -3.34% | -0.642 | 0.558 | 0.649 | 0.00% |
| INDUSTRIALS | XLI | industrials_and_defense | -0.53% | 1.36% | 0.15% | 19.61% | -4.60% | -0.856 | 0.732 | 0.968 | -2.92% |
| ENERGY | XLE | energy | 4.01% | 3.67% | 9.87% | 24.85% | -13.21% | -0.792 | -0.120 | -0.200 | -8.20% |
| MATERIALS | XLB | materials_and_mining | 1.25% | -2.42% | -0.88% | 19.08% | -6.43% | -0.518 | 0.548 | 0.763 | -4.31% |
| UTILITIES | XLU | rate_sensitive_defensive | 0.75% | 2.57% | -3.96% | 17.63% | -8.00% | -0.469 | 0.132 | 0.156 | -3.46% |
| REAL_ESTATE | XLRE | rate_sensitive_defensive | 2.78% | 2.22% | 1.56% | 16.65% | -3.38% | -0.655 | 0.252 | 0.288 | 0.00% |
| INTERMEDIATE_TREASURY | IEF | rates_and_duration | 0.01% | 0.02% | -9.60% | 5.07% | -2.62% | -0.703 | 0.215 | 0.080 | -2.80% |
| LONG_TREASURY | TLT | rates_and_duration | -0.33% | -1.11% | -9.64% | 8.94% | -4.30% | -0.684 | 0.173 | 0.128 | -5.54% |
| TIPS | TIP | rates_and_duration | -0.14% | -0.38% | -7.90% | 3.53% | -1.16% | -0.470 | 0.242 | 0.067 | -1.00% |
| INVESTMENT_GRADE_CREDIT | LQD | credit | -0.19% | -0.73% | -8.81% | 5.41% | -2.27% | -0.302 | 0.419 | 0.176 | -1.96% |
| HIGH_YIELD_CREDIT | HYG | credit | 0.06% | 0.45% | -7.83% | 3.68% | -1.10% | -0.657 | 0.766 | 0.233 | -0.09% |
| AGGREGATE_BONDS | AGG | rates_and_duration | -0.05% | -0.11% | -8.81% | 4.16% | -1.90% | -0.158 | 0.325 | 0.098 | -1.61% |
| DEVELOPED_EX_US | VEA | international_equity | -0.99% | -2.46% | 3.22% | 21.01% | -4.85% | -0.530 | 0.797 | 1.079 | -3.26% |
| EMERGING_MARKETS | VWO | international_equity | -1.09% | -2.88% | -0.38% | 20.43% | -5.67% | -0.316 | 0.798 | 1.091 | -3.92% |
| EUROPE | VGK | international_equity | 0.43% | 0.43% | -3.85% | 18.36% | -4.41% | -0.941 | 0.739 | 0.932 | -1.31% |
| JAPAN | EWJ | international_equity | -1.72% | -2.00% | 2.89% | 21.92% | -5.22% | -0.677 | 0.704 | 1.166 | -5.22% |
| CHINA | MCHI | international_equity | 1.79% | -1.15% | -22.05% | 20.65% | -15.01% | -0.002 | 0.576 | 0.934 | -17.65% |
| INDIA | INDA | international_equity | -0.67% | -0.87% | -16.23% | 16.31% | -7.94% | -0.621 | 0.516 | 0.615 | -11.94% |
| GOLD | IAU | precious_metals | -3.50% | -7.66% | -15.00% | 23.98% | -18.11% | -0.502 | 0.301 | 0.664 | -26.36% |
| BROAD_COMMODITIES | PDBC | non_energy_commodities | 3.29% | 0.70% | 12.76% | 21.60% | -16.55% | -0.376 | -0.113 | -0.170 | -10.31% |
| SEMICONDUCTORS | SMH | technology_and_growth | -6.39% | -11.79% | 56.18% | 52.06% | -14.95% | 0.713 | 0.781 | 2.293 | -14.95% |
| SOFTWARE | IGV | technology_and_growth | -0.19% | 1.39% | -19.41% | 34.52% | -21.29% | -0.371 | 0.516 | 1.176 | -20.44% |
| BROAD_AI_TECH | AIQ | technology_and_growth | -7.08% | -10.59% | 17.33% | 39.04% | -15.44% | 0.825 | 0.850 | 1.872 | -15.44% |
| AUTONOMOUS_ROBOTICS | ARKQ | technology_and_growth | -5.26% | -12.00% | -6.03% | 38.01% | -17.86% | -0.916 | 0.789 | 2.165 | -17.86% |
| CYBERSECURITY | CIBR | technology_and_growth | -2.51% | 6.89% | 9.90% | 32.61% | -11.74% | -0.005 | 0.538 | 1.101 | -3.00% |
| SOLAR | TAN | clean_energy | -1.40% | -13.30% | 11.04% | 45.47% | -28.15% | -0.666 | 0.579 | 1.781 | -26.71% |
| METALS_MINING | XME | materials_and_mining | -4.12% | -17.59% | -8.31% | 40.31% | -25.43% | -0.519 | 0.588 | 1.701 | -25.43% |
| EQUAL_WEIGHT_SP500 | RSP | diversified_us_equity | 0.73% | 1.70% | -1.00% | 10.88% | -2.04% | -0.678 | 0.776 | 0.725 | 0.00% |
| BIOTECH | XBI | healthcare_and_biotech | -7.48% | 11.83% | 1.03% | 30.21% | -8.57% | 0.574 | 0.483 | 1.023 | -7.48% |
| REGIONAL_BANKS | KRE | financials | 4.38% | 8.80% | 0.58% | 20.80% | -5.29% | -0.371 | 0.443 | 0.809 | 0.00% |
| AEROSPACE_DEFENSE | ITA | industrials_and_defense | -3.64% | -2.45% | -9.02% | 26.17% | -8.91% | -0.411 | 0.583 | 1.025 | -7.93% |
| CANADA | EWC | international_equity | 1.73% | 1.07% | -1.68% | 13.16% | -3.20% | -0.733 | 0.681 | 0.771 | -0.17% |
| UNITED_KINGDOM | EWU | international_equity | 1.21% | 1.93% | -4.89% | 17.09% | -5.55% | -0.475 | 0.609 | 0.719 | -2.13% |
| AUSTRALIA | EWA | international_equity | 1.52% | 0.39% | 0.72% | 18.57% | -7.27% | -0.788 | 0.676 | 0.928 | -4.06% |
| SOUTH_KOREA | EWY | international_equity | -11.58% | -22.45% | 87.53% | 77.72% | -25.47% | 0.359 | 0.649 | 2.661 | -25.47% |
| TAIWAN | EWT | international_equity | -4.65% | -5.55% | 51.82% | 40.97% | -10.19% | 0.096 | 0.745 | 1.716 | -10.19% |
| BRAZIL | EWZ | international_equity | 1.06% | 2.28% | -1.93% | 22.94% | -18.76% | -0.947 | 0.509 | 1.013 | -14.53% |
| MEXICO | EWW | international_equity | 1.32% | -2.98% | 0.54% | 20.53% | -7.30% | -0.639 | 0.529 | 0.923 | -6.04% |
| SOUTH_AFRICA | EZA | international_equity | -0.54% | -6.81% | -14.37% | 33.64% | -15.34% | -0.432 | 0.618 | 1.582 | -21.18% |
| MORTGAGE_BACKED_BONDS | MBB | rates_and_duration | -0.06% | -0.16% | -8.58% | 4.85% | -2.24% | -0.483 | 0.319 | 0.112 | -1.54% |
| MUNICIPAL_BONDS | MUB | rates_and_duration | -0.30% | 0.04% | -8.16% | 2.74% | -1.36% | -0.402 | 0.309 | 0.071 | -0.88% |
| EMERGING_MARKET_BONDS | EMB | credit | -0.39% | -0.46% | -6.31% | 5.99% | -2.10% | -0.599 | 0.659 | 0.293 | -0.86% |
| INTERNATIONAL_BONDS | BNDX | rates_and_duration | -0.12% | -0.13% | -8.52% | 4.35% | -1.34% | -0.362 | 0.404 | 0.113 | -1.40% |
| SILVER | SLV | precious_metals | -6.93% | -20.32% | -28.35% | 50.99% | -36.50% | -0.669 | 0.349 | 1.697 | -52.28% |
| COPPER | CPER | non_energy_commodities | 0.82% | -3.72% | -1.62% | 28.97% | -10.57% | -0.627 | 0.456 | 1.236 | -6.26% |
| AGRICULTURE | DBA | non_energy_commodities | -0.43% | 4.88% | -5.93% | 13.45% | -8.67% | -0.082 | 0.083 | 0.072 | -3.97% |
| OIL | USO | energy | 9.44% | -1.29% | 55.86% | 53.95% | -32.49% | -0.582 | -0.286 | -1.019 | -22.01% |
| US_DOLLAR | UUP | currencies | -0.07% | 1.61% | -6.83% | 4.95% | -0.98% | 0.026 | -0.275 | -0.132 | -0.67% |
| EURO | FXE | currencies | 0.14% | -0.88% | -9.34% | 4.73% | -3.70% | -0.716 | 0.257 | 0.126 | -4.62% |
| YEN | FXY | currencies | -0.05% | -1.09% | -10.00% | 6.54% | -3.85% | -0.230 | 0.111 | 0.071 | -10.18% |
| BITCOIN_ETF | IBIT | crypto_assets | 1.62% | -3.29% | -38.65% | 38.65% | -28.36% | -0.321 | 0.513 | 1.808 | -48.95% |
| ETHEREUM_ETF | ETHA | crypto_assets | 7.13% | 2.98% | -52.29% | 53.61% | -36.13% | -0.453 | 0.544 | 2.973 | -61.38% |
