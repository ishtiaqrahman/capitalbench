# Portfolio V3.0 Holdout Comparison

Status: **frozen before model calls**

This is the final low-cost historical decision test for the fixed Portfolio
V3.0 candidate. It uses twelve new calls: four approved models across three
weekly periods. No V1 or V2.2 calls are repeated.

## Question

Does the unchanged V3.0 rule beat both SPY and the exact saved V2.2 portfolios
for the same models and dates strongly enough to replace V2.2?

## Test Sample

The test uses three non-overlapping V2.2 rounds that were not the three exact
V3 development rounds:

| Set | Entry | Exit | Exact control |
| --- | --- | --- | --- |
| V3-H1 | 2026-07-22 | 2026-07-29 | official V2.2 |
| V3-H2 | 2026-07-29 | 2026-08-05 | official V2.2 |
| V3-H3 | 2026-08-05 | 2026-08-12 | official V2.2 |

The models are GPT-5.6 SOL, Gemini 3.1 Pro, Grok 4.3, and Grok 4.5. Each model
gets one single-turn, non-agentic call per period. Tools, browsing, retrieval,
follow-up, and response selection are disabled. Transport retries are zero.

## Frozen V3 Rule

The packet and response schema are unchanged from the V3 development replay.
The final portfolio is built by the already-frozen V3.0 constructor:

1. Preserve the model's candidate rank.
2. Admit only non-SPY candidates labeled `overreaction` with at least a 55%
   model-estimated chance of beating SPY.
3. Fill the 35%, 35%, and 30% slots in rank order.
4. Put every unused slot in SPY.

No result from this holdout may change that rule or its threshold.

## Decision Rule

Accept V3.0 for the next production round only if all checks pass:

- at least 10 of 12 valid exact V3/V2.2 pairs;
- positive mean V3 alpha versus SPY;
- at least 1.00 percentage point mean improvement over paired V2.2;
- at least 8 cells at or above SPY;
- positive mean V3 alpha for at least 3 of 4 models;
- positive mean V3 alpha in at least 2 of 3 periods;
- weakest-period mean V3 alpha no worse than -0.50%; and
- selected top-three capture no worse than V2.2.

If any check fails, reject V3.0. Do not tune it on these periods.

## V1 Comparison Boundary

An exact same-model, same-date V1 comparison is impossible without another
twelve calls: GPT-5.6 SOL and Grok 4.5 were not present through most of the V1
history, and V1 ended before these V2.2 rounds. The report therefore includes
the saved weekly V1 performance of these model IDs as a historical reference,
not as a paired acceptance test. The definitive decision is based on the exact
V3 versus V2.2 pairs and SPY.

## Evidence Limits

These dates are different from the exact V3 development dates, but they are
adjacent one-day-shifted windows and therefore share much of the same market
history. This is stronger than reusing the same three cells and cheaper than a
new paired prospective program, but it is not statistically independent proof
of future alpha. The result is an operational accept/reject decision, not a
claim of proven persistent market outperformance.
