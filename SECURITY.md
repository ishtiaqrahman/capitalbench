# Security Policy

## Secrets

Do not commit API keys, `.env` files, private model configs, provider smoke-test
outputs, raw provider responses, local credentials, generated screenshots,
Lighthouse output, Supabase project refs, or deployment hooks.

CapitalBench expects real provider keys to come from environment variables:

- `OPENAI_API_KEY`
- `ANTHROPIC_API_KEY`
- `GOOGLE_API_KEY`
- `XAI_API_KEY`
- `TIINGO_API_KEY`
- `SUPABASE_SERVICE_ROLE_KEY`
- `PUBLIC_SUPABASE_ANON_KEY`
- `CLOUDFLARE_PAGES_DEPLOY_HOOK`
- `GITHUB_TOKEN`

The CLI reports only whether keys are present or missing. It must not print full
key values or write keys to disk.

The frontend may use hosted `PUBLIC_SUPABASE_URL` and
`PUBLIC_SUPABASE_ANON_KEY` values, but production values should still live in
Cloudflare Pages environment variables rather than committed files.

## Reporting Security Issues

If you find a security issue in CapitalBench, open a private disclosure channel
with the maintainer rather than posting secrets or exploit details publicly.

For now, contact the repository owner through GitHub:

https://github.com/ishtiaqrahman

## Before Publishing A Round

Run the public repository audit before committing or publishing:

```bash
python scripts/public_repo_audit.py
```

The audit checks tracked and unignored files for likely secrets, operational
Supabase identifiers, generated local output, provider smoke-test output, and
raw provider response files. Placeholder values in `.env.example` are
acceptable; real keys are not.
