import randam

import toml
import numpy as np

from Reversi-API.reversi_packages import ReversiPackages


class ReversiProcessor(object):
    
    '''
    This class processes reversi game.
    '''

    def __init__(
            self,
            player_white_class, 
            player_black_class,
            options = None,
            play_game_num = 1, 
            display_board = True, 
            display_result = True, 
            stat=1000000
            ):

        self.__player_white = player_white_class
        self.__player_black = player_black_class

        if options == None:
            self.__options = toml.load('settings.toml')['REVERSI_PROCESSOR']
        else:
            self.__options = options
            
        self.__play_game_num = play_game_num
        self.__display_board = display_board
        self.__display_result = display_result
        self.__stat = stat
        self.__win_num_cnt = {
                self.__player_white: 0,
                self.__player_black: 0
                draw: 0
                }
        self.__board = None
        self.__player_list = [
                self.__player_white,
                self.__player_black
                ]
        self.__whose_turn = self.__player_tupple[random.randrange(2)]
        self.__finished_game_num = 0


        
