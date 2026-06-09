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

  if (Math.abs(maxPossibleReturn) <= SCORE_EPSILON) {
    return Math.abs(portfolioReturn - maxPossibleReturn) <= SCORE_EPSILON ? 100 : null;
  }

  return Math.min(100, (portfolioReturn / maxPossibleReturn) * 100);
}

export function cumulativeCapitalBenchScore(portfolioReturns, maxPossibleReturns) {
  if (
    !Array.isArray(portfolioReturns) ||
    !Array.isArray(maxPossibleReturns) ||
    portfolioReturns.length === 0 ||
    portfolioReturns.length !== maxPossibleReturns.length ||
    portfolioReturns.some((value) => typeof value !== "number" || !Number.isFinite(value)) ||
    maxPossibleReturns.some((value) => typeof value !== "number" || !Number.isFinite(value))
  ) {
    return null;
  }

  const totalPortfolioReturn = portfolioReturns.reduce((total, value) => total + value, 0);
  const totalMaxPossibleReturn = maxPossibleReturns.reduce((total, value) => total + value, 0);
  return capitalBenchScore(totalPortfolioReturn, totalMaxPossibleReturn);
}
