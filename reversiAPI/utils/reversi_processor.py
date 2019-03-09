import random
import toml
import numpy as np
from reversi_packages import ReversiPackages


class ReversiProcessor(object):
    
    '''
    This class processes reversi game.
    '''

    def __init__(
            self, 
            player_white_class, 
            player_black_class, 
            play_num = 1, 
            display_board = True, 
            display_result = True, 
            stat=1000000
            ):
        self.__player_white = player_white_class
        self.__player_black = player_black_class

        



    def switch_player(self):
        if self.player_turn == self.player_w:
            if not self.board.get_possible_pos(player_b):
                self.player_turn = self.player_b
            elif self.board.get_possible_pos(player_b):
                self.player_turn = self.player_w
                if self.board.get_possible_pos(player_w):
                    self.board.check_winner()
        else:
            if not self.board.get_possible_pos(player_w):
                self.player_turn = self.player_w
            elif self.board.get_possible_pos(player_w):
                self.player_turn = self.player_b
                if self.board.get_possible_pos(player_b):
                    self.board.check_winner()


