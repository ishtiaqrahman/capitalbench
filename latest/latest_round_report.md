# CapitalBench Latest Round Leaderboard

## Round

- Round ID: CB-2026-08-21-1W
- Decision deadline: 2026-08-21T13:25:00Z
- Horizon: one week
- Official run ID: official-v3-20260821-weekly
- Mock: no

## Model Decisions

| model_id | provider | submission_format | selected_option_id | holding_count | confidence | rationale_summary | key_risks |
| --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | anthropic | portfolio | CYBERSECURITY | 3 | 0.5833 | SPY fell 1.96% over the week with VIX up to 16 and yields rising; dispersion is elevated (4.38%). High-quality tech/growth pullbacks (cybersecurity, software, defense) sit against a strong prior relative trend, with the NVIDIA earnings catalyst on Aug 26 inside the window offering a mean-reversion path if results support the AI trade. Crypto has extreme short-term continuation but poor quality and heavy 52w-high distance, arguing against chasing. | NVIDIA earnings on Aug 26 could disappoint and extend the tech/growth selloff; Rising long-end yields (10y ~4.70%, 30y ~5.23%) pressure high-beta growth exposures; Hawkish FOMC minutes tone and sticky inflation prints (PCE Aug 26) could deepen risk-off; Persian Gulf oil disruption could push energy higher at the expense of the picked sectors |
| openai-gpt-5-6-sol | openai | portfolio | CYBERSECURITY | 3 | 0.5833 | High cross-sectional dispersion, weak near-term breadth, rising yields, and major inflation and NVIDIA event risk favor selective reversal trades over broad continuation. Strong prior trends followed by sharp relative pullbacks offer the clearest one-week opportunities. | Hot PCE or durable-goods data could push yields higher and extend growth-sector weakness.; NVIDIA results could trigger a broad technology selloff despite selective reversal signals.; A worsening Persian Gulf disruption could produce an oil and inflation shock that pressures equities.; The recent pullbacks may reflect a durable factor rotation rather than temporary overreaction. |
| anthropic-claude-opus-5 | anthropic | portfolio | CYBERSECURITY | 3 | 0.5633 | Equities pulled back ~2% on the week with VIX up to 16 and 10y/30y yields rising to 4.70%/5.23%. Breadth was defensive: only 32% of assets positive over 5 sessions while commodities, gold, healthcare and energy led. NVIDIA's Aug 26 report plus the Aug 26 PCE print sit inside the scoring window, so high-beta AI/semi exposure carries two-sided event risk rather than clean edge. Quality-pullback names with strong prior trend (cybersecurity, aerospace/defense, software) show the best combination of prior relative strength and a sharp one-week relative drawdown, making them the most credible short-horizon reversal candidates. | NVIDIA results on Aug 26 could drive a broad tech drawdown that hits cybersecurity, software, and robotics together; Aug 26 PCE and second GDP estimate could push the 10-year above 4.80% and compress high-multiple growth valuations; Reversal thesis may fail if the recent pullback marks the start of a sustained factor rotation out of tech-adjacent leaders; Concentration in correlated technology_and_growth exposures reduces diversification across the three slots; Persian Gulf shipping uncertainty and Brent near $94 could sustain a defensive, energy-led rotation away from selected names |
| xai-grok-4-6 | xai | portfolio | CYBERSECURITY | 3 | 0.56 | SPY finished the week lower with VIX still modest at 16 while 5-session active-return dispersion is 4.38% and only about 32% of assets were positive. High-beta growth names sold off after prior strength, crypto extended a short bounce, and rates drifted higher into a data-heavy week including NVIDIA after the close on Aug 26. | NVIDIA results after the Aug 26 close can extend semiconductor and high-beta tech weakness through the Friday exit.; Rising 10-year yields near 4.70% and hawkish July FOMC minutes can keep duration-sensitive growth from bouncing.; Brent near $94 and Gulf tanker uncertainty can rotate risk into energy rather than the pulled-back tech sleeves.; Aug 26 GDP/PCE and Aug 21 PMIs can reprice the whole equity complex inside the scoring window. |
| xai-grok-4-3 | xai | portfolio | ETHEREUM_ETF | 3 | 0.6 | Equity pullbacks amid rising yields and mixed macro data, with crypto showing volume-driven strength but high reversal risk over one week. | Crypto volatility exceeding one-week horizon; Rising Treasury yields pressuring risk assets; NVIDIA earnings and GDP revisions as near-term catalysts |
| google-gemini-3-1-pro | google | portfolio | SEMICONDUCTORS | 3 | 0.5933 | The market is experiencing a pullback with the S&P 500 down 1.9% for the week, driven by rising yields and uncertainty around inflation and Fed policy. The upcoming NVIDIA earnings report is a major catalyst for the tech sector. | NVIDIA earnings disappoint, leading to a broad sell-off in the technology sector.; Interest rates continue to rise, putting pressure on growth stock valuations. |
| xai-grok-4-5 | xai | portfolio | CYBERSECURITY | 3 | 0.5933 | SPY pulled back ~2% with VIX at 16 amid sticky inflation prints, rising yields near 4.7%, and soft retail/payroll data; quality tech/defense names show sharp relative pullbacks after strong priors while crypto extended hard on volume; NVIDIA print and PCE/GDP revisions dominate the one-week window, favoring selective mean-reversion over broad continuation. | NVIDIA earnings Aug 26 could drive broad tech/semiconductor volatility and spill into robotics/cyber; Sticky inflation and rising 10y yields near 4.7% may pressure duration-sensitive growth equities further; Geopolitical oil/tanker uncertainty and Brent near $94 could sustain risk-off if escalates; PCE/GDP revisions Aug 26 may reprice Fed path after July minutes flagged upside inflation risks |

