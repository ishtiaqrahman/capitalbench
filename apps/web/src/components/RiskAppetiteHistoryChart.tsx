import { Activity, BriefcaseBusiness, Layers3, LineChart } from "lucide-react";
import { useMemo, useState } from "react";
import type { CSSProperties } from "react";

type RiskHistoryMode = "pulse" | "agreement" | "regime" | "outstanding";

type AssetDriver = {
  option_id: string;
  label: string;
  ticker: string;
  allocation_pct: number;
};

type RegimeExposure = {
  key: string;
  label: string;
  allocation_pct: number;
};

type DecisionHistoryPoint = {
  date: string;
  combined_score: number | null;
  label: string;
  weekly_score: number | null;
  monthly_score: number | null;
  weekly_round_id: string | null;
  monthly_round_id: string | null;
  model_count: number;
  agreement_label: string;
  agreement_standard_deviation: number | null;
  agreement_range: { minimum: number | null; maximum: number | null };
  top_regime: RegimeExposure | null;
  top_assets: AssetDriver[];
  regime_exposure: RegimeExposure[];
};

type OutstandingHistoryPoint = {
  date: string;
  score: number | null;
  label: string;
  weekly_score: number | null;
  monthly_score: number | null;
  portfolio_count: number;
  round_count: number;
  weekly_portfolio_count: number;
  monthly_portfolio_count: number;
};

type ScaleBand = {
  minimum: number;
  maximum: number;
  label: string;
};

interface Props {
  decisionHistory: DecisionHistoryPoint[];
  outstandingHistory: OutstandingHistoryPoint[];
  scale: {
    minimum: number;
    maximum: number;
    bands: ScaleBand[];
  };
}

const MODES: Array<{
  key: RiskHistoryMode;
  label: string;
  icon: typeof LineChart;
}> = [
  { key: "pulse", label: "Pulse", icon: LineChart },
  { key: "agreement", label: "Agreement", icon: Activity },
  { key: "regime", label: "Regime Mix", icon: Layers3 },
  { key: "outstanding", label: "Live Book", icon: BriefcaseBusiness }
];

const REGIME_ORDER = [
  "liquidity_defensive",
  "duration_credit",
  "defensive_equity",
  "broad_cyclical_equity",
  "growth_technology",
  "international_equity",
  "real_assets_inflation",
  "crypto"
];

const REGIME_COLORS: Record<string, string> = {
  liquidity_defensive: "#607d78",
  duration_credit: "#3f6f9f",
  defensive_equity: "#2f866f",
  broad_cyclical_equity: "#d19a38",
  growth_technology: "#7259a5",
  international_equity: "#bf5b5b",
  real_assets_inflation: "#b76d2a",
  crypto: "#171d1b"
};

const width = 900;
const height = 370;
const pad = { top: 22, right: 24, bottom: 44, left: 48 };

function finite(value: number | null | undefined): value is number {
  return typeof value === "number" && Number.isFinite(value);
}

function score(value: number | null | undefined): string {
  return finite(value) ? value.toFixed(1) : "n/a";
}

function pct(value: number | null | undefined): string {
  if (!finite(value)) return "n/a";
  return `${value.toFixed(value >= 10 ? 1 : 2)}%`;
}

function assetLabel(asset: AssetDriver): string {
  return asset.ticker ? `${asset.label} (${asset.ticker})` : asset.label || asset.option_id;
}

function shortDate(value: string): string {
  const [year, month, day] = value.split("-").map(Number);
  if (!year || !month || !day) return value;
  return new Intl.DateTimeFormat("en-US", {
    month: "short",
    day: "numeric",
    timeZone: "UTC"
  }).format(new Date(Date.UTC(year, month - 1, day)));
}

function longDate(value: string): string {
  const [year, month, day] = value.split("-").map(Number);
  if (!year || !month || !day) return value;
  return new Intl.DateTimeFormat("en-US", {
    month: "long",
    day: "numeric",
    year: "numeric",
    timeZone: "UTC"
  }).format(new Date(Date.UTC(year, month - 1, day)));
}

function dateValue(value: string): number {
  return Date.parse(`${value}T00:00:00Z`);
}

function xScale(dates: string[]) {
  const values = dates.map(dateValue);
  const minimum = Math.min(...values);
  const maximum = Math.max(...values);
  const range = Math.max(1, maximum - minimum);
  return (date: string) => pad.left + ((dateValue(date) - minimum) / range) * (width - pad.left - pad.right);
}

