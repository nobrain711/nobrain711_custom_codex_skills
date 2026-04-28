---
name: comment
description: Add or improve Korean Python inline and block comments. Use when Codex needs to clarify non-obvious intent, invariants, edge cases, external constraints, performance tradeoffs, or maintenance warnings without changing behavior.
---

# Comment

## Goal

Add Korean comments that help a reader understand why code exists or what assumption it protects.

## Rules

- Preserve runtime behavior.
- Keep comments rare and high-signal.
- Explain intent, assumptions, invariants, edge cases, external constraints, or tradeoffs.
- Do not translate simple code operations into Korean.
- Do not add comments that restate the next line.
- Prefer improving unclear names or structure only if the user explicitly asks for refactoring; otherwise keep documentation-only changes narrow.
- Remove or update stale comments when they conflict with the code.

## Style

Write for readers who understand Python but do not yet know this implementation.

Prefer:

```python
# 입력 순서를 유지해야 이후 결과를 원본 행 번호와 다시 매칭할 수 있다.
```

Avoid:

```python
# 리스트에 값을 추가한다.
```
