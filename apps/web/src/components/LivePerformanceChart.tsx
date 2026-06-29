import { Activity, BarChart3 } from "lucide-react";
import { useMemo, useState } from "react";
import type { CSSProperties } from "react";
import { modelLabel, providerLabel } from "../data/fallback";
import { pct } from "../lib/format";
import { providerLogoSrc } from "../lib/scoreReturnChart";
import type { LivePerformanceRecord } from "../lib/localRoundRecords";

type TrackFilter = "all" | "weekly" | "monthly";

type LiveModelRow = {
  modelId: string;
  provider: string;
  label: string;
  logoSrc?: string;
  returnValue: number;
  sp500Value: number;
  alphaValue: number;
  liveRoundCount: number;
  latestPriceDate: string;
  tracks: Set<string>;
};

type ChartRow = {
  key: string;
  kind: "model" | "benchmark";
  label: string;
  provider?: string;
  logoSrc?: string;
  returnValue: number;
  sp500Value: number;
  alphaValue?: number;
  liveRoundCount: number;
  latestPriceDate: string;
  barClass: string;
};

interface Props {
  rows: LivePerformanceRecord[];
  openRoundCounts: Record<TrackFilter, number>;
}

const TRACKS: Array<{ key: TrackFilter; label: string }> = [
  { key: "all", label: "All Live" },
  { key: "monthly", label: "Monthly" },
  { key: "weekly", label: "Weekly" }
];

function finite(value: number | null | undefined): value is number {
  return typeof value === "number" && Number.isFinite(value);
}

function average(values: number[]): number {
  return values.length ? values.reduce((total, value) => total + value, 0) / values.length : 0;
}

function signedPct(value: number): string {
  const formatted = pct(value) || "0.00%";
  return value > 0 ? `+${formatted}` : formatted;
}

function shortDate(value: string): string {
  if (!value) return "n/a";
  const [year, month, day] = value.slice(0, 10).split("-").map(Number);
  if (!year || !month || !day) return value.slice(0, 10);
  return new Intl.DateTimeFormat("en-US", { month: "short", day: "numeric", timeZone: "UTC" }).format(
    new Date(Date.UTC(year, month - 1, day))
  );
}

function usableRows(rows: LivePerformanceRecord[], track: TrackFilter): LivePerformanceRecord[] {
  const latestByKey = new Map<string, LivePerformanceRecord>();
  for (const row of rows) {
    if (track !== "all" && row.track !== track) continue;
    if (row.status !== "pending") continue;
    if (row.published === false) continue;
    if (!finite(row.model_return) || !finite(row.sp500_return) || !finite(row.alpha_vs_sp500)) continue;
    if (row.days_elapsed <= 0 || row.target_date <= row.entry_date || row.target_date >= row.exit_date) continue;
    const key = `${row.round_id}:${row.run_id}:${row.model_id}`;
    const existing = latestByKey.get(key);
    if (!existing || row.target_date > existing.target_date || (row.target_date === existing.target_date && row.price_date > existing.price_date)) {
      latestByKey.set(key, row);
    }
  }
  return Array.from(latestByKey.values());
}

function modelColorClass(modelId: string, index: number): string {
  const colors: Record<string, string> = {
    "openai-gpt-5-5": "live-bar-openai",
    "xai-grok-4-3": "live-bar-xai",
    "anthropic-claude-fable-5": "live-bar-anthropic-fable",
    "anthropic-claude-opus-4-7": "live-bar-anthropic",
    "anthropic-claude-opus-4-8": "live-bar-anthropic-alt",
    "google-gemini-3-1-pro": "live-bar-google"
  };
  return colors[modelId] ?? `live-bar-model-${(index % 6) + 1}`;
}

