import pytest

from src.cart import apply_threshold_discount, subtotal


@pytest.mark.entity
def test_inv_1_subtotal_equals_sum_of_price_times_qty():
    """INV-1: subtotal == Σ(price × qty)."""
    items = [{"price": 1000, "qty": 3}, {"price": 2000, "qty": 2}]
    assert subtotal(items) == 7000


@pytest.mark.entity
@pytest.mark.parametrize(
    "amount, expected",
    [
        (50000, 45000),
        (49999, 49999),
    ],
)
def test_inv_2_apply_threshold_discount_boundary_inclusive(amount, expected):
    """INV-2: amount>=50000 → round(*0.9) / <50000 그대로 (경계 포함)."""
    assert apply_threshold_discount(amount) == expected
