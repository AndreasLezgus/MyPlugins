---
name: heartbeat
description: Prüft, ob die Infrastruktur läuft und ob die Cron-Jobs tatsächlich ausgeführt wurden.
---

## Systemprüfungen (bei jedem Heartbeat ausführen)

**Browser:** Prüfen, ob der verwendete Browser (Safari) läuft. Falls nicht laufend: Browser starten.
Matthias ist darauf für seine Content-Erstellung angewiesen.

**Cron-Jobs:** Alle Scheduled Tasks auflisten (`list_scheduled_tasks`) und prüfen, ob tägliche Jobs einen veralteten `lastRunAt`-Wert haben (>26 Stunden seit letztem Lauf).
Falls veraltet, per CLI auslösen: `claude cron run <jobId> --force`

Zu überwachende Jobs (per `list_scheduled_tasks` identifizieren):
- **Matthias Content** – läuft morgens, erstellt Content-Pipeline-Output
- **Claudia Newsletter** – läuft abends, erstellt Newsletter aus Wochenproduktion

> **Hinweis:** Job-IDs sind dynamisch. Nicht hardcoden, sondern immer per `list_scheduled_tasks` auflösen. Falls ein erwarteter Job fehlt, dies im Heartbeat-Protokoll melden.

Jede Prüfung nur einmal pro Heartbeat-Session ausführen.
