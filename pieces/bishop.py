from pieces.piece import Piece


def bishop_move(board, row, col):
    moves = list()
    for i in range(1, 15):
        if row + i <= 15 and col + i <= 15 and board[row + i][col + i] == ' ':
            moves.append([row, col, row + i, col + i])
    for i in range(1, 15):
        if row + i <= 15 and col - i >= 0 and board[row + i][col - i] == ' ':
            moves.append([row, col, row + i, col - i])
    for i in range(1, 15):
        if row - i >= 0 and col + i <= 15 and board[row - i][col + i] == ' ':
            moves.append([row, col, row - i, col + i])
    for i in range(1, 15):
        if row - i >= 0 and col - i >= 0 and board[row - i][col - i] == ' ':
            moves.append([row, col, row - i, col - i])
    return moves


def black_forward_right(attacks, board, row, col):
    for i in range(1, 15):
        if row + i > 15 or col + i > 15 or board[row + i][col + i].islower():
            return False
        if board[row + i][col + i].isupper():
            attacks.append([board[row + i][col + i], row, col, row + i, col + i])
            return


def black_forward_left(attacks, board, row, col):
    for i in range(1, 15):
        if row + i > 15 or col - i < 0 or board[row + i][col - i].islower():
            return False
        if board[row + i][col - i].isupper():
            attacks.append([board[row + i][col - i], row, col, row + i, col - i])
            return


def black_back_left(attacks, board, row, col):
    for i in range(1, 15):
        if row - i < 0 or col - i < 0 or board[row - i][col - i].islower():
            return False
        if board[row - i][col - i].isupper():
            attacks.append([board[row - i][col - i], row, col, row - i, col - i])
            return


def black_back_right(attacks, board, row, col):
    for i in range(1, 15):
        if row - i < 0 or col + i > 15 or board[row - i][col + i].islower():
            return False
        if board[row - i][col + i].isupper():
            attacks.append([board[row - i][col + i], row, col, row - i, col + i])
            return


class BlackBishop(Piece):
    def __init__(self, row, col):
        Piece.__init__(self, row, col)

    def black_bishop_attack(self, board):
        attacks = list()
        black_forward_right(attacks, board, self.row, self.col)
        black_forward_left(attacks, board, self.row, self.col)
        black_back_right(attacks, board, self.row, self.col)
        black_back_left(attacks, board, self.row, self.col)
        if attacks:
            return attacks
        return False

    def move(self, board):
        return bishop_move(board, self.row, self.col)


# ----------------------------------------WHITE-------------------------------- #

def white_back_right(attacks, board, row, col):
    for i in range(1, 15):
        if row + i > 15 or col + i > 15 or board[row + i][col + i].isupper():
            return False
        if board[row + i][col + i].islower():
            attacks.append([board[row + i][col + i], row, col, row + i, col + i])
            return


def white_back_left(attacks, board, row, col):
    for i in range(1, 15):
        if row + i > 15 or col - i < 0 or board[row + i][col - i].isupper():
            return False
        if board[row + i][col - i].islower():
            attacks.append([board[row + i][col - i], row, col, row + i, col - i])
            return


def white_forward_left(attacks, board, row, col):
    for i in range(1, 15):
        if row - i < 0 or col - i < 0 or board[row - i][col - i].isupper():
            return False
        if board[row - i][col - i].islower():
            attacks.append([board[row - i][col - i], row, col, row - i, col - i])
            return


def white_forward_right(attacks, board, row, col):
    for i in range(1, 15):
        if row - i < 0 or col + i > 15 or board[row - i][col + i].isupper():
            return False
        if board[row - i][col + i].islower():
            attacks.append([board[row - i][col + i], row, col, row - i, col + i])
            return


class WhiteBishop(Piece):

    def __init__(self, row, col):
        Piece.__init__(self, row, col)

    def white_bishop_attack(self, board):
        attacks = list()
        white_forward_right(attacks, board, self.row, self.col)
        white_forward_left(attacks, board, self.row, self.col)
        white_back_right(attacks, board, self.row, self.col)
        white_back_left(attacks, board, self.row, self.col)
        if attacks:
            return attacks
        return False

    def move(self, board):
        return bishop_move(board, self.row, self.col)
