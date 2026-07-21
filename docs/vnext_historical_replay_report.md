# VNext Historical Replay Results

Generated at: `2026-07-21T04:07:25+00:00`

Protocol: `docs/experiments/vnext-historical-replay-2026-07-20.md`

## Bottom Line

No challenger passed the frozen discovery gate. The experiment stopped after discovery, so the historical replay does not support changing the V2.1 input or prompt.

## Discovery

| Treatment | Valid pairs | Winner captures challenger/control | Top-5 alpha improvement | Positive pairs | Gate |
| --- | --- | --- | --- | --- | --- |
| H1 | 4 | 0/0 | 1.62% | 2 | Fail |
| H2 | 4 | 0/0 | 1.00% | 3 | Fail |
| H3 | 4 | 0/0 | -1.12% | 0 | Fail |

## Execution

- Provider calls: 24
- Valid responses: 24
- Input tokens: 389,429
- Output tokens: 21,525
- Reported reasoning tokens: 16,273
- Total provider latency: 458.2 seconds

## Interpretation

This is a retrospective screening test. Dates and setup identifiers were reduced, tools and search were disabled, and packets were frozen before outcomes were loaded. Current models may still possess historical knowledge, so even a passing treatment requires a genuinely prospective live shadow test.

The experiment measures candidate discovery, not final portfolio construction. Top-five returns are equal-weight diagnostics and are not official CapitalBench portfolio results.
