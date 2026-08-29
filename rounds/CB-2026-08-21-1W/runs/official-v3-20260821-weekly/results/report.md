# CapitalBench Report: CB-2026-08-21-1W / official-v3-20260821-weekly

## Official Public Leaderboard

This is the official CapitalBench score for this run.



## Round Summary

- Run ID: official-v3-20260821-weekly
- Run type: official
- Replicates: 1
- Mock: no
- Title: CapitalBench CB-2026-08-21-1W
- Description: One-week market allocation evaluation round.
- Decision date: 2026-08-21
- Decision deadline: 2026-08-21T13:25:00Z
- Horizon: one week
- Entry date: 2026-08-21
- Exit date: 2026-08-28
- Entry rule: Use the official entry prices supplied in prices/entry_prices.csv.
- Exit rule: Use the official exit prices supplied in prices/exit_prices.csv.
- Options: 70

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

## Portfolio Allocations

| model_id | option_id | allocation_pct | option_return | return_contribution | rationale |
| --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | CYBERSECURITY | 35.0 | 0.03911440786044018 | 0.013690042751154062 | V3 selected model rank 1: overreaction with 60% estimated probability of beating SPY. |
| anthropic-claude-fable-5 | SOFTWARE | 35.0 | 0.059301510017814696 | 0.020755528506235143 | V3 selected model rank 2: overreaction with 58% estimated probability of beating SPY. |
| anthropic-claude-fable-5 | AEROSPACE_DEFENSE | 30.0 | -0.019044393728968045 | -0.005713318118690414 | V3 selected model rank 3: overreaction with 57% estimated probability of beating SPY. |
| anthropic-claude-opus-5 | CYBERSECURITY | 35.0 | 0.03911440786044018 | 0.013690042751154062 | V3 selected model rank 1: overreaction with 58% estimated probability of beating SPY. |
| anthropic-claude-opus-5 | AEROSPACE_DEFENSE | 35.0 | -0.019044393728968045 | -0.006665537805138816 | V3 selected model rank 2: overreaction with 56% estimated probability of beating SPY. |
| anthropic-claude-opus-5 | SOFTWARE | 30.0 | 0.059301510017814696 | 0.017790453005344407 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |
| google-gemini-3-1-pro | SEMICONDUCTORS | 35.0 | -0.013043758490189572 | -0.00456531547156635 | V3 selected model rank 1: overreaction with 65% estimated probability of beating SPY. |
| google-gemini-3-1-pro | CYBERSECURITY | 35.0 | 0.03911440786044018 | 0.013690042751154062 | V3 selected model rank 3: overreaction with 58% estimated probability of beating SPY. |
| google-gemini-3-1-pro | AEROSPACE_DEFENSE | 30.0 | -0.019044393728968045 | -0.005713318118690414 | V3 selected model rank 4: overreaction with 55% estimated probability of beating SPY. |
| openai-gpt-5-6-sol | CYBERSECURITY | 35.0 | 0.03911440786044018 | 0.013690042751154062 | V3 selected model rank 1: overreaction with 60% estimated probability of beating SPY. |
| openai-gpt-5-6-sol | AEROSPACE_DEFENSE | 35.0 | -0.019044393728968045 | -0.006665537805138816 | V3 selected model rank 2: overreaction with 58% estimated probability of beating SPY. |
| openai-gpt-5-6-sol | SOFTWARE | 30.0 | 0.059301510017814696 | 0.017790453005344407 | V3 selected model rank 3: overreaction with 57% estimated probability of beating SPY. |
| xai-grok-4-3 | ETHEREUM_ETF | 35.0 | 0.007127205620237165 | 0.0024945219670830074 | V3 selected model rank 1: overreaction with 62% estimated probability of beating SPY. |
| xai-grok-4-3 | BITCOIN_ETF | 35.0 | 0.005036623014816 | 0.0017628180551855998 | V3 selected model rank 2: overreaction with 58% estimated probability of beating SPY. |
| xai-grok-4-3 | SP500 | 30.0 | 0.004740674705848047 | 0.001422202411754414 | Deterministic SPY fallback for V3 slots without an eligible active candidate. |
| xai-grok-4-5 | CYBERSECURITY | 35.0 | 0.03911440786044018 | 0.013690042751154062 | V3 selected model rank 1: overreaction with 62% estimated probability of beating SPY. |
| xai-grok-4-5 | AEROSPACE_DEFENSE | 35.0 | -0.019044393728968045 | -0.006665537805138816 | V3 selected model rank 2: overreaction with 59% estimated probability of beating SPY. |
| xai-grok-4-5 | AUTONOMOUS_ROBOTICS | 30.0 | -0.025959561900950168 | -0.00778786857028505 | V3 selected model rank 3: overreaction with 57% estimated probability of beating SPY. |
| xai-grok-4-6 | CYBERSECURITY | 35.0 | 0.03911440786044018 | 0.013690042751154062 | V3 selected model rank 1: overreaction with 57% estimated probability of beating SPY. |
| xai-grok-4-6 | AEROSPACE_DEFENSE | 35.0 | -0.019044393728968045 | -0.006665537805138816 | V3 selected model rank 2: overreaction with 56% estimated probability of beating SPY. |
| xai-grok-4-6 | SOFTWARE | 30.0 | 0.059301510017814696 | 0.017790453005344407 | V3 selected model rank 3: overreaction with 55% estimated probability of beating SPY. |

