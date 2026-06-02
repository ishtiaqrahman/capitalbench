# CapitalBench Operations Runbook

This runbook covers the production path after a manually executed provider run.
It intentionally excludes provider keys, Supabase service keys, Cloudflare API
tokens, and raw provider responses.

## Production Systems

- Public site: `https://www.capitalbench.org/`
- GitHub repo: `ishtiaqrahman/capitalbench`
- Cloudflare Pages project: `capitalbench-web`
- Supabase project: dedicated CapitalBench production project
- Scheduled resolver: GitHub Actions workflow `CapitalBench Resolver`
- Scheduled interim refresh: GitHub Actions workflow `Interim Performance Refresh`
- Production health check: GitHub Actions workflow `Site Health`

## New Round Checklist

1. Create and freeze the round inputs.

   ```bash
   capitalbench init-round ...
   capitalbench import-research --round rounds/<round_id> ...
   capitalbench fetch-universe-performance --round rounds/<round_id> ...
   capitalbench hash-round --round rounds/<round_id>
   ```

2. Run provider calls manually.

   ```bash
   capitalbench run-round \
     --round rounds/<round_id> \
     --run-id official-<yyyymmdd> \
     --run-type official \
     --allow-real-api-calls
   ```

3. Validate the run.

   ```bash
   capitalbench validate-submissions \
     --round rounds/<round_id> \
     --run-id official-<yyyymmdd>

   capitalbench list-runs --round rounds/<round_id>
   ```

4. Accept only one official valid run.

   ```bash
   capitalbench accept-run \
     --round rounds/<round_id> \
     --run-id official-<yyyymmdd>
   ```

   Acceptance must pass the gate: official run type, not mock, official-score
   eligible, zero invalid submissions, valid submission count matching enabled
   model count, matching round hashes, and required round files present.

5. Confirm the automation job exists.

   ```bash
   capitalbench automation-status --rounds-dir rounds
   ```

6. Commit and push accepted round metadata if the acceptance command changed
   tracked files.

   ```bash
   python scripts/public_repo_audit.py
   git status --short
   git add rounds/<round_id>
   git commit -m "Accept <round_id> official run"
   git push
   ```

## Resolution Path

The scheduled GitHub resolver runs every 30 minutes. When a job is due, it:

1. Claims the due automation job.
2. Fetches exit prices.
3. Scores the accepted official run.
4. Publishes the round report.
5. Updates latest and cumulative leaderboards.
6. Syncs public rows to Supabase.
7. Commits generated artifacts.
8. Builds and deploys `apps/web` to Cloudflare Pages.

Check status:

```bash
gh run list --repo ishtiaqrahman/capitalbench --workflow "CapitalBench Resolver" --limit 5
gh run view <run_id> --repo ishtiaqrahman/capitalbench --log
```

## Interim Monthly Charts

The scheduled interim refresh runs after U.S. market close on market weekdays.
It fetches or reuses one full-universe daily price snapshot, updates every
active monthly round whose timeline includes that close date, syncs public rows
to Supabase when credentials are configured, commits changed artifacts, and
deploys the website only when generated files changed.

Manual reuse-only refresh:

```bash
capitalbench update-interim-performance \
  --rounds-dir rounds \
  --snapshot-date YYYY-MM-DD \
  --track monthly \
  --skip-fetch
```

Manual fetch-and-refresh:

```bash
capitalbench update-interim-performance \
  --rounds-dir rounds \
  --snapshot-date YYYY-MM-DD \
  --track monthly
```

The command reuses full-universe `entry_prices.csv` and `exit_prices.csv`
packages from other rounds as eligible snapshots. That keeps free-tier Tiingo
usage low: one new daily full-universe pull can update all active monthly
charts.

## Manual Recovery

Retry a local job:

```bash
capitalbench automation-retry --round rounds/<round_id>
```

Resolve one accepted round immediately:

```bash
capitalbench automation-resolve \
  --rounds-dir rounds \
  --round-id <round_id> \
  --run-id <run_id>
```

Cancel a local job only when replacing it with a corrected acceptance:

```bash
capitalbench automation-cancel --round rounds/<round_id>
```

## Website Deployment

Normal production deployment is automatic on pushes to `main` that touch
`apps/web/**` or the web deploy workflow. Manual deployment:

```bash
gh workflow run deploy-web.yml --repo ishtiaqrahman/capitalbench
gh run list --repo ishtiaqrahman/capitalbench --workflow "Deploy Web" --limit 5
```

Required GitHub secrets:

- `CLOUDFLARE_ACCOUNT_ID`
- `CLOUDFLARE_API_TOKEN`
- `PUBLIC_SUPABASE_URL`
- `PUBLIC_SUPABASE_ANON_KEY`
- `SUPABASE_URL`
- `SUPABASE_SERVICE_ROLE_KEY`
- `TIINGO_API_KEY`

Never commit these values.

## Health Checks

The `Site Health` workflow checks the canonical hostname, apex redirect,
`robots.txt`, and `sitemap.xml` every 30 minutes.

Manual check:

```bash
gh workflow run site-health.yml --repo ishtiaqrahman/capitalbench
curl -I https://www.capitalbench.org/
curl -I https://capitalbench.org/
```

Expected:

- `https://www.capitalbench.org/` returns `200`
- `https://capitalbench.org/` returns `301` to `https://www.capitalbench.org/`

## Search Console

After launch, add `https://www.capitalbench.org/` in Google Search Console and
submit:

```text
https://www.capitalbench.org/sitemap.xml
```

## Token Rotation

If a Cloudflare token is exposed or suspected exposed:

1. Create a replacement token in Cloudflare with account-level Cloudflare Pages
   edit access for the CapitalBench account.
2. Replace the GitHub secret.

   ```bash
   gh secret set CLOUDFLARE_API_TOKEN --repo ishtiaqrahman/capitalbench
   ```

3. Revoke the old token in Cloudflare.
4. Run `Deploy Web` manually and verify production.
