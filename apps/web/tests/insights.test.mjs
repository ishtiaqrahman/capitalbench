import assert from "node:assert/strict";
import test from "node:test";
import { publishedInsightRows, roundReferenceTokens } from "../src/lib/insights.js";

test("roundReferenceTokens links CapitalBench round IDs", () => {
  const tokens = roundReferenceTokens("Compare CB-2026-06-15-1W with CB-2026-06-22-1M.");

  assert.deepEqual(tokens, [
    { type: "text", text: "Compare " },
    { type: "round", text: "CB-2026-06-15-1W", href: "/rounds/CB-2026-06-15-1W" },
    { type: "text", text: " with " },
    { type: "round", text: "CB-2026-06-22-1M", href: "/rounds/CB-2026-06-22-1M" },
    { type: "text", text: "." }
  ]);
});

test("publishedInsightRows sorts newer benchmark subjects before older high-importance insights", () => {
  const rows = publishedInsightRows([
    {
      id: "older",
      status: "published",
      importance_score: 100,
      context: { data_as_of: "2026-06-17", round_id: "CB-2026-05-17-1M" }
    },
    {
      id: "newer",
      status: "published",
      importance_score: 20,
      context: { data_as_of: "2026-06-22", round_id: "CB-2026-06-15-1W" }
    },
    {
      id: "draft-newer",
      status: "draft",
      importance_score: 200,
      context: { data_as_of: "2026-06-23" }
    }
  ]);

  assert.deepEqual(rows.map((row) => row.id), ["newer", "older"]);
});

test("publishedInsightRows uses round context before importance inside the same data date", () => {
  const rows = publishedInsightRows([
    {
      id: "older-round-high-importance",
      status: "published",
      importance_score: 100,
      data_as_of: "2026-06-22",
      context: { round_id: "CB-2026-06-15-1W" }
    },
    {
      id: "newer-round-low-importance",
      status: "published",
      importance_score: 20,
      data_as_of: "2026-06-22",
      context: { round_id: "CB-2026-06-22-1W" }
    }
  ]);

  assert.deepEqual(rows.map((row) => row.id), ["newer-round-low-importance", "older-round-high-importance"]);
});
