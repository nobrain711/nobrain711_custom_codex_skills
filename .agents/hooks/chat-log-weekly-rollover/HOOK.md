# Chat Log Weekly Rollover Hook

## Purpose

Rotate the active project chat log from `log.md` into a weekly archive under `logs/<year>/W<number>.md`.

## Trigger

Run every Monday at 00:00. This is the moment immediately after Sunday ends, so the archive uses the ISO week number for the Sunday that just ended.

## Command

```powershell
powershell -ExecutionPolicy Bypass -File .\.agents\hooks\chat-log-weekly-rollover\scripts\rollover-chat-log.ps1
```

## Register Schedule On Windows

```powershell
powershell -ExecutionPolicy Bypass -File .\.agents\hooks\chat-log-weekly-rollover\scripts\register-windows-task.ps1
```

## Expected Effect

- If `log.md` has content, append it to `logs/<year>/W<number>.md`.
- Create the archive directory when it does not exist.
- Reset `log.md` with a fresh header for the new week.
- Do nothing destructive outside the current project folder.
