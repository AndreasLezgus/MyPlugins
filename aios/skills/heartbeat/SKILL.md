---
name: heartbeat
description: Prüft, ob die Infrastruktur läuft und ob die Cron-Jobs tatsächlich ausgeführt wurden.
---

## Systemprüfungen (bei jedem Heartbeat ausführen)

**Browser:** Prüfen, ob der von verwendete Browser (Safari) läuft. Falls nicht laufend: Browser starten. 
Matthias ist darauf für seine Content Erstellung angewiesen.

**Cron-Jobs:** Prüfen, ob tägliche Jobs einen veralteten lastRunAtMs-Wert haben (>26 Stunden).
Falls veraltet, per CLI auslösen: claude cron run <jobId> --force

Zu überwachende Jobs:
- Matthias Content (8:01 Uhr): 01f2e5c5-3a83-4018-a725-dee59e54733e
- Claudia Newsletter (18:01 Uhr): [ID ERGÄNZEN]

Jede Prüfung nur einmal pro Heartbeat-Session ausführen.

