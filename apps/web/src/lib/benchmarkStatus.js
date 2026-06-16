import { insightHref, leadInsightsByCategory } from "./insights.js";

function shortDate(value) {
  if (!value) return "n/a";
  const date = new Date(`${String(value).slice(0, 10)}T00:00:00Z`);
  if (Number.isNaN(date.getTime())) return String(value);
  return new Intl.DateTimeFormat("en", { month: "short", day: "numeric", timeZone: "UTC" }).format(date);
}

function refreshTimestamp(value) {
  if (!value) return "n/a";
  const date = new Date(value);
  if (Number.isNaN(date.getTime())) return String(value);
  return new Intl.DateTimeFormat("en", {
    month: "short",
    day: "numeric",
    hour: "2-digit",
    minute: "2-digit",
    timeZone: "UTC",
    timeZoneName: "short"
  }).format(date);
}

function roundTrack(round) {
  if (!round) return "other";
  const roundId = String(round.round_id ?? "");
  const horizon = String(round.horizon ?? "");
  const horizonDays = Number(round.horizon_days);
  if (roundId.endsWith("-1W") || horizonDays <= 10 || /week/i.test(horizon)) return "weekly";
  if (roundId.endsWith("-1M") || horizonDays >= 28 || /month/i.test(horizon)) return "monthly";
  return "other";
}

function trackLabel(track) {
  if (track === "weekly") return "Weekly";
  if (track === "monthly") return "Monthly";
  return "";
}

function trackNoun(track) {
  if (track === "weekly") return "weekly";
  if (track === "monthly") return "monthly";
  return "official";
}

function activeTrackLabel(track) {
  if (track === "weekly") return "weekly";
  if (track === "monthly") return "monthly";
  return "open";
}

function numberLabel(value, digits = 1) {
  const numeric = Number(value);
  if (!Number.isFinite(numeric)) return "n/a";
  return numeric.toFixed(digits);
}

function percentageLabel(value, digits = 1) {
  const numeric = Number(value);
  if (!Number.isFinite(numeric)) return "n/a";
  return `${numeric.toFixed(digits)}%`;
}

function signedPpLabel(value, digits = 1) {
  const numeric = Number(value);
  if (!Number.isFinite(numeric)) return "n/a";
  const sign = numeric > 0 ? "+" : "";
  return `${sign}${numeric.toFixed(digits)} pp`;
}

function compactCount(value, singular, plural = `${singular}s`) {
  const numeric = Number(value);
  if (!Number.isFinite(numeric)) return `0 ${plural}`;
  return `${numeric} ${numeric === 1 ? singular : plural}`;
}

function latestResolvedRound(rounds, track) {
  return rounds
    .filter((round) => round.status === "resolved" && (!track || roundTrack(round) === track))
    .sort(
      (left, right) =>
        String(right.exit_date ?? "").localeCompare(String(left.exit_date ?? "")) ||
        String(right.decision_deadline_utc ?? "").localeCompare(String(left.decision_deadline_utc ?? "")) ||
        String(right.round_id ?? "").localeCompare(String(left.round_id ?? ""))
    )[0];
}

function latestPriceClose(readModel) {
  return (readModel.interim_performance ?? []).reduce(
    (latest, row) => (String(row.price_date ?? "") > latest ? String(row.price_date ?? "") : latest),
    ""
  );
}

function nextScheduledScore(activeRounds, latestPriceDate) {
  return activeRounds
    .map((round) => String(round.exit_date ?? "").slice(0, 10))
    .filter((date) => date && (!latestPriceDate || date > latestPriceDate))
    .sort()[0] ?? "";
}

function modelById(readModel) {
  return new Map((readModel.models ?? []).map((model) => [model.model_id, model]));
}

