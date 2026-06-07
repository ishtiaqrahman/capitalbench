import apiReadModel from "../generated/apiReadModel.js";

const API_VERSION = "v1";
const DEFAULT_MINUTE_LIMIT = 120;
const DEFAULT_DAY_LIMIT = 10_000;
const VALID_TRACKS = new Set(["weekly", "monthly", "all"]);
const VALID_SCOPES = new Set(["active", "cumulative"]);
const VALID_GROUPS = new Set(["asset", "category", "model"]);
const CORS_HEADERS = {
  "access-control-allow-origin": "*",
  "access-control-allow-methods": "GET, OPTIONS",
  "access-control-allow-headers": "authorization, content-type",
  "access-control-max-age": "86400"
};

let apiAuthSchemaReady = false;

export function jsonApiResult(status, body, extraHeaders = {}) {
  return {
    status,
    headers: {
      "content-type": "application/json; charset=utf-8",
      "cache-control": "no-store",
      "x-capitalbench-api-version": API_VERSION,
      ...CORS_HEADERS,
      ...extraHeaders
    },
    body
  };
}

export function dataResultToResponse(result) {
  const body = result.status === 204 || result.status === 304 ? null : JSON.stringify(result.body);
  return new Response(body, {
    status: result.status,
    headers: result.headers
  });
}

function errorResult(status, error, message, extra = {}, headers = {}) {
  return jsonApiResult(status, { error, message, ...extra }, headers);
}

async function sha256Hex(value) {
  const data = new TextEncoder().encode(String(value));
  const hash = await crypto.subtle.digest("SHA-256", data);
  return Array.from(new Uint8Array(hash))
    .map((byte) => byte.toString(16).padStart(2, "0"))
    .join("");
}

export async function hashApiKey(apiKey) {
  return await sha256Hex(apiKey);
}

async function ensureApiAuthSchema(db) {
  if (apiAuthSchemaReady) return;

  await db
    .prepare(
      `create table if not exists data_api_keys (
         id text primary key,
         key_hash text not null unique,
         name text not null,
         email text,
         status text not null default 'active' check (status in ('active', 'disabled', 'revoked')),
         scopes text not null default 'read:v1',
         rate_limit_per_minute integer,
         rate_limit_per_day integer,
         created_at text not null,
         last_used_at text
       )`
    )
    .run();
  await db.prepare("create index if not exists idx_data_api_keys_status on data_api_keys(status)").run();
  await db
    .prepare(
      `create table if not exists data_api_rate_limits (
         key_hash text not null,
         window_name text not null,
         window_start text not null,
         count integer not null default 0,
         updated_at text not null,
         primary key (key_hash, window_name, window_start)
       )`
    )
    .run();

  apiAuthSchemaReady = true;
}

export function createD1ApiAuthRepository(db) {
  if (!db) throw new Error("EMAIL_DB binding is not configured");
  return {
    async findKeyByHash(keyHash) {
      await ensureApiAuthSchema(db);
      return await db
        .prepare("select * from data_api_keys where key_hash = ? and status = 'active'")
        .bind(keyHash)
        .first();
    },

    async touchKey(keyHash, nowIso) {
      await ensureApiAuthSchema(db);
      await db.prepare("update data_api_keys set last_used_at = ? where key_hash = ?").bind(nowIso, keyHash).run();
    },

    async incrementWindow(keyHash, windowName, windowStart, limit, nowIso) {
      await ensureApiAuthSchema(db);
      const existing = await db
        .prepare(
          "select count from data_api_rate_limits where key_hash = ? and window_name = ? and window_start = ?"
        )
        .bind(keyHash, windowName, windowStart)
        .first();
      const count = Number(existing?.count ?? 0);
      if (count >= limit) {
        return { ok: false, count, limit };
      }
      if (existing) {
        await db
          .prepare(
            `update data_api_rate_limits
             set count = count + 1, updated_at = ?
             where key_hash = ? and window_name = ? and window_start = ?`
          )
          .bind(nowIso, keyHash, windowName, windowStart)
          .run();
      } else {
        await db
          .prepare(
            `insert into data_api_rate_limits (key_hash, window_name, window_start, count, updated_at)
             values (?, ?, ?, 1, ?)`
          )
          .bind(keyHash, windowName, windowStart, nowIso)
          .run();
      }
      return { ok: true, count: count + 1, limit };
    }
  };
}

export function createMemoryApiAuthRepository(keys = []) {
  const keysByHash = new Map(keys.map((key) => [key.key_hash, { status: "active", scopes: "read:v1", ...key }]));
  const windows = new Map();
  return {
    keysByHash,
    windows,
    async findKeyByHash(keyHash) {
      const key = keysByHash.get(keyHash);
      return key?.status === "active" ? key : null;
    },
    async touchKey(keyHash, nowIso) {
      const key = keysByHash.get(keyHash);
      if (key) keysByHash.set(keyHash, { ...key, last_used_at: nowIso });
    },
    async incrementWindow(keyHash, windowName, windowStart, limit, nowIso) {
      const id = `${keyHash}:${windowName}:${windowStart}`;
      const existing = windows.get(id) ?? { count: 0 };
      if (existing.count >= limit) return { ok: false, count: existing.count, limit };
      windows.set(id, { count: existing.count + 1, updated_at: nowIso });
      return { ok: true, count: existing.count + 1, limit };
    }
  };
}

