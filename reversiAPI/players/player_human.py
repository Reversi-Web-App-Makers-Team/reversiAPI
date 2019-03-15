import sys

class PlayerHuman:
    def __init__(self, name, stone_color):
        self.__name = name
        self.__stone_color = stone_color
        
    @property
    def name(self):
        return self.__name
    
    @preperty
    def stone_color(self):
        return self.__stone_color

    @classmethod
    def put_stone(self, reversi_packages):
        is_invalid_putting = True
        while is_invalid_putting:
            try:
                sys.stdout.write("\rどこ置きまっか？")
                stone_putting_place = int(input())
                sys.stdout.write("\r" + stone_putting_place)
                sys.stdout.flush()
                if stone_putting_place - 1 in reversi_packages.stone_putable_pos(self.stone_color):
                    is_invalid_putting = False
                    return stone_putting_place - 1
                else:
                    sys.stdout.write("\rそこおけへんで〜〜")
                    sys.stdout.flush()
            except Exception as e:
                sys.stdout.write("\rアホちゃう?")
                sys.stdout.flush()