## Leaderboard

Official Public Leaderboard

| model_id | selected_option_id | holding_count | confidence | selected_asset_return | portfolio_return | alpha_vs_sp500 | regret_vs_best_option | rank_among_options | beats_sp500 | beats_cash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| anthropic-claude-fable-5 | CYBERSECURITY | 3 | 0.5833 | 0.03911440786044018 | 0.028732253138698788 | 0.02399157843285074 |  |  | True | True |
| openai-gpt-5-6-sol | CYBERSECURITY | 3 | 0.5833 | 0.03911440786044018 | 0.024814957951359653 | 0.020074283245511606 |  |  | True | True |
| anthropic-claude-opus-5 | CYBERSECURITY | 3 | 0.5633 | 0.03911440786044018 | 0.024814957951359653 | 0.020074283245511606 |  |  | True | True |
| xai-grok-4-6 | CYBERSECURITY | 3 | 0.56 | 0.03911440786044018 | 0.024814957951359653 | 0.020074283245511606 |  |  | True | True |
| xai-grok-4-3 | ETHEREUM_ETF | 3 | 0.6 | 0.007127205620237165 | 0.005679542434023022 | 0.0009388677281749747 |  |  | True | True |
| google-gemini-3-1-pro | SEMICONDUCTORS | 3 | 0.5933 | -0.013043758490189572 | 0.0034114091608972996 | -0.0013292655449507473 |  |  | False | True |
| xai-grok-4-5 | CYBERSECURITY | 3 | 0.5933 | 0.03911440786044018 | -0.0007633636242698038 | -0.005504038330117851 |  |  | False | False |

## Cost-Adjusted Leaderboard

_No cost data available._

## Invalid Submissions

- Invalid raw submissions: 0
- Files: none

## Reproducibility

- hashes.json matches current files: yes

| file | sha256 |
| --- | --- |
| briefing.md | 372f50f24fa959af52ec28cce32c44f66688daa9ba59b9ef2f4c3307d4923470 |
| options.yaml | 1003c5795615371c4808eb307b1057c658972e2e36b5522e72c894bc4ce0c729 |
| prompt.md | c86dfbb217e032991acc64cd3d0bcbb7f26d32639a67b7473af5122ac2230431 |
| manifest.yaml | 1d99f75b9004f6fbd744d208d2a3979953e2e5a69015a4ab4d8ddb0342acd45b |
| submission_schema.json | fb15e640b97fa100237112e5d6bd8548696c72f75ce22b2d3ae2bf212e10166d |
| market_data/universe_decision_context.csv | 6ea62f08417f417a4db8c6aaef03a807ee6e339fa3bd1e6cb8f3ce62b971c16f |
| market_data/universe_decision_context.md | d14678cdff38db03891a4f3e0a145d533a411819995e161f08129f58ec33da6b |
| market_data/universe_decision_context.json | d50c36981ea32264fd6b5c3ee891d67900d04fc928d1c743a2fb097454ab7767 |
| market_data/decision_context_source_history.json | 155bab36d9bfb16a0ce14c713d88d8e081b54e84f67884e5d788ae0f40c158ca |
| market_data/universe_quality_evidence.md | 3a2b082312978342026e55b52b054f52bc34bc0347d9a2e1bcd50b05a9e82bbb |
| market_data/universe_quality_evidence.json | 985bd31ff9c35abbd589365574c740fc4432278722e548e55fab73ec6a9561cc |

## Research Artifacts

- Market fact report: stored in research/market_fact_report.md, audit-only
- Briefing audit report: stored in research/briefing_audit_report.md, audit-only
- Final briefing: stored in research/final_briefing.md and copied to briefing.md, model-facing
- final_briefing.md hash matches briefing.md: yes

| artifact | path | visibility | sha256 | exists |
| --- | --- | --- | --- | --- |
| Market fact report | research/market_fact_report.md | audit-only | b799bad6842f0384d16df626fb10a05cbef220ff299d47a7beb265d3874c8fcc | yes |
| Briefing audit report | research/briefing_audit_report.md | audit-only | 9d295a31b55247f6431c13617f5395df910b100c4fc0a865e22fb6e7990e5c0d | yes |
| Final briefing | research/final_briefing.md | model-facing | 372f50f24fa959af52ec28cce32c44f66688daa9ba59b9ef2f4c3307d4923470 | yes |

## Limitations

- Prices are loaded from local CSV files and are not fetched live.
- Official scoring uses the round's declared submission format.
- Stability analysis, when present, is separate and does not change this leaderboard.
- Portfolio-format rounds score weighted realized returns; single-pick rounds score one selected option.
- Results depend on the round briefing, prompt, options, and local price files supplied by the operator.