## Realized Returns

| option_id | label | entry_price | exit_price | return | rank |
| --- | --- | --- | --- | --- | --- |
| SOFTWARE | Software | 103.37000274658203 | 109.5 | 0.059301510017814696 |  |
| CYBERSECURITY | Cybersecurity | 94.8499984741211 | 98.56 | 0.03911440786044018 |  |
| ETHEREUM_ETF | Ethereum ETF | 18.239999771118164 | 18.37 | 0.007127205620237165 |  |
| BITCOIN_ETF | Bitcoin ETF | 43.68000030517578 | 43.9 | 0.005036623014816 |  |
| SP500 | S&P 500 | 765.719970703125 | 769.35 | 0.004740674705848047 |  |
| CASH | Cash / Do Not Invest | 1.0 | 1.0 | 0.0 |  |
| SEMICONDUCTORS | Semiconductors | 560.4199829101562 | 553.11 | -0.013043758490189572 |  |
| AEROSPACE_DEFENSE | Aerospace and Defense | 237.33999633789062 | 232.82 | -0.019044393728968045 |  |
| AUTONOMOUS_ROBOTICS | Autonomous Technology and Robotics | 125.58000183105469 | 122.32 | -0.025959561900950168 |  |

## Official Leaderboard

| model_id | submission_format | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | portfolio | CYBERSECURITY | 3 | 0.5833 | 0.03911440786044018 | 0.028732253138698788 | 0.02399157843285074 |  |  | True | True |
| openai-gpt-5-6-sol | portfolio | CYBERSECURITY | 3 | 0.5833 | 0.03911440786044018 | 0.024814957951359653 | 0.020074283245511606 |  |  | True | True |
| anthropic-claude-opus-5 | portfolio | CYBERSECURITY | 3 | 0.5633 | 0.03911440786044018 | 0.024814957951359653 | 0.020074283245511606 |  |  | True | True |
| xai-grok-4-6 | portfolio | CYBERSECURITY | 3 | 0.56 | 0.03911440786044018 | 0.024814957951359653 | 0.020074283245511606 |  |  | True | True |
| xai-grok-4-3 | portfolio | ETHEREUM_ETF | 3 | 0.6 | 0.007127205620237165 | 0.005679542434023022 | 0.0009388677281749747 |  |  | True | True |
| google-gemini-3-1-pro | portfolio | SEMICONDUCTORS | 3 | 0.5933 | -0.013043758490189572 | 0.0034114091608972996 | -0.0013292655449507473 |  |  | False | True |
| xai-grok-4-5 | portfolio | CYBERSECURITY | 3 | 0.5933 | 0.03911440786044018 | -0.0007633636242698038 | -0.005504038330117851 |  |  | False | False |

## Notes

- This is one standalone round.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Cumulative results are separate.
- Stability results are separate and do not affect this leaderboard.

## Warnings

- Round CB-2026-07-16-1W has no scored official run.
- Round CB-2026-08-23-1W has no scored official run.
- Round CB-2026-08-24-1W has no scored official run.
- Round CB-2026-08-25-1W has no scored official run.
- Round CB-2026-08-26-1W has no scored official run.
- Round CB-2026-08-27-1W has no scored official run.