function yScale(minimum: number, maximum: number) {
  const range = Math.max(1, maximum - minimum);
  return (value: number) => pad.top + ((maximum - value) / range) * (height - pad.top - pad.bottom);
}

function linePath<T>(points: T[], valueFor: (point: T) => number | null, dateFor: (point: T) => string, x: (date: string) => number, y: (value: number) => number) {
  let path = "";
  let drawing = false;
  for (const point of points) {
    const value = valueFor(point);
    if (!finite(value)) {
      drawing = false;
      continue;
    }
    path += `${drawing ? " L" : "M"} ${x(dateFor(point)).toFixed(2)} ${y(value).toFixed(2)}`;
    drawing = true;
  }
  return path;
}

function labelIndices(length: number): Set<number> {
  if (length <= 5) return new Set(Array.from({ length }, (_, index) => index));
  return new Set([0, Math.round((length - 1) * 0.25), Math.round((length - 1) * 0.5), Math.round((length - 1) * 0.75), length - 1]);
}

function regimeValue(point: DecisionHistoryPoint, key: string): number {
  return point.regime_exposure.find((row) => row.key === key)?.allocation_pct ?? 0;
}

function regimeAreaPath(points: DecisionHistoryPoint[], key: string, x: (date: string) => number, y: (value: number) => number) {
  const regimeIndex = REGIME_ORDER.indexOf(key);
  const lower = points.map((point) =>
    REGIME_ORDER.slice(0, regimeIndex).reduce((total, regimeKey) => total + regimeValue(point, regimeKey), 0)
  );
  const upper = points.map((point, index) => lower[index] + regimeValue(point, key));
  const top = points.map((point, index) => `${x(point.date).toFixed(2)} ${y(upper[index]).toFixed(2)}`);
  const bottom = [...points]
    .reverse()
    .map((point, reverseIndex) => {
      const index = points.length - 1 - reverseIndex;
      return `${x(point.date).toFixed(2)} ${y(lower[index]).toFixed(2)}`;
    });
  return `M ${top.join(" L ")} L ${bottom.join(" L ")} Z`;
}

function PulseChart({
  points,
  scale,
  selectedIndex,
  onSelect
}: {
  points: DecisionHistoryPoint[];
  scale: Props["scale"];
  selectedIndex: number;
  onSelect: (index: number) => void;
}) {
  const x = xScale(points.map((point) => point.date));
  const y = yScale(scale.minimum, scale.maximum);
  const ticks = [0, 20, 40, 60, 80, 100];
  const labels = labelIndices(points.length);
  const selected = points[selectedIndex];
  const lines = [
    { key: "combined", label: "Combined", color: "#0b1413", value: (point: DecisionHistoryPoint) => point.combined_score },
    { key: "monthly", label: "Monthly", color: "#b47413", value: (point: DecisionHistoryPoint) => point.monthly_score },
    { key: "weekly", label: "Weekly", color: "#087b69", value: (point: DecisionHistoryPoint) => point.weekly_score }
  ];

  return (
    <>
      <div className="risk-history-legend" aria-label="Pulse chart legend">
        {lines.map((line) => (
          <span key={line.key} style={{ "--legend-color": line.color } as CSSProperties}>{line.label}</span>
        ))}
      </div>
      <svg viewBox={`0 0 ${width} ${height}`} role="img" aria-label="Historical combined, monthly, and weekly AI Risk Appetite">
        {scale.bands.map((band, index) => (
          <rect
            key={band.label}
            x={pad.left}
            y={y(band.maximum)}
            width={width - pad.left - pad.right}
            height={y(band.minimum) - y(band.maximum)}
            className={`risk-history-band risk-history-band-${index + 1}`}
          />
        ))}
        {ticks.map((tick) => (
          <g key={tick}>
            <line x1={pad.left} x2={width - pad.right} y1={y(tick)} y2={y(tick)} className="risk-history-grid-line" />
            <text x={pad.left - 10} y={y(tick) + 4} textAnchor="end" className="risk-history-axis-label">{tick}</text>
          </g>
        ))}
        {points.map((point, index) =>
          labels.has(index) ? (
            <text key={point.date} x={x(point.date)} y={height - 15} textAnchor="middle" className="risk-history-axis-label">
              {shortDate(point.date)}
            </text>
          ) : null
        )}
        {selected ? (
          <line
            x1={x(selected.date)}
            x2={x(selected.date)}
            y1={pad.top}
            y2={height - pad.bottom}
            className="risk-history-selected-line"
          />
        ) : null}
        {lines.map((line) => (
          <g key={line.key}>
            <path
              d={linePath(points, line.value, (point) => point.date, x, y)}
              fill="none"
              stroke={line.color}
              className={`risk-history-line risk-history-line-${line.key}`}
            />
            {points.map((point, index) => {
              const value = line.value(point);
              if (!finite(value)) return null;
              return (
                <circle
                  key={`${line.key}-${point.date}`}
                  cx={x(point.date)}
                  cy={y(value)}
                  r={index === selectedIndex ? 5.5 : 3.5}
                  fill={line.color}
                  className="risk-history-point"
                  tabIndex={0}
                  aria-label={`${line.label}, ${longDate(point.date)}, ${score(value)}`}
                  onMouseEnter={() => onSelect(index)}
                  onFocus={() => onSelect(index)}
                  onClick={() => onSelect(index)}
                />
              );
            })}
          </g>
        ))}
      </svg>
    </>
  );
}