function latestOfficialResult(readModel, track) {
  const round = latestResolvedRound(readModel.rounds ?? [], track);
  if (!round) return null;
  const results = (readModel.results ?? [])
    .filter((row) => row.round_id === round.round_id && (!round.official_run_id || row.run_id === round.official_run_id))
    .sort(
      (left, right) =>
        Number(left.rank ?? 999) - Number(right.rank ?? 999) ||
        Number(right.portfolio_return_pct ?? -Infinity) - Number(left.portfolio_return_pct ?? -Infinity)
    );
  const top = results[0];
  if (!top) return { round, top: null };
  const models = modelById(readModel);
  return {
    round,
    top: {
      ...top,
      label: models.get(top.model_id)?.label ?? top.model_id
    }
  };
}

function resolvedRoundIds(readModel, track) {
  return (readModel.rounds ?? [])
    .filter((round) => round.status === "resolved" && (!track || roundTrack(round) === track))
    .sort(
      (left, right) =>
        String(left.exit_date ?? "").localeCompare(String(right.exit_date ?? "")) ||
        String(left.round_id ?? "").localeCompare(String(right.round_id ?? ""))
    )
    .map((round) => round.round_id);
}

function cumulativeLeader(readModel, track) {
  const roundIds = resolvedRoundIds(readModel, track);
  if (roundIds.length === 0) return null;
  const models = modelById(readModel);
  const byModel = new Map();
  for (const row of readModel.results ?? []) {
    if (!roundIds.includes(row.round_id)) continue;
    if (track && row.track !== track) continue;
    const model = byModel.get(row.model_id) ?? {
      model_id: row.model_id,
      label: models.get(row.model_id)?.label ?? row.model_id,
      portfolioReturns: [],
      maxPossibleReturns: [],
      testsIncluded: 0
    };
    if (Number.isFinite(Number(row.portfolio_return_pct)) && Number.isFinite(Number(row.max_possible_return_pct))) {
      model.portfolioReturns.push(Number(row.portfolio_return_pct));
      model.maxPossibleReturns.push(Number(row.max_possible_return_pct));
      model.testsIncluded += 1;
    }
    byModel.set(row.model_id, model);
  }
  const testsRequired = roundIds.length;
  return Array.from(byModel.values())
    .filter((row) => row.testsIncluded > 0)
    .map((row) => {
      const totalPortfolio = row.portfolioReturns.reduce((total, value) => total + value, 0);
      const totalMax = row.maxPossibleReturns.reduce((total, value) => total + value, 0);
      return {
        ...row,
        testsRequired,
        totalPortfolio,
        totalMax,
        capitalBenchScore: Math.abs(totalMax) < 1e-7 ? null : (totalPortfolio / totalMax) * 100
      };
    })
    .sort(
      (left, right) =>
        Number(right.capitalBenchScore ?? -Infinity) - Number(left.capitalBenchScore ?? -Infinity) ||
        Number(right.totalPortfolio ?? -Infinity) - Number(left.totalPortfolio ?? -Infinity) ||
        left.label.localeCompare(right.label)
    )[0] ?? null;
}

function activeAllocations(readModel, track) {
  const rows = (readModel.allocations ?? []).filter((row) => row.status === "active" && (!track || row.track === track));
  const portfolioKeys = new Set(rows.map((row) => `${row.round_id}:${row.run_id}:${row.model_id}`));
  const denominator = Math.max(1, portfolioKeys.size);
  const byAsset = new Map();
  for (const row of rows) {
    const existing = byAsset.get(row.option_id) ?? {
      option_id: row.option_id,
      label: row.label ?? row.option_id,
      ticker: row.ticker ?? "",
      category: row.category ?? "unknown",
      allocationPct: 0,
      models: new Set(),
      rounds: new Set(),
      tracks: new Set()
    };
    existing.allocationPct += Number(row.allocation_pct ?? 0) / denominator;
    existing.models.add(row.model_id);
    existing.rounds.add(row.round_id);
    existing.tracks.add(row.track);
    byAsset.set(row.option_id, existing);
  }
  return {
    portfolioCount: portfolioKeys.size,
    assets: Array.from(byAsset.values()).sort(
      (left, right) => right.allocationPct - left.allocationPct || left.label.localeCompare(right.label)
    )
  };
}

