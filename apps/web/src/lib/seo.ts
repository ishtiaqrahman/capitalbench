import { rounds } from "../data/fallback";

export type RouteMeta = {
  path: string;
  title: string;
  description: string;
  priority: number;
  changefreq: "weekly" | "monthly";
  lastmod: string;
  sitemap?: boolean;
  noindex?: boolean;
};

export type BreadcrumbItem = {
  name: string;
  href: string;
};

export type JsonLdRecord = Record<string, unknown>;

export const siteConfig = {
  name: "CapitalBench",
  defaultTitle: "CapitalBench - LLM Market Benchmark and Leaderboards",
  description:
    "CapitalBench is a public benchmark for one-shot LLM market decisions, official model picks, audit hashes, and leaderboards.",
  url: "https://www.capitalbench.org",
  githubUrl: "https://github.com/ishtiaqrahman/capitalbench",
  ogImage: "/og-image.png",
  ogImageAlt:
    "CapitalBench public LLM market benchmark showing frozen inputs, official picks, and pending leaderboard status.",
  ogImageWidth: 1200,
  ogImageHeight: 630,
  themeColor: "#f7f8f6"
};

const defaultLastmod = "2026-05-12";

export const routeMeta: RouteMeta[] = [
  {
    path: "/",
    title: siteConfig.defaultTitle,
    description: siteConfig.description,
    priority: 1,
    changefreq: "weekly",
    lastmod: defaultLastmod
  },
  {
    path: "/leaderboards",
    title: "CapitalBench Leaderboards",
    description:
      "CapitalBench leaderboard hub for latest official results, cumulative one-shot scores, and repeated-run stability metrics.",
    priority: 0.82,
    changefreq: "weekly",
    lastmod: defaultLastmod
  },
  {
    path: "/leaderboards/latest",
    title: "Latest LLM Market Leaderboard",
    description:
      "Latest CapitalBench official leaderboard for one-shot LLM market decisions, with pending picks shown before scored performance is published.",
    priority: 0.9,
    changefreq: "weekly",
    lastmod: defaultLastmod
  },
  {
    path: "/leaderboards/cumulative-official",
    title: "Cumulative Official LLM Leaderboard",
    description:
      "Cumulative official CapitalBench results, averaging one-shot LLM alpha versus S&P 500 across resolved benchmark rounds.",
    priority: 0.86,
    changefreq: "weekly",
    lastmod: defaultLastmod
  },
  {
    path: "/leaderboards/cumulative-stability",
    title: "Cumulative Stability Leaderboard",
    description:
      "Repeated-run CapitalBench stability results for LLM market decisions, reported separately from official one-shot scores.",
    priority: 0.82,
    changefreq: "weekly",
    lastmod: defaultLastmod
  },
  {
    path: "/rounds",
    title: "CapitalBench Rounds",
    description:
      "Index of CapitalBench benchmark rounds with deadlines, horizons, official run IDs, scoring status, and audit links.",
    priority: 0.84,
    changefreq: "weekly",
    lastmod: defaultLastmod
  },
  ...rounds.map((round) => ({
    path: `/rounds/${round.round_id}`,
    title: `${round.round_id} Round Audit Packet`,
    description: `${round.title}: official LLM picks, entry prices, pending status, and published audit hashes for the ${round.horizon} benchmark round.`,
    priority: 0.8,
    changefreq: "weekly" as const,
    lastmod: defaultLastmod
  })),
  {
    path: "/methodology",
    title: "CapitalBench Methodology",
    description:
      "CapitalBench methodology for frozen prompts, one-shot LLM submissions, official scoring, stability runs, fairness controls, and audit artifacts.",
    priority: 0.88,
    changefreq: "monthly",
    lastmod: defaultLastmod
  },
  {
    path: "/universe",
    title: "CapitalBench Option Universe",
    description:
      "Frozen CapitalBench option universe for public benchmark rounds, including cash, ETFs, sectors, factors, bonds, commodities, and AI themes.",
    priority: 0.76,
    changefreq: "monthly",
    lastmod: defaultLastmod
  },
  {
    path: "/scoring",
    title: "CapitalBench Scoring",
    description:
      "Definitions for CapitalBench official scores, selected-option returns, alpha versus S&P 500, regret, cash comparison, and stability metrics.",
    priority: 0.72,
    changefreq: "monthly",
    lastmod: defaultLastmod
  },
  {
    path: "/fairness",
    title: "CapitalBench Fairness Controls",
    description:
      "Fairness controls for CapitalBench benchmark rounds: identical prompt surfaces, frozen inputs, run isolation, and no retroactive backfills.",
    priority: 0.7,
    changefreq: "monthly",
    lastmod: defaultLastmod
  },
  {
    path: "/limitations",
    title: "CapitalBench Limitations",
    description:
      "Limitations of one-month LLM market benchmarks, including noisy outcomes, small samples, provider changes, and the non-advice boundary.",
    priority: 0.68,
    changefreq: "monthly",
    lastmod: defaultLastmod
  },
  {
    path: "/docs",
    title: "CapitalBench Documentation",
    description:
      "Public CapitalBench documentation hub for methodology, scoring, fairness, limitations, universe data, and round audit pages.",
    priority: 0.74,
    changefreq: "monthly",
    lastmod: defaultLastmod
  },
  {
    path: "/changelog",
    title: "CapitalBench Changelog",
    description:
      "Public CapitalBench changelog for major website, benchmark, data, methodology, security, and operations updates.",
    priority: 0.66,
    changefreq: "monthly",
    lastmod: "2026-05-13"
  },
  {
    path: "/pro",
    title: "CapitalBench Pro",
    description:
      "CapitalBench Pro is a future gated product shell for exports, API access, and advanced benchmark analytics.",
    priority: 0.2,
    changefreq: "monthly",
    lastmod: defaultLastmod,
    sitemap: false,
    noindex: true
  }
];

