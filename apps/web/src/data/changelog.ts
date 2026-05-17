export type ChangelogCategory =
  | "Benchmark"
  | "Data"
  | "Methodology"
  | "Operations"
  | "Research"
  | "Security"
  | "Site";

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
    category: "Site",
    status: "published",
    summary:
      "CapitalBench now has a dedicated public changelog for user-approved major changes to the site, benchmark protocol, round data, scoring, and operations.",
    details: [
      "Entries are reverse chronological and anchored so individual updates can be linked directly.",
      "Each entry includes a category, status, concise impact summary, implementation notes, and relevant links.",
      "Only major changes that are explicitly selected for public reporting should be added here."
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
  "Security",
  "Site"
];
