import { readFileSync } from "node:fs";
import { join, resolve } from "node:path";
import { parse as parseYaml } from "yaml";

export type RiskRegimeGroup =
  | "liquidity_defensive"
  | "duration_credit"
  | "defensive_equity"
  | "broad_cyclical_equity"
  | "growth_technology"
  | "international_equity"
  | "real_assets_inflation"
  | "crypto";

export type AssetRiskDefinition = {
  risk_score_1_5: number;
  risk_on_loading: number;
  regime_group: RiskRegimeGroup;
  defensive: boolean;
  technology: boolean;
};

export type AssetRiskModel = {
  version: string;
  published_at: string;
  description: string;
  regime_groups: Record<RiskRegimeGroup, string>;
  assets: Record<string, AssetRiskDefinition>;
};

function repoRootPath(): string {
  const candidates = [resolve(process.cwd()), resolve(process.cwd(), "../..")];
  return (
    candidates.find((candidate) => {
      try {
        readFileSync(join(candidate, "configs", "asset_risk_model.yaml"), "utf8");
        return true;
      } catch {
        return false;
      }
    }) ?? resolve(process.cwd(), "../..")
  );
}

let cachedRiskModel: AssetRiskModel | null = null;

export function assetRiskModel(): AssetRiskModel {
  if (cachedRiskModel) return cachedRiskModel;
  const path = join(repoRootPath(), "configs", "asset_risk_model.yaml");
  const parsed = parseYaml(readFileSync(path, "utf8")) as AssetRiskModel;
  if (!parsed?.version || !parsed.assets) throw new Error(`Invalid asset-risk model: ${path}`);
  cachedRiskModel = parsed;
  return parsed;
}

export function assetRiskDefinition(optionId: string): AssetRiskDefinition {
  const definition = assetRiskModel().assets[optionId];
  if (!definition) throw new Error(`Missing asset-risk definition for ${optionId}`);
  return definition;
}
