import type { APIRoute } from "astro";
import { canonicalUrl, publicSitemapRoutes } from "../lib/seo";

export const prerender = true;

export const GET: APIRoute = () => {
  const urls = publicSitemapRoutes()
    .map(
      (route) => `  <url>
    <loc>${canonicalUrl(route.path)}</loc>
    <lastmod>${route.lastmod}</lastmod>
    <changefreq>${route.changefreq}</changefreq>
    <priority>${route.priority.toFixed(2)}</priority>
  </url>`
    )
    .join("\n");

  return new Response(`<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n${urls}\n</urlset>\n`, {
    headers: {
      "Content-Type": "application/xml; charset=utf-8"
    }
  });
};
