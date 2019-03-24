from reversiAPI.players.dqnkun import PlayerDqn
from reversiAPI.players.randomkun import PlayerRandom
from reversiAPI.utils.reversi_processor import ReversiProcessor


def _dqn_vs_random(white, black, file_path):
    player_white_instance = PlayerRandom(white)
    player_black_instance = PlayerDqn(black, file_path)
    game = ReversiProcessor(
        player_white_instance=player_white_instance,
        player_black_instance=player_black_instance,
        options=None,
        play_game_num=100,
        display_board=True,
        display_result=True
    )
    game.progress()


def _main(file_path):
    _dqn_vs_random(1, -1, file_path)


if __name__ == '__main__':
    _main('/Users/hiroya/s1-9/Reversi/reversiAPI/reversiAPI/players/models/model1/model1.pt')
