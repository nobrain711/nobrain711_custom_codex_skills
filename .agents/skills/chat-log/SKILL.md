---
name: chat-log
description: Maintain project-local chat logs and weekly log archives. Use when Codex needs to write the current session summary to log.md, rotate log.md into weekly archive files under logs by year and week number, configure weekly chat-log hooks, or explain the chat logging workflow.
---

# Chat Log

## Goal

Keep important project conversation history in `log.md` first, then archive it weekly under `logs/<year>/W<number>.md`.

## Rules

- Store the active chat log at project root `log.md`.
- Keep weekly archives under `logs/<iso-week-year>/W<iso-week-number>.md`.
- Treat Monday 00:00 as the rollover time for the week that ended on Sunday.
- When rotating, archive the current `log.md` content before resetting it.
- Do not include secrets, tokens, private keys, or credentials in logs.
- Prefer concise session summaries over full raw transcripts unless the user explicitly asks for verbatim logging.
- Keep log entries chronological and easy to scan.

## Log Entry Style

Write log entries in Korean unless the project clearly uses English-only documentation.

Use this shape:

```md
## YYYY-MM-DD HH:mm - Short Title

- 요청:
- 결정:
- 변경:
- 검증:
- 다음 작업:
```

## Hook Workflow

Use `.agents/hooks/chat-log-weekly-rollover/` for the project-local hook. The hook script rotates `log.md` into `logs/<year>/W<number>.md` and creates a fresh `log.md` for the new week.

On Windows, register the schedule with:

```powershell
powershell -ExecutionPolicy Bypass -File .\.agents\hooks\chat-log-weekly-rollover\scripts\register-windows-task.ps1
```
