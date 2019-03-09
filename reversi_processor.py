import randam

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

        
