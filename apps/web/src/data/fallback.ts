export type RoundStatus = "pending" | "resolved" | "archived";
export type SubmissionFormat = "single_pick" | "portfolio";
export type ScoreEtaSource = "automation" | "derived";

export interface RoundRecord {
  round_id: string;
  title: string;
  description: string;
  decision_date: string;
  decision_deadline_utc: string;
  horizon: string;
  horizon_days: number;
  entry_date: string;
  exit_date: string;
  status: RoundStatus;
  methodology_version: string;
  universe_version?: string;
  submission_format?: SubmissionFormat;
  official_run_id: string;
  stability_run_id?: string;
  score_eta_utc?: string;
  score_eta_source?: ScoreEtaSource;
  notes: string;
}

export interface SubmissionRecord {
  round_id: string;
  run_id: string;
  model_id: string;
  provider: string;
  submission_format?: SubmissionFormat;
  selected_option_id: string;
  holding_count?: number;
  max_allocation_bps?: number;
  cash_allocation_bps?: number;
  benchmark_allocation_bps?: number;
  concentration_hhi?: number;
  portfolio?: Array<{
    option_id: string;
    allocation_pct?: number;
    allocation_bps?: number;
    rationale?: string;
  }>;
  portfolio_rationale?: string;
  confidence: number;
  rationale_summary: string;
  key_risks: string[];
}

export interface UniverseOption {
  option_id: string;
  name: string;
  symbol: string;
  asset_class: string;
  option_group: string;
  risk_bucket: string;
  is_cash?: boolean;
  is_benchmark?: boolean;
  sort_order?: number;
}

export interface EntryPrice {
  option_id: string;
  symbol: string;
  date: string;
  price: number;
  source: string;
}

export interface HashRecord {
  path: string;
  sha256: string;
}

export interface LeaderboardRecord {
  model_id: string;
  provider: string;
  selected_option_id?: string;
  submission_format?: SubmissionFormat;
  holding_count?: number;
  portfolio_return?: number;
  max_allocation_bps?: number;
  cash_allocation_bps?: number;
  benchmark_allocation_bps?: number;
  concentration_hhi?: number;
  confidence?: number;
  selected_asset_return?: number;
  sp500_return?: number;
  alpha_vs_sp500?: number;
  rank_among_options?: number;
  resolved_rounds?: number;
  average_alpha_vs_sp500?: number;
  average_repeated_alpha_vs_sp500?: number;
  average_consistency_rate?: number;
}

export interface WeeklyPerformanceRecord {
  round_id: string;
  run_id: string;
  model_id: string;
  provider: string;
  target_date: string;
  price_date: string;
  days_elapsed: number;
  run_type?: string;
  submission_format?: SubmissionFormat;
  selected_option_id: string;
  holding_count?: number;
  model_return: number;
  sp500_return: number;
  alpha_vs_sp500: number;
  price_status?: string;
  published?: boolean;
}

export const rounds: RoundRecord[] = [
  {
    round_id: "CB-2026-05-10-1M",
    title: "CapitalBench May 10 2026 One-Month Round",
    description: "One-month official evaluation round using the frozen May 10, 2026 briefing.",
    decision_date: "2026-05-10",
    decision_deadline_utc: "2026-05-11T01:00:00Z",
    horizon: "one month",
    horizon_days: 33,
    entry_date: "2026-05-08",
    exit_date: "2026-06-10",
    status: "pending",
    methodology_version: "round1-v1.0",
    universe_version: "capitalbench_universe_v1_5",
    official_run_id: "official-round-1-clean",
    score_eta_utc: "2026-06-10T23:30:00Z",
    score_eta_source: "derived",
    notes:
      "Official model submissions are collected. Performance remains unpublished until exit prices are available."
  }
];

