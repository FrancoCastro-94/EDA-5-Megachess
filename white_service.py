from pawn import WhitePawn
from queen import BlackQueen
from turn import WhiteTurn

"""
# create_pawns create a list of pawns for each 'p' in the board
def update_white_pawns(board):
    pawns = list()
    for row in range(13, 8, -1):
        for col in range(16):
            if board[row][col] == 'P':
                new_pawn = WhitePawn(row, col)
                pawns.append(new_pawn)
    return pawns


# possible_pawn_attacks groups possible pawn attacks
def possible_pawn_attacks(pawns, board):
    pawn_attacks = list()
    for p in pawns:
        pawn_attacks.append(p.atack(board))
    return pawn_attacks


# create_black_queens create a list of queens for each 'q' in the board
def update_black_queens(board):
    queens = list()
    for row in range(16):
        for col in range(16):  # Atencion cambiar las reinas a blancas
            if board[row][col] == 'q':
                new_pawn = BlackQueen(row, col)
                queens.append(new_pawn)
    return queens


# possible_queens_attacks groups possible queens attacks
def possible_queens_attacks(queens, board):
    queens_attacks = list()
    for q in queens:
        queens_attacks.append(q.atack(board))
    return queens_attacks
"""

def move_pawns(pawns, board):
    try:
        for p in pawns:
            move = p.move(board)
            if move:
                return move
    finally:
        return False


"""
def attack_pawns(pawns, board):
    pawn_attacks = list()
    try:
        for p in pawns:
            attack = p.attack(board)
            if attack:
                pawn_attacks.append(attack)
        return pawn_attacks
    except:
        return [False]


def update_pieces(board):
    pawns = update_black_pawns(board)    
"""


def possible_attack(attacks):
    try:
        for a in attacks:
            if a:
                return a
    finally:
        return False

