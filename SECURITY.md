# Security Policy

## Secrets

Do not commit API keys, `.env` files, private model configs, provider smoke-test
outputs, or local credentials.

CapitalBench expects real provider keys to come from environment variables:

- `OPENAI_API_KEY`
- `ANTHROPIC_API_KEY`
- `GOOGLE_API_KEY`
- `XAI_API_KEY`
- `TIINGO_API_KEY`

The CLI reports only whether keys are present or missing. It must not print full
key values or write keys to disk.

## Reporting Security Issues

If you find a security issue in CapitalBench, open a private disclosure channel
with the maintainer rather than posting secrets or exploit details publicly.

For now, contact the repository owner through GitHub:

https://github.com/ishtiaqrahman

## Before Publishing A Round

Run a secret scan before committing:

```bash
rg -n "AIza|sk-ant|xai-|sk-proj|OPENAI_API_KEY=|ANTHROPIC_API_KEY=|GOOGLE_API_KEY=|XAI_API_KEY=|TIINGO_API_KEY=" .
```

Review all findings. Placeholder values in `.env.example` are acceptable; real
keys are not.
