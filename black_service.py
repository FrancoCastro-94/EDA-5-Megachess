from pawn import blackPawn
from queen import blackQueen


# create_pawns create a list of pawns for each 'p' in the board
def update_black_pawns(board):
    pawns = list()
    for row in range(2, 9):
        for col in range(16):
            if board[row][col] == 'p':
                new_pawn = blackPawn(row, col)
                pawns.append(new_pawn)
    return pawns


# possible_pawn_attacks groups possible pawn attacks
def possible_pawn_attacks(pawns, board):
    possible_pawn_attacks = list()
    for p in pawns:
        possible_pawn_attacks.append(p.atack(board))
    return possible_pawn_attacks


# create_black_queens create a list of queens for each 'q' in the board
def update_black_queens(board):
    queens = list()
    for row in range(16):
        for col in range(16):
            if board[row][col] == 'q':
                new_pawn = blackQueen(row, col)
                queens.append(new_pawn)
    return queens


# possible_queens_attacks groups possible queens attacks
def possible_queens_attacks(queens, board):
    possible_queens_attacks = list()
    for q in queens:
        possible_queens_attacks.append(q.atack(board))
    return possible_queens_attacks


def move_pawns(pawns, board):
    try:
        for p in pawns:
            move = p.move(board)
            if move[0]:
                return move
    except:
        return [False]


def attack_pawns(pawns, board):
    possible_pawn_attacks = list()
    try:
        for p in pawns:
            attack = p.attack(board)
            if attack[0]:
                possible_pawn_attacks.append(attack)
        return possible_pawn_attacks
    except:
        return [False]


def best_pawn_attack(pawns):
    best_attack_list = attack_pawns(pawns)
    try:
        for a in best_attack_list:
            if a[0]:
                if a[1] == 'Q':
                    return a
                if a[1] == 'R':
                    return a
                if a[1] == 'B':
                    return a
                if a[1] == 'H':
                    return a
        return [False]
    except:
        return [False]

"""
def update_pieces(board):
    pawns = update_black_pawns(board)    
"""