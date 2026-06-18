# CapitalBench Input-Side Improvement Hypotheses

Read-only audit summary. No files were changed during the audit.

## Main Finding

There are input-side changes worth testing, but none can guarantee better realized returns. The current setup is fair and auditable, but it likely nudges models toward salient narrative/momentum bets and away from a disciplined "can I really beat SPY?" hurdle.

The current prompt assembly is:

- `src/capitalbench/prompting.py`: `prompt.md` + round metadata + `briefing.md` + full-universe trailing returns + verbose option list.

The latest prompts are clear on horizon/scoring, but the model-facing briefing is intentionally neutral and prohibits interpretation/recommendation language. That keeps the benchmark clean, but it also leaves models to invent their own portfolio process.

## Evidence From Results

Resolved weekly rounds are the weak spot:

- Weekly resolved sample: 9 rounds, 43 model rows.
- Average weekly alpha vs SPY: about `-1.31%`.
- Hit rate vs SPY: about `37%`.
- Monthly has only one resolved round so far, and that one was positive: about `+2.42%` alpha.

Behavior pattern:

- May 24-28: trailing momentum worked; models crowded into semis/tech/Taiwan/Korea and beat SPY.
- May 29-June 8: trailing momentum flipped strongly negative; models kept chasing recent leaders, then rotated defensive too late, and mostly missed SPY or the oracle winners.
- June 16/17 current live portfolios are again highly crowded into `SEMICONDUCTORS`, `SOUTH_KOREA`, `MOMENTUM`, `TAIWAN`, and `AEROSPACE_DEFENSE`.

The trailing return table is useful, but in the resolved sample its predictive correlation flips regime:

- Late May: 7d/30d trailing returns correlated positively with next-week returns.
- May 29-June 8: those same signals were negative, roughly `-0.36` to `-0.55` for 7d in several rounds.

## Highest-Value Hypotheses

1. Add a stronger SPY hurdle.

   Models almost never allocate to `SP500`, even when SPY would have beaten them. The prompt should explicitly say: if active edge is weak, allocate partially or fully to `SP500`; do not force active bets just because this is a contest. This should reduce negative alpha, though it may reduce upside.

2. Split weekly and monthly briefings.

   Right now the same briefing includes both weekly and monthly dates/events. For the weekly run, remove or clearly mark after-exit events as outside the scoring window. For monthly, include only the monthly-relevant calendar. This should reduce horizon confusion and make the two runs less copy/paste similar.

3. Add benchmark-relative mechanical data.

   Keep it neutral, but add columns like excess return vs SPY, beta/volatility, drawdown from recent high, 1d return, 7d return, 30d return, and maybe 20/50/200-day distance. The current raw trailing-return table encourages "big number = good"; benchmark-relative/risk context would support better alpha reasoning.

4. Add market surprise/pricing context.

   The briefing has raw macro values, but little about consensus, surprise, or market-implied pricing. Models need to know what is already priced. Useful neutral fields: actual vs consensus, yield changes after the release, Fed funds futures/implied cuts, sector reaction after the event.

5. Add a private decision-process instruction.

   Example conceptually: before final JSON, internally compare continuation, mean-reversion, risk-off, and benchmark-only cases; choose active exposure only where expected alpha clears the SPY hurdle. Do not output that reasoning. This keeps JSON clean but may reduce shallow momentum chasing.

6. Increase reasoning effort where supported.

   Configs are currently `temperature: 0` and mostly `reasoning_effort: low` or null. That helps reproducibility, but it may encourage deterministic crowding. Testing medium/high reasoning for official runs could improve scenario evaluation without changing the public information set.

7. Compact the option list.

   The option section is about 900 lines. A compact table with ID, ticker, group, risk bucket, and exposure may be easier for models than repeated verbose blocks. Less low-signal context may improve attention to the actual decision data.

## First Test Recommendation

Test SPY hurdle language + horizon-specific briefing + benchmark-relative mechanical table first. That targets the observed failure mode without turning the benchmark into operator-provided recommendations.
