from config import SALE_BOUNDARIES, RENTAL_BOUNDARIES

from utils import check_value_in_boundary


class Property(object):
    def __init__(self, sale_price=80, rental_price=10):
        if not check_value_in_boundary(sale_price, *SALE_BOUNDARIES):
            raise ValueError('Sale price({}) must be between {} and {}'.format(sale_price, *SALE_BOUNDARIES))
        if not check_value_in_boundary(rental_price, *RENTAL_BOUNDARIES):
            raise ValueError('Rent price({}) must be between {} and {}'.format(rental_price, *RENTAL_BOUNDARIES))

        self.sale_price = sale_price # sale_price can go from 80 to 200
        self.rental_price = rental_price #rental_price can go from 10 to 100
        self.owner = None