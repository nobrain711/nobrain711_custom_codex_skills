---
name: function
description: Add or improve Python function and method docstrings with accurate type hints. Use when Codex needs to document function purpose, parameters, return values, raised errors, side effects, examples, or add behavior-preserving annotations.
---

# Function

## Goal

Document Python functions and methods so a reader can roughly use them after reading once.

## Rules

- Preserve runtime behavior.
- Add type hints that match observed values and existing call sites.
- Do not add imports with runtime side effects just for annotations.
- Prefer built-in generics such as `list[str]` when the project supports modern Python.
- Use `typing` imports only when they improve clarity or compatibility.
- Avoid changing function names, parameter order, defaults, or return shapes.
- Keep private helper docstrings optional; add them only when they clarify intent.

## Docstring Style

Write docstrings in Korean unless the file or project clearly uses English-only documentation.

For public functions and methods, include these sections when useful:

- `Args`: 중요한 매개변수와 제약.
- `Returns`: 반환값의 의미와 형태.
- `Raises`: 호출자가 처리해야 하는 예외.
- `Examples`: 한 번 보고 따라 할 수 있는 짧은 예시.

Example:

```python
def normalize_user_name(name: str, *, max_length: int = 40) -> str:
    """사용자 이름을 저장 가능한 표시 이름으로 정규화한다.

    앞뒤 공백을 제거하고, 연속된 공백을 하나로 줄인 뒤 최대 길이를 넘지 않도록
    자른다. 빈 문자열은 유효한 표시 이름이 아니므로 예외를 발생시킨다.

    Args:
        name: 사용자가 입력한 원본 이름.
        max_length: 반환할 이름의 최대 길이.

    Returns:
        정규화된 사용자 표시 이름.

    Raises:
        ValueError: 정규화 후 이름이 비어 있을 때.

    Examples:
        >>> normalize_user_name("  Kim   Min  ")
        'Kim Min'
    """
```
