import numpy as np
import torch

from reversiAPI.players.models.models import TheModelClassSl1

def load_model(file_path):
    model = TheModelClassSl1()
    model.load_state_dict(torch.load(file_path))
    model.eval()
    return model

class PlayerSl(object):
    def __init__(self, stone_color, file_path, display=True):
        self.stone_color = stone_color
        self.model = load_model(file_path)
        self.display = display

    def put_stone(self, reversi_pakages):
        with torch.no_grad():
            input_array = np.array(reversi_pakages.get_board_status(self.stone_color))

            # 上記boardにはputtable_pos(2)が含まれているので削除する
            input_array = np.where(input_array == 2, 0, input_array)

            # 黒手番の時の盤面情報は反転させる
            if self.stone_color == -1:
                input_array *= -1

            # 推論に使えるデータサイズに変更する
            input_array = input_array.reshape(-1, 1, 8, 8)

            # NNの出力を算出
            input_tensor = torch.Tensor(input_array)
            output = self.model(input_tensor)
            output = np.array(output[0])

        # 置ける場所のうち最大のindexに石を置く
        puttable_index = reversi_pakages.get_stone_putable_pos(self.stone_color)
        filterd_probability = np.full(64, -1000)
        filterd_probability[puttable_index] = output[puttable_index]
        stone_put_index = np.argmax(filterd_probability)

        if self.display:
            print(stone_put_index + 1, self.stone_color)

        return stone_put_index



