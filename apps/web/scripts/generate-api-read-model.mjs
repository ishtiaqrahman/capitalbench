import { existsSync, mkdirSync, readdirSync, readFileSync, writeFileSync } from "node:fs";
import { join, resolve } from "node:path";
import { parse as parseYaml } from "yaml";
import {
  buildRiskAppetiteSnapshot,
  historicalRiskLabel
} from "../src/lib/riskAppetiteCore.js";
import { capitalBenchScore } from "../src/lib/capitalBenchScore.js";

const repoRoot = resolve(process.cwd(), "../..");
const roundsRoot = join(repoRoot, "rounds");
const insightsRoot = join(repoRoot, "insights");
const outputPath = join(process.cwd(), "src", "generated", "apiReadModel.js");
const buildDate = new Date().toISOString().slice(0, 10);

const PROVIDER_LABELS = {
  anthropic: "Anthropic",
  google: "Google",
  openai: "OpenAI",
  xai: "xAI"
};

const MODEL_LABELS = {
  "anthropic-claude-fable-5": "Claude Fable 5",
  "anthropic-claude-opus-4-7": "Claude Opus 4.7",
  "anthropic-claude-opus-4-8": "Claude Opus 4.8",
  "google-gemini-3-1-pro": "Gemini 3.1 Pro",
  "openai-gpt-5-5": "GPT-5.5",
  "xai-grok-4-3": "Grok 4.3"
};

const PROVIDER_LOGOS = {
  anthropic: "/labs/icons/claude-icon.svg",
  google: "/labs/icons/gemini-icon.svg",
  openai: "/labs/icons/openai-icon.svg",
  xai: "/labs/icons/xai-icon.svg"
};

function readText(path) {
  if (!existsSync(path)) return "";
  return readFileSync(path, "utf8").trim();
}

function readJson(path, fallback = null) {
  if (!existsSync(path)) return fallback;
  try {
    return JSON.parse(readFileSync(path, "utf8"));
  } catch {
    return fallback;
  }
}

function readYaml(path, fallback = null) {
  if (!existsSync(path)) return fallback;
  try {
    return parseYaml(readFileSync(path, "utf8"));
  } catch {
    return fallback;
  }
}

function loadLatestInsights() {
  const payload = readJson(join(insightsRoot, "latest.json"), null);
  if (!payload || !Array.isArray(payload.insights)) {
    return {
      status: "unavailable",
      engine_version: null,
      generated_at: null,
      data_as_of: null,
      insight_count: 0,
      insights: []
    };
  }
  return payload;
}

const assetRiskModel = readYaml(join(repoRoot, "configs", "asset_risk_model.yaml"), {});
const assetRiskDefinitions = assetRiskModel.assets ?? {};
const benchmarkSetConfig = readYaml(join(repoRoot, "benchmark_sets.yaml"), {
  version: "benchmark_sets_v1",
  qualification_thresholds: { weekly: 6, monthly: 3 },
  sets: []
});
const MONTH_LABELS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];

function normalizeModelIds(modelIds) {
  return Array.from(new Set(modelIds.map(String).filter(Boolean))).sort();
}

function rosterContains(definition, modelIds) {
  const definitionIds = new Set(definition.model_ids ?? []);
  return modelIds.every((modelId) => definitionIds.has(modelId));
}

function roundSortValue(round) {
  return `${round?.exit_date ?? ""}:${round?.decision_deadline_utc ?? ""}:${round?.round_id ?? ""}`;
}

function definitionStartsAtOrBeforeRound(definition, roundById, round) {
  const startRound = roundById.get(definition.started_round_id);
  if (!startRound) return false;
  if (startRound.track !== round.track) return false;
  return roundSortValue(startRound) <= roundSortValue(round);
}

function trackLabel(track) {
  return track === "weekly" ? "Weekly" : "Monthly";
}

function shortMonthDay(dateString) {
  const match = /^(\d{4})-(\d{2})-(\d{2})/.exec(String(dateString ?? ""));
  if (!match) return String(dateString ?? "Unknown date");
  const monthIndex = Number(match[2]) - 1;
  return `${MONTH_LABELS[monthIndex] ?? match[2]} ${Number(match[3])}`;
}

function dateIdForRound(round) {
  const decisionMatch = /^(\d{4}-\d{2}-\d{2})/.exec(String(round?.decision_date ?? ""));
  if (decisionMatch) return decisionMatch[1];
  const roundMatch = /^CB-(\d{4})-(\d{2})-(\d{2})/.exec(String(round?.round_id ?? ""));
  if (roundMatch) return `${roundMatch[1]}-${roundMatch[2]}-${roundMatch[3]}`;
  return String(round?.round_id ?? "unknown").toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "");
}

function uniqueSetId(baseId, usedIds) {
  if (!usedIds.has(baseId)) return baseId;
  let suffix = 2;
  while (usedIds.has(`${baseId}-${suffix}`)) suffix += 1;
  return `${baseId}-${suffix}`;
}

function configuredBenchmarkSetDefinitions() {
  return Array.isArray(benchmarkSetConfig.sets)
    ? benchmarkSetConfig.sets
        .map((set) => ({
          set_id: String(set.set_id ?? ""),
          track: String(set.track ?? ""),
          label: String(set.label ?? set.set_id ?? ""),
          short_label: String(set.short_label ?? set.label ?? set.set_id ?? ""),
          description: String(set.description ?? ""),
          started_round_id: String(set.started_round_id ?? ""),
          model_ids: normalizeModelIds(Array.isArray(set.model_ids) ? set.model_ids : [])
        }))
        .filter((set) => set.set_id && ["weekly", "monthly"].includes(set.track) && set.model_ids.length > 0)
    : [];
}

function autoBenchmarkSetDescription(round, modelIds) {
  return `${trackLabel(round.track)} comparison set automatically opened when the ${shortMonthDay(round.decision_date)} official roster first required a new equal-run benchmark group across ${modelIds.length} models.`;
}

function buildBenchmarkSetDefinitions({ rounds, portfolios }) {
  const definitions = configuredBenchmarkSetDefinitions();
  const roundById = new Map(rounds.map((round) => [round.round_id, round]));
  const usedIds = new Set(definitions.map((set) => set.set_id));
  const definitionsByTrack = new Map([
    ["weekly", definitions.filter((set) => set.track === "weekly")],
    ["monthly", definitions.filter((set) => set.track === "monthly")]
  ]);

  const chronologicalRounds = [...rounds]
    .filter((round) => ["weekly", "monthly"].includes(round.track) && round.official_run_id)
    .sort((left, right) => roundSortValue(left).localeCompare(roundSortValue(right)));

  for (const round of chronologicalRounds) {
    const modelIds = normalizeModelIds(
      portfolios
        .filter((portfolio) => portfolio.round_id === round.round_id && portfolio.run_id === round.official_run_id)
        .map((portfolio) => portfolio.model_id)
    );
    if (modelIds.length === 0) continue;

    const trackDefinitions = definitionsByTrack.get(round.track) ?? [];
    const coveredByStartedSet = trackDefinitions.some(
      (definition) => definitionStartsAtOrBeforeRound(definition, roundById, round) && rosterContains(definition, modelIds)
    );
    if (coveredByStartedSet) continue;

    const baseId = `${round.track}-set-${dateIdForRound(round)}`;
    const setId = uniqueSetId(baseId, usedIds);
    usedIds.add(setId);
    const definition = {
      set_id: setId,
      track: round.track,
      label: `${trackLabel(round.track)} Set: ${shortMonthDay(round.decision_date)}, ${String(round.decision_date).slice(0, 4)}`,
      short_label: `${shortMonthDay(round.decision_date)} ${trackLabel(round.track)}`,
      description: autoBenchmarkSetDescription(round, modelIds),
      started_round_id: round.round_id,
      model_ids: modelIds
    };
    definitions.push(definition);
    trackDefinitions.push(definition);
    definitionsByTrack.set(round.track, trackDefinitions);
  }

  return definitions;
}

