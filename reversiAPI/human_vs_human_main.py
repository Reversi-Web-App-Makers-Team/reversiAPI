import os
print(os.getcwd())
import sys
import pprint
pprint.pprint(sys.path)

from reversiAPI.players.player_human import PlayerHuman
from reversiAPI.utils.reversi_processor import ReversiProcessor

def _human_vs_human(white, black):
    player_white_name = input("player1の名前は?:")
    player_black_name = input("player2の名前は?:")
    player_white_class = PlayerHuman(white, player_white_name)
    player_black_class = PlayerHuman(black, player_black_name)
    game = ReversiProcessor(
            player_white_class = player_white_class,
            player_black_class = player_black_class,
            options = None,
            play_game_num = 1,
            display_board = True,
            display_result = True
            )
    game.progress()

def _main():
    _human_vs_human(1, -1)

if __name__ == '__main__':
    _main()