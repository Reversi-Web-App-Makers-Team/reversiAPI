REVERSI_PACKAGES = {
    'EMPTY': 0,
    'WHITE': 1,
    'BLACK': -1,
    'DRAW': 2,
    'ERROR': -999,
    'EDGE_PAD': -999,
    'SQUARE_NUM': 64,
    'SIDES_NUM': 8,
    'CHANGE_COLOR': -1,
    'ALL_VECTORS': [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]],
    'VECTOR_NUM': 8,
    'INITIAL_REVERSIBLE_STONE_NUMBER_LIST': [0, 0, 0, 0, 0, 0, 0, 0],
    'INITIAL_WHITE_PLACES': [27, 36],
    'INITIAL_BLACK_PLACES': [28, 35]
}

MARKS = {
    '0': " ",
    '1': "⚪️",
    '-1': "⚫️"
}

REVERSI_PROCESSOR = {
    'DRAW': 2,
    'WHITE': 1,
    'BLACK': -1
}

DQN = {
        'pt_path1': 'players/models/model1/model1_1.pt',
        'pt_path2': 'players/models/model2/model2_1.pt'
}

SL = {
        'pt_path1': 'players/models/modelSL1/model_sl1_1.pt',
        'pt_path2': 'players/models/modelSL2/model_sl2_1.pt'
}