function assetRiskDefinition(optionId) {
  const definition = assetRiskDefinitions[optionId];
  if (!definition) throw new Error(`Missing asset-risk definition for ${optionId}`);
  return definition;
}

function inferUniverseVersion(roundPath, manifestVersion) {
  if (manifestVersion) return manifestVersion;
  const optionsText = readText(join(roundPath, "options.yaml"));
  if (!optionsText) return "";
  const universeRoot = join(repoRoot, "configs", "universes");
  if (!existsSync(universeRoot)) return "";
  for (const filename of readdirSync(universeRoot).filter((item) => /^capitalbench_universe_.*\.yaml$/.test(item)).sort().reverse()) {
    if (readText(join(universeRoot, filename)) === optionsText) return filename.replace(/\.yaml$/, "");
  }
  return "";
}

function parseCsvLine(line) {
  const cells = [];
  let cell = "";
  let inQuotes = false;
  for (let index = 0; index < line.length; index += 1) {
    const char = line[index];
    const next = line[index + 1];
    if (char === '"' && inQuotes && next === '"') {
      cell += '"';
      index += 1;
    } else if (char === '"') {
      inQuotes = !inQuotes;
    } else if (char === "," && !inQuotes) {
      cells.push(cell);
      cell = "";
    } else {
      cell += char;
    }
  }
  cells.push(cell);
  return cells;
}

function parseCsv(text) {
  const lines = text.trim().split(/\r?\n/).filter(Boolean);
  if (lines.length === 0) return [];
  const headers = parseCsvLine(lines[0]);
  return lines.slice(1).map((line) => {
    const cells = parseCsvLine(line);
    return Object.fromEntries(headers.map((header, index) => [header, cells[index] ?? ""]));
  });
}

function numberValue(value) {
  if (value === undefined || value === null || value === "") return null;
  const numeric = Number(value);
  return Number.isFinite(numeric) ? numeric : null;
}

function boolValue(value) {
  return String(value ?? "").toLowerCase() === "true";
}

function isBenchmarkOption(optionId, value) {
  return Boolean(value) || String(optionId ?? "").toUpperCase() === "SP500";
}

function percentReturnValue(value) {
  const numeric = numberValue(value);
  return numeric === null ? null : numeric * 100;
}

function maxPossibleReturnPct(roundPath, selectedRun) {
  const rows = parseCsv(readText(join(roundPath, "runs", selectedRun.run_id, "results", "returns.csv")));
  const values = rows.map((row) => percentReturnValue(row.return)).filter((value) => typeof value === "number");
  return values.length ? Math.max(...values) : null;
}

function modelLabel(modelId) {
  if (MODEL_LABELS[modelId]) return MODEL_LABELS[modelId];
  return modelId
    .replace(/^openai-/, "")
    .replace(/^anthropic-/, "")
    .replace(/^google-/, "")
    .replace(/^xai-/, "")
    .split("-")
    .filter(Boolean)
    .map((part) => {
      if (part === "gpt") return "GPT";
      if (/^\d+$/.test(part)) return part;
      return part.length <= 3 ? part.toUpperCase() : part[0].toUpperCase() + part.slice(1);
    })
    .join(" ");
}

function publicOfficialRuns(roundPath) {
  const runsPath = join(roundPath, "runs");
  if (!existsSync(runsPath)) return [];
  return readdirSync(runsPath, { withFileTypes: true })
    .filter((entry) => entry.isDirectory())
    .map((entry) => ({
      run_id: entry.name,
      manifest: readYaml(join(runsPath, entry.name, "run_manifest.yaml"), {})
    }))
    .filter((run) => {
      return (
        run.manifest.run_type === "official" &&
        run.manifest.official_score_eligible === true &&
        Number(run.manifest.invalid_submissions ?? 0) === 0
      );
    })
    .sort((a, b) => {
      if (a.manifest.operator_selected_official && !b.manifest.operator_selected_official) return -1;
      if (!a.manifest.operator_selected_official && b.manifest.operator_selected_official) return 1;
      return a.run_id.localeCompare(b.run_id);
    });
}

function trackFromRound(round) {
  const id = String(round.round_id ?? "").toUpperCase();
  const horizon = String(round.horizon ?? "").toLowerCase();
  if (id.endsWith("-1W") || horizon.includes("week")) return "weekly";
  if (id.endsWith("-1M") || horizon.includes("month")) return "monthly";
  return round.horizon_days && round.horizon_days <= 10 ? "weekly" : "monthly";
}

function horizonDays(entryDate, exitDate) {
  const start = Date.parse(`${entryDate}T00:00:00Z`);
  const end = Date.parse(`${exitDate}T00:00:00Z`);
  if (!Number.isFinite(start) || !Number.isFinite(end)) return null;
  return Math.round((end - start) / 86_400_000);
}

function roundStatus({ hasResults, exitDate }) {
  if (hasResults) return "resolved";
  return exitDate && exitDate < buildDate ? "overdue" : "active";
}

function loadOptions(roundPath, currentOptionIds, roundId) {
  const yaml = readYaml(join(roundPath, "options.yaml"), {});
  const options = Array.isArray(yaml.options) ? yaml.options : [];
  return options
    .filter((option) => option.include_in_universe !== false)
    .map((option, index) => {
      const optionId = String(option.id ?? option.option_id ?? "");
      return {
        option_id: optionId,
        label: String(option.name ?? option.label ?? optionId),
        ticker: String(option.symbol ?? option.asset_symbol ?? ""),
        asset_class: String(option.asset_class ?? "unknown"),
        category: String(option.option_group ?? option.category ?? "unknown"),
        risk_bucket: String(option.risk_bucket ?? "medium"),
        is_cash: Boolean(option.is_cash),
        is_benchmark: isBenchmarkOption(optionId, option.is_benchmark),
        sort_order: index + 1,
        first_seen_round_id: roundId,
        latest_round_id: roundId,
        in_current_universe: currentOptionIds ? currentOptionIds.has(optionId) : false
      };
    })
    .filter((option) => option.option_id);
}

function primaryOptionId(payload) {
  if (payload.selected_option_id) return payload.selected_option_id;
  const allocations = Array.isArray(payload.portfolio) ? payload.portfolio : [];
  const [primary] = [...allocations].sort((a, b) => {
    const aBps = typeof a.allocation_bps === "number" ? a.allocation_bps : Number(a.allocation_pct ?? 0) * 100;
    const bBps = typeof b.allocation_bps === "number" ? b.allocation_bps : Number(b.allocation_pct ?? 0) * 100;
    return bBps - aBps;
  });
  return primary?.option_id ?? "";
}

function decisionAllocations(payload) {
  if (Array.isArray(payload.portfolio) && payload.portfolio.length > 0) {
    return payload.portfolio
      .filter((allocation) => allocation.option_id)
      .map((allocation) => {
        const allocationBps =
          typeof allocation.allocation_bps === "number"
            ? allocation.allocation_bps
            : Number(allocation.allocation_pct ?? 0) * 100;
        return {
          option_id: String(allocation.option_id),
          allocation_bps: allocationBps,
          allocation_pct: allocationBps / 100,
          rationale: allocation.rationale ? String(allocation.rationale) : ""
        };
      });
  }
  if (!payload.selected_option_id) return [];
  return [
    {
      option_id: String(payload.selected_option_id),
      allocation_bps: 10_000,
      allocation_pct: 100,
      rationale: payload.rationale_summary ? String(payload.rationale_summary) : ""
    }
  ];
}