function activeCategoryLeader(readModel, track) {
  const rows = (readModel.allocations ?? []).filter((row) => row.status === "active" && (!track || row.track === track));
  const portfolioKeys = new Set(rows.map((row) => `${row.round_id}:${row.run_id}:${row.model_id}`));
  const denominator = Math.max(1, portfolioKeys.size);
  const byCategory = new Map();
  for (const row of rows) {
    const existing = byCategory.get(row.category) ?? {
      category: row.category ?? "unknown",
      allocationPct: 0,
      assets: new Set()
    };
    existing.allocationPct += Number(row.allocation_pct ?? 0) / denominator;
    existing.assets.add(row.option_id);
    byCategory.set(row.category, existing);
  }
  return Array.from(byCategory.values()).sort((left, right) => right.allocationPct - left.allocationPct)[0] ?? null;
}

function isUsableLivePerformanceRow(row) {
  return (
    row.status === "active" &&
    row.published !== false &&
    Number(row.days_elapsed ?? 0) > 0 &&
    String(row.target_date ?? "") > String(row.entry_date ?? "") &&
    String(row.target_date ?? "") < String(row.exit_date ?? "") &&
    Number.isFinite(Number(row.model_return_pct)) &&
    Number.isFinite(Number(row.sp500_return_pct)) &&
    Number.isFinite(Number(row.alpha_pp))
  );
}

function latestLivePerformance(readModel, track) {
  const latestByKey = new Map();
  for (const row of readModel.interim_performance ?? []) {
    if (track && row.track !== track) continue;
    if (!isUsableLivePerformanceRow(row)) continue;
    const key = `${row.round_id}:${row.run_id}:${row.model_id}`;
    const existing = latestByKey.get(key);
    if (
      !existing ||
      String(row.target_date ?? "") > String(existing.target_date ?? "") ||
      (String(row.target_date ?? "") === String(existing.target_date ?? "") &&
        String(row.price_date ?? "") > String(existing.price_date ?? ""))
    ) {
      latestByKey.set(key, row);
    }
  }
  const rows = Array.from(latestByKey.values());
  const models = modelById(readModel);
  const byModel = new Map();
  for (const row of rows) {
    const existing = byModel.get(row.model_id) ?? {
      model_id: row.model_id,
      label: models.get(row.model_id)?.label ?? row.model_id,
      returns: [],
      alphas: [],
      rounds: new Set(),
      latestPriceDate: ""
    };
    existing.returns.push(Number(row.model_return_pct));
    existing.alphas.push(Number(row.alpha_pp));
    existing.rounds.add(row.round_id);
    if (String(row.price_date ?? "") > existing.latestPriceDate) existing.latestPriceDate = String(row.price_date ?? "");
    byModel.set(row.model_id, existing);
  }
  const data = Array.from(byModel.values())
    .map((row) => ({
      ...row,
      portfolioReturnPct: row.returns.reduce((total, value) => total + value, 0) / Math.max(1, row.returns.length),
      alphaPp: row.alphas.reduce((total, value) => total + value, 0) / Math.max(1, row.alphas.length),
      roundCount: row.rounds.size
    }))
    .sort(
      (left, right) =>
        Number(right.portfolioReturnPct ?? -Infinity) - Number(left.portfolioReturnPct ?? -Infinity) ||
        Number(right.alphaPp ?? -Infinity) - Number(left.alphaPp ?? -Infinity) ||
        left.label.localeCompare(right.label)
    );
  return {
    snapshotCount: rows.length,
    roundCount: new Set(rows.map((row) => row.round_id)).size,
    latestPriceDate: rows.reduce(
      (latest, row) => (String(row.price_date ?? "") > latest ? String(row.price_date ?? "") : latest),
      ""
    ),
    leader: data[0] ?? null
  };
}

