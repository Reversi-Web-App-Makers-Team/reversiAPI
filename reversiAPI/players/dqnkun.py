import torch


def load_model(file_path):
    model = TheModelClass(*args, **kwargs)
    model.load_state_dict(torch.load(file_path))
    model.eval()
    return model

class PlayerDqn(object):
    def __init__(self, stone_color, file_path):
        self.stone_color = stone_color
        self.model = load_model(file_path)
        self.reversi_packages = ReversiPackages()

    def put_stone(self, reversi_packages):
        with torch.no_grad():
            input_array = np.append(
                    np.array(self.stone_color), np.array(reversi_packages.board)
                    )
            input_data = torch.from_numpy(input_array).type(torch.FloatTensor)
            input_data_unsqueezed = torch.unsqueeze(input_data, 0)
            probability = np.array(self.model(input_data_unsqueezed)).reshape(-1)

        puttable_index = reversi_packages.get_stone_putable_pos(self.stone_color)
        filtered_probability = np.zeros(64)
        for index in puttable_index:
            filtered_probability[index] = probability[index]

        stone_put_index = np.argmax(filtered_probability)
        print(stone_put_index + 1, self.stone_color)
 
        return stone_put_index
