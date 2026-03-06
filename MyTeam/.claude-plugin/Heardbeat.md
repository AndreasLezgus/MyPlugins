---
name: heardbeat
description: > 
Checks whether the infrastructure is alive, and whether the cron jobs actually ran.
---


## Health Checks (run on each heartbeat)

**Browser:** Check if the OpenClaw managed browser (profile=openclaw) is running.
If running: false, start it. The browser has X account logged in.
Dwight depends on it for intel sweeps.

**Cron jobs:** Check if any daily jobs have stale lastRunAtMs (>26 hours).
If stale, trigger via CLI: openclaw cron run <jobId> --force

Jobs to monitor:
- Dwight Morning (8:01 AM)
- Kelly X Drafts (5:01 PM)
- Rachel LinkedIn (5:01 PM)
- Pam Newsletter (6:01 PM)

Only run each check once per heartbeat session.


Beispiele:

## Cron Health Check (run on each heartbeat)

Check if any daily cron jobs have stale lastRunAtMs (>26 hours
since last run). If stale, trigger them via CLI:
`openclaw cron run <jobId> --force`

Jobs to monitor:
- Dwight Morning (8:01 AM): 01f2e5c5-3a83-4018-a725-dee59e54733e
- Kelly Viral (9:01 AM, 1:01 PM): c9458766-78bb-4eeb-b8f4-d63dc1f0e601
- Ross Engineering (10:01 AM): b12b2fc6-dd7d-4123-b904-2148a5cfb70b
- Dwight Afternoon (4:01 PM): 19ff40e4-b1b0-4d32-9d24-753ac2cf8f46
- Kelly X Drafts (5:01 PM): 05da0c81-39e1-4d06-bdcd-2dfab4562ba4
- Rachel LinkedIn (5:01 PM): 9819bc6b-7e36-406f-b0c3-d80ca383d914