function positioningChange(readModel, track) {
  const rounds = (readModel.rounds ?? [])
    .filter(
      (round) =>
        (!track || roundTrack(round) === track) &&
        (readModel.allocations ?? []).some((allocation) => allocation.round_id === round.round_id)
    )
    .sort(
      (left, right) =>
        String(right.decision_deadline_utc ?? "").localeCompare(String(left.decision_deadline_utc ?? "")) ||
        String(right.round_id ?? "").localeCompare(String(left.round_id ?? ""))
    );
  const [current, prior] = rounds;
  if (!current || !prior) return null;

  function aggregate(roundId) {
    const rows = (readModel.allocations ?? []).filter((row) => row.round_id === roundId);
    const portfolioKeys = new Set(rows.map((row) => `${row.round_id}:${row.run_id}:${row.model_id}`));
    const denominator = Math.max(1, portfolioKeys.size);
    const byAsset = new Map();
    for (const row of rows) {
      const existing = byAsset.get(row.option_id) ?? {
        option_id: row.option_id,
        label: row.label ?? row.option_id,
        ticker: row.ticker ?? "",
        allocationPct: 0
      };
      existing.allocationPct += Number(row.allocation_pct ?? 0) / denominator;
      byAsset.set(row.option_id, existing);
    }
    return byAsset;
  }

  const currentRows = aggregate(current.round_id);
  const priorRows = aggregate(prior.round_id);
  return Array.from(currentRows.values())
    .map((row) => {
      const priorRow = priorRows.get(row.option_id);
      return {
        ...row,
        priorAllocationPct: priorRow?.allocationPct ?? 0,
        changePp: row.allocationPct - (priorRow?.allocationPct ?? 0),
        currentRoundId: current.round_id,
        priorRoundId: prior.round_id
      };
    })
    .sort((left, right) => Math.abs(right.changePp) - Math.abs(left.changePp))[0] ?? null;
}

function categoryLabel(value) {
  const labels = {
    ai_and_technology: "AI and technology",
    broad_cyclical_equity: "broad cyclical equity",
    cash_and_ultra_short: "cash and ultra-short bonds",
    commodities: "commodities",
    crypto: "crypto",
    defensive_equity: "defensive equity",
    duration_credit: "duration and credit",
    international_equity: "international equity",
    real_assets_inflation: "real assets and inflation",
    us_equity_broad: "broad US equity",
    us_factor_style: "US factor/style",
    us_sector: "US sectors"
  };
  return labels[value] ?? String(value ?? "unknown").replaceAll("_", " ");
}

function staleSignals({ generatedAt, latestPriceDate, nextScoreDate }) {
  const signals = [];
  const generatedTime = generatedAt ? new Date(generatedAt).getTime() : NaN;
  if (!Number.isFinite(generatedTime)) {
    signals.push("Site data refresh time is unavailable.");
  } else if (Date.now() - generatedTime > 24 * 60 * 60 * 1000) {
    signals.push("Site data is more than 24 hours old.");
  }
  if (latestPriceDate) {
    const latestPriceTime = new Date(`${latestPriceDate}T00:00:00Z`).getTime();
    if (Number.isFinite(latestPriceTime) && Date.now() - latestPriceTime > 5 * 24 * 60 * 60 * 1000) {
      signals.push("Latest price close may be stale.");
    }
  }
  if (nextScoreDate) {
    const nextScoreTime = new Date(`${nextScoreDate}T23:59:59Z`).getTime();
    if (Number.isFinite(nextScoreTime) && nextScoreTime < Date.now()) {
      signals.push("A scheduled score date has passed.");
    }
  }
  return signals;
}

