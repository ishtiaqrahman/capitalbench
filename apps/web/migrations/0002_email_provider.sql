alter table email_campaigns
add column provider text not null default 'cloudflare';
