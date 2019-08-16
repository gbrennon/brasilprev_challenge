from enum import Enum


class Behavior(Enum):
    IMPULSIVE = 0
    DEMANDING = 1
    CAUTIOUS = 2
    RANDOM = 3


class Player(object):
    def __init__(self, name, behavior=Behavior.IMPULSIVE, balance=300):
        self.name = name
        self.behavior = behavior
        self.balance = balance
        self.position = 0
        self.properties = []

    def move(self, steps):
        # This should make the player move
        old_position = self.position
        self.position += steps

        if(self.position >= 20):
            self.position -= 20
            self.balance += 100

    def can_buy(self, property_):
        if (
            self.balance >= property_.sale_price and
            property_ not in self.properties and
            property_.owner
        ):
            return True
        return False

    def buy(self, property_):
        # the game engine must ensure to call this after can_buy method
        self.balance -= property_.sale_price
        self.properties.append(property_)
        property_.owner = self

        return self.balance
