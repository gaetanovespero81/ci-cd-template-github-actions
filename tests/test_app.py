"""
Module containing tests for app.py.
"""

from src.app import add


def test_add() -> None:
    """Check that the add() function returns the correct sum."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
