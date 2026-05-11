Exact raw provider response text was not persisted for this run because the run
was created before CapitalBench added `raw_responses/` sidecar preservation.

Available audit evidence for this run:

- `submissions/raw/*.json` contains the normalized provider submission payloads.
- `submissions/parsed/*.json` contains validated parsed submissions.
- `run_log.jsonl` contains provider/model metadata, usage, validation status,
  and the SHA256 hash of the original provider text seen at runtime.

Future runs preserve exact provider text in `raw_responses/<submission>.txt`
and record the sidecar path in `run_log.jsonl`.
