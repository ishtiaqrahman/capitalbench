import { ArrowRight, Info, Scale, TrendingUp } from "lucide-react";
import { useState } from "react";
import type { CSSProperties, KeyboardEvent } from "react";

type RiskReturnModel = {
  modelId: string;
  label: string;
  provider: string;
  providerLabel: string;
  logoSrc?: string | null;
  returnPct: number;
  riskScore: number;
  riskLabel: string;
  riskMinimum: number;
  riskMaximum: number;
  roundCount: number;
  returnRank: number;
  alphaVsBenchmarkPct: number | null;
  beatsBenchmarkWithNoMoreRisk: boolean;
  href: string;
};

type RiskReturnData = {
  setId: string;
  track: "weekly" | "monthly";
  roundCount: number;
  methodologyVersion?: string | null;
  riskDomain: { minimum: number; maximum: number };
  benchmark: {
    label: string;
    returnPct: number;
    riskScore: number;
    roundCount: number;
  } | null;
  models: RiskReturnModel[];
  returnLeader: RiskReturnModel | null;
  strongTradeoffModels: RiskReturnModel[];
};

interface Props {
  data: RiskReturnData;
}

type ChartGeometry = {
  width: number;
  height: number;
  pad: { top: number; right: number; bottom: number; left: number };
};

const DESKTOP_GEOMETRY: ChartGeometry = {
  width: 920,
  height: 450,
  pad: { top: 42, right: 34, bottom: 68, left: 72 }
};

const MOBILE_GEOMETRY: ChartGeometry = {
  width: 420,
  height: 410,
  pad: { top: 36, right: 18, bottom: 62, left: 54 }
};

const RISK_BANDS = [
  { minimum: 0, maximum: 20, label: "Defensive", key: "defensive" },
  { minimum: 20, maximum: 40, label: "Cautious", key: "cautious" },
  { minimum: 40, maximum: 60, label: "Balanced", key: "balanced" },
  { minimum: 60, maximum: 80, label: "Risk-seeking", key: "seeking" },
  { minimum: 80, maximum: 100, label: "Aggressive", key: "aggressive" }
];

function finiteNumber(value: number | null | undefined): value is number {
  return typeof value === "number" && Number.isFinite(value);
}

function returnLabel(value: number, signed = false): string {
  const prefix = signed && value > 0 ? "+" : "";
  return `${prefix}${value.toFixed(2)}%`;
}

function alphaLabel(value: number | null): string {
  if (!finiteNumber(value)) return "n/a";
  const prefix = value > 0 ? "+" : "";
  return `${prefix}${value.toFixed(2)} pp`;
}

function niceStep(value: number): number {
  if (!finiteNumber(value) || value <= 0) return 1;
  const power = 10 ** Math.floor(Math.log10(value));
  const fraction = value / power;
  const multiple = fraction <= 1 ? 1 : fraction <= 2 ? 2 : fraction <= 5 ? 5 : 10;
  return multiple * power;
}

function returnDomain(data: RiskReturnData) {
  const values = [
    0,
    ...data.models.map((model) => model.returnPct),
    ...(data.benchmark ? [data.benchmark.returnPct] : [])
  ];
  const rawMinimum = Math.min(...values);
  const rawMaximum = Math.max(...values);
  const padding = Math.max((rawMaximum - rawMinimum) * 0.12, 0.2);
  const step = niceStep((rawMaximum - rawMinimum + padding * 2) / 4);
  let minimum = Math.floor((rawMinimum - padding) / step) * step;
  let maximum = Math.ceil((rawMaximum + padding) / step) * step;
  if (minimum === maximum) maximum = minimum + step * 4;
  const ticks = Array.from(
    { length: Math.round((maximum - minimum) / step) + 1 },
    (_, index) => minimum + step * index
  );
  return { minimum, maximum, ticks };
}

function riskTicks(domain: RiskReturnData["riskDomain"]): number[] {
  const step = (domain.maximum - domain.minimum) / 4;
  return Array.from({ length: 5 }, (_, index) => domain.minimum + step * index);
}

function providerClass(provider: string): string {
  return provider ? `is-${provider}` : "is-neutral";
}

function plotLabel(label: string): string {
  return label
    .replace(/^Claude\s+/, "")
    .replace(/\s+Pro$/, "");
}

function plotLabelPosition(
  model: RiskReturnModel,
  pointX: number,
  geometry: ChartGeometry,
  compact: boolean
) {
  const { width, pad } = geometry;
  const edgeBuffer = compact ? 72 : 110;
  let side = model.returnRank % 2 === 1 ? 1 : -1;

  if (pointX > width - pad.right - edgeBuffer) side = -1;
  if (pointX < pad.left + edgeBuffer) side = 1;

  const verticalOffsets = compact
    ? [-16, -46, 1, 1, 17, 17, 24, -22]
    : [-18, -50, 2, 2, 20, 20, 30, -26];
  const distance = compact ? 17 : 21;

  return {
    dx: side * distance,
    dy: verticalOffsets[(model.returnRank - 1) % verticalOffsets.length],
    side,
    textAnchor: side > 0 ? "start" as const : "end" as const
  };
}

