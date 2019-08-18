import unittest

from factories import PropertyFactory, SALE_BOUNDARIES, RENTAL_BOUNDARIES

class PropertyTestCases(unittest.TestCase):
    def test_property_sale_price_in_boundaries(self):
        try:
            PropertyFactory(sale_price=SALE_BOUNDARIES[1])
        except ValueError:
            self.fail('Property sale_price raised ValueError unexpectedly!')

    def test_property_rental_price_in_boundaries(self):
        try:
            PropertyFactory(rental_price=RENTAL_BOUNDARIES[1])
        except ValueError:
            self.fail('Property rental_price raised ValueError unexpectedly!')

    def test_property_sale_price_out_of_boundaries(self):
        with self.assertRaises(ValueError):
            PropertyFactory(sale_price=SALE_BOUNDARIES[1]+1)

    def test_property_rental_price_not_in_boundary(self):
        with self.assertRaises(ValueError):
            PropertyFactory(rental_price=RENTAL_BOUNDARIES[1]+1)
