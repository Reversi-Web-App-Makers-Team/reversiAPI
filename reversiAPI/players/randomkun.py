import random


class PlayerRandom:
    def __init__(self, stone_color):
        self.stone_color = stone_color

    def put_stone(self, reversi_packages):
        stone_put_index = random.choice(
                reversi_packages.get_stone_putable_pos(self.stone_color)
                )
        print(stone_put_index + 1, self.stone_color)
        return stone_put_index
