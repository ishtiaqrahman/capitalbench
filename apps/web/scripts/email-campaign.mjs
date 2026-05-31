#!/usr/bin/env node
import fs from "node:fs/promises";
import path from "node:path";

const DEFAULT_ENDPOINT = "https://www.capitalbench.org/api/email/send";
const DEFAULT_GROUP = "website_collection";

function usage() {
  return `Usage:
  npm run email:campaign -- --file campaigns/example/update.md --subject "CapitalBench update" --dry-run
  npm run email:campaign -- --file campaigns/example/update.md --subject "CapitalBench update" --test you@example.com
  npm run email:campaign -- --file campaigns/example/update.md --subject "CapitalBench update" --send --confirm

Options:
  --file <path>        Markdown/plain-text campaign body
  --subject <text>     Email subject
  --group <slug>       Audience group slug (default: ${DEFAULT_GROUP})
  --endpoint <url>     Admin send endpoint (default: EMAIL_ADMIN_ENDPOINT or production)
  --dry-run            Render and print summary without sending
  --test <email>       Send one test email
  --send               Send to active group members
  --confirm            Required with --send
`;
}

function parseArgs(argv) {
  const args = {
    group: DEFAULT_GROUP,
    endpoint: process.env.EMAIL_ADMIN_ENDPOINT || DEFAULT_ENDPOINT
  };
  for (let i = 0; i < argv.length; i += 1) {
    const arg = argv[i];
    if (arg === "--dry-run") args.mode = "dry-run";
    else if (arg === "--send") args.mode = "send";
    else if (arg === "--confirm") args.confirm = true;
    else if (arg === "--file") args.file = argv[++i];
    else if (arg === "--subject") args.subject = argv[++i];
    else if (arg === "--group") args.group = argv[++i];
    else if (arg === "--endpoint") args.endpoint = argv[++i];
    else if (arg === "--test") {
      args.mode = "test";
      args.testRecipient = argv[++i];
    } else if (arg === "--help" || arg === "-h") {
      args.help = true;
    } else {
      throw new Error(`Unknown argument: ${arg}`);
    }
  }
  return args;
}

function escapeHtml(value) {
  return String(value ?? "")
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;");
}

export function renderMarkdown(markdown) {
  const lines = String(markdown).replace(/\r\n/g, "\n").split("\n");
  const html = [];
  let paragraph = [];
  let listOpen = false;

  function flushParagraph() {
    if (paragraph.length) {
      html.push(`<p>${escapeHtml(paragraph.join(" "))}</p>`);
      paragraph = [];
    }
  }

  function closeList() {
    if (listOpen) {
      html.push("</ul>");
      listOpen = false;
    }
  }

  for (const line of lines) {
    const trimmed = line.trim();
    if (!trimmed) {
      flushParagraph();
      closeList();
      continue;
    }
    if (trimmed.startsWith("### ")) {
      flushParagraph();
      closeList();
      html.push(`<h3>${escapeHtml(trimmed.slice(4))}</h3>`);
      continue;
    }
    if (trimmed.startsWith("## ")) {
      flushParagraph();
      closeList();
      html.push(`<h2>${escapeHtml(trimmed.slice(3))}</h2>`);
      continue;
    }
    if (trimmed.startsWith("# ")) {
      flushParagraph();
      closeList();
      html.push(`<h1>${escapeHtml(trimmed.slice(2))}</h1>`);
      continue;
    }
    if (trimmed.startsWith("- ")) {
      flushParagraph();
      if (!listOpen) {
        html.push("<ul>");
        listOpen = true;
      }
      html.push(`<li>${escapeHtml(trimmed.slice(2))}</li>`);
      continue;
    }
    paragraph.push(trimmed);
  }

  flushParagraph();
  closeList();

  return {
    html: html.join("\n"),
    text: String(markdown).trim()
  };
}

async function main() {
  const args = parseArgs(process.argv.slice(2));
  if (args.help) {
    console.log(usage());
    return;
  }
  if (!args.file || !args.subject) {
    throw new Error("--file and --subject are required.\n\n" + usage());
  }
  if (!args.mode) {
    throw new Error("Choose --dry-run, --test, or --send.\n\n" + usage());
  }
  if (args.mode === "send" && !args.confirm) {
    throw new Error("--send requires --confirm");
  }

  const body = await fs.readFile(path.resolve(args.file), "utf8");
  const rendered = renderMarkdown(body);
  const payload = {
    groupSlug: args.group,
    subject: args.subject,
    html: rendered.html,
    text: rendered.text
  };

  if (args.mode === "dry-run") {
    console.log(JSON.stringify({
      ok: true,
      mode: "dry-run",
      group: args.group,
      subject: args.subject,
      htmlBytes: Buffer.byteLength(rendered.html),
      textBytes: Buffer.byteLength(rendered.text),
      preview: rendered.text.slice(0, 280)
    }, null, 2));
    return;
  }

  const token = process.env.EMAIL_ADMIN_TOKEN;
  if (!token) {
    throw new Error("EMAIL_ADMIN_TOKEN is required for --test and --send");
  }
  if (args.mode === "test") {
    payload.testRecipient = args.testRecipient;
  }

  const response = await fetch(args.endpoint, {
    method: "POST",
    headers: {
      "authorization": `Bearer ${token}`,
      "content-type": "application/json"
    },
    body: JSON.stringify(payload)
  });
  const result = await response.json();
  if (!response.ok || !result.ok) {
    throw new Error(JSON.stringify(result, null, 2));
  }
  console.log(JSON.stringify(result, null, 2));
}

main().catch((error) => {
  console.error(error.message);
  process.exitCode = 1;
});
