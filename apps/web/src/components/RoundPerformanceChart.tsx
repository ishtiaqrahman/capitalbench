import { Activity, Download } from "lucide-react";
import { useEffect, useMemo, useState } from "react";
import { modelLabel, providerLabel, type WeeklyPerformanceRecord } from "../data/fallback";
import { pct } from "../lib/format";
import { getSupabaseClient, hasSupabaseConfig } from "../lib/supabase";

interface Props {
  fallbackRows: WeeklyPerformanceRecord[];
  roundId: string;
  runId: string;
}

type ChartPoint = WeeklyPerformanceRecord & {
  model_return: number;
  sp500_return: number;
  alpha_vs_sp500: number;
  days_elapsed: number;
};

const palette = ["#006b5f", "#214f8f", "#a76600", "#5f3dc4", "#b42318", "#0b6f55", "#475569"];
const width = 780;
const height = 330;
const pad = { top: 24, right: 28, bottom: 42, left: 56 };

function numeric(value: number | string | null | undefined): number {
  const parsed = typeof value === "number" ? value : Number(value);
  return Number.isFinite(parsed) ? parsed : 0;
}

function normalize(row: WeeklyPerformanceRecord): ChartPoint {
  return {
    ...row,
    model_return: numeric(row.model_return),
    sp500_return: numeric(row.sp500_return),
    alpha_vs_sp500: numeric(row.alpha_vs_sp500),
    days_elapsed: numeric(row.days_elapsed)
  };
}

function formatSignedPct(value: number): string {
  const formatted = pct(value);
  if (!formatted) return "";
  return value > 0 ? `+${formatted}` : formatted;
}

function dateLabel(value: string): string {
  const date = new Date(`${value.slice(0, 10)}T00:00:00Z`);
  if (!Number.isFinite(date.getTime())) return value.slice(0, 10);
  return new Intl.DateTimeFormat("en", { month: "short", day: "numeric", timeZone: "UTC" }).format(date);
}

