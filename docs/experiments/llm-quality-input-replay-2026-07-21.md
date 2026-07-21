# LLM Quality-Input Replay

## Research Question

Can all four research LLMs make better one-week selections when they receive a
compact, complete option-level representation of the price pattern that
survived the frozen historical feature screen?

This experiment changes the information and instructions inside the LLM call.
It does not blend, rerank, or alter portfolios after the response.

## Models And Periods

The frozen roster is Gemini 3.5 Flash, Grok 4.3, Grok 4.5, and GPT-5.6 SOL.
The periods are V1 through V3 from the existing event-ranking replay. Exact
saved H4 balanced-search responses are the paired controls. At most 24 new
treatment calls are allowed. Two exact Gemini H4 repairs are also frozen for
controls that previously failed with HTTP 503, making the total provider-call
ceiling 26. The repairs do not change H4 instructions or the treatment gate.

## Outcome-Free Evidence Table

For every active option, the treatment packet adds only entry-date percentile
ranks for:

- prior active return versus SPY;
- reverse recent active return, so a larger value means a deeper recent
  relative pullback;
- lower volatility;
- shallower drawdown;
- and their frozen 45/30/15/10 composite.

The table is complete and sorted by frozen option order. It contains no future
return, winner label, realized rank, recommendation, or outcome-derived text.
The evidence score was discovered retrospectively, so this remains adaptive
historical development work.

## Treatments

**Q1, information only:** Preserve the H4 balanced-search task and response
contract. Add the evidence table with a neutral description. The model remains
free to ignore it.

**Q2, information plus explicit use:** Add the same table and require the model
to compare its lane representatives with the highest-evidence options. At
least three quality top-ten options must appear in the model's ten-name
shortlist and at least two in its final five. The model still forecasts SPY and
each finalist, may reject any particular option, and makes the final ranking.

Both treatments remain single-turn, non-agentic, with tools, search, browsing,
and remembered outcomes prohibited.

## Frozen Gate

Each treatment is judged separately against H4. It must have at least ten
valid paired cells, improve mean equal-weight top-five return by 0.75 points,
produce positive mean alpha versus SPY, improve at least eight paired cells,
improve all four model families on average, improve at least two of three
periods, avoid worsening shortlist regret, and avoid worsening the worst
period's mean alpha.

Failure stops the branch. Passing historical results authorize only a
prospective private LLM shadow using all four models. They do not alter
Portfolio V2.0 or official scores.