export const officialSubmissions: SubmissionRecord[] = [
  {
    round_id: "CB-2026-05-10-1M",
    run_id: "official-round-1-clean",
    model_id: "anthropic-claude-opus-4-7",
    provider: "anthropic",
    selected_option_id: "SEMICONDUCTORS",
    confidence: 0.58,
    rationale_summary:
      "Semiconductors show dominant momentum with AI capex tailwinds, while credit and volatility conditions remain benign.",
    key_risks: [
      "Middle East escalation could spike oil and pressure high-beta tech",
      "Hot CPI could push real yields higher",
      "Weak payroll growth could undermine cyclical chip demand"
    ]
  },
  {
    round_id: "CB-2026-05-10-1M",
    run_id: "official-round-1-clean",
    model_id: "google-gemini-3-1-pro",
    provider: "google",
    selected_option_id: "SEMICONDUCTORS",
    confidence: 0.6,
    rationale_summary:
      "Semiconductors had exceptional cross-horizon momentum and AI-driven earnings support despite macro uncertainty.",
    key_risks: [
      "Recent strength could reverse",
      "Geopolitical tension could hit risk appetite",
      "Inflation surprises could pressure growth multiples"
    ]
  },
  {
    round_id: "CB-2026-05-10-1M",
    run_id: "official-round-1-clean",
    model_id: "openai-gpt-5-5",
    provider: "openai",
    selected_option_id: "SEMICONDUCTORS",
    confidence: 0.34,
    rationale_summary:
      "Semiconductors showed the strongest trailing returns in the allowed universe, with positive risk appetite and contained volatility.",
    key_risks: [
      "Low confidence due to noisy one-month horizon",
      "High beta exposure can underperform rapidly",
      "Crowded AI positioning can reverse"
    ]
  },
  {
    round_id: "CB-2026-05-10-1M",
    run_id: "official-round-1-clean",
    model_id: "xai-grok-4-3",
    provider: "xai",
    selected_option_id: "SEMICONDUCTORS",
    confidence: 0.55,
    rationale_summary:
      "Semiconductors had the strongest 30-day momentum amid AI-driven demand and favorable earnings growth estimates.",
    key_risks: [
      "Momentum can fade over a short horizon",
      "Geopolitical shocks could punish growth risk",
      "Macro data could move rates against technology"
    ]
  }
];

export const universeOptions: UniverseOption[] = [
  ["CASH", "Cash / Do Not Invest", "", "cash", "cash", "cash", true, false],
  ["SHORT_TREASURY", "Short-Term Treasury Bills", "BIL", "cash_like", "cash_and_short_duration", "low", false, false],
  ["SP500", "S&P 500", "SPY", "equity", "us_broad_market", "medium", false, true],
  ["TOTAL_US_MARKET", "Total US Stock Market", "VTI", "equity", "us_broad_market", "medium", false, false],
  ["NASDAQ100", "Nasdaq 100", "QQQ", "equity", "us_growth_and_technology", "high", false, false],
  ["LARGE_GROWTH", "US Large-Cap Growth", "IWF", "equity", "us_style_factor", "high", false, false],
  ["LARGE_VALUE", "US Large-Cap Value", "IWD", "equity", "us_style_factor", "medium", false, false],
  ["MID_CAP", "US Mid-Cap Stocks", "IJH", "equity", "us_size_factor", "high", false, false],
  ["SMALL_CAP", "US Small-Cap Stocks", "IWM", "equity", "us_size_factor", "high", false, false],
  ["SMALL_VALUE", "US Small-Cap Value", "IWN", "equity", "us_style_factor", "high", false, false],
  ["DIVIDEND", "US Dividend Equities", "SCHD", "equity", "us_factor_equity", "medium", false, false],
  ["LOW_VOL", "US Low Volatility Equities", "SPLV", "equity", "us_factor_equity", "medium", false, false],
  ["MOMENTUM", "US Momentum Equities", "MTUM", "equity", "us_factor_equity", "high", false, false],
  ["TECHNOLOGY", "Technology Sector", "XLK", "equity", "us_sector", "high", false, false],
  ["COMMUNICATIONS", "Communication Services Sector", "XLC", "equity", "us_sector", "high", false, false],
  ["CONSUMER_DISCRETIONARY", "Consumer Discretionary Sector", "XLY", "equity", "us_sector", "high", false, false],
  ["CONSUMER_STAPLES", "Consumer Staples Sector", "XLP", "equity", "us_sector", "medium", false, false],
  ["HEALTHCARE", "Healthcare Sector", "XLV", "equity", "us_sector", "medium", false, false],
  ["FINANCIALS", "Financials Sector", "XLF", "equity", "us_sector", "high", false, false],
  ["INDUSTRIALS", "Industrials Sector", "XLI", "equity", "us_sector", "medium", false, false],
  ["ENERGY", "Energy Sector", "XLE", "equity", "us_sector", "high", false, false],
  ["MATERIALS", "Materials Sector", "XLB", "equity", "us_sector", "medium", false, false],
  ["UTILITIES", "Utilities Sector", "XLU", "equity", "us_sector", "medium", false, false],
  ["REAL_ESTATE", "Real Estate Sector", "XLRE", "equity", "us_sector", "high", false, false],
  ["INTERMEDIATE_TREASURY", "Intermediate-Term US Treasury Bonds", "IEF", "bond", "bonds_and_rates", "medium", false, false],
  ["LONG_TREASURY", "Long-Term US Treasury Bonds", "TLT", "bond", "bonds_and_rates", "high", false, false],
  ["TIPS", "Treasury Inflation-Protected Securities", "TIP", "bond", "bonds_and_rates", "medium", false, false],
  ["INVESTMENT_GRADE_CREDIT", "Investment Grade Corporate Bonds", "LQD", "bond", "credit", "medium", false, false],
  ["HIGH_YIELD_CREDIT", "High Yield Corporate Bonds", "HYG", "bond", "credit", "high", false, false],
  ["AGGREGATE_BONDS", "US Aggregate Bond Market", "AGG", "bond", "bonds_and_rates", "medium", false, false],
  ["DEVELOPED_EX_US", "Developed Markets ex-US", "VEA", "equity", "international_equity", "high", false, false],
  ["EMERGING_MARKETS", "Emerging Markets", "VWO", "equity", "international_equity", "very_high", false, false],
  ["EUROPE", "Europe Equities", "VGK", "equity", "international_equity", "high", false, false],
  ["JAPAN", "Japan Equities", "EWJ", "equity", "international_equity", "high", false, false],
  ["CHINA", "China Equities", "MCHI", "equity", "international_equity", "very_high", false, false],
  ["INDIA", "India Equities", "INDA", "equity", "international_equity", "very_high", false, false],
  ["GOLD", "Gold", "IAU", "commodity", "commodities", "medium", false, false],
  ["BROAD_COMMODITIES", "Broad Commodities", "PDBC", "commodity", "commodities", "high", false, false],
  ["SEMICONDUCTORS", "Semiconductors", "SMH", "equity", "ai_and_technology", "very_high", false, false],
  ["SOFTWARE", "Software", "IGV", "equity", "ai_and_technology", "high", false, false]
].map(([option_id, name, symbol, asset_class, option_group, risk_bucket, is_cash, is_benchmark]) => ({
  option_id: String(option_id),
  name: String(name),
  symbol: String(symbol),
  asset_class: String(asset_class),
  option_group: String(option_group),
  risk_bucket: String(risk_bucket),
  is_cash: Boolean(is_cash),
  is_benchmark: Boolean(is_benchmark)
}));