function joinLabels(models: RiskReturnModel[]): string {
  if (!models.length) return "No model";
  if (models.length === 1) return models[0].label;
  if (models.length === 2) return `${models[0].label} and ${models[1].label}`;
  return `${models.slice(0, -1).map((model) => model.label).join(", ")}, and ${models.at(-1)?.label}`;
}

function Plot({
  data,
  selectedModelId,
  selectModel,
  compact
}: {
  data: RiskReturnData;
  selectedModelId: string;
  selectModel: (modelId: string) => void;
  compact: boolean;
}) {
  const geometry = compact ? MOBILE_GEOMETRY : DESKTOP_GEOMETRY;
  const { width, height, pad } = geometry;
  const returns = returnDomain(data);
  const xRange = Math.max(1, data.riskDomain.maximum - data.riskDomain.minimum);
  const yRange = Math.max(0.0001, returns.maximum - returns.minimum);
  const plotWidth = width - pad.left - pad.right;
  const plotHeight = height - pad.top - pad.bottom;
  const x = (value: number) => pad.left + ((value - data.riskDomain.minimum) / xRange) * plotWidth;
  const y = (value: number) => pad.top + ((returns.maximum - value) / yRange) * plotHeight;
  const clipId = `risk-return-clip-${data.setId}-${compact ? "mobile" : "desktop"}`.replace(/[^a-zA-Z0-9_-]/g, "-");
  const benchmarkX = data.benchmark ? x(data.benchmark.riskScore) : null;
  const benchmarkY = data.benchmark ? y(data.benchmark.returnPct) : null;
  const markerRadius = compact ? 9 : 10;
  const logoSize = compact ? 11 : 12;

  function onPointKeyDown(event: KeyboardEvent<SVGGElement>, modelId: string) {
    if (event.key !== "Enter" && event.key !== " ") return;
    event.preventDefault();
    selectModel(modelId);
  }

  return (
    <svg
      className="benchmark-risk-return-svg"
      viewBox={`0 0 ${width} ${height}`}
      role="img"
      aria-labelledby={`${clipId}-title ${clipId}-description`}
    >
      <title id={`${clipId}-title`}>Risk and return for models in this comparison set</title>
      <desc id={`${clipId}-description`}>
        Average frozen portfolio allocation risk is plotted horizontally and average realized return is plotted vertically across {data.roundCount} shared rounds.
      </desc>
      <defs>
        <clipPath id={clipId}>
          <rect x={pad.left} y={pad.top} width={plotWidth} height={plotHeight} rx="6" />
        </clipPath>
      </defs>

      <g clipPath={`url(#${clipId})`}>
        <rect className="benchmark-risk-return-plot-bg" x={pad.left} y={pad.top} width={plotWidth} height={plotHeight} />
        {RISK_BANDS.map((band) => {
          const minimum = Math.max(band.minimum, data.riskDomain.minimum);
          const maximum = Math.min(band.maximum, data.riskDomain.maximum);
          if (minimum >= maximum) return null;
          return (
            <rect
              key={band.key}
              className={`benchmark-risk-return-band is-${band.key}`}
              x={x(minimum)}
              y={pad.top}
              width={x(maximum) - x(minimum)}
              height={plotHeight}
            />
          );
        })}
        {data.benchmark && benchmarkX !== null && benchmarkY !== null ? (
          <rect
            className="benchmark-risk-return-target-zone"
            x={pad.left}
            y={pad.top}
            width={Math.max(0, benchmarkX - pad.left)}
            height={Math.max(0, benchmarkY - pad.top)}
          />
        ) : null}

        {returns.ticks.map((tick) => (
          <line
            key={`return-${tick}`}
            className="benchmark-risk-return-grid-line"
            x1={pad.left}
            x2={width - pad.right}
            y1={y(tick)}
            y2={y(tick)}
          />
        ))}
        {riskTicks(data.riskDomain).map((tick) => (
          <line
            key={`risk-${tick}`}
            className="benchmark-risk-return-grid-line is-vertical"
            x1={x(tick)}
            x2={x(tick)}
            y1={pad.top}
            y2={height - pad.bottom}
          />
        ))}
        {returns.minimum < 0 && returns.maximum > 0 ? (
          <line
            className="benchmark-risk-return-zero-line"
            x1={pad.left}
            x2={width - pad.right}
            y1={y(0)}
            y2={y(0)}
          />
        ) : null}

        {data.benchmark && benchmarkX !== null && benchmarkY !== null ? (
          <g className="benchmark-risk-return-benchmark-guides">
            <line x1={pad.left} x2={width - pad.right} y1={benchmarkY} y2={benchmarkY} />
            <line x1={benchmarkX} x2={benchmarkX} y1={pad.top} y2={height - pad.bottom} />
          </g>
        ) : null}
      </g>

      {returns.ticks.map((tick) => (
        <text
          key={`return-label-${tick}`}
          className="benchmark-risk-return-axis-tick"
          x={pad.left - 10}
          y={y(tick) + 4}
          textAnchor="end"
        >
          {returnLabel(tick)}
        </text>
      ))}
      {riskTicks(data.riskDomain).map((tick) => (
        <text
          key={`risk-label-${tick}`}
          className="benchmark-risk-return-axis-tick"
          x={x(tick)}
          y={height - pad.bottom + 24}
          textAnchor="middle"
        >
          {tick.toFixed(0)}
        </text>
      ))}

      <text className="benchmark-risk-return-axis-title" x={pad.left + plotWidth / 2} y={height - 10} textAnchor="middle">
        CapitalBench allocation risk
      </text>
      <text
        className="benchmark-risk-return-axis-title"
        x={17}
        y={pad.top + plotHeight / 2}
        textAnchor="middle"
        transform={`rotate(-90 17 ${pad.top + plotHeight / 2})`}
      >
        Average return
      </text>

      {data.benchmark && benchmarkX !== null && benchmarkY !== null ? (
        <g className="benchmark-risk-return-benchmark-point" aria-label={`S&P 500: ${returnLabel(data.benchmark.returnPct)} return, ${data.benchmark.riskScore.toFixed(1)} risk score`}>
          <polygon
            points={`${benchmarkX},${benchmarkY - 12} ${benchmarkX + 12},${benchmarkY} ${benchmarkX},${benchmarkY + 12} ${benchmarkX - 12},${benchmarkY}`}
          />
          <text x={Math.min(width - pad.right - 4, benchmarkX + 17)} y={benchmarkY - 10} textAnchor="start">
            S&amp;P 500
          </text>
        </g>
      ) : null}

      {!compact && data.benchmark && benchmarkX !== null && benchmarkY !== null && benchmarkX - pad.left > 170 && benchmarkY - pad.top > 28 ? (
        <text className="benchmark-risk-return-zone-label" x={pad.left + 12} y={pad.top + 20}>
          Beat S&amp;P with lower allocation risk
        </text>
      ) : null}

      {data.models.map((model) => {
        const pointX = x(model.riskScore);
        const pointY = y(model.returnPct);
        const active = model.modelId === selectedModelId;
        const labelPosition = plotLabelPosition(model, pointX, geometry, compact);
        return (
          <g
            key={model.modelId}
            className={`benchmark-risk-return-point ${providerClass(model.provider)} ${active ? "is-selected" : ""}`}
            transform={`translate(${pointX} ${pointY})`}
            role="button"
            tabIndex={0}
            aria-label={`${model.label}: ${returnLabel(model.returnPct)} average return, ${model.riskScore.toFixed(1)} out of 100 allocation risk`}
            onMouseEnter={() => selectModel(model.modelId)}
            onFocus={() => selectModel(model.modelId)}
            onClick={() => selectModel(model.modelId)}
            onKeyDown={(event) => onPointKeyDown(event, model.modelId)}
          >
            <line
              className="benchmark-risk-return-point-connector"
              x1={labelPosition.side * markerRadius}
              y1={0}
              x2={labelPosition.dx - labelPosition.side * 3}
              y2={labelPosition.dy}
            />
            <circle className="benchmark-risk-return-point-marker" r={markerRadius} />
            {model.logoSrc ? (
              <image
                className="benchmark-risk-return-point-logo"
                href={model.logoSrc}
                x={-logoSize / 2}
                y={-logoSize / 2}
                width={logoSize}
                height={logoSize}
                preserveAspectRatio="xMidYMid meet"
              />
            ) : (
              <text className="benchmark-risk-return-point-fallback" y={3} textAnchor="middle">
                {model.label.slice(0, 1)}
              </text>
            )}
            <text
              className="benchmark-risk-return-point-label"
              x={labelPosition.dx}
              y={labelPosition.dy + 4}
              textAnchor={labelPosition.textAnchor}
            >
              {plotLabel(model.label)}
            </text>
          </g>
        );
      })}
    </svg>
  );
}

