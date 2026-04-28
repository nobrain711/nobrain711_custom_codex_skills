---
name: sql
description: Create, review, or improve SQL queries, schema changes, and database documentation. Use when Codex works on SELECT queries, joins, indexes, migrations, constraints, transactions, query performance, reporting SQL, seed data, or database-facing application code.
---

# SQL

## Goal

Write SQL that is correct, readable, and safe for the target database.

## Rules

- Identify the database dialect before using dialect-specific syntax.
- Inspect schema, constraints, indexes, and existing query style before changing SQL.
- Prefer explicit column lists over `SELECT *` except for quick inspection queries.
- Use parameterized queries in application code; do not concatenate untrusted input into SQL.
- Make joins explicit and confirm join keys.
- For migrations, include forward changes and rollback guidance when the project expects it.
- Avoid destructive statements without clear confirmation and backup or rollback context.
- Consider indexes only after identifying query patterns and write overhead.

## Documentation Style

Write SQL comments in Korean when they clarify business rules, non-obvious filters, performance assumptions, or migration safety notes.

For query changes, explain:

- 어떤 테이블과 관계를 사용했는지.
- 결과 행의 기준이 무엇인지.
- 성능상 중요한 필터, 조인, 인덱스 가정이 있는지.
