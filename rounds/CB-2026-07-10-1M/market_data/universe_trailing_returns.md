# Full-Universe Price, Risk, And Benchmark Context

This table is mechanically calculated from adjusted close data. It is sorted in the option order from `options.yaml`, not by performance. CASH is shown as 0.00%.

Price-history note: trailing returns are descriptive context, not forecasts. Treat recent gains or losses as one input alongside catalysts, macro context, volatility, drawdown, benchmark-relative risk, and any valuation or fundamental facts supplied in the briefing.

Benchmark-relative values are asset return minus SPY return over the same window. Beta and correlation use available one-year daily adjusted-close returns.

- Source: tiingo_eod_adj_close; yahoo_chart_adjclose fallback for rows marked in CSV message
- As-of date requested: 2026-07-10
- Failed options: 0

| option_id | symbol | option_group | as_of_price_date | return_7d | return_30d | return_6m | return_1y | return_vs_sp500_30d | volatility_30d | max_drawdown_30d | up_day_share_30d | distance_from_52w_high | beta_to_sp500_1y | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | cash | 2026-07-10 | 0.00% | 0.00% | 0.00% | 0.00% | -4.34% | 0.00% | 0.00% |  |  | 0.00 | cash |
| SHORT_TREASURY | BIL | cash_and_short_duration | 2026-07-10 | 0.07% | 0.33% | 1.78% | 3.84% | -4.01% | 0.26% | -0.01% | 75.00% | 0.00% | -0.00 | pass |
| SP500 | SPY | us_broad_market | 2026-07-10 | 1.37% | 4.34% | 9.35% | 21.97% | 0.00% | 14.77% | -3.17% | 50.00% | -0.35% | 1.00 | pass |
| TOTAL_US_MARKET | VTI | us_broad_market | 2026-07-10 | 1.07% | 4.39% | 9.50% | 22.29% | 0.05% | 14.11% | -2.49% | 50.00% | -0.16% | 1.01 | pass |
| NASDAQ100 | QQQ | us_growth_and_technology | 2026-07-10 | 1.81% | 4.70% | 16.05% | 31.25% | 0.36% | 29.98% | -4.93% | 55.00% | -2.66% | 1.37 | pass |
| LARGE_GROWTH | IWF | us_style_factor | 2026-07-10 | 2.30% | 3.65% | 4.30% | 16.08% | -0.69% | 21.99% | -5.03% | 55.00% | -3.66% | 1.24 | pass |
| LARGE_VALUE | IWD | us_style_factor | 2026-07-10 | 0.01% | 5.26% | 14.23% | 27.13% | 0.92% | 13.25% | -1.39% | 65.00% | -0.36% | 0.74 | pass |
| MID_CAP | IJH | us_size_factor | 2026-07-10 | -0.55% | 3.00% | 10.02% | 19.80% | -1.34% | 15.41% | -3.09% | 55.00% | -1.87% | 1.01 | pass |
| SMALL_CAP | IWM | us_size_factor | 2026-07-10 | -0.53% | 5.19% | 14.21% | 33.03% | 0.85% | 16.74% | -2.32% | 55.00% | -1.48% | 1.27 | pass |
| SMALL_VALUE | IWN | us_style_factor | 2026-07-10 | -0.61% | 4.67% | 15.83% | 34.20% | 0.33% | 13.39% | -1.83% | 55.00% | -0.80% | 1.04 | pass |
| DIVIDEND | SCHD | us_factor_equity | 2026-07-10 | 0.03% | 1.23% | 15.35% | 22.08% | -3.10% | 12.47% | -2.93% | 50.00% | -0.52% | 0.30 | pass |
| LOW_VOL | SPLV | us_factor_equity | 2026-07-10 | -1.16% | 2.83% | 6.74% | 6.18% | -1.51% | 14.49% | -1.89% | 55.00% | -1.40% | 0.06 | pass |
| MOMENTUM | MTUM | us_factor_equity | 2026-07-10 | 1.66% | 5.64% | 25.45% | 36.38% | 1.30% | 45.79% | -9.50% | 65.00% | -6.79% | 1.50 | pass |
| TECHNOLOGY | XLK | us_sector | 2026-07-10 | 2.87% | 5.31% | 27.42% | 45.34% | 0.97% | 37.91% | -6.75% | 60.00% | -6.16% | 1.67 | pass |
| COMMUNICATIONS | XLC | us_sector | 2026-07-10 | 1.86% | 0.83% | -4.77% | 5.95% | -3.50% | 19.65% | -5.75% | 60.00% | -6.49% | 0.69 | pass |
| CONSUMER_DISCRETIONARY | XLY | us_sector | 2026-07-10 | 0.10% | 3.51% | -5.39% | 6.74% | -0.82% | 22.44% | -4.21% | 60.00% | -5.47% | 1.18 | pass |
| CONSUMER_STAPLES | XLP | us_sector | 2026-07-10 | -1.02% | -0.92% | 7.49% | 6.60% | -5.25% | 17.78% | -3.57% | 45.00% | -5.36% | -0.04 | pass |
| HEALTHCARE | XLV | us_sector | 2026-07-10 | -1.77% | 5.69% | 3.11% | 20.04% | 1.35% | 20.57% | -3.04% | 55.00% | -2.19% | 0.35 | pass |
| FINANCIALS | XLF | us_sector | 2026-07-10 | 0.16% | 7.03% | 0.82% | 7.32% | 2.70% | 15.17% | -2.08% | 65.00% | -0.77% | 0.66 | pass |
| INDUSTRIALS | XLI | us_sector | 2026-07-10 | -1.08% | 7.49% | 12.93% | 22.23% | 3.15% | 20.96% | -2.77% | 70.00% | -1.96% | 0.97 | pass |
| ENERGY | XLE | us_sector | 2026-07-10 | 3.49% | -4.77% | 19.63% | 27.99% | -9.11% | 23.31% | -8.69% | 40.00% | -11.33% | -0.18 | pass |
| MATERIALS | XLB | us_sector | 2026-07-10 | -2.15% | 2.98% | 6.31% | 12.30% | -1.35% | 22.22% | -4.50% | 60.00% | -4.32% | 0.78 | pass |
| UTILITIES | XLU | us_sector | 2026-07-10 | -0.76% | 3.86% | 8.25% | 13.04% | -0.48% | 15.56% | -3.10% | 65.00% | -3.59% | 0.17 | pass |
| REAL_ESTATE | XLRE | us_sector | 2026-07-10 | -0.51% | -0.34% | 11.44% | 10.48% | -4.68% | 18.29% | -3.31% | 55.00% | -1.75% | 0.31 | pass |
| INTERMEDIATE_TREASURY | IEF | bonds_and_rates | 2026-07-10 | -0.52% | 0.27% | -0.86% | 2.67% | -4.07% | 5.57% | -1.31% | 60.00% | -2.89% | 0.08 | pass |
| LONG_TREASURY | TLT | bonds_and_rates | 2026-07-10 | -1.22% | -0.11% | -1.75% | 1.54% | -4.45% | 10.18% | -3.17% | 45.00% | -5.24% | 0.13 | pass |
| TIPS | TIP | bonds_and_rates | 2026-07-10 | -0.18% | -0.02% | 0.76% | 3.13% | -4.36% | 4.42% | -0.78% | 60.00% | -0.85% | 0.07 | pass |
| INVESTMENT_GRADE_CREDIT | LQD | credit | 2026-07-10 | -1.09% | -0.30% | -0.67% | 3.37% | -4.64% | 5.49% | -1.70% | 50.00% | -1.99% | 0.18 | pass |
| HIGH_YIELD_CREDIT | HYG | credit | 2026-07-10 | 0.00% | 0.77% | 1.36% | 5.48% | -3.57% | 3.23% | -0.39% | 40.00% | -0.20% | 0.23 | pass |
| AGGREGATE_BONDS | AGG | bonds_and_rates | 2026-07-10 | -0.54% | 0.10% | -0.12% | 3.63% | -4.24% | 4.28% | -1.01% | 60.00% | -1.66% | 0.10 | pass |
| DEVELOPED_EX_US | VEA | international_equity | 2026-07-10 | 0.25% | 3.71% | 10.78% | 27.35% | -0.63% | 21.48% | -3.07% | 65.00% | -1.93% | 1.07 | pass |
| EMERGING_MARKETS | VWO | international_equity | 2026-07-10 | 1.44% | 3.88% | 8.17% | 23.73% | -0.46% | 21.82% | -4.34% | 55.00% | -2.20% | 1.08 | pass |
| EUROPE | VGK | international_equity | 2026-07-10 | -0.87% | 3.56% | 5.17% | 16.03% | -0.78% | 17.00% | -2.09% | 60.00% | -1.56% | 0.94 | pass |
| JAPAN | EWJ | international_equity | 2026-07-10 | 1.51% | 6.45% | 12.34% | 35.25% | 2.12% | 25.90% | -4.57% | 70.00% | -2.50% | 1.16 | pass |
| CHINA | MCHI | international_equity | 2026-07-10 | 4.36% | -1.17% | -14.05% | -1.59% | -5.50% | 19.07% | -8.10% | 50.00% | -19.19% | 0.92 | pass |
| INDIA | INDA | international_equity | 2026-07-10 | -0.52% | 4.23% | -7.29% | -10.80% | -0.11% | 15.29% | -2.54% | 65.00% | -10.83% | 0.62 | pass |
| GOLD | IAU | commodities | 2026-07-10 | -0.32% | 0.61% | -8.99% | 23.28% | -3.73% | 25.06% | -7.99% | 50.00% | -23.93% | 0.64 | pass |
| BROAD_COMMODITIES | PDBC | commodities | 2026-07-10 | 3.59% | -5.68% | 21.24% | 28.83% | -10.02% | 19.37% | -9.47% | 35.00% | -13.06% | -0.17 | pass |
| SEMICONDUCTORS | SMH | ai_and_technology | 2026-07-10 | 3.16% | 7.03% | 56.99% | 113.17% | 2.69% | 63.24% | -13.08% | 65.00% | -8.65% | 2.26 | pass |
| SOFTWARE | IGV | ai_and_technology | 2026-07-10 | -1.24% | 0.92% | -11.97% | -15.32% | -3.41% | 28.58% | -8.55% | 45.00% | -21.53% | 1.19 | pass |
| BROAD_AI_TECH | AIQ | ai_and_technology | 2026-07-10 | 2.57% | 3.39% | 20.66% | 45.47% | -0.95% | 42.93% | -7.81% | 60.00% | -9.55% | 1.85 | pass |
| AUTONOMOUS_ROBOTICS | ARKQ | ai_and_technology | 2026-07-10 | -3.09% | -0.29% | -4.06% | 36.92% | -4.63% | 38.85% | -8.23% | 35.00% | -13.79% | 2.15 | pass |
| CYBERSECURITY | CIBR | ai_and_technology | 2026-07-10 | 1.33% | 10.46% | 26.97% | 25.33% | 6.12% | 26.23% | -3.12% | 50.00% | -2.52% | 1.10 | pass |
| SOLAR | TAN | clean_energy | 2026-07-10 | -2.41% | -7.10% | 9.26% | 41.21% | -11.44% | 42.84% | -14.10% | 45.00% | -25.66% | 1.76 | pass |
| METALS_MINING | XME | commodities | 2026-07-10 | -1.37% | -7.71% | -11.18% | 44.25% | -12.05% | 33.31% | -15.43% | 45.00% | -21.88% | 1.68 | pass |
| EQUAL_WEIGHT_SP500 | RSP | us_broad_market | 2026-07-10 | -0.28% | 4.16% | 9.33% | 17.25% | -0.17% | 12.13% | -1.83% | 65.00% | -0.33% | 0.74 | pass |
| BIOTECH | XBI | healthcare_and_biotech | 2026-07-10 | -0.89% | 23.54% | 27.86% | 80.74% | 19.20% | 26.39% | -3.20% | 75.00% | -3.20% | 1.02 | pass |
| REGIONAL_BANKS | KRE | us_industry | 2026-07-10 | 0.00% | 5.32% | 12.46% | 20.87% | 0.99% | 20.00% | -3.73% | 70.00% | -1.52% | 0.84 | pass |
| AEROSPACE_DEFENSE | ITA | us_industry | 2026-07-10 | -3.68% | 6.38% | 2.75% | 27.36% | 2.05% | 26.09% | -4.67% | 60.00% | -4.67% | 1.01 | pass |
| CANADA | EWC | country_equity | 2026-07-10 | 1.52% | 2.10% | 7.86% | 28.10% | -2.23% | 10.48% | -3.08% | 70.00% | -0.90% | 0.78 | pass |
| UNITED_KINGDOM | EWU | country_equity | 2026-07-10 | -1.19% | 3.19% | 5.54% | 19.67% | -1.15% | 16.39% | -2.28% | 45.00% | -2.89% | 0.73 | pass |
| AUSTRALIA | EWA | country_equity | 2026-07-10 | 1.28% | 2.39% | 9.87% | 10.42% | -1.95% | 16.89% | -4.42% | 55.00% | -4.65% | 0.93 | pass |
| SOUTH_KOREA | EWY | country_equity | 2026-07-10 | 1.88% | 2.84% | 68.54% | 156.63% | -1.50% | 85.64% | -17.82% | 50.00% | -16.28% | 2.61 | pass |
| TAIWAN | EWT | country_equity | 2026-07-10 | 1.27% | 8.36% | 61.09% | 90.28% | 4.02% | 45.69% | -8.65% | 65.00% | -4.79% | 1.69 | pass |
| BRAZIL | EWZ | country_equity | 2026-07-10 | 4.36% | 7.38% | 9.72% | 35.56% | 3.04% | 20.37% | -2.99% | 45.00% | -13.08% | 1.00 | pass |
| MEXICO | EWW | country_equity | 2026-07-10 | -0.85% | 2.08% | 6.89% | 28.43% | -2.26% | 23.00% | -5.37% | 50.00% | -6.49% | 0.92 | pass |
| SOUTH_AFRICA | EZA | country_equity | 2026-07-10 | -0.28% | 3.17% | -7.81% | 27.44% | -1.17% | 31.20% | -8.61% | 55.00% | -20.13% | 1.58 | pass |
| MORTGAGE_BACKED_BONDS | MBB | bonds_and_rates | 2026-07-10 | -0.44% | 0.16% | -0.09% | 4.88% | -4.18% | 4.80% | -0.99% | 60.00% | -1.58% | 0.11 | pass |
| MUNICIPAL_BONDS | MUB | bonds_and_rates | 2026-07-10 | -0.46% | 0.45% | 0.99% | 5.97% | -3.89% | 2.52% | -0.61% | 60.00% | -0.52% | 0.07 | pass |
| EMERGING_MARKET_BONDS | EMB | credit | 2026-07-10 | -0.22% | 1.09% | 2.24% | 9.51% | -3.25% | 5.37% | -0.65% | 50.00% | -0.44% | 0.29 | pass |
| INTERNATIONAL_BONDS | BNDX | bonds_and_rates | 2026-07-10 | -0.33% | 0.61% | 0.42% | 2.09% | -3.73% | 3.77% | -1.19% | 55.00% | -1.16% | 0.11 | pass |
| SILVER | SLV | commodities | 2026-07-10 | -1.94% | -6.43% | -25.46% | 59.85% | -10.77% | 49.87% | -18.42% | 50.00% | -48.91% | 1.67 | pass |
| COPPER | CPER | commodities | 2026-07-10 | 1.88% | 0.72% | 5.09% | 9.17% | -3.62% | 27.47% | -8.42% | 55.00% | -6.43% | 1.23 | pass |
| AGRICULTURE | DBA | commodities | 2026-07-10 | 3.85% | 5.47% | 7.72% | 11.63% | 1.13% | 13.91% | -1.52% | 60.00% | -3.34% | 0.07 | pass |
| OIL | USO | commodities | 2026-07-10 | 4.54% | -19.06% | 53.57% | 44.18% | -23.40% | 41.87% | -23.10% | 35.00% | -28.94% | -1.00 | pass |
| US_DOLLAR | UUP | currencies | 2026-07-10 | 0.18% | 1.21% | 3.88% | 8.19% | -3.13% | 5.04% | -0.74% | 50.00% | -0.49% | -0.13 | pass |
| EURO | FXE | currencies | 2026-07-10 | -0.16% | -1.11% | -1.55% | -1.70% | -5.44% | 5.32% | -2.19% | 45.00% | -4.86% | 0.13 | pass |
| YEN | FXY | currencies | 2026-07-10 | -0.37% | -0.75% | -2.56% | -9.86% | -5.09% | 5.45% | -1.74% | 35.00% | -9.86% | 0.07 | pass |
| BITCOIN_ETF | IBIT | crypto_proxies | 2026-07-10 | 3.90% | 3.28% | -29.18% | -43.83% | -1.06% | 39.56% | -11.79% | 55.00% | -49.18% | 1.79 | pass |
| ETHEREUM_ETF | ETHA | crypto_proxies | 2026-07-10 | 5.21% | 10.18% | -41.66% | -36.63% | 5.84% | 58.39% | -14.68% | 50.00% | -63.02% | 2.93 | pass |
