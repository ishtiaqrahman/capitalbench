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
