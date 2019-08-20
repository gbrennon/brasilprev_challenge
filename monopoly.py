from utils import Dice
from enum import Enum

from config import ROUND_TIMEOUT


class Reason(Enum):
    TIMEOUT = 0
    SURVIVOR = 1


class Monopoly:
    def __init__(self, players=None, board=[]):
        self.round = 0
        self.players = players
        self.eliminated_players = []
        self.board = board
        self.dice = Dice()

    def eliminate_player(self, index, player):
        self.eliminated_players.append(player)
        self.players.pop(index)

    def concede_victory(self, winner, reason):
        game_result = {
            'winner': winner,
            'reason': reason,
            'round': self.round,
            'players': self.players
        }
        return game_result

    def loop(self):
        self.round = 0
        while len(self.players) > 1:
            self.round += 1

            if self.round == ROUND_TIMEOUT:
                winner = max(
                    self.players,
                    key=lambda p: p.balance
                )
                return self.concede_victory(winner, Reason.TIMEOUT)

            for index, p in enumerate(self.players):
                movement = self.dice.roll()

                p.move(movement)

                property_ = self.board[p.position]
                owner = property_.owner

                if owner and owner is not p:
                    p.balance -= property_.rental_price
                    owner.balance += property_.rental_price

                if p.can_buy(property_):
                    p.buy(property_)


                if p.balance < 0:
                    self.eliminate_player(index, p)

        return self.concede_victory(self.players[0], Reason.SURVIVOR)
