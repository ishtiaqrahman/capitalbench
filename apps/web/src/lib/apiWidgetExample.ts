type AnyRecord = Record<string, any>;

const formatNumber = (value: number | null | undefined, digits = 1) =>
  typeof value === "number" && Number.isFinite(value) ? value.toFixed(digits) : "n/a";

const roundedNumber = (value: number | null | undefined, digits = 1) =>
  typeof value === "number" && Number.isFinite(value) ? Number(value.toFixed(digits)) : null;

const categoryLabel = (value: string | null | undefined) =>
  String(value || "unknown")
    .split("_")
    .filter(Boolean)
    .map((part) => {
      const lower = part.toLowerCase();
      if (lower === "ai") return "AI";
      if (lower === "us") return "US";
      if (lower === "sp500") return "S&P 500";
      return part.charAt(0).toUpperCase() + part.slice(1);
    })
    .join(" ");

const formatDateTimeUtc = (value: string) => {
  const date = new Date(value);
  if (Number.isNaN(date.getTime())) return value;
  return new Intl.DateTimeFormat("en-US", {
    month: "short",
    day: "numeric",
    year: "numeric",
    hour: "numeric",
    minute: "2-digit",
    timeZone: "UTC",
    timeZoneName: "short"
  }).format(date);
};

const humanList = (items: string[], limit = 3) => {
  const values = items.filter(Boolean).slice(0, limit);
  if (values.length === 0) return "";
  if (values.length === 1) return values[0];
  if (values.length === 2) return `${values[0]} and ${values[1]}`;
  return `${values.slice(0, -1).join(", ")}, and ${values.at(-1)}`;
};

const mean = (values: number[]) => (values.length ? values.reduce((total, value) => total + value, 0) / values.length : 0);

const standardDeviation = (values: number[]) => {
  if (values.length === 0) return 0;
  const average = mean(values);
  return Math.sqrt(mean(values.map((value) => (value - average) ** 2)));
};

const modelDescriptor = (modelsById: Map<string, AnyRecord>, modelId: string) => {
  const model = modelsById.get(modelId);
  const modelName = model?.label ?? modelId;
  const provider = model?.provider_label ?? model?.provider ?? null;
  return {
    model_id: modelId,
    model_name: modelName,
    label: modelName,
    provider,
    display_label: provider ? `${modelName} (${provider})` : modelName
  };
};

const stanceLabel = (allocationPct: number, isHolder = true) => {
  if (!isHolder) return "Not holding";
  if (allocationPct >= 25) return "Heavy holder";
  if (allocationPct >= 10) return "Material holder";
  if (allocationPct >= 3) return "Small holder";
  return "Token holder";
};

const agreementLabel = (holderCount: number, activeModelCount: number) => {
  if (activeModelCount === 0) return "No active model data";
  const share = holderCount / activeModelCount;
  if (holderCount === activeModelCount) return "Unanimous ownership";
  if (share >= 0.75) return "High agreement";
  if (share >= 0.4) return "Mixed agreement";
  return "Low agreement";
};

const dispersionLabel = (rangePct: number, nonHolderCount: number) => {
  if (nonHolderCount > 0 && rangePct >= 12) return "Split ownership, wide sizing";
  if (nonHolderCount > 0) return "Split ownership";
  if (rangePct >= 15) return "Consensus ownership, wide sizing";
  if (rangePct >= 7) return "Consensus ownership, varied sizing";
  return "Tight sizing";
};

const crowdingLabel = (rank: number, holderSharePct: number) => {
  if (rank <= 3 && holderSharePct >= 70) return "Crowded AI-model position";
  if (rank <= 5 || holderSharePct >= 75) return "High-interest AI-model position";
  if (holderSharePct <= 40) return "Selective AI-model position";
  return "Contested AI-model position";
};

const buildInterpretation = (asset: AnyRecord) => {
  const ticker = asset.ticker || asset.optionId;
  const holderNames = asset.holders.map((holder: AnyRecord) => holder.model_name);
  const nonHolderNames = asset.nonHolders.map((model: AnyRecord) => model.model_name);
  const mostBullish = asset.mostBullishModel;
  const leastBullish = asset.leastBullishHolder;

  if (asset.modelCount === 0) {
    return `No active model currently holds ${ticker}, so the panel would present it as an avoided exposure rather than an AI consensus idea.`;
  }

  if (asset.modelCount === asset.activeModelCount) {
    return `All ${asset.activeModelCount} named models hold ${ticker}; the largest holders include ${humanList(holderNames)}. ${mostBullish?.model_name ?? "The largest holder"} has the largest active allocation at ${formatNumber(mostBullish?.average_allocation_pct, 1)}%, while ${leastBullish?.model_name ?? "the smallest holder"} is at ${formatNumber(leastBullish?.average_allocation_pct, 1)}%, a ${asset.allocationRangePct} percentage-point sizing spread.`;
  }

  return `${ticker} holders include ${humanList(holderNames)}, while non-holders include ${humanList(nonHolderNames)}. That makes the signal useful as a model-disagreement read: the asset has active AI demand, but it is not a consensus position across the full model set.`;
};

