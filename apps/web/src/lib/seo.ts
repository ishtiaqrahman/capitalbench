import { staticRoundRecords } from "./localRoundRecords";

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
  defaultTitle: "CapitalBench - AI Market Picks Scoreboard",
  description:
    "CapitalBench gives AI models the same market information, records their portfolios, and scores them using real market returns.",
  url: "https://www.capitalbench.org",
  githubUrl: "https://github.com/ishtiaqrahman/capitalbench",
  ogImage: "/og-image.png",
  ogImageAlt:
    "CapitalBench public AI market-picks scoreboard showing saved model portfolios, proof files, and pending results.",
  ogImageWidth: 1200,
  ogImageHeight: 630,
  themeColor: "#f4f6f5"
};

const defaultLastmod = "2026-05-26";
const publicRounds = staticRoundRecords();

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
    title: "CapitalBench Results",
    description:
      "CapitalBench results showing which AI model portfolios are winning in weekly and monthly market tests.",
    priority: 0.82,
    changefreq: "weekly",
    lastmod: defaultLastmod
  },
  {
    path: "/leaderboards/latest",
    title: "Latest CapitalBench Results",
    description:
      "Latest CapitalBench results split into one-week and one-month market tests.",
    priority: 0.9,
    changefreq: "weekly",
    lastmod: defaultLastmod
  },
  {
    path: "/leaderboards/latest-weekly",
    title: "Latest Weekly CapitalBench Results",
    description:
      "Latest one-week CapitalBench results with model portfolios and market returns kept separate from monthly tests.",
    priority: 0.9,
    changefreq: "weekly",
    lastmod: defaultLastmod
  },
  {
    path: "/leaderboards/latest-monthly",
    title: "Latest Monthly CapitalBench Results",
    description:
      "Latest one-month CapitalBench results with model portfolios and market returns kept separate from weekly tests.",
    priority: 0.9,
    changefreq: "weekly",
    lastmod: defaultLastmod
  },
  {
    path: "/leaderboards/cumulative-official",
    title: "Overall CapitalBench Results",
    description:
      "Overall CapitalBench results split into weekly and monthly market tests.",
    priority: 0.86,
    changefreq: "weekly",
    lastmod: defaultLastmod
  },
  {
    path: "/leaderboards/cumulative-stability",
    title: "CapitalBench Consistency Results",
    description:
      "CapitalBench consistency results split into weekly and monthly market tests.",
    priority: 0.82,
    changefreq: "weekly",
    lastmod: defaultLastmod
  },
  {
    path: "/leaderboards/cumulative-weekly",
    title: "Overall Weekly CapitalBench Results",
    description: "Overall CapitalBench results for completed one-week market tests only.",
    priority: 0.86,
    changefreq: "weekly",
    lastmod: defaultLastmod
  },
  {
    path: "/leaderboards/cumulative-monthly",
    title: "Overall Monthly CapitalBench Results",
    description: "Overall CapitalBench results for completed one-month market tests only.",
    priority: 0.86,
    changefreq: "weekly",
    lastmod: defaultLastmod
  },
  {
    path: "/rounds",
    title: "CapitalBench Test Rounds",
    description:
      "Index of CapitalBench market tests with dates, model portfolios, scoring status, and proof links.",
    priority: 0.84,
    changefreq: "weekly",
    lastmod: defaultLastmod
  },
  ...publicRounds.map((round) => ({
    path: `/rounds/${round.round_id}`,
    title: `${round.round_id} Proof Files`,
    description: `${round.title}: model portfolios, starting prices, pending status, and published proof hashes for the ${round.horizon} market test.`,
    priority: 0.8,
    changefreq: "weekly" as const,
    lastmod: defaultLastmod
  })),
  {
    path: "/methodology",
    title: "How CapitalBench Works",
    description:
      "How CapitalBench gives AI models the same market information, saves their portfolios, and scores them with real market prices.",
    priority: 0.88,
    changefreq: "monthly",
    lastmod: defaultLastmod
  },
  {
    path: "/universe",
    title: "CapitalBench Asset List",
    description:
      "Versioned CapitalBench asset lists for public market tests, including cash, ETFs, sectors, factors, bonds, commodities, country equity, currencies, and crypto proxies.",
    priority: 0.76,
    changefreq: "monthly",
    lastmod: defaultLastmod
  },
  {
    path: "/scoring",
    title: "CapitalBench Scoring",
    description:
      "How CapitalBench compares AI model portfolio returns with the S&P 500 in weekly and monthly tests.",
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
    title: "CapitalBench Proof And Data",
    description:
      "CapitalBench proof and data pages for scoring, fairness, limits, asset lists, and test-round source files.",
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
    lastmod: "2026-05-26"
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
  methodology: "How It Works",
  universe: "Asset List",
  scoring: "Scoring",
  fairness: "Fairness",
  limitations: "Limitations",
  docs: "Proof",
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
