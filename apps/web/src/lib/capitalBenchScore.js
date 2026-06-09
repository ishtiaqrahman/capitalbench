const SCORE_EPSILON = 1e-7;

export function capitalBenchScore(portfolioReturn, maxPossibleReturn) {
  if (
    typeof portfolioReturn !== "number" ||
    typeof maxPossibleReturn !== "number" ||
    !Number.isFinite(portfolioReturn) ||
    !Number.isFinite(maxPossibleReturn)
  ) {
    return null;
  }

  if (maxPossibleReturn <= SCORE_EPSILON) {
    return Math.abs(portfolioReturn - maxPossibleReturn) <= SCORE_EPSILON ? 100 : 0;
  }

  return Math.min(100, Math.max(0, (portfolioReturn / maxPossibleReturn) * 100));
}