export function buildApiWidgetDemo(readModel: AnyRecord) {
  const generatedAt = readModel.generated_at ?? new Date().toISOString();
  const activeAllocations = (readModel.allocations ?? []).filter((row: AnyRecord) => row.status === "active");
  const assetsById = new Map<string, AnyRecord>((readModel.assets ?? []).map((asset: AnyRecord) => [asset.option_id, asset]));
  const modelsById = new Map<string, AnyRecord>((readModel.models ?? []).map((model: AnyRecord) => [model.model_id, model]));
  const activePortfolioKeys = new Set(activeAllocations.map((row: AnyRecord) => `${row.round_id}:${row.run_id}:${row.model_id}`));
  const activeModelIds = new Set<string>(activeAllocations.map((row: AnyRecord) => row.model_id));
  const activeModelDescriptors = Array.from(activeModelIds)
    .sort((left, right) => modelDescriptor(modelsById, left).model_name.localeCompare(modelDescriptor(modelsById, right).model_name))
    .map((modelId) => modelDescriptor(modelsById, modelId));
  const activeRoundIds = Array.from(new Set(activeAllocations.map((row: AnyRecord) => row.round_id))).sort().reverse();
  const activePortfolioCount = Math.max(1, activePortfolioKeys.size);
  const aggregateByAsset = new Map<string, AnyRecord>();

  for (const row of activeAllocations) {
    const asset = assetsById.get(row.option_id) ?? row;
    const existing =
      aggregateByAsset.get(row.option_id) ??
      {
        option_id: row.option_id,
        label: asset.label ?? row.label ?? row.option_id,
        ticker: asset.ticker ?? row.ticker ?? null,
        category: asset.category ?? row.category ?? "unknown",
        asset_class: asset.asset_class ?? row.asset_class ?? "unknown",
        allocation_pct: 0,
        model_ids: new Set<string>(),
        portfolio_keys: new Set<string>(),
        holders: new Map<string, AnyRecord>()
      };

    existing.allocation_pct += Number(row.allocation_pct ?? 0) / activePortfolioCount;
    existing.model_ids.add(row.model_id);
    existing.portfolio_keys.add(`${row.round_id}:${row.run_id}:${row.model_id}`);

    const descriptor = modelDescriptor(modelsById, row.model_id);
    const holder =
      existing.holders.get(row.model_id) ??
      {
        ...descriptor,
        total_allocation_pct: 0,
        holding_count: 0,
        rationale: row.rationale ?? null
      };
    holder.total_allocation_pct += Number(row.allocation_pct ?? 0);
    holder.holding_count += 1;
    holder.rationale = holder.rationale ?? row.rationale ?? null;
    existing.holders.set(row.model_id, holder);
    aggregateByAsset.set(row.option_id, existing);
  }

  const rawAssets = Array.from(aggregateByAsset.values()).map((asset) => {
    const holders = Array.from((asset.holders as Map<string, AnyRecord>).values())
      .map((holder: AnyRecord) => {
        const averageAllocation = holder.holding_count ? holder.total_allocation_pct / holder.holding_count : 0;
        return {
          model_id: holder.model_id,
          model_name: holder.model_name,
          label: holder.model_name,
          provider: holder.provider,
          display_label: holder.display_label,
          average_allocation_pct: averageAllocation,
          allocationPct: formatNumber(averageAllocation, 1),
          stance: stanceLabel(averageAllocation),
          rationale: holder.rationale
        };
      })
      .sort((left: AnyRecord, right: AnyRecord) => right.average_allocation_pct - left.average_allocation_pct || left.model_name.localeCompare(right.model_name));
    const nonHolders = activeModelDescriptors
      .filter((model) => !(asset.model_ids as Set<string>).has(model.model_id))
      .map((model) => ({ ...model, average_allocation_pct: 0, allocationPct: "0.0", stance: stanceLabel(0, false) }));
    const holderAllocations = holders.map((holder: AnyRecord) => holder.average_allocation_pct);
    const activeAllocationsByModel = activeModelDescriptors.map((model) => holders.find((holder: AnyRecord) => holder.model_id === model.model_id)?.average_allocation_pct ?? 0);
    const maxHolderAllocation = holderAllocations.length ? Math.max(...holderAllocations) : 0;
    const minHolderAllocation = holderAllocations.length ? Math.min(...holderAllocations) : 0;
    const allocationRange = maxHolderAllocation - minHolderAllocation;
    const holderSharePct = activeModelDescriptors.length ? ((asset.model_ids as Set<string>).size / activeModelDescriptors.length) * 100 : 0;
    const mostBullishModel = holders[0] ?? null;
    const leastBullishHolder = holders.at(-1) ?? null;

    return {
      optionId: asset.option_id,
      label: asset.label,
      ticker: asset.ticker ?? asset.option_id,
      categoryLabel: categoryLabel(asset.category),
      assetClass: categoryLabel(asset.asset_class),
      allocationPct: formatNumber(asset.allocation_pct, 1),
      allocationPctNumber: roundedNumber(asset.allocation_pct, 2),
      modelCount: (asset.model_ids as Set<string>).size,
      activeModelCount: activeModelDescriptors.length,
      holderSharePct: formatNumber(holderSharePct, 0),
      portfolioHoldingCount: (asset.portfolio_keys as Set<string>).size,
      activePortfolioCount,
      holders,
      nonHolders,
      topHolders: holders.slice(0, 4),
      mostBullishModel,
      leastBullishHolder,
      allocationRangePct: formatNumber(allocationRange, 1),
      allocationStdDevPct: formatNumber(standardDeviation(activeAllocationsByModel), 1),
      agreementLabel: agreementLabel((asset.model_ids as Set<string>).size, activeModelDescriptors.length),
      dispersionLabel: dispersionLabel(allocationRange, nonHolders.length)
    };
  });

  const rankedAssets = rawAssets.sort((left, right) => Number(right.allocationPctNumber ?? 0) - Number(left.allocationPctNumber ?? 0) || left.label.localeCompare(right.label));
  const assets = rankedAssets.slice(0, 5).map((asset, index) => {
    const rank = index + 1;
    const relatedAssets = rankedAssets
      .filter((related) => related.optionId !== asset.optionId)
      .slice(0, 3)
      .map((related) => ({
        option_id: related.optionId,
        ticker: related.ticker,
        label: related.label,
        average_allocation_pct: related.allocationPctNumber,
        holder_count: related.modelCount,
        agreement_label: related.agreementLabel
      }));
    const enrichedAsset = {
      ...asset,
      crowdingRank: rank,
      crowdingLabel: crowdingLabel(rank, Number(asset.holderSharePct)),
      relatedAssets
    };
    const interpretation = buildInterpretation(enrichedAsset);
    const apiPaths = [
      `/v1/positioning/by-asset/${asset.optionId}?scope=active&track=all`,
      `/v1/assets/${asset.optionId}/model-holders?scope=active&track=all`,
      "/v1/positioning/active?track=all&group_by=asset",
      "/v1/positioning/consensus?track=all",
      "/v1/positioning/changes?track=all&group_by=asset"
    ];
    const sampleJson = {
      asset: {
        option_id: asset.optionId,
        ticker: asset.ticker,
        label: asset.label,
        category: asset.categoryLabel
      },
      positioning_signal: {
        average_allocation_pct: asset.allocationPctNumber,
        holder_count: asset.modelCount,
        active_model_count: asset.activeModelCount,
        holder_share_pct: roundedNumber(Number(asset.holderSharePct), 0),
        agreement_label: enrichedAsset.agreementLabel,
        crowding_label: enrichedAsset.crowdingLabel,
        dispersion_label: enrichedAsset.dispersionLabel,
        allocation_range_pp: roundedNumber(Number(asset.allocationRangePct), 1),
        allocation_stddev_pp: roundedNumber(Number(asset.allocationStdDevPct), 1),
        most_bullish_model: asset.mostBullishModel
          ? {
              model_id: asset.mostBullishModel.model_id,
              model_name: asset.mostBullishModel.model_name,
              provider: asset.mostBullishModel.provider,
              average_allocation_pct: roundedNumber(asset.mostBullishModel.average_allocation_pct, 2)
            }
          : null,
        least_bullish_holder: asset.leastBullishHolder
          ? {
              model_id: asset.leastBullishHolder.model_id,
              model_name: asset.leastBullishHolder.model_name,
              provider: asset.leastBullishHolder.provider,
              average_allocation_pct: roundedNumber(asset.leastBullishHolder.average_allocation_pct, 2)
            }
          : null,
        holders: asset.holders.slice(0, 5).map((holder: AnyRecord) => ({
          model_id: holder.model_id,
          model_name: holder.model_name,
          provider: holder.provider,
          stance: holder.stance,
          average_allocation_pct: roundedNumber(holder.average_allocation_pct, 2)
        })),
        non_holders: asset.nonHolders.map((model: AnyRecord) => ({
          model_id: model.model_id,
          model_name: model.model_name,
          provider: model.provider
        })),
        related_assets: relatedAssets
      },
      interpretation
    };

    return {
      ...enrichedAsset,
      interpretation,
      apiPaths,
      integrationSnippet: `<CapitalBenchPanel asset="${asset.ticker ?? asset.optionId}" view="model-positioning" />`,
      sampleJson
    };
  });

  return {
    generatedAt,
    generatedAtDisplay: formatDateTimeUtc(generatedAt),
    activeRoundIds,
    activePortfolioCount,
    activeModelCount: activeModelDescriptors.length,
    assets
  };
}
