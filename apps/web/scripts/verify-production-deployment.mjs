import apiReadModel from "../src/generated/apiReadModel.js";

const siteUrl = (process.env.PRODUCTION_SITE_URL || "https://www.capitalbench.org").replace(/\/$/, "");
const attempts = Math.max(1, Number(process.env.DEPLOY_VERIFY_ATTEMPTS || 6));
const retryDelayMs = Math.max(0, Number(process.env.DEPLOY_VERIFY_DELAY_MS || 10_000));
const cacheKey = process.env.GITHUB_SHA || String(Date.now());
const buildDate = new Date().toISOString().slice(0, 10);

function renderedStatus(round) {
  if (round.status === "active") return round.exit_date && round.exit_date < buildDate ? "overdue" : "pending";
  return round.status;
}

function latestRound(rounds, track) {
  return rounds
    .filter((round) => round.track === track)
    .sort((left, right) =>
      `${right.decision_deadline_utc}:${right.round_id}`.localeCompare(`${left.decision_deadline_utc}:${left.round_id}`)
    )[0];
}

function tagWithAriaLabel(html, label) {
  const escaped = label.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
  return html.match(new RegExp(`<[^>]*aria-label=["']${escaped}["'][^>]*>`, "i"))?.[0] || "";
}

function numericAttribute(tag, name) {
  const value = tag.match(new RegExp(`${name}=["'](\\d+)["']`, "i"))?.[1];
  return value === undefined ? null : Number(value);
}

async function fetchHtml(path) {
  const separator = path.includes("?") ? "&" : "?";
  const response = await fetch(`${siteUrl}${path}${separator}deployment=${encodeURIComponent(cacheKey)}`, {
    headers: { "Cache-Control": "no-cache" }
  });
  if (!response.ok) throw new Error(`${path} returned HTTP ${response.status}`);
  return response.text();
}

function assert(condition, message) {
  if (!condition) throw new Error(message);
}

const activeRounds = apiReadModel.rounds.filter((round) => {
  if (!["weekly", "monthly"].includes(round.track) || renderedStatus(round) !== "pending" || !round.official_run_id) return false;
  return apiReadModel.portfolios.some(
    (portfolio) => portfolio.round_id === round.round_id && portfolio.run_id === round.official_run_id
  );
});
const activeRunByRoundId = new Map(activeRounds.map((round) => [round.round_id, round.official_run_id]));
const activePortfolioKeys = new Set(
  apiReadModel.portfolios
    .filter((portfolio) => activeRunByRoundId.get(portfolio.round_id) === portfolio.run_id)
    .map((portfolio) => `${portfolio.round_id}:${portfolio.run_id}:${portfolio.model_id}`)
);
const expected = {
  all: activeRounds.length,
  weekly: activeRounds.filter((round) => round.track === "weekly").length,
  monthly: activeRounds.filter((round) => round.track === "monthly").length,
  portfolios: activePortfolioKeys.size
};
const latestByTrack = [latestRound(activeRounds, "weekly"), latestRound(activeRounds, "monthly")].filter(Boolean);

async function verify() {
  const [homepageHtml, liveHtml, roundsHtml, ...roundPages] = await Promise.all([
    fetchHtml("/"),
    fetchHtml("/live/"),
    fetchHtml("/rounds/"),
    ...latestByTrack.map((round) => fetchHtml(`/rounds/${round.round_id}/`))
  ]);
  const homepageTag = tagWithAriaLabel(homepageHtml, "Live dashboard summary");
  const liveTag = tagWithAriaLabel(liveHtml, "Current live dashboard status");
  assert(homepageTag, "homepage live dashboard summary is missing");
  assert(liveTag, "live dashboard status is missing");
  assert(homepageTag.includes("data-count-up-skip"), "homepage live counts can be hidden by reveal animation");

  for (const [attribute, value] of [
    ["data-open-round-count", expected.all],
    ["data-weekly-open-round-count", expected.weekly],
    ["data-monthly-open-round-count", expected.monthly],
    ["data-live-portfolio-count", expected.portfolios]
  ]) {
    assert(numericAttribute(homepageTag, attribute) === value, `homepage ${attribute} is stale`);
    assert(numericAttribute(liveTag, attribute) === value, `live dashboard ${attribute} is stale`);
  }

  latestByTrack.forEach((round, index) => {
    const href = `/rounds/${round.round_id}/`;
    assert(homepageHtml.includes(href), `homepage is missing ${round.round_id}`);
    assert(liveHtml.includes(href), `live dashboard is missing ${round.round_id}`);
    assert(roundsHtml.includes(href), `rounds index is missing ${round.round_id}`);
    assert(roundPages[index].includes(round.round_id), `${round.round_id} audit packet is incomplete`);
  });
}

let lastError;
for (let attempt = 1; attempt <= attempts; attempt += 1) {
  try {
    await verify();
    console.log(JSON.stringify({ ok: true, site_url: siteUrl, expected, latest_round_ids: latestByTrack.map((round) => round.round_id) }));
    process.exit(0);
  } catch (error) {
    lastError = error;
    if (attempt < attempts) {
      console.warn(`Production verification attempt ${attempt}/${attempts} failed: ${error.message}`);
      await new Promise((resolve) => setTimeout(resolve, retryDelayMs));
    }
  }
}

console.error(`Production verification failed after ${attempts} attempt(s): ${lastError?.message || "unknown error"}`);
process.exit(1);
