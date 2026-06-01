import { existsSync, mkdirSync, readdirSync, readFileSync, writeFileSync } from "node:fs";
import { join, resolve } from "node:path";
import { parse as parseYaml } from "yaml";

const repoRoot = resolve(process.cwd(), "../..");
const roundsRoot = join(repoRoot, "rounds");
const outputPath = join(process.cwd(), "src", "generated", "apiReadModel.js");

const PROVIDER_LABELS = {
  anthropic: "Anthropic",
  google: "Google",
  openai: "OpenAI",
  xai: "xAI"
};

const MODEL_LABELS = {
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

const TECH_OPTION_IDS = new Set(["NASDAQ100", "LARGE_GROWTH", "TECHNOLOGY", "SEMICONDUCTORS", "SOFTWARE", "BROAD_AI_TECH", "CYBERSECURITY"]);
const DEFENSIVE_OPTION_IDS = new Set([
  "CASH",
  "SHORT_TREASURY",
  "INTERMEDIATE_TREASURY",
  "TIPS",
  "INVESTMENT_GRADE_CREDIT",
  "AGGREGATE_BONDS",
  "GOLD",
  "DIVIDEND",
  "LOW_VOL",
  "CONSUMER_STAPLES",
  "UTILITIES"
]);

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

function percentReturnValue(value) {
  const numeric = numberValue(value);
  return numeric === null ? null : numeric * 100;
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
        is_benchmark: Boolean(option.is_benchmark),
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

function riskScore(asset) {
  if (!asset) return 3;
  if (asset.is_cash) return 1;
  if (String(asset.asset_class).toLowerCase() === "crypto") return 5;
  switch (String(asset.risk_bucket).toLowerCase()) {
    case "cash":
      return 1;
    case "low":
      return 2;
    case "medium":
      return 3;
    case "high":
      return 4;
    case "very_high":
    case "very-high":
    case "speculative":
      return 5;
    default:
      return 3;
  }
}

function riskLabel(score) {
  if (score === null) return "Not enough history";
  if (score < 2.15) return "Defensive";
  if (score < 3.15) return "Balanced";
  if (score < 4.15) return "Growth";
  return "Aggressive";
}

function isDefensive(optionId, asset) {
  if (DEFENSIVE_OPTION_IDS.has(optionId)) return true;
  const category = String(asset?.category ?? "").toLowerCase();
  return category.includes("cash") || category.includes("bond") || category.includes("credit");
}

function isTechnology(optionId, asset) {
  if (TECH_OPTION_IDS.has(optionId)) return true;
  const category = String(asset?.category ?? "").toLowerCase();
  const label = String(asset?.label ?? "").toLowerCase();
  return category.includes("technology") || category.includes("ai") || label.includes("technology") || label.includes("software");
}

function loadRound(row) {
  const roundPath = join(roundsRoot, row.name);
  const manifest = readYaml(join(roundPath, "manifest.yaml"), {});
  if (!manifest.round_id) return null;
  const selectedRun = publicOfficialRuns(roundPath)[0];
  if (!selectedRun) return null;
  const resultsPath = join(roundPath, "runs", selectedRun.run_id, "results", "leaderboard.csv");
  const status = existsSync(resultsPath) ? "resolved" : "active";
  const entryDate = String(manifest.entry_date ?? "");
  const exitDate = String(manifest.exit_date ?? "");
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
    universe_version: manifest.universe_version ?? "",
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
      track: round.track,
      status: round.status,
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
  return rows
    .map((row, index) => ({
      round_id: row.round_id || round.round_id,
      run_id: selectedRun.run_id,
      track: round.track,
      model_id: row.model_id,
      provider: row.provider,
      rank: index + 1,
      selected_option_id: row.selected_option_id || "",
      submission_format: row.submission_format || "",
      holding_count: numberValue(row.holding_count),
      portfolio_return_pct: percentReturnValue(row.portfolio_return || row.selected_asset_return),
      selected_asset_return_pct: percentReturnValue(row.selected_asset_return),
      benchmark_return_pct: percentReturnValue(row.sp500_return),
      alpha_pp: percentReturnValue(row.alpha_vs_sp500),
      regret_vs_best_option_pct: percentReturnValue(row.regret_vs_best_option),
      rank_among_options: numberValue(row.rank_among_options),
      confidence: numberValue(row.confidence)
    }))
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
      is_benchmark: boolValue(row.is_benchmark),
      is_cash: boolValue(row.is_cash)
    }))
    .filter((row) => row.option_id);
}

function buildModelStyles(models, allocations, assetsById) {
  const styles = [];
  for (const model of models) {
    const rows = allocations.filter((row) => row.model_id === model.model_id);
    const portfolioKeys = new Set(rows.map((row) => `${row.round_id}:${row.run_id}:${row.model_id}`));
    let weightedRisk = 0;
    let totalPct = 0;
    let highRiskPct = 0;
    let defensivePct = 0;
    let techPct = 0;
    let cashPct = 0;
    let equityPct = 0;
    const categoryPct = new Map();
    for (const row of rows) {
      const asset = assetsById.get(row.option_id);
      weightedRisk += row.allocation_pct * riskScore(asset);
      totalPct += row.allocation_pct;
      if (riskScore(asset) >= 4) highRiskPct += row.allocation_pct;
      if (isDefensive(row.option_id, asset)) defensivePct += row.allocation_pct;
      if (isTechnology(row.option_id, asset)) techPct += row.allocation_pct;
      if (asset?.is_cash) cashPct += row.allocation_pct;
      if (String(asset?.asset_class ?? "").toLowerCase() === "equity") equityPct += row.allocation_pct;
      const category = asset?.category ?? row.category ?? "unknown";
      categoryPct.set(category, (categoryPct.get(category) ?? 0) + row.allocation_pct);
    }
    const score = totalPct > 0 ? weightedRisk / totalPct : null;
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
  const proof = [];

  for (const item of roundRows) {
    const loaded = loadSubmissions({ ...item, assetsById });
    item.round.model_count = new Set(loaded.portfolios.map((portfolio) => portfolio.model_id)).size;
    rounds.push(item.round);
    portfolios.push(...loaded.portfolios);
    allocations.push(...loaded.allocations);
    results.push(...loadResults(item));
    returns.push(...loadReturns(item));
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
  const assets = Array.from(assetsById.values()).sort((a, b) => Number(a.sort_order ?? 9999) - Number(b.sort_order ?? 9999) || a.label.localeCompare(b.label));
  const modelStyles = buildModelStyles(models, allocations, assetsById);

  return {
    generated_at: new Date().toISOString(),
    api_version: "v1",
    source: "capitalbench_local_rounds",
    current_universe_round_id: latestRoundWithOptions?.round.round_id ?? null,
    rounds,
    models,
    assets,
    portfolios,
    allocations,
    results,
    returns,
    model_styles: modelStyles,
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
