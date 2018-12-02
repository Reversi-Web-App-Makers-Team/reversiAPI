import numpy as np
import random

empty = 0
player_w = 1
player_b = -1
marks = {empty: " ", player_w: "⚪️", player_b: "⚫️"}
draw = 2
error = -999

class ReversiBoard:

    def __init__(self, board=None):
        self.index_board = []
        for i in range(64):
            self.index_board.append(i + 1)
        if board == None:
            self.board = []
            for i in range(64):
                self.board.append(empty)
            self.board[27] = player_w
            self.board[28] = player_b
            self.board[35] = player_b
            self.board[36] = player_w


        else:
            self.board = board
        self.winner = None
        self.counter = 0
        self.dd_dict = {}

    def select_pos_roop(self, d1, d0, i, board, player):
        self.counter += 1
        board_i = board[i // 8 + 1 + d1[0]][i % 8 + 1 + d1[1]]
        if board_i == player:
            return i, self.counter
        elif board_i == -1 * player:
            d2 = [0, 0]
            d2[0] = d1[0] + d0[0]
            d2[1] = d1[1] + d0[1]
            return self.select_pos_roop(d2, d0, i, board, player)
        else:
            return error, empty

    def select_pos(self, d1, d0, i, board, player):
        self.counter += 1
        board_i = board[i // 8 + 1 + 2 * d1[0]][i % 8 + 1 + 2 * d1[1]]
        if board_i == player:
            return i, self.counter
        elif board_i == -1 * player:
            d2 = [0, 0]
            d2[0] = 2 * d1[0] + d0[0]
            d2[1] = 2 * d1[1] + d0[1]
            return self.select_pos_roop(d2, d0, i, board, player)
        else:
            return error, empty

    def get_possible_pos(self, player):
        board_8x8 = np.array(self.board).reshape(8, 8)
        pad_1 = np.full((1, 8), error)
        pad_2 = np.full((10, 1), error)
        a = np.vstack((pad_1, board_8x8))
        b = np.vstack((a, pad_1))
        c = np.hstack((pad_2, b))
        padded_board = np.hstack((c, pad_2))
        empty_index = []
        for i in range(64):
            if self.board[i] == empty:
                empty_index.append(i)

        pos = []
        for i in empty_index:
            d_d = [0, 0, 0, 0, 0, 0, 0, 0]
            if padded_board[i // 8][i % 8 + 1] == -1 * player:
                ip, counter = self.select_pos([-1, 0], [-1, 0], i, padded_board, player)
                if ip == i:
                    d_d[0] = counter
                    if i not in pos:
                        pos.append(ip)
                self.counter = 0
            if padded_board[i // 8][i % 8 + 2] == -1 * player:
                ip, counter = self.select_pos([-1, 1], [-1, 1], i, padded_board, player)
                if ip == i:
                    d_d[1] = counter
                    if i not in pos:
                        pos.append(ip)
                self.counter = 0
            if padded_board[i // 8 + 1][i % 8 + 2] == -1 * player:
                ip, counter = self.select_pos([0, 1], [0, 1], i, padded_board, player)
                if ip == i:
                    d_d[2] = counter
                    if i not in pos:
                        pos.append(ip)
                self.counter = 0
            if padded_board[i // 8 + 2][i % 8 + 2] == -1 * player:
                ip, counter = self.select_pos([1, 1], [1, 1], i, padded_board, player)
                if ip == i:
                    d_d[3] = counter
                    if i not in pos:
                        pos.append(ip)
                self.counter = 0
            if padded_board[i // 8 + 2][i % 8 + 1] == -1 * player:
                ip, counter = self.select_pos([1, 0], [1, 0], i, padded_board, player)
                if ip == i:
                    d_d[4] = counter
                    if i not in pos:
                        pos.append(ip)
                self.counter = 0
            if padded_board[i // 8 + 2][i % 8] == -1 * player:
                ip, counter = self.select_pos([1, -1], [1, -1], i, padded_board, player)
                if ip == i:
                    d_d[5] = counter
                    if i not in pos:
                        pos.append(ip)
                self.counter = 0
            if padded_board[i // 8 + 1][i % 8] == -1 * player:
                ip, counter = self.select_pos([0, -1], [0, -1], i, padded_board, player)
                if ip == i:
                    d_d[6] = counter
                    if i not in pos:
                        pos.append(ip)
                self.counter = 0
            if padded_board[i // 8][i % 8] == -1 * player:
                ip, counter = self.select_pos([-1, -1], [-1, -1], i, padded_board, player)
                if ip == i:
                    d_d[7] = counter
                    if i not in pos:
                        pos.append(ip)
                self.counter = 0

            self.dd_dict[i] = d_d
        return pos

    def print_board(self):
        temp_board = []
        for i in self.board:
            temp_board.append(marks[i])
        for i in range(64):
            if temp_board[i] == " ":
                temp_board[i] = "%02d" % self.index_board[i]
        row = " {} | {} | {} | {} | {} | {} | {} | {} "
        hr = "\n---------------------------------------\n"

        print((row + hr + row + hr + row + hr + row + hr + row + hr + row + hr + row + hr + row).format(*temp_board))

    def check_winner(self):
        Sum = sum(self.board)
        if Sum > 0:
            self.winner = player_w
        elif Sum == 0:
            self.winner = draw
        else:
            self.winner = player_b

    def move(self, act, player):
        self.board[act] = player
        for i in range(self.dd_dict[act][0]):
            i += 1
            self.board[act - 8 * i] *= -1
        for i in range(self.dd_dict[act][1]):
            i += 1
            self.board[act - 7 * i] *= -1
        for i in range(self.dd_dict[act][2]):
            i += 1
            self.board[act + i] *= -1
        for i in range(self.dd_dict[act][3]):
            i += 1
            self.board[act + 9 * i] *= -1
        for i in range(self.dd_dict[act][4]):
            i += 1
            self.board[act + 8 * i] *= -1
        for i in range(self.dd_dict[act][5]):
            i += 1
            self.board[act + 7 * i] *= -1
        for i in range(self.dd_dict[act][6]):
            i += 1
            self.board[act - i] *= -1
        for i in range(self.dd_dict[act][7]):
            i += 1
            self.board[act - 9 * i] *= -1

    def clone(self):
        return ReversiBoard(self.board.copy())


class ReversiOrgnaizer:
    # act_turn = 0
    winner = None

    def __init__(self, pw, pb, nplay=1, show_board=True, show_result=True, stat=10000):
        self.player_w = pw
        self.player_b = pb
        self.nwon = {pw.myturn: 0, pb.myturn: 0, draw: 0}
        self.nplay = nplay
        self.players = (self.player_w, self.player_b)
        self.board = None
        self.disp = show_board
        self.show_result = show_result
        self.player_turn = self.players[random.randrange(2)]
        self.nplayed = 0
        self.stat = stat

    def progress(self):
        while self.nplayed < self.nplay:
            self.board = ReversiBoard()
            self.board.print_board()

            while self.board.winner == None:
                if self.disp:
                    print(self.player_turn.name + "の番やで〜")
                    p_pos = self.board.get_possible_pos(self.player_turn.myturn)
                    plus_1 = [1 for i in range(len(p_pos))]
                    print(str(np.array(p_pos) + np.array(plus_1)) + "に置けるで")
                act = self.player_turn.act(self.board)
                self.board.move(act, self.player_turn.myturn)
                if self.disp:
                    self.board.print_board()
                self.switch_player()
                if self.board.winner != None:
                    # for i in self.players:
                    #     i.getGameResult(self.board)
                    if self.board.winner == draw:
                        if self.show_result:
                            print ("おあいこやないかい!")
                    elif self.board.winner == self.player_turn.myturn:
                        out = self.player_turn.name + "の勝ちやで〜〜よーやったなあ！"
                        if self.show_result:
                            print(out)
                    # self.player_turn.getGameResult(self.board)

            self.nwon[self.board.winner] += 1
            self.nplayed += 1
            # if self.nplayed % self.stat == 0 or self.nplayed == self.nplay:
            #     print(self.player_w.name + ":" + str(
            #         self.nwon[self.player_w.myturn]) + "," + self.player_b.name + ":" + str(
            #         self.nwon[self.player_b.myturn])
            #           + ",おあいこ:" + str(self.nwon[draw]))

    def switch_player(self):
        if self.player_turn == self.player_w:
            if self.board.get_possible_pos(player_b) != []:
                self.player_turn = self.player_b
            elif self.board.get_possible_pos(player_b) == []:
                self.player_turn = self.player_w
                if self.board.get_possible_pos(player_w) == []:
                    self.board.check_winner()
        else:
            if self.board.get_possible_pos(player_w) != []:
                self.player_turn = self.player_w
            elif self.board.get_possible_pos(player_w) == []:
                self.player_turn = self.player_b
                if self.board.get_possible_pos(player_b) == []:
                    self.board.check_winner()
