import type { APIRoute } from "astro";
import { assetUrl } from "../lib/seo";

export const prerender = true;

export const GET: APIRoute = () =>
  new Response(`User-agent: *\nAllow: /\n\nSitemap: ${assetUrl("/sitemap.xml")}\n`, {
    headers: {
      "Content-Type": "text/plain; charset=utf-8"
    }
  });
