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
      { label: "Asset list", href: "/assets" },
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
      "Round pages can now show interim model allocation returns versus S&P 500 when weekly price snapshots are available.",
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
