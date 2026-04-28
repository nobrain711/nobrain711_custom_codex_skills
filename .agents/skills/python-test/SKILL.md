---
name: python-test
description: Create, review, or improve Python test code. Use when Codex needs to add pytest or unittest tests, test fixtures, parametrized cases, regression tests, edge case coverage, temporary file tests, exception assertions, or test documentation for Python code.
---

# Python Test

## Goal

Write Python tests that verify behavior clearly without overfitting to implementation details.

## Rules

- Inspect the existing test framework before adding tests.
- Prefer the project's current style, fixtures, naming, and assertion patterns.
- If no framework exists, prefer `pytest` for new test examples unless the project clearly requires `unittest`.
- Test public behavior and important edge cases rather than private implementation details.
- Include regression tests when fixing a bug.
- Use temporary directories or files for filesystem behavior.
- Avoid network, time, randomness, and environment dependencies unless they are controlled.
- Keep tests deterministic and easy to run locally.
- Do not change production behavior just to make tests pass unless the user asked for a fix.

## Coverage Targets

For Python modules, consider:

- Normal successful paths.
- Boundary values.
- Invalid inputs and raised exceptions.
- File read/write behavior.
- Serialization and deserialization.
- State changes that callers rely on.

## Style

Write test names in English if the project already follows English naming. Korean comments are acceptable when they clarify non-obvious test intent, but prefer clear test names and assertions.

Example:

```python
def test_divide_rejects_zero() -> None:
    calculator = Calculator()

    with pytest.raises(ZeroDivisionError):
        calculator.divide(10, 0)
```
