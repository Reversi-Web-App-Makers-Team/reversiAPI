# for checking dqn's strength
import os
import sys


from reversiAPI.players.random import PlayerRandom
from reversiAPI.utils.reversi_processor import ReversiProcessor
from reversiAPI.utils.settings import DQN
# from reversiAPI.players.dqn1 import PlayerDqn1
from reversiAPI.players.dqn2 import PlayerDqn2


def _dqn_vs_random(file_path):
    # if dqn is white
    player_white_instance = PlayerDqn(1, file_path, False)
    player_black_instance = PlayerRandom(-1, False)
    game = ReversiProcessor(
        player_white_instance=player_white_instance,
        player_black_instance=player_black_instance,
        options=None,
        play_game_num=10000,
        display_board=False,
        display_result=True
    )
    game.progress()

    # if dqn is black
    player_white_instance = PlayerRandom(1, False)
    player_black_instance = PlayerDqn(-1, file_path, False)
    game = ReversiProcessor(
        player_white_instance=player_white_instance,
        player_black_instance=player_black_instance,
        options=None,
        play_game_num=10000,
        display_board=False,
        display_result=True
    )
    game.progress()


def _main(file_path):
    _dqn_vs_random(file_path)


if __name__ == '__main__':
    executing_file_path = os.path.dirname(os.path.abspath(__file__))
    # model_path = DQN['dqn1']
    model_path = DQN['dqn2']
    path = os.path.join(executing_file_path, model_path)
    _main(path)
