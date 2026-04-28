---
name: docker
description: Create, review, or improve Docker-related project files. Use when Codex works on Dockerfiles, docker-compose files, .dockerignore, image build behavior, container runtime configuration, multi-stage builds, ports, volumes, environment variables, or containerized development workflows.
---

# Docker

## Goal

Create and maintain Docker configuration that is small, reproducible, and easy to understand.

## Rules

- Inspect the application stack before choosing a base image or build strategy.
- Prefer official, pinned major-version base images unless the project already has a stricter convention.
- Use multi-stage builds when they reduce final image size or separate build tools from runtime.
- Keep `.dockerignore` aligned with the project so builds do not copy caches, secrets, local virtual environments, or generated artifacts.
- Do not bake secrets into images. Use environment variables, secret mounts, or orchestrator-level configuration.
- Make container ports, volumes, and required environment variables explicit.
- Preserve existing compose service names and volume semantics unless the user asks for a redesign.

## Documentation Style

Write Docker comments in Korean when adding comments. Use comments only for non-obvious build choices, security constraints, or runtime assumptions.

For Docker examples, include the exact command needed to build or run when useful:

```powershell
docker build -t example-app .
docker run --rm -p 8000:8000 example-app
```
