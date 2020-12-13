from pieces.piece import Piece


class WhiteBishop(Piece):

    def __init__(self, row, col):
        Piece.__init__(self, row, col)

    def white_bishop_attack(self, board, attacks):
        white_forward_right(attacks, board, self.row, self.col)
        white_forward_left(attacks, board, self.row, self.col)
        white_back_right(attacks, board, self.row, self.col)
        white_back_left(attacks, board, self.row, self.col)
        return attacks

    def move(self, board):
        return bishop_move(board, self.row, self.col)


class BlackBishop(Piece):
    def __init__(self, row, col):
        Piece.__init__(self, row, col)

    def black_bishop_attack(self, board, attacks):
        black_forward_right(attacks, board, self.row, self.col)
        black_forward_left(attacks, board, self.row, self.col)
        black_back_right(attacks, board, self.row, self.col)
        black_back_left(attacks, board, self.row, self.col)
        return attacks

    def move(self, board):
        return bishop_move(board, self.row, self.col)


def bishop_move(board, row, col):  # return a list with all possible moves
    moves = list()
    for i in range(1, 16):
        if row + i <= 15 and col + i <= 15 and board[row + i][col + i] == ' ':
            moves.append([row, col, row + i, col + i])
    for i in range(1, 16):
        if row + i <= 15 and col - i >= 0 and board[row + i][col - i] == ' ':
            moves.append([row, col, row + i, col - i])
    for i in range(1, 16):
        if row - i >= 0 and col + i <= 15 and board[row - i][col + i] == ' ':
            moves.append([row, col, row - i, col + i])
    for i in range(1, 16):
        if row - i >= 0 and col - i >= 0 and board[row - i][col - i] == ' ':
            moves.append([row, col, row - i, col - i])
    return moves


def white_back_right(attacks, board, row, col):
    for i in range(1, 16):
        if row + i > 15 or col + i > 15 or board[row + i][col + i].isupper():    # verify if move is not possible
            return False
        if board[row + i][col + i].islower():     # add attack if it exists
            attacks.append([board[row + i][col + i], row, col, row + i, col + i])
            return attacks


def white_back_left(attacks, board, row, col):
    for i in range(1, 16):
        if row + i > 15 or col - i < 0 or board[row + i][col - i].isupper():
            return False
        if board[row + i][col - i].islower():
            attacks.append([board[row + i][col - i], row, col, row + i, col - i])
            return attacks


def white_forward_left(attacks, board, row, col):
    for i in range(1, 16):
        if row - i < 0 or col - i < 0 or board[row - i][col - i].isupper():
            return False
        if board[row - i][col - i].islower():
            attacks.append([board[row - i][col - i], row, col, row - i, col - i])
            return attacks


def white_forward_right(attacks, board, row, col):
    for i in range(1, 16):
        if row - i < 0 or col + i > 15 or board[row - i][col + i].isupper():
            return False
        if board[row - i][col + i].islower():
            attacks.append([board[row - i][col + i], row, col, row - i, col + i])
            return attacks


# ---------------------------------------- Black -------------------------------- #


def black_forward_right(attacks, board, row, col):
    for i in range(1, 16):
        if row + i > 15 or col + i > 15 or board[row + i][col + i].islower():
            return False
        if board[row + i][col + i].isupper():
            attacks.append([board[row + i][col + i], row, col, row + i, col + i])
            return attacks


def black_forward_left(attacks, board, row, col):
    for i in range(1, 16):
        if row + i > 15 or col - i < 0 or board[row + i][col - i].islower():
            return False
        if board[row + i][col - i].isupper():
            attacks.append([board[row + i][col - i], row, col, row + i, col - i])
            return attacks


def black_back_left(attacks, board, row, col):
    for i in range(1, 16):
        if row - i < 0 or col - i < 0 or board[row - i][col - i].islower():
            return False
        if board[row - i][col - i].isupper():
            attacks.append([board[row - i][col - i], row, col, row - i, col - i])
            return attacks


def black_back_right(attacks, board, row, col):
    for i in range(1, 16):
        if row - i < 0 or col + i > 15 or board[row - i][col + i].islower():
            return False
        if board[row - i][col + i].isupper():
            attacks.append([board[row - i][col + i], row, col, row - i, col + i])
            return attacks
