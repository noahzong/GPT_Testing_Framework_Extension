from functions.branch11 import branch11
import pytest

@pytest.mark.parametrize('base_price, is_discounted, has_shipping, shipping_location, expected_total_cost',
                         [
                             (100, False, False, None, 110.0),
                             (100, True, False, None, 88.0),
                             (100, False, True, "domestic", 115.0),
                             (100, False, True, "international", 125.0)
                         ])
def test_branch11_total_cost(base_price, is_discounted, has_shipping, shipping_location, expected_total_cost):
    total_cost = branch11(base_price, is_discounted, has_shipping, shipping_location)
    assert total_cost == expected_total_cost