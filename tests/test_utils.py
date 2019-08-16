import unittest

from utils import check_value_in_boundary, Dice


class UtilsTestCase(unittest.TestCase):
    def test_value_is_in_boundary(self):
        value = 5
        min_ = 0
        max_ = 10

        result = check_value_in_boundary(value, min_, max_)
        self.assertTrue(result)

    def test_value_not_in_boundary(self):
        value = 100
        min_ = 0
        max_ = 10

        result = check_value_in_boundary(value, min_, max_)
        self.assertFalse(result)

    def test_dice_roll_is_between_min_and_max(self):
        min_ = 1
        max_ = 6

        dice = Dice(max_)
        result = dice.roll()

        self.assertTrue(min_ <= result  <= max_)
