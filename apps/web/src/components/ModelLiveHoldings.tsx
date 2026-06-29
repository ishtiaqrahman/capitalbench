import { useEffect, useMemo, useState } from "react";
import type { ModelLiveScope, ModelScopeKey } from "../lib/modelProfiles";

type Props = {
  scopes: Record<ModelScopeKey, ModelLiveScope>;
};

const SCOPE_OPTIONS: Array<{ key: ModelScopeKey; label: string }> = [
  { key: "all", label: "All live" },
  { key: "monthly", label: "Monthly" },
  { key: "weekly", label: "Weekly" }
];

function formatPct(value: number | null | undefined): string {
  if (value === null || value === undefined || !Number.isFinite(value)) return "n/a";
  if (Math.abs(value) >= 10) return `${value.toFixed(1)}%`;
  if (Math.abs(value) >= 1) return `${value.toFixed(1)}%`;
  return `${value.toFixed(2)}%`;
}

function formatDate(value?: string): string {
  if (!value) return "Not scheduled";
  return value.slice(0, 10);
}

function portfolioLabel(count: number): string {
  return count === 1 ? "1 portfolio" : `${count} portfolios`;
}

function openPortfolioLabel(count: number): string {
  return count === 1 ? "1 open portfolio" : `${count} open portfolios`;
}

export default function ModelLiveHoldings({ scopes }: Props) {
  const [scopeKey, setScopeKey] = useState<ModelScopeKey>("all");
  const scope = scopes[scopeKey];
  const [selectedOptionId, setSelectedOptionId] = useState<string | null>(scope.topHolding?.optionId ?? null);
  const selectedHolding = useMemo(
    () => scope.holdings.find((holding) => holding.optionId === selectedOptionId) ?? scope.topHolding,
    [scope, selectedOptionId]
  );

  useEffect(() => {
    setSelectedOptionId(scope.topHolding?.optionId ?? null);
  }, [scopeKey, scope.topHolding?.optionId]);

  if (scopes.all.portfolioCount === 0) {
    return (
      <div className="model-live-empty">
        <strong>No open portfolios.</strong>
        <span>This model has no live holdings waiting for final prices.</span>
      </div>
    );
  }

  return (
    <div className="model-live-widget">
      <div className="model-live-tabs" aria-label="Filter current holdings by track">
        {SCOPE_OPTIONS.map((option) => (
          <button
            key={option.key}
            type="button"
            className={scopeKey === option.key ? "is-active" : ""}
            aria-pressed={scopeKey === option.key}
            onClick={() => setScopeKey(option.key)}
          >
            {option.label}
          </button>
        ))}
      </div>

      {scope.portfolioCount > 0 ? (
        <>
          <div className="model-live-chart-grid">
            <div className="model-live-chart-panel">
              <div className="model-live-chart-head">
                <div>
                  <span className="metric-label">{scope.label}</span>
                  <strong>{openPortfolioLabel(scope.portfolioCount)}</strong>
                </div>
                <span>{scope.holdings.length} assets</span>
              </div>

              <div className="model-live-stack" aria-label={`${scope.label} allocation by asset`}>
                {scope.holdings.map((holding) => (
                  <button
                    key={holding.optionId}
                    type="button"
                    className={`${holding.themeClass} ${selectedHolding?.optionId === holding.optionId ? "is-selected" : ""}`}
                    style={{ flexBasis: `${Math.max(holding.exposurePct, 0.5)}%` }}
                    title={`${holding.label}: ${formatPct(holding.exposurePct)}`}
                    aria-label={`${holding.label}: ${formatPct(holding.exposurePct)}`}
                    onClick={() => setSelectedOptionId(holding.optionId)}
                  />
                ))}
              </div>

              <div className="model-live-asset-list">
                {scope.holdings.map((holding) => (
                  <button
                    key={holding.optionId}
                    type="button"
                    className={selectedHolding?.optionId === holding.optionId ? "is-selected" : ""}
                    onClick={() => setSelectedOptionId(holding.optionId)}
                  >
                    <span className={`model-live-dot ${holding.themeClass}`} aria-hidden="true" />
                    <span>
                      <strong>{holding.label}</strong>
                      <small>{holding.group}</small>
                    </span>
                    <em>{portfolioLabel(holding.portfolioCount)}</em>
                    <b>{formatPct(holding.exposurePct)}</b>
                  </button>
                ))}
              </div>
            </div>

            <aside className="model-live-detail" aria-live="polite">
              <div className="model-live-stat-grid">
                <div>
                  <span>Top holding</span>
                  <strong>{scope.topHolding?.label ?? "None"}</strong>
                  <small>{scope.topHolding ? formatPct(scope.topHolding.exposurePct) : "0%"}</small>
                </div>
                <div>
                  <span>Top 3</span>
                  <strong>{formatPct(scope.topThreePct)}</strong>
                  <small>of live exposure</small>
                </div>
                <div>
                  <span>Monthly</span>
                  <strong>{scope.monthlyPortfolioCount}</strong>
                  <small>open portfolios</small>
                </div>
                <div>
                  <span>Weekly</span>
                  <strong>{scope.weeklyPortfolioCount}</strong>
                  <small>open portfolios</small>
                </div>
              </div>

              {selectedHolding && (
                <div className="model-selected-holding">
                  <span className={`model-live-dot ${selectedHolding.themeClass}`} aria-hidden="true" />
                  <div>
                    <span>{selectedHolding.group}</span>
                    <strong>{selectedHolding.label}</strong>
                    <p>
                      {formatPct(selectedHolding.exposurePct)} across {portfolioLabel(selectedHolding.portfolioCount)}.
                    </p>
                  </div>
                </div>
              )}

              <div className="model-live-rounds">
                <span className="metric-label">Included active rounds</span>
                {selectedHolding ? (
                  selectedHolding.rounds.map((round) => (
                    <a href={`/rounds/${round.roundId}/`} key={`${round.roundId}-${round.track}-${round.allocationPct}`}>
                      <span>{round.roundId}</span>
                      <strong>{formatPct(round.allocationPct)}</strong>
                      <small>{round.track} / scores {formatDate(round.scoreEtaUtc ?? round.exitDate)}</small>
                    </a>
                  ))
                ) : (
                  <p>No active round data.</p>
                )}
              </div>
            </aside>
          </div>

          <div className="model-live-footnote">
            <span>Completed rounds are excluded from this live view.</span>
            <span>Next scoring target: {formatDate(scope.nextScoreDate)}</span>
          </div>
        </>
      ) : (
        <div className="model-live-empty compact">
          <strong>No {scope.label.toLowerCase()} holdings.</strong>
          <span>Choose another track to see this model's open portfolios.</span>
        </div>
      )}
    </div>
  );
}
