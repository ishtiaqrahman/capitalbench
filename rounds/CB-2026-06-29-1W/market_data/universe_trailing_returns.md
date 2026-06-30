# Full-Universe Price, Risk, And Benchmark Context

This table is mechanically calculated from adjusted close data. It is sorted in the option order from `options.yaml`, not by performance. CASH is shown as 0.00%.

Price-history note: trailing returns are descriptive context, not forecasts. Treat recent gains or losses as one input alongside catalysts, macro context, volatility, drawdown, benchmark-relative risk, and any valuation or fundamental facts supplied in the briefing.

Benchmark-relative values are asset return minus SPY return over the same window. Beta and correlation use available one-year daily adjusted-close returns.

- Source: tiingo_eod_adj_close; yahoo_chart_adjclose fallback for rows marked in CSV message
- As-of date requested: 2026-06-29
- Failed options: 0

| option_id | symbol | option_group | as_of_price_date | return_7d | return_30d | return_6m | return_1y | return_vs_sp500_30d | volatility_30d | max_drawdown_30d | up_day_share_30d | distance_from_52w_high | beta_to_sp500_1y | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | cash | 2026-06-29 | 0.00% | 0.00% | 0.00% | 0.00% | 1.79% | 0.00% | 0.00% |  |  | 0.00 | cash |
| SHORT_TREASURY | BIL | cash_and_short_duration | 2026-06-29 | 0.08% | 0.27% | 1.76% | 3.84% | 2.07% | 0.24% | -0.01% | 73.68% | 0.00% | -0.00 | pass |
| SP500 | SPY | us_broad_market | 2026-06-29 | -0.46% | -1.79% | 8.30% | 21.84% | 0.00% | 18.52% | -4.49% | 47.37% | -2.19% | 1.00 | pass |
| TOTAL_US_MARKET | VTI | us_broad_market | 2026-06-29 | -0.17% | -1.17% | 9.14% | 22.82% | 0.62% | 18.24% | -4.36% | 47.37% | -1.65% | 1.02 | pass |
| NASDAQ100 | QQQ | us_growth_and_technology | 2026-06-29 | -1.88% | -1.82% | 16.90% | 32.75% | -0.03% | 34.18% | -7.03% | 42.11% | -2.85% | 1.36 | pass |
| LARGE_GROWTH | IWF | us_style_factor | 2026-06-29 | 0.18% | -4.51% | 2.27% | 16.13% | -2.71% | 23.72% | -8.21% | 42.11% | -5.19% | 1.23 | pass |
| LARGE_VALUE | IWD | us_style_factor | 2026-06-29 | -0.32% | 2.33% | 15.28% | 27.59% | 4.13% | 15.70% | -2.40% | 57.89% | -0.68% | 0.75 | pass |
| MID_CAP | IJH | us_size_factor | 2026-06-29 | 0.60% | 2.84% | 14.90% | 25.01% | 4.64% | 16.67% | -2.40% | 63.16% | 0.00% | 1.01 | pass |
| SMALL_CAP | IWM | us_size_factor | 2026-06-29 | 0.26% | 3.19% | 20.14% | 40.19% | 4.98% | 22.71% | -3.55% | 63.16% | -0.29% | 1.27 | pass |
| SMALL_VALUE | IWN | us_style_factor | 2026-06-29 | 1.51% | 3.84% | 21.24% | 42.69% | 5.63% | 18.19% | -2.60% | 57.89% | -0.07% | 1.05 | pass |
| DIVIDEND | SCHD | us_factor_equity | 2026-06-29 | 0.92% | -0.97% | 17.51% | 25.44% | 0.82% | 10.86% | -2.93% | 47.37% | -1.97% | 0.31 | pass |
| LOW_VOL | SPLV | us_factor_equity | 2026-06-29 | 3.21% | 4.88% | 6.25% | 6.98% | 6.67% | 13.69% | -1.89% | 68.42% | -1.67% | 0.07 | pass |
| MOMENTUM | MTUM | us_factor_equity | 2026-06-29 | -2.67% | 6.51% | 32.81% | 42.35% | 8.30% | 48.31% | -7.46% | 57.89% | -2.67% | 1.47 | pass |
| TECHNOLOGY | XLK | us_sector | 2026-06-29 | -3.51% | -2.82% | 27.42% | 48.65% | -1.03% | 43.51% | -10.89% | 47.37% | -6.35% | 1.65 | pass |
| COMMUNICATIONS | XLC | us_sector | 2026-06-29 | 0.95% | -6.51% | -7.96% | 1.45% | -4.71% | 18.17% | -8.44% | 47.37% | -9.64% | 0.70 | pass |
| CONSUMER_DISCRETIONARY | XLY | us_sector | 2026-06-29 | 1.90% | -2.91% | -2.70% | 7.99% | -1.12% | 24.05% | -4.21% | 52.63% | -5.57% | 1.18 | pass |
| CONSUMER_STAPLES | XLP | us_sector | 2026-06-29 | 2.66% | 2.47% | 9.14% | 7.65% | 4.26% | 16.23% | -3.58% | 47.37% | -5.08% | -0.02 | pass |
| HEALTHCARE | XLV | us_sector | 2026-06-29 | 7.12% | 8.01% | 4.05% | 22.11% | 9.81% | 20.06% | -3.34% | 63.16% | 0.00% | 0.38 | pass |
| FINANCIALS | XLF | us_sector | 2026-06-29 | 0.04% | 4.51% | -2.05% | 5.03% | 6.31% | 14.57% | -1.44% | 63.16% | -3.93% | 0.67 | pass |
| INDUSTRIALS | XLI | us_sector | 2026-06-29 | 0.53% | 5.82% | 17.12% | 26.11% | 7.62% | 24.32% | -3.69% | 63.16% | -0.74% | 0.96 | pass |
| ENERGY | XLE | us_sector | 2026-06-29 | -0.89% | -4.13% | 21.74% | 29.54% | -2.33% | 22.99% | -8.48% | 47.37% | -13.74% | -0.15 | pass |
| MATERIALS | XLB | us_sector | 2026-06-29 | -1.86% | -0.59% | 11.66% | 17.38% | 1.21% | 23.43% | -3.93% | 52.63% | -4.75% | 0.78 | pass |
| UTILITIES | XLU | us_sector | 2026-06-29 | 2.91% | 4.26% | 8.81% | 16.32% | 6.06% | 13.99% | -1.87% | 78.95% | -2.29% | 0.19 | pass |
| REAL_ESTATE | XLRE | us_sector | 2026-06-29 | 2.04% | 3.01% | 12.28% | 13.01% | 4.80% | 18.65% | -3.31% | 63.16% | -0.71% | 0.33 | pass |
| INTERMEDIATE_TREASURY | IEF | bonds_and_rates | 2026-06-29 | 1.13% | 0.77% | 0.03% | 3.54% | 2.56% | 5.38% | -0.76% | 63.16% | -1.73% | 0.08 | pass |
| LONG_TREASURY | TLT | bonds_and_rates | 2026-06-29 | 1.58% | 2.37% | 1.17% | 4.63% | 4.17% | 8.95% | -1.20% | 57.89% | -2.26% | 0.14 | pass |
| TIPS | TIP | bonds_and_rates | 2026-06-29 | 0.88% | -0.03% | 1.44% | 3.93% | 1.76% | 4.47% | -0.98% | 52.63% | -0.20% | 0.07 | pass |
| INVESTMENT_GRADE_CREDIT | LQD | credit | 2026-06-29 | 0.85% | 0.69% | 0.91% | 5.27% | 2.49% | 5.17% | -0.80% | 47.37% | -0.30% | 0.18 | pass |
| HIGH_YIELD_CREDIT | HYG | credit | 2026-06-29 | 0.09% | 0.14% | 1.74% | 5.60% | 1.93% | 3.98% | -0.59% | 47.37% | -0.04% | 0.24 | pass |
| AGGREGATE_BONDS | AGG | bonds_and_rates | 2026-06-29 | 0.75% | 0.65% | 0.86% | 4.62% | 2.44% | 4.20% | -0.55% | 63.16% | -0.70% | 0.10 | pass |
| DEVELOPED_EX_US | VEA | international_equity | 2026-06-29 | -2.03% | -0.66% | 13.86% | 28.40% | 1.13% | 25.38% | -4.85% | 57.89% | -2.03% | 1.07 | pass |
| EMERGING_MARKETS | VWO | international_equity | 2026-06-29 | -3.36% | -1.05% | 10.52% | 22.96% | 0.74% | 25.62% | -5.67% | 47.37% | -3.36% | 1.07 | pass |
| EUROPE | VGK | international_equity | 2026-06-29 | -0.20% | 0.29% | 7.19% | 17.40% | 2.09% | 18.55% | -2.55% | 57.89% | -0.89% | 0.93 | pass |
| JAPAN | EWJ | international_equity | 2026-06-29 | -3.88% | 0.81% | 15.57% | 29.15% | 2.61% | 28.87% | -5.14% | 68.42% | -3.88% | 1.15 | pass |
| CHINA | MCHI | international_equity | 2026-06-29 | -3.92% | -7.21% | -15.31% | -6.21% | -5.42% | 21.79% | -11.15% | 36.84% | -22.75% | 0.91 | pass |
| INDIA | INDA | international_equity | 2026-06-29 | -1.48% | 1.28% | -8.02% | -11.96% | 3.07% | 16.58% | -1.71% | 57.89% | -11.93% | 0.60 | pass |
| GOLD | IAU | commodities | 2026-06-29 | -4.15% | -11.65% | -7.45% | 22.51% | -9.86% | 30.63% | -11.17% | 47.37% | -25.64% | 0.63 | pass |
| BROAD_COMMODITIES | PDBC | commodities | 2026-06-29 | -3.18% | -10.10% | 18.74% | 26.29% | -8.31% | 17.61% | -12.58% | 26.32% | -16.23% | -0.16 | pass |
| SEMICONDUCTORS | SMH | ai_and_technology | 2026-06-29 | -5.52% | 5.52% | 73.52% | 127.69% | 7.31% | 70.28% | -10.69% | 57.89% | -5.52% | 2.23 | pass |
| SOFTWARE | IGV | ai_and_technology | 2026-06-29 | 2.95% | -11.56% | -16.28% | -16.58% | -9.77% | 33.42% | -21.29% | 21.05% | -23.67% | 1.19 | pass |
| BROAD_AI_TECH | AIQ | ai_and_technology | 2026-06-29 | -4.28% | -4.60% | 24.83% | 48.20% | -2.81% | 51.05% | -12.52% | 52.63% | -8.44% | 1.82 | pass |
| AUTONOMOUS_ROBOTICS | ARKQ | ai_and_technology | 2026-06-29 | -1.27% | -10.14% | 10.59% | 45.71% | -8.34% | 45.82% | -12.87% | 36.84% | -10.73% | 2.13 | pass |
| CYBERSECURITY | CIBR | ai_and_technology | 2026-06-29 | 5.98% | -0.52% | 22.30% | 19.29% | 1.27% | 30.01% | -11.74% | 36.84% | -6.09% | 1.09 | pass |
| SOLAR | TAN | clean_energy | 2026-06-29 | -5.74% | -22.09% | 14.90% | 68.72% | -20.29% | 51.40% | -21.34% | 36.84% | -22.09% | 1.75 | pass |
| METALS_MINING | XME | commodities | 2026-06-29 | -7.55% | -14.87% | 1.09% | 61.06% | -13.07% | 46.43% | -19.75% | 31.58% | -19.75% | 1.68 | pass |
| EQUAL_WEIGHT_SP500 | RSP | us_broad_market | 2026-06-29 | 1.64% | 2.42% | 10.99% | 19.73% | 4.21% | 14.12% | -2.04% | 57.89% | 0.00% | 0.75 | pass |
| BIOTECH | XBI | healthcare_and_biotech | 2026-06-29 | 8.54% | 15.93% | 28.43% | 91.58% | 17.72% | 35.18% | -4.39% | 73.68% | 0.00% | 1.06 | pass |
| REGIONAL_BANKS | KRE | us_industry | 2026-06-29 | 3.83% | 8.01% | 14.69% | 28.79% | 9.81% | 21.14% | -3.08% | 78.95% | -0.56% | 0.83 | pass |
| AEROSPACE_DEFENSE | ITA | us_industry | 2026-06-29 | 1.54% | 1.64% | 10.35% | 28.15% | 3.43% | 28.24% | -3.00% | 52.63% | -4.44% | 1.00 | pass |
| CANADA | EWC | country_equity | 2026-06-29 | -0.69% | -1.78% | 6.31% | 27.85% | 0.01% | 15.74% | -3.20% | 52.63% | -2.86% | 0.79 | pass |
| UNITED_KINGDOM | EWU | country_equity | 2026-06-29 | 1.01% | -0.25% | 6.34% | 20.13% | 1.54% | 15.04% | -2.39% | 47.37% | -3.84% | 0.74 | pass |
| AUSTRALIA | EWA | country_equity | 2026-06-29 | -1.20% | -2.55% | 7.65% | 11.12% | -0.75% | 20.30% | -4.78% | 47.37% | -5.80% | 0.94 | pass |
| SOUTH_KOREA | EWY | country_equity | 2026-06-29 | -9.83% | -4.05% | 100.06% | 185.46% | -2.25% | 97.99% | -19.16% | 36.84% | -9.90% | 2.58 | pass |
| TAIWAN | EWT | country_equity | 2026-06-29 | -5.15% | 2.93% | 67.05% | 91.27% | 4.72% | 49.82% | -8.51% | 57.89% | -5.15% | 1.68 | pass |
| BRAZIL | EWZ | country_equity | 2026-06-29 | 0.82% | -2.87% | 11.38% | 28.29% | -1.08% | 22.38% | -5.84% | 42.11% | -16.42% | 0.99 | pass |
| MEXICO | EWW | country_equity | 2026-06-29 | 0.21% | -1.52% | 9.54% | 30.51% | 0.28% | 25.50% | -5.91% | 42.11% | -4.91% | 0.92 | pass |
| SOUTH_AFRICA | EZA | country_equity | 2026-06-29 | -2.64% | -6.63% | -5.29% | 29.86% | -4.83% | 37.97% | -8.61% | 57.89% | -20.58% | 1.58 | pass |
| MORTGAGE_BACKED_BONDS | MBB | bonds_and_rates | 2026-06-29 | 0.76% | 0.54% | 1.25% | 5.94% | 2.34% | 4.60% | -0.67% | 68.42% | -0.62% | 0.11 | pass |
| MUNICIPAL_BONDS | MUB | bonds_and_rates | 2026-06-29 | 0.36% | 0.77% | 1.97% | 6.60% | 2.56% | 2.33% | -0.35% | 52.63% | -0.05% | 0.07 | pass |
| EMERGING_MARKET_BONDS | EMB | credit | 2026-06-29 | 0.44% | 0.83% | 2.45% | 10.62% | 2.62% | 6.28% | -1.02% | 47.37% | 0.00% | 0.30 | pass |
| INTERNATIONAL_BONDS | BNDX | bonds_and_rates | 2026-06-29 | 0.52% | 0.63% | 1.46% | 2.53% | 2.42% | 3.24% | -0.62% | 63.16% | -0.48% | 0.11 | pass |
| SILVER | SLV | commodities | 2026-06-29 | -10.58% | -22.90% | -20.19% | 61.50% | -21.11% | 55.30% | -23.84% | 42.11% | -50.11% | 1.64 | pass |
| COPPER | CPER | commodities | 2026-06-29 | -4.07% | -4.19% | 8.92% | 17.56% | -2.40% | 33.13% | -10.57% | 52.63% | -8.30% | 1.22 | pass |
| AGRICULTURE | DBA | commodities | 2026-06-29 | -0.53% | -2.72% | 3.35% | 4.31% | -0.92% | 10.76% | -3.67% | 31.58% | -7.73% | 0.06 | pass |
| OIL | USO | commodities | 2026-06-29 | -4.98% | -17.05% | 53.83% | 46.12% | -15.26% | 40.93% | -25.12% | 36.84% | -29.99% | -0.98 | pass |
| US_DOLLAR | UUP | currencies | 2026-06-29 | 0.04% | 2.57% | 5.15% | 8.58% | 4.36% | 5.05% | -0.56% | 52.63% | -0.56% | -0.13 | pass |
| EURO | FXE | currencies | 2026-06-29 | 0.02% | -2.03% | -2.59% | -1.74% | -0.24% | 5.70% | -2.39% | 52.63% | -4.79% | 0.12 | pass |
| YEN | FXY | currencies | 2026-06-29 | -0.23% | -1.67% | -3.13% | -10.90% | 0.13% | 2.69% | -1.48% | 21.05% | -11.65% | 0.08 | pass |
| BITCOIN_ETF | IBIT | crypto_proxies | 2026-06-29 | -6.36% | -17.90% | -30.78% | -43.71% | -16.10% | 49.19% | -17.21% | 31.58% | -52.05% | 1.81 | pass |
| ETHEREUM_ETF | ETHA | crypto_proxies | 2026-06-29 | -6.28% | -19.47% | -44.62% | -33.00% | -17.68% | 74.58% | -22.30% | 31.58% | -66.55% | 2.97 | pass |
