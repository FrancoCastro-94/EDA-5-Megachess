def white_right_attack(board, row, col):
    if row - 1 < 0 or col + 1 > 15:
        return False
    if board[row - 1][col + 1].islower():
        return [board[row - 1][col + 1], row, col, row - 1, col + 1]
    return False


def white_left_attack(board, row, col):
    if row - 1 < 0 or col - 1 < 0:
        return False
    if board[row - 1][col - 1].islower():
        return [board[row - 1][col - 1], row, col, row - 1, col - 1]
    return False


def white_move_two(board, row, col):
    if board[row - 1][col] == ' ' and board[row - 2][col] == ' ':
        return [row, col, row - 2, col]
    return False


def white_move(board, row, col):
    if board[row - 1][col] == ' ':
        return [row, col, row - 1, col]
    return False


class WhitePawn:

    def __init__(self, row, col):
        self.col = col
        self.row = row

    def white_pawn_attack(self, board):
        left = white_left_attack(board, self.row, self.col)
        right = white_right_attack(board, self.row, self.col)
        possibleAttack = []
        if left:
            possibleAttack.append(left)
        if right:
            possibleAttack.append(right)
        if possibleAttack:
            return possibleAttack
        else:
            return False

    def move(self, board):
        if self.row > 11:
            return white_move_two(board, self.row, self.col)
        else:
            return white_move(board, self.row, self.col)



# ------------------------------------------------- WHITE PAWN ---------------------------------------------- #

def black_right_attack(board, row, col):
    if row + 1 > 15 or col + 1 > 15:
        return False
    if board[row + 1][col + 1].isupper():
        return [board[row + 1][col + 1], row, col, row + 1, col + 1]
    return False


def black_left_attack(board, row, col):
    if row + 1 > 15 or col - 1 < 0:
        return False
    if board[row + 1][col - 1].isupper():
        return [board[row + 1][col - 1], row, col, row + 1, col - 1]
    return False


def black_move_two(board, row, col):
    if board[row + 1][col] == ' ' and board[row + 2][col] == ' ':
        return [row, col, row + 2, col]
    return False


def black_move(board, row, col):
    if board[row + 1][col] == ' ':
        return [row, col, row + 1, col]
    else:
        return False


class BlackPawn:

    def __init__(self, row, col):
        self.col = col
        self.row = row

    def black_pawn_attack(self, board):
        left = black_left_attack(board, self.row, self.col)
        right = black_right_attack(board, self.row, self.col)
        possibleAttack = []
        if left:
            possibleAttack.append(left)
        if right:
            possibleAttack.append(right)
        if possibleAttack:
            return possibleAttack
        else:
            return False

    def move(self, board):
        if self.row < 4:
            return black_move_two(board, self.row, self.col)
        else:
            return black_move(board, self.row, self.col)

