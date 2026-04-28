---
name: github-actions
description: Create, review, or improve GitHub Actions workflows. Use when Codex works on .github/workflows YAML files, CI jobs, build/test/lint automation, deployment workflows, reusable workflows, action permissions, secrets, matrices, caches, artifacts, or workflow troubleshooting.
---

# GitHub Actions

## Goal

Create GitHub Actions workflows that are secure, readable, and aligned with the project's build and release process.

## Rules

- Inspect existing `.github/workflows` files before adding a new workflow.
- Keep workflow names, job names, and step names explicit enough to understand in the Actions UI.
- Use the minimum required `permissions` for each workflow or job.
- Do not hard-code secrets. Reference GitHub Actions secrets or environment variables.
- Pin third-party actions to a version tag or commit SHA according to the project's existing security standard.
- Prefer dependency caching only when the package manager lockfile and cache key are clear.
- Use matrices only when they reduce duplication or intentionally test multiple versions/platforms.
- Keep deployment jobs gated with branches, environments, approvals, or explicit conditions when appropriate.
- Avoid adding broad automation that changes releases, deployments, or repository state without user confirmation.

## Workflow Style

Write YAML comments in Korean only when they explain non-obvious CI behavior, security constraints, or release conditions. Prefer clear step names over comments for straightforward commands.

For workflow changes, explain:

- 어떤 이벤트가 workflow를 실행하는지.
- 어떤 job이 어떤 순서와 조건으로 실행되는지.
- 어떤 secrets, permissions, cache, artifacts가 필요한지.
- 실패했을 때 어디를 먼저 확인해야 하는지.

Example:

```yaml
name: CI

on:
  pull_request:
  push:
    branches: [main]

permissions:
  contents: read

jobs:
  test:
    name: Test
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
```
