from random import randint

def check_value_in_boundary(value, min_, max_):
    if min_ <= value <= max_:
        return True
    return False


class Dice(object):
    def __init__(self, sides):
        self.min = 1
        self.max = sides

    def roll(self):
        return randint(self.min, self.max)
