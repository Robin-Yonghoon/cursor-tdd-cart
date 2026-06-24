import pytest

from src.cart import subtotal


@pytest.mark.entity
def test_inv_1_subtotal_equals_sum_of_price_times_qty():
    """INV-1: subtotal == Σ(price × qty)."""
    items = [{"price": 1000, "qty": 3}, {"price": 2000, "qty": 2}]
    assert subtotal(items) == 7000