function bearerToken(request) {
  const header = request.headers.get("authorization") ?? "";
  if (!header.toLowerCase().startsWith("bearer ")) return "";
  return header.slice("bearer ".length).trim();
}

function numericLimit(value, fallback) {
  const parsed = Number(value);
  return Number.isFinite(parsed) && parsed > 0 ? Math.floor(parsed) : fallback;
}

function minuteWindow(now) {
  return now.toISOString().slice(0, 16);
}

function dayWindow(now) {
  return now.toISOString().slice(0, 10);
}

async function authenticateRequest({ request, env, authRepo, now }) {
  if (String(env.API_AUTH_REQUIRED ?? "true").toLowerCase() === "false") {
    return { ok: true, key: { id: "anonymous", key_hash: "anonymous", name: "Anonymous" } };
  }

  const token = bearerToken(request);
  if (!token) {
    return { ok: false, result: errorResult(401, "unauthorized", "Missing bearer API key.") };
  }

  const keyHash = await hashApiKey(token);
  const key = await authRepo.findKeyByHash(keyHash);
  if (!key) {
    return { ok: false, result: errorResult(401, "unauthorized", "Invalid or inactive API key.") };
  }

  const nowIso = now.toISOString();
  const minuteLimit = numericLimit(key.rate_limit_per_minute ?? env.API_RATE_LIMIT_PER_MINUTE, DEFAULT_MINUTE_LIMIT);
  const dayLimit = numericLimit(key.rate_limit_per_day ?? env.API_RATE_LIMIT_PER_DAY, DEFAULT_DAY_LIMIT);
  const minuteUsage = await authRepo.incrementWindow(keyHash, "minute", minuteWindow(now), minuteLimit, nowIso);
  if (!minuteUsage.ok) {
    return {
      ok: false,
      result: errorResult(
        429,
        "rate_limit_exceeded",
        "Per-minute API rate limit exceeded.",
        { limit: minuteLimit, window: "minute" },
        { "retry-after": "60" }
      )
    };
  }
  const dayUsage = await authRepo.incrementWindow(keyHash, "day", dayWindow(now), dayLimit, nowIso);
  if (!dayUsage.ok) {
    return {
      ok: false,
      result: errorResult(
        429,
        "rate_limit_exceeded",
        "Daily API rate limit exceeded.",
        { limit: dayLimit, window: "day" },
        { "retry-after": "3600" }
      )
    };
  }
  await authRepo.touchKey(keyHash, nowIso);
  return { ok: true, key };
}

function parsePath(request) {
  const pathname = new URL(request.url).pathname.replace(/\/+$/g, "");
  const cleaned = pathname || "/";
  for (const prefix of ["/api/v1", "/v1"]) {
    if (cleaned === prefix) return [];
    if (cleaned.startsWith(`${prefix}/`)) return cleaned.slice(prefix.length + 1).split("/").filter(Boolean);
  }
  return cleaned.split("/").filter(Boolean);
}

function normalizedTrack(url) {
  const value = String(url.searchParams.get("track") || "all").toLowerCase();
  return VALID_TRACKS.has(value) ? value : null;
}

function normalizedScope(url) {
  const value = String(url.searchParams.get("scope") || "active").toLowerCase();
  return VALID_SCOPES.has(value) ? value : null;
}

function normalizedGroupBy(url) {
  const value = String(url.searchParams.get("group_by") || "asset").toLowerCase();
  return VALID_GROUPS.has(value) ? value : null;
}

function limitAndCursor(url) {
  const limit = Math.min(250, Math.max(1, numericLimit(url.searchParams.get("limit"), 100)));
  const cursor = Math.max(0, Number.parseInt(url.searchParams.get("cursor") || "0", 10) || 0);
  return { limit, cursor };
}

function pageRows(rows, url) {
  const { limit, cursor } = limitAndCursor(url);
  const data = rows.slice(cursor, cursor + limit);
  const nextCursor = cursor + limit < rows.length ? String(cursor + limit) : null;
  return { data, next_cursor: nextCursor };
}

const assetById = new Map(apiReadModel.assets.map((asset) => [asset.option_id, asset]));
const modelById = new Map(apiReadModel.models.map((model) => [model.model_id, model]));
const styleByModelId = new Map(apiReadModel.model_styles.map((style) => [style.model_id, style]));
const CATEGORY_LABEL_OVERRIDES = new Map([
  ["ai_and_technology", "AI and Technology"],
  ["cash", "Cash"],
  ["cash_and_short_duration", "Cash and Short Duration"],
  ["country_equity", "Country Equity"],
  ["us_broad_market", "US Broad Market"],
  ["us_factor_equity", "US Factor Equity"],
  ["us_growth_and_technology", "US Growth and Technology"],
  ["us_sector", "US Sector"]
]);

function readableCategory(category) {
  const normalized = category || "unknown";
  if (CATEGORY_LABEL_OVERRIDES.has(normalized)) return CATEGORY_LABEL_OVERRIDES.get(normalized);
  return normalized
    .split("_")
    .filter(Boolean)
    .map((part) => part.charAt(0).toUpperCase() + part.slice(1))
    .join(" ");
}

