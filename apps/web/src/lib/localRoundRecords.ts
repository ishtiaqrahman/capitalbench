import { existsSync, readdirSync, readFileSync } from "node:fs";
import { join, resolve } from "node:path";
import { parse as parseYaml } from "yaml";
import {
  rounds,
  type EntryPrice,
  type LeaderboardRecord,
  type RoundRecord,
  type ScoreEtaSource,
  type SubmissionRecord,
  type UniverseOption,
  type WeeklyPerformanceRecord
} from "../data/fallback";
import { roundTrack, type BenchmarkTrack } from "./tracks";

type RoundManifestYaml = {
  round_id: string;
  title?: string;
  description?: string;
  decision_date?: string;
  decision_deadline?: string;
  horizon?: string;
  entry_date?: string;
  exit_date?: string;
  methodology_version?: string;
  universe_version?: string;
  submission_format?: "single_pick" | "portfolio";
  notes?: string;
};

type RunManifestYaml = {
  run_id?: string;
  run_type?: string;
  official_score_eligible?: boolean;
  operator_selected_official?: boolean;
  methodology_version?: string;
  invalid_submissions?: number;
};

type ResolutionJobYaml = {
  due_at_utc?: string;
  next_attempt_at_utc?: string;
  status?: string;
};

type ParsedSubmissionJson = {
  round_id?: string;
  model_id?: string;
  provider?: string;
  mode?: string;
  run_type?: string;
  replicate_index?: number;
  replicate_count?: number;
  selected_option_id?: string;
  portfolio?: Array<{
    option_id?: string;
    allocation_pct?: number;
    allocation_bps?: number;
    rationale?: string;
  }>;
  portfolio_rationale?: string;
  confidence?: number;
  rationale_summary?: string;
  key_risks?: string[];
};

type OptionYaml = {
  id?: string;
  option_id?: string;
  name?: string;
  label?: string;
  symbol?: string;
  asset_symbol?: string;
  asset_class?: string;
  category?: string;
  option_group?: string;
  risk_bucket?: string;
  is_cash?: boolean;
  is_benchmark?: boolean;
  include_in_universe?: boolean;
};

export interface ResultReturnRecord {
  option_id: string;
  label: string;
  asset_symbol: string;
  entry_price: number;
  exit_price: number;
  entry_price_source: string;
  exit_price_source: string;
  return: number;
  rank: number;
  is_benchmark: boolean;
  is_cash: boolean;
}

export interface ResultAllocationRecord {
  round_id: string;
  model_id: string;
  provider: string;
  option_id: string;
  allocation_bps: number;
  allocation_pct: number;
  allocation_rank: number;
  option_return: number;
  return_contribution: number;
  rationale: string;
}

export interface ScoringPriceRecord {
  option_id: string;
  symbol: string;
  entry_date: string;
  entry_price: number;
  exit_date?: string;
  exit_price?: number;
  return?: number;
  source: string;
}

export type LivePerformanceRecord = WeeklyPerformanceRecord & {
  track: BenchmarkTrack;
  status: RoundRecord["status"];
  entry_date: string;
  exit_date: string;
};

function readYamlFile<T>(path: string): T | null {
  if (!existsSync(path)) return null;
  try {
    return parseYaml(readFileSync(path, "utf-8")) as T;
  } catch {
    return null;
  }
}

function readJsonFile<T>(path: string): T | null {
  if (!existsSync(path)) return null;
  try {
    return JSON.parse(readFileSync(path, "utf-8")) as T;
  } catch {
    return null;
  }
}

function readTextFile(path: string): string {
  if (!existsSync(path)) return "";
  return readFileSync(path, "utf-8").trim();
}

