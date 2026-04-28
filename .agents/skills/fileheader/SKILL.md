---
name: fileheader
description: Add or improve Python file-level module docstrings. Use when Codex needs to explain what a Python file does, its responsibility in the project, main usage context, important side effects, or module-level constraints.
---

# Fileheader

## Goal

Add a Korean module docstring near the top of a Python file so readers can quickly understand the file's role before reading the implementation.

## Rules

- Preserve runtime behavior.
- Place the module docstring after shebang, encoding comments, and license comments, but before imports.
- Explain the file's responsibility, main usage context, and important constraints.
- Keep simple scripts short: one summary sentence plus one short paragraph is enough.
- For reusable modules, include broader context such as inputs, outputs, side effects, and integration points.
- Do not describe every function in the file unless that is necessary to understand the module.
- Do not add noisy prose that repeats the filename.

## Style

Write in Korean unless the surrounding project clearly uses English-only documentation. Prefer plain, specific sentences that a Python reader can understand without already knowing this implementation.

Example:

```python
"""사용자 입력 데이터를 검증하고 정규화하는 유틸리티 모듈.

이 모듈은 API 요청이나 CSV 행처럼 외부에서 들어온 문자열 값을 내부 도메인
객체에서 사용할 수 있는 형태로 변환한다. 각 함수는 원본 입력을 직접 수정하지
않고, 검증 실패 시 명시적인 예외를 발생시킨다.
"""
```