function enrichedModel(model) {
  if (!model) return null;
  return {
    ...model,
    style: styleByModelId.get(model.model_id) ?? null
  };
}

function enrichedAsset(asset) {
  if (!asset) return null;
  return asset;
}

function portfolioKey(row) {
  return `${row.round_id}:${row.run_id}:${row.model_id}`;
}

function filterByTrack(rows, track) {
  return track === "all" ? rows : rows.filter((row) => row.track === track);
}

function filterByScope(rows, scope) {
  return scope === "active" ? rows.filter((row) => row.status === "active") : rows;
}

function filterByRoundStatus(rounds, status) {
  if (status === "all") return rounds;
  if (status === "active") return rounds.filter((round) => round.status === "active");
  return rounds.filter((round) => round.status === status);
}

function average(values) {
  const finite = values.filter((value) => typeof value === "number" && Number.isFinite(value));
  return finite.length ? finite.reduce((total, value) => total + value, 0) / finite.length : null;
}

function positioningKey(row, groupBy) {
  if (groupBy === "model") {
    const model = modelById.get(row.model_id);
    return {
      key: row.model_id,
      label: model?.label ?? row.model_id,
      ticker: null,
      category: model?.provider_label ?? row.provider
    };
  }
  if (groupBy === "category") {
    const asset = assetById.get(row.option_id);
    const category = asset?.category ?? row.category ?? "unknown";
    return { key: category, label: category.replaceAll("_", " "), ticker: null, category };
  }
  const asset = assetById.get(row.option_id);
  return {
    key: row.option_id,
    label: asset?.label ?? row.label ?? row.option_id,
    ticker: asset?.ticker ?? row.ticker ?? null,
    category: asset?.category ?? row.category ?? "unknown"
  };
}

function aggregatePositioning(rows, groupBy, scope, track) {
  const portfolioKeys = new Set(rows.map(portfolioKey));
  const denominator = Math.max(1, portfolioKeys.size);
  const groups = new Map();
  for (const row of rows) {
    const meta = positioningKey(row, groupBy);
    const existing =
      groups.get(meta.key) ??
      {
        key: meta.key,
        label: meta.label,
        ticker: meta.ticker,
        category: meta.category,
        allocation_pct: 0,
        modelIds: new Set(),
        roundIds: new Set(),
        tracks: new Set(),
        modelWeights: new Map()
      };
    existing.allocation_pct += row.allocation_pct / denominator;
    existing.modelIds.add(row.model_id);
    existing.roundIds.add(row.round_id);
    existing.tracks.add(row.track);
    const model = modelById.get(row.model_id);
    const modelWeight =
      existing.modelWeights.get(row.model_id) ??
      {
        model_id: row.model_id,
        label: model?.label ?? row.model_id,
        allocation_pct: 0
      };
    modelWeight.allocation_pct += row.allocation_pct / denominator;
    existing.modelWeights.set(row.model_id, modelWeight);
    groups.set(meta.key, existing);
  }
  return {
    as_of: apiReadModel.generated_at,
    scope,
    track,
    group_by: groupBy,
    portfolio_count: portfolioKeys.size,
    data: Array.from(groups.values())
      .map((row) => ({
        key: row.key,
        label: row.label,
        ticker: row.ticker,
        category: row.category,
        allocation_pct: row.allocation_pct,
        model_count: row.modelIds.size,
        round_count: row.roundIds.size,
        tracks: Array.from(row.tracks).sort(),
        models: Array.from(row.modelWeights.values()).sort((a, b) => b.allocation_pct - a.allocation_pct)
      }))
      .sort((a, b) => b.allocation_pct - a.allocation_pct || a.label.localeCompare(b.label))
  };
}

function positioningResponse(url, options = {}) {
  const track = options.track ?? normalizedTrack(url);
  const scope = options.scope ?? normalizedScope(url);
  const groupBy = options.groupBy ?? normalizedGroupBy(url);
  if (!track) return errorResult(400, "invalid_track", "track must be weekly, monthly, or all.");
  if (!scope) return errorResult(400, "invalid_scope", "scope must be active or cumulative.");
  if (!groupBy) return errorResult(400, "invalid_group_by", "group_by must be asset, category, or model.");
  const modelId = options.modelId ?? url.searchParams.get("model_id");
  const optionId = options.optionId ?? null;
  if (modelId && !modelById.has(modelId)) return errorResult(404, "not_found", "Model not found.");
  if (optionId && !assetById.has(optionId)) return errorResult(404, "not_found", "Asset not found.");
  let rows = filterByScope(filterByTrack(apiReadModel.allocations, track), scope);
  if (modelId) rows = rows.filter((row) => row.model_id === modelId);
  if (optionId) rows = rows.filter((row) => row.option_id === optionId);
  if (options.category) rows = rows.filter((row) => (assetById.get(row.option_id)?.category ?? row.category) === options.category);
  return jsonApiResult(200, aggregatePositioning(rows, groupBy, scope, track));
}

