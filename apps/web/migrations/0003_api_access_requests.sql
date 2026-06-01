create table if not exists api_access_requests (
  id text primary key,
  name text not null,
  email text not null,
  email_normalized text not null unique,
  source text not null default 'api_page',
  status text not null default 'requested' check (status in ('requested', 'contacted', 'approved', 'declined')),
  notification_status text not null default 'pending' check (notification_status in ('pending', 'sent', 'failed')),
  notification_provider text,
  notification_message_id text,
  notification_error text,
  created_at text not null,
  updated_at text not null,
  notified_at text
);

create index if not exists idx_api_access_requests_status_created
  on api_access_requests(status, created_at);

create index if not exists idx_api_access_requests_notification_status
  on api_access_requests(notification_status);
