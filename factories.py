from random import randint
from factory import Factory, Faker, fuzzy

from player import Player, Behavior
from property import Property, SALE_BOUNDARIES, RENTAL_BOUNDARIES


class PlayerFactory(Factory):
    class Meta:
        model = Player

    name = Faker('name')
    behavior = fuzzy.FuzzyChoice(Behavior)


class PropertyFactory(Factory):
    class Meta:
        model = Property

    sale_price = fuzzy.FuzzyAttribute(lambda: randint(*SALE_BOUNDARIES))
    rental_price = fuzzy.FuzzyAttribute(lambda: randint(*RENTAL_BOUNDARIES))
