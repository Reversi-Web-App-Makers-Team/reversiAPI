import random
import toml
import numpy as np
from reversiAPI.utils.reversi_packages import ReversiPackages


class ReversiProcessor(object):
    '''
    This class processes reversi game.
    '''

    def __init__(
            self,
            player_white_class,
            player_black_class,
            options=None,
            play_game_num=1,
            display_board=True,
            display_result=True,
            stat=1000000
    ):
        self.__player_white = player_white_class
        self.__player_black = player_black_class
        if options == None:
            self.__options = toml.load('reversiAPI/utils/settings.toml')['REVERSI_PROCESSOR']
        else:
            self.__options = options
        self.__play_game_num = play_game_num
        self.__display_board = display_board
        self.__display_result = display_result
        self.__stat = stat
        self.__win_num_cnt = {
            player_white_class.myturn: 0,
            player_black_class.myturn: 0,
            draw: 0
        }
        self.__player_list = [
            self.__player_white,
            self.__player_black
        ]
        self.__whose_turn = self.__player_list[random.randrange(2)]
        self.__finished_game_num = 0

    def progress(self):
        while self.__finished_game_num < self.__play_game_num:
            self.__board = ReversiPackages()
            self.__board.display_board()

            while self.board.winner == None:
                if self.disp:
                    print(self.player_turn.name + "の番やで〜")
                    p_pos = self.board.get_possible_pos(self.player_turn.myturn)
                    plus_1 = [1 for i in range(len(p_pos))]
                    print(str(np.array(p_pos) + np.array(plus_1)) + "に置けるで")
                act = self.player_turn.act(self.board)

    # TODO -> iyori: implement here.
    def switch_player(self):
        if self.player_turn == self.__player_white:
            if not self.board.get_possible_pos(self.__options['BLACK']):
                self.player_turn = self.player_b
            elif self.board.get_possible_pos(self.__options['BLACK']):
                self.player_turn = self.player_w
                if self.board.get_possible_pos(self.__options['WHITE']):
                    self.board.check_winner()
        else:
            if not self.board.get_possible_pos(self.__options['WHITE']):
                self.player_turn = self.player_w
            elif self.board.get_possible_pos(self.__options['WHITE']):
                self.player_turn = self.player_b
                if self.board.get_possible_pos(self.__options['BLACK']):
                    self.board.check_winner()
