# Full-Universe Price, Risk, And Benchmark Context

This table is mechanically calculated from adjusted close data. It is sorted in the option order from `options.yaml`, not by performance. CASH is shown as 0.00%.

Price-history note: trailing returns are descriptive context, not forecasts. Treat recent gains or losses as one input alongside catalysts, macro context, volatility, drawdown, benchmark-relative risk, and any valuation or fundamental facts supplied in the briefing.

Benchmark-relative values are asset return minus SPY return over the same window. Beta and correlation use available one-year daily adjusted-close returns.

- Source: tiingo_eod_adj_close; yahoo_chart_adjclose fallback for rows marked in CSV message
- As-of date requested: 2026-07-06
- Failed options: 0

| option_id | symbol | option_group | as_of_price_date | return_7d | return_30d | return_6m | return_1y | return_vs_sp500_30d | volatility_30d | max_drawdown_30d | up_day_share_30d | distance_from_52w_high | beta_to_sp500_1y | status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CASH |  | cash | 2026-07-06 | 0.00% | 0.00% | 0.00% | 0.00% | -2.12% | 0.00% | 0.00% |  |  | 0.00 | cash |
| SHORT_TREASURY | BIL | cash_and_short_duration | 2026-07-06 | 0.06% | 0.27% | 1.45% | 3.50% | -1.85% | 0.25% | -0.01% | 72.22% | -0.01% | -0.00 | pass |
| SP500 | SPY | us_broad_market | 2026-07-06 | 1.39% | 2.12% | 9.17% | 21.47% | 0.00% | 16.57% | -3.17% | 44.44% | -0.84% | 1.00 | pass |
| TOTAL_US_MARKET | VTI | us_broad_market | 2026-07-06 | 1.24% | 2.58% | 9.58% | 22.07% | 0.45% | 15.78% | -2.49% | 44.44% | -0.43% | 1.01 | pass |
| NASDAQ100 | QQQ | us_growth_and_technology | 2026-07-06 | -0.17% | 2.63% | 16.22% | 30.58% | 0.51% | 31.71% | -4.93% | 44.44% | -3.02% | 1.37 | pass |
| LARGE_GROWTH | IWF | us_style_factor | 2026-07-06 | 0.84% | 0.34% | 3.60% | 15.31% | -1.78% | 23.63% | -5.03% | 44.44% | -4.40% | 1.24 | pass |
| LARGE_VALUE | IWD | us_style_factor | 2026-07-06 | 1.85% | 4.91% | 14.96% | 27.29% | 2.78% | 14.28% | -1.39% | 61.11% | 0.00% | 0.74 | pass |
| MID_CAP | IJH | us_size_factor | 2026-07-06 | -0.14% | 3.60% | 11.68% | 21.36% | 1.47% | 15.55% | -1.55% | 61.11% | -0.89% | 1.00 | pass |
| SMALL_CAP | IWM | us_size_factor | 2026-07-06 | -0.02% | 6.38% | 17.21% | 35.38% | 4.25% | 16.58% | -1.62% | 61.11% | -0.52% | 1.27 | pass |
| SMALL_VALUE | IWN | us_style_factor | 2026-07-06 | 0.21% | 6.25% | 18.73% | 36.70% | 4.13% | 12.81% | -1.77% | 55.56% | 0.00% | 1.03 | pass |
| DIVIDEND | SCHD | us_factor_equity | 2026-07-06 | 0.97% | 0.61% | 16.67% | 22.21% | -1.51% | 12.50% | -2.93% | 50.00% | -1.02% | 0.30 | pass |
| LOW_VOL | SPLV | us_factor_equity | 2026-07-06 | 0.77% | 3.87% | 7.51% | 6.40% | 1.75% | 14.47% | -1.89% | 61.11% | -0.91% | 0.06 | pass |
| MOMENTUM | MTUM | us_factor_equity | 2026-07-06 | -4.25% | 5.09% | 24.89% | 35.35% | 2.96% | 47.53% | -8.31% | 55.56% | -6.81% | 1.49 | pass |
| TECHNOLOGY | XLK | us_sector | 2026-07-06 | -0.99% | 1.94% | 25.48% | 43.63% | -0.19% | 39.76% | -6.02% | 50.00% | -7.28% | 1.66 | pass |
| COMMUNICATIONS | XLC | us_sector | 2026-07-06 | 2.16% | -1.05% | -5.52% | 3.29% | -3.17% | 19.25% | -5.76% | 55.56% | -7.69% | 0.69 | pass |
| CONSUMER_DISCRETIONARY | XLY | us_sector | 2026-07-06 | 0.76% | 2.95% | -2.14% | 7.52% | 0.82% | 23.51% | -4.21% | 61.11% | -4.85% | 1.18 | pass |
| CONSUMER_STAPLES | XLP | us_sector | 2026-07-06 | -0.32% | 1.49% | 9.93% | 5.17% | -0.63% | 18.70% | -3.58% | 50.00% | -5.39% | -0.03 | pass |
| HEALTHCARE | XLV | us_sector | 2026-07-06 | 0.76% | 6.32% | 3.32% | 21.62% | 4.19% | 20.84% | -3.34% | 61.11% | -1.09% | 0.36 | pass |
| FINANCIALS | XLF | us_sector | 2026-07-06 | 4.50% | 7.72% | 0.40% | 7.18% | 5.59% | 13.46% | -1.44% | 66.67% | 0.00% | 0.66 | pass |
| INDUSTRIALS | XLI | us_sector | 2026-07-06 | 1.53% | 6.80% | 15.13% | 25.79% | 4.67% | 24.76% | -3.38% | 72.22% | 0.00% | 0.97 | pass |
| ENERGY | XLE | us_sector | 2026-07-06 | -0.84% | -7.21% | 18.02% | 25.90% | -9.33% | 20.94% | -8.81% | 33.33% | -14.46% | -0.16 | pass |
| MATERIALS | XLB | us_sector | 2026-07-06 | 2.61% | 3.05% | 10.33% | 15.85% | 0.93% | 22.85% | -3.55% | 61.11% | -2.26% | 0.77 | pass |
| UTILITIES | XLU | us_sector | 2026-07-06 | -1.56% | 2.79% | 6.99% | 13.79% | 0.67% | 15.83% | -3.10% | 72.22% | -3.82% | 0.18 | pass |
| REAL_ESTATE | XLRE | us_sector | 2026-07-06 | -1.40% | -0.05% | 10.51% | 9.61% | -2.17% | 19.18% | -3.31% | 55.56% | -2.10% | 0.31 | pass |
| INTERMEDIATE_TREASURY | IEF | bonds_and_rates | 2026-07-06 | -0.60% | 0.93% | -0.62% | 2.93% | -1.19% | 5.46% | -0.76% | 66.67% | -2.65% | 0.08 | pass |
| LONG_TREASURY | TLT | bonds_and_rates | 2026-07-06 | -1.93% | 0.83% | -0.27% | 2.33% | -1.29% | 10.16% | -1.93% | 50.00% | -4.52% | 0.13 | pass |
| TIPS | TIP | bonds_and_rates | 2026-07-06 | -0.32% | 0.27% | 0.02% | 2.43% | -1.85% | 4.56% | -0.78% | 61.11% | -1.66% | 0.07 | pass |
| INVESTMENT_GRADE_CREDIT | LQD | credit | 2026-07-06 | -0.59% | 0.82% | 0.22% | 3.83% | -1.31% | 5.12% | -0.78% | 55.56% | -1.26% | 0.18 | pass |
| HIGH_YIELD_CREDIT | HYG | credit | 2026-07-06 | 0.29% | 1.02% | 1.18% | 4.84% | -1.10% | 3.38% | -0.39% | 44.44% | -0.09% | 0.23 | pass |
| AGGREGATE_BONDS | AGG | bonds_and_rates | 2026-07-06 | -0.38% | 0.84% | 0.28% | 3.88% | -1.29% | 4.08% | -0.54% | 66.67% | -1.41% | 0.10 | pass |
| DEVELOPED_EX_US | VEA | international_equity | 2026-07-06 | 1.37% | 4.48% | 12.86% | 29.27% | 2.36% | 22.38% | -3.07% | 61.11% | -0.69% | 1.07 | pass |
| EMERGING_MARKETS | VWO | international_equity | 2026-07-06 | 1.50% | 3.64% | 8.19% | 23.23% | 1.51% | 22.05% | -4.34% | 50.00% | -1.91% | 1.07 | pass |
| EUROPE | VGK | international_equity | 2026-07-06 | 2.16% | 4.67% | 7.24% | 19.27% | 2.54% | 17.79% | -2.08% | 61.11% | 0.00% | 0.93 | pass |
| JAPAN | EWJ | international_equity | 2026-07-06 | 2.21% | 5.59% | 15.31% | 33.21% | 3.46% | 26.73% | -4.50% | 66.67% | -1.75% | 1.15 | pass |
| CHINA | MCHI | international_equity | 2026-07-06 | 2.42% | -3.81% | -16.50% | -3.13% | -5.94% | 18.36% | -8.10% | 50.00% | -20.88% | 0.92 | pass |
| INDIA | INDA | international_equity | 2026-07-06 | 1.42% | 5.37% | -7.77% | -10.59% | 3.24% | 14.15% | -1.70% | 66.67% | -10.43% | 0.60 | pass |
| GOLD | IAU | commodities | 2026-07-06 | 3.67% | -3.60% | -7.47% | 24.54% | -5.72% | 30.53% | -7.99% | 50.00% | -22.91% | 0.64 | pass |
| BROAD_COMMODITIES | PDBC | commodities | 2026-07-06 | 1.64% | -7.79% | 18.91% | 25.56% | -9.91% | 17.53% | -10.44% | 27.78% | -14.86% | -0.15 | pass |
| SEMICONDUCTORS | SMH | ai_and_technology | 2026-07-06 | -4.38% | 6.08% | 55.90% | 113.73% | 3.95% | 65.90% | -11.45% | 55.56% | -9.66% | 2.25 | pass |
| SOFTWARE | IGV | ai_and_technology | 2026-07-06 | 5.45% | -1.09% | -9.64% | -14.79% | -3.21% | 30.68% | -11.37% | 44.44% | -19.51% | 1.18 | pass |
| BROAD_AI_TECH | AIQ | ai_and_technology | 2026-07-06 | -0.59% | 2.11% | 21.25% | 45.22% | -0.01% | 45.43% | -7.81% | 55.56% | -8.98% | 1.85 | pass |
| AUTONOMOUS_ROBOTICS | ARKQ | ai_and_technology | 2026-07-06 | 1.34% | 0.39% | 3.16% | 46.95% | -1.73% | 40.45% | -8.23% | 33.33% | -9.53% | 2.14 | pass |
| CYBERSECURITY | CIBR | ai_and_technology | 2026-07-06 | 4.98% | 7.25% | 29.04% | 23.02% | 5.13% | 25.63% | -3.34% | 50.00% | -1.41% | 1.10 | pass |
| SOLAR | TAN | clean_energy | 2026-07-06 | -0.10% | -10.16% | 11.71% | 48.57% | -12.29% | 44.86% | -11.42% | 38.89% | -22.17% | 1.75 | pass |
| METALS_MINING | XME | commodities | 2026-07-06 | -0.41% | -10.50% | -7.65% | 51.94% | -12.62% | 34.65% | -13.43% | 38.89% | -20.08% | 1.68 | pass |
| EQUAL_WEIGHT_SP500 | RSP | us_broad_market | 2026-07-06 | 0.92% | 3.85% | 10.03% | 18.03% | 1.73% | 12.97% | -1.83% | 66.67% | 0.00% | 0.74 | pass |
| BIOTECH | XBI | healthcare_and_biotech | 2026-07-06 | 1.58% | 25.10% | 31.84% | 89.52% | 22.98% | 24.56% | -1.93% | 77.78% | 0.00% | 1.04 | pass |
| REGIONAL_BANKS | KRE | us_industry | 2026-07-06 | 1.08% | 8.31% | 13.70% | 22.40% | 6.19% | 17.60% | -3.08% | 77.78% | -0.81% | 0.82 | pass |
| AEROSPACE_DEFENSE | ITA | us_industry | 2026-07-06 | 4.87% | 9.37% | 9.08% | 34.89% | 7.25% | 25.93% | -3.00% | 72.22% | 0.00% | 1.01 | pass |
| CANADA | EWC | country_equity | 2026-07-06 | 0.99% | 0.52% | 6.74% | 26.10% | -1.60% | 10.46% | -3.08% | 61.11% | -1.90% | 0.78 | pass |
| UNITED_KINGDOM | EWU | country_equity | 2026-07-06 | 2.32% | 3.27% | 6.32% | 22.61% | 1.15% | 16.91% | -2.28% | 44.44% | -1.61% | 0.73 | pass |
| AUSTRALIA | EWA | country_equity | 2026-07-06 | 0.78% | 2.38% | 8.45% | 10.34% | 0.26% | 17.48% | -4.42% | 55.56% | -5.06% | 0.93 | pass |
| SOUTH_KOREA | EWY | country_equity | 2026-07-06 | -3.87% | 8.37% | 76.42% | 167.01% | 6.24% | 89.51% | -17.82% | 44.44% | -13.39% | 2.60 | pass |
| TAIWAN | EWT | country_equity | 2026-07-06 | 1.40% | 9.37% | 62.95% | 88.76% | 7.25% | 44.68% | -7.82% | 61.11% | -3.82% | 1.68 | pass |
| BRAZIL | EWZ | country_equity | 2026-07-06 | 1.07% | 3.65% | 6.47% | 24.49% | 1.53% | 18.07% | -2.99% | 44.44% | -15.52% | 0.98 | pass |
| MEXICO | EWW | country_equity | 2026-07-06 | 0.41% | 3.27% | 10.73% | 28.11% | 1.14% | 22.80% | -5.37% | 50.00% | -4.52% | 0.92 | pass |
| SOUTH_AFRICA | EZA | country_equity | 2026-07-06 | 1.91% | 2.60% | -9.20% | 27.14% | 0.48% | 33.77% | -8.61% | 55.56% | -19.06% | 1.57 | pass |
| MORTGAGE_BACKED_BONDS | MBB | bonds_and_rates | 2026-07-06 | -0.37% | 0.94% | 0.68% | 5.28% | -1.19% | 4.65% | -0.65% | 72.22% | -1.34% | 0.11 | pass |
| MUNICIPAL_BONDS | MUB | bonds_and_rates | 2026-07-06 | 0.14% | 0.83% | 1.48% | 6.23% | -1.29% | 2.13% | -0.21% | 61.11% | -0.17% | 0.07 | pass |
| EMERGING_MARKET_BONDS | EMB | credit | 2026-07-06 | -0.07% | 1.42% | 2.20% | 9.16% | -0.71% | 5.63% | -0.49% | 50.00% | -0.07% | 0.29 | pass |
| INTERNATIONAL_BONDS | BNDX | bonds_and_rates | 2026-07-06 | -0.39% | 0.67% | 0.68% | 1.86% | -1.46% | 2.97% | -0.39% | 55.56% | -1.10% | 0.11 | pass |
| SILVER | SLV | commodities | 2026-07-06 | 6.51% | -8.87% | -23.88% | 67.44% | -10.99% | 52.23% | -18.42% | 50.00% | -46.87% | 1.65 | pass |
| COPPER | CPER | commodities | 2026-07-06 | 1.64% | -0.63% | 1.53% | 18.58% | -2.75% | 28.84% | -8.42% | 55.56% | -6.80% | 1.22 | pass |
| AGRICULTURE | DBA | commodities | 2026-07-06 | 3.89% | 4.32% | 6.58% | 10.21% | 2.19% | 14.79% | -1.52% | 50.00% | -4.14% | 0.07 | pass |
| OIL | USO | commodities | 2026-07-06 | -2.55% | -21.55% | 52.31% | 38.78% | -23.68% | 37.42% | -23.59% | 33.33% | -31.78% | -0.97 | pass |
| US_DOLLAR | UUP | currencies | 2026-07-06 | -0.18% | 1.07% | 4.27% | 8.55% | -1.05% | 5.23% | -0.74% | 50.00% | -0.74% | -0.13 | pass |
| EURO | FXE | currencies | 2026-07-06 | 0.18% | -0.61% | -1.79% | -2.04% | -2.74% | 5.56% | -2.19% | 55.56% | -4.68% | 0.12 | pass |
| YEN | FXY | currencies | 2026-07-06 | -0.12% | -1.26% | -3.51% | -10.91% | -3.38% | 5.31% | -1.74% | 22.22% | -10.32% | 0.07 | pass |
| BITCOIN_ETF | IBIT | crypto_proxies | 2026-07-06 | 5.68% | 5.80% | -31.13% | -41.92% | 3.68% | 40.83% | -11.79% | 44.44% | -49.33% | 1.79 | pass |
| ETHEREUM_ETF | ETHA | crypto_proxies | 2026-07-06 | 10.70% | 14.15% | -44.69% | -30.48% | 12.03% | 60.90% | -14.68% | 44.44% | -62.97% | 2.95 | pass |
