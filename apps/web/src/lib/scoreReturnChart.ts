import {
  modelLabel,
  providerLabel,
  type LeaderboardRecord,
  type UniverseOption
} from "../data/fallback";
import { allocationThemeClass, formatAllocationPct, optionDisplayName, optionShortDisplayName } from "./allocations";
import { pct } from "./format";
import type { ResultAllocationRecord, ResultReturnRecord } from "./localRoundRecords";

export type ScoreReturnChartRowKind = "model" | "benchmark" | "reference";

export type ScoreReturnChartHolding = {
  optionId: string;
  label: string;
  fullLabel: string;
  allocationPct: number;
  allocationLabel: string;
  themeClass: string;
};

export type ScoreReturnChartRow = {
  key: string;
  kind: ScoreReturnChartRowKind;
  label: string;
  detailName: string;
  detailMeta: string;
  detailText: string;
  logoSrc?: string;
  logoAlt: string;
  returnValue?: number;
  returnLabel: string;
  vsBenchmarkLabel: string;
  barStyle: string;
  valueStyle: string;
  mobileBarStyle: string;
  barClass: string;
  columnClass: string;
  holdings: ScoreReturnChartHolding[];
};

export type ScoreReturnChartTick = {
  value: number;
  label: string;
  position: string;
};

export type ScoreReturnChartData = {
  rows: ScoreReturnChartRow[];
  ticks: ScoreReturnChartTick[];
};

type BuildScoreReturnChartDataArgs = {
  leaderboard: LeaderboardRecord[];
  returns: ResultReturnRecord[];
  optionsById: Record<string, UniverseOption | undefined>;
  allocations?: ResultAllocationRecord[];
};

function finiteNumber(value: number | null | undefined): value is number {
  return typeof value === "number" && Number.isFinite(value);
}

function leaderboardReturn(row: LeaderboardRecord): number | undefined {
  return row.portfolio_return ?? row.selected_asset_return;
}

function percentagePoints(value: number | null | undefined): string {
  if (!finiteNumber(value)) return "n/a";
  return `${(value * 100).toFixed(2)} pp`;
}

function signedPercentagePoints(value: number | null | undefined): string {
  if (!finiteNumber(value)) return "n/a";
  const formatted = percentagePoints(value);
  return value > 0 ? `+${formatted}` : formatted;
}

export function providerLogoSrc(provider: string): string | undefined {
  const logos: Record<string, string> = {
    anthropic: "/labs/icons/claude-icon.svg",
    google: "/labs/icons/gemini-icon.svg",
    openai: "/labs/icons/openai-icon.svg",
    xai: "/labs/icons/xai-icon.svg"
  };
  return logos[provider];
}

function resultAssetLabel(asset?: { label: string; asset_symbol: string }): string {
  if (!asset) return "Not available";
  return asset.asset_symbol ? `${asset.label} (${asset.asset_symbol})` : asset.label;
}

function scoreChartModelColorClass(modelId: string, index: number): string {
  const modelColors: Record<string, string> = {
    "openai-gpt-5-5": "score-bar-openai",
    "xai-grok-4-3": "score-bar-xai",
    "anthropic-claude-opus-4-7": "score-bar-anthropic",
    "anthropic-claude-opus-4-8": "score-bar-anthropic-alt",
    "google-gemini-3-1-pro": "score-bar-google"
  };
  return modelColors[modelId] ?? `score-bar-model-${(index % 5) + 1}`;
}

