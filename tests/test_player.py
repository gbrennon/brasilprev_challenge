import unittest

from factories import PlayerFactory

class PlayerTestCases(unittest.TestCase):
    def setUp(self):
        self.player = PlayerFactory()

    def test_player_is_moving(self):
        steps_to_move = 6

        self.player.move(steps_to_move)

        self.assertEqual(self.player.position, steps_to_move)

    def test_player_passed_20th_house(self):
        # the player should be cycling the board, so if he reaches the 20th
        # house he should return to 0 and continue his moves
        # also he should receive +100 of cash in his balance
        self.player.position = 16
        steps_to_move = 6

        future_position = self.player.position + steps_to_move - 20
        future_balance = self.player.balance + 100

        self.player.move(steps_to_move)

        self.assertEqual(self.player.position, future_position)
        self.assertEqual(self.player.balance, future_balance)
