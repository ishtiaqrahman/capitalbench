Exact raw provider response text is preserved locally in this directory for
private operator audit.

The `*.txt` sidecars are intentionally excluded from the public repository.
Available public audit evidence for this run:

- `submissions/raw/*.json` contains the normalized provider submission payloads.
- `submissions/parsed/*.json` contains validated parsed submissions.
- `run_log.jsonl` contains provider/model metadata, usage, validation status,
  the raw response sidecar path, and the SHA256 hash of the exact provider text
  seen at runtime.
