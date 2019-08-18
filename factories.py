from random import randint
from factory import Factory, Faker, fuzzy, SubFactory

from player import (
    Player,
    ImpulsivePlayer,
    DemandingPlayer,
    CautiousPlayer,
    RandomPlayer,
)
from property import Property, SALE_BOUNDARIES, RENTAL_BOUNDARIES


class PlayerFactory(Factory):
    class Meta:
        model = Player

    name = Faker('name')


class ImpulsivePlayerFactory(Factory):
    class Meta:
        model = ImpulsivePlayer

    name = Faker('name')


class DemandingPlayerFactory(Factory):
    class Meta:
        model = DemandingPlayer

    name = Faker('name')


class CautiousPlayerFactory(Factory):
    class Meta:
        model = CautiousPlayer

    name = Faker('name')


class RandomPlayerFactory(Factory):
    class Meta:
        model = RandomPlayer

    name = Faker('name')


class PropertyFactory(Factory):
    class Meta:
        model = Property

    sale_price = fuzzy.FuzzyAttribute(lambda: randint(*SALE_BOUNDARIES))
    rental_price = fuzzy.FuzzyAttribute(lambda: randint(*RENTAL_BOUNDARIES))
    owner = SubFactory(PlayerFactory)
