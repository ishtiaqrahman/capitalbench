import { randomBytes, randomUUID, webcrypto } from "node:crypto";
import { execFileSync } from "node:child_process";

function argValue(name, fallback = "") {
  const index = process.argv.indexOf(name);
  if (index < 0) return fallback;
  return process.argv[index + 1] ?? fallback;
}

function hasFlag(name) {
  return process.argv.includes(name);
}

function base64url(bytes) {
  return bytes.toString("base64").replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/g, "");
}

async function sha256Hex(value) {
  const data = new TextEncoder().encode(String(value));
  const hash = await webcrypto.subtle.digest("SHA-256", data);
  return Array.from(new Uint8Array(hash))
    .map((byte) => byte.toString(16).padStart(2, "0"))
    .join("");
}

function sqlString(value) {
  return String(value ?? "").replace(/'/g, "''");
}

const name = argValue("--name");
const email = argValue("--email");
const database = argValue("--database", "capitalbench_email");
const minuteLimit = Number(argValue("--minute-limit", "120"));
const dayLimit = Number(argValue("--day-limit", "10000"));
const apply = hasFlag("--apply");

if (!name) {
  console.error("Usage: node scripts/api-key.mjs --name \"Firm Name\" [--email analyst@example.com] [--apply]");
  process.exit(1);
}

const key = `cb_live_${base64url(randomBytes(32))}`;
const keyHash = await sha256Hex(key);
const id = randomUUID();
const createdAt = new Date().toISOString();
const schemaSql = `create table if not exists data_api_keys (
  id text primary key,
  key_hash text not null unique,
  name text not null,
  email text,
  status text not null default 'active' check (status in ('active', 'disabled', 'revoked')),
  scopes text not null default 'read:v1',
  rate_limit_per_minute integer,
  rate_limit_per_day integer,
  created_at text not null,
  last_used_at text
);
create index if not exists idx_data_api_keys_status on data_api_keys(status);
create table if not exists data_api_rate_limits (
  key_hash text not null,
  window_name text not null,
  window_start text not null,
  count integer not null default 0,
  updated_at text not null,
  primary key (key_hash, window_name, window_start)
);`;
const insertSql = `insert into data_api_keys
  (id, key_hash, name, email, status, scopes, rate_limit_per_minute, rate_limit_per_day, created_at)
values
  ('${id}', '${keyHash}', '${sqlString(name)}', ${email ? `'${sqlString(email)}'` : "null"}, 'active', 'read:v1', ${minuteLimit}, ${dayLimit}, '${createdAt}');`;

const result = {
  api_key: key,
  key_hash: keyHash,
  id,
  name,
  email: email || null,
  database,
  rate_limit_per_minute: minuteLimit,
  rate_limit_per_day: dayLimit,
  schema_sql: schemaSql,
  insert_sql: insertSql
};

if (apply) {
  execFileSync(
    "npx",
    ["wrangler", "d1", "execute", database, "--remote", "--command", schemaSql],
    { stdio: "inherit" }
  );
  execFileSync(
    "npx",
    ["wrangler", "d1", "execute", database, "--remote", "--command", insertSql],
    { stdio: "inherit" }
  );
  result.applied = true;
}

console.log(JSON.stringify(result, null, 2));
