import os

from reversiAPI.players.player_random import PlayerRandom
from reversiAPI.players.player_sl1 import PlayerSl1
from reversiAPI.utils.reversi_processor import ReversiProcessor
from reversiAPI.utils.settings import SL


def _dqn_vs_random(white, black, file_path):
    player_white_instance = PlayerSl1(white, file_path, False)
    player_black_instance = PlayerRandom(black, False)
    game = ReversiProcessor(
        player_white_instance=player_white_instance,
        player_black_instance=player_black_instance,
        options=None,
        play_game_num=1000,
        display_board=False,
        display_result=True
    )
    game.progress()


print('==' + os.getcwd())

def _main(file_path):
    _dqn_vs_random(1, -1, file_path)


if __name__ == '__main__':
    executing_file_path = os.path.dirname(os.path.abspath(__file__))
    pt_path = SL['sl1']
    path = os.path.join(executing_file_path, pt_path)
    _main(path)