function AgreementChart({
  points,
  selectedIndex,
  onSelect
}: {
  points: DecisionHistoryPoint[];
  selectedIndex: number;
  onSelect: (index: number) => void;
}) {
  const x = xScale(points.map((point) => point.date));
  const maximumValue = Math.max(15, ...points.map((point) => point.agreement_standard_deviation ?? 0));
  const domainMaximum = Math.ceil(maximumValue / 5) * 5;
  const y = yScale(0, domainMaximum);
  const ticks = Array.from({ length: domainMaximum / 5 + 1 }, (_, index) => index * 5);
  const labels = labelIndices(points.length);
  const selected = points[selectedIndex];

  return (
    <>
      <div className="risk-history-legend risk-history-threshold-legend" aria-label="Agreement thresholds">
        <span style={{ "--legend-color": "#2f866f" } as CSSProperties}>Tight under 5</span>
        <span style={{ "--legend-color": "#d19a38" } as CSSProperties}>Mixed 5-12</span>
        <span style={{ "--legend-color": "#bf5b5b" } as CSSProperties}>Divided above 12</span>
      </div>
      <svg viewBox={`0 0 ${width} ${height}`} role="img" aria-label="Historical model agreement measured by score dispersion">
        <rect x={pad.left} y={y(5)} width={width - pad.left - pad.right} height={y(0) - y(5)} className="risk-history-agreement-tight" />
        <rect x={pad.left} y={y(12)} width={width - pad.left - pad.right} height={y(5) - y(12)} className="risk-history-agreement-mixed" />
        <rect x={pad.left} y={y(domainMaximum)} width={width - pad.left - pad.right} height={y(12) - y(domainMaximum)} className="risk-history-agreement-divided" />
        {ticks.map((tick) => (
          <g key={tick}>
            <line x1={pad.left} x2={width - pad.right} y1={y(tick)} y2={y(tick)} className="risk-history-grid-line" />
            <text x={pad.left - 10} y={y(tick) + 4} textAnchor="end" className="risk-history-axis-label">{tick}</text>
          </g>
        ))}
        {points.map((point, index) =>
          labels.has(index) ? (
            <text key={point.date} x={x(point.date)} y={height - 15} textAnchor="middle" className="risk-history-axis-label">
              {shortDate(point.date)}
            </text>
          ) : null
        )}
        {selected ? (
          <line x1={x(selected.date)} x2={x(selected.date)} y1={pad.top} y2={height - pad.bottom} className="risk-history-selected-line" />
        ) : null}
        <path
          d={linePath(points, (point) => point.agreement_standard_deviation, (point) => point.date, x, y)}
          fill="none"
          stroke="#214f8f"
          className="risk-history-line"
        />
        {points.map((point, index) =>
          finite(point.agreement_standard_deviation) ? (
            <circle
              key={point.date}
              cx={x(point.date)}
              cy={y(point.agreement_standard_deviation)}
              r={index === selectedIndex ? 5.5 : 3.5}
              fill="#214f8f"
              className="risk-history-point"
              tabIndex={0}
              aria-label={`${longDate(point.date)}, ${point.agreement_label}, ${score(point.agreement_standard_deviation)} point standard deviation`}
              onMouseEnter={() => onSelect(index)}
              onFocus={() => onSelect(index)}
              onClick={() => onSelect(index)}
            />
          ) : null
        )}
      </svg>
    </>
  );
}

