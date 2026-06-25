"""Tests for budget.core."""

from budget.core import add_transaction


def test_add_transaction_increases_length() -> None:
    """Adding a transaction should increase the collection length by one."""
    transactions = []
    transaction = {"date": "2026-06-25", "amount": 10000, "category": "food"}

    result = add_transaction(transactions, transaction)

    assert len(result) == 1