export function buildScoreReturnChartData({
  leaderboard,
  returns,
  optionsById,
  allocations = []
}: BuildScoreReturnChartDataArgs): ScoreReturnChartData {
  const benchmarkReturn = leaderboard[0]?.sp500_return;
  const allocationsByModel = new Map<string, ResultAllocationRecord[]>();
  for (const allocation of allocations) {
    const modelAllocations = allocationsByModel.get(allocation.model_id) ?? [];
    modelAllocations.push(allocation);
    allocationsByModel.set(allocation.model_id, modelAllocations);
  }
  for (const modelAllocations of allocationsByModel.values()) {
    modelAllocations.sort((a, b) => a.allocation_rank - b.allocation_rank || b.allocation_bps - a.allocation_bps);
  }
  const bestResultAsset = returns
    .filter((item) => !item.is_benchmark && !item.is_cash && finiteNumber(item.return))
    .sort((a, b) => b.return - a.return)[0];
  const values = [
    ...leaderboard.map(leaderboardReturn).filter(finiteNumber),
    ...(finiteNumber(benchmarkReturn) ? [benchmarkReturn] : []),
    ...(finiteNumber(bestResultAsset?.return) ? [bestResultAsset.return] : [])
  ];
  const chartMin = Math.min(0, ...values);
  const chartMax = Math.max(0, ...values);
  const tickStep = chartMax > 0.1 ? 0.05 : 0.02;
  const topTick = Math.max(tickStep, Math.ceil(chartMax / tickStep) * tickStep);
  const padding = Math.max((chartMax - chartMin) * 0.08, 0.005);
  const domainMin = chartMin < 0 ? chartMin - padding : 0;
  const domainMax = chartMax > 0 ? topTick : padding;
  const range = Math.max(domainMax - domainMin, 0.001);
  const coordinate = (value: number) => Math.min(100, Math.max(0, ((value - domainMin) / range) * 100));
  const yPosition = (value: number | null | undefined) => `${coordinate(finiteNumber(value) ? value : 0).toFixed(2)}%`;
  const tickLabel = (value: number) => {
    if (Math.abs(value) < 0.00001) return "0%";
    return `${(value * 100).toFixed(tickStep >= 0.01 ? 0 : 1)}%`;
  };
  const verticalBarStyle = (value: number | null | undefined) => {
    if (!finiteNumber(value)) return "bottom: 0%; height: 0%;";
    const zero = coordinate(0);
    const endpoint = coordinate(value);
    return `bottom: ${Math.min(zero, endpoint).toFixed(2)}%; height: ${Math.max(1.5, Math.abs(endpoint - zero)).toFixed(2)}%;`;
  };
  const mobileBarStyle = (value: number | null | undefined) => {
    if (!finiteNumber(value)) return "width: 0%;";
    const zero = coordinate(0);
    const endpoint = coordinate(value);
    return `width: ${Math.max(2, Math.abs(endpoint - zero)).toFixed(2)}%;`;
  };
  const ticks =
    domainMin < 0
      ? [domainMin, 0, domainMax]
      : Array.from({ length: Math.round(domainMax / tickStep) + 1 }, (_, index) => index * tickStep);
  const holdingsForModel = (row: LeaderboardRecord): ScoreReturnChartHolding[] => {
    const savedAllocations = allocationsByModel.get(row.model_id) ?? [];
    const sourceAllocations = savedAllocations.length
      ? savedAllocations
      : row.selected_option_id
        ? [
            {
              option_id: row.selected_option_id,
              allocation_pct: 100,
              allocation_bps: 10000
            }
          ]
        : [];
    return sourceAllocations.map((allocation) => {
      const allocationPct = finiteNumber(allocation.allocation_pct)
        ? allocation.allocation_pct
        : finiteNumber(allocation.allocation_bps)
          ? allocation.allocation_bps / 100
          : 0;
      return {
        optionId: allocation.option_id,
        label: optionShortDisplayName(allocation.option_id, optionsById),
        fullLabel: optionDisplayName(allocation.option_id, optionsById),
        allocationPct,
        allocationLabel: formatAllocationPct(allocationPct),
        themeClass: allocationThemeClass(allocation.option_id)
      };
    });
  };
  const modelRows: ScoreReturnChartRow[] = leaderboard.map((row, index) => {
    const returnValue = leaderboardReturn(row);
    const providerName = providerLabel(row.provider);
    const holdings = holdingsForModel(row);
    const detailText = holdings.length
      ? `Holdings: ${holdings.map((holding) => `${holding.fullLabel} ${holding.allocationLabel}`).join(" / ")}`
      : "No holdings reported";
    return {
      key: row.model_id,
      kind: "model",
      label: modelLabel(row.model_id),
      detailName: modelLabel(row.model_id),
      detailMeta: providerName,
      detailText,
      logoSrc: providerLogoSrc(row.provider),
      logoAlt: providerName,
      returnValue,
      returnLabel: pct(returnValue) || "n/a",
      vsBenchmarkLabel: signedPercentagePoints(row.alpha_vs_sp500),
      barStyle: verticalBarStyle(returnValue),
      valueStyle: `bottom: calc(${yPosition(returnValue)} + 8px);`,
      mobileBarStyle: mobileBarStyle(returnValue),
      barClass: scoreChartModelColorClass(row.model_id, index),
      columnClass: index === 0 ? "score-vertical-column-winner" : "",
      holdings
    };
  });
  const benchmarkRow: ScoreReturnChartRow | undefined = finiteNumber(benchmarkReturn)
    ? {
        key: "sp500-benchmark",
        kind: "benchmark",
        label: "S&P 500",
        detailName: "S&P 500",
        detailMeta: "Benchmark",
        detailText: "Benchmark return over the same scoring window",
        logoAlt: "S&P 500",
        returnValue: benchmarkReturn,
        returnLabel: pct(benchmarkReturn) || "n/a",
        vsBenchmarkLabel: "0.00 pp",
        barStyle: verticalBarStyle(benchmarkReturn),
        valueStyle: `bottom: calc(${yPosition(benchmarkReturn)} + 8px);`,
        mobileBarStyle: mobileBarStyle(benchmarkReturn),
        barClass: "score-bar-benchmark",
        columnClass: "score-vertical-column-benchmark",
        holdings: []
      }
    : undefined;
  const bestAssetRow: ScoreReturnChartRow | undefined = bestResultAsset
    ? {
        key: "best-universe-asset",
        kind: "reference",
        label: "Max",
        detailName: "Max possible",
        detailMeta: bestResultAsset.asset_symbol || bestResultAsset.label,
        detailText: `100% ${resultAssetLabel(bestResultAsset)} hindsight ceiling`,
        logoAlt: "Maximum possible return",
        returnValue: bestResultAsset.return,
        returnLabel: pct(bestResultAsset.return) || "n/a",
        vsBenchmarkLabel:
          finiteNumber(benchmarkReturn) && finiteNumber(bestResultAsset.return)
            ? signedPercentagePoints(bestResultAsset.return - benchmarkReturn)
            : "n/a",
        barStyle: verticalBarStyle(bestResultAsset.return),
        valueStyle: `bottom: calc(${yPosition(bestResultAsset.return)} + 8px);`,
        mobileBarStyle: mobileBarStyle(bestResultAsset.return),
        barClass: "score-bar-best-asset",
        columnClass: "score-vertical-column-best-asset",
        holdings: []
      }
    : undefined;
  return {
    rows: [
      ...modelRows,
      ...(benchmarkRow ? [benchmarkRow] : []),
      ...(bestAssetRow ? [bestAssetRow] : [])
    ],
    ticks: ticks.map((tick) => ({
      value: tick,
      label: tickLabel(tick),
      position: yPosition(tick)
    }))
  };
}
