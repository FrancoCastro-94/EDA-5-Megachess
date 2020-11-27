from random import randint
import numpy as np
from turn import WhiteTurn
from turn import BlackTurn


def update_board(data_board):
    list_board = list(data_board)
    toArray = np.array(list_board)
    ToBoard = toArray.reshape(16, 16)
    return ToBoard


def move_pawns(pawns, new_board):
    try:
        for p in pawns:
            move = p.move(new_board)
            if move:
                return move
    except:
        return False


def possible_attack(attacks):
    try:
        for a in attacks:
            if a:
                print(a)
                return a[0]
    except:
        return False


def forced_move():
    move = [randint(0, 15), randint(0, 15), randint(0, 15), randint(0, 15)]
    return move


def play_black(data_board):
    turn = BlackTurn(update_board(data_board))
    turn.update()
    attack = possible_attack(turn.possible_attacks())
    print(turn.board)
    if attack:
        return [attack[1], attack[2], attack[3], attack[4]]
    try:
        move = move_pawns(turn.pawns, turn.board)
        return [move[0], move[1], move[2], move[3]]
    except:
        return forced_move()


def play_white(data_board):
    turn = WhiteTurn(update_board(data_board))
    turn.update()
    attack = possible_attack(turn.possible_attacks())
    print(turn.board)
    if attack:
        return [attack[1], attack[2], attack[3], attack[4]]
    try:
        move = move_pawns(turn.pawns, turn.board)
        return [move[0], move[1], move[2], move[3]]
    except:
        return forced_move()
