def forward_black_attack(board, row, col):
    try:
        for i in range(1, 16):
            if row + i == 16:
                return False
            if board[row + i][col].islower():
                return False
            if board[row + i][col].isupper():
                return [board[row + i][col], row, col, row + i, col]
    except:
        return False


def back_black_attack(board, row, col):
    try:
        for i in range(1, 16):
            if row - i == -1:
                return False
            if board[row - i][col].islower():
                return False
            if board[row - i][col].isupper():
                return [board[row - i][col], row, col, row - i, col]
    except:
        return False


def left_black_attack(board, row, col):
    try:
        for i in range(1, 16):
            if col - i == -1:
                return False
            if board[row][col - i].islower():
                return False
            if board[row][col - i].isupper():
                return [board[row - i][col], row, col, row, col - i]
    except:
        return False


def right_black_attack(board, row, col):
    try:
        for i in range(1, 16):
            if col + i == 16:
                return False
            if board[row][col + i].islower():
                return False
            if board[row][col + i].isupper():
                return [board[row][col + i], row, col, row, col + i]
    except:
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

def back_white_attack(board, row, col):
    try:
        for i in range(1, 16):
            if row + i == 16:
                return False
            if board[row + i][col].isupper():
                return False
            if board[row + i][col].islower():
                return [board[row + i][col], row, col, row + i, col]
    except:
        return False


def forward_white_attack(board, row, col):
    try:
        for i in range(1, 16):
            if row - i == -1:
                return False
            if board[row - i][col].isupper():
                return False
            if board[row - i][col].islower():
                return [board[row - i][col], row, col, row - i, col]
    except:
        return False


def left_white_attack(board, row, col):
    try:
        for i in range(1, 16):
            if col - i == -1:
                return False
            if board[row][col - i].isupper():
                return False
            if board[row][col - i].islower():
                return [board[row][col - i], row, col, row, col - i]
    except:
        return False


def right_white_attack(board, row, col):
    try:
        for i in range(1, 16):
            if col + i == 16:
                return False
            if board[row][col + i].isupper():
                return False
            if board[row][col + i].islower():
                return [board[row][col + i], row, col, row, col + i]
    except:
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