function riskScore(optionId) {
  return Number(assetRiskDefinition(optionId).risk_score_1_5);
}

function riskLabel(score) {
  return historicalRiskLabel(score);
}

function average(values) {
  const finite = values.filter((value) => typeof value === "number" && Number.isFinite(value));
  return finite.length > 0 ? finite.reduce((total, value) => total + value, 0) / finite.length : null;
}

function median(values) {
  const finite = values.filter((value) => typeof value === "number" && Number.isFinite(value)).sort((a, b) => a - b);
  if (finite.length === 0) return null;
  const middle = Math.floor(finite.length / 2);
  return finite.length % 2 ? finite[middle] : (finite[middle - 1] + finite[middle]) / 2;
}

function standardDeviation(values) {
  const finite = values.filter((value) => typeof value === "number" && Number.isFinite(value));
  const mean = average(finite);
  if (mean === null) return null;
  return Math.sqrt(finite.reduce((total, value) => total + (value - mean) ** 2, 0) / finite.length);
}

function isDefensive(optionId) {
  return Boolean(assetRiskDefinition(optionId).defensive);
}

function isTechnology(optionId) {
  return Boolean(assetRiskDefinition(optionId).technology);
}

function isCashDuration(optionId, assetsById) {
  const asset = assetsById.get(optionId);
  const regime = String(assetRiskDefinition(optionId).regime_group ?? "");
  return Boolean(asset?.is_cash) || regime === "liquidity_defensive" || regime === "duration_credit";
}

function isInternational(optionId, assetsById) {
  const asset = assetsById.get(optionId);
  const regime = String(assetRiskDefinition(optionId).regime_group ?? "");
  const category = String(asset?.category ?? "");
  return regime === "international_equity" || category === "country_equity" || category === "international_equity";
}

function isRealAsset(optionId, assetsById) {
  const asset = assetsById.get(optionId);
  const regime = String(assetRiskDefinition(optionId).regime_group ?? "");
  const category = String(asset?.category ?? "");
  return regime === "real_assets_inflation" || category === "commodities" || category === "crypto";
}

function scoreRiskPulse(allocations) {
  const totalPct = allocations.reduce((total, allocation) => total + allocation.allocation_pct, 0);
  if (totalPct <= 0) return { risk_pulse: null, risk_score_1_5: null, risk_on_loading: null };
  let riskOnLoading = 0;
  let riskScore1To5 = 0;
  for (const allocation of allocations) {
    const weight = allocation.allocation_pct / totalPct;
    const definition = assetRiskDefinition(allocation.option_id);
    riskOnLoading += weight * Number(definition.risk_on_loading);
    riskScore1To5 += weight * Number(definition.risk_score_1_5);
  }
  return {
    risk_pulse: 50 + 50 * riskOnLoading,
    risk_score_1_5: riskScore1To5,
    risk_on_loading: riskOnLoading
  };
}

function portfolioKey(row) {
  return `${row.round_id}:${row.run_id}:${row.model_id}`;
}

function roundChronology(roundById, row) {
  const round = roundById.get(row.round_id);
  return `${round?.decision_deadline_utc ?? ""}:${round?.entry_date ?? row.entry_date ?? ""}:${row.round_id}:${row.run_id}`;
}

function scoredBehaviorPortfolios({ portfolios, rounds, assetsById }) {
  const roundById = new Map(rounds.map((round) => [round.round_id, round]));
  return portfolios
    .map((portfolio) => {
      const allocations = (portfolio.allocations ?? [])
        .filter((allocation) => allocation.option_id && typeof allocation.allocation_pct === "number" && allocation.allocation_pct > 0)
        .map((allocation) => ({
          option_id: allocation.option_id,
          label: allocation.label,
          ticker: allocation.ticker,
          category: allocation.category,
          allocation_pct: allocation.allocation_pct
        }));
      const totalPct = allocations.reduce((total, allocation) => total + allocation.allocation_pct, 0);
      if (totalPct <= 0) return null;
      const normalized = allocations.map((allocation) => ({
        ...allocation,
        allocation_pct: (allocation.allocation_pct / totalPct) * 100
      }));
      const risk = scoreRiskPulse(normalized);
      const topAllocation = Math.max(...normalized.map((allocation) => allocation.allocation_pct));
      const hhi = normalized.reduce((total, allocation) => total + (allocation.allocation_pct / 100) ** 2, 0);
      const highRiskPct = normalized
        .filter((allocation) => riskScore(allocation.option_id) >= 4)
        .reduce((total, allocation) => total + allocation.allocation_pct, 0);
      const defensivePct = normalized
        .filter((allocation) => isDefensive(allocation.option_id))
        .reduce((total, allocation) => total + allocation.allocation_pct, 0);
      const techPct = normalized
        .filter((allocation) => isTechnology(allocation.option_id))
        .reduce((total, allocation) => total + allocation.allocation_pct, 0);
      const cashDurationPct = normalized
        .filter((allocation) => isCashDuration(allocation.option_id, assetsById))
        .reduce((total, allocation) => total + allocation.allocation_pct, 0);
      const internationalPct = normalized
        .filter((allocation) => isInternational(allocation.option_id, assetsById))
        .reduce((total, allocation) => total + allocation.allocation_pct, 0);
      const realAssetsPct = normalized
        .filter((allocation) => isRealAsset(allocation.option_id, assetsById))
        .reduce((total, allocation) => total + allocation.allocation_pct, 0);
      return {
        key: portfolioKey(portfolio),
        round_id: portfolio.round_id,
        run_id: portfolio.run_id,
        model_id: portfolio.model_id,
        provider: portfolio.provider,
        track: portfolio.track,
        status: portfolio.status,
        entry_date: portfolio.entry_date,
        exit_date: portfolio.exit_date,
        chronology: roundChronology(roundById, portfolio),
        holding_count: normalized.length,
        top_allocation_pct: topAllocation,
        concentration_hhi: hhi,
        effective_asset_count: hhi > 0 ? 1 / hhi : null,
        risk_pulse: risk.risk_pulse,
        risk_score_1_5: risk.risk_score_1_5,
        risk_on_loading: risk.risk_on_loading,
        high_risk_pct: highRiskPct,
        defensive_pct: defensivePct,
        tech_pct: techPct,
        cash_duration_pct: cashDurationPct,
        international_pct: internationalPct,
        real_assets_pct: realAssetsPct,
        allocations: normalized
      };
    })
    .filter(Boolean);
}

function cosineSimilarity(left, right) {
  const leftMap = new Map(left.allocations.map((allocation) => [allocation.option_id, allocation.allocation_pct / 100]));
  const rightMap = new Map(right.allocations.map((allocation) => [allocation.option_id, allocation.allocation_pct / 100]));
  const keys = new Set([...leftMap.keys(), ...rightMap.keys()]);
  let dot = 0;
  let leftNorm = 0;
  let rightNorm = 0;
  for (const key of keys) {
    const leftValue = leftMap.get(key) ?? 0;
    const rightValue = rightMap.get(key) ?? 0;
    dot += leftValue * rightValue;
    leftNorm += leftValue ** 2;
    rightNorm += rightValue ** 2;
  }
  if (leftNorm <= 0 || rightNorm <= 0) return null;
  return dot / Math.sqrt(leftNorm * rightNorm);
}

