def forward_black_attack(board, row, col):
    for i in range(1, 15):
        if row + i > 15:
            return False
        if board[row + i][col].islower():
            return False
        if board[row + i][col].isupper():
            return [board[row + i][col], row, col, row + i, col]
    return False


def back_black_attack(board, row, col):
    for i in range(1, 15):
        if row - i < 0:
            return False
        if board[row - i][col].islower():
            return False
        if board[row - i][col].isupper():
            return [board[row - i][col], row, col, row - i, col]
    return False


def left_black_attack(board, row, col):
    for i in range(1, 15):
        if col - i < 0:
            return False
        if board[row][col - i].islower():
            return False
        if board[row][col - i].isupper():
            return [board[row][col - i], row, col, row, col - i]
    return False


def right_black_attack(board, row, col):
    for i in range(1, 15):
        if col + i > 15:
            return False
        if board[row][col + i].islower():
            return False
        if board[row][col + i].isupper():
            return [board[row][col + i], row, col, row, col + i]
    return False


class BlackRook:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def black_rook_attack(self, board):
        forward = forward_black_attack(board, self.row, self.col)
        back = back_black_attack(board, self.row, self.col)
        left = left_black_attack(board, self.row, self.col)
        right = right_black_attack(board, self.row, self.col)
        possibleAttack = []
        if forward:
            possibleAttack.append(forward)
        if back:
            possibleAttack.append(back)
        if left:
            possibleAttack.append(left)
        if right:
            possibleAttack.append(right)
        if possibleAttack:
            return possibleAttack
        return False


# ------------------------------------------------ WHITE ROOK ---------------------------------------------------- #

def forward_white_attack(board, row, col):
    for i in range(1, 15):
        if row + i > 15:
            return False
        if board[row + i][col].isupper():
            return False
        if board[row + i][col].islower():
            return [board[row + i][col], row, col, row + i, col]
    return False


def back_white_attack(board, row, col):
    for i in range(1, 15):
        if row - i < 0:
            return False
        if board[row - i][col].isupper():
            return False
        if board[row - i][col].islower():
            return [board[row - i][col], row, col, row - i, col]
    return False


def left_white_attack(board, row, col):
    for i in range(1, 15):
        if col - i < 0:
            return False
        if board[row][col - i].isupper():
            return False
        if board[row][col - i].islower():
            return [board[row][col - i], row, col, row, col - i]
    return False


def right_white_attack(board, row, col):
    for i in range(1, 15):
        if col + i > 15:
            return False
        if board[row][col + i].isupper():
            return False
        if board[row][col + i].islower():
            return [board[row][col + i], row, col, row, col + i]
    return False


class WhiteRook:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def white_rook_attack(self, board):
        forward = forward_white_attack(board, self.row, self.col)
        back = back_white_attack(board, self.row, self.col)
        left = left_white_attack(board, self.row, self.col)
        right = right_white_attack(board, self.row, self.col)
        possibleAttack = []
        if forward:
            possibleAttack.append(forward)
        if back:
            possibleAttack.append(back)
        if left:
            possibleAttack.append(left)
        if right:
            possibleAttack.append(right)
        if possibleAttack:
            return possibleAttack
        return False
