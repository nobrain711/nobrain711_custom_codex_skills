"""계산기 예제 모듈의 정상 동작과 실패 경로를 검증하는 테스트 모듈.

이 모듈은 `Calculator`의 사칙연산 기록, JSON 저장/불러오기, 기록 초기화,
0 나눗셈과 잘못된 기록 파일 처리처럼 호출자가 의존하는 공개 동작을 검증한다.
파일 시스템 검증은 pytest의 임시 경로를 사용해 로컬 작업 파일을 오염시키지 않는다.
"""

import json

import pytest

from src.calculator import CalculationRecord, Calculator


def test_basic_operations_record_successful_results() -> None:
    calculator = Calculator()

    assert calculator.add(2, 3) == 5
    assert calculator.subtract(10, 4) == 6
    assert calculator.multiply(3, 4) == 12
    assert calculator.divide(10, 2) == 5.0

    assert calculator.history == [
        CalculationRecord("add", 2, 3, 5),
        CalculationRecord("subtract", 10, 4, 6),
        CalculationRecord("multiply", 3, 4, 12),
        CalculationRecord("divide", 10, 2, 5.0),
    ]


def test_save_and_load_history_successfully_round_trips_records(tmp_path) -> None:
    history_path = tmp_path / "history.json"
    calculator = Calculator()
    calculator.add(7, 8)
    calculator.divide(9, 3)

    calculator.save_history(history_path)

    restored = Calculator()
    restored.load_history(history_path)

    assert restored.history == [
        CalculationRecord("add", 7, 8, 15),
        CalculationRecord("divide", 9, 3, 3.0),
    ]


def test_clear_history_removes_existing_records() -> None:
    calculator = Calculator()
    calculator.add(1, 2)

    calculator.clear_history()

    assert calculator.history == []


def test_divide_rejects_zero_and_does_not_record_failed_operation() -> None:
    calculator = Calculator()

    with pytest.raises(ZeroDivisionError, match="0으로 나눌 수 없습니다"):
        calculator.divide(10, 0)

    assert calculator.history == []


def test_load_history_rejects_non_list_json(tmp_path) -> None:
    history_path = tmp_path / "history.json"
    history_path.write_text(json.dumps({"operation": "add"}), encoding="utf-8")
    calculator = Calculator()

    with pytest.raises(ValueError, match="목록 형식"):
        calculator.load_history(history_path)


def test_load_history_rejects_non_object_record(tmp_path) -> None:
    history_path = tmp_path / "history.json"
    history_path.write_text(json.dumps(["not-a-record"]), encoding="utf-8")
    calculator = Calculator()

    with pytest.raises(ValueError, match="객체 형식"):
        calculator.load_history(history_path)


def test_load_history_rejects_record_with_missing_required_key(tmp_path) -> None:
    history_path = tmp_path / "history.json"
    history_path.write_text(
        json.dumps([{"operation": "add", "left": 1, "right": 2}]),
        encoding="utf-8",
    )
    calculator = Calculator()

    with pytest.raises(ValueError, match="필수 키"):
        calculator.load_history(history_path)