export function buildBenchmarkStatus(readModel, options = {}) {
  const track = options.track === "weekly" || options.track === "monthly" ? options.track : undefined;
  const resolvedTrackLabel = trackLabel(track);
  const rounds = readModel.rounds ?? [];
  const activeRounds = rounds.filter((round) => round.status === "active" && (!track || roundTrack(round) === track));
  const latestOfficial = latestResolvedRound(rounds, track);
  const latestPriceDate = latestPriceClose(readModel);
  const nextScoreDate = nextScheduledScore(activeRounds, latestPriceDate);

  return {
    latestOfficialLabel: resolvedTrackLabel ? `Latest ${resolvedTrackLabel.toLowerCase()} score` : "Latest official score",
    latestOfficialRoundId: latestOfficial?.round_id ?? "No official score",
    latestOfficialRoundHref: latestOfficial?.round_id ? `/rounds/${latestOfficial.round_id}/` : "/leaderboards/latest",
    liveRoundLabel: resolvedTrackLabel ? `${resolvedTrackLabel} live` : "Live rounds",
    liveRoundCount: activeRounds.length,
    latestPriceDate,
    latestPriceLabel: shortDate(latestPriceDate),
    nextScoreDate,
    nextScoreLabel: shortDate(nextScoreDate),
    refreshedAt: readModel.generated_at ?? "",
    refreshedAtLabel: refreshTimestamp(readModel.generated_at)
  };
}

