from reversiAPI.players.randomkun import PlayerRandom
from reversiAPI.utils.reversi_processor import ReversiProcessor


def _random_vs_random(white, black):
    player_white_instance = PlayerRandom(white)
    player_black_instance = PlayerRandom(black)
    game = ReversiProcessor(
        player_white_instance=player_white_instance,
        player_black_instance=player_black_instance,
        options=None,
        play_game_num=5,
        display_board=True,
        display_result=True
    )
    game.progress()


def _main():
    _random_vs_random(1, -1)


if __name__ == '__main__':
    _main()
