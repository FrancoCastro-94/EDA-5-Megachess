from pieces.piece import Piece


def black_attack_forward(attacks, board, row, col):
    if row + 2 <= 15:
        if col - 1 >= 0 and board[row + 2][col - 1].isupper():
            attacks.append([board[row + 2][col - 1], row, col, row + 2, col - 1])
        if col + 1 <= 15 and board[row + 2][col + 1].isupper():
            attacks.append([board[row + 2][col + 1], row, col, row + 2, col + 1])
    return attacks


def black_attack_right(attacks, board, row, col):
    if col + 2 <= 15:
        if row + 1 <= 15 and board[row + 1][col + 2].isupper():
            attacks.append([board[row + 1][col + 2], row, col, row + 1, col + 2])
        if row - 1 >= 0 and board[row - 1][col + 2].isupper():
            attacks.append([board[row - 1][col + 2], row, col, row - 1, col + 2])
    return attacks


def black_attack_back(attacks, board, row, col):
    if row - 2 >= 0:
        if col + 1 <= 15 and board[row - 2][col + 1].isupper():
            attacks.append([board[row - 2][col + 1], row, col, row - 2, col + 1])
        if col - 1 >= 0 and board[row - 2][col - 1].isupper():
            attacks.append([board[row - 2][col - 1], row, col, row - 2, col - 1])
    return attacks


def black_attack_left(attacks, board, row, col):
    if col - 2 >= 0:
        if row + 1 <= 15 and board[row + 1][col - 2].isupper():
            attacks.append([board[row + 1][col - 2], row, col, row + 1, col - 2])
        if row - 1 >= 0 and board[row - 1][col - 2].isupper():
            attacks.append([board[row - 1][col - 2], row, col, row - 1, col - 2])
    return attacks


def black_move(board, row, col):
    moves = list()
    if row + 2 <= 15:
        if col - 1 >= 0 and board[row + 2][col - 1] == ' ':
            moves.append([row, col, row + 2, col - 1])
        if col + 1 <= 15 and board[row + 2][col + 1] == ' ':
            moves.append([row, col, row + 2, col + 1])
    if col + 2 <= 15:
        if row + 1 <= 15 and board[row + 1][col + 2] == ' ':
            moves.append([row, col, row + 1, col + 2])
        if row - 1 >= 0 and board[row - 1][col + 2] == ' ':
            moves.append([row, col, row - 1, col + 2])
    if col - 2 >= 0:
        if row + 1 <= 15 and board[row + 1][col - 2] == ' ':
            moves.append([row, col, row + 1, col - 2])
        if row - 1 >= 0 and board[row - 1][col - 2] == ' ':
            moves.append([row, col, row - 1, col - 2])
    if row - 2 >= 0:
        if col - 1 >= 0 and board[row - 2][col - 1] == ' ':
            moves.append([row, col, row - 2, col - 1])
        if col + 1 <= 15 and board[row - 2][col + 1] == ' ':
            moves.append([row, col, row - 2, col + 1])
    return moves


class BlackHorse(Piece):
    def __init__(self, row, col):
        Piece.__init__(self, row, col)

    def black_horse_move(self, board):
        move = black_move(board, self.row, self.col)
        if move:
            return move
        return False

    def black_horse_attack(self, board):
        attacks = list()
        black_attack_forward(attacks, board, self.row, self.col)
        black_attack_right(attacks, board, self.row, self.col)
        black_attack_back(attacks, board, self.row, self.col)
        black_attack_left(attacks, board, self.row, self.col)
        if attacks:
            return attacks
        return False


# ------------------------------------------------------ WHITE ------------------------------------------------------ #
def white_attack_back(attacks, board, row, col):
    if row + 2 <= 15:
        if col - 1 >= 0 and board[row + 2][col - 1].islower():
            attacks.append([board[row + 2][col - 1], row, col, row + 2, col - 1])
        if col + 1 <= 15 and board[row + 2][col + 1].islower():
            attacks.append([board[row + 2][col + 1], row, col, row + 2, col + 1])
    return attacks


def white_attack_right(attacks, board, row, col):
    if col + 2 <= 15:
        if row + 1 <= 15 and board[row + 1][col + 2].islower():
            attacks.append([board[row + 1][col + 2], row, col, row + 1, col + 2])
        if row - 1 >= 0 and board[row - 1][col + 2].islower():
            attacks.append([board[row - 1][col + 2], row, col, row - 1, col + 2])
    return attacks


def white_attack_forward(attacks, board, row, col):
    if row - 2 >= 0:
        if col + 1 <= 15 and board[row - 2][col + 1].islower():
            attacks.append([board[row - 2][col + 1], row, col, row - 2, col + 1])
        if col - 1 >= 0 and board[row - 2][col - 1].islower():
            attacks.append([board[row - 2][col - 1], row, col, row - 2, col - 1])
    return attacks


def white_attack_left(attacks, board, row, col):
    if col - 2 >= 0:
        if row - 1 >= 0 and board[row - 1][col - 2].islower():
            attacks.append([board[row - 1][col - 2], row, col, row - 1, col - 2])
        if row + 1 <= 15 and board[row + 1][col - 2].islower():
            attacks.append([board[row + 1][col - 2], row, col, row + 1, col - 2])
    return attacks


def white_move(board, row, col):
    moves = list()
    if row - 2 >= 0:
        if col - 1 >= 0 and board[row - 2][col - 1] == ' ':
            moves.append([row, col, row - 2, col - 1])
        if col + 1 <= 15 and board[row - 2][col + 1] == ' ':
            moves.append([row, col, row - 2, col + 1])
    if col + 2 <= 15:
        if row + 1 <= 15 and board[row + 1][col + 2] == ' ':
            moves.append([row, col, row + 1, col + 2])
        if row - 1 >= 0 and board[row - 1][col + 2] == ' ':
            moves.append([row, col, row - 1, col + 2])
    if col - 2 >= 0:
        if row + 1 <= 15 and board[row + 1][col - 2] == ' ':
            moves.append([row, col, row + 1, col - 2])
        if row - 1 >= 0 and board[row - 1][col - 2] == ' ':
            moves.append([row, col, row - 1, col - 2])
    if row + 2 <= 15:
        if col - 1 >= 0 and board[row + 2][col - 1] == ' ':
            moves.append([row, col, row + 2, col - 1])
        if col + 1 <= 15 and board[row + 2][col + 1] == ' ':
            moves.append([row, col, row + 2, col + 1])
    return moves


class WhiteHorse(Piece):
    def __init__(self, row, col):
        Piece.__init__(self, row, col)

    def white_horse_move(self, board):
        move = white_move(board, self.row, self.col)
        if move:
            return move
        return False

    def white_horse_attack(self, board):
        attacks = list()
        white_attack_back(attacks, board, self.row, self.col)
        white_attack_right(attacks, board, self.row, self.col)
        white_attack_forward(attacks, board, self.row, self.col)
        white_attack_left(attacks, board, self.row, self.col)
        if attacks:
            return attacks
        return False