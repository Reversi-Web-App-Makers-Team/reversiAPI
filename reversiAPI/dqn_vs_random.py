import os

from reversiAPI.players.dqnkun import PlayerDqn
from reversiAPI.players.randomkun import PlayerRandom
from reversiAPI.utils.reversi_processor import ReversiProcessor
from reversiAPI.utils.settings import DQN


def _dqn_vs_random(white, black, file_path):
    player_white_instance = PlayerRandom(white, False)
    player_black_instance = PlayerDqn(black, file_path, False)
    game = ReversiProcessor(
        player_white_instance=player_white_instance,
        player_black_instance=player_black_instance,
        options=None,
        play_game_num=100,
        display_board=False,
        display_result=True
    )
    game.progress()


def _main(file_path):
    _dqn_vs_random(1, -1, file_path)


if __name__ == '__main__':
    executing_file_path = os.path.dirname(os.path.abspath(__file__))
    pt_path = DQN['pt_path']
    path = os.path.join(executing_file_path, pt_path)
    _main(path)
