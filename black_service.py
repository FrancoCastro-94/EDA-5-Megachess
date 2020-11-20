from pawn import blackPawn
from queen import blackQueen
from board import board as b

board = b('rrhhbbqqkkbbhhrrrrhhbbqqkkbbhhrrpppppppppppppppppppppppppppppppp                                                                                                                                PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPRRHHBBQQKKBBHHRRRRHHBBQQKKBBHHRR')


def uptdate_board(board):
    board.update(board)


# create_pawns create a list of pawns for each 'p' in the board
def create_black_pawns():
    pawns = list()
    for i in range(16):
        for j in range(16):
            if board[i][j] == 'p':
                new_pawn = blackPawn(i, j)
                pawns.append(new_pawn)
    return pawns


# possible_pawn_attacks groups possible pawn attacks
def possible_pawn_attacks(pawns):
    possible_pawn_attacks = list()
    for p in pawns:
        possible_pawn_attacks.append(p.atack())
    return possible_pawn_attacks


# create_black_queens create a list of queens for each 'q' in the board
def create_black_queens():
    queens = list()
    for i in range(16):
        for j in range(16):
            if board[i][j] == 'q':
                new_pawn = blackQueen(i, j)
                queens.append(new_pawn)
    return queens


# possible_queens_attacks groups possible queens attacks
def possible_queens_attacks(queens):
    possible_queens_attacks = list()
    for q in queens:
        possible_queens_attacks.append(q.atack())
    return possible_queens_attacks


def move_pawns(pawns):
    try:
        for p in pawns:
            move = p.move(board)
            if move[0]:
                return move
    except:
        return [False]


def attack_pawns(pawns):
    possible_pawn_attacks = list()
    try:
        for p in pawns:
            attack = p.attack(board)
            if attack[0]:
                possible_pawn_attacks.append(attack)
        return possible_pawn_attacks
    except:
        return [False]


def best_pawn_attack():
    pawns = create_black_pawns()
    best_attack_list = attack_pawns(pawns)
    try:
        for a in best_attack_list:
            if a[0]:
                if a[1] == 'K':
                    return [a[2], a[3], a[4], a[6]]
                if a[1] == 'Q':
                    return [a[2], a[3], a[4], a[6]]
                if a[1] == 'R':
                    return [a[2], a[3], a[4], a[6]]
                if a[1] == 'B':
                    return [a[2], a[3], a[4], a[6]]
                if a[1] == 'H':
                    return [a[2], a[3], a[4], a[6]]
        return [False]
    except:
        return [False]
