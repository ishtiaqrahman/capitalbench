const countSelectors = [
  ".ai-positioning-summary strong",
  ".ai-positioning-summary em",
  ".live-risk-pulse-score strong",
  ".live-risk-pulse-compare strong",
  ".live-risk-driver-list em",
  ".live-risk-regime-list em",
  ".current-setup-stat-row strong",
  ".live-dashboard-promo-stats strong",
  ".live-dashboard-promo-stats em",
  "#benchmark-insights .insight-calculation-list dd",
  ".score-vertical-value",
  ".score-mobile-rank-head > strong",
  ".track-scorecard-value",
  ".published-score-context span",
  ".market-regime-preview-return"
].join(",");

const groupSelectors = [
  ".score-vertical-plot",
  ".score-mobile-rank-chart",
  ".track-scorecard-panel",
  ".latest-official-result-panel",
  ".ai-positioning-summary",
  ".live-risk-pulse",
  ".insight-card",
  ".benchmark-evidence-card",
  ".current-setup-panel",
  ".live-dashboard-promo",
  ".published-score-context",
  ".market-regime-preview-panel"
].join(",");

const skipNumberPattern = /\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec|January|February|March|April|June|July|August|September|October|November|December)\b/i;
const numberPattern = /([+-]?)(\d[\d,]*(?:\.\d+)?)(%?)/g;
const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

type CountToken = HTMLSpanElement & {
  dataset: DOMStringMap & {
    countFinal?: string;
    countDecimals?: string;
    countSuffix?: string;
    countPlus?: string;
  };
};

function easing(progress: number): number {
  return 1 - Math.pow(1 - progress, 3);
}

function isVisible(element: Element): boolean {
  if (element.closest("[hidden]")) return false;
  return element.getClientRects().length > 0;
}

function formatCount(value: number, decimals: number, suffix: string, showPlus: boolean): string {
  const safeValue = Math.abs(value) < 0.000001 ? 0 : value;
  const sign = safeValue < 0 ? "-" : showPlus && safeValue > 0 ? "+" : "";
  return `${sign}${Math.abs(safeValue).toFixed(decimals)}${suffix}`;
}

function animateCount(token: CountToken, delay: number): void {
  const finalValue = Number(token.dataset.countFinal);
  if (!Number.isFinite(finalValue)) return;

  const decimals = Number(token.dataset.countDecimals ?? "0");
  const suffix = token.dataset.countSuffix ?? "";
  const showPlus = token.dataset.countPlus === "true";
  const duration = Math.min(1150, Math.max(720, 740 + Math.abs(finalValue) * 7));

  if (reducedMotion) {
    token.textContent = formatCount(finalValue, decimals, suffix, showPlus);
    return;
  }

  window.setTimeout(() => {
    const start = Date.now();

    const interval = window.setInterval(() => {
      const progress = Math.min(1, (Date.now() - start) / duration);
      token.textContent = formatCount(finalValue * easing(progress), decimals, suffix, showPlus);
      if (progress >= 1) window.clearInterval(interval);
    }, 16);
  }, delay);
}

function prepareTextNode(node: Text): CountToken[] {
  const text = node.textContent ?? "";
  numberPattern.lastIndex = 0;
  if (!numberPattern.test(text) || skipNumberPattern.test(text)) {
    numberPattern.lastIndex = 0;
    return [];
  }
  numberPattern.lastIndex = 0;

  const fragment = document.createDocumentFragment();
  const tokens: CountToken[] = [];
  let cursor = 0;
  let match: RegExpExecArray | null;

  while ((match = numberPattern.exec(text)) !== null) {
    const [raw, sign, numericText, suffix] = match;
    const start = match.index;
    const finalNumber = Number(`${sign}${numericText.replace(/,/g, "")}`);
    if (!Number.isFinite(finalNumber)) continue;

    if (start > cursor) fragment.append(text.slice(cursor, start));

    const decimals = numericText.includes(".") ? numericText.split(".")[1].length : 0;
    const token = document.createElement("span") as CountToken;
    token.dataset.countToken = "true";
    token.dataset.countFinal = String(finalNumber);
    token.dataset.countDecimals = String(decimals);
    token.dataset.countSuffix = suffix;
    token.dataset.countPlus = sign === "+" ? "true" : "false";
    token.textContent = formatCount(0, decimals, suffix, sign === "+");
    fragment.append(token);
    tokens.push(token);
    cursor = start + raw.length;
  }

  if (cursor < text.length) fragment.append(text.slice(cursor));
  if (tokens.length > 0) node.replaceWith(fragment);
  return tokens;
}

function shouldSkipTextNode(node: Text): boolean {
  const parent = node.parentElement;
  if (!parent) return true;
  return Boolean(parent.closest("small, script, style, time, [data-count-up-skip]"));
}