function positioningChanges(url) {
  const track = normalizedTrack(url);
  if (!track) return errorResult(400, "invalid_track", "track must be weekly, monthly, or all.");
  const window = String(url.searchParams.get("window") || "latest").toLowerCase();
  if (window !== "latest") return errorResult(400, "invalid_window", "window must be latest.");
  const groupBy = normalizedGroupBy(url) ?? "asset";
  const rounds = filterByTrack(apiReadModel.rounds, track)
    .filter((round) => apiReadModel.allocations.some((allocation) => allocation.round_id === round.round_id))
    .sort((a, b) => b.decision_deadline_utc.localeCompare(a.decision_deadline_utc));
  const [currentRound, priorRound] = rounds;
  if (!currentRound || !priorRound) {
    return jsonApiResult(200, {
      as_of: apiReadModel.generated_at,
      window,
      data: []
    });
  }
  const current = aggregatePositioning(
    apiReadModel.allocations.filter((row) => row.round_id === currentRound.round_id),
    groupBy,
    "cumulative",
    track
  );
  const prior = aggregatePositioning(
    apiReadModel.allocations.filter((row) => row.round_id === priorRound.round_id),
    groupBy,
    "cumulative",
    track
  );
  const priorByKey = new Map(prior.data.map((row) => [row.key, row]));
  return jsonApiResult(200, {
    as_of: apiReadModel.generated_at,
    window,
    current_round_id: currentRound.round_id,
    prior_round_id: priorRound.round_id,
    group_by: groupBy,
    data: current.data
      .map((row) => {
        const priorRow = priorByKey.get(row.key);
        const priorAllocation = priorRow?.allocation_pct ?? 0;
        return {
          key: row.key,
          label: row.label,
          allocation_pct: row.allocation_pct,
          prior_allocation_pct: priorAllocation,
          change_pp: row.allocation_pct - priorAllocation
        };
      })
      .sort((a, b) => Math.abs(b.change_pp) - Math.abs(a.change_pp))
  });
}

function latestResolvedRound(track) {
  return filterByTrack(apiReadModel.rounds, track)
    .filter((round) => round.status === "resolved")
    .sort((a, b) => b.exit_date.localeCompare(a.exit_date) || b.round_id.localeCompare(a.round_id))[0];
}

function leaderboardRowsForRound(round) {
  if (!round) return [];
  return apiReadModel.results
    .filter((row) => row.round_id === round.round_id)
    .sort((a, b) => a.rank - b.rank)
    .map((row) => ({
      ...row,
      label: modelById.get(row.model_id)?.label ?? row.model_id
    }));
}

function latestLeaderboard(url) {
  const track = normalizedTrack(url);
  if (!track) return errorResult(400, "invalid_track", "track must be weekly, monthly, or all.");
  if (track === "all") return errorResult(400, "invalid_track", "leaderboards require track weekly or monthly.");
  const round = latestResolvedRound(track);
  return jsonApiResult(200, {
    track,
    round_id: round?.round_id ?? null,
    benchmark_option_id: round?.benchmark_option_id ?? "SP500",
    data: leaderboardRowsForRound(round)
  });
}

function resultRoundSortValue(round) {
  return `${round?.exit_date ?? ""}:${round?.decision_deadline_utc ?? ""}:${round?.round_id ?? ""}`;
}

function resolvedResultSet(readModel, track) {
  const rows = track === "all" ? readModel.results : readModel.results.filter((row) => row.track === track);
  const roundById = new Map(readModel.rounds.map((round) => [round.round_id, round]));
  const byRound = new Map();
  for (const row of rows) {
    const existing = byRound.get(row.round_id) ?? [];
    existing.push(row);
    byRound.set(row.round_id, existing);
  }
  const scoredRoundIds = Array.from(byRound.keys()).sort((left, right) =>
    resultRoundSortValue(roundById.get(left)).localeCompare(resultRoundSortValue(roundById.get(right)))
  );
  const modelIds = new Set(rows.map((row) => row.model_id).filter(Boolean));
  return {
    rows,
    completedRoundIds: scoredRoundIds,
    comparisonRoundIds: scoredRoundIds,
    excludedRoundIds: [],
    comparisonModelCount: modelIds.size
  };
}

