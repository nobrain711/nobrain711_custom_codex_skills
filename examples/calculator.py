"""계산 결과를 기록하고 파일로 저장할 수 있는 간단한 계산기 모듈.

이 모듈은 사칙연산을 수행하는 `Calculator` 클래스를 제공한다. 각 연산은
계산 기록에 자동으로 저장되며, 기록은 JSON 파일로 저장하거나 다시 불러올 수
있다. 예제나 테스트에서 사용하기 쉽도록 외부 의존성 없이 표준 라이브러리만
사용한다.
"""

from __future__ import annotations

import json
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any


Number = int | float


@dataclass(frozen=True)
class CalculationRecord:
    """계산기에서 수행한 한 번의 사칙연산을 표현하는 불변 기록.

    `CalculationRecord`는 `Calculator.history`에 저장되는 단일 기록 단위다.
    한 번 생성된 기록은 변경되지 않으므로, 저장 전에 기록 내용이 실수로
    바뀌는 상황을 막을 수 있다. JSON 저장 시에는 `dataclasses.asdict()`로
    직렬화할 수 있는 단순한 값만 보관한다.

    Args:
        operation: 수행한 연산 이름.
        left: 왼쪽 피연산자.
        right: 오른쪽 피연산자.
        result: 연산 결과.

    Attributes:
        operation: `add`, `subtract`, `multiply`, `divide` 중 하나의 연산 이름.
        left: 계산에 사용된 왼쪽 값.
        right: 계산에 사용된 오른쪽 값.
        result: 계산 결과.

    Examples:
        >>> record = CalculationRecord("add", 2, 3, 5)
        >>> record.result
        5
    """

    operation: str
    left: Number
    right: Number
    result: Number


class Calculator:
    """사칙연산 결과를 기록하고 JSON 파일로 저장하는 계산기.

    `Calculator`는 기본적인 덧셈, 뺄셈, 곱셈, 나눗셈을 제공한다. 각 연산
    메서드는 계산 결과를 반환하면서 내부 기록에도 같은 내용을 추가한다.
    저장된 기록은 `save_history()`로 JSON 파일에 저장하고, `load_history()`로
    다시 불러올 수 있다. 인스턴스는 별도의 외부 리소스를 소유하지 않으며,
    계산 기록은 명시적으로 저장하거나 지우기 전까지 메모리에 유지된다.

    Attributes:
        history: 지금까지 수행한 계산 기록 목록. `load_history()`를 호출하면
            파일에서 읽은 기록으로 전체 목록이 교체된다.

    Raises:
        ZeroDivisionError: `divide()`에서 0으로 나누려고 할 때.
        OSError: `save_history()` 또는 `load_history()`가 파일 시스템에 접근하지
            못할 때.
        ValueError: `load_history()`가 계산 기록 형식이 아닌 JSON을 읽을 때.

    Examples:
        >>> calculator = Calculator()
        >>> calculator.add(2, 3)
        5
        >>> calculator.divide(10, 2)
        5.0
        >>> len(calculator.history)
        2

        계산 기록을 파일로 저장한 뒤 다른 계산기 인스턴스에서 다시 사용할 수 있다.

        >>> from pathlib import Path
        >>> path = Path("history.json")
        >>> calculator.save_history(path)
        >>> restored = Calculator()
        >>> restored.load_history(path)
        >>> restored.history[0].result
        5
    """

    def __init__(self) -> None:
        """빈 계산 기록을 가진 계산기를 생성한다."""

        self.history: list[CalculationRecord] = []

    def add(self, left: Number, right: Number) -> Number:
        """두 숫자를 더하고 계산 기록에 저장한다.

        Args:
            left: 더할 왼쪽 값.
            right: 더할 오른쪽 값.

        Returns:
            두 값을 더한 결과.
        """

        return self._record("add", left, right, left + right)

    def subtract(self, left: Number, right: Number) -> Number:
        """왼쪽 값에서 오른쪽 값을 빼고 계산 기록에 저장한다.

        Args:
            left: 기준이 되는 왼쪽 값.
            right: 왼쪽 값에서 뺄 오른쪽 값.

        Returns:
            `left - right` 계산 결과.
        """

        return self._record("subtract", left, right, left - right)

    def multiply(self, left: Number, right: Number) -> Number:
        """두 숫자를 곱하고 계산 기록에 저장한다.

        Args:
            left: 곱할 왼쪽 값.
            right: 곱할 오른쪽 값.

        Returns:
            두 값을 곱한 결과.
        """

        return self._record("multiply", left, right, left * right)

    def divide(self, left: Number, right: Number) -> float:
        """왼쪽 값을 오른쪽 값으로 나누고 계산 기록에 저장한다.

        Args:
            left: 나눌 대상 값.
            right: 나누는 값.

        Returns:
            `left / right` 계산 결과.

        Raises:
            ZeroDivisionError: `right`가 0일 때.
        """

        if right == 0:
            raise ZeroDivisionError("0으로 나눌 수 없습니다.")

        return float(self._record("divide", left, right, left / right))

    def clear_history(self) -> None:
        """현재 계산 기록을 모두 삭제한다."""

        self.history.clear()

    def save_history(self, file_path: str | Path) -> None:
        """계산 기록을 JSON 파일로 저장한다.

        Args:
            file_path: 계산 기록을 저장할 JSON 파일 경로.

        Raises:
            OSError: 파일을 쓰는 중 운영체제 수준의 오류가 발생할 때.
        """

        path = Path(file_path)
        records = [asdict(record) for record in self.history]
        path.write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")

    def load_history(self, file_path: str | Path) -> None:
        """JSON 파일에서 계산 기록을 불러와 현재 기록을 교체한다.

        Args:
            file_path: `save_history()`로 저장한 JSON 파일 경로.

        Raises:
            FileNotFoundError: 지정한 파일이 없을 때.
            json.JSONDecodeError: 파일 내용이 올바른 JSON이 아닐 때.
            ValueError: JSON 구조가 계산 기록 목록 형식이 아닐 때.
        """

        path = Path(file_path)
        raw_records = json.loads(path.read_text(encoding="utf-8"))

        if not isinstance(raw_records, list):
            raise ValueError("계산 기록 파일은 목록 형식이어야 합니다.")

        self.history = [self._record_from_json(record) for record in raw_records]

    def _record(self, operation: str, left: Number, right: Number, result: Number) -> Number:
        """계산 결과를 기록으로 추가하고 결과값을 그대로 반환한다."""

        self.history.append(CalculationRecord(operation, left, right, result))
        return result

    @staticmethod
    def _record_from_json(record: Any) -> CalculationRecord:
        """JSON 객체 하나를 계산 기록 객체로 변환한다."""

        if not isinstance(record, dict):
            raise ValueError("계산 기록 항목은 객체 형식이어야 합니다.")

        required_keys = {"operation", "left", "right", "result"}
        missing_keys = required_keys.difference(record)
        if missing_keys:
            missing = ", ".join(sorted(missing_keys))
            raise ValueError(f"계산 기록 항목에 필수 키가 없습니다: {missing}")

        return CalculationRecord(
            operation=record["operation"],
            left=record["left"],
            right=record["right"],
            result=record["result"],
        )
