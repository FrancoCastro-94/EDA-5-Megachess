def black_forward_right(attacks, board, row, col):
    for i in range(1, 15):
        if row + i > 15 or col + i > 15 or board[row + i][col + i].islower():
            return False
        if board[row + i][col + i].isupper():
            attacks.append([board[row + i][col + i], row, col, row + i, col + i])
    return False


def black_forward_left(attacks, board, row, col):
    for i in range(1, 15):
        if row + i > 15 or col - i < 0 or board[row + i][col - i].islower():
            return False
        if board[row + i][col - i].isupper():
            attacks.append([board[row + i][col - i], row, col, row + i, col - i])
    return False


def black_back_left(attacks, board, row, col):
    for i in range(1, 15):
        if row - i < 0 or col - i < 0 or board[row - i][col - i].islower():
            return False
        if board[row - i][col - i].isupper():
            attacks.append([board[row - i][col - i], row, col, row - i, col - i])
    return False


def black_back_right(attacks, board, row, col):
    for i in range(1, 15):
        if row - i < 0 or col + i > 15 or board[row - i][col + i].islower():
            return False
        if board[row - i][col + i].isupper():
            attacks.append([board[row - i][col + i], row, col, row - i, col + i])
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


class WhiteBishop:

    def __init__(self, row, col):
        self.row = row
        self.col = col

    def white_bishop_attack(self, board):
        attacks = []
        white_forward_right(attacks, board, self.row, self.col)
        white_forward_left(attacks, board, self.row, self.col)
        white_back_right(attacks, board, self.row, self.col)
        white_back_left(attacks, board, self.row, self.col)
        if attacks:
            return attacks
        return False
