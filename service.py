import numpy
from random import randint
from turn import WhiteTurn, BlackTurn


def to_matrix_board(data_board):
    list_board = list(data_board)
    to_array = numpy.array(list_board)
    to_matrix = to_array.reshape(16, 16)
    return to_matrix


def move_horse(horses):
    for h in horses:
        if h.move:
            return h.move


def move_pawns(pawns, horses, board):
    try:
        for p in reversed(pawns):
            move = p.move(board)
            if move:
                return move
        for h in horses:
            move = h.move
            if move:
                return move[0]
    except Exception as e:
        print(e)
        return False


def move_pawns_black(pawns, horses, board):
    defenders_pawns = [10, 9, 8, 7]
    try:
        for p in reversed(pawns):
            if p.col in defenders_pawns:
                continue
            move = p.move(board)
            if move:
                return move
        for h in horses:
            move = h.move
            if move:
                return move[0]

    except Exception as e:
        print(e)
        return False


def possible_attack(attacks):
    try:
        for a in attacks:
            if a:
                return a
    except Exception as e:
        print(e)
        return False


def forced_move():
    move = [randint(0, 15), randint(0, 15), randint(0, 15), randint(0, 15)]
    return move


def play_black(data):
    current_board = to_matrix_board(data['board'])
    turn = BlackTurn(current_board)
    attack = possible_attack(turn.update())

    try:
        if attack:
            return [attack[1], attack[2], attack[3], attack[4]]
        else:
            move = move_pawns_black(turn.pawns, turn.horses, turn.board)
            return [move[0], move[1], move[2], move[3]]

    except Exception as e:
        print(e)
    return forced_move()


def play_white(data):
    current_board = to_matrix_board(data['board'])
    print(current_board)
    turn = WhiteTurn(current_board)
    attack = possible_attack(turn.update())
    try:
        if attack:
            return [attack[1], attack[2], attack[3], attack[4]]
        else:
            move = move_pawns(turn.pawns, turn.horses, turn.board)
            return [move[0], move[1], move[2], move[3]]
    except Exception as e:
        print(e)
        return forced_move()
