# Full-Universe Price, Risk, And Benchmark Context

This table is mechanically calculated from adjusted close data. It is sorted in the option order from `options.yaml`, not by performance. CASH is shown as 0.00%.

Price-history note: trailing returns are descriptive context, not forecasts. Treat recent gains or losses as one input alongside catalysts, macro context, volatility, drawdown, benchmark-relative risk, and any valuation or fundamental facts supplied in the briefing.

Benchmark-relative values are asset return minus SPY return over the same window. Beta and correlation use available one-year daily adjusted-close returns.

- Source: tiingo_eod_adj_close; yahoo_chart_adjclose fallback for rows marked in CSV message
- As-of date requested: 2026-07-13
- Failed options: 0

| option_id | symbol | option_group | as_of_price_date | return_7d | return_30d | return_6m | return_1y | return_vs_sp500_30d | volatility_30d | max_drawdown_30d | up_day_share_30d | distance_from_52w_high | beta_to_sp500_1y | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | cash | 2026-07-13 | 0.00% | 0.00% | 0.00% | 0.00% | -1.26% | 0.00% | 0.00% |  |  | 0.00 | cash |
| SHORT_TREASURY | BIL | cash_and_short_duration | 2026-07-13 | 0.08% | 0.28% | 1.76% | 3.82% | -0.98% | 0.27% | -0.01% | 72.22% | 0.00% | -0.00 | pass |
| SP500 | SPY | us_broad_market | 2026-07-13 | -0.28% | 1.26% | 8.56% | 21.46% | 0.00% | 13.15% | -3.17% | 38.89% | -1.12% | 1.00 | pass |
| TOTAL_US_MARKET | VTI | us_broad_market | 2026-07-13 | -0.51% | 1.22% | 8.67% | 21.85% | -0.04% | 12.39% | -2.49% | 38.89% | -0.94% | 1.01 | pass |
| NASDAQ100 | QQQ | us_growth_and_technology | 2026-07-13 | -1.53% | -1.22% | 13.92% | 29.05% | -2.48% | 27.24% | -4.93% | 44.44% | -4.51% | 1.38 | pass |
| LARGE_GROWTH | IWF | us_style_factor | 2026-07-13 | -1.15% | 0.07% | 2.40% | 14.17% | -1.19% | 21.97% | -5.03% | 44.44% | -5.49% | 1.25 | pass |
| LARGE_VALUE | IWD | us_style_factor | 2026-07-13 | 0.15% | 2.59% | 14.63% | 28.21% | 1.33% | 11.46% | -1.39% | 61.11% | -0.05% | 0.73 | pass |
| MID_CAP | IJH | us_size_factor | 2026-07-13 | -1.54% | -0.81% | 9.00% | 20.15% | -2.07% | 13.13% | -3.09% | 44.44% | -2.43% | 1.01 | pass |
| SMALL_CAP | IWM | us_size_factor | 2026-07-13 | -1.81% | 0.42% | 12.76% | 33.75% | -0.84% | 13.86% | -2.32% | 44.44% | -2.32% | 1.26 | pass |
| SMALL_VALUE | IWN | us_style_factor | 2026-07-13 | -0.88% | 1.03% | 15.28% | 35.48% | -0.23% | 10.74% | -1.83% | 50.00% | -0.88% | 1.03 | pass |
| DIVIDEND | SCHD | us_factor_equity | 2026-07-13 | 0.99% | -0.00% | 15.64% | 23.51% | -1.26% | 12.30% | -2.36% | 50.00% | -0.03% | 0.29 | pass |
| LOW_VOL | SPLV | us_factor_equity | 2026-07-13 | 0.32% | 2.80% | 7.13% | 7.63% | 1.54% | 15.09% | -1.89% | 61.11% | -0.66% | 0.05 | pass |
| MOMENTUM | MTUM | us_factor_equity | 2026-07-13 | -2.20% | -2.90% | 21.76% | 34.12% | -4.17% | 43.99% | -9.50% | 55.56% | -8.86% | 1.51 | pass |
| TECHNOLOGY | XLK | us_sector | 2026-07-13 | -1.25% | -1.79% | 24.06% | 42.45% | -3.05% | 35.60% | -6.75% | 50.00% | -8.43% | 1.68 | pass |
| COMMUNICATIONS | XLC | us_sector | 2026-07-13 | 1.25% | 0.21% | -3.98% | 6.59% | -1.05% | 20.29% | -5.76% | 55.56% | -6.53% | 0.69 | pass |
| CONSUMER_DISCRETIONARY | XLY | us_sector | 2026-07-13 | -1.67% | -0.28% | -6.20% | 5.62% | -1.54% | 21.25% | -4.21% | 50.00% | -6.44% | 1.18 | pass |
| CONSUMER_STAPLES | XLP | us_sector | 2026-07-13 | 0.58% | -0.75% | 5.61% | 7.58% | -2.01% | 18.68% | -3.32% | 50.00% | -4.84% | -0.04 | pass |
| HEALTHCARE | XLV | us_sector | 2026-07-13 | -0.34% | 5.40% | 3.86% | 21.48% | 4.14% | 21.30% | -2.31% | 61.11% | -1.84% | 0.35 | pass |
| FINANCIALS | XLF | us_sector | 2026-07-13 | -0.12% | 5.49% | 4.29% | 9.16% | 4.23% | 15.48% | -2.08% | 61.11% | -0.12% | 0.66 | pass |
| INDUSTRIALS | XLI | us_sector | 2026-07-13 | -2.80% | 2.63% | 10.56% | 21.63% | 1.37% | 18.73% | -2.80% | 61.11% | -2.80% | 0.97 | pass |
| ENERGY | XLE | us_sector | 2026-07-13 | 6.79% | -0.70% | 22.39% | 31.29% | -1.96% | 22.53% | -4.25% | 44.44% | -8.65% | -0.19 | pass |
| MATERIALS | XLB | us_sector | 2026-07-13 | -2.69% | -2.70% | 4.65% | 12.55% | -3.96% | 18.44% | -4.50% | 50.00% | -4.90% | 0.77 | pass |
| UTILITIES | XLU | us_sector | 2026-07-13 | 0.93% | 3.33% | 8.13% | 14.00% | 2.07% | 16.14% | -3.10% | 61.11% | -2.93% | 0.16 | pass |
| REAL_ESTATE | XLRE | us_sector | 2026-07-13 | 0.93% | -0.60% | 10.89% | 11.21% | -1.86% | 18.81% | -2.75% | 61.11% | -1.19% | 0.30 | pass |
| INTERMEDIATE_TREASURY | IEF | bonds_and_rates | 2026-07-13 | -0.94% | -0.62% | -1.23% | 2.77% | -1.88% | 5.34% | -1.54% | 55.56% | -3.25% | 0.08 | pass |
| LONG_TREASURY | TLT | bonds_and_rates | 2026-07-13 | -1.73% | -1.74% | -2.22% | 2.34% | -3.00% | 9.64% | -3.62% | 44.44% | -5.81% | 0.13 | pass |
| TIPS | TIP | bonds_and_rates | 2026-07-13 | -0.53% | -0.59% | 0.46% | 3.09% | -1.85% | 4.46% | -0.85% | 50.00% | -1.05% | 0.07 | pass |
| INVESTMENT_GRADE_CREDIT | LQD | credit | 2026-07-13 | -1.57% | -1.54% | -1.23% | 3.51% | -2.80% | 4.93% | -2.15% | 50.00% | -2.45% | 0.18 | pass |
| HIGH_YIELD_CREDIT | HYG | credit | 2026-07-13 | -0.44% | -0.06% | 1.07% | 5.36% | -1.32% | 2.74% | -0.44% | 33.33% | -0.44% | 0.23 | pass |
| AGGREGATE_BONDS | AGG | bonds_and_rates | 2026-07-13 | -0.96% | -0.73% | -0.53% | 3.67% | -1.99% | 4.09% | -1.34% | 55.56% | -2.03% | 0.10 | pass |
| DEVELOPED_EX_US | VEA | international_equity | 2026-07-13 | -2.96% | -1.99% | 8.81% | 26.21% | -3.25% | 18.59% | -3.63% | 55.56% | -3.63% | 1.08 | pass |
| EMERGING_MARKETS | VWO | international_equity | 2026-07-13 | -2.13% | -1.16% | 5.18% | 21.65% | -2.42% | 20.56% | -4.34% | 44.44% | -4.00% | 1.08 | pass |
| EUROPE | VGK | international_equity | 2026-07-13 | -2.35% | -0.63% | 4.29% | 16.41% | -1.89% | 13.73% | -2.35% | 50.00% | -2.35% | 0.93 | pass |
| JAPAN | EWJ | international_equity | 2026-07-13 | -2.68% | 0.55% | 10.39% | 33.65% | -0.71% | 24.82% | -4.57% | 61.11% | -4.38% | 1.16 | pass |
| CHINA | MCHI | international_equity | 2026-07-13 | 0.98% | -3.56% | -16.75% | -2.59% | -4.82% | 19.64% | -8.10% | 38.89% | -20.10% | 0.92 | pass |
| INDIA | INDA | international_equity | 2026-07-13 | -2.19% | 0.95% | -8.01% | -11.10% | -0.31% | 14.14% | -2.54% | 55.56% | -11.76% | 0.62 | pass |
| GOLD | IAU | commodities | 2026-07-13 | -3.90% | -4.98% | -12.86% | 18.88% | -6.24% | 22.75% | -7.99% | 38.89% | -25.91% | 0.66 | pass |
| BROAD_COMMODITIES | PDBC | commodities | 2026-07-13 | 4.97% | -0.94% | 21.93% | 30.72% | -2.20% | 22.60% | -6.57% | 44.44% | -10.63% | -0.18 | pass |
| SEMICONDUCTORS | SMH | ai_and_technology | 2026-07-13 | -3.09% | -5.54% | 49.57% | 104.33% | -6.80% | 60.92% | -13.07% | 55.56% | -12.45% | 2.28 | pass |
| SOFTWARE | IGV | ai_and_technology | 2026-07-13 | -2.20% | 2.22% | -10.29% | -13.74% | 0.96% | 28.90% | -8.55% | 50.00% | -21.29% | 1.17 | pass |
| BROAD_AI_TECH | AIQ | ai_and_technology | 2026-07-13 | -3.98% | -4.22% | 16.45% | 41.76% | -5.48% | 41.15% | -8.63% | 50.00% | -12.60% | 1.86 | pass |
| AUTONOMOUS_ROBOTICS | ARKQ | ai_and_technology | 2026-07-13 | -7.23% | -6.73% | -7.64% | 31.73% | -7.99% | 33.38% | -10.39% | 27.78% | -16.08% | 2.16 | pass |
| CYBERSECURITY | CIBR | ai_and_technology | 2026-07-13 | -1.15% | 7.72% | 26.80% | 27.22% | 6.46% | 26.22% | -3.12% | 44.44% | -2.57% | 1.10 | pass |
| SOLAR | TAN | clean_energy | 2026-07-13 | -7.68% | -15.72% | 1.78% | 39.42% | -16.98% | 39.98% | -15.28% | 38.89% | -28.15% | 1.76 | pass |
| METALS_MINING | XME | commodities | 2026-07-13 | -3.76% | -15.18% | -14.64% | 40.11% | -16.44% | 25.32% | -15.44% | 33.33% | -23.09% | 1.69 | pass |
| EQUAL_WEIGHT_SP500 | RSP | us_broad_market | 2026-07-13 | -0.36% | 1.61% | 9.20% | 18.09% | 0.35% | 11.09% | -1.83% | 55.56% | -0.36% | 0.74 | pass |
| BIOTECH | XBI | healthcare_and_biotech | 2026-07-13 | -3.40% | 16.22% | 25.55% | 79.33% | 14.96% | 29.19% | -5.44% | 66.67% | -5.44% | 1.02 | pass |
| REGIONAL_BANKS | KRE | us_industry | 2026-07-13 | -0.58% | 2.93% | 14.73% | 22.35% | 1.67% | 19.14% | -3.73% | 72.22% | -1.39% | 0.83 | pass |
| AEROSPACE_DEFENSE | ITA | us_industry | 2026-07-13 | -6.27% | 0.61% | -0.91% | 24.48% | -0.65% | 20.37% | -6.27% | 55.56% | -6.27% | 1.02 | pass |
| CANADA | EWC | country_equity | 2026-07-13 | 1.15% | 0.42% | 7.05% | 29.05% | -0.84% | 9.36% | -3.08% | 66.67% | -0.76% | 0.77 | pass |
| UNITED_KINGDOM | EWU | country_equity | 2026-07-13 | -1.82% | -0.29% | 4.54% | 20.07% | -1.55% | 14.77% | -2.28% | 38.89% | -3.40% | 0.72 | pass |
| AUSTRALIA | EWA | country_equity | 2026-07-13 | 0.07% | -1.61% | 8.85% | 10.93% | -2.87% | 13.82% | -4.42% | 50.00% | -5.00% | 0.93 | pass |
| SOUTH_KOREA | EWY | country_equity | 2026-07-13 | -11.50% | -14.91% | 56.24% | 136.83% | -16.17% | 78.85% | -23.35% | 44.44% | -23.35% | 2.65 | pass |
| TAIWAN | EWT | country_equity | 2026-07-13 | -5.02% | -0.72% | 54.13% | 82.78% | -1.98% | 46.05% | -8.65% | 55.56% | -8.65% | 1.71 | pass |
| BRAZIL | EWZ | country_equity | 2026-07-13 | 1.35% | 1.79% | 9.49% | 34.32% | 0.53% | 19.55% | -2.63% | 38.89% | -14.39% | 1.01 | pass |
| MEXICO | EWW | country_equity | 2026-07-13 | -2.98% | -4.11% | 4.55% | 27.53% | -5.38% | 18.02% | -5.37% | 38.89% | -7.37% | 0.92 | pass |
| SOUTH_AFRICA | EZA | country_equity | 2026-07-13 | -2.89% | -4.09% | -12.25% | 27.68% | -5.35% | 23.32% | -8.61% | 44.44% | -21.40% | 1.58 | pass |
| MORTGAGE_BACKED_BONDS | MBB | bonds_and_rates | 2026-07-13 | -1.08% | -0.83% | -0.47% | 4.79% | -2.09% | 4.66% | -1.45% | 55.56% | -2.06% | 0.11 | pass |
| MUNICIPAL_BONDS | MUB | bonds_and_rates | 2026-07-13 | -0.62% | 0.13% | 0.96% | 6.17% | -1.13% | 2.55% | -0.62% | 55.56% | -0.62% | 0.07 | pass |
| EMERGING_MARKET_BONDS | EMB | credit | 2026-07-13 | -1.01% | -0.60% | 1.80% | 9.38% | -1.87% | 4.74% | -1.08% | 38.89% | -1.08% | 0.29 | pass |
| INTERNATIONAL_BONDS | BNDX | bonds_and_rates | 2026-07-13 | -0.68% | -0.54% | 0.02% | 1.94% | -1.80% | 3.57% | -1.20% | 44.44% | -1.55% | 0.11 | pass |
| SILVER | SLV | commodities | 2026-07-13 | -7.04% | -14.90% | -33.64% | 48.90% | -16.16% | 45.10% | -18.42% | 38.89% | -50.61% | 1.69 | pass |
| COPPER | CPER | commodities | 2026-07-13 | 0.26% | -4.07% | 2.85% | 9.94% | -5.33% | 25.25% | -8.42% | 44.44% | -6.55% | 1.23 | pass |
| AGRICULTURE | DBA | commodities | 2026-07-13 | 0.65% | 5.64% | 8.41% | 11.45% | 4.38% | 14.58% | -1.52% | 61.11% | -3.52% | 0.07 | pass |
| OIL | USO | commodities | 2026-07-13 | 12.88% | -6.09% | 60.30% | 52.40% | -7.35% | 52.76% | -14.80% | 44.44% | -22.99% | -1.03 | pass |
| US_DOLLAR | UUP | currencies | 2026-07-13 | 0.64% | 1.97% | 4.20% | 8.28% | 0.71% | 5.18% | -0.74% | 55.56% | -0.11% | -0.13 | pass |
| EURO | FXE | currencies | 2026-07-13 | -0.53% | -1.64% | -1.93% | -1.92% | -2.90% | 5.46% | -2.19% | 38.89% | -5.12% | 0.13 | pass |
| YEN | FXY | currencies | 2026-07-13 | -0.23% | -1.40% | -2.25% | -9.61% | -2.66% | 5.60% | -1.42% | 33.33% | -10.17% | 0.07 | pass |
| BITCOIN_ETF | IBIT | crypto_proxies | 2026-07-13 | -2.49% | -2.28% | -34.25% | -47.60% | -3.54% | 37.39% | -11.79% | 50.00% | -50.60% | 1.81 | pass |
| ETHEREUM_ETF | ETHA | crypto_proxies | 2026-07-13 | -1.33% | 6.36% | -44.80% | -41.36% | 5.10% | 48.99% | -14.68% | 44.44% | -63.46% | 2.95 | pass |