export function buildCumulativeLeaderboardData(readModel, track) {
  const cohort = resolvedResultSet(readModel, track);
  const byModel = new Map();
  const localModelById = new Map(readModel.models.map((model) => [model.model_id, model]));
  for (const row of cohort.rows) {
    const existing =
      byModel.get(row.model_id) ??
      {
        model_id: row.model_id,
        label: localModelById.get(row.model_id)?.label ?? row.model_id,
        portfolio_return_values: [],
        benchmark_return_values: [],
        alpha_values: [],
        max_possible_return_values: [],
        capitalbench_score_values: [],
        wins: 0,
        positive_alpha: 0,
        round_count: 0
      };
    if (typeof row.portfolio_return_pct === "number") existing.portfolio_return_values.push(row.portfolio_return_pct);
    if (typeof row.benchmark_return_pct === "number") existing.benchmark_return_values.push(row.benchmark_return_pct);
    if (typeof row.max_possible_return_pct === "number") existing.max_possible_return_values.push(row.max_possible_return_pct);
    if (typeof row.capitalbench_score === "number") existing.capitalbench_score_values.push(row.capitalbench_score);
    if (typeof row.alpha_pp === "number") {
      existing.alpha_values.push(row.alpha_pp);
      if (row.alpha_pp > 0) existing.positive_alpha += 1;
    }
    if (row.rank === 1) existing.wins += 1;
    existing.round_count += 1;
    byModel.set(row.model_id, existing);
  }

  const testsRequired = cohort.comparisonRoundIds.length;
  const data = Array.from(byModel.values())
    .map((row) => {
      const isRankEligible = testsRequired > 0 && row.round_count === testsRequired;
      return {
        model_id: row.model_id,
        label: row.label,
        portfolio_return_pct: average(row.portfolio_return_values),
        benchmark_return_pct: average(row.benchmark_return_values),
        alpha_pp: average(row.alpha_values),
        max_possible_return_pct: average(row.max_possible_return_values),
        capitalbench_score: average(row.capitalbench_score_values),
        round_count: row.round_count,
        tests_required: testsRequired,
        tests_included: row.round_count,
        is_rank_eligible: isRankEligible,
        sample_status: isRankEligible ? "eligible" : "provisional",
        wins: row.wins,
        win_rate_pct: row.round_count ? (row.wins / row.round_count) * 100 : null,
        positive_alpha_rate_pct: row.round_count ? (row.positive_alpha / row.round_count) * 100 : null
      };
    })
    .sort((a, b) =>
      Number(b.is_rank_eligible) - Number(a.is_rank_eligible) ||
      Number(b.capitalbench_score ?? -Infinity) - Number(a.capitalbench_score ?? -Infinity) ||
      Number(b.alpha_pp ?? -Infinity) - Number(a.alpha_pp ?? -Infinity)
    )
    .map((row, index) => ({ rank: index + 1, ...row }));

  return {
    track,
    comparison: {
      mode: "all_resolved_rounds",
      completed_round_count: cohort.completedRoundIds.length,
      completed_round_ids: cohort.completedRoundIds,
      comparison_round_count: testsRequired,
      comparison_round_ids: cohort.comparisonRoundIds,
      excluded_round_ids: cohort.excludedRoundIds,
      comparison_model_count: cohort.comparisonModelCount,
      is_early_cohort: testsRequired === 1
    },
    data
  };
}

function isUsableLiveRow(row) {
  return (
    row.status === "active" &&
    row.published !== false &&
    Number(row.days_elapsed ?? 0) > 0 &&
    row.target_date > row.entry_date &&
    row.target_date < row.exit_date &&
    typeof row.model_return_pct === "number" &&
    typeof row.sp500_return_pct === "number" &&
    typeof row.alpha_pp === "number"
  );
}

function latestLiveSnapshots({ track = "all", roundId = null, modelId = null } = {}) {
  const latestByKey = new Map();
  for (const row of apiReadModel.interim_performance ?? []) {
    if (track !== "all" && row.track !== track) continue;
    if (roundId && row.round_id !== roundId) continue;
    if (modelId && row.model_id !== modelId) continue;
    if (!isUsableLiveRow(row)) continue;
    const key = `${row.round_id}:${row.run_id}:${row.model_id}`;
    const existing = latestByKey.get(key);
    if (!existing || row.target_date > existing.target_date || (row.target_date === existing.target_date && row.price_date > existing.price_date)) {
      latestByKey.set(key, row);
    }
  }
  return Array.from(latestByKey.values()).sort(
    (a, b) => {
      const aLabel = modelById.get(a.model_id)?.label ?? a.model_id;
      const bLabel = modelById.get(b.model_id)?.label ?? b.model_id;
      return b.target_date.localeCompare(a.target_date) || b.round_id.localeCompare(a.round_id) || aLabel.localeCompare(bLabel);
    }
  );
}

