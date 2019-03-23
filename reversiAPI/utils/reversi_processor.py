import random

import numpy as np

from reversiAPI.utils.reversi_packages import ReversiPackages
from reversiAPI.utils.settings import REVERSI_PROCESSOR


class ReversiProcessor(object):
    '''
    This class processes reversi game.
    '''

    def __init__(
            self,
            player_white_instance,
            player_black_instance,
            options=None,
            play_game_num=1,
            display_board=True,
            display_result=True,

    ):

        '''
        initialize function
        Args:
            player_white_instance(Class), player_black_instance(Class):
                instruction: each color (black or white) player's class.
                             player class must have two class variables and one method.
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
                                                instruction: game board information

            options(dict):
                global variables

            play_game_num(int):
                how many times playint reversi game

            display_board(boolean):
                True -> displaying board
                False -> not displaying board

            display_result(boolean):
                True -> displaying result of game when finished
                Flase -> not displaying result of game
        '''

        # player class

        self.__player_white = player_white_instance
        self.__player_black = player_black_instance

        # global variables
        if options == None:
            self.__options = REVERSI_PROCESSOR
        else:
            self.__options = options

        self.__winner = None

        # how many times playing game
        self.__play_game_num = play_game_num

        # display or not board and result
        self.__display_board = display_board
        self.__display_result = display_result

        # class ReversiPackages
        self.__reversi_packages = None

        # win number counter (dictionary)
        self.__win_num_cnt = {
            player_white_instance.stone_color: 0,
            player_black_instance.stone_color: 0,
            self.__options['DRAW']: 0
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
        """
        Progress reversi game
        """
        while self.__finished_game_num < self.__play_game_num:
            self.__winner = None
            self.__reversi_packages = ReversiPackages(
                board=None,
                options=None,
                display_board=self.__display_board
            )

            self.__reversi_packages.display_board()

            # while the __winner is not defined, progress the game
            while self.__winner == None:
                if self.__display_board:
                    # print(self.__whose_turn.name, "の番やで〜")

                    p_pos = self.__reversi_packages.get_stone_putable_pos(self.__whose_turn.stone_color)
                    plus_1 = [1 for i in range(len(p_pos))]
                    print(str(np.array(p_pos) + np.array(plus_1)), "に置けるで")
                act = self.__whose_turn.put_stone(self.__reversi_packages)
                self.__reversi_packages.reversing_stones(act, self.__whose_turn.stone_color)

                if self.__display_board:
                    self.__reversi_packages.display_board()
                self.switch_player()
                if self.__winner != None:
                    if self.__winner == self.__options['DRAW']:
                        if self.__display_result:
                            print("おあいこやないかい!")
                    # elif self.__winner == self.__whose_turn.stone_color:
                    #     out = self.__whose_turn.name + "の勝ちやで〜〜よーやったなあ！"
                    # if self.__display_result:
                    # print(out)

            self.__win_num_cnt[self.__winner] += 1
            self.__finished_game_num += 1


    def switch_player(self):
        """
        swich player in reversi game
        """
        # if it is white player's turn, decide next player by get_stone_putable_pos
        if self.__whose_turn == self.__player_white:
            if self.__reversi_packages.get_stone_putable_pos(self.__options['BLACK']):
                self.__whose_turn = self.__player_black
            elif not self.__reversi_packages.get_stone_putable_pos(self.__options['WHITE']):
                self.__winner = self.__reversi_packages.check_winner()
            else:
                self.__whose_turn = self.__player_white
        else:
            if self.__reversi_packages.get_stone_putable_pos(self.__options['WHITE']):
                self.__whose_turn = self.__player_white
            elif not self.__reversi_packages.get_stone_putable_pos(self.__options['BLACK']):
                self.__winner = self.__reversi_packages.check_winner()
            else:
                self.__whose_turn = self.__player_black
