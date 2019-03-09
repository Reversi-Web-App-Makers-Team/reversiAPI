import toml
import numpy as np


class ReversiPackages(object):

    '''
    This class is packages used in organizing reversi game
    '''
    
    def __init__(self, board=None, options=None, printing=True):
        
        '''
        Initialize class parameters.
        
        Args:
            printing(boolean):
                False -> not printing board.
                True -> printing board.

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
                
            # set initial 2 white stones.
            for initial_white_place in self.__options['INITIAL_WHITE_PLACES']:
                self.__board[initial_white_place] = self.__options['WHITE']

            # set initial 2 black stones.
            for initial_black_place in self.__options['INITIAL_BLACK_PLACES']:
                self.__board[initial_black_place] = self.__options['BLACK']
            
        else:
            self.__board = board
            
        # self.__winner flag is used when checking winner.
        self.__winner == None

        # self.__reversable_stone_number_dict: dictionary
        #   keys: empty(no stone) index in game board
        #   values: list of how many stones reversed when putting stone there for all 8 directions
        self.__reversable_stone_number_dict = {}

        # make class variables for printing board.
        if printing:

            # converter dictinary (1, -1, 0 -> "⚪️", " ⚫️", "None")
            self.__marks = toml.load('./settings.toml')['MARKS']

            # number board (1 ~ 64) for displaying
            self.__index_board_for_print = []
            for index in range(self.__options['SQUARE_NUM']):
                self.__index_board_for_print.append(index + 1)


    def check_winner(self):

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


    def reversing_stones(self, putting_index, stone_color):

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

        # reversing stone for all 8 directions adapting to self.__reversable_stone_number_dict
        for i in range(self.__reversable_stone_number_dict[putting_index][0]):
            i += 1
            self.__board[putting_index - 8 * i] *= self.__options['CHANGE_COLOR']

        for i in range(self.__reversable_stone_number_dict[putting_index][1]):
            i += 1
            self.__board[putting_index - 7 * i] *= self.__options['CHANGE_COLOR']

        for i in range(self.__reversable_stone_number_dict[putting_index][2]):
            i += 1
            self.__board[putting_index + i] *= self.__options['CHANGE_COLOR']

        for i in range(self.__reversable_stone_number_dict[putting_index][3]):
            i += 1
            self.__board[putting_index + 9 * i] *= self.__options['CHANGE_COLOR']

        for i in range(self.__reversable_stone_number_dict[putting_index][4]):
            i += 1
            self.__board[putting_index + 8 * i] *= self.__options['CHANGE_COLOR']

        for i in range(self.__reversable_stone_number_dict[putting_index][5]):
            i += 1
            self.__board[putting_index + 7 * i] *= self.__options['CHANGE_COLOR']

        for i in range(self.__reversable_stone_number_dict[putting_index][6]):
            i += 1
            self.__board[putting_index - i] *= self.__options['CHANGE_COLOR']

        for i in range(self.__reversable_stone_number_dict[putting_index][7]):
            i += 1
            self.__board[putting_index - 9 * i] *= self.__options['CHANGE_COLOR']

    
    def print_board(self):
        temp_board = []

        # convert (1, -1, 0) -> ("⚪️", " ⚫️", "None")
        for i in self.board:
            temp_board.append(marks[i])

        # convert "None" -> index (1 ~ 64)
        for i in range(self.__options['SQUARE_NUM']):
            if temp_board[i] == " ":
                temp_board[i] = "%02d" % self.index_board[i]

        # lines
        row = " {} | {} | {} | {} | {} | {} | {} | {} "
        hr = "\n---------------------------------------\n"

        # printing board
        print((row + hr + row + hr + row + hr + row + hr + row + hr + row + hr + row + hr + row).format(*temp_board))