function buildChartRows(rows: LivePerformanceRecord[]): ChartRow[] {
  const modelGroups = new Map<string, LiveModelRow & { returnValues: number[]; sp500Values: number[]; alphaValues: number[]; roundIds: Set<string> }>();
  const benchmarkByRound = new Map<string, LivePerformanceRecord>();
  for (const row of rows) {
    const existing =
      modelGroups.get(row.model_id) ??
      ({
        modelId: row.model_id,
        provider: row.provider,
        label: modelLabel(row.model_id),
        logoSrc: providerLogoSrc(row.provider),
        returnValue: 0,
        sp500Value: 0,
        alphaValue: 0,
        returnValues: [],
        sp500Values: [],
        alphaValues: [],
        liveRoundCount: 0,
        roundIds: new Set<string>(),
        latestPriceDate: "",
        tracks: new Set<string>()
      } satisfies LiveModelRow & { returnValues: number[]; sp500Values: number[]; alphaValues: number[]; roundIds: Set<string> });
    existing.returnValues.push(row.model_return);
    existing.sp500Values.push(row.sp500_return);
    existing.alphaValues.push(row.alpha_vs_sp500);
    existing.roundIds.add(row.round_id);
    existing.latestPriceDate = row.price_date > existing.latestPriceDate ? row.price_date : existing.latestPriceDate;
    existing.tracks.add(row.track);
    modelGroups.set(row.model_id, existing);

    const roundKey = `${row.round_id}:${row.run_id}`;
    const benchmark = benchmarkByRound.get(roundKey);
    if (!benchmark || row.target_date > benchmark.target_date) benchmarkByRound.set(roundKey, row);
  }

  const modelRows = Array.from(modelGroups.values())
    .map((row) => ({
      key: row.modelId,
      kind: "model" as const,
      label: row.label,
      provider: row.provider,
      logoSrc: row.logoSrc,
      returnValue: average(row.returnValues),
      sp500Value: average(row.sp500Values),
      alphaValue: average(row.alphaValues),
      liveRoundCount: row.roundIds.size,
      latestPriceDate: row.latestPriceDate,
      barClass: ""
    }))
    .sort((a, b) => b.returnValue - a.returnValue || b.alphaValue - a.alphaValue || a.label.localeCompare(b.label))
    .map((row, index) => ({ ...row, barClass: modelColorClass(row.key, index) }));

  const benchmarkRows = Array.from(benchmarkByRound.values());
  const benchmark: ChartRow | null = benchmarkRows.length
    ? {
        key: "sp500",
        kind: "benchmark",
        label: "S&P 500",
        returnValue: average(benchmarkRows.map((row) => row.sp500_return)),
        sp500Value: average(benchmarkRows.map((row) => row.sp500_return)),
        liveRoundCount: benchmarkRows.length,
        latestPriceDate: benchmarkRows.reduce((latest, row) => (row.price_date > latest ? row.price_date : latest), ""),
        barClass: "live-bar-benchmark"
      }
    : null;

  return benchmark ? [...modelRows, benchmark] : modelRows;
}

function barStyle(value: number, domainMin: number, domainMax: number): CSSProperties {
  const range = Math.max(0.0001, domainMax - domainMin);
  const point = (input: number) => ((input - domainMin) / range) * 100;
  const zero = point(0);
  const end = point(value);
  const left = Math.min(zero, end);
  const width = Math.max(1.5, Math.abs(end - zero));
  return {
    "--live-bar-left": `${left.toFixed(2)}%`,
    "--live-bar-width": `${width.toFixed(2)}%`,
    "--live-zero-left": `${zero.toFixed(2)}%`
  } as CSSProperties;
}

function axisStyle(domainMin: number, domainMax: number): CSSProperties {
  const range = Math.max(0.0001, domainMax - domainMin);
  const zero = ((0 - domainMin) / range) * 100;
  const clampedZero = Math.min(100, Math.max(0, zero));
  return {
    "--live-axis-zero-left": `${clampedZero.toFixed(2)}%`
  } as CSSProperties;
}