function parseCsvLine(line: string): string[] {
  const cells: string[] = [];
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

function parseCsv(text: string): Array<Record<string, string>> {
  const lines = text.trim().split(/\r?\n/).filter(Boolean);
  const [headerLine, ...rowLines] = lines;
  if (!headerLine) return [];
  const headers = parseCsvLine(headerLine);
  return rowLines.map((line) => {
    const cells = parseCsvLine(line);
    return Object.fromEntries(headers.map((header, index) => [header, cells[index] ?? ""]));
  });
}

function numberFromCell(value: string | undefined): number | undefined {
  if (value === undefined || value === "") return undefined;
  const numeric = Number(value);
  return Number.isFinite(numeric) ? numeric : undefined;
}

function booleanFromCell(value: string | undefined): boolean {
  return String(value ?? "").toLowerCase() === "true";
}

function priceValue(row: Record<string, string>): number | undefined {
  for (const key of ["price", "adj_close", "adjClose", "close", "entry_price"]) {
    const value = numberFromCell(row[key]);
    if (value !== undefined) return value;
  }
  return undefined;
}

function publicOfficialRuns(roundPath: string): Array<{ runId: string; manifest: RunManifestYaml }> {
  const runsPath = join(roundPath, "runs");
  if (!existsSync(runsPath)) return [];
  return readdirSync(runsPath)
    .map((runId) => ({
      runId,
      manifest: readYamlFile<RunManifestYaml>(join(runsPath, runId, "run_manifest.yaml"))
    }))
    .filter((item): item is { runId: string; manifest: RunManifestYaml } => {
      return (
        item.manifest !== null &&
        item.manifest.run_type === "official" &&
        item.manifest.official_score_eligible === true &&
        Number(item.manifest.invalid_submissions ?? 0) === 0
      );
    })
    .sort((a, b) => {
      if (a.manifest.operator_selected_official && !b.manifest.operator_selected_official) return -1;
      if (!a.manifest.operator_selected_official && b.manifest.operator_selected_official) return 1;
      return a.runId.localeCompare(b.runId);
    });
}

function horizonDays(entryDate?: string, exitDate?: string): number {
  if (!entryDate || !exitDate) return 0;
  const start = Date.parse(`${entryDate}T00:00:00Z`);
  const end = Date.parse(`${exitDate}T00:00:00Z`);
  if (!Number.isFinite(start) || !Number.isFinite(end)) return 0;
  return Math.round((end - start) / 86_400_000);
}

function validIsoDateTime(value?: string): string | undefined {
  if (!value) return undefined;
  return Number.isFinite(Date.parse(value)) ? value : undefined;
}

function scoreEta(roundPath: string, manifest: RoundManifestYaml): { score_eta_utc?: string; score_eta_source?: ScoreEtaSource } {
  const job = readYamlFile<ResolutionJobYaml>(join(roundPath, "automation", "resolution_job.yaml"));
  const automationEta = validIsoDateTime(job?.due_at_utc ?? job?.next_attempt_at_utc);
  if (automationEta) {
    return { score_eta_utc: automationEta, score_eta_source: "automation" };
  }
  const derivedEta = validIsoDateTime(manifest.exit_date ? `${manifest.exit_date}T23:30:00Z` : undefined);
  if (derivedEta) {
    return { score_eta_utc: derivedEta, score_eta_source: "derived" };
  }
  return {};
}

function discoverRoundRecord(roundPath: string): RoundRecord | null {
  const manifest = readYamlFile<RoundManifestYaml>(join(roundPath, "manifest.yaml"));
  if (!manifest?.round_id) return null;
  const fallback = rounds.find((item) => item.round_id === manifest.round_id);
  const entryDate = manifest.entry_date ?? fallback?.entry_date ?? "";
  const exitDate = manifest.exit_date ?? fallback?.exit_date ?? "";
  const manifestHorizonDays = horizonDays(entryDate, exitDate);
  const selectedRun = publicOfficialRuns(roundPath)[0];
  const hasScoredResults =
    selectedRun !== undefined &&
    existsSync(join(roundPath, "runs", selectedRun.runId, "results", "leaderboard.csv"));
  const scoreEtaFields = scoreEta(roundPath, manifest);
  return {
    round_id: manifest.round_id,
    title: manifest.title ?? fallback?.title ?? manifest.round_id,
    description: manifest.description ?? fallback?.description ?? "CapitalBench benchmark round.",
    decision_date: manifest.decision_date ?? fallback?.decision_date ?? "",
    decision_deadline_utc: manifest.decision_deadline ?? fallback?.decision_deadline_utc ?? "",
    horizon: manifest.horizon ?? fallback?.horizon ?? "one month",
    horizon_days: manifestHorizonDays || fallback?.horizon_days || 0,
    entry_date: entryDate,
    exit_date: exitDate,
    status: hasScoredResults ? "resolved" : fallback?.status ?? "pending",
    methodology_version:
      selectedRun?.manifest.methodology_version ??
      manifest.methodology_version ??
      fallback?.methodology_version ??
      "",
    universe_version: manifest.universe_version ?? fallback?.universe_version,
    submission_format: manifest.submission_format ?? fallback?.submission_format ?? "single_pick",
    official_run_id: selectedRun?.runId ?? fallback?.official_run_id ?? "",
    stability_run_id: fallback?.stability_run_id,
    score_eta_utc: hasScoredResults ? undefined : scoreEtaFields.score_eta_utc ?? fallback?.score_eta_utc,
    score_eta_source: hasScoredResults ? undefined : scoreEtaFields.score_eta_source ?? fallback?.score_eta_source,
    notes: manifest.notes ?? fallback?.notes ?? ""
  };
}

export function staticRoundRecords(): RoundRecord[] {
  const byId = new Map(rounds.map((round) => [round.round_id, round]));
  const roundsRoot = join(repoRootPath(), "rounds");
  if (existsSync(roundsRoot)) {
    for (const entry of readdirSync(roundsRoot, { withFileTypes: true })) {
      if (!entry.isDirectory() || !entry.name.startsWith("CB-")) continue;
      const record = discoverRoundRecord(join(roundsRoot, entry.name));
      if (record) byId.set(record.round_id, record);
    }
  }
  return Array.from(byId.values()).sort((a, b) => b.decision_deadline_utc.localeCompare(a.decision_deadline_utc));
}

function roundPathForId(roundId: string): string | null {
  const roundsRoot = join(repoRootPath(), "rounds");
  const directPath = join(roundsRoot, roundId);
  if (existsSync(directPath)) return directPath;
  return null;
}

function primaryOptionId(payload: ParsedSubmissionJson): string {
  if (payload.selected_option_id) return payload.selected_option_id;
  const allocations = payload.portfolio ?? [];
  const [primary] = [...allocations].sort((a, b) => {
    const bpsA = a.allocation_bps ?? Number(a.allocation_pct ?? 0) * 100;
    const bpsB = b.allocation_bps ?? Number(b.allocation_pct ?? 0) * 100;
    return bpsB - bpsA;
  });
  return primary?.option_id ?? "";
}

function normalizeSubmission(
  payload: ParsedSubmissionJson,
  fallback: { fallbackRoundId: string; fallbackRunId: string }
): SubmissionRecord | null {
  if (!payload.model_id || !payload.provider) return null;
  const portfolio = (payload.portfolio ?? [])
    .filter((item) => item.option_id)
    .map((item) => ({
      option_id: String(item.option_id),
      allocation_pct:
        typeof item.allocation_pct === "number"
          ? item.allocation_pct
          : typeof item.allocation_bps === "number"
            ? item.allocation_bps / 100
            : undefined,
      allocation_bps:
        typeof item.allocation_bps === "number"
          ? item.allocation_bps
          : typeof item.allocation_pct === "number"
            ? item.allocation_pct * 100
            : undefined,
      rationale: item.rationale ? String(item.rationale) : undefined
    }));
  return {
    round_id: payload.round_id ?? fallback.fallbackRoundId,
    run_id: fallback.fallbackRunId,
    model_id: payload.model_id,
    provider: payload.provider,
    submission_format: portfolio.length > 0 ? "portfolio" : "single_pick",
    selected_option_id: primaryOptionId(payload),
    holding_count: portfolio.length > 0 ? portfolio.length : 1,
    max_allocation_bps:
      portfolio.length > 0
        ? Math.max(...portfolio.map((item) => item.allocation_bps ?? Number(item.allocation_pct ?? 0) * 100))
        : 10000,
    cash_allocation_bps: portfolio
      .filter((item) => item.option_id.toUpperCase() === "CASH")
      .reduce((total, item) => total + (item.allocation_bps ?? Number(item.allocation_pct ?? 0) * 100), 0),
    benchmark_allocation_bps: portfolio
      .filter((item) => item.option_id.toUpperCase() === "SP500")
      .reduce((total, item) => total + (item.allocation_bps ?? Number(item.allocation_pct ?? 0) * 100), 0),
    portfolio,
    portfolio_rationale: payload.portfolio_rationale,
    confidence: Number(payload.confidence ?? 0),
    rationale_summary: payload.rationale_summary ?? "",
    key_risks: Array.isArray(payload.key_risks) ? payload.key_risks : []
  };
}

export function staticOfficialSubmissions(roundId: string, runId?: string): SubmissionRecord[] {
  const roundPath = roundPathForId(roundId);
  if (!roundPath) return [];
  const selectedRunId = runId || publicOfficialRuns(roundPath)[0]?.runId;
  if (!selectedRunId) return [];
  const parsedPath = join(roundPath, "runs", selectedRunId, "submissions", "parsed");
  if (!existsSync(parsedPath)) return [];
  return readdirSync(parsedPath)
    .filter((filename) => filename.endsWith(".json"))
    .map((filename) =>
      normalizeSubmission(readJsonFile<ParsedSubmissionJson>(join(parsedPath, filename)) ?? {}, {
        fallbackRoundId: roundId,
        fallbackRunId: selectedRunId
      })
    )
    .filter((item): item is SubmissionRecord => item !== null)
    .sort((a, b) => a.provider.localeCompare(b.provider));
}

export function staticAllOfficialSubmissions(roundRows = staticRoundRecords()): SubmissionRecord[] {
  return roundRows.flatMap((round) => staticOfficialSubmissions(round.round_id, round.official_run_id));
}

export function staticUniverseOptions(roundId: string): UniverseOption[] {
  const roundPath = roundPathForId(roundId);
  if (!roundPath) return [];
  const yaml = readYamlFile<{ options?: OptionYaml[] }>(join(roundPath, "options.yaml"));
  const options = Array.isArray(yaml?.options) ? yaml.options : [];
  return options
    .filter((option) => option.include_in_universe !== false)
    .map((option, index) => ({
      option_id: String(option.id ?? option.option_id ?? ""),
      name: String(option.name ?? option.label ?? option.id ?? option.option_id ?? ""),
      symbol: String(option.symbol ?? option.asset_symbol ?? ""),
      asset_class: String(option.asset_class ?? "unknown"),
      option_group: String(option.option_group ?? option.category ?? "unknown"),
      risk_bucket: String(option.risk_bucket ?? "medium"),
      is_cash: Boolean(option.is_cash),
      is_benchmark: Boolean(option.is_benchmark),
      sort_order: index + 1
    }))
    .filter((option) => option.option_id);
}

export function staticEntryPrices(roundId: string): EntryPrice[] {
  const roundPath = roundPathForId(roundId);
  if (!roundPath) return [];
  return parseCsv(readTextFile(join(roundPath, "prices", "entry_prices.csv")))
    .map((row) => {
      const price = priceValue(row);
      if (!row.option_id || price === undefined) return null;
      return {
        option_id: row.option_id,
        symbol: row.symbol ?? "",
        date: row.date ?? "",
        price,
        source: row.source || (row.adj_close ? "adj_close" : row.close ? "close" : "")
      };
    })
    .filter((row): row is EntryPrice => row !== null);
}

export function staticExitPrices(roundId: string): EntryPrice[] {
  const roundPath = roundPathForId(roundId);
  if (!roundPath) return [];
  return parseCsv(readTextFile(join(roundPath, "prices", "exit_prices.csv")))
    .map((row) => {
      const price = priceValue(row);
      if (!row.option_id || price === undefined) return null;
      return {
        option_id: row.option_id,
        symbol: row.symbol ?? "",
        date: row.date ?? "",
        price,
        source: row.source || (row.adj_close ? "adj_close" : row.close ? "close" : "")
      };
    })
    .filter((row): row is EntryPrice => row !== null);
}

export function staticRoundLeaderboard(roundId: string, runId?: string): LeaderboardRecord[] {
  const roundPath = roundPathForId(roundId);
  if (!roundPath) return [];
  const selectedRunId = runId || publicOfficialRuns(roundPath)[0]?.runId;
  if (!selectedRunId) return [];
  return parseCsv(readTextFile(join(roundPath, "runs", selectedRunId, "results", "leaderboard.csv")))
    .map((row) => ({
      round_id: row.round_id || roundId,
      run_id: selectedRunId,
      model_id: row.model_id,
      provider: row.provider,
      mode: row.mode,
      selected_option_id: row.selected_option_id,
      submission_format: row.submission_format === "portfolio" ? ("portfolio" as const) : ("single_pick" as const),
      holding_count: numberFromCell(row.holding_count),
      portfolio_return: numberFromCell(row.portfolio_return),
      selected_asset_return: numberFromCell(row.selected_asset_return),
      sp500_return: numberFromCell(row.sp500_return),
      alpha_vs_sp500: numberFromCell(row.alpha_vs_sp500),
      regret_vs_best_option: numberFromCell(row.regret_vs_best_option),
      rank_among_options: numberFromCell(row.rank_among_options),
      max_allocation_bps: numberFromCell(row.max_allocation_bps),
      cash_allocation_bps: numberFromCell(row.cash_allocation_bps),
      benchmark_allocation_bps: numberFromCell(row.benchmark_allocation_bps),
      concentration_hhi: numberFromCell(row.concentration_hhi),
      confidence: numberFromCell(row.confidence)
    }))
    .filter((row) => Boolean(row.model_id && row.provider))
    .sort((a, b) => Number(b.alpha_vs_sp500 ?? -Infinity) - Number(a.alpha_vs_sp500 ?? -Infinity));
}

export function staticRoundReturns(roundId: string, runId?: string): ResultReturnRecord[] {
  const roundPath = roundPathForId(roundId);
  if (!roundPath) return [];
  const selectedRunId = runId || publicOfficialRuns(roundPath)[0]?.runId;
  if (!selectedRunId) return [];
  return parseCsv(readTextFile(join(roundPath, "runs", selectedRunId, "results", "returns.csv")))
    .map((row) => {
      const entryPrice = numberFromCell(row.entry_price);
      const exitPrice = numberFromCell(row.exit_price);
      const resultReturn = numberFromCell(row.return);
      const rank = numberFromCell(row.rank);
      if (!row.option_id || entryPrice === undefined || exitPrice === undefined || resultReturn === undefined || rank === undefined) {
        return null;
      }
      return {
        option_id: row.option_id,
        label: row.label || row.option_id,
        asset_symbol: row.asset_symbol || "",
        entry_price: entryPrice,
        exit_price: exitPrice,
        entry_price_source: row.entry_price_source || "",
        exit_price_source: row.exit_price_source || "",
        return: resultReturn,
        rank,
        is_benchmark: booleanFromCell(row.is_benchmark),
        is_cash: booleanFromCell(row.is_cash)
      };
    })
    .filter((row): row is ResultReturnRecord => row !== null)
    .sort((a, b) => a.rank - b.rank);
}

export function staticRoundAllocations(roundId: string, runId?: string): ResultAllocationRecord[] {
  const roundPath = roundPathForId(roundId);
  if (!roundPath) return [];
  const selectedRunId = runId || publicOfficialRuns(roundPath)[0]?.runId;
  if (!selectedRunId) return [];
  return parseCsv(readTextFile(join(roundPath, "runs", selectedRunId, "results", "allocations.csv")))
    .map((row) => {
      const allocationBps = numberFromCell(row.allocation_bps);
      const allocationPct = numberFromCell(row.allocation_pct);
      const allocationRank = numberFromCell(row.allocation_rank);
      const optionReturn = numberFromCell(row.option_return);
      const returnContribution = numberFromCell(row.return_contribution);
      if (
        !row.round_id ||
        !row.model_id ||
        !row.provider ||
        !row.option_id ||
        allocationBps === undefined ||
        allocationPct === undefined ||
        allocationRank === undefined ||
        optionReturn === undefined ||
        returnContribution === undefined
      ) {
        return null;
      }
      return {
        round_id: row.round_id,
        model_id: row.model_id,
        provider: row.provider,
        option_id: row.option_id,
        allocation_bps: allocationBps,
        allocation_pct: allocationPct,
        allocation_rank: allocationRank,
        option_return: optionReturn,
        return_contribution: returnContribution,
        rationale: row.rationale || ""
      };
    })
    .filter((row): row is ResultAllocationRecord => row !== null)
    .sort((a, b) => a.model_id.localeCompare(b.model_id) || a.allocation_rank - b.allocation_rank);
}

export function staticRoundWeeklyPerformance(roundId: string, runId?: string): LivePerformanceRecord[] {
  const round = staticRoundRecords().find((item) => item.round_id === roundId);
  const track = round ? roundTrack(round) : "other";
  if (!round || (track !== "weekly" && track !== "monthly")) return [];
  const roundPath = roundPathForId(roundId);
  if (!roundPath) return [];
  const selectedRunId = runId || publicOfficialRuns(roundPath)[0]?.runId;
  if (!selectedRunId) return [];
  return parseCsv(readTextFile(join(roundPath, "runs", selectedRunId, "results", "weekly_performance.csv")))
    .map((row): LivePerformanceRecord | null => {
      const daysElapsed = numberFromCell(row.days_elapsed);
      const modelReturn = numberFromCell(row.model_return);
      const sp500Return = numberFromCell(row.sp500_return);
      const alpha = numberFromCell(row.alpha_vs_sp500);
      if (
        !row.round_id ||
        !row.model_id ||
        !row.provider ||
        !row.target_date ||
        daysElapsed === undefined ||
        modelReturn === undefined ||
        sp500Return === undefined ||
        alpha === undefined
      ) {
        return null;
      }
      return {
        round_id: row.round_id || roundId,
        run_id: row.run_id || selectedRunId,
        model_id: row.model_id,
        provider: row.provider,
        target_date: row.target_date,
        price_date: row.price_date || row.target_date,
        days_elapsed: daysElapsed,
        run_type: row.run_type || undefined,
        submission_format: row.submission_format === "portfolio" ? ("portfolio" as const) : ("single_pick" as const),
        selected_option_id: row.selected_option_id || "",
        holding_count: numberFromCell(row.holding_count),
        model_return: modelReturn,
        sp500_return: sp500Return,
        alpha_vs_sp500: alpha,
        price_status: row.price_status || undefined,
        published: booleanFromCell(row.published),
        track,
        status: round.status,
        entry_date: round.entry_date,
        exit_date: round.exit_date
      };
    })
    .filter((row): row is LivePerformanceRecord => row !== null)
    .sort((a, b) => a.target_date.localeCompare(b.target_date) || a.model_id.localeCompare(b.model_id));
}

export function staticAllWeeklyPerformance(roundRows = staticRoundRecords()): LivePerformanceRecord[] {
  return roundRows.flatMap((round) => staticRoundWeeklyPerformance(round.round_id, round.official_run_id));
}

export function staticScoringPrices(roundId: string, runId?: string): ScoringPriceRecord[] {
  const resultReturns = staticRoundReturns(roundId, runId);
  if (resultReturns.length > 0) {
    const entries = staticEntryPrices(roundId);
    const exits = staticExitPrices(roundId);
    const entryById = Object.fromEntries(entries.map((entry) => [entry.option_id, entry]));
    const exitById = Object.fromEntries(exits.map((exit) => [exit.option_id, exit]));
    return resultReturns.map((row) => ({
      option_id: row.option_id,
      symbol: row.asset_symbol,
      entry_date: entryById[row.option_id]?.date ?? "",
      entry_price: row.entry_price,
      exit_date: exitById[row.option_id]?.date,
      exit_price: row.exit_price,
      return: row.return,
      source: row.exit_price_source || row.entry_price_source
    }));
  }
  return staticEntryPrices(roundId).map((row) => ({
    option_id: row.option_id,
    symbol: row.symbol,
    entry_date: row.date,
    entry_price: row.price,
    source: row.source
  }));
}

export function repoRootPath(): string {
  const candidates = [resolve(process.cwd()), resolve(process.cwd(), "../..")];
  return (
    candidates.find((candidate) => existsSync(join(candidate, "configs")) && existsSync(join(candidate, "rounds"))) ??
    resolve(process.cwd(), "../..")
  );
}
