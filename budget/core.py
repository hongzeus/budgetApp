"""Core business logic for the budget CLI app."""

from __future__ import annotations

from typing import Any

Transaction = dict[str, Any]


def add_transaction(
    transactions: list[Transaction],
    transaction: Transaction,
) -> list[Transaction]:
    """Add a transaction and return the updated transactions."""
    updated_transactions = transactions.copy()
    updated_transactions.append(transaction)
    return updated_transactions


def get_balance(transactions: list[Transaction]) -> float:
    """Return the balance by summing income and expense amounts."""
    return float(sum(transaction["amount"] for transaction in transactions))


def filter_by_category(
    transactions: list[Transaction],
    category: str,
) -> list[Transaction]:
    """Return transactions that match the category without case sensitivity."""
    target_category = category.casefold()
    return [
        transaction
        for transaction in transactions
        if str(transaction["category"]).casefold() == target_category
    ]