export default function LivePerformanceChart({ rows, openRoundCounts }: Props) {
  const [track, setTrack] = useState<TrackFilter>("all");
  const latestRows = useMemo(() => usableRows(rows, track), [rows, track]);
  const chartRows = useMemo(() => buildChartRows(latestRows), [latestRows]);
  const values = chartRows.map((row) => row.returnValue);
  const rawMin = Math.min(0, ...values);
  const rawMax = Math.max(0, ...values);
  const padding = Math.max((rawMax - rawMin) * 0.12, 0.004);
  const domainMin = rawMin < 0 ? rawMin - padding : 0;
  const domainMax = rawMax > 0 ? rawMax + padding : padding;
  const latestPriceDate = latestRows.reduce((latest, row) => (row.price_date > latest ? row.price_date : latest), "");
  const openRoundCount = new Set(latestRows.map((row) => row.round_id)).size;
  const totalOpenRoundCount = openRoundCounts[track];
  const nextFinalDate = latestRows
    .map((row) => row.exit_date)
    .filter((date) => !latestPriceDate || date > latestPriceDate)
    .filter(Boolean)
    .sort()[0];

  return (
    <section className="live-performance-panel" aria-label="Live mark-to-market returns for live rounds">
      <div className="live-performance-head">
        <div>
          <span className="panel-kicker">Live tests</span>
          <h3>Live Portfolio Returns</h3>
          <p>Live rounds marked to the latest available close. These are not final scores.</p>
        </div>
        <div className="live-performance-tabs" role="tablist" aria-label="Live performance track filter">
          {TRACKS.map((item) => (
            <button
              key={item.key}
              type="button"
              className={track === item.key ? "is-active" : ""}
              aria-pressed={track === item.key}
              onClick={() => setTrack(item.key)}
            >
              {item.label}
            </button>
          ))}
        </div>
      </div>

      <div className="live-performance-stats" aria-label="Live performance context">
        <div>
          <span>Priced live rounds</span>
          <strong>{openRoundCount} of {totalOpenRoundCount}</strong>
        </div>
        <div>
          <span>Latest close</span>
          <strong>{shortDate(latestPriceDate)}</strong>
        </div>
        <div>
          <span>Next final score</span>
          <strong>{shortDate(nextFinalDate)}</strong>
        </div>
      </div>

      {chartRows.length > 0 ? (
        <div className="live-performance-chart">
          <div className="live-performance-axis" aria-hidden="true">
            <div className="live-performance-axis-scale" style={axisStyle(domainMin, domainMax)}>
              <span>{signedPct(domainMin)}</span>
              <span>0%</span>
              <span>{signedPct(domainMax)}</span>
            </div>
          </div>
          <div className="live-performance-bars">
            {chartRows.map((row) => (
              <article className={`live-performance-row live-performance-row-${row.kind}`} key={row.key}>
                <div className="live-performance-model">
                  {row.logoSrc ? (
                    <span className="live-performance-logo">
                      <img src={row.logoSrc} alt={providerLabel(row.provider ?? "")} width="36" height="36" loading="lazy" />
                    </span>
                  ) : (
                    <span className="live-performance-benchmark-chip" aria-hidden="true">S&amp;P</span>
                  )}
                  <span>
                    <strong>{row.label}</strong>
                    <small>
                      {row.kind === "benchmark"
                        ? `${row.liveRoundCount} open test${row.liveRoundCount === 1 ? "" : "s"}`
                        : `${providerLabel(row.provider ?? "")} / ${row.liveRoundCount} open`}
                    </small>
                  </span>
                </div>
                <div className="live-performance-track" style={barStyle(row.returnValue, domainMin, domainMax)} aria-hidden="true">
                  <span className="live-performance-zero"></span>
                  <span className={`live-performance-fill ${row.barClass}`}></span>
                </div>
                <div className="live-performance-value">
                  <span>
                    <em>{row.kind === "benchmark" ? "S&P 500 return" : "Portfolio"}</em>
                    <strong>{signedPct(row.returnValue)}</strong>
                  </span>
                  {row.kind === "model" ? (
                    <>
                      <span>
                        <em>S&P 500</em>
                        <strong>{signedPct(row.sp500Value)}</strong>
                      </span>
                      <span>
                        <em>Portfolio Minus S&P 500</em>
                        <strong className={(row.alphaValue ?? 0) >= 0 ? "positive" : "negative"}>{signedPct(row.alphaValue ?? 0)}</strong>
                      </span>
                    </>
                  ) : (
                    <span>
                      <em>Close</em>
                      <strong>{shortDate(row.latestPriceDate)}</strong>
                    </span>
                  )}
                </div>
              </article>
            ))}
          </div>
          <p className="live-performance-note">
            Interim returns use live rounds only. Completed rounds move to official scored results.
          </p>
        </div>
      ) : (
        <div className="live-performance-empty">
          <Activity size={20} aria-hidden="true" />
          <div>
            <strong>No live price snapshot yet</strong>
            <p>After the first close inside an open test window, live returns will appear here.</p>
          </div>
        </div>
      )}
      <div className="live-performance-foot">
        <BarChart3 size={17} aria-hidden="true" />
        <span>Marked to market from saved entry prices. Official results wait for the scheduled ending close.</span>
      </div>
    </section>
  );
}