function aggregateLivePerformance(rows, track) {
  const byModel = new Map();
  const byRound = new Map();
  for (const row of rows) {
    const model = modelById.get(row.model_id);
    const modelRow =
      byModel.get(row.model_id) ??
      {
        model_id: row.model_id,
        label: model?.label ?? row.model_id,
        provider: row.provider,
        provider_label: model?.provider_label ?? row.provider,
        logo_src: model?.logo_src ?? null,
        portfolio_return_values: [],
        sp500_return_values: [],
        alpha_values: [],
        roundIds: new Set(),
        tracks: new Set(),
        latest_price_date: "",
        rounds: []
      };
    modelRow.portfolio_return_values.push(row.model_return_pct);
    modelRow.sp500_return_values.push(row.sp500_return_pct);
    modelRow.alpha_values.push(row.alpha_pp);
    modelRow.roundIds.add(row.round_id);
    modelRow.tracks.add(row.track);
    modelRow.latest_price_date = row.price_date > modelRow.latest_price_date ? row.price_date : modelRow.latest_price_date;
    modelRow.rounds.push({
      round_id: row.round_id,
      run_id: row.run_id,
      track: row.track,
      target_date: row.target_date,
      price_date: row.price_date,
      days_elapsed: row.days_elapsed,
      entry_date: row.entry_date,
      exit_date: row.exit_date,
      portfolio_return_pct: row.model_return_pct,
      sp500_return_pct: row.sp500_return_pct,
      alpha_pp: row.alpha_pp,
      selected_option_id: row.selected_option_id,
      holding_count: row.holding_count
    });
    byModel.set(row.model_id, modelRow);

    const roundKey = `${row.round_id}:${row.run_id}`;
    const roundRow =
      byRound.get(roundKey) ??
      {
        round_id: row.round_id,
        run_id: row.run_id,
        track: row.track,
        target_date: row.target_date,
        price_date: row.price_date,
        entry_date: row.entry_date,
        exit_date: row.exit_date,
        sp500_return_pct: row.sp500_return_pct,
        model_count: 0
      };
    roundRow.target_date = row.target_date > roundRow.target_date ? row.target_date : roundRow.target_date;
    roundRow.price_date = row.price_date > roundRow.price_date ? row.price_date : roundRow.price_date;
    roundRow.model_count += 1;
    byRound.set(roundKey, roundRow);
  }

  const data = Array.from(byModel.values())
    .map((row) => ({
      model_id: row.model_id,
      label: row.label,
      provider: row.provider,
      provider_label: row.provider_label,
      logo_src: row.logo_src,
      portfolio_return_pct: average(row.portfolio_return_values),
      sp500_return_pct: average(row.sp500_return_values),
      alpha_pp: average(row.alpha_values),
      live_round_count: row.roundIds.size,
      tracks: Array.from(row.tracks).sort(),
      latest_price_date: row.latest_price_date || null,
      rounds: row.rounds.sort((a, b) => b.exit_date.localeCompare(a.exit_date) || b.round_id.localeCompare(a.round_id))
    }))
    .sort(
      (a, b) =>
        Number(b.portfolio_return_pct ?? -Infinity) - Number(a.portfolio_return_pct ?? -Infinity) ||
        Number(b.alpha_pp ?? -Infinity) - Number(a.alpha_pp ?? -Infinity) ||
        a.label.localeCompare(b.label)
    )
    .map((row, index) => ({ rank: index + 1, ...row }));

  const roundRows = Array.from(byRound.values()).sort((a, b) => b.exit_date.localeCompare(a.exit_date) || b.round_id.localeCompare(a.round_id));
  return {
    as_of: apiReadModel.generated_at,
    track,
    status: "live_not_final",
    latest_price_date: rows.reduce((latest, row) => (row.price_date > latest ? row.price_date : latest), "") || null,
    round_count: roundRows.length,
    model_count: data.length,
    snapshot_count: rows.length,
    benchmark: {
      label: "S&P 500",
      return_pct: average(roundRows.map((row) => row.sp500_return_pct)),
      round_count: roundRows.length
    },
    data,
    rounds: roundRows
  };
}

function livePerformance(url, options = {}) {
  const track = options.track ?? normalizedTrack(url);
  if (!track) return errorResult(400, "invalid_track", "track must be weekly, monthly, or all.");
  const rows = latestLiveSnapshots({ track, roundId: options.roundId ?? null, modelId: options.modelId ?? null });
  return jsonApiResult(200, aggregateLivePerformance(rows, track));
}

function roundLivePerformance(roundId) {
  const round = apiReadModel.rounds.find((item) => item.round_id === roundId);
  if (!round) return errorResult(404, "not_found", "Round not found.");
  const rows = latestLiveSnapshots({ track: "all", roundId });
  const history = (apiReadModel.interim_performance ?? [])
    .filter((row) => row.round_id === roundId)
    .sort((a, b) => a.target_date.localeCompare(b.target_date) || a.model_id.localeCompare(b.model_id));
  return jsonApiResult(200, {
    round_id: roundId,
    ...aggregateLivePerformance(rows, round.track),
    history
  });
}

function modelLivePerformance(modelId, url) {
  if (!modelById.has(modelId)) return errorResult(404, "not_found", "Model not found.");
  const track = normalizedTrack(url);
  if (!track) return errorResult(400, "invalid_track", "track must be weekly, monthly, or all.");
  const rows = latestLiveSnapshots({ track, modelId });
  return jsonApiResult(200, {
    model_id: modelId,
    ...aggregateLivePerformance(rows, track)
  });
}

function cumulativeLeaderboard(url) {
  const track = normalizedTrack(url);
  if (!track) return errorResult(400, "invalid_track", "track must be weekly, monthly, or all.");
  if (track === "all") return errorResult(400, "invalid_track", "leaderboards require track weekly or monthly.");
  return jsonApiResult(200, buildCumulativeLeaderboardData(apiReadModel, track));
}

function listRounds(url) {
  const track = normalizedTrack(url);
  if (!track) return errorResult(400, "invalid_track", "track must be weekly, monthly, or all.");
  const status = String(url.searchParams.get("status") || "all").toLowerCase();
  if (!["active", "resolved", "all"].includes(status)) {
    return errorResult(400, "invalid_status", "status must be active, resolved, or all.");
  }
  const rows = filterByRoundStatus(filterByTrack(apiReadModel.rounds, track), status);
  return jsonApiResult(200, pageRows(rows, url));
}

function roundDetails(roundId) {
  const round = apiReadModel.rounds.find((item) => item.round_id === roundId);
  if (!round) return errorResult(404, "not_found", "Round not found.");
  return jsonApiResult(200, round);
}

