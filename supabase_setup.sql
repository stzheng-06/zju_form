create table if not exists public.survey_responses (
  id uuid primary key,
  created_at timestamptz not null default now(),
  survey_version text not null,
  consent boolean not null check (consent is true),
  answers jsonb not null check (jsonb_typeof(answers) = 'object')
);

alter table public.survey_responses enable row level security;
revoke all on public.survey_responses from anon, authenticated;
grant insert on public.survey_responses to anon;
drop policy if exists survey_responses_anon_insert on public.survey_responses;
create policy survey_responses_anon_insert
  on public.survey_responses for insert to anon
  with check (consent is true and jsonb_typeof(answers) = 'object');