export function buildBenchmarkPulseSlides(readModel, options = {}) {
  const track = options.track === "weekly" || options.track === "monthly" ? options.track : undefined;
  const rounds = readModel.rounds ?? [];
  const activeRounds = rounds.filter((round) => round.status === "active" && (!track || roundTrack(round) === track));
  const latestPriceDate = latestPriceClose(readModel);
  const nextScoreDate = nextScheduledScore(activeRounds, latestPriceDate);
  const refreshedAt = readModel.generated_at ?? "";
  const refreshedAtLabel = refreshTimestamp(refreshedAt);
  const statusWarnings = staleSignals({ generatedAt: refreshedAt, latestPriceDate, nextScoreDate });
  const pulse = readModel.risk_appetite?.current_decision_pulse;
  const outstanding = readModel.risk_appetite?.outstanding_live_book;
  const positioningTrack = track ?? undefined;
  const active = activeAllocations(readModel, positioningTrack);
  const categoryLeader = activeCategoryLeader(readModel, positioningTrack);
  const livePerformance = latestLivePerformance(readModel, positioningTrack);
  const changeTrack = track ?? "weekly";
  const change = positioningChange(readModel, changeTrack);
  const officialTrack = track ?? "weekly";
  const latestOfficial = latestOfficialResult(readModel, officialTrack);
  const cumulative = cumulativeLeader(readModel, officialTrack);
  const proofCount = (readModel.proof ?? []).length;
  const currentUniverseCount = (readModel.assets ?? []).filter((asset) => asset.in_current_universe).length;
  const activeWeeklyCount = rounds.filter((round) => round.status === "active" && roundTrack(round) === "weekly").length;
  const activeMonthlyCount = rounds.filter((round) => round.status === "active" && roundTrack(round) === "monthly").length;
  const topAsset = active.assets[0];
  const trackText = activeTrackLabel(track);
  const officialTrackText = trackNoun(officialTrack);

  const slides = [
    {
      key: "context",
      tone: "neutral",
      label: "CapitalBench Live Pulse",
      value: "AI model portfolios, scored against real market returns",
      detail:
        "Frontier models receive the same market brief, choose frozen portfolios, then results are scored after 1 week or 1 month.",
      href: "/methodology",
      actionLabel: "How it works"
    }
  ];

  if (pulse) {
    const agreement = pulse.agreement?.label ? ` Model agreement: ${pulse.agreement.label}.` : "";
    const changeText = Number.isFinite(Number(pulse.change_from_previous))
      ? ` ${Number(pulse.change_from_previous) >= 0 ? "+" : ""}${numberLabel(pulse.change_from_previous)} vs prior pulse.`
      : "";
    const outstandingText = outstanding?.score
      ? ` Open-book risk: ${outstanding.label ?? "live"} ${numberLabel(outstanding.score)}/100.`
      : "";
    slides.push({
      key: "risk-positioning",
      tone: Number(pulse.score) >= 75 ? "hot" : Number(pulse.score) >= 55 ? "positive" : "caution",
      label: "Current AI Positioning",
      value: `${pulse.label ?? "Live positioning"} risk-taking · ${numberLabel(pulse.score)}/100`,
      detail: `${pulse.regime ?? "Live portfolios are being scored for allocation risk."}.${changeText}${agreement}${outstandingText}`.replace(
        /\s+/g,
        " "
      ),
      href: "/risk-appetite",
      actionLabel: "View AI positioning"
    });
  }

  if (topAsset) {
    const categoryText = categoryLeader
      ? ` The largest category exposure is ${categoryLabel(categoryLeader.category)} at ${percentageLabel(categoryLeader.allocationPct)}.`
      : "";
    slides.push({
      key: "crowded-position",
      tone: "positive",
      label: "Most Crowded Live Position",
      value: `${topAsset.label} · ${percentageLabel(topAsset.allocationPct)} of ${trackText} portfolios`,
      detail: `${topAsset.ticker ? `${topAsset.ticker} is` : "This is"} the largest shared allocation across ${compactCount(
        active.portfolioCount,
        "open model portfolio"
      )} and ${compactCount(topAsset.models.size, "model")}.${categoryText}`,
      href: track === "monthly" ? "/leaderboards/latest-monthly" : "/leaderboards/latest-weekly",
      actionLabel: "View model portfolios"
    });
  }

  if (change) {
    const changeTrackText = activeTrackLabel(changeTrack);
    slides.push({
      key: "positioning-change",
      tone: Number(change.changePp) >= 0 ? "positive" : "caution",
      label: "Biggest Allocation Change",
      value: `${change.label} ${Number(change.changePp) >= 0 ? "up" : "down"} ${numberLabel(Math.abs(change.changePp))} pp`,
      detail: `Compared with the previous saved ${changeTrackText} round, AI models ${
        Number(change.changePp) >= 0 ? "increased" : "reduced"
      } ${change.ticker ? `${change.ticker} ` : ""}exposure the most.`,
      href: "/#ai-positioning",
      actionLabel: "View positioning changes"
    });
  }

  if (livePerformance.leader) {
    slides.push({
      key: "live-performance",
      tone: Number(livePerformance.leader.portfolioReturnPct) >= 0 ? "positive" : "caution",
      label: "Live Mark-To-Market",
      value: `${livePerformance.leader.label} leads open rounds at ${percentageLabel(livePerformance.leader.portfolioReturnPct)}`,
      detail: `Open portfolios are marked to prices through ${shortDate(
        livePerformance.latestPriceDate || latestPriceDate
      )}. These are not final benchmark scores. Latest alpha: ${signedPpLabel(livePerformance.leader.alphaPp)}.`,
      href: "/rounds",
      actionLabel: "View live rounds"
    });
  }

  if (latestOfficial?.top) {
    slides.push({
      key: "latest-official",
      tone: Number(latestOfficial.top.portfolio_return_pct) >= Number(latestOfficial.top.benchmark_return_pct) ? "positive" : "caution",
      label: `Latest Official ${trackLabel(officialTrack)} Score`,
      value: `${latestOfficial.top.label} led the latest scored ${officialTrackText} round`,
      detail: `Return ${percentageLabel(latestOfficial.top.portfolio_return_pct)} vs S&P 500 ${percentageLabel(
        latestOfficial.top.benchmark_return_pct
      )}. Max possible was ${percentageLabel(latestOfficial.top.max_possible_return_pct)}.`,
      href: `/rounds/${latestOfficial.round.round_id}/`,
      actionLabel: "Open result"
    });
  }

  if (cumulative) {
    slides.push({
      key: "cumulative-leader",
      tone: Number(cumulative.capitalBenchScore) >= 0 ? "positive" : "caution",
      label: `Full ${trackLabel(officialTrack)} History`,
      value: `${cumulative.label} leads completed ${officialTrackText} history`,
      detail: `CapitalBench Score ${numberLabel(cumulative.capitalBenchScore)} across ${cumulative.testsIncluded}/${cumulative.testsRequired} completed ${officialTrackText} tests.`,
      href: officialTrack === "monthly" ? "/leaderboards/cumulative-monthly" : "/leaderboards/cumulative-weekly",
      actionLabel: `View cumulative ${officialTrackText}`
    });
  }

  slides.push({
    key: "trust-freshness",
    tone: statusWarnings.length > 0 ? "warning" : "neutral",
    label: "Data And Audit Status",
    value: `Prices through ${shortDate(latestPriceDate)} · ${proofCount}/${rounds.length} rounds audited`,
    detail: `${
      statusWarnings[0] ?? `Current universe: ${currentUniverseCount} assets. Site data refreshed ${refreshedAtLabel}.`
    } Open tests: ${activeWeeklyCount} weekly and ${activeMonthlyCount} monthly. Next ${trackText} score: ${shortDate(nextScoreDate)}.`,
    href: "/docs",
    actionLabel: "Open audit data"
  });

  return {
    slides,
    latestPriceLabel: shortDate(latestPriceDate),
    latestPriceDate,
    refreshedAt,
    refreshedAtLabel,
    warningCount: statusWarnings.length,
    activeRoundSummary: `${activeWeeklyCount} weekly / ${activeMonthlyCount} monthly`
  };
}

