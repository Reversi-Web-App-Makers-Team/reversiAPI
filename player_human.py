class PlayerHuman:
    def __init__(self, turn, name):
        self.name = name
        self.myturn = turn

    def act(self, board):
        valid = False
        while not valid:
            try:
                act = input("どこ置きまっか？" + str(marks[self.myturn]))
                act = int(act)
                if act-1 in board.get_possible_pos(self.myturn):
                    valid = True
                    return act - 1
                elif act-1 not in board.get_possible_pos(self.myturn):
                    print("そこおけへんで〜〜")
            except Exception as e:
                print(act + "はやめて")
        return act

    def getGameResult(self, board):
        if board.winner is not None and board.winner != self.myturn and board.winner != draw:
            print(self.name + "の負けや")