const labelOverrides: Record<string, string> = {
  leaderboards: "Leaderboards",
  latest: "Latest",
  "cumulative-official": "Cumulative Official",
  "cumulative-stability": "Cumulative Stability",
  rounds: "Rounds",
  methodology: "Methodology",
  universe: "Universe",
  scoring: "Scoring",
  fairness: "Fairness",
  limitations: "Limitations",
  docs: "Docs",
  changelog: "Changelog",
  pro: "Pro"
};

export function normalizePath(pathname: string): string {
  const withoutQuery = pathname.split("?")[0]?.split("#")[0] ?? "/";
  if (withoutQuery === "" || withoutQuery === "/") return "/";
  return `/${withoutQuery.replace(/^\/+|\/+$/g, "")}`;
}

export function canonicalPath(pathname: string): string {
  const normalized = normalizePath(pathname);
  return normalized === "/" ? "/" : `${normalized}/`;
}

export function canonicalUrl(pathname: string): string {
  return new URL(canonicalPath(pathname), siteConfig.url).toString();
}

export function publicSitemapRoutes(): RouteMeta[] {
  return routeMeta.filter((route) => route.sitemap !== false && route.noindex !== true);
}

export function getRouteMeta(pathname: string): RouteMeta | undefined {
  const normalized = normalizePath(pathname);
  return routeMeta.find((route) => normalizePath(route.path) === normalized);
}

export function pageTitle(title?: string): string {
  if (!title || title === siteConfig.name) return siteConfig.defaultTitle;
  return title.includes(siteConfig.name) ? title : `${title} | ${siteConfig.name}`;
}

export function assetUrl(pathname: string): string {
  return new URL(pathname, siteConfig.url).toString();
}

export function getBreadcrumbs(pathname: string): BreadcrumbItem[] {
  const normalized = normalizePath(pathname);
  if (normalized === "/") return [];

  const segments = normalized.split("/").filter(Boolean);
  const items: BreadcrumbItem[] = [{ name: "Home", href: siteConfig.url }];
  let accumulated = "";

  for (const segment of segments) {
    accumulated += `/${segment}`;
    const route = getRouteMeta(accumulated);
    items.push({
      name: route?.title.replace(` | ${siteConfig.name}`, "") ?? labelOverrides[segment] ?? segment,
      href: canonicalUrl(accumulated)
    });
  }

  return items;
}

export function organizationSchema(): JsonLdRecord {
  return {
    "@type": "Organization",
    "@id": `${siteConfig.url}/#organization`,
    name: siteConfig.name,
    url: siteConfig.url,
    logo: assetUrl("/favicon.svg"),
    sameAs: [siteConfig.githubUrl],
    description: siteConfig.description
  };
}

export function websiteSchema(): JsonLdRecord {
  return {
    "@type": "WebSite",
    "@id": `${siteConfig.url}/#website`,
    name: siteConfig.name,
    alternateName: "CapitalBench LLM Market Benchmark",
    url: siteConfig.url,
    publisher: { "@id": `${siteConfig.url}/#organization` },
    inLanguage: "en-US"
  };
}

export function webPageSchema(pathname: string, title: string, description: string): JsonLdRecord {
  const url = canonicalUrl(pathname);
  return {
    "@type": "WebPage",
    "@id": `${url}#webpage`,
    url,
    name: title,
    description,
    isPartOf: { "@id": `${siteConfig.url}/#website` },
    about: { "@id": `${siteConfig.url}/#organization` },
    inLanguage: "en-US"
  };
}

export function breadcrumbSchema(pathname: string): JsonLdRecord | undefined {
  const breadcrumbs = getBreadcrumbs(pathname);
  if (breadcrumbs.length === 0) return undefined;
  return {
    "@type": "BreadcrumbList",
    itemListElement: breadcrumbs.map((item, index) => ({
      "@type": "ListItem",
      position: index + 1,
      name: item.name,
      item: item.href
    }))
  };
}

export function datasetSchema(input: {
  name: string;
  description: string;
  path: string;
  keywords: string[];
  datePublished?: string;
  temporalCoverage?: string;
  variableMeasured?: string[];
}): JsonLdRecord {
  return {
    "@type": "Dataset",
    "@id": `${canonicalUrl(input.path)}#dataset`,
    name: input.name,
    description: input.description,
    url: canonicalUrl(input.path),
    creator: { "@id": `${siteConfig.url}/#organization` },
    publisher: { "@id": `${siteConfig.url}/#organization` },
    isAccessibleForFree: true,
    datePublished: input.datePublished,
    temporalCoverage: input.temporalCoverage,
    keywords: input.keywords,
    variableMeasured: input.variableMeasured
  };
}

export function jsonLdGraph(items: Array<JsonLdRecord | undefined>): string {
  return JSON.stringify(
    {
      "@context": "https://schema.org",
      "@graph": items.filter(Boolean)
    },
    null,
    0
  ).replace(/</g, "\\u003c");
}
