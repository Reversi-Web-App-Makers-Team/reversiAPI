class PlayerHuman:
    def __init__(self, name, stone_color):
        self.name = name
        self.stone_color = stone_color
        self.reversi_packages = ReversiPackages()

    def put_stone(self, reversi_packages):
        is_invalid_putting = True
        while is_invalid_putting:
            try:
                print("\rどこ置きまっか？")
                stone_putting_place = int(input())

                print("\r" + str(stone_putting_place))

                if stone_putting_place - 1 in reversi_packages.get_stone_putable_pos(self.stone_color):
                    is_invalid_putting = False
                    return stone_putting_place - 1
                else:
                    print("\rそこおけへんで〜〜")

            except Exception as e:
                print("\rアホちゃう?")