function csvEscape(value: string | number): string {
  const text = String(value);
  if (/[",\n]/.test(text)) return `"${text.replaceAll('"', '""')}"`;
  return text;
}

export default function RoundPerformanceChart({ fallbackRows, roundId, runId }: Props) {
  const [rows, setRows] = useState<WeeklyPerformanceRecord[]>(fallbackRows);

  useEffect(() => {
    const supabase = getSupabaseClient();
    if (!hasSupabaseConfig() || supabase === null) return;
    supabase
      .from("round_weekly_performance")
      .select("*")
      .eq("published", true)
      .eq("round_id", roundId)
      .eq("run_id", runId)
      .order("target_date", { ascending: true })
      .then(({ data, error }) => {
        if (!error && data) setRows(data as WeeklyPerformanceRecord[]);
      });
  }, [roundId, runId]);

  const chartRows = useMemo(() => rows.map(normalize), [rows]);
  const dates = useMemo(
    () => Array.from(new Set(chartRows.map((row) => row.target_date))).sort(),
    [chartRows]
  );
  const modelIds = useMemo(
    () => Array.from(new Set(chartRows.map((row) => row.model_id))).sort((a, b) => modelLabel(a).localeCompare(modelLabel(b))),
    [chartRows]
  );
  const latestDate = dates.at(-1);
  const latestRows = latestDate
    ? modelIds
        .map((modelId) => chartRows.find((row) => row.model_id === modelId && row.target_date === latestDate))
        .filter((row): row is ChartPoint => Boolean(row))
        .sort((a, b) => b.alpha_vs_sp500 - a.alpha_vs_sp500 || modelLabel(a.model_id).localeCompare(modelLabel(b.model_id)))
    : [];
  const hasAtLeastOneWeek = chartRows.some((row) => row.days_elapsed >= 7);
  const isRenderable = dates.length >= 2 && hasAtLeastOneWeek && chartRows.length > 0;

  if (!isRenderable) {
    return (
      <div className="performance-empty">
        <Activity size={20} aria-hidden="true" />
        <div>
          <strong>Weekly chart pending</strong>
          <p>At least one weekly price snapshot after the start date is required before interim performance is shown.</p>
        </div>
      </div>
    );
  }

  const values = chartRows.flatMap((row) => [row.model_return, row.sp500_return, 0]);
  const minValue = Math.min(...values);
  const maxValue = Math.max(...values);
  const range = Math.max(0.01, maxValue - minValue);
  const yMin = minValue - range * 0.18;
  const yMax = maxValue + range * 0.18;
  const innerWidth = width - pad.left - pad.right;
  const innerHeight = height - pad.top - pad.bottom;
  const x = (dateValue: string) => {
    const index = dates.indexOf(dateValue);
    return pad.left + (dates.length === 1 ? innerWidth / 2 : (index / (dates.length - 1)) * innerWidth);
  };
  const y = (value: number) => pad.top + ((yMax - value) / (yMax - yMin)) * innerHeight;
  const zeroY = y(0);
  const ticks = [yMin, yMin + (yMax - yMin) * 0.5, yMax];
  const sp500Points = dates
    .map((dateValue) => {
      const row = chartRows.find((item) => item.target_date === dateValue);
      return row ? `${x(dateValue)},${y(row.sp500_return)}` : "";
    })
    .filter(Boolean)
    .join(" ");

  function modelPolyline(modelId: string): string {
    return dates
      .map((dateValue) => {
        const row = chartRows.find((item) => item.model_id === modelId && item.target_date === dateValue);
        return row ? `${x(dateValue)},${y(row.model_return)}` : "";
      })
      .filter(Boolean)
      .join(" ");
  }

  function exportCsv() {
    const header = ["Model", "Provider", "Target date", "Price date", "Days elapsed", "Model return", "S&P 500 return", "Return vs S&P 500"].join(",");
    const body = chartRows
      .map((row) =>
        [
          modelLabel(row.model_id),
          providerLabel(row.provider),
          row.target_date,
          row.price_date,
          row.days_elapsed,
          row.model_return,
          row.sp500_return,
          row.alpha_vs_sp500
        ]
          .map(csvEscape)
          .join(",")
      )
      .join("\n");
    const blob = new Blob([`${header}\n${body}\n`], { type: "text/csv;charset=utf-8" });
    const url = URL.createObjectURL(blob);
    const anchor = document.createElement("a");
    anchor.href = url;
    anchor.download = `capitalbench-${roundId}-weekly-performance.csv`;
    anchor.click();
    URL.revokeObjectURL(url);
  }

  return (
    <div className="performance-chart-shell">
      <div className="performance-chart-toolbar">
        <div>
          <strong>{latestDate ? `${dateLabel(latestDate)} snapshot` : "Weekly snapshot"}</strong>
          <span>Interim returns from the start date; final scoring still waits for ending prices.</span>
        </div>
        <button className="small-button" type="button" onClick={exportCsv}>
          <Download size={15} aria-hidden="true" />
          CSV
        </button>
      </div>
      <div className="performance-chart-grid">
        <div className="performance-svg-wrap">
          <svg viewBox={`0 0 ${width} ${height}`} role="img" aria-label="Model returns compared with S&P 500 at weekly intervals">
            <line x1={pad.left} x2={width - pad.right} y1={zeroY} y2={zeroY} className="chart-zero-line" />
            {ticks.map((tick) => (
              <g key={tick}>
                <line x1={pad.left} x2={width - pad.right} y1={y(tick)} y2={y(tick)} className="chart-grid-line" />
                <text x={pad.left - 10} y={y(tick) + 4} textAnchor="end" className="chart-axis-label">
                  {formatSignedPct(tick)}
                </text>
              </g>
            ))}
            {dates.map((dateValue) => (
              <g key={dateValue}>
                <line x1={x(dateValue)} x2={x(dateValue)} y1={pad.top} y2={height - pad.bottom} className="chart-grid-line vertical" />
                <text x={x(dateValue)} y={height - 15} textAnchor="middle" className="chart-axis-label">
                  {dateLabel(dateValue)}
                </text>
              </g>
            ))}
            <polyline points={sp500Points} fill="none" className="chart-sp500-line" />
            {dates.map((dateValue) => {
              const row = chartRows.find((item) => item.target_date === dateValue);
              return row ? <circle key={`sp500-${dateValue}`} cx={x(dateValue)} cy={y(row.sp500_return)} r="4" className="chart-sp500-dot" /> : null;
            })}
            {modelIds.map((modelId, index) => {
              const color = palette[index % palette.length];
              return (
                <g key={modelId}>
                  <polyline points={modelPolyline(modelId)} fill="none" stroke={color} className="chart-model-line" />
                  {dates.map((dateValue) => {
                    const row = chartRows.find((item) => item.model_id === modelId && item.target_date === dateValue);
                    return row ? <circle key={`${modelId}-${dateValue}`} cx={x(dateValue)} cy={y(row.model_return)} r="4.5" fill={color} className="chart-model-dot" /> : null;
                  })}
                </g>
              );
            })}
          </svg>
        </div>
        <div className="performance-legend" aria-label="Chart legend">
          <div className="legend-row benchmark">
            <span></span>
            <strong>S&P 500</strong>
            <em>{formatSignedPct(latestRows[0]?.sp500_return ?? 0)}</em>
          </div>
          {modelIds.map((modelId, index) => {
            const latest = latestRows.find((row) => row.model_id === modelId);
            return (
              <div className="legend-row" key={modelId}>
                <span style={{ background: palette[index % palette.length] }}></span>
                <strong>{modelLabel(modelId)}</strong>
                <em>{latest ? formatSignedPct(latest.model_return) : ""}</em>
              </div>
            );
          })}
        </div>
      </div>
      <div className="performance-table" aria-label="Latest weekly performance snapshot">
        {latestRows.map((row) => (
          <article key={row.model_id}>
            <span className={`provider-badge provider-${row.provider}`}>{providerLabel(row.provider)}</span>
            <strong>{modelLabel(row.model_id)}</strong>
            <dl>
              <div>
                <dt>Return</dt>
                <dd>{formatSignedPct(row.model_return)}</dd>
              </div>
              <div>
                <dt>Vs S&P 500</dt>
                <dd className={row.alpha_vs_sp500 >= 0 ? "positive" : "negative"}>{formatSignedPct(row.alpha_vs_sp500)}</dd>
              </div>
              <div>
                <dt>Primary</dt>
                <dd>{row.selected_option_id}</dd>
              </div>
            </dl>
          </article>
        ))}
      </div>
    </div>
  );
}