function vectorTurnover(left, right) {
  const leftMap = new Map(left.allocations.map((allocation) => [allocation.option_id, allocation.allocation_pct]));
  const rightMap = new Map(right.allocations.map((allocation) => [allocation.option_id, allocation.allocation_pct]));
  const keys = new Set([...leftMap.keys(), ...rightMap.keys()]);
  let grossChange = 0;
  for (const key of keys) {
    grossChange += Math.abs((rightMap.get(key) ?? 0) - (leftMap.get(key) ?? 0));
  }
  return grossChange / 2;
}

function aggregateBehaviorHoldings(rows, assetsById, limit = 6) {
  const byAsset = new Map();
  for (const row of rows) {
    for (const allocation of row.allocations) {
      const existing =
        byAsset.get(allocation.option_id) ??
        {
          option_id: allocation.option_id,
          label: assetsById.get(allocation.option_id)?.label ?? allocation.label ?? allocation.option_id,
          ticker: assetsById.get(allocation.option_id)?.ticker ?? allocation.ticker ?? "",
          category: assetsById.get(allocation.option_id)?.category ?? allocation.category ?? "unknown",
          allocation_values: [],
          portfolio_keys: new Set()
        };
      existing.allocation_values.push(allocation.allocation_pct);
      existing.portfolio_keys.add(row.key);
      byAsset.set(allocation.option_id, existing);
    }
  }
  const portfolioCount = rows.length || 1;
  return Array.from(byAsset.values())
    .map((row) => ({
      option_id: row.option_id,
      label: row.label,
      ticker: row.ticker,
      category: row.category,
      average_allocation_pct: row.allocation_values.reduce((total, value) => total + value, 0) / portfolioCount,
      frequency_pct: (row.portfolio_keys.size / portfolioCount) * 100
    }))
    .sort((a, b) => b.average_allocation_pct - a.average_allocation_pct || b.frequency_pct - a.frequency_pct || a.label.localeCompare(b.label))
    .slice(0, limit);
}

function aggregateBehaviorCategories(rows, assetsById, limit = 6) {
  const byCategory = new Map();
  for (const row of rows) {
    const rowCategories = new Map();
    for (const allocation of row.allocations) {
      const category = assetsById.get(allocation.option_id)?.category ?? allocation.category ?? "unknown";
      rowCategories.set(category, (rowCategories.get(category) ?? 0) + allocation.allocation_pct);
    }
    for (const [category, value] of rowCategories.entries()) {
      byCategory.set(category, (byCategory.get(category) ?? 0) + value);
    }
  }
  const divisor = rows.length || 1;
  return Array.from(byCategory.entries())
    .map(([category, value]) => ({ category, average_allocation_pct: value / divisor }))
    .sort((a, b) => b.average_allocation_pct - a.average_allocation_pct || a.category.localeCompare(b.category))
    .slice(0, limit);
}

function peerSimilarityStats(scoredRows) {
  const groups = new Map();
  const modelValues = new Map();
  const modelOutliers = new Map();
  const pairValues = new Map();
  for (const row of scoredRows) {
    const key = `${row.round_id}:${row.run_id}`;
    groups.set(key, [...(groups.get(key) ?? []), row]);
  }
  for (const rows of groups.values()) {
    if (rows.length < 2) continue;
    const roundModelValues = new Map();
    for (let leftIndex = 0; leftIndex < rows.length; leftIndex += 1) {
      for (let rightIndex = leftIndex + 1; rightIndex < rows.length; rightIndex += 1) {
        const left = rows[leftIndex];
        const right = rows[rightIndex];
        const similarity = cosineSimilarity(left, right);
        if (similarity === null) continue;
        modelValues.set(left.model_id, [...(modelValues.get(left.model_id) ?? []), similarity]);
        modelValues.set(right.model_id, [...(modelValues.get(right.model_id) ?? []), similarity]);
        roundModelValues.set(left.model_id, [...(roundModelValues.get(left.model_id) ?? []), similarity]);
        roundModelValues.set(right.model_id, [...(roundModelValues.get(right.model_id) ?? []), similarity]);
        const [a, b] = [left.model_id, right.model_id].sort();
        const pairKey = `${a}::${b}`;
        pairValues.set(pairKey, [...(pairValues.get(pairKey) ?? []), similarity]);
      }
    }
    const roundAverages = Array.from(roundModelValues.entries()).map(([modelId, values]) => ({
      model_id: modelId,
      average: average(values)
    }));
    const mean = average(roundAverages.map((row) => row.average));
    const deviation = standardDeviation(roundAverages.map((row) => row.average));
    if (mean !== null && deviation !== null && deviation > 0) {
      for (const row of roundAverages) {
        if (typeof row.average === "number" && row.average < mean - deviation) {
          modelOutliers.set(row.model_id, (modelOutliers.get(row.model_id) ?? 0) + 1);
        }
      }
    }
  }

  const modelStats = new Map();
  for (const [modelId, values] of modelValues.entries()) {
    const pairRows = Array.from(pairValues.entries())
      .filter(([key]) => key.split("::").includes(modelId))
      .map(([key, pair]) => {
        const [left, right] = key.split("::");
        return {
          peer_model_id: left === modelId ? right : left,
          average_similarity: average(pair),
          shared_round_count: pair.length
        };
      })
      .sort((a, b) => Number(b.average_similarity ?? -Infinity) - Number(a.average_similarity ?? -Infinity));
    const eligiblePeerRows = pairRows.filter((row) => row.shared_round_count >= 6);
    modelStats.set(modelId, {
      average_peer_similarity: average(values),
      similarity_observation_count: values.length,
      outlier_round_count: modelOutliers.get(modelId) ?? 0,
      closest_peer: eligiblePeerRows[0] ?? pairRows[0] ?? null
    });
  }

  const pairwise = Array.from(pairValues.entries())
    .map(([key, values]) => {
      const [left, right] = key.split("::");
      return {
        left_model_id: left,
        right_model_id: right,
        average_similarity: average(values),
        shared_round_count: values.length
      };
    })
    .sort((a, b) => Number(b.average_similarity ?? -Infinity) - Number(a.average_similarity ?? -Infinity));
  return { modelStats, pairwise };
}

function turnoverStats(scoredRows) {
  const rowsByModelTrack = new Map();
  for (const row of scoredRows) {
    const key = `${row.model_id}:${row.track}`;
    rowsByModelTrack.set(key, [...(rowsByModelTrack.get(key) ?? []), row]);
  }
  const output = new Map();
  for (const [key, rows] of rowsByModelTrack.entries()) {
    const [modelId, track] = key.split(":");
    const sorted = [...rows].sort((a, b) => a.chronology.localeCompare(b.chronology));
    const values = [];
    for (let index = 1; index < sorted.length; index += 1) {
      values.push(vectorTurnover(sorted[index - 1], sorted[index]));
    }
    const existing =
      output.get(modelId) ??
      {
        all_values: [],
        weekly_values: [],
        monthly_values: []
      };
    existing.all_values.push(...values);
    existing[`${track}_values`]?.push(...values);
    output.set(modelId, existing);
  }
  return new Map(
    Array.from(output.entries()).map(([modelId, values]) => [
      modelId,
      {
        average_turnover_pct: average(values.all_values),
        weekly_turnover_pct: average(values.weekly_values),
        monthly_turnover_pct: average(values.monthly_values),
        turnover_observation_count: values.all_values.length
      }
    ])
  );
}

