function finiteValues(values) {
  return values.filter((value) => typeof value === "number" && Number.isFinite(value));
}

function niceStep(range, targetIntervals) {
  if (!(range > 0)) return 1;
  const rawStep = range / Math.max(1, targetIntervals);
  const power = 10 ** Math.floor(Math.log10(rawStep));
  const fraction = rawStep / power;
  const niceFraction = fraction <= 1 ? 1 : fraction <= 2 ? 2 : fraction <= 2.5 ? 2.5 : fraction <= 5 ? 5 : 10;
  return niceFraction * power;
}

/**
 * Builds a stable, zero-aware scale for benchmark bar charts.
 * Values remain on their real shared scale; no rank-based width normalization is used.
 */
export function buildBenchmarkBarDomain(values, options = {}) {
  const clean = finiteValues(values);
  const includeZero = options.includeZero !== false;
  const targetTicks = Math.max(2, Number(options.targetTicks ?? 4));
  let minimum = clean.length ? Math.min(...clean) : 0;
  let maximum = clean.length ? Math.max(...clean) : 1;

  if (includeZero) {
    minimum = Math.min(0, minimum);
    maximum = Math.max(0, maximum);
  }

  if (options.symmetric) {
    const bound = Math.max(Math.abs(minimum), Math.abs(maximum), Number(options.minimumSpan ?? 0) / 2);
    minimum = -bound;
    maximum = bound;
  }

  if (minimum === maximum) {
    const fallback = Math.max(Math.abs(minimum), Number(options.minimumSpan ?? 0), 1);
    minimum = includeZero && minimum >= 0 ? 0 : minimum - fallback / 2;
    maximum = includeZero && maximum <= 0 ? 0 : maximum + fallback / 2;
  }

  const requiredSpan = Number(options.minimumSpan ?? 0);
  if (requiredSpan > 0 && maximum - minimum < requiredSpan) {
    if (options.symmetric) {
      minimum = -requiredSpan / 2;
      maximum = requiredSpan / 2;
    } else if (minimum >= 0) {
      maximum = minimum + requiredSpan;
    } else if (maximum <= 0) {
      minimum = maximum - requiredSpan;
    } else {
      const extra = (requiredSpan - (maximum - minimum)) / 2;
      minimum -= extra;
      maximum += extra;
    }
  }

  const step = niceStep(maximum - minimum, targetTicks);
  if (options.symmetric) {
    const bound = Math.ceil(Math.max(Math.abs(minimum), Math.abs(maximum)) / step) * step;
    minimum = -bound;
    maximum = bound;
  } else {
    minimum = Math.floor(minimum / step) * step;
    maximum = Math.ceil(maximum / step) * step;
    if (includeZero) {
      minimum = Math.min(0, minimum);
      maximum = Math.max(0, maximum);
    }
  }

  const ticks = [];
  const epsilon = step / 1000;
  for (let value = minimum; value <= maximum + epsilon; value += step) {
    const normalized = Math.abs(value) < epsilon ? 0 : Number(value.toPrecision(12));
    ticks.push(normalized);
  }
  if (ticks.at(-1) < maximum - epsilon) ticks.push(maximum);

  return { minimum, maximum, ticks };
}

export function benchmarkBarCoordinate(value, domain) {
  const range = Math.max(domain.maximum - domain.minimum, Number.EPSILON);
  return Math.min(100, Math.max(0, ((value - domain.minimum) / range) * 100));
}
