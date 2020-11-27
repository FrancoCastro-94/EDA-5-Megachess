import numpy as np

b = 'rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrpppppppppppppppppppQppppppppppppp                                      r                                                                                        PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR'
#  0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15
a = [['r' 'r' 'h' 'h' 'b' 'b' 'q' 'q' 'k' 'k' 'b' 'b' 'h' 'h' 'r' 'r'],  #
     ['r' 'r' 'h' 'h' 'b' 'b' 'q' 'q' 'k' 'k' 'b' 'b' 'h' 'h' 'r' 'r'],  # 1
     [' ' ' ' 'p' 'p' 'p' 'p' 'p' 'p' 'p' 'p' 'p' 'p' 'p' 'p' 'p' 'p'],  #
     ['p' 'p' 'p' 'p' 'p' 'p' 'p' 'p' 'p' 'p' 'p' 'p' 'p' 'p' 'p' 'p'],  # 3
     ['p' 'p' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' '],  #
     [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' '],  # 5
     [' ' ' ' ' ' ' ' ' ' ' ' ' ' 'r' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' '],  # 6
     [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' '],  # 7
     [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' '],
     [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' '],  # 9
     [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' '],
     [' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' ' 'P' 'P'],  # 11
     ['P' 'P' 'P' 'P' 'P' 'P' 'P' 'P' 'P' 'P' 'P' 'P' 'q' 'P' 'P' 'P'],
     ['P' 'P' 'P' 'P' 'P' 'P' 'P' 'P' 'P' 'P' 'P' 'P' 'P' 'P' ' ' ' '],  # 13
     ['R' 'R' 'H' 'H' 'B' 'B' 'Q' 'Q' 'K' 'K' 'B' 'B' 'H' 'H' 'R' 'R'],
     ['R' 'R' 'H' 'H' 'B' 'B' 'Q' 'Q' 'K' 'K' 'B' 'B' 'H' 'H' 'R' 'R']]  # 15

c = "rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrr                                                pppppppppppppppp pppppppppppppppq                              QPPPPPPPPPPPPPPP PPPPPPPPPPPPPPPP                                                RRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR"


def update(data_board):
    list_board = list(data_board)
    toArray = np.array(list_board)
    ToBoard = toArray.reshape(16, 16)
    return ToBoard


def update_board(data_board):
    board = list()
    to_list = list(data_board)
    for i in range(0, 256, 16):
        board.append(to_list[i:i + 16])
    return board


def nueva():
    toArray = np.array(a)
    ToBoard = toArray.reshape(16, 16)
    return ToBoard
