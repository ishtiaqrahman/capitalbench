export function orderedComparableBarWidth(value, minimum, maximum) {
  const range = maximum - minimum;
  if (!Number.isFinite(value)) return 0;
  if (!Number.isFinite(range) || range <= 0.0001) {
    return value > 0 ? 64 : value < 0 ? 30 : 38;
  }

  const normalized = Math.min(1, Math.max(0, (value - minimum) / range));
  const minimumWidth = 10;
  const maximumWidth = maximum <= 0 ? 48 : minimum >= 0 ? 88 : 78;
  return minimumWidth + normalized * (maximumWidth - minimumWidth);
}
