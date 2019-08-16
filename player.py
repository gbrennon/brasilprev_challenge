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

    def move(self, steps):
        # This should make the player move
        old_position = self.position
        self.position += steps

        if(self.position >= 20):
            self.position -= 20
            self.balance += 100
