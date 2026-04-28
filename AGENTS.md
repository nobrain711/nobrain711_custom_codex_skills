# AGENTS.md

## Role

Act as a project-local Codex workflow agent for this folder. Focus on creating, editing, and explaining Codex skills and hooks for Python documentation, Docker, Kubernetes, React TypeScript, and SQL work.

## Scope

All skills and hooks created for this project must be stored relative to the current project folder, not in the user's global Codex home.

Use these locations:

- Skills: `.agents/skills/<skill-name>/`
- Hooks: `.agents/hooks/<hook-name>/`

## Skill Rules

- Use lowercase hyphenated skill names.
- Keep `SKILL.md` concise and focused on reusable behavior.
- Put detailed reusable material in `references/` only when `SKILL.md` would become bulky.
- Add `agents/openai.yaml` when the skill should appear clearly in skill lists.
- Validate skills with the available skill validator after edits.

## Local Documentation Skills

- Use `$fileheader` for Python file-level module docstrings.
- Use `$function` for Python function and method docstrings plus accurate type hints.
- Use `$class` for Python class docstrings, constructor documentation, attributes, and class-level type documentation.
- Use `$comment` for Korean inline and block comments that explain non-obvious intent or constraints.

## Local Engineering Skills

- Use `$docker` for Dockerfiles, docker-compose files, image builds, and container workflows.
- Use `$github-actions` for GitHub Actions CI, workflow YAML, permissions, secrets, matrices, caches, and artifacts.
- Use `$k8s` for Kubernetes manifests, deployment resources, kubectl workflow notes, and cluster-facing configuration.
- Use `$project-readme` for repository README creation, setup instructions, usage documentation, project layout, and command documentation.
- Use `$python-test` for Python pytest/unittest tests, fixtures, edge cases, regression tests, and filesystem behavior tests.
- Use `$react-ts` for React TypeScript components, hooks, props, state, accessibility, and frontend typing.
- Use `$sql` for SQL queries, migrations, schema documentation, joins, indexes, and database-facing code.

## Python Documentation Rules

- Preserve runtime behavior when adding comments, docstrings, or type hints.
- Prefer type hints that match existing runtime values and imports.
- Use docstrings for public modules, classes, functions, and methods when the behavior is not obvious.
- Add a module docstring to Python files so readers can quickly understand the file's role, responsibility, and main usage context.
- Write comments and docstrings in Korean unless the surrounding project clearly uses English-only documentation.
- Write Korean comments so a reader can understand the intent without already knowing the implementation details.
- Keep inline comments rare and use them only to clarify non-obvious intent, invariants, edge cases, or tradeoffs.
- Do not add noisy comments that restate the code.
- Write function docstrings so a reader can roughly use the function after one pass.
- For modularized public APIs, write documentation at the level expected from official packages: purpose, parameters, return value, raised errors, side effects, and a concise example when useful.
- Avoid broad formatting or refactoring unless required to add accurate documentation or type hints.

## Hook Rules

- Keep hooks project-local under `.agents/hooks/`.
- Make hook behavior explicit before adding automation.
- Prefer small, auditable scripts over broad shell commands.
- Document the trigger, command, and expected effect in the hook folder.

## Git Workflow Rules

- Keep `main` as the stable branch.
- Create a domain branch before starting non-trivial work.
- Use branch prefixes by work area:
  - `python/<short-topic>` for Python documentation, tests, or Python examples.
  - `react/<short-topic>` for React TypeScript work.
  - `sql/<short-topic>` for SQL work.
  - `docker/<short-topic>` for Docker work.
  - `k8s/<short-topic>` for Kubernetes work.
  - `github-actions/<short-topic>` for GitHub Actions workflow work.
  - `docs/<short-topic>` for README or general documentation work.
  - `skills/<short-topic>` for project-local skill or hook changes.
- Use lowercase hyphenated branch topics.
- Check `git status --short` before switching branches, committing, or pushing.

## Commit Rules

- Use Conventional Commits: `<type>(<scope>): <summary>`.
- Keep summaries short, imperative, and lowercase after the type.
- Prefer these types:
  - `feat`: new skill, workflow, example, or user-visible capability.
  - `fix`: bug fix or correction.
  - `docs`: README, comments, docstrings, or documentation-only changes.
  - `test`: test code or test fixtures.
  - `chore`: repository maintenance, cleanup, config, or tooling.
  - `refactor`: behavior-preserving restructuring.
- Use scopes that match the work area, such as `python`, `react`, `sql`, `docker`, `k8s`, `github-actions`, `skills`, or `readme`.
- Do not mix unrelated domains in one commit unless the user explicitly asks for a combined change.

## Working Style

- Inspect current files before changing them.
- Preserve user-created changes.
- Keep examples small and easy to delete.
- Do not add unrelated application scaffolding unless explicitly requested.
