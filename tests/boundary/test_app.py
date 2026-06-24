import pytest

from src.cart import subtotal


@pytest.mark.boundary
def test_e_1_subtotal_none_raises_type_error():
    """E-1: items is None → TypeError."""
    with pytest.raises(TypeError):
        subtotal(None)


@pytest.mark.boundary
@pytest.mark.parametrize(
    "items, expected_index",
    [
        ([{"price": -100, "qty": 1}], 0),
        ([{"price": 100, "qty": -1}], 0),
    ],
)
def test_e_2_negative_price_or_qty_raises_value_error_with_index(items, expected_index):
    """E-2: 음수 price/qty → ValueError(인덱스 포함)."""
    with pytest.raises(ValueError) as exc_info:
        subtotal(items)
    assert str(expected_index) in str(exc_info.value)
