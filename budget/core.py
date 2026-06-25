"""Core business logic for the budget CLI app."""

from __future__ import annotations

from typing import Any

Transaction = dict[str, Any]


def add_transaction(transactions: list[Transaction], transaction: Transaction) -> list[Transaction]:
    """Add a transaction to the collection and return the updated transactions."""
    updated_transactions = transactions.copy()
    updated_transactions.append(transaction)
    return updated_transactions
