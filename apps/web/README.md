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

## Email Collection And Updates

The website includes an email-only subscription system for the `Website Collection`
audience. It uses Cloudflare Pages Functions, D1, Turnstile, and Cloudflare Email
delivery through Resend or Cloudflare Email Service. Subscribers are added
immediately after submitting the website form; no double confirmation is required.

### Cloudflare Setup

Create the D1 database and apply migrations:

```bash
npx wrangler d1 create capitalbench_email
npx wrangler d1 migrations apply capitalbench_email --remote
```

Add the returned database ID to the Pages project as the `EMAIL_DB` D1 binding.
The local `wrangler.toml` shows the expected binding name.

The default sending provider is Resend. Add `capitalbench.org` as a Resend
sending domain, add the Resend DNS records, verify the domain, and use
`updates@capitalbench.org` as the sender unless the product owner chooses a
different address.

Cloudflare Email Sending remains available as a later provider switch. It
requires the domain to exist as a Cloudflare DNS zone in the account used by
Wrangler, and the API token must include Email Sending permissions. If
`wrangler email sending settings capitalbench.org` cannot find the zone, finish
the domain/account setup before trying to use Cloudflare for campaign delivery.
The checked-in Pages config is Resend-first and does not include a Cloudflare
Email binding.

Configure these Cloudflare Pages variables/secrets:

```text
EMAIL_PROVIDER=resend
RESEND_API_KEY=<Resend API key>
RESEND_DAILY_SEND_LIMIT=100
EMAIL_FROM=updates@capitalbench.org
EMAIL_REPLY_TO=<reply inbox>
EMAIL_PUBLIC_BASE_URL=https://www.capitalbench.org
EMAIL_MAILING_ADDRESS=Toronto, Ontario, CA
EMAIL_ADMIN_TOKEN=<long random secret>
UNSUBSCRIBE_TOKEN_SECRET=<long random secret>
PUBLIC_TURNSTILE_SITE_KEY=<Cloudflare Turnstile site key>
TURNSTILE_SECRET_KEY=<Cloudflare Turnstile secret key>
```

Set `EMAIL_PROVIDER=cloudflare` later to send through the Cloudflare `EMAIL`
binding instead. The D1 subscriber list and unsubscribe system do not change.
`RESEND_DAILY_SEND_LIMIT` defaults to `100` so the free Resend daily limit is not
exceeded accidentally; set it higher after upgrading the Resend plan.

The public signup form posts to `/api/subscribe`. The unsubscribe endpoint is
`/unsubscribe?token=...`. Admin campaign sends use `/api/email/send` with
`Authorization: Bearer $EMAIL_ADMIN_TOKEN`. The only active audience group in
this MVP is `website_collection` (`Website Collection`).

### Campaign Operation

Draft a markdown email, then dry-run it:

```bash
npm run email:campaign -- --file campaigns/example/update.md --subject "CapitalBench update" --dry-run
```

Send one test email:

```bash
EMAIL_ADMIN_TOKEN=<token> npm run email:campaign -- \
  --file campaigns/example/update.md \
  --subject "CapitalBench update" \
  --test you@example.com
```

Send to the active `Website Collection` audience:

```bash
EMAIL_ADMIN_TOKEN=<token> npm run email:campaign -- \
  --file campaigns/example/update.md \
  --subject "CapitalBench update" \
  --send --confirm
```

Each campaign email gets a one-click unsubscribe footer and `List-Unsubscribe`
header. The MVP intentionally does not collect names, roles, companies, or other
profile fields.

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
