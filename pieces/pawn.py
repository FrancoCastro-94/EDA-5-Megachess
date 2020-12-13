from pieces.piece import Piece


class WhitePawn(Piece):
    def __init__(self, row, col):
        Piece.__init__(self, row, col)

    def white_pawn_attack(self, board, attacks):     # add the possible attacks to the 'attacks' list
        white_left_attack(attacks, board, self.row, self.col)
        white_right_attack(attacks, board, self.row, self.col)
        return attacks

    def move(self, board):
        if self.row > 11:
            return white_move_two(board, self.row, self.col)
        else:
            return white_move(board, self.row, self.col)


class BlackPawn(Piece):

    def __init__(self, row, col):
        Piece.__init__(self, row, col)

    def black_pawn_attack(self, board, attacks):
        black_left_attack(attacks, board, self.row, self.col)
        black_right_attack(attacks, board, self.row, self.col)
        return attacks

    def move(self, board):
        if self.row < 4:
            return black_move_two(board, self.row, self.col)
        else:
            return black_move(board, self.row, self.col)


def white_right_attack(attacks, board, row, col):
    if row - 1 >= 0 and col + 1 <= 15:     # verify if move is in the table
        if board[row - 1][col + 1].islower():     # add the possible attacks to the 'attacks' list
            attacks.append([board[row - 1][col + 1], row, col, row - 1, col + 1])
            return


def white_left_attack(attacks, board, row, col):
    if row - 1 >= 0 and col - 1 >= 0:
        if board[row - 1][col - 1].islower():
            attacks.append([board[row - 1][col - 1], row, col, row - 1, col - 1])
            return


def white_move_two(board, row, col):
    if board[row - 1][col] == ' ' and board[row - 2][col] == ' ':
        return [row, col, row - 2, col]
    return False


def white_move(board, row, col):
    if board[row - 1][col] == ' ':
        return [row, col, row - 1, col]
    return False


# ------------------------------------------------- Black ---------------------------------------------- #

def black_right_attack(attacks, board, row, col):
    if row + 1 <= 15 and col + 1 <= 15:
        if board[row + 1][col + 1].isupper():
            attacks.append([board[row + 1][col + 1], row, col, row + 1, col + 1])
            return attacks


def black_left_attack(attacks, board, row, col):
    if row + 1 <= 15 and col - 1 >= 0:
        if board[row + 1][col - 1].isupper():
            attacks.append([board[row + 1][col - 1], row, col, row + 1, col - 1])
            return attacks


def black_move_two(board, row, col):
    if board[row + 1][col] == ' ' and board[row + 2][col] == ' ':
        return [row, col, row + 2, col]
    return False


def black_move(board, row, col):
    if board[row + 1][col] == ' ':
        return [row, col, row + 1, col]
    return False
