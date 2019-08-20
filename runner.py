from player import ImpulsivePlayer, DemandingPlayer, CautiousPlayer, RandomPlayer
from property import Property
from monopoly import Monopoly, Reason

from config import NUMBER_GAMES as n_games

import pprint

def run():
    winning_counter = {}
    winning_percentage = {}
    game_results = []

    for i in range(n_games):
        board = (
            Property(100, 30),
            Property(200, 50),
            Property(200, 50),
            Property(200, 60),
            Property(120, 5),
            Property(130, 10),
            Property(200, 55),
            Property(150, 30),
            Property(120, 5),
            Property(190, 30),
            Property(160, 10),
            Property(200, 55),
            Property(200, 10),
            Property(150, 5),
            Property(130, 10),
            Property(190, 5),
            Property(190, 2),
            Property(200, 55),
            Property(160, 4),
            Property(180, 5),
        )
        players = [
            ImpulsivePlayer(),
            DemandingPlayer(),
            CautiousPlayer(),
            RandomPlayer()
        ]
        m = Monopoly(players, board)
        game_results.append(m.loop())


    for g in game_results:
        winner_name = str(g['winner'])

        if winner_name in winning_counter:
            winning_counter[winner_name] += 1
        else:
            winning_counter[winner_name] = 1


    for player, wins in winning_counter.items():
        winning_percentage[player] = wins / len(game_results)

    total_rounds = sum(map(lambda g: g['round'], game_results))

    game_statistics = {
        'timeout_games': len(list(filter(
            lambda g: g['reason'] == Reason.TIMEOUT, game_results
        ))),
        'total_rounds': total_rounds,
        'average_game_duration': float(total_rounds / len(game_results)),
        'winning_percentage': winning_percentage,
        'most_wins': max(
            winning_percentage.items(),
            key=lambda x: x[1]
        )[0]
    }

    # print(game_results) for results
    return game_statistics


if __name__ == '__main__':
    pprint.pprint(run(), width=2)
