from random import randint, choice
from factory import Factory, Faker, fuzzy, SubFactory, List

from player import (
    Player,
    ImpulsivePlayer,
    DemandingPlayer,
    CautiousPlayer,
    RandomPlayer,
)
from property import Property, SALE_BOUNDARIES, RENTAL_BOUNDARIES

from monopoly import Monopoly


class PlayerFactory(Factory):
    class Meta:
        model = Player


class ImpulsivePlayerFactory(Factory):
    class Meta:
        model = ImpulsivePlayer


class DemandingPlayerFactory(Factory):
    class Meta:
        model = DemandingPlayer


class CautiousPlayerFactory(Factory):
    class Meta:
        model = CautiousPlayer


class RandomPlayerFactory(Factory):
    class Meta:
        model = RandomPlayer


class PropertyFactory(Factory):
    class Meta:
        model = Property

    sale_price = fuzzy.FuzzyAttribute(lambda: randint(*SALE_BOUNDARIES))
    rental_price = fuzzy.FuzzyAttribute(lambda: randint(*RENTAL_BOUNDARIES))
    owner = SubFactory(PlayerFactory)

player_subfactories_list = [
    ImpulsivePlayerFactory,
    RandomPlayerFactory,
    DemandingPlayerFactory,
    CautiousPlayerFactory
]

class MonopolyFactory(Factory):
    class Meta:
        model = Monopoly

    players = List([
        SubFactory(
            choice(player_subfactories_list)
        ) for _ in range(4)
    ])
    board = [
        PropertyFactory() for _ in range(20)
    ]