function roundPortfolios(roundId) {
  const round = apiReadModel.rounds.find((item) => item.round_id === roundId);
  if (!round) return errorResult(404, "not_found", "Round not found.");
  return jsonApiResult(200, {
    round_id: roundId,
    data: apiReadModel.portfolios.filter((row) => row.round_id === roundId)
  });
}

function roundConcentration(roundId) {
  const round = apiReadModel.rounds.find((item) => item.round_id === roundId);
  if (!round) return errorResult(404, "not_found", "Round not found.");

  const rows = apiReadModel.allocations.filter(
    (row) => row.round_id === roundId && (!round.official_run_id || row.run_id === round.official_run_id)
  );
  const portfolioKeys = new Set(rows.map(portfolioKey));
  const denominator = Math.max(1, portfolioKeys.size);
  const byAsset = new Map();

  for (const row of rows) {
    const asset = assetById.get(row.option_id);
    const category = asset?.category ?? row.category ?? "unknown";
    const existing =
      byAsset.get(row.option_id) ??
      {
        option_id: row.option_id,
        label: asset?.label ?? row.label ?? row.option_id,
        ticker: asset?.ticker ?? row.ticker ?? null,
        category,
        allocation_pct: 0,
        models: new Map()
      };
    existing.allocation_pct += row.allocation_pct / denominator;

    const model = modelById.get(row.model_id);
    const modelWeight =
      existing.models.get(row.model_id) ??
      {
        model_id: row.model_id,
        label: model?.label ?? row.model_id,
        provider: model?.provider ?? row.provider ?? null,
        allocation_pct: 0
      };
    modelWeight.allocation_pct += row.allocation_pct / denominator;
    existing.models.set(row.model_id, modelWeight);
    byAsset.set(row.option_id, existing);
  }

  const assets = Array.from(byAsset.values())
    .map((row) => ({
      option_id: row.option_id,
      label: row.label,
      ticker: row.ticker,
      category: row.category,
      allocation_pct: row.allocation_pct,
      model_count: row.models.size,
      models: Array.from(row.models.values()).sort((a, b) => b.allocation_pct - a.allocation_pct || a.label.localeCompare(b.label))
    }))
    .sort((a, b) => b.allocation_pct - a.allocation_pct || a.label.localeCompare(b.label));

  const byCategory = new Map();
  for (const asset of assets) {
    const existing =
      byCategory.get(asset.category) ??
      {
        key: asset.category,
        label: readableCategory(asset.category),
        allocation_pct: 0,
        asset_count: 0
      };
    existing.allocation_pct += asset.allocation_pct;
    existing.asset_count += 1;
    byCategory.set(asset.category, existing);
  }

  const concentrationScore = assets.reduce((total, asset) => total + (asset.allocation_pct / 100) ** 2, 0);
  return jsonApiResult(200, {
    as_of: apiReadModel.generated_at,
    round_id: roundId,
    run_id: round.official_run_id ?? null,
    track: round.track,
    status: round.status,
    model_count: portfolioKeys.size,
    portfolio_count: portfolioKeys.size,
    summary: {
      top_asset_share_pct: assets[0]?.allocation_pct ?? 0,
      top_three_share_pct: assets.slice(0, 3).reduce((total, asset) => total + asset.allocation_pct, 0),
      effective_asset_count: concentrationScore > 0 ? 1 / concentrationScore : 0
    },
    assets,
    categories: Array.from(byCategory.values()).sort((a, b) => b.allocation_pct - a.allocation_pct || a.label.localeCompare(b.label))
  });
}

function roundResults(roundId) {
  const round = apiReadModel.rounds.find((item) => item.round_id === roundId);
  if (!round) return errorResult(404, "not_found", "Round not found.");
  const data = leaderboardRowsForRound(round);
  const benchmarkReturn = apiReadModel.returns.find((row) => row.round_id === roundId && row.is_benchmark)?.return_pct ?? null;
  return jsonApiResult(200, {
    round_id: roundId,
    benchmark_option_id: round.benchmark_option_id,
    benchmark_return_pct: benchmarkReturn,
    data,
    asset_returns: apiReadModel.returns.filter((row) => row.round_id === roundId).sort((a, b) => Number(a.rank ?? 9999) - Number(b.rank ?? 9999))
  });
}

function listModels() {
  return jsonApiResult(200, { data: apiReadModel.models.map(enrichedModel) });
}

function modelDetails(modelId) {
  const model = enrichedModel(modelById.get(modelId));
  if (!model) return errorResult(404, "not_found", "Model not found.");
  return jsonApiResult(200, model);
}

function modelHoldings(modelId, url) {
  if (!modelById.has(modelId)) return errorResult(404, "not_found", "Model not found.");
  const track = normalizedTrack(url);
  const scope = normalizedScope(url);
  if (!track) return errorResult(400, "invalid_track", "track must be weekly, monthly, or all.");
  if (!scope) return errorResult(400, "invalid_scope", "scope must be active or cumulative.");
  const rows = filterByScope(filterByTrack(apiReadModel.allocations, track), scope).filter((row) => row.model_id === modelId);
  return jsonApiResult(200, {
    model_id: modelId,
    track,
    scope,
    data: rows
  });
}