export const entryPrices: EntryPrice[] = [
  { option_id: "CASH", symbol: "", date: "2026-05-08", price: 1.0, source: "cash" },
  { option_id: "SP500", symbol: "SPY", date: "2026-05-08", price: 737.62, source: "tiingo_eod" },
  { option_id: "SEMICONDUCTORS", symbol: "SMH", date: "2026-05-08", price: 566.54, source: "tiingo_eod" },
  { option_id: "SOFTWARE", symbol: "IGV", date: "2026-05-08", price: 91.15, source: "tiingo_eod" }
];

export const auditHashes: HashRecord[] = [
  { path: "briefing.md", sha256: "cea86d1651e4dd4ed86f33bfe3e4fd5d4ff2a6fa3b068c611c7aa4fc01844479" },
  { path: "manifest.yaml", sha256: "6e2a34c3e1a363db1dcc89476a02867c0ce47fbe5110aa85782780f4f193b860" },
  { path: "options.yaml", sha256: "451c26dbfd8a498bef50df205d8c7489acf8edde5c48c21e132bda42e47cf056" },
  { path: "prompt.md", sha256: "3e45c33a3f6e05123183178793e55b179febd00a121af2f63ba41b825981c998" },
  {
    path: "market_data/universe_trailing_returns.csv",
    sha256: "810d24dc8f9490af2a78f768658829a8c230bb91cb5e8f691eac96b959e4c087"
  },
  {
    path: "market_data/universe_trailing_returns.json",
    sha256: "fecfc3b0246786c2d25772808fd421d28c149b87c2bc33ebde572f02ac0a4535"
  }
];

export const latestLeaderboard: LeaderboardRecord[] = [];
export const cumulativeOfficialLeaderboard: LeaderboardRecord[] = [];
export const cumulativeStabilityLeaderboard: LeaderboardRecord[] = [];

export function providerLabel(provider: string): string {
  const labels: Record<string, string> = {
    anthropic: "Anthropic",
    google: "Google",
    openai: "OpenAI",
    xai: "xAI"
  };
  return labels[provider] ?? provider;
}

export function modelLabel(modelId: string): string {
  const known: Record<string, string> = {
    "anthropic-claude-opus-4-7": "Claude Opus 4.7",
    "google-gemini-3-1-pro": "Gemini 3.1 Pro",
    "openai-gpt-5-5": "GPT-5.5",
    "xai-grok-4-3": "Grok 4.3"
  };
  if (known[modelId]) return known[modelId];
  return modelId
    .replace(/^openai-/, "")
    .replace(/^anthropic-/, "")
    .replace(/^google-/, "")
    .replace(/^xai-/, "")
    .split("-")
    .map((part) => {
      if (part === "gpt") return "GPT";
      if (/^\d+$/.test(part)) return part;
      return part.length <= 3 ? part.toUpperCase() : part[0].toUpperCase() + part.slice(1);
    })
    .join(" ");
}
