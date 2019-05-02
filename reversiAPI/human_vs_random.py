import random

from reversiAPI.players.player_human import PlayerHuman
from reversiAPI.players.player_random import PlayerRandom
from reversiAPI.utils.reversi_processor import ReversiProcessor


def _human_vs_random():
    player_human_name = input("playerの名前は?:")

    player_color = random.choice([-1, 1])
    if player_color == 1:
        player_white_instance = PlayerHuman(player_human_name, player_color)
        player_black_instance = PlayerRandom(-1 * player_color, display=True)
    else:
        player_white_instance = PlayerRandom(-1 * player_color, display=True)
        player_black_instance = PlayerHuman(player_human_name, player_color)

    game = ReversiProcessor(
        player_white_instance=player_white_instance,
        player_black_instance=player_black_instance,
        options=None,
        play_game_num=1,
        display_board=True,
        display_result=True
    )
    game.progress()


def _main():
    _human_vs_random()


if __name__ == '__main__':
    _main()