function modelStyle(modelId) {
  if (!modelById.has(modelId)) return errorResult(404, "not_found", "Model not found.");
  return jsonApiResult(200, styleByModelId.get(modelId) ?? { model_id: modelId, risk_appetite_score: null, sample_round_count: 0 });
}

function currentUniverse() {
  return jsonApiResult(200, {
    universe_version: apiReadModel.rounds.find((round) => round.round_id === apiReadModel.current_universe_round_id)?.universe_version ?? null,
    round_id: apiReadModel.current_universe_round_id,
    data: apiReadModel.assets.filter((asset) => asset.in_current_universe)
  });
}

function riskAppetite() {
  return jsonApiResult(200, apiReadModel.risk_appetite);
}

function assetDetails(optionId) {
  const asset = enrichedAsset(assetById.get(optionId));
  if (!asset) return errorResult(404, "not_found", "Asset not found.");
  return jsonApiResult(200, asset);
}

function indexResponse() {
  return jsonApiResult(200, {
    name: "CapitalBench Data API",
    version: API_VERSION,
    generated_at: apiReadModel.generated_at,
    endpoints: [
      "/v1/positioning/active",
      "/v1/positioning/cumulative",
      "/v1/positioning/consensus",
      "/v1/positioning/by-model/{model_id}",
      "/v1/positioning/by-asset/{option_id}",
      "/v1/positioning/by-category",
      "/v1/positioning/changes",
      "/v1/risk-appetite",
      "/v1/live/performance",
      "/v1/rounds",
      "/v1/rounds/{round_id}",
      "/v1/rounds/{round_id}/portfolios",
      "/v1/rounds/{round_id}/concentration",
      "/v1/rounds/{round_id}/live-performance",
      "/v1/rounds/{round_id}/results",
      "/v1/leaderboards/latest",
      "/v1/leaderboards/cumulative",
      "/v1/models",
      "/v1/models/{model_id}",
      "/v1/models/{model_id}/holdings",
      "/v1/models/{model_id}/live-performance",
      "/v1/models/{model_id}/style",
      "/v1/universe/current",
      "/v1/assets/{option_id}",
      "/v1/assets/{option_id}/model-holders"
    ]
  });
}

function routeGet(request) {
  const url = new URL(request.url);
  const parts = parsePath(request).map(decodeURIComponent);
  if (parts.length === 0) return indexResponse();

  if (parts[0] === "positioning") {
    if (parts[1] === "active") return positioningResponse(url, { scope: "active" });
    if (parts[1] === "cumulative") return positioningResponse(url, { scope: "cumulative" });
    if (parts[1] === "consensus") return positioningResponse(url, { scope: normalizedScope(url), groupBy: "asset" });
    if (parts[1] === "changes") return positioningChanges(url);
    if (parts[1] === "by-model" && parts[2]) return positioningResponse(url, { modelId: parts[2], groupBy: normalizedGroupBy(url) ?? "asset" });
    if (parts[1] === "by-asset" && parts[2]) return positioningResponse(url, { optionId: parts[2], groupBy: "model" });
    if (parts[1] === "by-category") return positioningResponse(url, { groupBy: "category" });
  }

  if (parts[0] === "live" && parts[1] === "performance") return livePerformance(url);
  if (parts[0] === "risk-appetite" && parts.length === 1) return riskAppetite();

  if (parts[0] === "rounds") {
    if (parts.length === 1) return listRounds(url);
    if (parts.length === 2) return roundDetails(parts[1]);
    if (parts.length === 3 && parts[2] === "portfolios") return roundPortfolios(parts[1]);
    if (parts.length === 3 && parts[2] === "concentration") return roundConcentration(parts[1]);
    if (parts.length === 3 && parts[2] === "live-performance") return roundLivePerformance(parts[1]);
    if (parts.length === 3 && parts[2] === "results") return roundResults(parts[1]);
  }

  if (parts[0] === "leaderboards") {
    if (parts[1] === "latest") return latestLeaderboard(url);
    if (parts[1] === "cumulative") return cumulativeLeaderboard(url);
  }

  if (parts[0] === "models") {
    if (parts.length === 1) return listModels();
    if (parts.length === 2) return modelDetails(parts[1]);
    if (parts.length === 3 && parts[2] === "holdings") return modelHoldings(parts[1], url);
    if (parts.length === 3 && parts[2] === "live-performance") return modelLivePerformance(parts[1], url);
    if (parts.length === 3 && parts[2] === "style") return modelStyle(parts[1]);
  }

  if (parts[0] === "universe" && parts[1] === "current") return currentUniverse();

  if (parts[0] === "assets") {
    if (parts.length === 2) return assetDetails(parts[1]);
    if (parts.length === 3 && parts[2] === "model-holders") return positioningResponse(url, { optionId: parts[1], groupBy: "model" });
  }

  return errorResult(404, "not_found", "API endpoint not found.");
}

export async function handleDataApiRequest({ request, env, authRepo, now = new Date() }) {
  if (request.method === "OPTIONS") return jsonApiResult(204, {});
  if (request.method !== "GET") {
    return errorResult(405, "method_not_allowed", "Only GET requests are supported.", {}, { allow: "GET, OPTIONS" });
  }

  const auth = await authenticateRequest({ request, env, authRepo, now });
  if (!auth.ok) return auth.result;
  return routeGet(request);
}