function performanceBehaviorStats(results) {
  const roundModelCounts = new Map();
  for (const row of results) {
    roundModelCounts.set(row.round_id, (roundModelCounts.get(row.round_id) ?? 0) + 1);
  }
  const byModel = new Map();
  for (const row of results) {
    const existing =
      byModel.get(row.model_id) ??
      {
        rows: [],
        returns: [],
        alphas: [],
        scores: [],
        ranks: [],
        regrets: [],
        confidence_rows: []
      };
    existing.rows.push(row);
    if (typeof row.portfolio_return_pct === "number") existing.returns.push(row.portfolio_return_pct);
    if (typeof row.alpha_pp === "number") existing.alphas.push(row.alpha_pp);
    if (typeof row.capitalbench_score === "number") existing.scores.push(row.capitalbench_score);
    if (typeof row.rank === "number") existing.ranks.push(row.rank);
    if (typeof row.regret_vs_best_option_pct === "number") existing.regrets.push(row.regret_vs_best_option_pct);
    if (typeof row.confidence === "number" && typeof row.portfolio_return_pct === "number") {
      existing.confidence_rows.push({ confidence: row.confidence, return_pct: row.portfolio_return_pct });
    }
    byModel.set(row.model_id, existing);
  }
  return new Map(
    Array.from(byModel.entries()).map(([modelId, values]) => {
      const confidenceMedian = median(values.confidence_rows.map((row) => row.confidence));
      const highConfidence = confidenceMedian === null ? [] : values.confidence_rows.filter((row) => row.confidence >= confidenceMedian);
      const lowConfidence = confidenceMedian === null ? [] : values.confidence_rows.filter((row) => row.confidence < confidenceMedian);
      const highReturn = average(highConfidence.map((row) => row.return_pct));
      const lowReturn = average(lowConfidence.map((row) => row.return_pct));
      return [
        modelId,
        {
          resolved_round_count: values.rows.length,
          average_return_pct: average(values.returns),
          average_alpha_pp: average(values.alphas),
          average_capitalbench_score: average(values.scores),
          average_rank: average(values.ranks),
          win_count: values.rows.filter((row) => row.rank === 1).length,
          last_count: values.rows.filter((row) => row.rank === roundModelCounts.get(row.round_id)).length,
          beat_sp500_count: values.rows.filter((row) => typeof row.alpha_pp === "number" && row.alpha_pp > 0).length,
          beat_sp500_rate_pct: values.rows.length
            ? (values.rows.filter((row) => typeof row.alpha_pp === "number" && row.alpha_pp > 0).length / values.rows.length) * 100
            : null,
          average_regret_vs_oracle_pct: average(values.regrets),
          confidence_calibration:
            values.confidence_rows.length >= 6 && highReturn !== null && lowReturn !== null
              ? {
                  median_confidence: confidenceMedian,
                  high_confidence_average_return_pct: highReturn,
                  low_confidence_average_return_pct: lowReturn,
                  high_minus_low_return_pp: highReturn - lowReturn,
                  observation_count: values.confidence_rows.length
                }
              : {
                  median_confidence: confidenceMedian,
                  high_confidence_average_return_pct: null,
                  low_confidence_average_return_pct: null,
                  high_minus_low_return_pp: null,
                  observation_count: values.confidence_rows.length
                }
        }
      ];
    })
  );
}

function behaviorArchetype({ sample, metrics, peer }) {
  if (sample.portfolio_count < 8) {
    return {
      label: "Early sample",
      description: "This model has too few saved official portfolios for a stable behavioral label.",
      confidence: "low"
    };
  }
  if (metrics.average_top_allocation_pct >= 37 && metrics.average_holding_count <= 4.1) {
    return {
      label: "High-conviction concentrator",
      description: "Usually expresses views through fewer holdings and a larger top position than peers.",
      confidence: "medium"
    };
  }
  if (metrics.average_risk_pulse >= 82 && metrics.high_risk_pct >= 82 && metrics.defensive_pct < 8) {
    return {
      label: "Aggressive upside hunter",
      description: "Often leans toward growth, momentum, and high-beta allocations with little defensive ballast.",
      confidence: "medium"
    };
  }
  if (metrics.defensive_pct >= 15 && metrics.average_holding_count >= 4.5) {
    return {
      label: "Risk-managed allocator",
      description: "Keeps more diversified portfolios and pairs risk assets with defensive exposure more often than peers.",
      confidence: "medium"
    };
  }
  if (typeof peer.average_peer_similarity === "number" && peer.average_peer_similarity < 0.52) {
    return {
      label: "Contrarian allocator",
      description: "Historically builds portfolios that overlap less with the rest of the model roster.",
      confidence: "medium"
    };
  }
  if (typeof peer.average_peer_similarity === "number" && peer.average_peer_similarity >= 0.64 && (metrics.tech_pct >= 45 || metrics.high_risk_pct >= 78)) {
    return {
      label: "Momentum consensus follower",
      description: "Tends to align with the model crowd while emphasizing growth, technology, or momentum exposure.",
      confidence: "medium"
    };
  }
  return {
    label: "Balanced allocator",
    description: "Shows a mixed profile without one dominant allocation behavior standing out yet.",
    confidence: "medium"
  };
}

function percentileValue(rows, modelId, getter, { lowerIsHigher = false } = {}) {
  const values = rows
    .map((row) => ({ model_id: row.model_id, value: getter(row) }))
    .filter((row) => typeof row.value === "number" && Number.isFinite(row.value));
  const target = values.find((row) => row.model_id === modelId);
  if (!target || values.length <= 1) return null;
  const comparableCount = values.filter((row) => (lowerIsHigher ? row.value >= target.value : row.value <= target.value)).length;
  return ((comparableCount - 1) / (values.length - 1)) * 100;
}

