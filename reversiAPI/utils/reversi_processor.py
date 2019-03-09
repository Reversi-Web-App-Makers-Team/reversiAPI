import random

import numpy as np
import toml

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

        '''
        initialize function
        Args:
            player_white_class(Class), player_black_class(Class):
                instruction: each color (black or white) player's class.
                             player class must two class variables and one method.
                                class variables:
                                    self.name(str):
                                        player's name

                                    self.stone_color(int):
                                        white -> 1
                                        black -> -1

                                class method:
                                    self.put_stone(self, board):
                                        Args:
                                            board(list):
                                                shape = (64, 1)
                                                instruction: game board infomation

            options(toml):
                global variables

            play_game_num(int):
                how many times playint reversi game

            display_board(boolean):
                True -> displaying board
                False -> not displaying board

            display_result(boolean):
                True -> displaying result of game when finished
                Flase -> not displaying result of game

            stat(int):
                TODO -> teramoto: implement here.
        '''

        # player class

        self.__player_white = player_white_class
        self.__player_black = player_black_class

        # global variables
        if options == None:
            self.__options = toml.load('reversiAPI/utils/settings.toml')['REVERSI_PROCESSOR']
        else:
            self.__options = options

        # how many times playing game
        self.__play_game_num = play_game_num

        # display or not board and result
        self.__display_board = display_board
        self.__display_result = display_result

        # stat TODO-> teramoto: implement here
        self.__stat = stat

        # board info (size==64)
        self.__board = None

        # win number counter (dictionary)
        self.__win_num_cnt = {
            player_white_class.stone_color: 0,
            player_black_class.stone_color: 0,
            draw: 0
        }

        # players' list
        self.__player_list = [
            self.__player_white,
            self.__player_black
        ]

        # who puts stone next
        #   1 -> player_white
        #   -1 -> player_black
        self.__whose_turn = self.__player_list[random.randrange(2)]

        # how many games are already played
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
