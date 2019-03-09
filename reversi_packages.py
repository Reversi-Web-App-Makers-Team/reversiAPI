import toml
import numpy as np


class ReversiPackages(object):
    '''
    This class is packages used in organizing reversi game
    '''
    
    def __init__(self, board=None, options=None):
        
        '''
        Initialize class parameters.
        
        Args:
            board(list):
                shape = (total_square_num=64, 1)
                instructions: board state.
                              empty -> 0
                              white -> 1
                              brack -> -1
            options(toml):
                global parameters.
        '''
        
        # options is global parameters.
        if options == None:
            self.__options = toml.load(./settings.toml)['REVERSI_PACKAGES']
        else:
            self.__options = options
        
        # board is game board
        if board == None:
            self.__board=[]
            
            # make empty board.
            for index in range(self.__options['SQUARE_NUM']):
                self.__board.append(self.__options['EMPTY'])
                
            # set initial 4 stones.
            self.__board[27] = self.__options['WHITE']
            self.__board[28] = self.__options['BRACK']
            self.__board[35] = self.__options['BRACK']
            self.__board[36] = self.__options['WHITE']
            
        else:
            self.__board = board
            
        self.__winner == None
        self.__vector_and_distance_dict = {}
