# for debugging
from reversiAPI.players.randomkun import PlayerRandom
from reversiAPI.utils.reversi_processor import ReversiProcessor


def _random_vs_random(n_times):
    player_white_instance = PlayerRandom(1)
    player_black_instance = PlayerRandom(-1)
    game = ReversiProcessor(
        player_white_instance=player_white_instance,
        player_black_instance=player_black_instance,
        options=None,
        play_game_num=n_times,
        display_board=True,
        display_result=True
    )
    game.progress()


def _main():
    _random_vs_random(100)


if __name__ == '__main__':
    _main()
