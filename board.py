import numpy as np


def update_board(data_board):
    list_board = list(data_board)
    toArray = np.array(list_board)
    ToBoard = toArray.reshape(16, 16)
    return ToBoard


class board:
    def __init__(self, data_board):
        self.board = update_board(data_board)

    def update(self, data_board):
        self.board = update_board(data_board)
