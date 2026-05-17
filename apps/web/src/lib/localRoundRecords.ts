import { existsSync, readdirSync, readFileSync } from "node:fs";
import { join, resolve } from "node:path";
import { parse as parseYaml } from "yaml";
import { rounds, type RoundRecord, type SubmissionRecord, type UniverseOption } from "../data/fallback";

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

function discoverRoundRecord(roundPath: string): RoundRecord | null {
  const manifest = readYamlFile<RoundManifestYaml>(join(roundPath, "manifest.yaml"));
  if (!manifest?.round_id) return null;
  const fallback = rounds.find((item) => item.round_id === manifest.round_id);
  const selectedRun = publicOfficialRuns(roundPath)[0];
  const hasScoredResults =
    selectedRun !== undefined &&
    existsSync(join(roundPath, "runs", selectedRun.runId, "results", "leaderboard.csv"));
  return {
    round_id: manifest.round_id,
    title: manifest.title ?? fallback?.title ?? manifest.round_id,
    description: manifest.description ?? fallback?.description ?? "CapitalBench benchmark round.",
    decision_date: manifest.decision_date ?? fallback?.decision_date ?? "",
    decision_deadline_utc: manifest.decision_deadline ?? fallback?.decision_deadline_utc ?? "",
    horizon: manifest.horizon ?? fallback?.horizon ?? "one month",
    horizon_days: fallback?.horizon_days ?? horizonDays(manifest.entry_date, manifest.exit_date),
    entry_date: manifest.entry_date ?? fallback?.entry_date ?? "",
    exit_date: manifest.exit_date ?? fallback?.exit_date ?? "",
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

export function repoRootPath(): string {
  const candidates = [resolve(process.cwd()), resolve(process.cwd(), "../..")];
  return (
    candidates.find((candidate) => existsSync(join(candidate, "configs")) && existsSync(join(candidate, "rounds"))) ??
    resolve(process.cwd(), "../..")
  );
}