export default function BenchmarkSetRiskReturn({ data }: Props) {
  const [selectedModelId, setSelectedModelId] = useState(data.returnLeader?.modelId ?? data.models[0]?.modelId ?? "");
  const selected = data.models.find((model) => model.modelId === selectedModelId) ?? data.returnLeader;
  const tradeoffFinding = data.strongTradeoffModels.length
    ? `${joinLabels(data.strongTradeoffModels)} beat the S&P 500 while taking no more allocation risk.`
    : "No model beat the S&P 500 while taking the same or less allocation risk in this set.";
  const leaderFinding = data.returnLeader
    ? `${data.returnLeader.label} led the models at ${returnLabel(data.returnLeader.returnPct, true)} average return with a ${data.returnLeader.riskScore.toFixed(1)}/100 risk score.`
    : "A return leader is not available yet.";

  return (
    <section className="benchmark-risk-return" aria-labelledby={`benchmark-risk-return-title-${data.setId}`}>
      <header className="benchmark-risk-return-heading">
        <span className="panel-kicker">Risk and return</span>
        <div className="benchmark-risk-return-title-row">
          <h2 id={`benchmark-risk-return-title-${data.setId}`}>Who earned more return for the risk they took?</h2>
          <span
            className="home-info-tip"
            tabIndex={0}
            aria-label="Risk is the CapitalBench allocation-risk score of each frozen portfolio. It is not realized volatility or a Sharpe ratio."
          >
            <Info size={15} aria-hidden="true" />
          </span>
        </div>
        <p>
          Average realized return and frozen portfolio risk across the same {data.roundCount} shared {data.track} {data.roundCount === 1 ? "round" : "rounds"}.
        </p>
      </header>

      <div className="benchmark-risk-return-frame">
        <div className="benchmark-risk-return-chart benchmark-risk-return-chart-desktop">
          <Plot data={data} selectedModelId={selectedModelId} selectModel={setSelectedModelId} compact={false} />
        </div>
        <div className="benchmark-risk-return-chart benchmark-risk-return-chart-mobile">
          <Plot data={data} selectedModelId={selectedModelId} selectModel={setSelectedModelId} compact />
        </div>

        <div className="benchmark-risk-return-legend" aria-label="Models plotted in the risk-return map">
          {data.models.map((model) => (
            <button
              key={model.modelId}
              type="button"
              className={model.modelId === selectedModelId ? "is-selected" : ""}
              aria-pressed={model.modelId === selectedModelId}
              onClick={() => setSelectedModelId(model.modelId)}
              onMouseEnter={() => setSelectedModelId(model.modelId)}
              style={{ "--model-accent": `var(--risk-return-${model.provider || "neutral"})` } as CSSProperties}
            >
              <span className="benchmark-risk-return-rank">{model.returnRank}</span>
              <span className={`benchmark-risk-return-logo ${providerClass(model.provider)}`}>
                {model.logoSrc ? <img src={model.logoSrc} alt="" width="22" height="22" /> : model.label.slice(0, 1)}
              </span>
              <span>
                <strong>{model.label}</strong>
                <small>{model.providerLabel}</small>
              </span>
            </button>
          ))}
        </div>

        {selected ? (
          <div className="benchmark-risk-return-selection" aria-live="polite">
            <div className="benchmark-risk-return-selection-model">
              <span className={`benchmark-risk-return-logo ${providerClass(selected.provider)}`}>
                {selected.logoSrc ? <img src={selected.logoSrc} alt="" width="26" height="26" /> : selected.label.slice(0, 1)}
              </span>
              <span>
                <strong>{selected.label}</strong>
                <small>{selected.providerLabel}</small>
              </span>
            </div>
            <span><strong>{returnLabel(selected.returnPct, true)}</strong><small>average return</small></span>
            <span><strong>{selected.riskScore.toFixed(1)}<em>/100</em></strong><small>{selected.riskLabel}</small></span>
            <span><strong>{alphaLabel(selected.alphaVsBenchmarkPct)}</strong><small>versus S&amp;P 500</small></span>
            <span><strong>{selected.riskMinimum.toFixed(1)}-{selected.riskMaximum.toFixed(1)}</strong><small>risk range</small></span>
            <a href={selected.href} aria-label={`Open ${selected.label} model profile`}>
              <ArrowRight size={17} aria-hidden="true" />
            </a>
          </div>
        ) : null}

        <div className="benchmark-risk-return-findings">
          <p><TrendingUp size={17} aria-hidden="true" /><span><strong>Return leader</strong>{leaderFinding}</span></p>
          <p><Scale size={17} aria-hidden="true" /><span><strong>Benchmark test</strong>{tradeoffFinding}</span></p>
        </div>

        <footer className="benchmark-risk-return-footer">
          <span>
            Risk axis shown from {data.riskDomain.minimum} to {data.riskDomain.maximum} on the full 0-100 scale.
          </span>
          <a href="/risk-appetite/#risk-calculation-title">How allocation risk is measured</a>
        </footer>
      </div>
    </section>
  );
}
