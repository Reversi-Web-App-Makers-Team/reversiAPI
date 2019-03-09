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
                              empty(no stone) -> 0
                              white stone -> 1
                              brack stone -> -1
            options(toml):
                global parameters.
        '''
        
        # self.__options is global parameters.
        if options == None:
            self.__options = toml.load('./settings.toml')['REVERSI_PACKAGES']
        else:
            self.__options = options
        
        # self.__board is game board
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
            
        # self.__winner flag is used when checking winner.
        self.__winner == None

        # self.__reversed_stone_number_dict: dictionary
        #   keys: empty(no stone) index in game board
        #   values: list of how many stones reversed when putting stone there for all 8 directions
        self.__reversed_stone_number_dict = {}


    def _check_winner(self):

        '''
        This function check which player wins (black stone player of white stone player) or draw.
            if winner is white, self.__winner <- 1
            if winner is brack, self.__winner <- -1
            if draw, self.__winner <-  2
        '''

        sum_score = sum(self.__board)

        # if winner is white, sum_score > 0
        if sum_score > 0:
            self.__winner = options['WHITE']

        # if winner is black, sum_score < 0
        elif sum_score < 0:
            self.__winner = options['BLACK']

        # if draw, sum_score = 0
        else:
            self.__winner = options['DRAW']


    def _reversing_stones(self, putting_index, stone_color):

        '''
        This function reversing stones adapted to putting place.
        inserting reversed board information to self.__board.

        Args:
            putting_index(int):
                index where putting new stone
            stone_color(int):
                stone's color
                white -> 1
                black -> -1
        '''

        # putting new stone.
        self.__board[putting_index] = player

        # reversing stone for all 8 directions adapting to self.__reversed_stone_number_dict
        for i in range(self.__reversed_stone_number_dict[putting_index][0]):
            i += 1
            self.__board[putting_index - 8 * i] *= -1

        for i in range(self.__reversed_stone_number_dict[putting_index][1]):
            i += 1
            self.__board[putting_index - 7 * i] *= -1

        for i in range(self.__reversed_stone_number_dict[putting_index][2]):
            i += 1
            self.__board[putting_index + i] *= -1

        for i in range(self.__reversed_stone_number_dict[putting_index][3]):
            i += 1
            self.__board[putting_index + 9 * i] *= -1

        for i in range(self.__reversed_stone_number_dict[putting_index][4]):
            i += 1
            self.__board[putting_index + 8 * i] *= -1

        for i in range(self.__reversed_stone_number_dict[putting_index][5]):
            i += 1
            self.__board[putting_index + 7 * i] *= -1

        for i in range(self.__reversed_stone_number_dict[putting_index][6]):
            i += 1
            self.__board[putting_index - i] *= -1

        for i in range(self.__reversed_stone_number_dict[putting_index][7]):
            i += 1
            self.__board[putting_index - 9 * i] *= -1

