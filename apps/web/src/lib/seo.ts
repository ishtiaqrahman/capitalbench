import { staticRoundRecords } from "./localRoundRecords";
import { staticModelProfiles } from "./modelProfiles";
import apiReadModel from "../generated/apiReadModel.js";
import { buildBenchmarkSetsData } from "./benchmarkSets.js";
import { changelogEntries } from "../data/changelog";

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
  defaultTitle: "AI Capital Allocation Benchmark | CapitalBench",
  description:
    "CapitalBench tracks live AI model portfolios, current AI positioning, risk appetite, and benchmark results scored against real market returns.",
  url: "https://www.capitalbench.org",
  githubUrl: "https://github.com/ishtiaqrahman/capitalbench",
  ogImage: "/og-image.png",
  ogImageAlt:
    "CapitalBench live AI capital allocation benchmark showing model portfolios, audit packets, and benchmark results.",
  ogImageWidth: 1200,
  ogImageHeight: 630,
  themeColor: "#f4f6f5"
};

function dateOnly(value: string | null | undefined): string | undefined {
  if (!value) return undefined;
  return String(value).slice(0, 10);
}

function latestDate(values: Array<string | null | undefined>, maxDate?: string): string | undefined {
  return values
    .map(dateOnly)
    .filter((value): value is string => Boolean(value))
    .filter((value) => !maxDate || value <= maxDate)
    .sort()
    .at(-1);
}

const latestPublicChangeDate = changelogEntries[0]?.date ?? "2026-05-26";
const publicRounds = staticRoundRecords();
const publicModels = staticModelProfiles();
const benchmarkSets = buildBenchmarkSetsData(apiReadModel).sets as any[];
const latestDataDate = dateOnly((apiReadModel as any).generated_at) ?? latestPublicChangeDate;
const latestRoundDate =
  latestDate(publicRounds.flatMap((round) => [round.exit_date, round.entry_date, round.decision_date]), latestDataDate) ??
  latestDataDate;
const latestResolvedRoundDate =
  latestDate(
    publicRounds
      .filter((round) => round.status === "resolved")
      .flatMap((round) => [round.exit_date, round.entry_date, round.decision_date]),
    latestDataDate
  ) ?? latestRoundDate;
const latestInsightDate =
  latestDate([(apiReadModel as any).insights?.data_as_of, (apiReadModel as any).insights?.generated_at]) ??
  latestDataDate;
const defaultLastmod = latestPublicChangeDate;