function prepareCountElement(element: Element): CountToken[] {
  if ((element as HTMLElement).dataset.countPrepared === "true") return [];
  (element as HTMLElement).dataset.countPrepared = "true";

  const walker = document.createTreeWalker(element, NodeFilter.SHOW_TEXT, {
    acceptNode(node) {
      return shouldSkipTextNode(node as Text) ? NodeFilter.FILTER_REJECT : NodeFilter.FILTER_ACCEPT;
    }
  });

  const textNodes: Text[] = [];
  while (walker.nextNode()) textNodes.push(walker.currentNode as Text);
  return textNodes.flatMap(prepareTextNode);
}

function prepareBar(element: HTMLElement): void {
  if (element.dataset.revealPrepared === "true") return;
  element.dataset.revealPrepared = "true";
  if (!reducedMotion) element.style.setProperty("--reveal-scale", "0.001");
}

function prepareMeter(element: HTMLElement): void {
  if (element.dataset.revealPrepared === "true") return;
  element.dataset.revealPrepared = "true";
  const finalPosition = element.style.getPropertyValue("--pulse-position") || getComputedStyle(element).getPropertyValue("--pulse-position");
  element.dataset.revealPulsePosition = finalPosition.trim() || "0%";
  if (!reducedMotion) element.style.setProperty("--pulse-position", "0%");
}

function revealElement(element: HTMLElement, delay: number): void {
  if (element.dataset.revealed === "true") return;
  element.dataset.revealed = "true";

  if (element.dataset.countToken === "true") {
    animateCount(element as CountToken, delay);
    return;
  }

  window.setTimeout(() => {
    if (element.dataset.revealMeter === "true") {
      element.style.setProperty("--pulse-position", element.dataset.revealPulsePosition || "0%");
      return;
    }

    if (element.dataset.revealBar) {
      element.style.setProperty("--reveal-scale", "1");
    }
  }, reducedMotion ? 0 : delay);
}

function groupFor(element: Element): Element {
  return element.closest(groupSelectors) ?? element;
}

function revealGroup(group: Element, groupedElements: Map<Element, HTMLElement[]>): void {
  const elements = groupedElements.get(group) ?? [];
  elements.forEach((element, index) => revealElement(element, Math.min(index * 55, 420)));
}

function setupHomepageReveals(): void {
  const groupedElements = new Map<Element, HTMLElement[]>();

  function addToGroup(element: HTMLElement): void {
    const group = groupFor(element);
    const elements = groupedElements.get(group) ?? [];
    if (!elements.includes(element)) elements.push(element);
    groupedElements.set(group, elements);
  }

  document.querySelectorAll(countSelectors).forEach((element) => {
    prepareCountElement(element).forEach(addToGroup);
  });

  document.querySelectorAll<HTMLElement>("[data-reveal-bar]").forEach((element) => {
    prepareBar(element);
    addToGroup(element);
  });

  document.querySelectorAll<HTMLElement>("[data-reveal-meter]").forEach((element) => {
    prepareMeter(element);
    addToGroup(element);
  });

  if (reducedMotion || !("IntersectionObserver" in window)) {
    Array.from(groupedElements.keys()).forEach((group) => revealGroup(group, groupedElements));
    return;
  }

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting || !isVisible(entry.target)) return;
        revealObservedGroup(entry.target);
      });
    },
    { rootMargin: "0px 0px -12% 0px", threshold: 0.2 }
  );

  groupedElements.forEach((_elements, group) => observer.observe(group));

  function revealObservedGroup(group: Element): void {
    revealGroup(group, groupedElements);
    observer.unobserve(group);
    groupedElements.delete(group);
  }

  function revealVisibleGroups(): void {
    groupedElements.forEach((_elements, group) => {
      if (!isVisible(group)) return;
      const rect = group.getBoundingClientRect();
      if (rect.top < window.innerHeight * 0.88 && rect.bottom > 0) {
        revealObservedGroup(group);
      }
    });
  }

  let visibilityCheckQueued = false;
  function queueRevealVisibleGroups(): void {
    if (visibilityCheckQueued) return;
    visibilityCheckQueued = true;
    requestAnimationFrame(() => {
      visibilityCheckQueued = false;
      revealVisibleGroups();
    });
  }

  window.addEventListener("scroll", queueRevealVisibleGroups, { passive: true });
  window.addEventListener("resize", queueRevealVisibleGroups);
  queueRevealVisibleGroups();
  const visibilityPoll = window.setInterval(revealVisibleGroups, 250);
  window.setTimeout(() => window.clearInterval(visibilityPoll), 90000);

  const mutationObserver = new MutationObserver(() => {
    queueRevealVisibleGroups();
  });

  mutationObserver.observe(document.body, {
    attributes: true,
    subtree: true,
    attributeFilter: ["hidden", "class", "style", "data-active-track", "data-active-index"]
  });
}

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", setupHomepageReveals, { once: true });
} else {
  setupHomepageReveals();
}
