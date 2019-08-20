from config import SALE_BOUNDARIES, RENTAL_BOUNDARIES

from utils import check_value_in_boundary



class Property:
    def __init__(self, sale_price=50, rental_price=2, owner=None):
        if not check_value_in_boundary(sale_price, *SALE_BOUNDARIES):
            raise ValueError('Sale price({}) must be between {} and {}'
                             .format(sale_price, *SALE_BOUNDARIES))
        if not check_value_in_boundary(rental_price, *RENTAL_BOUNDARIES):
            raise ValueError('Rent price({}) must be between {} and {}'
                             .format(rental_price, *RENTAL_BOUNDARIES))

        self.sale_price = sale_price # sale_price can go from 80 to 200
        self.rental_price = rental_price #rental_price can go from 10 to 100
        self.owner = owner