export const routeMeta: RouteMeta[] = [
  {
    path: "/",
    title: siteConfig.defaultTitle,
    description: siteConfig.description,
    priority: 1,
    changefreq: "weekly",
    lastmod: latestDataDate
  },
  {
    path: "/leaderboards",
    title: "AI Portfolio Benchmark Results",
    description:
      "Weekly and monthly AI model portfolio results, rankings, market returns, and public audit packets from CapitalBench.",
    priority: 0.82,
    changefreq: "weekly",
    lastmod: latestResolvedRoundDate
  },
  {
    path: "/leaderboards/latest",
    title: "Latest AI Portfolio Benchmark Results",
    description:
      "Latest scored AI model portfolio results from CapitalBench, split into one-week and one-month market tests.",
    priority: 0.9,
    changefreq: "weekly",
    lastmod: latestResolvedRoundDate
  },
  {
    path: "/leaderboards/latest-weekly",
    title: "Latest Weekly AI Portfolio Results",
    description:
      "Latest one-week CapitalBench rankings with AI model portfolios, S&P 500 comparison, and audit evidence.",
    priority: 0.9,
    changefreq: "weekly",
    lastmod: latestResolvedRoundDate
  },
  {
    path: "/leaderboards/latest-monthly",
    title: "Latest Monthly AI Portfolio Results",
    description:
      "Latest one-month CapitalBench rankings with AI model portfolios, S&P 500 comparison, and audit evidence.",
    priority: 0.9,
    changefreq: "weekly",
    lastmod: latestResolvedRoundDate
  },
  {
    path: "/leaderboards/benchmark-sets",
    title: "Equal-Run AI Benchmark Sets",
    description:
      "CapitalBench equal-run comparison sets for fair weekly and monthly AI model benchmark rankings.",
    priority: 0.88,
    changefreq: "weekly",
    lastmod: latestResolvedRoundDate
  },
  ...benchmarkSets.map((set) => ({
    path: `/leaderboards/benchmark-sets/${set.set_id}`,
    title: `${set.label} AI Benchmark Comparison Set`,
    description: `${set.label} ranks AI models only on ${set.track} rounds every set model completed.`,
    priority: set.is_current ? 0.86 : 0.78,
    changefreq: "weekly" as const,
    lastmod: latestResolvedRoundDate
  })),
  {
    path: "/leaderboards/cumulative-official",
    title: "Overall AI Portfolio Benchmark Results",
    description:
      "Overall CapitalBench scorecards across completed weekly and monthly AI portfolio market tests.",
    priority: 0.86,
    changefreq: "weekly",
    lastmod: latestResolvedRoundDate
  },
  {
    path: "/leaderboards/cumulative-stability",
    title: "AI Model Consistency Results",
    description:
      "CapitalBench consistency results for AI model portfolios across completed weekly and monthly tests.",
    priority: 0.82,
    changefreq: "weekly",
    lastmod: latestResolvedRoundDate
  },
  {
    path: "/leaderboards/cumulative-weekly",
    title: "Overall Weekly AI Portfolio Results",
    description: "Overall CapitalBench Score results for completed one-week AI portfolio market tests.",
    priority: 0.86,
    changefreq: "weekly",
    lastmod: latestResolvedRoundDate
  },
  {
    path: "/leaderboards/cumulative-monthly",
    title: "Overall Monthly AI Portfolio Results",
    description: "Overall CapitalBench Score results for completed one-month AI portfolio market tests.",
    priority: 0.86,
    changefreq: "weekly",
    lastmod: latestResolvedRoundDate
  },
  {
    path: "/rounds",
    title: "AI Portfolio Benchmark Rounds",
    description:
      "CapitalBench round index with AI model portfolios, scoring status, market windows, and audit packet links.",
    priority: 0.84,
    changefreq: "weekly",
    lastmod: latestRoundDate
  },
  {
    path: "/models",
    title: "AI Model Portfolio Profiles",
    description:
      "CapitalBench model profiles with live holdings, weekly and monthly records, allocation patterns, and audit packet links.",
    priority: 0.86,
    changefreq: "weekly",
    lastmod: latestDataDate
  },
  {
    path: "/models/patterns",
    title: "AI Model Behavior Patterns",
    description:
      "Compare AI models by risk appetite, concentration, defensive ballast, overlap, turnover, and resolved performance profile.",
    priority: 0.84,
    changefreq: "weekly",
    lastmod: latestDataDate
  },
  {
    path: "/api",
    title: "AI Model Portfolio Data API",
    description:
      "API documentation for AI model portfolios, active positioning, benchmark scores, asset universes, and audit metadata.",
    priority: 0.84,
    changefreq: "weekly",
    lastmod: latestDataDate
  },
  {
    path: "/api/use-cases",
    title: "AI Portfolio Data API Use Cases",
    description:
      "Visual API use cases for financial websites, trading platforms, quant workflows, research desks, and AI model teams.",
    priority: 0.82,
    changefreq: "monthly",
    lastmod: latestDataDate
  },
  {
    path: "/private-evals",
    title: "Private AI Investment Benchmark Evaluations",
    description:
      "Privately benchmark AI investment models with frozen inputs, real market outcomes, consistency testing, and auditable results.",
    priority: 0.86,
    changefreq: "monthly",
    lastmod: defaultLastmod
  },
  {
    path: "/private-eval-sample-report",
    title: "Sample Private Eval Report",
    description:
      "A rendered sample CapitalBench private evaluation report using public benchmark evidence and the private-report format.",
    priority: 0.58,
    changefreq: "monthly",
    lastmod: defaultLastmod
  },
  {
    path: "/insights",
    title: "AI Investment Model Insights",
    description:
      "Insights from AI model positioning, benchmark results, risk appetite, model behavior, and market-window math.",
    priority: 0.86,
    changefreq: "weekly",
    lastmod: latestInsightDate
  },
  {
    path: "/manifesto",
    title: "AI Capital Allocation Benchmark Manifesto",
    description:
      "Why CapitalBench measures AI investment decisions with frozen public-market portfolios, auditable records, and real outcomes.",
    priority: 0.84,
    changefreq: "monthly",
    lastmod: defaultLastmod
  },
  ...publicModels.map((profile) => ({
    path: `/models/${profile.modelId}`,
    title: `${profile.label} AI Portfolio Profile`,
    description: `${profile.label} live holdings, weekly and monthly CapitalBench results, allocation patterns, and public audit packets.`,
    priority: 0.78,
    changefreq: "weekly" as const,
    lastmod: latestDataDate
  })),
  ...publicRounds.map((round) => ({
    path: `/rounds/${round.round_id}`,
    title: round.status === "resolved" ? `${round.round_id} Result And Audit Packet` : `${round.round_id} Audit Packet`,
    description:
      round.status === "resolved"
        ? `${round.round_id} ${round.horizon} result with model portfolio scores, S&P 500 comparison, scoring prices, and audit hashes.`
        : round.status === "overdue"
          ? `${round.round_id} ${round.horizon} audit packet with frozen model portfolios, starting prices, overdue status, and audit hashes.`
        : `${round.round_id} ${round.horizon} audit packet with frozen model portfolios, starting prices, pending status, and audit hashes.`,
    priority: 0.8,
    changefreq: "weekly" as const,
    lastmod:
      round.status === "pending" || round.status === "overdue"
        ? latestDataDate
        : latestDate([round.exit_date, round.entry_date, round.decision_date]) ?? latestRoundDate
  })),
  {
    path: "/methodology",
    title: "AI Investment Benchmark Methodology",
    description:
      "How CapitalBench gives AI models the same market information, freezes their portfolios, and scores them with real market prices.",
    priority: 0.88,
    changefreq: "monthly",
    lastmod: defaultLastmod
  },
  {
    path: "/risk-appetite",
    title: "AI Portfolio Risk Appetite",
    description:
      "CapitalBench AI Risk Appetite methodology, current readings, model agreement, open-book risk, and versioned asset ratings.",
    priority: 0.82,
    changefreq: "weekly",
    lastmod: latestDataDate
  },
  {
    path: "/universe",
    title: "AI Benchmark Asset Universe",
    description:
      "Versioned CapitalBench asset universe for public market tests, including cash, ETFs, sectors, factors, bonds, commodities, and crypto proxies.",
    priority: 0.76,
    changefreq: "monthly",
    lastmod: defaultLastmod
  },
  {
    path: "/scoring",
    title: "AI Portfolio Benchmark Scoring",
    description:
      "How CapitalBench scores AI model portfolio returns against S&P 500 returns and maximum possible return context.",
    priority: 0.72,
    changefreq: "monthly",
    lastmod: defaultLastmod
  },
  {
    path: "/fairness",
    title: "CapitalBench Fairness Controls",
    description:
      "Fairness controls for CapitalBench market tests: same information, saved inputs, separate runs, and no retroactive score changes.",
    priority: 0.7,
    changefreq: "monthly",
    lastmod: defaultLastmod
  },
  {
    path: "/limitations",
    title: "CapitalBench Limitations",
    description:
      "Limitations of weekly and monthly AI market-pick tests, including noisy outcomes, small samples, provider changes, and the non-advice boundary.",
    priority: 0.68,
    changefreq: "monthly",
    lastmod: defaultLastmod
  },
  {
    path: "/docs",
    title: "CapitalBench Audit And Data Docs",
    description:
      "CapitalBench audit and data pages for scoring, fairness, limits, asset lists, and round source files.",
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
    lastmod: latestPublicChangeDate
  },
  {
    path: "/contribute",
    title: "Contribute to CapitalBench",
    description:
      "Contribute to CapitalBench public benchmark infrastructure through monthly or one-time Stripe-hosted contributions.",
    priority: 0.62,
    changefreq: "monthly",
    lastmod: "2026-05-13"
  },
  {
    path: "/contribute/thanks",
    title: "Thank You for Contributing to CapitalBench",
    description: "Thank you for contributing to CapitalBench public benchmark infrastructure.",
    priority: 0.1,
    changefreq: "monthly",
    lastmod: "2026-05-13",
    sitemap: false,
    noindex: true
  },
  {
    path: "/privacy",
    title: "CapitalBench Privacy",
    description: "CapitalBench privacy note for website analytics, contribution links, and public benchmark data.",
    priority: 0.42,
    changefreq: "monthly",
    lastmod: "2026-05-14"
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
  leaderboards: "Results",
  latest: "Latest Results",
  "latest-weekly": "Weekly Results",
  "latest-monthly": "Monthly Results",
  "cumulative-official": "Overall Results",
  "cumulative-stability": "Consistency Results",
  "cumulative-weekly": "Overall Weekly",
  "cumulative-monthly": "Overall Monthly",
  rounds: "Rounds",
  models: "Models",
  api: "API",
  "use-cases": "Use Cases",
  "private-evals": "Private Evals",
  "private-eval-sample-report": "Sample Private Eval Report",
  insights: "Insights",
  manifesto: "Manifesto",
  methodology: "Methodology",
  "risk-appetite": "AI Risk Appetite",
  universe: "Asset List",
  scoring: "Scoring",
  fairness: "Fairness",
  limitations: "Limitations",
  docs: "Audit",
  changelog: "Changelog",
  contribute: "Contribute",
  thanks: "Thanks",
  privacy: "Privacy",
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
  dateModified?: string;
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
    dateModified: input.dateModified,
    temporalCoverage: input.temporalCoverage,
    keywords: input.keywords,
    variableMeasured: input.variableMeasured
  };
}

export function itemListSchema(input: {
  name: string;
  description: string;
  path: string;
  items: Array<{
    name: string;
    url: string;
    description?: string;
    position?: number;
  }>;
}): JsonLdRecord {
  return {
    "@type": "ItemList",
    "@id": `${canonicalUrl(input.path)}#item-list`,
    name: input.name,
    description: input.description,
    url: canonicalUrl(input.path),
    itemListOrder: "https://schema.org/ItemListOrderDescending",
    numberOfItems: input.items.length,
    itemListElement: input.items.map((item, index) => {
      const url = item.url.startsWith("http") ? item.url : canonicalUrl(item.url);
      return {
        "@type": "ListItem",
        position: item.position ?? index + 1,
        item: {
          "@type": "WebPage",
          "@id": `${url}#webpage`,
          url,
          name: item.name,
          description: item.description
        }
      };
    })
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
