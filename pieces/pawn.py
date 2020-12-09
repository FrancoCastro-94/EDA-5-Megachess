from pieces.piece import Piece


def white_right_attack(attacks, board, row, col):
    if row - 1 < 0 or col + 1 > 15:
        return False
    if board[row - 1][col + 1].islower():
        attacks.append([board[row - 1][col + 1], row, col, row - 1, col + 1])
        return
    return False


def white_left_attack(attacks, board, row, col):
    if row - 1 < 0 or col - 1 < 0:
        return False
    if board[row - 1][col - 1].islower():
        attacks.append([board[row - 1][col - 1], row, col, row - 1, col - 1])
        return
    return False


def white_move_two(board, row, col):
    if board[row - 1][col] == ' ' and board[row - 2][col] == ' ':
        return [row, col, row - 2, col]
    return False


def white_move(board, row, col):
    if board[row - 1][col] == ' ':
        return [row, col, row - 1, col]
    return False


class WhitePawn(Piece):
    def __init__(self, row, col):
        Piece.__init__(self, row, col)

    def white_pawn_attack(self, board):
        attacks = list()
        white_left_attack(attacks, board, self.row, self.col)
        white_right_attack(attacks, board, self.row, self.col)
        if attacks:
            return attacks
        return False

    def move(self, board):
        if self.row > 11:
            return white_move_two(board, self.row, self.col)
        else:
            return white_move(board, self.row, self.col)


# ------------------------------------------------- WHITE PAWN ---------------------------------------------- #


def black_right_attack(attacks, board, row, col):
    if row + 1 > 15 or col + 1 > 15:
        return False
    if board[row + 1][col + 1].isupper():
        attacks.append([board[row + 1][col + 1], row, col, row + 1, col + 1])
        return
    return False


def black_left_attack(attacks, board, row, col):
    if row + 1 > 15 or col - 1 < 0:
        return False
    if board[row + 1][col - 1].isupper():
        attacks.append([board[row + 1][col - 1], row, col, row + 1, col - 1])
        return
    return False


def black_move_two(board, row, col):
    if board[row + 1][col] == ' ' and board[row + 2][col] == ' ':
        return [row, col, row + 2, col]
    return False


def black_move(board, row, col):
    if board[row + 1][col] == ' ':
        return [row, col, row + 1, col]
    return False


class BlackPawn(Piece):

    def __init__(self, row, col):
        Piece.__init__(self, row, col)

    def black_pawn_attack(self, board):
        attacks = list()
        black_left_attack(attacks, board, self.row, self.col)
        black_right_attack(attacks, board, self.row, self.col)
        if attacks:
            return attacks
        return False

    def move(self, board):
        if self.row < 4:
            return black_move_two(board, self.row, self.col)
        else:
            return black_move(board, self.row, self.col)
