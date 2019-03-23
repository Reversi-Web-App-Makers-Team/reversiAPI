# from reversiAPI.players.player_human import PlayerHuman
# from reversiAPI.utils.reversi_processor import ReversiProcessor
from players.player_human import PlayerHuman
from utils.reversi_processor import ReversiProcessor


def _human_vs_human(white, black):
    player_white_name = input("player1の名前は?:")
    player_black_name = input("player2の名前は?:")
    player_white_instance = PlayerHuman(player_white_name, white)
    player_black_instance = PlayerHuman(player_black_name, black)
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
    _human_vs_human(1, -1)


if __name__ == '__main__':
    _main()