function buildModelBehavior({ models, rounds, portfolios, results, assetsById }) {
  const scoredRows = scoredBehaviorPortfolios({ portfolios, rounds, assetsById });
  const peer = peerSimilarityStats(scoredRows);
  const turnover = turnoverStats(scoredRows);
  const performance = performanceBehaviorStats(results);
  const rowsByModel = new Map();
  for (const row of scoredRows) {
    rowsByModel.set(row.model_id, [...(rowsByModel.get(row.model_id) ?? []), row]);
  }

  const rawProfiles = models.map((model) => {
    const rows = rowsByModel.get(model.model_id) ?? [];
    const liveRows = rows.filter((row) => row.status === "active");
    const sortedRows = [...rows].sort((a, b) => a.chronology.localeCompare(b.chronology));
    const latestRows = liveRows.length ? liveRows : sortedRows.slice(-2);
    const priorRows = sortedRows.filter((row) => !new Set(latestRows.map((item) => item.key)).has(row.key)).slice(-latestRows.length || -1);
    const weeklyRows = rows.filter((row) => row.track === "weekly");
    const monthlyRows = rows.filter((row) => row.track === "monthly");
    const sample = {
      portfolio_count: rows.length,
      weekly_portfolio_count: weeklyRows.length,
      monthly_portfolio_count: monthlyRows.length,
      active_portfolio_count: liveRows.length,
      resolved_round_count: performance.get(model.model_id)?.resolved_round_count ?? 0,
      first_round_id: sortedRows[0]?.round_id ?? null,
      latest_round_id: sortedRows.at(-1)?.round_id ?? null
    };
    const metrics = {
      average_risk_pulse: average(rows.map((row) => row.risk_pulse)),
      average_risk_score_1_5: average(rows.map((row) => row.risk_score_1_5)),
      weekly_risk_pulse: average(weeklyRows.map((row) => row.risk_pulse)),
      monthly_risk_pulse: average(monthlyRows.map((row) => row.risk_pulse)),
      horizon_risk_delta_points:
        average(monthlyRows.map((row) => row.risk_pulse)) !== null && average(weeklyRows.map((row) => row.risk_pulse)) !== null
          ? average(monthlyRows.map((row) => row.risk_pulse)) - average(weeklyRows.map((row) => row.risk_pulse))
          : null,
      high_risk_pct: average(rows.map((row) => row.high_risk_pct)) ?? 0,
      defensive_pct: average(rows.map((row) => row.defensive_pct)) ?? 0,
      tech_pct: average(rows.map((row) => row.tech_pct)) ?? 0,
      cash_duration_pct: average(rows.map((row) => row.cash_duration_pct)) ?? 0,
      international_pct: average(rows.map((row) => row.international_pct)) ?? 0,
      real_assets_pct: average(rows.map((row) => row.real_assets_pct)) ?? 0,
      average_holding_count: average(rows.map((row) => row.holding_count)),
      average_top_allocation_pct: average(rows.map((row) => row.top_allocation_pct)),
      concentration_hhi: average(rows.map((row) => row.concentration_hhi)),
      effective_asset_count: average(rows.map((row) => row.effective_asset_count))
    };
    const peerStats = peer.modelStats.get(model.model_id) ?? {
      average_peer_similarity: null,
      similarity_observation_count: 0,
      outlier_round_count: 0,
      closest_peer: null
    };
    const turnoverStatsForModel = turnover.get(model.model_id) ?? {
      average_turnover_pct: null,
      weekly_turnover_pct: null,
      monthly_turnover_pct: null,
      turnover_observation_count: 0
    };
    const recentScore = average(latestRows.map((row) => row.risk_pulse));
    const priorScore = average(priorRows.map((row) => row.risk_pulse));
    const recent = {
      active_portfolio_count: liveRows.length,
      current_or_latest_risk_pulse: recentScore,
      previous_comparable_risk_pulse: priorScore,
      risk_pulse_change_points: recentScore !== null && priorScore !== null ? recentScore - priorScore : null,
      top_assets: aggregateBehaviorHoldings(latestRows, assetsById, 5)
    };
    const archetype = behaviorArchetype({ sample, metrics, peer: peerStats });
    return {
      model_id: model.model_id,
      label: model.label,
      provider: model.provider,
      provider_label: model.provider_label,
      archetype,
      sample,
      metrics,
      peer: peerStats,
      turnover: turnoverStatsForModel,
      performance: performance.get(model.model_id) ?? {
        resolved_round_count: 0,
        average_return_pct: null,
        average_alpha_pp: null,
        average_capitalbench_score: null,
        average_rank: null,
        win_count: 0,
        last_count: 0,
        beat_sp500_count: 0,
        beat_sp500_rate_pct: null,
        average_regret_vs_oracle_pct: null,
        confidence_calibration: {
          median_confidence: null,
          high_confidence_average_return_pct: null,
          low_confidence_average_return_pct: null,
          high_minus_low_return_pp: null,
          observation_count: 0
        }
      },
      recent,
      top_assets: aggregateBehaviorHoldings(rows, assetsById, 8),
      top_categories: aggregateBehaviorCategories(rows, assetsById, 8),
      methodology_href: "/risk-appetite/#model-behavior-methodology"
    };
  });

  const profiles = rawProfiles
    .map((profile) => ({
      ...profile,
      peer_percentiles: {
        risk_pulse: percentileValue(rawProfiles, profile.model_id, (row) => row.metrics.average_risk_pulse),
        concentration: percentileValue(rawProfiles, profile.model_id, (row) => row.metrics.concentration_hhi),
        defensiveness: percentileValue(rawProfiles, profile.model_id, (row) => row.metrics.defensive_pct),
        peer_similarity: percentileValue(rawProfiles, profile.model_id, (row) => row.peer.average_peer_similarity),
        turnover_stability: percentileValue(rawProfiles, profile.model_id, (row) => row.turnover.average_turnover_pct, { lowerIsHigher: true }),
        capitalbench_score: percentileValue(rawProfiles, profile.model_id, (row) => row.performance.average_capitalbench_score)
      }
    }))
    .sort((a, b) => a.label.localeCompare(b.label));

  function leaderBy(getter, direction = "desc") {
    return [...profiles]
      .filter((profile) => typeof getter(profile) === "number" && Number.isFinite(getter(profile)))
      .sort((a, b) =>
        direction === "asc"
          ? getter(a) - getter(b) || a.label.localeCompare(b.label)
          : getter(b) - getter(a) || a.label.localeCompare(b.label)
      )[0] ?? null;
  }

  const dataAsOf = portfolios.map((portfolio) => portfolio.entry_date || portfolio.exit_date || "").filter(Boolean).sort().at(-1) ?? null;
  return {
    version: "model_behavior_v1",
    generated_at: new Date().toISOString(),
    data_as_of: dataAsOf,
    methodology_href: "/risk-appetite/#model-behavior-methodology",
    summary: {
      model_count: profiles.length,
      portfolio_count: scoredRows.length,
      resolved_result_count: results.length,
      highest_risk_model_id: leaderBy((row) => row.metrics.average_risk_pulse)?.model_id ?? null,
      most_concentrated_model_id: leaderBy((row) => row.metrics.concentration_hhi)?.model_id ?? null,
      most_defensive_model_id: leaderBy((row) => row.metrics.defensive_pct)?.model_id ?? null,
      most_consensus_aligned_model_id: leaderBy((row) => row.peer.average_peer_similarity)?.model_id ?? null,
      most_distinctive_model_id: leaderBy((row) => row.peer.average_peer_similarity, "asc")?.model_id ?? null,
      lowest_turnover_model_id: leaderBy((row) => row.turnover.average_turnover_pct, "asc")?.model_id ?? null
    },
    profiles,
    pairwise_similarity: peer.pairwise
  };
}

function loadRound(row) {
  const roundPath = join(roundsRoot, row.name);
  const manifest = readYaml(join(roundPath, "manifest.yaml"), {});
  if (!manifest.round_id) return null;
  const selectedRun = publicOfficialRuns(roundPath)[0];
  if (!selectedRun) return null;
  const resultsPath = join(roundPath, "runs", selectedRun.run_id, "results", "leaderboard.csv");
  const entryDate = String(manifest.entry_date ?? "");
  const exitDate = String(manifest.exit_date ?? "");
  const status = roundStatus({ hasResults: existsSync(resultsPath), exitDate });
  const round = {
    round_id: String(manifest.round_id),
    title: String(manifest.title ?? manifest.round_id),
    description: String(manifest.description ?? "CapitalBench benchmark round."),
    track: trackFromRound(manifest),
    status,
    decision_date: String(manifest.decision_date ?? ""),
    decision_deadline_utc: String(manifest.decision_deadline ?? ""),
    start_at: entryDate ? `${entryDate}T20:00:00Z` : null,
    end_at: exitDate ? `${exitDate}T20:00:00Z` : null,
    entry_date: entryDate,
    exit_date: exitDate,
    horizon: String(manifest.horizon ?? ""),
    horizon_days: horizonDays(entryDate, exitDate),
    methodology_version: selectedRun.manifest.methodology_version ?? manifest.methodology_version ?? "",
    universe_version: inferUniverseVersion(roundPath, manifest.universe_version),
    submission_format: manifest.submission_format ?? "single_pick",
    official_run_id: selectedRun.run_id,
    benchmark_option_id: "SP500",
    model_count: 0,
    proof: {
      round_page_url: `https://www.capitalbench.org/rounds/${manifest.round_id}/`,
      portfolio_file_url: null,
      hashes: readJson(join(roundPath, "hashes.json"), [])
    }
  };
  return { roundPath, round, selectedRun };
}

