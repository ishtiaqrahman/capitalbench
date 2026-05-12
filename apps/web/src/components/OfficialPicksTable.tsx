import { ChevronDown, Download, Search } from "lucide-react";
import { Fragment, useEffect, useMemo, useState } from "react";
import { modelLabel, providerLabel, type SubmissionRecord } from "../data/fallback";
import { getSupabaseClient, hasSupabaseConfig } from "../lib/supabase";

interface Props {
  fallbackRows: SubmissionRecord[];
  roundId: string;
  runId: string;
}

function csvEscape(value: string | number): string {
  const text = String(value);
  if (/[",\n]/.test(text)) return `"${text.replaceAll('"', '""')}"`;
  return text;
}

function providerClass(provider: string): string {
  return `provider-badge provider-${provider}`;
}

export default function OfficialPicksTable({ fallbackRows, roundId, runId }: Props) {
  const [rows, setRows] = useState<SubmissionRecord[]>(fallbackRows);
  const [query, setQuery] = useState("");
  const [expanded, setExpanded] = useState<string | null>(fallbackRows[0]?.model_id ?? null);

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
        if (!error && data) {
          setRows(data as SubmissionRecord[]);
          setExpanded((data as SubmissionRecord[])[0]?.model_id ?? null);
        }
      });
  }, [roundId, runId]);

  const filteredRows = useMemo(() => {
    const normalized = query.trim().toLowerCase();
    const sorted = [...rows].sort((a, b) => providerLabel(a.provider).localeCompare(providerLabel(b.provider)));
    if (!normalized) return sorted;
    return sorted.filter((row) =>
      [
        modelLabel(row.model_id),
        providerLabel(row.provider),
        row.selected_option_id,
        row.rationale_summary,
        ...(row.key_risks ?? [])
      ]
        .join(" ")
        .toLowerCase()
        .includes(normalized)
    );
  }, [query, rows]);

  function exportCsv() {
    const header = ["Model", "Provider", "Pick", "Confidence", "Status", "Rationale", "Key risks"].join(",");
    const body = filteredRows
      .map((row) =>
        [
          modelLabel(row.model_id),
          providerLabel(row.provider),
          row.selected_option_id,
          row.confidence.toFixed(2),
          "Pending",
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
    anchor.download = "capitalbench-official-picks.csv";
    anchor.click();
    URL.revokeObjectURL(url);
  }

  return (
    <div className="picks-shell" aria-label="Official one-shot picks">
      <div className="table-toolbar">
        <label className="search-box">
          <Search size={16} aria-hidden="true" />
          <input
            value={query}
            onChange={(event) => setQuery(event.target.value)}
            placeholder="Search picks"
            aria-label="Search official picks"
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
              <th>Pick</th>
              <th className="numeric">Confidence</th>
              <th>Status</th>
              <th aria-label="Details"></th>
            </tr>
          </thead>
          <tbody>
            {filteredRows.map((row) => {
              const isExpanded = expanded === row.model_id;
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
                    <td data-label="Pick">
                      <div className="pick-cell">
                        <strong>{row.selected_option_id}</strong>
                      </div>
                    </td>
                    <td className="numeric" data-label="Confidence">
                      <div className="pick-cell" style={{ justifyContent: "flex-end" }}>
                        <span>{row.confidence.toFixed(2)}</span>
                        <span className="confidence-bar" aria-hidden="true">
                          <span style={{ width: `${Math.max(4, row.confidence * 100)}%` }}></span>
                        </span>
                      </div>
                    </td>
                    <td data-label="Status">
                      <span className="status-badge status-pending">Pending</span>
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
                            <p>{row.rationale_summary}</p>
                          </div>
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
      {filteredRows.length === 0 && <p className="empty-state">No official picks match the current filter.</p>}
    </div>
  );
}
