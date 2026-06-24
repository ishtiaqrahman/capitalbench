import { existsSync, readdirSync, readFileSync, statSync } from "node:fs";
import { join, relative } from "node:path";

const distDir = new URL("../dist/", import.meta.url).pathname;
const changelogSourcePath = new URL("../src/data/changelog.ts", import.meta.url).pathname;
const siteUrl = "https://www.capitalbench.org";

function walk(dir) {
  return readdirSync(dir).flatMap((entry) => {
    const full = join(dir, entry);
    return statSync(full).isDirectory() ? walk(full) : [full];
  });
}

function pageUrlFromFile(file) {
  const rel = relative(distDir, file).replaceAll("\\", "/");
  if (rel === "index.html") return `${siteUrl}/`;
  if (rel.endsWith("/index.html")) return `${siteUrl}/${rel.replace(/\/index\.html$/, "/")}`;
  return `${siteUrl}/${rel}`;
}

function matchOne(html, pattern, label, file) {
  const match = html.match(pattern);
  if (!match?.[1]) throw new Error(`${label} missing in ${file}`);
  return match[1].trim();
}

if (!existsSync(distDir)) {
  throw new Error("dist directory is missing. Run npm run build first.");
}

const sitemapPath = join(distDir, "sitemap.xml");
const robotsPath = join(distDir, "robots.txt");
const sitemap = readFileSync(sitemapPath, "utf8");
const robots = readFileSync(robotsPath, "utf8");
const changelogSource = readFileSync(changelogSourcePath, "utf8");
const htmlFiles = walk(distDir).filter((file) => file.endsWith(".html"));
const titles = new Map();
const descriptions = new Map();
const sitemapUrls = new Set([...sitemap.matchAll(/<loc>(.*?)<\/loc>/g)].map((match) => match[1]));
const sitemapLastmodByUrl = new Map(
  [...sitemap.matchAll(/<url>\s*<loc>(.*?)<\/loc>\s*<lastmod>(.*?)<\/lastmod>/g)].map((match) => [match[1], match[2]])
);
const latestChangelogDate = matchOne(changelogSource, /date:\s*"(\d{4}-\d{2}-\d{2})"/, "latest changelog date", "src/data/changelog.ts");
const today = new Date().toISOString().slice(0, 10);

if (!robots.includes(`${siteUrl}/sitemap.xml`)) {
  throw new Error("robots.txt does not reference the canonical sitemap URL.");
}

for (const url of sitemapUrls) {
  const lastmod = sitemapLastmodByUrl.get(url);
  if (!lastmod) throw new Error(`sitemap lastmod missing for ${url}`);
  if (!/^\d{4}-\d{2}-\d{2}$/.test(lastmod)) throw new Error(`invalid sitemap lastmod for ${url}: ${lastmod}`);
  if (lastmod > today) throw new Error(`future sitemap lastmod for ${url}: ${lastmod} > ${today}`);
}

const changelogLastmod = sitemapLastmodByUrl.get(`${siteUrl}/changelog/`);
if (changelogLastmod !== latestChangelogDate) {
  throw new Error(`stale changelog sitemap lastmod: ${changelogLastmod} !== ${latestChangelogDate}`);
}

for (const file of htmlFiles) {
  const rel = relative(distDir, file).replaceAll("\\", "/");
  const html = readFileSync(file, "utf8");
  const url = pageUrlFromFile(file);
  const title = matchOne(html, /<title>(.*?)<\/title>/, "title", rel);
  const description = matchOne(html, /<meta name="description" content="([^"]+)"/, "meta description", rel);
  const canonical = matchOne(html, /<link rel="canonical" href="([^"]+)"/, "canonical", rel);
  const robotsMeta = matchOne(html, /<meta name="robots" content="([^"]+)"/, "robots meta", rel);

  if (!html.includes('type="application/ld+json"')) throw new Error(`JSON-LD missing in ${rel}`);
  if (!html.includes('property="og:image"')) throw new Error(`Open Graph image missing in ${rel}`);
  if (!html.includes('name="twitter:card" content="summary_large_image"')) {
    throw new Error(`large Twitter card missing in ${rel}`);
  }

  const h1Count = [...html.matchAll(/<h1[\s>]/g)].length;
  if (h1Count !== 1) throw new Error(`expected one h1 in ${rel}, found ${h1Count}`);

  if (titles.has(title)) throw new Error(`duplicate title "${title}" in ${rel} and ${titles.get(title)}`);
  titles.set(title, rel);

  if (descriptions.has(description)) {
    throw new Error(`duplicate meta description in ${rel} and ${descriptions.get(description)}`);
  }
  descriptions.set(description, rel);

  if (robotsMeta.includes("noindex")) {
    if (sitemapUrls.has(url)) throw new Error(`noindex page appears in sitemap: ${url}`);
    continue;
  }

  if (canonical !== url) throw new Error(`canonical mismatch in ${rel}: ${canonical} !== ${url}`);
  if (!sitemapUrls.has(url)) throw new Error(`indexable page missing from sitemap: ${url}`);
}

console.log(`SEO validation passed for ${htmlFiles.length} HTML pages and ${sitemapUrls.size} sitemap URLs.`);
