def black_forward_right(board, row, col):
    try:
        for i in range(1, 16):
            if row + i == 16 or col + i == 16:
                return False
            if board[row + i][col + i].islower():
                return False
            if board[row + i][col + i].isupper():
                return [board[row + i][col + i], row, col, row + i, col + i]
    except:
        return False


def black_forward_left(board, row, col):
    try:
        for i in range(1, 16):
            if row + i == 16 or col - i == -1:
                return False
            if board[row + i][col - i].islower():
                return False
            if board[row + i][col - i].isupper():
                return [board[row + i][col - i], row, col, row + i, col - i]
    except:
        return False


def black_back_left(board, row, col):
    try:
        for i in range(1, 16):
            if row - i == -1 or col - i == -1:
                return False
            if board[row - i][col - i].islower():
                return False
            if board[row - i][col - i].isupper():
                return [board[row - i][col - i], row, col, row - i, col - i]
    except:
        return False


def black_back_right(board, row, col):
    try:
        for i in range(1, 16):
            if row - i == -1 or col + i == 16:
                return False
            if board[row - i][col + i].islower():
                return False
            if board[row - i][col + i].isupper():
                return [board[row - i][col + i], row, col, row - i, col + i]
    except:
        return False


class BlackBishop:

    def __init__(self, row, col):
        self.row = row
        self.col = col

    def black_bishop_attack(self, board):
        forward_right = black_forward_right(board, self.row, self.col)
        forward_left = black_forward_left(board, self.row, self.col)
        back_right = black_back_right(board, self.row, self.col)
        back_left = black_back_left(board, self.row, self.col)
        possibleAttack = []
        if forward_right:
            possibleAttack.append(forward_right)
        if forward_left:
            possibleAttack.append(forward_left)
        if back_right:
            possibleAttack.append(back_right)
        if back_left:
            possibleAttack.append(back_left)
        if possibleAttack:
            return possibleAttack
        return False


# ----------------------------------------WHITE-------------------------------- #

def white_back_right(board, row, col):
    try:
        for i in range(1, 16):
            if row + i == 16 or col + i == 16:
                return False
            if board[row + i][col + i].isupper():
                return False
            if board[row + i][col + i].islower():
                return [board[row + i][col + i], row, col, row + i, col + i]
    except:
        return False


def white_back_left(board, row, col):
    try:
        for i in range(1, 16):
            if row + i == 16 or col - i == -1:
                return False
            if board[row + i][col - i].isupper():
                return False
            if board[row + i][col - i].islower():
                return [board[row + i][col - i], row, col, row + i, col - i]
    except:
        return False


def white_forward_left(board, row, col):
    try:
        for i in range(1, 16):
            if row - i == -1 or col - i == -1:
                return False
            if board[row - i][col - i].isupper():
                return False
            if board[row - i][col - i].islower():
                return [board[row - i][col - i], row, col, row - i, col - i]
    except:
        return False


def white_forward_right(board, row, col):
    try:
        for i in range(1, 16):
            if row - i == -1 or col + i == 16:
                return False
            if board[row - i][col + i].isupper():
                return False
            if board[row - i][col + i].islower():
                return [board[row - i][col + i], row, col, row - i, col + i]
    except:
        return False


class WhiteBishop:

    def __init__(self, row, col):
        self.row = row
        self.col = col

    def white_bishop_attack(self, board):
        forward_right = white_forward_right(board, self.row, self.col)
        forward_left = white_forward_left(board, self.row, self.col)
        back_right = white_back_right(board, self.row, self.col)
        back_left = white_back_left(board, self.row, self.col)
        possibleAttack = []
        if forward_right:
            possibleAttack.append(forward_right)
        if forward_left:
            possibleAttack.append(forward_left)
        if back_right:
            possibleAttack.append(back_right)
        if back_left:
            possibleAttack.append(back_left)
        if possibleAttack:
            return possibleAttack
        return False