function RegimeChart({
  points,
  selectedIndex,
  onSelect
}: {
  points: DecisionHistoryPoint[];
  selectedIndex: number;
  onSelect: (index: number) => void;
}) {
  const x = xScale(points.map((point) => point.date));
  const y = yScale(0, 100);
  const labels = labelIndices(points.length);
  const selected = points[selectedIndex];
  const presentRegimes = REGIME_ORDER.filter((key) => points.some((point) => regimeValue(point, key) > 0));

  return (
    <>
      <div className="risk-history-legend risk-history-regime-legend" aria-label="Regime chart legend">
        {presentRegimes.map((key) => {
          const label = points.flatMap((point) => point.regime_exposure).find((row) => row.key === key)?.label ?? key;
          return <span key={key} style={{ "--legend-color": REGIME_COLORS[key] } as CSSProperties}>{label}</span>;
        })}
      </div>
      <svg viewBox={`0 0 ${width} ${height}`} role="img" aria-label="Historical allocation regime mix">
        {[0, 25, 50, 75, 100].map((tick) => (
          <g key={tick}>
            <line x1={pad.left} x2={width - pad.right} y1={y(tick)} y2={y(tick)} className="risk-history-grid-line" />
            <text x={pad.left - 10} y={y(tick) + 4} textAnchor="end" className="risk-history-axis-label">{tick}%</text>
          </g>
        ))}
        {presentRegimes.map((key) => (
          <path
            key={key}
            d={regimeAreaPath(points, key, x, y)}
            fill={REGIME_COLORS[key]}
            className="risk-history-regime-area"
          />
        ))}
        {points.map((point, index) =>
          labels.has(index) ? (
            <text key={point.date} x={x(point.date)} y={height - 15} textAnchor="middle" className="risk-history-axis-label">
              {shortDate(point.date)}
            </text>
          ) : null
        )}
        {selected ? (
          <line x1={x(selected.date)} x2={x(selected.date)} y1={pad.top} y2={height - pad.bottom} className="risk-history-selected-line is-light" />
        ) : null}
        {points.map((point, index) => (
          <rect
            key={point.date}
            x={x(point.date) - 12}
            y={pad.top}
            width={24}
            height={height - pad.top - pad.bottom}
            fill="transparent"
            className="risk-history-hit-area"
            tabIndex={0}
            aria-label={`${longDate(point.date)}, largest regime ${point.top_regime?.label ?? "not available"} ${pct(point.top_regime?.allocation_pct)}`}
            onMouseEnter={() => onSelect(index)}
            onFocus={() => onSelect(index)}
            onClick={() => onSelect(index)}
          />
        ))}
      </svg>
    </>
  );
}

function OutstandingChart({
  points,
  scale,
  selectedIndex,
  onSelect
}: {
  points: OutstandingHistoryPoint[];
  scale: Props["scale"];
  selectedIndex: number;
  onSelect: (index: number) => void;
}) {
  const x = xScale(points.map((point) => point.date));
  const y = yScale(scale.minimum, scale.maximum);
  const ticks = [0, 20, 40, 60, 80, 100];
  const labels = labelIndices(points.length);
  const selected = points[selectedIndex];
  const lines = [
    { key: "combined", label: "Combined live book", color: "#0b1413", value: (point: OutstandingHistoryPoint) => point.score },
    { key: "monthly", label: "Monthly exposure", color: "#b47413", value: (point: OutstandingHistoryPoint) => point.monthly_score },
    { key: "weekly", label: "Weekly exposure", color: "#087b69", value: (point: OutstandingHistoryPoint) => point.weekly_score }
  ];

  return (
    <>
      <div className="risk-history-legend" aria-label="Outstanding live-book chart legend">
        {lines.map((line) => (
          <span key={line.key} style={{ "--legend-color": line.color } as CSSProperties}>{line.label}</span>
        ))}
      </div>
      <svg viewBox={`0 0 ${width} ${height}`} role="img" aria-label="Historical risk level of all portfolios still open on each date">
        {scale.bands.map((band, index) => (
          <rect
            key={band.label}
            x={pad.left}
            y={y(band.maximum)}
            width={width - pad.left - pad.right}
            height={y(band.minimum) - y(band.maximum)}
            className={`risk-history-band risk-history-band-${index + 1}`}
          />
        ))}
        {ticks.map((tick) => (
          <g key={tick}>
            <line x1={pad.left} x2={width - pad.right} y1={y(tick)} y2={y(tick)} className="risk-history-grid-line" />
            <text x={pad.left - 10} y={y(tick) + 4} textAnchor="end" className="risk-history-axis-label">{tick}</text>
          </g>
        ))}
        {points.map((point, index) =>
          labels.has(index) ? (
            <text key={point.date} x={x(point.date)} y={height - 15} textAnchor="middle" className="risk-history-axis-label">
              {shortDate(point.date)}
            </text>
          ) : null
        )}
        {selected ? (
          <line x1={x(selected.date)} x2={x(selected.date)} y1={pad.top} y2={height - pad.bottom} className="risk-history-selected-line" />
        ) : null}
        {lines.map((line) => (
          <g key={line.key}>
            <path
              d={linePath(points, line.value, (point) => point.date, x, y)}
              fill="none"
              stroke={line.color}
              className={`risk-history-line risk-history-line-${line.key}`}
            />
            {points.map((point, index) => {
              const value = line.value(point);
              if (!finite(value)) return null;
              return (
                <circle
                  key={`${line.key}-${point.date}`}
                  cx={x(point.date)}
                  cy={y(value)}
                  r={index === selectedIndex ? 5.5 : 3.5}
                  fill={line.color}
                  className="risk-history-point"
                  tabIndex={0}
                  aria-label={`${line.label}, ${longDate(point.date)}, ${score(value)}`}
                  onMouseEnter={() => onSelect(index)}
                  onFocus={() => onSelect(index)}
                  onClick={() => onSelect(index)}
                />
              );
            })}
          </g>
        ))}
      </svg>
    </>
  );
}

