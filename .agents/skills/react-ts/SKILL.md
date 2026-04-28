---
name: react-ts
description: Create, review, or improve React TypeScript code. Use when Codex works on React components, hooks, props, state, TypeScript types, frontend structure, forms, API calls, styling integration, tests, accessibility, or Vite/Next-style React project conventions.
---

# React TS

## Goal

Build React TypeScript code that is typed, accessible, maintainable, and consistent with the existing project.

## Rules

- Inspect the existing framework, routing, styling, state management, and test setup before adding patterns.
- Prefer explicit prop types for exported components.
- Keep component state minimal and derived values out of state when they can be computed safely.
- Use semantic HTML and accessible labels for interactive UI.
- Do not introduce new UI libraries, state libraries, or data-fetching libraries without user approval.
- Keep side effects in appropriate hooks and include cleanup where needed.
- Avoid broad visual redesigns unless the task is explicitly design-focused.
- Follow existing formatting and naming conventions.

## TypeScript Rules

- Avoid `any` unless the boundary is genuinely unknown and explain why.
- Prefer narrow union types for modes, variants, and statuses.
- Use runtime validation or defensive checks at external data boundaries.
- Keep exported types close to the component or module that owns them unless the project has a shared types pattern.

## Documentation Style

Write comments in Korean only for non-obvious UI behavior, accessibility constraints, or data-flow decisions. Prefer clear names and types over comments for straightforward code.
