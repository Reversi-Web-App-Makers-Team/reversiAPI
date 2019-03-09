class PlayerHuman:
    def __init__(self, turn, name):
        self.name = name
        self.myturn = turn

    def act(self, board):
        valid = True
        while valid:
            try:
                act = input(str(marks[self.myturn]) + "どこ置きまっか？:")
                act = int(act)
                if act - 1 in board.get_possible_pos(self.myturn):
                    valid *= -1
                    return act - 1
                else:
                    print("そこおけへんで〜〜")
            except Exception as e:
                print("アホちゃう?")
    #    return act

    # def getGameResult(self, board):
    #     if board.winner is not None and board.winner != self.myturn and board.winner != draw:
    #         print("おまえの負けや")
