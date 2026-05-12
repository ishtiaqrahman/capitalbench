# CapitalBench Web

Astro + React islands site for `www.capitalbench.org`.

## Local Development

```bash
npm install
npm run dev -- --port 4321
```

The site ships with fallback Round 1 data from the repository so it builds
before Supabase is configured. When these variables are present, React islands
hydrate from the public Supabase read model:

```bash
PUBLIC_SUPABASE_URL=https://<project-ref>.supabase.co
PUBLIC_SUPABASE_ANON_KEY=<anon-key>
```

## Cloudflare Pages

Use:

- Build command: `npm run build`
- Build output: `dist`
- Root directory: `apps/web`

Set Cloudflare Pages env vars:

- `PUBLIC_SUPABASE_URL`
- `PUBLIC_SUPABASE_ANON_KEY`

Do not add `SUPABASE_SERVICE_ROLE_KEY` to Cloudflare Pages.

The `_redirects` file redirects `capitalbench.org` traffic to
`www.capitalbench.org` when both hostnames are routed to Pages.

Production deploys are also supported through GitHub Actions. The
`Deploy Web` workflow builds `apps/web`, runs SEO validation, and deploys the
`dist` directory to the existing `capitalbench-web` Pages project when these
repository secrets are configured:

- `CLOUDFLARE_ACCOUNT_ID`
- `CLOUDFLARE_API_TOKEN`
- `PUBLIC_SUPABASE_URL`
- `PUBLIC_SUPABASE_ANON_KEY`

The token should be scoped to Cloudflare Pages edit access for the CapitalBench
account. The workflow skips deployment cleanly if the Cloudflare deployment
secrets are absent.

The `Site Health` workflow checks the canonical hostname, robots file, sitemap,
and apex redirect every 30 minutes.

## SEO Validation

Run the production build and static SEO checks before deploying:

```bash
npm run build
npm run seo:check
```

The SEO check validates titles, descriptions, canonical URLs, robots meta,
Open Graph/Twitter image metadata, JSON-LD presence, one `h1` per page, and
sitemap coverage for indexable pages.

After production deploy:

- Submit `https://www.capitalbench.org/sitemap.xml` in Google Search Console.
- Inspect `/`, `/methodology/`, `/leaderboards/latest/`, `/rounds/`, and the
  latest round detail URL with URL Inspection.
- Test structured data with Google's Rich Results Test.
- Run PageSpeed Insights against production URLs, not the Astro dev server.
- Confirm `SUPABASE_SERVICE_ROLE_KEY` is absent from built assets and Pages env.
