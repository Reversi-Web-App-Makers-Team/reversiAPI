import torch

from reversiAPI.utils.reversi_packages import ReversiPackages

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

    def put_stone(self):
        with torch.no_grad():
            
        

