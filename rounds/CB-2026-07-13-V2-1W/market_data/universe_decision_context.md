# Full-Universe Horizon-Specific Decision Context

Profile: weekly. All values stop at the requested close and are sorted by frozen option order, not performance.

Returns, volatility, and drawdown are descriptive context rather than forecasts. Active return is option return minus SPY return. The prior-window active return excludes the latest decision window so recent movement can be separated from the preceding trend.

No rank, recommendation, or composite buy score is included. Volume z-scores compare recent average reported volume with the immediately preceding baseline.

- Source: yahoo_chart_adjusted_close_and_reported_volume
- As-of date requested: 2026-07-13
- Failed options: 0

## Mechanical Market State

| metric | value |
| --- | --- |
| spy_return_5s | -0.28% |
| spy_return_21s | 3.54% |
| rsp_return_5s | -0.36% |
| rsp_return_21s | 4.13% |
| hyg_return_5s | -0.44% |
| hyg_return_21s | 0.53% |
| tlt_return_5s | -1.73% |
| tlt_return_21s | -0.71% |
| uup_return_5s | 0.64% |
| uup_return_21s | 1.60% |
| uso_return_5s | 12.88% |
| uso_return_21s | -12.29% |
| iau_return_5s | -3.90% |
| iau_return_21s | -2.01% |
| rsp_minus_spy_5s | -0.08% |
| rsp_minus_spy_21s | 0.59% |
| positive_asset_share_5s | 26.09% |
| positive_asset_share_21s | 71.01% |
| active_return_dispersion_5s | 3.16% |

## Option Decision Context