export function buildBenchmarkTickerTape(readModel, options = {}) {
  const track = options.track === "weekly" || options.track === "monthly" ? options.track : undefined;
  const rounds = readModel.rounds ?? [];
  const activeRounds = rounds.filter((round) => round.status === "active" && (!track || roundTrack(round) === track));
  const latestPriceDate = latestPriceClose(readModel);
  const nextScoreDate = nextScheduledScore(activeRounds, latestPriceDate);
  const refreshedAt = readModel.generated_at ?? "";
  const statusWarnings = staleSignals({ generatedAt: refreshedAt, latestPriceDate, nextScoreDate });
  const pulse = readModel.risk_appetite?.current_decision_pulse;
  const positioningTrack = track ?? undefined;
  const active = activeAllocations(readModel, positioningTrack);
  const livePerformance = latestLivePerformance(readModel, positioningTrack);
  const changeTrack = track ?? "weekly";
  const change = positioningChange(readModel, changeTrack);
  const officialTrack = track ?? "weekly";
  const latestOfficial = latestOfficialResult(readModel, officialTrack);
  const cumulative = cumulativeLeader(readModel, officialTrack);
  const proofCount = (readModel.proof ?? []).length;
  const activeWeeklyCount = rounds.filter((round) => round.status === "active" && roundTrack(round) === "weekly").length;
  const activeMonthlyCount = rounds.filter((round) => round.status === "active" && roundTrack(round) === "monthly").length;
  const topAsset = active.assets[0];
  const tickerInsight = leadInsightsByCategory(
    readModel,
    ["current_positioning", "risk_regime", "horizon_agreement", "live_performance", "oracle_comparison"],
    1
  )[0];

  const items = [
    {
      key: "benchmark",
      tone: "neutral",
      label: "Benchmark",
      value: "Live AI capital allocation",
      detail: "same brief, frozen portfolios, real returns",
      href: "/methodology"
    }
  ];

  if (pulse) {
    items.push({
      key: "risk-positioning",
      tone: Number(pulse.score) >= 75 ? "hot" : Number(pulse.score) >= 55 ? "positive" : "caution",
      label: "AI Positioning",
      value: `${pulse.label ?? "Live"} ${numberLabel(pulse.score)}/100`,
      detail: pulse.regime ?? "live allocation signal",
      href: "/risk-appetite"
    });

    if (pulse.agreement?.label) {
      items.push({
        key: "model-agreement",
        tone: pulse.agreement.label === "Tight" ? "positive" : "caution",
        label: "Model Agreement",
        value: pulse.agreement.label,
        detail: `${numberLabel(pulse.agreement.standard_deviation)} point dispersion`,
        href: "/risk-appetite"
      });
    }
  }

  if (tickerInsight) {
    items.push({
      key: "benchmark-insight",
      tone: "neutral",
      label: "Insight",
      value: tickerInsight.title,
      detail: tickerInsight.summary,
      href: insightHref(tickerInsight)
    });
  }

  if (topAsset) {
    items.push({
      key: "crowded-position",
      tone: "positive",
      label: "Crowded Position",
      value: `${topAsset.label} ${percentageLabel(topAsset.allocationPct)}`,
      detail: `${compactCount(topAsset.models.size, "model")} hold ${topAsset.ticker || topAsset.label}`,
      href: track === "monthly" ? "/leaderboards/latest-monthly" : "/leaderboards/latest-weekly"
    });
  }

  if (change) {
    items.push({
      key: "positioning-change",
      tone: Number(change.changePp) >= 0 ? "positive" : "caution",
      label: "Biggest Shift",
      value: `${change.label} ${Number(change.changePp) >= 0 ? "up" : "down"} ${numberLabel(Math.abs(change.changePp))} pp`,
      detail: `vs prior ${activeTrackLabel(changeTrack)} round`,
      href: "/#ai-positioning"
    });
  }

  if (livePerformance.leader) {
    items.push({
      key: "live-performance",
      tone: Number(livePerformance.leader.portfolioReturnPct) >= 0 ? "positive" : "caution",
      label: "Live MTM",
      value: `${livePerformance.leader.label} ${percentageLabel(livePerformance.leader.portfolioReturnPct)}`,
      detail: "not final",
      href: "/rounds"
    });
  }

  if (latestOfficial?.top) {
    items.push({
      key: "latest-official",
      tone: Number(latestOfficial.top.portfolio_return_pct) >= Number(latestOfficial.top.benchmark_return_pct) ? "positive" : "caution",
      label: `Latest ${trackLabel(officialTrack)}`,
      value: `${latestOfficial.top.label} led`,
      detail: `${percentageLabel(latestOfficial.top.portfolio_return_pct)} vs S&P ${percentageLabel(
        latestOfficial.top.benchmark_return_pct
      )}`,
      href: `/rounds/${latestOfficial.round.round_id}/`
    });
  }

  if (cumulative) {
    items.push({
      key: "cumulative-leader",
      tone: Number(cumulative.capitalBenchScore) >= 0 ? "positive" : "caution",
      label: `Full ${trackLabel(officialTrack)} History`,
      value: `${cumulative.label} leads`,
      detail: `score ${numberLabel(cumulative.capitalBenchScore)} across ${cumulative.testsIncluded}/${cumulative.testsRequired}`,
      href: officialTrack === "monthly" ? "/leaderboards/cumulative-monthly" : "/leaderboards/cumulative-weekly"
    });
  }

  return {
    items,
    brand: {
      label: "CapitalBench Live",
      value: "AI benchmark tape",
      detail: `${activeWeeklyCount} weekly / ${activeMonthlyCount} monthly open`,
      href: "/"
    },
    data: {
      label: "Data",
      value: `Prices ${shortDate(latestPriceDate)}`,
      detail: `${proofCount}/${rounds.length} audited`,
      href: "/docs",
      tone: statusWarnings.length > 0 ? "warning" : "neutral",
      title: `${statusWarnings[0] ?? "Data checks passed."} Next score: ${shortDate(nextScoreDate)}. Refreshed ${refreshTimestamp(
        refreshedAt
      )}.`
    }
  };
}

export { refreshTimestamp, shortDate };
