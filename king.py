from pieces.piece import Piece


def black_forward_attack(attacks, board, row, col):
    if row + 1 <= 15:
        if board[row + 1][col].isupper():
            attacks.append([board[row + 1][col], row, col, row + 1, col])
        if col - 1 >= 0 and board[row + 1][col - 1].isupper():
            attacks.append([board[row + 1][col - 1], row, col, row + 1, col - 1])
        if col + 1 <= 15 and board[row + 1][col + 1].isupper():
            attacks.append([board[row + 1][col + 1], row, col, row + 1, col + 1])
    return attacks


def black_back_attack(attacks, board, row, col):
    if row - 1 >= 0:
        if board[row - 1][col].isupper():
            attacks.append([board[row - 1][col], row, col, row - 1, col])
        if col - 1 >= 0 and board[row - 1][col - 1].isupper():
            attacks.append([board[row - 1][col - 1], row, col, row - 1, col - 1])
        if col + 1 <= 15 and board[row - 1][col + 1].isupper():
            attacks.append([board[row - 1][col + 1], row, col, row - 1, col + 1])
    return attacks


def black_sides_attacks(attacks, board, row, col):
    if col - 1 >= 0 and board[row][col - 1].isupper():
        attacks.append([board[row][col - 1], row, col, row, col - 1])
    if col + 1 <= 15 and board[row][col + 1].isupper():
        attacks.append([board[row][col + 1], row, col, row, col + 1])
    return


def black_move(board, row, col):
    moves = list()
    if col - 1 >= 0 and board[row][col - 1] == ' ':
        moves.append([row, col, row, col - 1])
    if col + 1 <= 15 and board[row][col + 1] == ' ':
        moves.append([row, col, row, col + 1])
    if row + 1 <= 15:
        if board[row + 1][col] == ' ':
            moves.append([row, col, row + 1, col])
        if col - 1 >= 0 and board[row + 1][col - 1] == ' ':
            moves.append([row, col, row + 1, col - 1])
        if col + 1 <= 15 and board[row + 1][col + 1] == ' ':
            moves.append([row, col, row + 1, col + 1])
    if row - 1 >= 0:
        if board[row - 1][col] == ' ':
            moves.append([row, col, row - 1, col])
        if col - 1 >= 0 and board[row - 1][col - 1] == ' ':
            moves.append([row, col, row - 1, col - 1])
        if col + 1 <= 15 and board[row - 1][col + 1] == ' ':
            moves.append([row, col, row - 1, col + 1])
    return moves


class BlackKing(Piece):
    def __init__(self, row, col):
        Piece.__init__(self, row, col)

    def black_king_attack(self, board):
        attacks = list()
        black_forward_attack(attacks, board, self.row, self.col)
        black_back_attack(attacks, board, self.row, self.col)
        black_sides_attacks(attacks, board, self.row, self.col)
        if attacks:
            return attacks
        return False

    def move(self, board):
        king_move = black_move(board, self.row, self.col)
        return king_move[0]


# -------------------------------------------------- WHITE KING ---------------------------------------------- #
def white_back_attack(attacks, board, row, col):
    if row + 1 <= 15:
        if board[row + 1][col].islower():
            attacks.append([board[row + 1][col], row, col, row + 1, col])
        if col - 1 >= 0 and board[row + 1][col - 1].islower():
            attacks.append([board[row + 1][col - 1], row, col, row + 1, col - 1])
        if col + 1 <= 15 and board[row + 1][col + 1].islower():
            attacks.append([board[row + 1][col + 1], row, col, row + 1, col + 1])
    return attacks


def white_forward_attack(attacks, board, row, col):
    if row - 1 >= 0:
        if board[row - 1][col].islower():
            attacks.append([board[row - 1][col], row, col, row - 1, col])
        if col - 1 >= 0 and board[row - 1][col - 1].islower():
            attacks.append([board[row - 1][col - 1], row, col, row - 1, col - 1])
        if col + 1 <= 15 and board[row - 1][col + 1].islower():
            attacks.append([board[row - 1][col + 1], row, col, row - 1, col + 1])
    return attacks


def white_sides_attacks(attacks, board, row, col):
    if col - 1 >= 0 and board[row][col - 1].islower():
        attacks.append([board[row][col - 1], row, col, row, col - 1])
    if col + 1 <= 15 and board[row][col + 1].islower():
        attacks.append([board[row][col + 1], row, col, row, col + 1])
    return


class WhiteKing(Piece):
    def __init__(self, row, col):
        Piece.__init__(self, row, col)

    def white_king_attack(self, board):
        attacks = list()
        white_forward_attack(attacks, board, self.row, self.col)
        white_back_attack(attacks, board, self.row, self.col)
        white_sides_attacks(attacks, board, self.row, self.col)
        if attacks:
            return attacks
        return False
