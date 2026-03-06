---
name: memory
description: > 
Courated long-term memory. Not raw logs. Not everything that ever happened. The stuff that matters.
---

# MEMORY.md

## Shubham's Writing Preferences
- NO EM DASHES. Use colons, periods, or restructure.

## Hard Lessons
- NEVER delete project folders without asking Shubham. On Feb 26,
  deleted Ross's gemini-council React app during cleanup. The React
  version was lost. Always ask before removing anything in agent
  project directories.

## Memory System (2026-02-26)
- Tried self-hosted Mem0 (Ollama + SQLite) → crashes, stored nothing.
- Tried Mem0 hosted API → free tier too limited. Removed.
- Now using built-in memory-core: Gemini embeddings, hybrid search,
  temporal decay, MMR. No external dependencies.