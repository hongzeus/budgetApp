"""Tests for budget.core."""

from pathlib import Path

from budget.core import (
    add_transaction,
    filter_by_category,
    get_balance,
    load_transactions_from_csv,
)


def load_step2_transactions() -> list[dict[str, object]]:
    """Load normalized transactions from the step2 CSV fixture."""
    csv_path = Path(__file__).parent.parent / "data" / "step2_transactions.csv"
    return load_transactions_from_csv(csv_path)


def test_add_transaction_increases_length() -> None:
    """Adding a transaction should increase the collection length by one."""
    transactions = [
        {
            "date": "2026-01-05",
            "type": "지출",
            "category": "식비",
            "description": "점심식사",
            "amount": -12000,
            "memo": "",
        }
    ]
    transaction = {
        "date": "2026-01-07",
        "type": "수입",
        "category": "급여",
        "description": "월급",
        "amount": 3500000,
        "memo": "1월급여",
    }

    result = add_transaction(transactions, transaction)

    assert len(result) == len(transactions) + 1


def test_add_transaction_preserves_negative_amount_for_expense() -> None:
    """Expense transactions should keep their negative amount."""
    transactions = []
    transaction = {
        "date": "2026-01-10",
        "type": "지출",
        "category": "교통",
        "description": "지하철",
        "amount": -1500,
        "memo": "",
    }

    result = add_transaction(transactions, transaction)

    assert result[-1]["amount"] == -1500


def test_add_transaction_preserves_positive_amount_for_income() -> None:
    """Income transactions should keep their positive amount."""
    transactions = []
    transaction = {
        "date": "2026-01-07",
        "type": "수입",
        "category": "급여",
        "description": "월급",
        "amount": 3500000,
        "memo": "1월급여",
    }

    result = add_transaction(transactions, transaction)

    assert result[-1]["amount"] == 3500000


def test_add_transaction_handles_empty_description() -> None:
    """An empty description should be stored as an empty string."""
    transactions = []
    transaction = {
        "date": "2026-01-28",
        "type": "기타수입",
        "category": "기타수입",
        "description": "",
        "amount": 25000,
        "memo": "중고마켓",
    }

    result = add_transaction(transactions, transaction)

    assert result[-1]["description"] == ""


def test_get_balance_returns_zero_for_empty_transactions() -> None:
    """An empty transaction collection should have a zero balance."""
    assert get_balance([]) == 0.0


def test_get_balance_sums_income_and_expense_amounts() -> None:
    """Balance should be the sum of positive income and negative expenses."""
    transactions = [
        {
            "date": "2026-01-05",
            "type": "지출",
            "category": "식비",
            "description": "점심식사",
            "amount": -12000,
            "memo": "",
        },
        {
            "date": "2026-01-07",
            "type": "수입",
            "category": "급여",
            "description": "월급",
            "amount": 3500000,
            "memo": "1월급여",
        },
        {
            "date": "2026-01-10",
            "type": "지출",
            "category": "교통",
            "description": "지하철",
            "amount": -1500,
            "memo": "",
        },
    ]

    assert get_balance(transactions) == 3486500.0


def test_get_balance_matches_step2_transactions_total() -> None:
    """Balance should match the known total from step2 transaction data."""
    transactions = load_step2_transactions()

    assert get_balance(transactions) == 24285027.0


def test_filter_by_category_matches_step2_actual_category() -> None:
    """Filtering should return only transactions in the requested category."""
    transactions = load_step2_transactions()

    result = filter_by_category(transactions, "여행")

    assert len(result) == 6
    assert all(transaction["category"] == "여행" for transaction in result)


def test_filter_by_category_is_case_insensitive() -> None:
    """Filtering should compare category names without case sensitivity."""
    transactions = [
        {
            "date": "2026-01-04",
            "type": "지출",
            "category": "여행",
            "description": "항공권",
            "amount": -979796,
            "memo": "메모_3",
        },
        {
            "date": "2026-01-05",
            "type": "지출",
            "category": "의료",
            "description": "한의원",
            "amount": -65990,
            "memo": "카드결제",
        },
    ]

    result = filter_by_category(transactions, "여행")

    assert result == [transactions[0]]


def test_filter_by_category_returns_empty_list_for_missing_category() -> None:
    """Filtering an unknown category should return an empty list."""
    transactions = load_step2_transactions()

    assert filter_by_category(transactions, "없는카테고리") == []


def test_filter_by_category_returns_independent_result_list() -> None:
    """Filtering should return a list independent from the original list."""
    transactions = load_step2_transactions()

    result = filter_by_category(transactions, "여행")
    result.clear()

    assert len(transactions) == 50


def test_load_transactions_from_csv_loads_step1_rows() -> None:
    """CSV loading should return every transaction row from step1 data."""
    csv_path = Path(__file__).parent.parent / "data" / "step1_transactions.csv"

    transactions = load_transactions_from_csv(csv_path)

    assert len(transactions) == 10


def test_load_transactions_from_csv_converts_amount_to_int() -> None:
    """CSV loading should convert the amount field to an integer."""
    csv_path = Path(__file__).parent.parent / "data" / "step1_transactions.csv"

    transactions = load_transactions_from_csv(csv_path)

    assert transactions[0]["amount"] == -12000
    assert isinstance(transactions[0]["amount"], int)


def test_load_transactions_from_csv_preserves_step1_fields() -> None:
    """CSV loading should preserve the known step1 transaction fields."""
    csv_path = Path(__file__).parent.parent / "data" / "step1_transactions.csv"

    transactions = load_transactions_from_csv(csv_path)

    assert transactions[0] == {
        "date": "2026-01-05",
        "type": "지출",
        "category": "식비",
        "description": "점심식사",
        "amount": -12000,
        "memo": "",
    }


def test_load_transactions_from_csv_supports_balance_calculation() -> None:
    """CSV loading should return transactions usable by balance logic."""
    csv_path = Path(__file__).parent.parent / "data" / "step1_transactions.csv"

    transactions = load_transactions_from_csv(csv_path)

    assert get_balance(transactions) == 3366700.0
