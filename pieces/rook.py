from pieces.piece import Piece


class WhiteRook(Piece):
    def __init__(self, row, col):
        Piece.__init__(self, row, col)

    def white_rook_attack(self, board, attacks):
        white_forward_attack(attacks, board, self.row, self.col)
        white_back_attack(attacks, board, self.row, self.col)
        white_left_attack(attacks, board, self.row, self.col)
        white_right_attack(attacks, board, self.row, self.col)
        return attacks

    def moves(self, board):
        return rook_move(board, self.row, self.col)


class BlackRook(Piece):
    def __init__(self, row, col):
        Piece.__init__(self, row, col)

    def black_rook_attack(self, board, attacks):
        black_forward_attack(attacks, board, self.row, self.col)
        black_back_attack(attacks, board, self.row, self.col)
        black_left_attack(attacks, board, self.row, self.col)
        black_right_attack(attacks, board, self.row, self.col)
        return attacks

    def moves(self, board):
        return rook_move(board, self.row, self.col)


def rook_move(board, row, col):
    moves = list()
    for i in range(1, 16):
        if row + i <= 15 and board[row + i][col] == ' ':
            moves.append([row, col, row + i, col])
    for i in range(1, 16):
        if col + i <= 15 and board[row][col + i] == ' ':
            moves.append([row, col, row, col + i])
    for i in range(1, 16):
        if row - i >= 0 and board[row - i][col] == ' ':
            moves.append([row, col, row - i, col])
    for i in range(1, 16):
        if col - i >= 0 and board[row][col - i] == ' ':
            moves.append([row, col, row, col - i])
    return moves


def white_forward_attack(attacks, board, row, col):
    for i in range(1, 16):
        if row - i < 0 or board[row - i][col].isupper():    # verify if move is not possible
            return False
        if board[row - i][col].islower():    # add attack if it exists
            attacks.append([board[row - i][col], row, col, row - i, col])
            return attacks


def white_back_attack(attacks, board, row, col):
    for i in range(1, 16):
        if row + i > 15 or board[row + i][col].isupper():
            return False
        if board[row + i][col].islower():
            attacks.append([board[row + i][col], row, col, row + i, col])
            return attacks


def white_left_attack(attacks, board, row, col):
    for i in range(1, 16):
        if col - i < 0 or board[row][col - i].isupper():
            return False
        if board[row][col - i].islower():
            attacks.append([board[row][col - i], row, col, row, col - i])
            return attacks


def white_right_attack(attacks, board, row, col):
    for i in range(1, 16):
        if col + i > 15 or board[row][col + i].isupper():
            return False
        if board[row][col + i].islower():
            attacks.append([board[row][col + i], row, col, row, col + i])
            return attacks


# ------------------------------------------------ Black ---------------------------------------------------- #

def black_forward_attack(attacks, board, row, col):
    for i in range(1, 16):
        if row + i > 15 or board[row + i][col].islower():
            return False
        if board[row + i][col].isupper():
            attacks.append([board[row + i][col], row, col, row + i, col])
            return attacks


def black_back_attack(attacks, board, row, col):
    for i in range(1, 16):
        if row - i < 0 or board[row - i][col].islower():
            return False
        if board[row - i][col].isupper():
            attacks.append([board[row - i][col], row, col, row - i, col])
            return attacks


def black_left_attack(attacks, board, row, col):
    for i in range(1, 16):
        if col - i < 0 or board[row][col - i].islower():
            return False
        if board[row][col - i].isupper():
            attacks.append([board[row][col - i], row, col, row, col - i])
            return attacks


def black_right_attack(attacks, board, row, col):
    for i in range(1, 16):
        if col + i > 15 or board[row][col + i].islower():
            return False
        if board[row][col + i].isupper():
            attacks.append([board[row][col + i], row, col, row, col + i])
            return attacks
