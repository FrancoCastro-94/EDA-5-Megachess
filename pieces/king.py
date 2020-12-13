from pieces.piece import Piece


class WhiteKing(Piece):
    def __init__(self, row, col):
        Piece.__init__(self, row, col)

    def white_king_attack(self, board, attacks):
        white_forward_attack(attacks, board, self.row, self.col)
        white_back_attack(attacks, board, self.row, self.col)
        white_sides_attacks(attacks, board, self.row, self.col)
        return attacks

    def move(self, board):
        return king_move(board, self.row, self.col)


class BlackKing(Piece):
    def __init__(self, row, col):
        Piece.__init__(self, row, col)

    def black_king_attack(self, board, attacks):
        black_forward_attack(attacks, board, self.row, self.col)
        black_back_attack(attacks, board, self.row, self.col)
        black_sides_attacks(attacks, board, self.row, self.col)
        return attacks

    def move(self, board):
        return king_move(board, self.row, self.col)


def king_move(board, row, col):    # return first possible move
    if col - 1 >= 0 and board[row][col - 1] == ' ':  # check if movement is possible
        return [row, col, row, col - 1]
    if col + 1 <= 15 and board[row][col + 1] == ' ':
        return [row, col, row, col + 1]
    if row - 1 >= 0:
        if board[row - 1][col] == ' ':
            return [row, col, row - 1, col]
        if col - 1 >= 0 and board[row - 1][col - 1] == ' ':
            return [row, col, row - 1, col - 1]
        if col + 1 <= 15 and board[row - 1][col + 1] == ' ':
            return [row, col, row - 1, col + 1]
    if row + 1 <= 15:
        if board[row + 1][col] == ' ':
            return [row, col, row + 1, col]
        if col - 1 >= 0 and board[row + 1][col - 1] == ' ':
            return [row, col, row + 1, col - 1]
        if col + 1 <= 15 and board[row + 1][col + 1] == ' ':
            return [row, col, row + 1, col + 1]
    return False


def white_back_attack(attacks, board, row, col):
    if row + 1 <= 15:
        if board[row + 1][col].islower():      # add attack if it is possible
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
    return attacks


# -------------------------------------------------- Black ---------------------------------------------- #

def black_forward_attack(attacks, board, row, col):
    if row + 1 <= 15:
        if board[row + 1][col].isupper():  # check if attack is possible
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
    return attacks
