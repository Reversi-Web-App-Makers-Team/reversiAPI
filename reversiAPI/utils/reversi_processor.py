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
    ):

        '''
        initialize function
        Args:
            player_white_class(Class), player_black_class(Class):
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

        # class ReversiPackages
        self.__reversi_packages = None

        # win number counter (dictionary)
        self.__win_num_cnt = {
            player_white_class.stone_color: 0,
            player_black_class.stone_color: 0,
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
            self.__reversi_packages = ReversiPackages(

                board=None,
                options=None,
                display_board=self.__display_board)
            self.__reversi_packages.display_board()

            # while the winner is defined, progress the game
            while self.__reversi_packages.check_winner() == None:
                if self.__display_board:
                    print(self.__whose_turn.name + "の番やで〜")
                    stone_putable_pos = self.__reversi_packages.get_stone_putable_pos(self.__whose_turn.myturn)
                    plus_one_index = [1 for i in range(len(stone_putable_pos))]
                    print(str(np.array(stone_putable_pos) + np.array(plus_one_index)) + "に置けるで")
                put_stone = self.__whose_turn.put_stone(self.__reversi_packages)
                self.__reversi_packages.reversing_stones(put_stone, self.__whose_turn.myturn)
                if self.__display_board:
                    self.__reversi_packages.display_board()
                self.switch_player()
                if self.__reversi_packages.check_winner() != None:
                    # for i in self.players:
                    #     i.getGameResult(self.board)
                    if self.__reversi_packages.check_winner() == self.__options['DRAW']:
                        if self.__display_result:
                            print("おあいこやないかい!")
                    elif self.__reversi_packages.check_winner() == self.__whose_turn.myturn:
                        out = self.__whose_turn.name + "の勝ちやで〜〜よーやったなあ！"
                        if self.__display_result:
                            print(out)
                    # self.__whose_turn.getGameResult(self.board)

            self.__win_num_cnt[self.__reversi_packages.check_winner()] += 1
            self.__finished_game_num += 1


    def switch_player(self):
        """
        swich player in reversi game
        """
        # if it is white player's turn, decide next player by get_stone_putable_pos
        if self.__whose_turn == self.__player_white:
            if not self.__reversi_packages.get_stone_putable_pos(self.__options['BLACK']):
                self.__whose_turn = self.__player_black
            elif self.__reversi_packages.get_stone_putable_pos(self.__options['BLACK']):
                self.__whose_turn = self.__player_white
                if self.__reversi_packages.get_stone_putable_pos(self.__options['WHITE']):
                    self.__reversi_packages.check_winner()
        else:
            if not self.__reversi_packages.get_stone_putable_pos(self.__options['WHITE']):
                self.__whose_turn = self.__player_white
            elif self.__reversi_packages.get_stone_putable_pos(self.__options['WHITE']):
                self.__whose_turn = self.__player_black
                if self.__reversi_packages.get_stone_putable_pos(self.__options['BLACK']):
                    self.__reversi_packages.check_winner()
