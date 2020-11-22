import numpy as np

b = 'rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrpppppppppppppppppppppppppppppppp                                                                                                                                PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR'


def update_board(data_board):
    list_board = list(data_board)
    toArray = np.array(list_board)
    ToBoard = toArray.reshape(16, 16)
    return ToBoard


def update_board(data_board):
    to_list = list(data_board)
    board = list()
    for i in range(0, 256, 16):
        board.append(to_list[i:i + 16])
    return board