| option_id | symbol | option_group | as_of_price_date | return_3s | return_5s | active_return_5s | prior_16s_active_return | volatility_21s | max_drawdown_21s | volume_zscore_5v60 | corr_spy_63s | beta_spy_63s | distance_52w_high | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | cash | 2026-07-13 | 0.00% | 0.00% | 0.28% | -3.83% | 0.00% | 0.00% | 0.000 |  | 0.000 |  | cash |
| SHORT_TREASURY | BIL | cash_and_short_duration | 2026-07-13 | 0.05% | 0.08% | 0.36% | -3.58% | 0.26% | -0.01% | -0.764 | -0.191 | -0.003 | 0.00% | pass |
| SP500 | SPY | us_broad_market | 2026-07-13 | 0.51% | -0.28% | 0.00% | 0.00% | 14.79% | -3.17% | -0.838 | 1.000 | 1.000 | -1.12% | pass |
| TOTAL_US_MARKET | VTI | us_broad_market | 2026-07-13 | 0.42% | -0.51% | -0.23% | 0.28% | 14.18% | -2.49% | 0.179 | 0.992 | 0.993 | -0.94% | pass |
| NASDAQ100 | QQQ | us_growth_and_technology | 2026-07-13 | 0.04% | -1.53% | -1.25% | 0.48% | 30.15% | -4.93% | -0.742 | 0.920 | 1.676 | -4.51% | pass |
| LARGE_GROWTH | IWF | us_style_factor | 2026-07-13 | -0.17% | -1.15% | -0.87% | -0.97% | 22.62% | -5.03% | -0.824 | 0.898 | 1.278 | -5.49% | pass |
| LARGE_VALUE | IWD | us_style_factor | 2026-07-13 | 0.99% | 0.15% | 0.43% | 1.60% | 12.91% | -1.39% | -0.438 | 0.731 | 0.651 | -0.05% | pass |
| MID_CAP | IJH | us_size_factor | 2026-07-13 | 0.68% | -1.54% | -1.26% | 0.19% | 15.22% | -3.09% | -0.878 | 0.772 | 0.875 | -2.43% | pass |
| SMALL_CAP | IWM | us_size_factor | 2026-07-13 | 0.00% | -1.81% | -1.53% | 2.40% | 16.76% | -2.32% | -1.366 | 0.795 | 1.136 | -2.32% | pass |
| SMALL_VALUE | IWN | us_style_factor | 2026-07-13 | 0.96% | -0.88% | -0.60% | 1.68% | 13.10% | -1.83% | -1.142 | 0.695 | 0.815 | -0.88% | pass |
| DIVIDEND | SCHD | us_factor_equity | 2026-07-13 | 0.68% | 0.99% | 1.27% | -3.10% | 12.25% | -2.93% | -0.784 | 0.147 | 0.122 | -0.03% | pass |
| LOW_VOL | SPLV | us_factor_equity | 2026-07-13 | 0.73% | 0.32% | 0.60% | -0.55% | 14.28% | -1.89% | -0.288 | -0.261 | -0.251 | -0.66% | pass |
| MOMENTUM | MTUM | us_factor_equity | 2026-07-13 | -0.07% | -2.20% | -1.92% | 1.79% | 45.49% | -9.50% | 0.371 | 0.775 | 2.038 | -8.86% | pass |
| TECHNOLOGY | XLK | us_sector | 2026-07-13 | -0.07% | -1.25% | -0.97% | 0.22% | 38.12% | -6.75% | -0.900 | 0.848 | 2.106 | -8.43% | pass |
| COMMUNICATIONS | XLC | us_sector | 2026-07-13 | 1.95% | 1.25% | 1.53% | -4.29% | 19.16% | -5.76% | 0.264 | 0.470 | 0.542 | -6.53% | pass |
| CONSUMER_DISCRETIONARY | XLY | us_sector | 2026-07-13 | 0.64% | -1.67% | -1.39% | 0.36% | 22.27% | -4.21% | 0.531 | 0.762 | 1.124 | -6.44% | pass |
| CONSUMER_STAPLES | XLP | us_sector | 2026-07-13 | 0.24% | 0.58% | 0.86% | -4.77% | 17.46% | -3.58% | -0.625 | -0.294 | -0.342 | -4.84% | pass |
| HEALTHCARE | XLV | us_sector | 2026-07-13 | -0.55% | -0.34% | -0.06% | 2.60% | 20.06% | -3.04% | -0.241 | -0.052 | -0.069 | -1.84% | pass |
| FINANCIALS | XLF | us_sector | 2026-07-13 | 2.00% | -0.12% | 0.16% | 4.03% | 14.83% | -2.08% | -0.645 | 0.198 | 0.202 | -0.12% | pass |
| INDUSTRIALS | XLI | us_sector | 2026-07-13 | -0.03% | -2.80% | -2.52% | 5.81% | 20.86% | -2.80% | -0.984 | 0.635 | 0.953 | -2.80% | pass |
| ENERGY | XLE | us_sector | 2026-07-13 | 2.05% | 6.79% | 7.08% | -11.96% | 25.36% | -8.69% | -0.412 | -0.403 | -0.765 | -8.65% | pass |
| MATERIALS | XLB | us_sector | 2026-07-13 | 0.84% | -2.69% | -2.41% | 1.36% | 21.82% | -4.50% | -0.244 | 0.520 | 0.756 | -4.90% | pass |
| UTILITIES | XLU | us_sector | 2026-07-13 | 0.79% | 0.93% | 1.21% | -0.22% | 15.26% | -3.10% | -0.886 | -0.075 | -0.101 | -2.93% | pass |
| REAL_ESTATE | XLRE | us_sector | 2026-07-13 | 1.25% | 0.93% | 1.21% | -4.52% | 17.94% | -3.31% | -0.852 | -0.012 | -0.015 | -1.19% | pass |
| INTERMEDIATE_TREASURY | IEF | bonds_and_rates | 2026-07-13 | -0.24% | -0.94% | -0.66% | -2.98% | 5.58% | -1.54% | -0.565 | 0.580 | 0.224 | -3.25% | pass |
| LONG_TREASURY | TLT | bonds_and_rates | 2026-07-13 | -0.46% | -1.73% | -1.45% | -2.79% | 10.13% | -3.62% | -0.511 | 0.451 | 0.309 | -5.81% | pass |
| TIPS | TIP | bonds_and_rates | 2026-07-13 | -0.13% | -0.53% | -0.25% | -3.52% | 4.37% | -0.85% | -0.758 | 0.607 | 0.165 | -1.05% | pass |
| INVESTMENT_GRADE_CREDIT | LQD | credit | 2026-07-13 | -0.66% | -1.57% | -1.29% | -3.01% | 5.58% | -2.16% | 0.413 | 0.609 | 0.251 | -2.45% | pass |
| HIGH_YIELD_CREDIT | HYG | credit | 2026-07-13 | -0.18% | -0.44% | -0.16% | -2.86% | 3.29% | -0.44% | -0.865 | 0.784 | 0.224 | -0.44% | pass |
| AGGREGATE_BONDS | AGG | bonds_and_rates | 2026-07-13 | -0.34% | -0.96% | -0.68% | -3.14% | 4.38% | -1.34% | 0.066 | 0.616 | 0.195 | -2.03% | pass |
| DEVELOPED_EX_US | VEA | international_equity | 2026-07-13 | -0.82% | -2.96% | -2.68% | 1.20% | 21.97% | -3.63% | 0.732 | 0.836 | 1.322 | -3.63% | pass |
| EMERGING_MARKETS | VWO | international_equity | 2026-07-13 | -0.64% | -2.13% | -1.85% | 0.36% | 22.41% | -4.34% | 0.620 | 0.869 | 1.348 | -4.00% | pass |
| EUROPE | VGK | international_equity | 2026-07-13 | -0.36% | -2.35% | -2.06% | 1.37% | 16.92% | -2.35% | -1.272 | 0.726 | 1.009 | -2.35% | pass |
| JAPAN | EWJ | international_equity | 2026-07-13 | 0.19% | -2.68% | -2.40% | 3.45% | 26.44% | -4.57% | -0.584 | 0.777 | 1.271 | -4.38% | pass |
| CHINA | MCHI | international_equity | 2026-07-13 | -0.61% | 0.98% | 1.26% | -7.06% | 18.97% | -8.10% | -0.355 | 0.547 | 0.840 | -20.10% | pass |
| INDIA | INDA | international_equity | 2026-07-13 | 0.29% | -2.19% | -1.90% | 1.62% | 15.51% | -2.54% | -0.497 | 0.625 | 0.777 | -11.76% | pass |
| GOLD | IAU | commodities | 2026-07-13 | -1.94% | -3.90% | -3.61% | -1.86% | 26.09% | -7.99% | -0.735 | 0.721 | 1.315 | -25.91% | pass |
| BROAD_COMMODITIES | PDBC | commodities | 2026-07-13 | 1.68% | 4.97% | 5.25% | -11.46% | 21.69% | -9.47% | -0.332 | -0.145 | -0.238 | -10.63% | pass |
| SEMICONDUCTORS | SMH | ai_and_technology | 2026-07-13 | -1.24% | -3.09% | -2.81% | 2.02% | 63.64% | -13.07% | -0.233 | 0.779 | 3.018 | -12.45% | pass |
| SOFTWARE | IGV | ai_and_technology | 2026-07-13 | 0.24% | -2.20% | -1.92% | -0.31% | 27.87% | -8.55% | -1.385 | 0.372 | 1.039 | -21.29% | pass |
| BROAD_AI_TECH | AIQ | ai_and_technology | 2026-07-13 | -2.03% | -3.98% | -3.70% | 0.21% | 43.64% | -8.63% | -0.154 | 0.840 | 2.474 | -12.60% | pass |
| AUTONOMOUS_ROBOTICS | ARKQ | ai_and_technology | 2026-07-13 | -2.51% | -7.23% | -6.95% | 0.80% | 38.98% | -10.39% | -1.298 | 0.854 | 2.463 | -16.08% | pass |
| CYBERSECURITY | CIBR | ai_and_technology | 2026-07-13 | 0.20% | -1.15% | -0.87% | 7.87% | 25.64% | -3.12% | 0.184 | 0.434 | 1.076 | -2.57% | pass |
| SOLAR | TAN | clean_energy | 2026-07-13 | -1.88% | -7.68% | -7.40% | -6.57% | 43.04% | -15.72% | -1.342 | 0.722 | 2.426 | -28.15% | pass |
| METALS_MINING | XME | commodities | 2026-07-13 | 0.15% | -3.76% | -3.48% | -9.41% | 32.72% | -15.44% | -0.116 | 0.704 | 2.094 | -23.09% | pass |
| EQUAL_WEIGHT_SP500 | RSP | us_broad_market | 2026-07-13 | 0.96% | -0.36% | -0.08% | 0.67% | 11.85% | -1.83% | -0.573 | 0.753 | 0.620 | -0.36% | pass |
| BIOTECH | XBI | healthcare_and_biotech | 2026-07-13 | -4.68% | -3.40% | -3.12% | 21.10% | 28.29% | -5.44% | 0.557 | 0.406 | 0.931 | -5.44% | pass |
| REGIONAL_BANKS | KRE | us_industry | 2026-07-13 | 2.43% | -0.58% | -0.30% | 2.26% | 19.50% | -3.73% | -0.501 | 0.183 | 0.278 | -1.39% | pass |
| AEROSPACE_DEFENSE | ITA | us_industry | 2026-07-13 | -1.91% | -6.27% | -5.99% | 7.77% | 26.36% | -6.27% | -1.007 | 0.484 | 0.953 | -6.27% | pass |
| CANADA | EWC | country_equity | 2026-07-13 | 1.31% | 1.15% | 1.43% | -2.75% | 10.22% | -3.08% | -0.721 | 0.636 | 0.639 | -0.76% | pass |
| UNITED_KINGDOM | EWU | country_equity | 2026-07-13 | -0.28% | -1.82% | -1.54% | 0.72% | 16.15% | -2.28% | 2.041 | 0.508 | 0.654 | -3.40% | pass |
| AUSTRALIA | EWA | country_equity | 2026-07-13 | 0.82% | 0.07% | 0.35% | -1.88% | 16.55% | -4.42% | -0.158 | 0.625 | 0.874 | -5.00% | pass |
| SOUTH_KOREA | EWY | country_equity | 2026-07-13 | -8.05% | -11.50% | -11.22% | 2.56% | 88.78% | -23.35% | 0.669 | 0.760 | 4.403 | -23.35% | pass |
| TAIWAN | EWT | country_equity | 2026-07-13 | -1.94% | -5.02% | -4.74% | 5.63% | 47.19% | -8.65% | 0.386 | 0.788 | 2.439 | -8.65% | pass |
| BRAZIL | EWZ | country_equity | 2026-07-13 | 2.85% | 1.35% | 1.63% | 0.53% | 20.88% | -2.99% | -0.679 | 0.430 | 0.733 | -14.39% | pass |
| MEXICO | EWW | country_equity | 2026-07-13 | -0.75% | -2.98% | -2.70% | 0.40% | 22.72% | -5.37% | -0.948 | 0.612 | 0.945 | -7.37% | pass |
| SOUTH_AFRICA | EZA | country_equity | 2026-07-13 | 0.11% | -2.89% | -2.61% | 0.72% | 31.17% | -8.61% | -0.333 | 0.770 | 1.966 | -21.40% | pass |
| MORTGAGE_BACKED_BONDS | MBB | bonds_and_rates | 2026-07-13 | -0.46% | -1.08% | -0.80% | -3.08% | 5.00% | -1.45% | -0.338 | 0.614 | 0.224 | -2.06% | pass |
| MUNICIPAL_BONDS | MUB | bonds_and_rates | 2026-07-13 | -0.01% | -0.62% | -0.34% | -2.86% | 2.50% | -0.62% | 0.080 | 0.605 | 0.126 | -0.62% | pass |
| EMERGING_MARKET_BONDS | EMB | credit | 2026-07-13 | -0.43% | -1.01% | -0.73% | -2.36% | 5.75% | -1.08% | 0.182 | 0.748 | 0.348 | -1.08% | pass |
| INTERNATIONAL_BONDS | BNDX | bonds_and_rates | 2026-07-13 | 0.13% | -0.68% | -0.40% | -2.93% | 3.96% | -1.20% | -0.308 | 0.568 | 0.189 | -1.55% | pass |
| SILVER | SLV | commodities | 2026-07-13 | -1.27% | -7.04% | -6.76% | -6.52% | 49.73% | -18.42% | -0.913 | 0.686 | 2.688 | -50.61% | pass |
| COPPER | CPER | commodities | 2026-07-13 | 2.35% | 0.26% | 0.55% | -3.51% | 26.78% | -8.42% | -1.104 | 0.722 | 1.596 | -6.55% | pass |
| AGRICULTURE | DBA | commodities | 2026-07-13 | 0.36% | 0.65% | 0.93% | 0.77% | 13.65% | -1.52% | -0.606 | -0.007 | -0.007 | -3.52% | pass |
| OIL | USO | commodities | 2026-07-13 | 4.97% | 12.88% | 13.16% | -26.13% | 52.17% | -23.10% | -0.183 | -0.345 | -1.423 | -22.99% | pass |
| US_DOLLAR | UUP | currencies | 2026-07-13 | 0.49% | 0.64% | 0.92% | -2.87% | 5.04% | -0.74% | -0.380 | -0.576 | -0.209 | -0.11% | pass |
| EURO | FXE | currencies | 2026-07-13 | -0.42% | -0.53% | -0.25% | -4.68% | 5.24% | -2.19% | -0.644 | 0.590 | 0.208 | -5.12% | pass |
| YEN | FXY | currencies | 2026-07-13 | 0.00% | -0.23% | 0.05% | -4.84% | 5.55% | -1.74% | -0.600 | 0.253 | 0.126 | -10.17% | pass |
| BITCOIN_ETF | IBIT | crypto_proxies | 2026-07-13 | -0.03% | -2.49% | -2.21% | -0.87% | 39.91% | -11.79% | -0.721 | 0.514 | 1.475 | -50.60% | pass |
| ETHEREUM_ETF | ETHA | crypto_proxies | 2026-07-13 | 1.98% | -1.33% | -1.05% | 6.51% | 57.23% | -14.68% | -0.686 | 0.612 | 2.418 | -63.46% | pass |
