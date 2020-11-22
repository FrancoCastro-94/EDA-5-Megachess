from datetime import time
from random import randint
import numpy as np
import black_service as black


def update_board(data_board):
    list_board = list(data_board)
    toArray = np.array(list_board)
    ToBoard = toArray.reshape(16, 16)
    return ToBoard


def forced_move():
    forced_move = [randint(0, 15), randint(0, 15), randint(0, 15), randint(0, 15)]
    return forced_move


def play_black(data):
    board = update_board(data['board'])
    print(board)
    time.sleep(8)
    pawns = black.update_black_pawns(board)
    attack = black.attack_pawns(pawns, board)
    if attack[0]:
        return [attack[2], attack[3], attack[4], attack[5]]
    try:
        move = black.move_pawns(pawns, board)
        return [move[1], move[2], move[3], move[4]]
    except:
        return forced_move()
