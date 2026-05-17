import type { SubmissionRecord, UniverseOption } from "../data/fallback";

export type DisplayAllocation = {
  option_id: string;
  allocation_pct: number;
  allocation_bps: number;
  rationale?: string;
};

export type OptionLabelMap = Record<string, Pick<UniverseOption, "name" | "symbol" | "is_cash"> | undefined>;

export function formatAllocationPct(value: number): string {
  if (Number.isInteger(value)) return `${value}%`;
  return `${value.toFixed(1)}%`;
}

export function decisionAllocations(row: SubmissionRecord): DisplayAllocation[] {
  if (row.portfolio && row.portfolio.length > 0) {
    return row.portfolio.map((item) => {
      const allocationBps = item.allocation_bps ?? Number(item.allocation_pct ?? 0) * 100;
      return {
        option_id: item.option_id,
        allocation_pct: allocationBps / 100,
        allocation_bps: allocationBps,
        rationale: item.rationale
      };
    });
  }
  if (!row.selected_option_id) return [];
  return [
    {
      option_id: row.selected_option_id,
      allocation_pct: 100,
      allocation_bps: 10000,
      rationale: row.rationale_summary
    }
  ];
}

export function allocationLabel(row: SubmissionRecord): string {
  const allocations = decisionAllocations(row);
  if (allocations.length === 0) return row.selected_option_id;
  return allocations.map((item) => `${item.option_id} ${formatAllocationPct(item.allocation_pct)}`).join(" / ");
}

export function optionDisplayName(optionId: string, optionsById: OptionLabelMap = {}): string {
  const option = optionsById[optionId];
  if (!option) return optionId;
  if (option.is_cash) return option.name || optionId;
  return option.symbol ? `${option.name || optionId} (${option.symbol})` : option.name || optionId;
}

export function allocationDisplayLabel(row: SubmissionRecord, optionsById: OptionLabelMap = {}): string {
  const allocations = decisionAllocations(row);
  if (allocations.length === 0) return optionDisplayName(row.selected_option_id, optionsById);
  return allocations
    .map((item) => `${optionDisplayName(item.option_id, optionsById)} ${formatAllocationPct(item.allocation_pct)}`)
    .join(" / ");
}

export function protocolLabel(row: Pick<SubmissionRecord, "submission_format">): string {
  return row.submission_format === "portfolio" ? "Portfolio round" : "Single-pick round";
}

export function allocationThemeClass(optionId: string): string {
  const normalized = optionId.toUpperCase();
  if (["ENERGY", "OIL", "BROAD_COMMODITIES"].includes(normalized)) return "allocation-energy";
  if (["SEMICONDUCTORS", "TECHNOLOGY", "SOFTWARE", "NASDAQ100", "LARGE_GROWTH"].includes(normalized)) {
    return "allocation-tech";
  }
  if (["GOLD", "MINERS"].includes(normalized)) return "allocation-gold";
  if (["SHORT_TREASURY", "INTERMEDIATE_TREASURY", "LONG_TREASURY", "TIPS", "CASH", "US_DOLLAR"].includes(normalized)) {
    return "allocation-defensive";
  }
  if (["CONSUMER_STAPLES", "UTILITIES", "HEALTHCARE"].includes(normalized)) return "allocation-stable";
  return "allocation-other";
}
