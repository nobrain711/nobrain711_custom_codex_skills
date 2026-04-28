---
name: project-readme
description: Create or improve project README files. Use when Codex needs to document a repository overview, setup steps, usage, commands, project layout, environment variables, testing, deployment notes, troubleshooting, or contribution guidance.
---

# Project README

## Goal

Write a README that helps a new developer understand what the project is, how to run it, and where to start.

## Rules

- Inspect the project structure, package files, config files, and existing scripts before writing setup or command instructions.
- Do not invent commands, environment variables, services, ports, or deployment steps.
- Prefer concise sections that match the actual project maturity.
- Keep placeholder text out of the final README unless the user explicitly wants a template.
- Include exact commands when they are discoverable from the project.
- Mention missing setup information clearly instead of guessing.
- Preserve existing README content that is still accurate.

## Recommended Sections

Use only the sections that fit the project:

- Project overview
- Features or included workflows
- Requirements
- Setup
- Usage
- Common commands
- Project structure
- Environment variables
- Testing
- Deployment
- Troubleshooting

## Style

Write in Korean unless the project clearly uses English-only documentation. Keep headings easy to scan and command blocks copy-pasteable.

For project-local Codex skill repositories, include:

- What skills are included.
- Where local skills and hooks live.
- How to invoke the main skills.
- How to validate skills when a validator is available.
