export type ChangelogCategory =
  | "Benchmark"
  | "Data"
  | "Methodology"
  | "Operations"
  | "Research"
  | "Security";

export type ChangelogStatus = "published" | "updated" | "deprecated";

export interface ChangelogLink {
  label: string;
  href: string;
}

export interface ChangelogEntry {
  id: string;
  date: string;
  title: string;
  category: ChangelogCategory;
  status: ChangelogStatus;
  summary: string;
  details: string[];
  links?: ChangelogLink[];
}

export const changelogEntries: ChangelogEntry[] = [
  {
    id: "2026-06-09-claude-fable-5-added",
    date: "2026-06-09",
    title: "Claude Fable 5 joins CapitalBench",
    category: "Benchmark",
    status: "published",
    summary:
      "Claude Fable 5 entered its first official weekly and monthly CapitalBench tests in the June 9, 2026 cohort.",
    details: [
      "The model is configured as anthropic-claude-fable-5 using the Anthropic API model ID claude-fable-5.",
      "Adaptive-thinking effort is pinned to low, Anthropic's lowest supported setting for Claude Fable 5.",
      "Both official June 9 runs produced valid submissions with the same frozen briefing, Universe v2.1 options, and June 9 adjusted-close entry snapshot used by the other five models.",
      "Older tests are not backfilled, so Fable's scorecards will show a shorter history until these rounds resolve."
    ],
    links: [
      { label: "Claude Fable 5", href: "/models/anthropic-claude-fable-5" },
      { label: "Rounds", href: "/rounds" },
      { label: "AI Risk Appetite", href: "/risk-appetite" }
    ]
  },
  {
    id: "2026-06-09-oracle-relative-capitalbench-score",
    date: "2026-06-09",
    title: "CapitalBench Score aligned directly with the oracle",
    category: "Methodology",
    status: "updated",
    summary:
      "CapitalBench Score now compares model return directly with the hindsight maximum, including the magnitude of losses.",
    details: [
      "A model that matches the best asset scores 100, no net return scores 0, and negative values represent losses relative to the oracle.",
      "Full-history scores divide summed model returns by summed oracle returns, so a small loss ranks above a large loss.",
      "Oracle-return weighting prevents a low-opportunity test with a small denominator from dominating the full history.",
      "Tests are not compounded because overlapping rounds are separate benchmark experiments rather than one sequential portfolio."
    ],
    links: [
      { label: "Scoring", href: "/scoring#capitalbench-score" },
      { label: "Overall weekly", href: "/leaderboards/cumulative-weekly" },
      { label: "API docs", href: "/api" }
    ]
  },
  {
    id: "2026-06-07-model-risk-pulse",
    date: "2026-06-07",
    title: "Live and historical AI Risk Appetite published",
    category: "Methodology",
    status: "published",
    summary:
      "CapitalBench now publishes current and historical allocation-based risk signals from weekly and monthly model portfolios.",
    details: [
      "Weekly tactical and monthly strategic readings are calculated separately and then equal-weighted into a 0-100 combined pulse.",
      "The landing page shows the current pulse, model agreement, allocation drivers, regime mix, and the risk level of all unresolved portfolios.",
      "A dedicated methodology page adds historical views for the decision pulse, model agreement, regime mix, and risk level of the live portfolio book.",
      "The methodology page publishes the formula and the complete versioned asset-risk table.",
      "The existing historical model risk profiles retain their 1-5 display and now use the same shared asset definitions as the live signal."
    ],
    links: [
      { label: "AI Risk Appetite", href: "/risk-appetite" },
      { label: "Homepage", href: "/" },
      { label: "API docs", href: "/api" }
    ]
  },
  {
    id: "2026-06-06-weekly-interim-refresh-fix",
    date: "2026-06-06",
    title: "Weekly interim price refresh corrected",
    category: "Operations",
    status: "updated",
    summary:
      "The scheduled interim-performance job now refreshes both weekly and monthly open tests from each eligible daily close.",
    details: [
      "The production workflow now invokes update-interim-performance with the all-track setting instead of limiting scheduled updates to monthly tests.",
      "Weekly live-return rows and the homepage priced-test count will update automatically after an eligible post-entry close is fetched and deployed.",
      "A regression test now verifies that the checked-in production workflow continues to refresh all tracks."
    ],
    links: [
      { label: "Homepage", href: "/" },
      { label: "Rounds", href: "/rounds" },
      { label: "Models", href: "/models" }
    ]
  },
  {
    id: "2026-06-05-adjusted-close-price-refresh",
    date: "2026-06-05",
    title: "Final scoring prices now refresh both adjusted-close endpoints",
    category: "Data",
    status: "updated",
    summary:
      "Resolved weekly scoring files were refreshed onto one adjusted-close basis, and future automated resolution now fetches both start and end prices before final scoring.",
    details: [
      "Final automated resolution now refreshes both entry and exit adjusted closes together after the scoring window closes, avoiding stale entry snapshots when ETF adjusted histories update for distributions.",
      "The three resolved weekly rounds were regenerated from same-source adjusted-close price files; Gemini's latest weekly CapitalBench Score remains 85.1, while OpenAI's latest weekly score moved from 53.6 to 53.5 after the price-basis correction.",
      "The external price audit now verifies all resolved weekly rounds against adjusted-close data, including local model returns, maximum possible returns, and CapitalBench Scores."
    ],
    links: [
      { label: "Scoring", href: "/scoring" },
      { label: "Methodology", href: "/methodology" },
      { label: "Latest weekly", href: "/leaderboards/latest-weekly" }
    ]
  },
  {
    id: "2026-06-05-selected-asset-return-correction",
    date: "2026-06-05",
    title: "Selected-asset return field corrected for portfolio tests",
    category: "Data",
    status: "updated",
    summary:
      "Portfolio-format weekly result files now separate the primary selected asset's return from the weighted portfolio return.",
    details: [
      "The affected CapitalBench scores, portfolio returns, S&P 500 comparisons, alpha values, regret values, and rankings did not change.",
      "The selected_asset_return field now reports the realized return of selected_option_id, while portfolio_return reports the allocation-weighted portfolio result.",
      "A raw CSV score audit command now recomputes every resolved score from leaderboard, return, and allocation files and rejects this field mixup."
    ],
    links: [
      { label: "Latest weekly", href: "/leaderboards/latest-weekly" },
      { label: "Scoring", href: "/scoring" },
      { label: "Rounds", href: "/rounds" }
    ]
  },
  {
    id: "2026-06-05-latest-result-selection-audit",
    date: "2026-06-05",
    title: "Latest-result selection hardened",
    category: "Data",
    status: "updated",
    summary:
      "CapitalBench now uses the scoring-window end date as the first rule for choosing the latest resolved test across local reports, synced tables, and public pages.",
    details: [
      "Latest leaderboard publishing and Supabase sync now share the same exit-date-first ordering used by the website and Data API.",
      "Regression tests cover overlapping rounds where a later decision date and a later scoring end date point to different tests.",
      "This prevents hydrated latest-result tables from drifting away from the static latest-result page when schedules overlap."
    ],
    links: [
      { label: "Latest weekly", href: "/leaderboards/latest-weekly" },
      { label: "Latest monthly", href: "/leaderboards/latest-monthly" },
      { label: "API docs", href: "/api" }
    ]
  },
  {
    id: "2026-06-05-public-data-contract-audit",
    date: "2026-06-05",
    title: "Public data contract validation expanded",
    category: "Data",
    status: "published",
    summary:
      "CapitalBench expanded automated checks for displayed benchmark data, documentation examples, sitemap metadata, and API contract behavior.",
    details: [
      "Rendered-page validation now checks homepage, leaderboards, round pages, model pages, universe data, methodology/scoring claims, and API documentation examples against generated source data.",
      "The OpenAPI spec now lists only the working production API host and documents only implemented parameters for leaderboard and positioning-change endpoints.",
      "The Data API now rejects mixed weekly/monthly leaderboard requests and unknown model or asset identifiers instead of returning misleading empty success responses.",
      "The website build and API tests now verify that documented API endpoints are actually served by the runtime handler with current model, asset, and round IDs."
    ],
    links: [
      { label: "API docs", href: "/api" },
      { label: "OpenAPI spec", href: "/api/openapi.json" },
      { label: "Scoring", href: "/scoring" }
    ]
  },
  {
    id: "2026-06-04-all-resolved-scorecards",
    date: "2026-06-04",
    title: "Overall scorecards now combine all resolved tests",
    category: "Methodology",
    status: "updated",
    summary:
      "Headline weekly and monthly scorecards combine every resolved test in each track.",
    details: [
      "CapitalBench Score leaderboards now use all resolved weekly or monthly tests instead of only the latest model cohort.",
      "Models added later are shown with fewer included tests and marked short history until they have the full resolved sample.",
      "The Data API cumulative leaderboard now includes resolved-round metadata, included-test counts, and rank-eligibility fields for downstream audits.",
      "The website build now validates that generated public result rows have matching canonical leaderboard and return files."
    ],
    links: [
      { label: "Scoring", href: "/scoring" },
      { label: "Overall weekly", href: "/leaderboards/cumulative-weekly" },
      { label: "API docs", href: "/api" }
    ]
  },
  {
    id: "2026-06-04-live-mark-to-market",
    date: "2026-06-04",
    title: "Live mark-to-market added for open tests",
    category: "Data",
    status: "published",
    summary:
      "Open weekly and monthly tests can now show interim portfolio returns from the latest available close while remaining separate from official final scores.",
    details: [
      "The homepage now includes a Live Portfolio Returns chart for open tests, with filters for all live, weekly, and monthly tracks.",
      "Model pages now show each model's current live return before final scoring, using only unresolved rounds and excluding completed results.",
      "The Data API exposes GET /v1/live/performance, GET /v1/rounds/{round_id}/live-performance, and GET /v1/models/{model_id}/live-performance for interim mark-to-market data.",
      "The scheduled interim refresh now updates all active tracks instead of only active monthly tests."
    ],
    links: [
      { label: "Homepage", href: "/" },
      { label: "API docs", href: "/api" },
      { label: "Models", href: "/models" }
    ]
  },
  {
    id: "2026-06-03-capitalbench-score-max-possible",
    date: "2026-06-03",
    title: "CapitalBench Score documented as the primary benchmark score",
    category: "Methodology",
    status: "published",
    summary:
      "Overall weekly and monthly results now explain CapitalBench Score as the primary benchmark score against the maximum possible return in each completed window.",
    details: [
      "Scoring documentation now separates raw portfolio return, S&P 500 return, Portfolio Minus S&P 500, regret, and CapitalBench Score.",
      "Overall weekly and monthly pages now lead with the CapitalBench Score chart, with average portfolio return and S&P 500 return kept as supporting context.",
      "The Data API read model and OpenAPI schema include max_possible_return_pct and capitalbench_score for resolved result rows and cumulative leaderboards."
    ],
    links: [
      { label: "Scoring", href: "/scoring" },
      { label: "Overall weekly", href: "/leaderboards/cumulative-weekly" },
      { label: "API docs", href: "/api" }
    ]
  },
  {
    id: "2026-06-02-interim-performance-automation",
    date: "2026-06-02",
    title: "Monthly interim performance refresh automated",
    category: "Operations",
    status: "published",
    summary:
      "Active monthly round charts now refresh from reusable daily full-universe price snapshots instead of manual per-round updates.",
    details: [
      "A new update-interim-performance command creates or reuses one daily price snapshot and applies it to every active monthly round whose timeline includes that close date.",
      "The scheduled GitHub Actions refresh runs after U.S. market close, commits changed interim artifacts, and deploys the website only when refreshed data changes.",
      "The website deploy workflow now watches universe configs, round artifacts, latest snapshots, and cumulative data so data-only updates can publish without an app-code edit.",
      "Existing full-universe entry and exit price packages can also serve as reusable snapshots, reducing Tiingo calls while keeping each round's frozen entry prices unchanged.",
      "Per-round Supabase sync failures are reported as warnings so one stale or mismatched round does not block other active monthly charts from updating."
    ],
    links: [
      { label: "Rounds", href: "/rounds" },
      { label: "Methodology", href: "/methodology" },
      { label: "Scoring", href: "/scoring" }
    ]
  },
  {
    id: "2026-06-02-run-concentration-analytics",
    date: "2026-06-02",
    title: "Run concentration analytics added",
    category: "Data",
    status: "published",
    summary:
      "CapitalBench now reports how concentrated each round is across the model portfolios submitted for that round.",
    details: [
      "Round pages and the latest scored-test view now show run-level consensus allocation, including the largest shared asset, top-three asset share, and effective asset count.",
      "Completed rounds remain available for concentration review, while active exposure still excludes completed rounds from live positioning.",
      "The Data API now exposes GET /v1/rounds/{round_id}/concentration for round-level concentration summaries, asset weights, category mix, and model-level holders."
    ],
    links: [
      { label: "API docs", href: "/api" },
      { label: "Rounds", href: "/rounds" },
      { label: "Latest results", href: "/leaderboards/latest" }
    ]
  },
  {
    id: "2026-06-01-data-api-v1",
    date: "2026-06-01",
    title: "CapitalBench Data API v1 added",
    category: "Data",
    status: "published",
    summary:
      "CapitalBench now has a protected read-only API for published model portfolios, active positioning, cumulative allocation behavior, results, assets, and proof metadata.",
    details: [
      "The web build now generates a static API read model from the same public round files used by the website, so API data refreshes when round artifacts are deployed.",
      "Versioned v1 endpoints expose active and cumulative positioning, model holdings, asset holders, rounds, portfolios, latest and cumulative leaderboards, current universe data, and model style metrics.",
      "API requests require bearer keys backed by Cloudflare D1, with per-minute and daily fixed-window rate limits.",
      "A local API-key CLI can generate one-time keys and insert them into the production D1 database when Cloudflare credentials are available."
    ],
    links: [
      { label: "API docs", href: "/api" },
      { label: "OpenAPI spec", href: "/api/openapi.json" },
      { label: "Rounds", href: "/rounds" }
    ]
  },
  {
    id: "2026-05-29-universe-v2-1-expanded",
    date: "2026-05-29",
    title: "Future rounds move to Universe v2.1",
    category: "Methodology",
    status: "published",
    summary:
      "CapitalBench Universe v2.1 adds five future-round ETF options to broaden the choice set while leaving completed rounds frozen.",
    details: [
      "The new future-round options are Broad AI Technology (AIQ), Autonomous Technology and Robotics (ARKQ), Cybersecurity (CIBR), Solar Energy (TAN), and Metals and Mining (XME).",
      "Universe v2.1 keeps all 65 v2.0 options unchanged and adds the new ETFs as neutral exposure options, not as recommendations or performance-ranked choices.",
      "New rounds initialized with capitalbench init-round now default to configs/universes/capitalbench_universe_v2_1.yaml and record universe_version: v2.1 unless an older or custom universe is explicitly passed.",
      "Existing v1.5 and v2.0 round directories, manifests, option files, hashes, and public results remain unchanged."
    ],
    links: [
      { label: "Asset list", href: "/universe" },
      { label: "Methodology", href: "/methodology" },
      { label: "Rounds", href: "/rounds" }
    ]
  },
  {
    id: "2026-05-28-claude-opus-4-8-added",
    date: "2026-05-28",
    title: "Claude Opus 4.8 joins future CapitalBench tests",
    category: "Benchmark",
    status: "published",
    summary:
      "Claude Opus 4.8 was added as a regular participant starting with the May 28, 2026 weekly and monthly tests.",
    details: [
      "The model is configured as anthropic-claude-opus-4-8 using the Anthropic API model ID claude-opus-4-8.",
      "Eligibility begins with the May 28, 2026 weekly and monthly rounds, so older completed tests are not backfilled.",
      "Anthropic effort is explicitly pinned to low, the lowest documented effort level, and no thinking field is sent for Claude Opus models."
    ],
    links: [
      { label: "Latest weekly", href: "/leaderboards/latest-weekly" },
      { label: "Latest monthly", href: "/leaderboards/latest-monthly" }
    ]
  },
  {
    id: "2026-05-24-weekly-track-separated",
    date: "2026-05-24",
    title: "Weekly benchmark track added separately from monthly rounds",
    category: "Benchmark",
    status: "published",
    summary:
      "CapitalBench now supports one-week rounds as a separate track with separate website lanes and leaderboard slots.",
    details: [
      "The first weekly packet, CB-2026-05-24-1W, uses its own manifest, prompt, model input, hashes, run folder, entry prices, and resolution job while reusing May 24 source research only as input material.",
      "Latest and cumulative public read models now use separate weekly and monthly slots so one-week and one-month scores cannot overwrite or mix with each other.",
      "The homepage, leaderboard hub, round index, and round pages now label weekly and monthly tracks separately.",
      "The landing page now presents weekly and monthly as equal track lanes with separate status cards, allocation previews, leaderboard links, timelines, and audit packet links.",
      "Weekly prompts now make the close-to-close timeline explicit, including the May 22 entry close, Memorial Day market holiday, Tuesday-to-Friday regular-session window, and May 29 exit close.",
      "Default monthly prompt generation and generated model-input metadata now reinforce close-to-close scoring and timeline-focused reasoning without using negative one-month wording in weekly rounds."
    ],
    links: [
      { label: "Latest weekly", href: "/leaderboards/latest-weekly" },
      { label: "Latest monthly", href: "/leaderboards/latest-monthly" },
      { label: "Rounds", href: "/rounds" }
    ]
  },
  {
    id: "2026-05-19-weekly-round-performance",
    date: "2026-05-19",
    title: "Interim weekly round performance added",
    category: "Benchmark",
    status: "published",
    summary:
      "Round pages can now show interim model allocation returns, S&P 500 returns, and Portfolio Minus S&P 500 when price snapshots are available.",
    details: [
      "The CLI can calculate weekly performance from existing price snapshots without resolving the official one-month leaderboard early.",
      "Supabase now stores published weekly price and model-performance rows so round pages can render the chart from the public read model.",
      "Round 1 is backfilled with the May 8 entry snapshot and the May 15 price snapshot already used for Round 2 inputs."
    ],
    links: [
      { label: "Round 1", href: "/rounds/CB-2026-05-10-1M" },
      { label: "Rounds", href: "/rounds" },
      { label: "Scoring", href: "/scoring" }
    ]
  },
  {
    id: "2026-05-18-one-month-objective-clarified",
    date: "2026-05-18",
    title: "One-month prompt objective clarified",
    category: "Methodology",
    status: "published",
    summary:
      "Future CapitalBench prompts now make the one-month scoring window explicit before models choose allocations.",
    details: [
      "Newly initialized portfolio prompts instruct models to optimize for the close-to-close one-month scoring window from entry adjusted close to exit adjusted close.",
      "Single-pick prompt defaults received the same clarification so older and newer submission formats remain conceptually aligned.",
      "Generated model inputs now include scoring-window, close-to-close scoring, and timeline-focus metadata derived from each round manifest's entry date, exit date, and horizon."
    ],
    links: [
      { label: "Methodology", href: "/methodology" },
      { label: "Scoring", href: "/scoring" }
    ]
  },
  {
    id: "2026-05-17-universe-v2-approved",
    date: "2026-05-17",
    title: "Universe v2.0 approved for future rounds",
    category: "Data",
    status: "published",
    summary:
      "CapitalBench now has an expanded 65-option universe for future rounds while preserving the original 40-option universe for completed rounds.",
    details: [
      "Universe v2.0 keeps every v1.5 option and adds 25 Tiingo-validated exposures across equal-weight US equity, biotechnology, regional banks, aerospace and defense, country equity, bonds, commodities, currencies, and crypto ETF proxies.",
      "Round manifests can now carry a universe_version value so the website and Supabase read model can show which option file was frozen for each round.",
      "The public universe page now shows version history and renders the latest approved option table without changing any completed round inputs."
    ],
    links: [
      { label: "Universe", href: "/universe" },
      { label: "Rounds", href: "/rounds" }
    ]
  },
  {
    id: "2026-05-13-portfolio-protocol-groundwork",
    date: "2026-05-13",
    title: "Portfolio round protocol groundwork added",
    category: "Methodology",
    status: "published",
    summary:
      "CapitalBench now supports a versioned portfolio submission protocol for future rounds while preserving single-pick compatibility for completed rounds.",
    details: [
      "Future portfolio rounds can require 1 to 5 holdings, 5% allocation increments, and exactly 100% total allocation through frozen round manifest constraints.",
      "CLI validation, mock submissions, scoring, reports, Supabase sync, and website tables now understand portfolio allocations and holding-level audit rows.",
      "Completed single-pick rounds remain labeled and scored under their original methodology; portfolio rounds are reported separately by submission format."
    ],
    links: [
      { label: "Methodology", href: "/methodology" },
      { label: "Scoring", href: "/scoring" }
    ]
  },
  {
    id: "2026-05-13-changelog-established",
    date: "2026-05-13",
    title: "Public changelog format established",
    category: "Operations",
    status: "published",
    summary:
      "CapitalBench now has a dedicated public changelog for user-approved major changes to benchmark protocol, round data, scoring, and operations.",
    details: [
      "Entries are reverse chronological and anchored so individual updates can be linked directly.",
      "Each entry includes a category, status, concise impact summary, implementation notes, and relevant links.",
      "Routine UI, UX, copy, and visual-design changes are excluded unless they materially affect benchmark interpretation."
    ],
    links: [
      { label: "Public docs", href: "/docs" },
      { label: "Rounds", href: "/rounds" }
    ]
  }
];

export const changelogCategories: ChangelogCategory[] = [
  "Benchmark",
  "Data",
  "Methodology",
  "Operations",
  "Research",
  "Security"
];
