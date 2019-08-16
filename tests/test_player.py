import unittest

from factories import PlayerFactory, PropertyFactory

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

    def test_player_can_buy(self):
        property_ = PropertyFactory()
        price = property_.sale_price
        self.player.balance = price

        self.assertTrue(self.player.can_buy(property_))

    def test_player_cant_buy_because_of_money(self):
        property_ = PropertyFactory()
        price = property_.sale_price
        self.player.balance = price - 1

        self.assertFalse(self.player.can_buy(property_))

    def test_player_cant_buy_because_is_owner(self):
        property_ = PropertyFactory(owner=self.player)
        self.player.properties.append(property_)

        price = property_.sale_price
        self.player.balance = price

        self.assertFalse(self.player.can_buy(property_))

    def test_player_cant_buy_someone_else_is_owner(self):
        property_ = PropertyFactory(owner=PlayerFactory())
        self.player.properties.append(property_)

        price = property_.sale_price
        self.player.balance = price

        self.assertFalse(self.player.can_buy(property_))

    def test_player_bought_property(self):
        property_ = PropertyFactory()
        self.player.balance = property_.sale_price
        future_balance = self.player.balance - property_.sale_price

        result = self.player.buy(property_)

        self.assertEqual(self.player.balance, future_balance)
        self.assertIn(property_, self.player.properties)
        self.assertEqual(self.player, property_.owner)
        self.assertEqual(self.player.balance, result)