function loadSubmissions({ roundPath, round, selectedRun, assetsById }) {
  const parsedPath = join(roundPath, "runs", selectedRun.run_id, "submissions", "parsed");
  if (!existsSync(parsedPath)) return { portfolios: [], allocations: [] };
  const portfolios = [];
  const allocations = [];
  for (const filename of readdirSync(parsedPath).filter((item) => item.endsWith(".json")).sort()) {
    const payload = readJson(join(parsedPath, filename), {});
    if (!payload.model_id || !payload.provider) continue;
    const modelId = String(payload.model_id);
    const provider = String(payload.provider);
    const portfolioAllocations = decisionAllocations(payload);
    const portfolio = {
      round_id: round.round_id,
      run_id: selectedRun.run_id,
      model_id: modelId,
      provider,
      mode: String(payload.mode ?? selectedRun.manifest.mode ?? ""),
      run_type: String(payload.run_type ?? selectedRun.manifest.run_type ?? ""),
      track: round.track,
      status: round.status,
      entry_date: round.entry_date,
      exit_date: round.exit_date,
      submission_format: portfolioAllocations.length > 1 ? "portfolio" : "single_pick",
      selected_option_id: primaryOptionId(payload),
      holding_count: portfolioAllocations.length || 1,
      confidence: numberValue(payload.confidence),
      rationale_summary: String(payload.rationale_summary ?? payload.portfolio_rationale ?? ""),
      portfolio_rationale: String(payload.portfolio_rationale ?? ""),
      key_risks: Array.isArray(payload.key_risks) ? payload.key_risks.map(String) : [],
      parsed_file_path: `rounds/${round.round_id}/runs/${selectedRun.run_id}/submissions/parsed/${filename}`,
      allocations: portfolioAllocations.map((allocation, index) => {
        const asset = assetsById.get(allocation.option_id);
        return {
          option_id: allocation.option_id,
          label: asset?.label ?? allocation.option_id,
          ticker: asset?.ticker ?? "",
          category: asset?.category ?? "unknown",
          asset_class: asset?.asset_class ?? "unknown",
          allocation_pct: allocation.allocation_pct,
          allocation_bps: allocation.allocation_bps,
          allocation_rank: index + 1,
          rationale: allocation.rationale
        };
      })
    };
    portfolios.push(portfolio);
    for (const allocation of portfolio.allocations) {
      allocations.push({
        round_id: round.round_id,
        run_id: selectedRun.run_id,
        model_id: modelId,
        provider,
        track: round.track,
        status: round.status,
        entry_date: round.entry_date,
        exit_date: round.exit_date,
        option_id: allocation.option_id,
        label: allocation.label,
        ticker: allocation.ticker,
        category: allocation.category,
        asset_class: allocation.asset_class,
        allocation_pct: allocation.allocation_pct,
        allocation_bps: allocation.allocation_bps,
        allocation_rank: allocation.allocation_rank,
        rationale: allocation.rationale
      });
    }
  }
  return { portfolios, allocations };
}

function loadResults({ roundPath, round, selectedRun }) {
  const rows = parseCsv(readText(join(roundPath, "runs", selectedRun.run_id, "results", "leaderboard.csv")));
  const maxReturnPct = maxPossibleReturnPct(roundPath, selectedRun);
  return rows
    .map((row, index) => {
      const portfolioReturnPct = percentReturnValue(row.portfolio_return || row.selected_asset_return);
      return {
        round_id: row.round_id || round.round_id,
        run_id: selectedRun.run_id,
        track: round.track,
        model_id: row.model_id,
        provider: row.provider,
        rank: index + 1,
        selected_option_id: row.selected_option_id || "",
        submission_format: row.submission_format || "",
        holding_count: numberValue(row.holding_count),
        portfolio_return_pct: portfolioReturnPct,
        selected_asset_return_pct: percentReturnValue(row.selected_asset_return),
        benchmark_return_pct: percentReturnValue(row.sp500_return),
        alpha_pp: percentReturnValue(row.alpha_vs_sp500),
        max_possible_return_pct: maxReturnPct,
        capitalbench_score: capitalBenchScore(portfolioReturnPct, maxReturnPct),
        regret_vs_best_option_pct: percentReturnValue(row.regret_vs_best_option),
        rank_among_options: numberValue(row.rank_among_options),
        confidence: numberValue(row.confidence)
      };
    })
    .filter((row) => row.model_id && row.provider);
}

function loadReturns({ roundPath, round, selectedRun }) {
  return parseCsv(readText(join(roundPath, "runs", selectedRun.run_id, "results", "returns.csv")))
    .map((row) => ({
      round_id: round.round_id,
      run_id: selectedRun.run_id,
      track: round.track,
      option_id: row.option_id,
      label: row.label || row.option_id,
      ticker: row.asset_symbol || "",
      entry_price: numberValue(row.entry_price),
      exit_price: numberValue(row.exit_price),
      entry_price_source: row.entry_price_source || "",
      exit_price_source: row.exit_price_source || "",
      return_pct: percentReturnValue(row.return),
      rank: numberValue(row.rank),
      is_benchmark: isBenchmarkOption(row.option_id, boolValue(row.is_benchmark)),
      is_cash: boolValue(row.is_cash)
    }))
    .filter((row) => row.option_id);
}

function loadInterimPerformance({ roundPath, round, selectedRun }) {
  return parseCsv(readText(join(roundPath, "runs", selectedRun.run_id, "results", "weekly_performance.csv")))
    .map((row) => {
      const modelReturnPct = percentReturnValue(row.model_return);
      const sp500ReturnPct = percentReturnValue(row.sp500_return);
      const alphaPp = percentReturnValue(row.alpha_vs_sp500);
      return {
        round_id: row.round_id || round.round_id,
        run_id: row.run_id || selectedRun.run_id,
        track: round.track,
        status: round.status,
        entry_date: round.entry_date,
        exit_date: round.exit_date,
        model_id: row.model_id,
        provider: row.provider,
        target_date: row.target_date || "",
        price_date: row.price_date || row.target_date || "",
        days_elapsed: numberValue(row.days_elapsed),
        run_type: row.run_type || "",
        submission_format: row.submission_format || "",
        selected_option_id: row.selected_option_id || "",
        holding_count: numberValue(row.holding_count),
        model_return_pct: modelReturnPct,
        sp500_return_pct: sp500ReturnPct,
        alpha_pp: alphaPp,
        price_status: row.price_status || "",
        published: boolValue(row.published)
      };
    })
    .filter(
      (row) =>
        row.model_id &&
        row.provider &&
        row.target_date &&
        typeof row.model_return_pct === "number" &&
        typeof row.sp500_return_pct === "number" &&
        typeof row.alpha_pp === "number"
    );
}

