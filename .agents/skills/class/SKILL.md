---
name: class
description: Add or improve Python class docstrings and class-level type documentation. Use when Codex needs to document a class purpose, lifecycle, constructor arguments, attributes, methods, invariants, usage examples, or behavior-preserving annotations.
---

# Class

## Goal

Document Python classes so readers can understand what the class represents, how to construct it, and how it should be used.

## Rules

- Preserve runtime behavior.
- Explain the class responsibility, lifecycle, and important invariants.
- Document constructor arguments in `__init__` or the class docstring, following the project's existing style.
- Document important public attributes when they are part of the intended API.
- Add type hints that match actual values and existing call sites.
- Do not rename attributes, methods, or constructor parameters while documenting.
- Avoid documenting every private method unless it clarifies class behavior.

## Docstring Style

Write docstrings in Korean unless the file or project clearly uses English-only documentation.

For public or reusable classes, include these sections when useful:

- `Args`: 생성자에서 받는 주요 값.
- `Attributes`: 외부에서 읽거나 사용하는 공개 속성.
- `Raises`: 생성 또는 주요 메서드 호출 중 발생할 수 있는 예외.
- `Examples`: 인스턴스를 만들고 대표 메서드를 호출하는 짧은 예시.

Example:

```python
class UserNameNormalizer:
    """사용자 이름을 일관된 표시 형식으로 정규화하는 객체.

    동일한 정규화 규칙을 여러 입력 소스에 재사용할 때 사용한다. 인스턴스는
    최대 길이 설정만 보관하며, 입력 문자열 자체는 변경하지 않는다.

    Args:
        max_length: 반환할 이름의 최대 길이.

    Attributes:
        max_length: 정규화된 이름에 적용되는 최대 길이.

    Examples:
        >>> normalizer = UserNameNormalizer(max_length=20)
        >>> normalizer.normalize("  Kim   Min  ")
        'Kim Min'
    """
```
