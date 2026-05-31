create table if not exists audience_groups (
  id text primary key,
  slug text not null unique,
  name text not null,
  description text not null default '',
  created_at text not null
);

create table if not exists subscribers (
  id text primary key,
  email text not null,
  email_normalized text not null unique,
  status text not null check (status in ('active', 'unsubscribed', 'suppressed')),
  created_at text not null,
  updated_at text not null
);

create table if not exists audience_memberships (
  subscriber_id text not null references subscribers(id) on delete cascade,
  group_id text not null references audience_groups(id) on delete cascade,
  status text not null check (status in ('active', 'unsubscribed')),
  source text not null,
  consent_text text not null,
  consent_version text not null,
  created_at text not null,
  updated_at text not null,
  primary key (subscriber_id, group_id)
);

create table if not exists email_campaigns (
  id text primary key,
  group_id text not null references audience_groups(id),
  subject text not null,
  content_hash text not null,
  status text not null check (status in ('draft', 'test_sent', 'sending', 'sent', 'failed')),
  recipient_count integer not null default 0,
  sent_count integer not null default 0,
  failed_count integer not null default 0,
  created_at text not null,
  sent_at text
);

create index if not exists idx_subscribers_status on subscribers(status);
create index if not exists idx_audience_memberships_group_status on audience_memberships(group_id, status);
create index if not exists idx_email_campaigns_group_created on email_campaigns(group_id, created_at);

insert into audience_groups (id, slug, name, description, created_at)
values (
  'website_collection',
  'website_collection',
  'Website Collection',
  'Emails collected from public website signup forms.',
  '2026-05-31T00:00:00.000Z'
)
on conflict(slug) do update set
  name = excluded.name,
  description = excluded.description;