function buildModelStyles(models, allocations, assetsById) {
  const styles = [];
  for (const model of models) {
    const rows = allocations.filter((row) => row.model_id === model.model_id);
    const portfolioKeys = new Set(rows.map((row) => `${row.round_id}:${row.run_id}:${row.model_id}`));
    const rowsByPortfolio = new Map();
    let highRiskPct = 0;
    let defensivePct = 0;
    let techPct = 0;
    let cashPct = 0;
    let equityPct = 0;
    const categoryPct = new Map();
    for (const row of rows) {
      const asset = assetsById.get(row.option_id);
      const portfolioKey = `${row.round_id}:${row.run_id}:${row.model_id}`;
      rowsByPortfolio.set(portfolioKey, [...(rowsByPortfolio.get(portfolioKey) ?? []), row]);
      if (riskScore(row.option_id) >= 4) highRiskPct += row.allocation_pct;
      if (isDefensive(row.option_id)) defensivePct += row.allocation_pct;
      if (isTechnology(row.option_id)) techPct += row.allocation_pct;
      if (asset?.is_cash) cashPct += row.allocation_pct;
      if (String(asset?.asset_class ?? "").toLowerCase() === "equity") equityPct += row.allocation_pct;
      const category = asset?.category ?? row.category ?? "unknown";
      categoryPct.set(category, (categoryPct.get(category) ?? 0) + row.allocation_pct);
    }
    const portfolioRiskScores = Array.from(rowsByPortfolio.values()).map((portfolioRows) => {
      const portfolioPct = portfolioRows.reduce((total, row) => total + row.allocation_pct, 0);
      if (portfolioPct <= 0) return null;
      return portfolioRows.reduce((total, row) => total + (row.allocation_pct / portfolioPct) * riskScore(row.option_id), 0);
    });
    const score = average(portfolioRiskScores);
    const sampleRoundCount = new Set(rows.map((row) => row.round_id)).size;
    const divisor = portfolioKeys.size || 1;
    styles.push({
      model_id: model.model_id,
      risk_appetite_score: score,
      risk_appetite_label: riskLabel(score),
      cash_allocation_pct: cashPct / divisor,
      equity_allocation_pct: equityPct / divisor,
      thematic_allocation_pct: techPct / divisor,
      high_risk_pct: highRiskPct / divisor,
      defensive_pct: defensivePct / divisor,
      tech_pct: techPct / divisor,
      top_category:
        Array.from(categoryPct.entries()).sort((a, b) => b[1] - a[1])[0]?.[0] ?? null,
      sample_round_count: sampleRoundCount,
      portfolio_count: portfolioKeys.size
    });
  }
  return styles;
}

function buildReadModel() {
  if (!existsSync(roundsRoot)) throw new Error(`Rounds directory not found: ${roundsRoot}`);
  const roundRows = readdirSync(roundsRoot, { withFileTypes: true })
    .filter((entry) => entry.isDirectory() && entry.name.startsWith("CB-"))
    .map(loadRound)
    .filter(Boolean)
    .sort((a, b) => b.round.decision_deadline_utc.localeCompare(a.round.decision_deadline_utc));

  const latestRoundWithOptions = roundRows.find((item) => existsSync(join(item.roundPath, "options.yaml")));
  const currentOptionIds = new Set(loadOptions(latestRoundWithOptions?.roundPath ?? "", null, latestRoundWithOptions?.round.round_id ?? "").map((option) => option.option_id));
  const assetsById = new Map();
  for (const item of [...roundRows].reverse()) {
    for (const asset of loadOptions(item.roundPath, currentOptionIds, item.round.round_id)) {
      const existing = assetsById.get(asset.option_id);
      assetsById.set(asset.option_id, {
        ...existing,
        ...asset,
        first_seen_round_id: existing?.first_seen_round_id ?? item.round.round_id,
        latest_round_id: item.round.round_id,
        in_current_universe: currentOptionIds.has(asset.option_id)
      });
    }
  }

  const rounds = [];
  const portfolios = [];
  const allocations = [];
  const results = [];
  const returns = [];
  const interimPerformance = [];
  const proof = [];

  for (const item of roundRows) {
    const loaded = loadSubmissions({ ...item, assetsById });
    item.round.model_count = new Set(loaded.portfolios.map((portfolio) => portfolio.model_id)).size;
    rounds.push(item.round);
    portfolios.push(...loaded.portfolios);
    allocations.push(...loaded.allocations);
    results.push(...loadResults(item));
    returns.push(...loadReturns(item));
    interimPerformance.push(...loadInterimPerformance(item));
    proof.push({
      round_id: item.round.round_id,
      run_id: item.selectedRun.run_id,
      hashes: item.round.proof.hashes,
      round_page_url: item.round.proof.round_page_url
    });
  }

  const modelMap = new Map();
  for (const portfolio of portfolios) {
    const existing = modelMap.get(portfolio.model_id);
    const modelRounds = portfolios.filter((row) => row.model_id === portfolio.model_id);
    modelMap.set(portfolio.model_id, {
      model_id: portfolio.model_id,
      label: modelLabel(portfolio.model_id),
      provider: portfolio.provider,
      provider_label: PROVIDER_LABELS[portfolio.provider] ?? portfolio.provider,
      logo_src: PROVIDER_LOGOS[portfolio.provider],
      active: modelRounds.some((row) => row.status === "active"),
      first_round_id:
        existing?.first_round_id ??
        [...modelRounds].sort((a, b) => a.round_id.localeCompare(b.round_id))[0]?.round_id ??
        portfolio.round_id,
      latest_round_id:
        [...modelRounds].sort((a, b) => b.round_id.localeCompare(a.round_id))[0]?.round_id ??
        portfolio.round_id
    });
  }
  const models = Array.from(modelMap.values()).sort((a, b) => a.provider_label.localeCompare(b.provider_label) || a.label.localeCompare(b.label));
  const assets = Array.from(assetsById.values())
    .map((asset) => {
      const definition = assetRiskDefinition(asset.option_id);
      return {
        ...asset,
        risk_score_1_5: Number(definition.risk_score_1_5),
        risk_on_loading: Number(definition.risk_on_loading),
        risk_regime_group: definition.regime_group,
        defensive: Boolean(definition.defensive),
        technology: Boolean(definition.technology)
      };
    })
    .sort((a, b) => Number(a.sort_order ?? 9999) - Number(b.sort_order ?? 9999) || a.label.localeCompare(b.label));
  const modelStyles = buildModelStyles(models, allocations, assetsById);
  const modelBehavior = buildModelBehavior({ models, rounds, portfolios, results, assetsById });
  const riskAppetite = buildRiskAppetiteSnapshot({
    rounds,
    portfolios,
    assets,
    definitions: assetRiskDefinitions,
    version: String(assetRiskModel.version ?? "")
  });

  return {
    generated_at: new Date().toISOString(),
    api_version: "v1",
    source: "capitalbench_local_rounds",
    current_universe_round_id: latestRoundWithOptions?.round.round_id ?? null,
    benchmark_set_policy: {
      version: String(benchmarkSetConfig.version ?? "benchmark_sets_v1"),
      qualification_thresholds: {
        weekly: Number(benchmarkSetConfig.qualification_thresholds?.weekly ?? 6),
        monthly: Number(benchmarkSetConfig.qualification_thresholds?.monthly ?? 3)
      }
    },
    benchmark_set_definitions: buildBenchmarkSetDefinitions({ rounds, portfolios }),
    rounds,
    models,
    assets,
    portfolios,
    allocations,
    results,
    returns,
    interim_performance: interimPerformance,
    model_styles: modelStyles,
    model_behavior: modelBehavior,
    risk_appetite: riskAppetite,
    insights: loadLatestInsights(),
    proof
  };
}

const readModel = buildReadModel();
mkdirSync(join(process.cwd(), "src", "generated"), { recursive: true });
writeFileSync(
  outputPath,
  `// Generated by scripts/generate-api-read-model.mjs. Do not edit by hand.\nexport const apiReadModel = ${JSON.stringify(readModel, null, 2)};\nexport default apiReadModel;\n`
);

console.log(
  JSON.stringify({
    ok: true,
    outputPath,
    rounds: readModel.rounds.length,
    models: readModel.models.length,
    assets: readModel.assets.length,
    allocations: readModel.allocations.length,
    results: readModel.results.length
  })
);
