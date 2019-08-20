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
        print('Eliminating player {} with balance {}'.format(
            player,
            player.balance
        ))

        self.eliminated_players.append(player)
        self.players.pop(index)

    def concede_victory(self, winner, reason):
        #print('Conceding victory to {}'.format(winner))
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
            print('Starting round {}'.format(self.round))
            #print('Players {} still in the game'.format([p for p in self.players]))

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

                ###at the end of the players loop
                for _p in self.players:
                    print('Player {} balance {}'.format(_p, _p.balance))

                if p.balance < 0:
                    print(p.balance)
                    self.eliminate_player(index, p)

            print('End of round {}'.format(self.round))

        return self.concede_victory(self.players[0], Reason.SURVIVOR)
