import { ChevronDown, Download, Search } from "lucide-react";
import { Fragment, useEffect, useMemo, useState } from "react";
import { modelLabel, providerLabel, type SubmissionRecord, type UniverseOption } from "../data/fallback";
import {
  allocationDisplayLabel,
  allocationThemeClass,
  decisionAllocations,
  formatAllocationPct,
  optionDisplayName,
  protocolLabel,
  type DisplayAllocation,
  type OptionLabelMap
} from "../lib/allocations";
import { getSupabaseClient, hasSupabaseConfig } from "../lib/supabase";

interface Props {
  fallbackRows: SubmissionRecord[];
  roundId: string;
  runId: string;
  options?: UniverseOption[];
  rankedModelIds?: string[];
}

function csvEscape(value: string | number): string {
  const text = String(value);
  if (/[",\n]/.test(text)) return `"${text.replaceAll('"', '""')}"`;
  return text;
}

function providerClass(provider: string): string {
  return `provider-badge provider-${provider}`;
}

function AllocationPortfolioView({
  allocations,
  optionsById
}: {
  allocations: DisplayAllocation[];
  optionsById: OptionLabelMap;
}) {
  if (allocations.length === 0) {
    return <span className="muted">No allocation</span>;
  }

  return (
    <div className="portfolio-cell">
      <div className="allocation-stack mini" aria-hidden="true">
        {allocations.map((allocation) => (
          <span
            key={allocation.option_id}
            className={allocationThemeClass(allocation.option_id)}
            style={{ width: `${Math.max(3, allocation.allocation_pct)}%` }}
            title={`${optionDisplayName(allocation.option_id, optionsById)} ${formatAllocationPct(allocation.allocation_pct)}`}
          />
        ))}
      </div>
      <div className="allocation-chip-row" aria-label="Portfolio holdings">
        {allocations.map((allocation) => (
          <span
            key={allocation.option_id}
            className="allocation-chip"
            title={`${optionDisplayName(allocation.option_id, optionsById)} ${formatAllocationPct(allocation.allocation_pct)}`}
          >
            <span className={`allocation-dot ${allocationThemeClass(allocation.option_id)}`} aria-hidden="true" />
            <strong>{optionDisplayName(allocation.option_id, optionsById)}</strong>
            <span>{formatAllocationPct(allocation.allocation_pct)}</span>
          </span>
        ))}
      </div>
    </div>
  );
}

export default function OfficialPicksTable({ fallbackRows, roundId, runId, options = [], rankedModelIds = [] }: Props) {
  const [rows, setRows] = useState<SubmissionRecord[]>(fallbackRows);
  const [query, setQuery] = useState("");
  const [expanded, setExpanded] = useState<string | null>(null);
  const optionsById = useMemo<OptionLabelMap>(
    () => Object.fromEntries(options.map((option) => [option.option_id, option])),
    [options]
  );
  const rankByModelId = useMemo(
    () => new Map(rankedModelIds.map((modelId, index) => [modelId, index])),
    [rankedModelIds]
  );

  useEffect(() => {
    const supabase = getSupabaseClient();
    if (!hasSupabaseConfig() || supabase === null) return;
    supabase
      .from("submissions")
      .select("*")
      .eq("published", true)
      .eq("round_id", roundId)
      .eq("run_id", runId)
      .order("provider", { ascending: true })
      .then(({ data, error }) => {
        if (!error && data) setRows(data as SubmissionRecord[]);
      });
  }, [roundId, runId]);

  const filteredRows = useMemo(() => {
    const normalized = query.trim().toLowerCase();
    const sorted = [...rows].sort((a, b) => {
      if (rankByModelId.size > 0) {
        const aRank = rankByModelId.get(a.model_id);
        const bRank = rankByModelId.get(b.model_id);
        if (aRank !== undefined || bRank !== undefined) {
          return (aRank ?? 9999) - (bRank ?? 9999);
        }
      }
      return providerLabel(a.provider).localeCompare(providerLabel(b.provider));
    });
    if (!normalized) return sorted;
    return sorted.filter((row) =>
      [
        modelLabel(row.model_id),
        providerLabel(row.provider),
        row.selected_option_id,
        allocationDisplayLabel(row, optionsById),
        row.portfolio_rationale ?? "",
        row.rationale_summary,
        ...(row.key_risks ?? [])
      ]
        .join(" ")
        .toLowerCase()
        .includes(normalized)
    );
  }, [optionsById, query, rankByModelId, rows]);

  function exportCsv() {
    const header = ["Model", "Provider", "Primary pick", "Portfolio", "Confidence", "Protocol", "Rationale", "Key risks"].join(",");
    const body = filteredRows
      .map((row) =>
        [
          modelLabel(row.model_id),
          providerLabel(row.provider),
          optionDisplayName(row.selected_option_id, optionsById),
          allocationDisplayLabel(row, optionsById),
          row.confidence.toFixed(2),
          protocolLabel(row),
          row.rationale_summary,
          (row.key_risks ?? []).join("; ")
        ]
          .map(csvEscape)
          .join(",")
      )
      .join("\n");
    const blob = new Blob([`${header}\n${body}\n`], { type: "text/csv;charset=utf-8" });
    const url = URL.createObjectURL(blob);
    const anchor = document.createElement("a");
    anchor.href = url;
    anchor.download = "capitalbench-model-portfolios.csv";
    anchor.click();
    URL.revokeObjectURL(url);
  }

  return (
    <div className="picks-shell" aria-label="Model portfolios">
      <div className="table-toolbar">
        <label className="search-box">
          <Search size={16} aria-hidden="true" />
          <input
            value={query}
            onChange={(event) => setQuery(event.target.value)}
            placeholder="Search portfolios"
            aria-label="Search model portfolios"
          />
        </label>
        <button className="small-button" type="button" onClick={exportCsv}>
          <Download size={15} aria-hidden="true" />
          CSV
        </button>
      </div>
      <div className="table-scroll">
        <table className="picks-table">
          <thead>
            <tr>
              <th>Model</th>
              <th>Provider</th>
              <th>Portfolio</th>
              <th className="numeric">Confidence</th>
              <th>Protocol</th>
              <th aria-label="Details"></th>
            </tr>
          </thead>
          <tbody>
            {filteredRows.map((row) => {
              const isExpanded = expanded === row.model_id;
              const allocations = decisionAllocations(row);
              return (
                <Fragment key={row.model_id}>
                  <tr className="picks-row" onClick={() => setExpanded(isExpanded ? null : row.model_id)}>
                    <td data-label="Model">
                      <span className="model-name">{modelLabel(row.model_id)}</span>
                      <br />
                      <span className="muted mono">{row.model_id}</span>
                    </td>
                    <td data-label="Provider">
                      <span className={providerClass(row.provider)}>{providerLabel(row.provider)}</span>
                    </td>
                    <td data-label="Portfolio">
                      <AllocationPortfolioView allocations={allocations} optionsById={optionsById} />
                    </td>
                    <td className="numeric" data-label="Confidence">
                      <div className="pick-cell" style={{ justifyContent: "flex-end" }}>
                        <span>{row.confidence.toFixed(2)}</span>
                        <span className="confidence-bar" aria-hidden="true">
                          <span style={{ width: `${Math.max(4, row.confidence * 100)}%` }}></span>
                        </span>
                      </div>
                    </td>
                    <td data-label="Protocol">
                      <span className="badge badge-neutral">{protocolLabel(row)}</span>
                    </td>
                    <td className="numeric" data-label="Details">
                      <ChevronDown
                        size={17}
                        aria-hidden="true"
                        style={{ transform: isExpanded ? "rotate(180deg)" : "none" }}
                      />
                    </td>
                  </tr>
                  {isExpanded && (
                    <tr className="details-row">
                      <td colSpan={6} data-label="Details">
                        <div className="pick-details">
                          <div>
                            <span className="metric-label">Rationale</span>
                            {row.portfolio_rationale && <p>{row.portfolio_rationale}</p>}
                            <p>{row.rationale_summary}</p>
                          </div>
                          {allocations.length > 0 && (
                            <div>
                              <span className="metric-label">Portfolio</span>
                              <ul>
                                {allocations.map((allocation) => {
                                  return (
                                    <li key={allocation.option_id}>
                                      <strong>{optionDisplayName(allocation.option_id, optionsById)}</strong>:{" "}
                                      {formatAllocationPct(allocation.allocation_pct)}
                                      {allocation.rationale ? ` - ${allocation.rationale}` : ""}
                                    </li>
                                  );
                                })}
                              </ul>
                            </div>
                          )}
                          <div>
                            <span className="metric-label">Key Risks</span>
                            <ul>
                              {(row.key_risks ?? []).map((risk) => (
                                <li key={risk}>{risk}</li>
                              ))}
                            </ul>
                          </div>
                        </div>
                      </td>
                    </tr>
                  )}
                </Fragment>
              );
            })}
          </tbody>
        </table>
      </div>
      {filteredRows.length === 0 && <p className="empty-state">No model portfolios match the current filter.</p>}
    </div>
  );
}