export default function RiskAppetiteHistoryChart({ decisionHistory, outstandingHistory, scale }: Props) {
  const [mode, setMode] = useState<RiskHistoryMode>("pulse");
  const [selectedIndex, setSelectedIndex] = useState(Math.max(0, decisionHistory.length - 1));
  const decisionPoint = decisionHistory[Math.min(selectedIndex, decisionHistory.length - 1)];
  const outstandingPoint = outstandingHistory[Math.min(selectedIndex, outstandingHistory.length - 1)];
  const activeDate = mode === "outstanding" ? outstandingPoint?.date : decisionPoint?.date;
  const chartDescription = useMemo(() => {
    if (mode === "agreement") return "Lower dispersion means models are taking similar levels of risk. Higher dispersion means their allocations disagree.";
    if (mode === "regime") return "The same headline score can come from different exposures. This view shows what kind of risk dominates.";
    if (mode === "outstanding") return "All portfolios that had been published and had not reached their scheduled exit date on each decision date.";
    return "The latest Monthly and Weekly decisions are calculated separately and then receive equal weight in the Combined line.";
  }, [mode]);

  if (!decisionHistory.length || !outstandingHistory.length) return null;

  return (
    <section className="risk-history" aria-labelledby="risk-history-title">
      <div className="risk-history-head">
        <div>
          <span className="panel-kicker">Saved allocation history</span>
          <h2 id="risk-history-title">Historical AI Risk Appetite</h2>
          <p>{chartDescription}</p>
        </div>
        <div className="risk-history-tabs" role="tablist" aria-label="Historical AI Risk Appetite view">
          {MODES.map((item) => {
            const Icon = item.icon;
            return (
              <button
                key={item.key}
                type="button"
                role="tab"
                aria-selected={mode === item.key}
                className={mode === item.key ? "is-active" : ""}
                onClick={() => setMode(item.key)}
              >
                <Icon size={15} aria-hidden="true" />
                <span>{item.label}</span>
              </button>
            );
          })}
        </div>
      </div>

      <div className="risk-history-workspace">
        <div className="risk-history-chart">
          {mode === "pulse" ? (
            <PulseChart points={decisionHistory} scale={scale} selectedIndex={selectedIndex} onSelect={setSelectedIndex} />
          ) : null}
          {mode === "agreement" ? (
            <AgreementChart points={decisionHistory} selectedIndex={selectedIndex} onSelect={setSelectedIndex} />
          ) : null}
          {mode === "regime" ? (
            <RegimeChart points={decisionHistory} selectedIndex={selectedIndex} onSelect={setSelectedIndex} />
          ) : null}
          {mode === "outstanding" ? (
            <OutstandingChart points={outstandingHistory} scale={scale} selectedIndex={selectedIndex} onSelect={setSelectedIndex} />
          ) : null}
        </div>

        <aside className="risk-history-inspector" aria-live="polite">
          <div className="risk-history-inspector-head">
            <span>Selected decision date</span>
            <strong>{activeDate ? longDate(activeDate) : "Not available"}</strong>
          </div>

          {mode === "pulse" && decisionPoint ? (
            <>
              <div className="risk-history-primary-value">
                <strong>{score(decisionPoint.combined_score)}</strong>
                <span>{decisionPoint.label}</span>
              </div>
              <dl className="risk-history-metrics">
                <div><dt>Monthly</dt><dd>{score(decisionPoint.monthly_score)}</dd></div>
                <div><dt>Weekly</dt><dd>{score(decisionPoint.weekly_score)}</dd></div>
                <div><dt>Agreement</dt><dd>{decisionPoint.agreement_label}</dd></div>
                <div><dt>Models</dt><dd>{decisionPoint.model_count}</dd></div>
              </dl>
              <div className="risk-history-detail-list">
                <span>Largest allocation drivers</span>
                {decisionPoint.top_assets.slice(0, 4).map((asset) => (
                  <div key={asset.option_id}>
                    <strong>{assetLabel(asset)}</strong>
                    <em>{pct(asset.allocation_pct)}</em>
                  </div>
                ))}
              </div>
              <div className="risk-history-rounds">
                <span>{decisionPoint.monthly_round_id ?? "No monthly round yet"}</span>
                <span>{decisionPoint.weekly_round_id ?? "No weekly round yet"}</span>
              </div>
            </>
          ) : null}

          {mode === "agreement" && decisionPoint ? (
            <>
              <div className="risk-history-primary-value">
                <strong>{score(decisionPoint.agreement_standard_deviation)}</strong>
                <span>{decisionPoint.agreement_label} dispersion</span>
              </div>
              <dl className="risk-history-metrics">
                <div><dt>Lowest model</dt><dd>{score(decisionPoint.agreement_range.minimum)}</dd></div>
                <div><dt>Highest model</dt><dd>{score(decisionPoint.agreement_range.maximum)}</dd></div>
                <div><dt>Range</dt><dd>{finite(decisionPoint.agreement_range.minimum) && finite(decisionPoint.agreement_range.maximum) ? score(decisionPoint.agreement_range.maximum - decisionPoint.agreement_range.minimum) : "n/a"}</dd></div>
                <div><dt>Models</dt><dd>{decisionPoint.model_count}</dd></div>
              </dl>
              <p className="risk-history-inspector-note">
                Standard deviation is calculated across each model's combined latest Monthly and Weekly score.
              </p>
            </>
          ) : null}

          {mode === "regime" && decisionPoint ? (
            <>
              <div className="risk-history-primary-value">
                <strong>{pct(decisionPoint.top_regime?.allocation_pct)}</strong>
                <span>{decisionPoint.top_regime?.label ?? "No dominant regime"}</span>
              </div>
              <div className="risk-history-regime-list">
                {decisionPoint.regime_exposure.map((regime) => (
                  <div key={regime.key}>
                    <i style={{ background: REGIME_COLORS[regime.key] }}></i>
                    <span>{regime.label}</span>
                    <strong>{pct(regime.allocation_pct)}</strong>
                  </div>
                ))}
              </div>
            </>
          ) : null}

          {mode === "outstanding" && outstandingPoint ? (
            <>
              <div className="risk-history-primary-value">
                <strong>{score(outstandingPoint.score)}</strong>
                <span>{outstandingPoint.label}</span>
              </div>
              <dl className="risk-history-metrics">
                <div><dt>Monthly</dt><dd>{score(outstandingPoint.monthly_score)}</dd></div>
                <div><dt>Weekly</dt><dd>{score(outstandingPoint.weekly_score)}</dd></div>
                <div><dt>Portfolios</dt><dd>{outstandingPoint.portfolio_count}</dd></div>
                <div><dt>Live rounds</dt><dd>{outstandingPoint.round_count}</dd></div>
              </dl>
              <div className="risk-history-detail-list">
                <span>Portfolio mix</span>
                <div><strong>Monthly portfolios</strong><em>{outstandingPoint.monthly_portfolio_count}</em></div>
                <div><strong>Weekly portfolios</strong><em>{outstandingPoint.weekly_portfolio_count}</em></div>
              </div>
            </>
          ) : null}
        </aside>
      </div>

      <p className="risk-history-note">
        Historical points are reconstructed only from portfolios and dates in the public record. Prices and subsequent returns are excluded.
      </p>
    </section>
  );
}
