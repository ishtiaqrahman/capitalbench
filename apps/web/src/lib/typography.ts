export type NoOrphanTextParts = {
  lead: string;
  tail: string;
};

export function noOrphanTextParts(text: string, keepWords = 2): NoOrphanTextParts {
  const normalized = text.trim().replace(/\s+/g, " ");
  if (!normalized) return { lead: "", tail: "" };

  const words = normalized.split(" ");
  if (words.length <= keepWords) return { lead: "", tail: normalized };

  return {
    lead: words.slice(0, -keepWords).join(" "),
    tail: words.slice(-keepWords).join(" ")
  };
}
