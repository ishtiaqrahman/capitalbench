import type { SubmissionRecord, UniverseOption } from "../data/fallback";
import { decisionAllocations } from "./allocations";

export type ConcentrationHolder = {
  modelId: string;
  provider: string;
  allocationPct: number;
  allocationBps: number;
};

export type ConcentrationAsset = {
  optionId: string;
  option?: UniverseOption;
  averagePct: number;
  totalBps: number;
  modelCount: number;
  holders: ConcentrationHolder[];
  categoryKey: string;
  categoryLabel: string;
};

export type ConcentrationCategory = {
  key: string;
  label: string;
  averagePct: number;
  assetCount: number;
};

export type RunConcentration = {
  modelCount: number;
  assets: ConcentrationAsset[];
  categories: ConcentrationCategory[];
  topAsset?: ConcentrationAsset;
  topAssetSharePct: number;
  topThreeSharePct: number;
  effectiveAssetCount: number;
};

const TECH_IDS = new Set([
  "NASDAQ100",
  "LARGE_GROWTH",
  "TECHNOLOGY",
  "SEMICONDUCTORS",
  "SOFTWARE",
  "BROAD_AI_TECH",
  "ROBOTICS",
  "CYBERSECURITY"
]);

function concentrationCategory(optionId: string, option?: UniverseOption): { key: string; label: string } {
  const group = option?.option_group ?? "";
  if (TECH_IDS.has(optionId) || group === "ai_and_technology" || group === "us_growth_and_technology") {
    return { key: "technology", label: "AI / technology" };
  }
  if (group === "international_equity" || group === "country_equity") {
    return { key: "international", label: "International equity" };
  }
  if (["cash", "cash_and_short_duration", "bonds_and_rates", "credit"].includes(group)) {
    return { key: "bonds", label: "Cash / bonds / credit" };
  }
  if (["commodities", "currencies", "crypto_proxies"].includes(group)) {
    return { key: "alternatives", label: "Real assets / alternatives" };
  }
  if (["us_broad_market", "us_style_factor", "us_size_factor", "us_factor_equity", "us_sector", "us_industry", "healthcare_and_biotech"].includes(group)) {
    return { key: "us_equity", label: "US equity / sectors" };
  }
  return { key: "other", label: "Other" };
}

export function buildRunConcentration(
  submissions: SubmissionRecord[],
  optionsById: Record<string, UniverseOption | undefined>
): RunConcentration {
  const totals = new Map<string, { totalBps: number; holders: ConcentrationHolder[] }>();
  const modelCount = submissions.length;

  for (const submission of submissions) {
    for (const allocation of decisionAllocations(submission)) {
      const existing = totals.get(allocation.option_id) ?? { totalBps: 0, holders: [] };
      existing.totalBps += allocation.allocation_bps;
      existing.holders.push({
        modelId: submission.model_id,
        provider: submission.provider,
        allocationPct: allocation.allocation_pct,
        allocationBps: allocation.allocation_bps
      });
      totals.set(allocation.option_id, existing);
    }
  }

  const assets = Array.from(totals.entries())
    .map(([optionId, value]) => {
      const option = optionsById[optionId];
      const category = concentrationCategory(optionId, option);
      return {
        optionId,
        option,
        averagePct: modelCount > 0 ? value.totalBps / modelCount / 100 : 0,
        totalBps: value.totalBps,
        modelCount: value.holders.length,
        holders: value.holders.sort((a, b) => b.allocationBps - a.allocationBps),
        categoryKey: category.key,
        categoryLabel: category.label
      };
    })
    .sort((a, b) => b.averagePct - a.averagePct || a.optionId.localeCompare(b.optionId));

  const categoryTotals = new Map<string, { label: string; averagePct: number; assetCount: number }>();
  for (const asset of assets) {
    const existing = categoryTotals.get(asset.categoryKey) ?? {
      label: asset.categoryLabel,
      averagePct: 0,
      assetCount: 0
    };
    existing.averagePct += asset.averagePct;
    existing.assetCount += 1;
    categoryTotals.set(asset.categoryKey, existing);
  }

  const categories = Array.from(categoryTotals.entries())
    .map(([key, value]) => ({ key, ...value }))
    .sort((a, b) => b.averagePct - a.averagePct || a.label.localeCompare(b.label));
  const concentrationScore = assets.reduce((total, asset) => total + (asset.averagePct / 100) ** 2, 0);

  return {
    modelCount,
    assets,
    categories,
    topAsset: assets[0],
    topAssetSharePct: assets[0]?.averagePct ?? 0,
    topThreeSharePct: assets.slice(0, 3).reduce((total, asset) => total + asset.averagePct, 0),
    effectiveAssetCount: concentrationScore > 0 ? 1 / concentrationScore : 0
  };
}
