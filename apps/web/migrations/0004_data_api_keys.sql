create table if not exists data_api_keys (
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

create index if not exists idx_data_api_keys_status
  on data_api_keys(status);

create table if not exists data_api_rate_limits (
  key_hash text not null,
  window_name text not null,
  window_start text not null,
  count integer not null default 0,
  updated_at text not null,
  primary key (key_hash, window_name, window_start)
);
