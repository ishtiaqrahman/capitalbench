export type MarketRegimePreviewDirection = "down" | "up";

export type MarketRegimePreviewItem = {
  direction: MarketRegimePreviewDirection;
  rangeLabel: string;
  ready: boolean;
  confidence: string;
  modelId?: string;
  modelLabel?: string;
  provider?: string;
  averageReturn?: number;
  averageSp500Return?: number;
  averageAlpha?: number;
  matchingResults: number;
  availableResults: number;
};

export type MarketRegimePreview = {
  dataAsOf?: string;
  readyEnvironmentCount: number;
  totalEnvironmentCount: number;
  items: MarketRegimePreviewItem[];
};

function finiteNumber(value: unknown): value is number {
  return typeof value === "number" && Number.isFinite(value);
}

export function buildMonthlyMarketRegimePreview(marketEnvironment: any): MarketRegimePreview {
  const track = marketEnvironment?.tracks?.monthly ?? {};
  const definitions = marketEnvironment?.definitions?.monthly ?? {};
  const environmentThreshold = Number(marketEnvironment?.thresholds?.environment_rounds ?? 3);
  const environments = Array.isArray(track.environments) ? track.environments : [];
  const signals = Array.isArray(track.signals) ? track.signals : [];
  const directionDefinitions = new Map(
    (Array.isArray(definitions.directions) ? definitions.directions : []).map((definition: any) => [
      String(definition.key),
      definition
    ])
  );

  const items = (["down", "up"] as MarketRegimePreviewDirection[]).map((direction) => {
    const signal = signals.find(
      (candidate: any) => candidate?.kind === "direction_leader" && candidate?.direction === direction
    );
    const model = signal?.model;
    const definition: any = directionDefinitions.get(direction) ?? {};
    const averageReturn = finiteNumber(model?.average_return) ? model.average_return : undefined;
    const averageSp500Return = finiteNumber(signal?.average_sp500_return)
      ? signal.average_sp500_return
      : finiteNumber(model?.average_sp500_return)
        ? model.average_sp500_return
        : undefined;
    const averageAlpha = finiteNumber(model?.average_alpha)
      ? model.average_alpha
      : finiteNumber(averageReturn) && finiteNumber(averageSp500Return)
        ? averageReturn - averageSp500Return
        : undefined;

    return {
      direction,
      rangeLabel: String(signal?.range_label ?? definition.range_label ?? ""),
      ready: signal?.maturity === "ready" && Boolean(model) && finiteNumber(averageReturn),
      confidence: String(signal?.confidence ?? "low"),
      modelId: model?.model_id,
      modelLabel: model?.model_label,
      provider: model?.provider,
      averageReturn,
      averageSp500Return,
      averageAlpha,
      matchingResults: Number(signal?.comparison_round_count ?? model?.tests ?? 0),
      availableResults: Number(signal?.environment_round_count ?? 0)
    };
  });

  return {
    dataAsOf: marketEnvironment?.data_as_of,
    readyEnvironmentCount: environments.filter((environment: any) =>
      environment?.status === "ready"
      || Number(environment?.comparison?.round_count ?? 0) >= environmentThreshold
    ).length,
    totalEnvironmentCount: Math.max(
      environments.length,
      Array.isArray(definitions.environments) ? definitions.environments.length : 0
    ),
    items
  };
}
