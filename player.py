from enum import Enum
import random

from config import ROUND_CASH


class Player:
    def __init__(self, balance=300):
        # self.name = name
        self.balance = balance
        self.position = 0
        self.properties = []

    def __str__(self):
        return self.__class__.__name__

    def move(self, steps):
        self.position += steps

        if self.position >= 20:
            self.position -= 20
            self.balance += ROUND_CASH

    def can_buy(self, property_):
        if(
                self.balance >= property_.sale_price and
                property_ not in self.properties and
                not property_.owner
        ):
            return True
        else:
            return False

    def buy(self, property_):
        # the game engine must ensure to call this after can_buy method
        self.balance -= property_.sale_price
        self.properties.append(property_)
        property_.owner = self


class ImpulsivePlayer(Player):
    def can_buy(self, property_):
        return super().can_buy(property_)


class DemandingPlayer(Player):
    def can_buy(self, property_):
        return (super().can_buy(property_) and property_.rental_price > 50)


class CautiousPlayer(Player):
    def can_buy(self, property_):
        value_after_buy = self.balance - property_.sale_price
        return (super().can_buy(property_) and value_after_buy >= 80)


class RandomPlayer(Player):
    def can_buy(self, property_):
        return (super().can_buy(property_) and random.randint(0, 1) == 1)
