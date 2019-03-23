from reversiAPI.players.player_human import PlayerHuman
from reversiAPI.players.dqnkun import PlayerDqn
from reversiAPI.utils.reversi_processor import ReversiProcessor


def _dqn_vs_human(white, black):
    player_human_name = input("playerの名前は?:")
    player_white_instance = PlayerHuman(player_human_name, white)
    player_black_instance = PlayerDqn(black)
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
    _random_vs_human(1, -1)


if __name__ == '__main__':
    _main()
