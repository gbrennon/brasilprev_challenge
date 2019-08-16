from factory import Factory, Faker, fuzzy

from player import Player, Behavior


class PlayerFactory(Factory):
    class Meta:
        model = Player

    name = Faker('name')
    behavior = fuzzy.FuzzyChoice(Behavior)
