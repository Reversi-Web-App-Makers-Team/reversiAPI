import toml
import numpy as np
import copy


class ReversiPackages(object):

    '''
    This class is packages used in reversi_processor.py
    '''
    
    def __init__(self, board=None, options=None, display_board=True):
        
        '''
        Initialize class parameters.
        
        Args:
            display_board(boolean):
                False -> not display board
                True -> display board

            board(list):
                shape = (total_square_num=64, 1)
                instructions: board state
                              empty(no stone) -> 0
                              white stone -> 1
                              brack stone -> -1

            options(toml):
                global parameters.
        '''
        
        # self.__options is global parameters
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
                
            # set initial 2 white stones
            for initial_white_place in self.__options['INITIAL_WHITE_PLACES']:
                self.__board[initial_white_place] = self.__options['WHITE']

            # set initial 2 black stones
            for initial_black_place in self.__options['INITIAL_BLACK_PLACES']:
                self.__board[initial_black_place] = self.__options['BLACK']
            
        else:
            self.__board = board
            
        # self.__winner flag is used when checking winner
        self.__winner == None

        # self.__reversable_stone_number_dict: dictionary
        #   keys: empty(no stone) index in game board
        #   values: list of how many stones reversed when putting stone there for all 8 directions
        self.__reversable_stone_number_dict = {}

        self.__display_board = display_board
        # make class variables for displaying board
        if self.__display_board:

            # converter dictinary (1, -1, 0 -> "⚪️", " ⚫️", "None")
            self.__marks = toml.load('./settings.toml')['MARKS']

            # number board (1 ~ 64) for displaying
            self.__index_board_for_displaying = []
            for index in range(self.__options['SQUARE_NUM']):
                self.__index_board_for_displaying.append(index + 1)


    def get_index_in_padded_board(self, index_in_1d_board):
        '''
        This function get index in padded 8x8 board from one dimension board index
        Args board:
        Returns:

        '''
        return index_in_1d_board // 8 + 1, index_in_1d_board % 8 + 1


    def select_pos_loop(self, base_vector, unit_vector, index, padded_board, stone_color, counter):
        '''

        :param base_vector:
        :param unit_vector:
        :param index:
        :param padded_board:
        :param stone_color:
        :return:
        '''
        counter += 1
        index_status = padded_board[self.get_index_in_padded_board(index)[0] + base_vector[0]][self.get_index_in_padded_board(index)[1] + base_vector[1]]
        if index_status == stone_color:
            return index, self.counter
        elif index_status == -1 * stone_color:
            base_vector+=unit_vector
            return self.select_pos_loop(base_vector, unit_vector, index, padded_board, stone_color)
        else:
            return False, 0

    def select_pos(self, unit_vector, index, padded_board, stone_color):
        '''

        :Args
            d1():
            d0:
            i:
            board:
            stone_color:
        :Return:
        '''
        # counter counts the number of reversible stone
        counter = 1
        index_status = padded_board[self.get_index_in_padded_board(index) + 2 * unit_vector[0]][self.get_index_in_padded_board(index) + 2 * unit_vector[1]]
        if index_status == stone_color:
            return True, counter
        elif index_status == -1 * stone_color:
            base_vector = 3 * unit_vector
            return self.select_pos_loop(base_vector, unit_vector, index, padded_board, stone_color,counter)
        else:
            return False, 0


    def get_stone_put_able_pos_set(self, stone_color):
        '''

            Initialize class parameters.

        Args:
            stone_color(int):
                shape = ()
                instructions:
                              white -> 1
                              brack -> -1

        Returns:
            pos_set(set):
                instructions:
                    get stone put able position set

        '''
        board_8x8 = np.array(self.__board).reshape(8,8)
        vertical_edge_pad = np.full((1, 8), self.__options['ERROR'])
        horizontal_edge_pad = np.full((10, 1), self.__options['ERROR'])
        vertical_padded_board = np.vstack((vertical_edge_pad, board_8x8, vertical_edge_pad))
        padded_board = np.hstack((horizontal_edge_pad, vertical_padded_board, horizontal_edge_pad))
        empty_pos_index_list = []
        for index in range(64):
            if self.board[index] == self.__options['EMPTY']:
                empty_pos_index_list.append(index)

        pos = {}
        for empty_pos_index in empty_pos_index_list:
            reversible_stone_number_list = [0, 0, 0, 0, 0, 0, 0, 0]
            if padded_board[self.get_index_in_padded_board(empty_pos_index)[0]-1][self.get_index_in_padded_board(empty_pos_index)[1]] == -1 * stone_color:
                put_able, counter = self.select_pos([-1, 0],  empty_pos_index, padded_board, stone_color)
                if put_able:
                    reversible_stone_number_list[0] = counter
                    pos.append(empty_pos_index)

            self.dd_dict[empty_pos_index] = reversible_stone_number_list

        return pos


    def check_winner(self):

        '''
        This function check which player wins (black stone player of white stone player) or draw.
            if winner is white, self.__winner <- 1
            if winner is brack, self.__winner <- -1
            if draw, self.__winner <- 2
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

        # putting new stone
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

    
    def display_board(self):
        if self.__display_board:
            temp_board = []

            # convert (1, -1, 0) -> ("⚪️", " ⚫️", "None")
            for i in self.__board:
                temp_board.append(marks[i])

            # convert "None" -> index (1 ~ 64)
            for i in range(self.__options['SQUARE_NUM']):
                if temp_board[i] == " ":
                    temp_board[i] = "%02d" % self.__index_board_for_displaying[i]

            # lines
            row = " {} | {} | {} | {} | {} | {} | {} | {} "
            hr = "\n---------------------------------------\n"

            # printing board
            print((row + hr + row + hr + row + hr + row + hr + row + hr + row + hr + row + hr + row).format(*temp_board))

        else:
            return

