# Fairness Notes

CapitalBench is only useful if every model faces the same information and the
same rules.

Use these rules for a fair round:

- Freeze `manifest.yaml`, `briefing.md`, `options.yaml`, `prompt.md`, and any `market_data/` prompt artifact before collecting submissions.
- Publish `hashes.json` so readers can verify the round inputs did not change.
- Give every model the same prompt and option list.
- Do not add information to one model's prompt that is not available to the others.
- Allow internal learned knowledge and general market priors equally for all models.
- Forbid browsing, tool calls, live market data retrieval, and intentional use of post-cutoff facts, prices, news, or events.
- Keep `briefing.md` factual. Do not include interpretation, scenario analysis, "why it matters" commentary, affected-market mapping, recommendations, or rankings.
- If full-universe trailing returns are included, generate them mechanically for every option and sort by option order rather than performance.
- Do not revise a completed round's option universe after seeing model choices just to create more varied picks.
- Collect submissions before the decision deadline.
- Preserve invalid raw submissions instead of deleting them.
- Use provider-native deterministic settings: temperature `0` where supported, tools/search disabled in API payloads, and the lowest provider-supported reasoning or thinking setting that still produces valid structured output.
- Record token usage, including reasoning or thinking tokens when exposed, but do not treat hidden reasoning counts as directly comparable across providers.
- Use the same local entry and exit price source for every option.
- State the entry and exit rules in `manifest.yaml`.
- Identify exactly one official one-shot run for public reporting.
- Mark incomplete or invalid official attempts as not official-score eligible.
- Retry official model calls only for infrastructure or format failures such as malformed JSON, truncation, provider transport failure, or schema output failure.
- Do not retry because of the selected asset, confidence value, or rationale quality.
- Keep multi-run stability analysis separate from the official leaderboard.
- Do not average or weight official and stability results into one headline score.
- For cumulative reporting, include only resolved rounds with scored outputs.
- If a round has multiple official-score-eligible runs, use an explicit cumulative selection file.
- Add newly released models only to future rounds.
- Do not backfill new models into old official rounds.
- Label any manual old-round run as retrospective and exclude it from public official and cumulative leaderboards.

For official scoring, each model gets one attempt and one schema-valid decision
under the round's declared submission format. For stability analysis, each
model can be called multiple times with the same prompt, briefing, and option
list. Stability reports consistency and repeated return statistics, but it is
not the official benchmark score.

If submissions are entered manually, the operator should record the model id,
provider, mode, run type, replicate index, confidence, rationale summary, key
risks, token usage if available, and cost if available.

CapitalBench does not prove that a model is good at investing. It measures a
narrow task under a specific prompt, option set, and time window.

Cumulative leaderboards reduce single-round noise but do not remove it. The
cumulative official leaderboard averages one-shot alpha across rounds. The
cumulative stability leaderboard averages repeated-run alpha and consistency
across rounds. They remain separate.

New models can have fewer resolved rounds than older models. This is expected
and should be shown transparently with the `resolved_rounds` count. A new model
should not be penalized for rounds it could not enter, and it should not be
credited by rerunning old rounds after outcomes are knowable.
