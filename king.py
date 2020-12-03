def black_one(board, row, col):
    if row - 1 < 0:
        return False
    if board[row - 1][col].isupper():
        return [board[row - 1][col], row, col, row - 1, col]
    return False


def black_two(board, row, col):
    if row - 1 < 0 or col + 1 > 15:
        return False
    if board[row - 1][col + 1].isupper():
        return [board[row - 1][col + 1], row, col, row - 1, col + 1]
    return False


def black_three(board, row, col):
    if col + 1 > 15:
        return False
    if board[row][col + 1].isupper():
        return [board[row][col + 1], row, col, row, col + 1]
    return False


def black_four(board, row, col):
    if row + 1 > 15 or col + 1 > 15:
        return False
    if board[row + 1][col + 1].isupper():
        return [board[row + 1][col + 1], row, col, row + 1, col + 1]
    return False


def black_five(board, row, col):
    if row + 1 > 15:
        return False
    if board[row + 1][col].isupper():
        return [board[row + 1][col], row, col, row + 1, col]
    return False


def black_six(board, row, col):
    if row + 1 > 15 or col - 1 < 0:
        return False
    if board[row + 1][col - 1].isupper():
        return [board[row + 1][col - 1], row, col, row + 1, col - 1]
    return False


def black_seven(board, row, col):
    if col - 1 < 0:
        return False
    if board[row][col - 1].isupper():
        return [board[row][col - 1], row, col, row, col - 1]
    return False


def black_eight(board, row, col):
    if row - 1 < 0 or col - 1 < 0:
        return False
    if board[row - 1][col - 1].isupper():
        return [board[row - 1][col - 1], row, col, row - 1, col - 1]
    return False


class BlackKing:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def black_king_attack(self, board):
        attacks = []
        one = black_one(board, self.row, self.col)
        two = black_two(board, self.row, self.col)
        three = black_three(board, self.row, self.col)
        four = black_four(board, self.row, self.col)
        five = black_five(board, self.row, self.col)
        six = black_six(board, self.row, self.col)
        seven = black_seven(board, self.row, self.col)
        eight = black_eight(board, self.row, self.col)
        if one:
            attacks.append(one)
        if two:
            attacks.append(two)
        if three:
            attacks.append(three)
        if four:
            attacks.append(four)
        if five:
            attacks.append(five)
        if six:
            attacks.append(six)
        if seven:
            attacks.append(seven)
        if eight:
            attacks.append(eight)
        if attacks:
            return attacks
        return False


# -------------------------------------------------- WHITE KING ---------------------------------------------- #

def white_one(board, row, col):
    if row - 1 < 0:
        return False
    if board[row - 1][col].islower():
        return [board[row - 1][col], row, col, row - 1, col]
    return False


def white_two(board, row, col):
    if row - 1 < 0 or col + 1 > 15:
        return False
    if board[row - 1][col + 1].islower():
        return [board[row - 1][col + 1], row, col, row - 1, col + 1]
    return False


def white_three(board, row, col):
    if col + 1 > 15:
        return False
    if board[row][col + 1].islower():
        return [board[row][col + 1], row, col, row, col + 1]
    return False


def white_four(board, row, col):
    if row + 1 > 15 or col + 1 > 15:
        return False
    if board[row + 1][col + 1].islower():
        return [board[row + 1][col + 1], row, col, row + 1, col + 1]
    return False


def white_five(board, row, col):
    if row + 1 > 15:
        return False
    if board[row + 1][col].islower():
        return [board[row + 1][col], row, col, row + 1, col]
    return False


def white_six(board, row, col):
    if row + 1 > 15 or col - 1 < 0:
        return False
    if board[row + 1][col - 1].islower():
        return [board[row + 1][col - 1], row, col, row + 1, col - 1]
    return False


def white_seven(board, row, col):
    if col - 1 < 0:
        return False
    if board[row][col - 1].islower():
        return [board[row][col - 1], row, col, row, col - 1]
    return False


def white_eight(board, row, col):
    if row - 1 < 0 or col - 1 < 0:
        return False
    if board[row - 1][col - 1].islower():
        return [board[row - 1][col - 1], row, col, row - 1, col - 1]
    return False


class WhiteKing:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def white_king_attack(self, board):
        attacks = []
        one = white_one(board, self.row, self.col)
        two = white_two(board, self.row, self.col)
        three = white_three(board, self.row, self.col)
        four = white_four(board, self.row, self.col)
        five = white_five(board, self.row, self.col)
        six = white_six(board, self.row, self.col)
        seven = white_seven(board, self.row, self.col)
        eight = white_eight(board, self.row, self.col)
        if one:
            attacks.append(one)
        if two:
            attacks.append(two)
        if three:
            attacks.append(three)
        if four:
            attacks.append(four)
        if five:
            attacks.append(five)
        if six:
            attacks.append(six)
        if seven:
            attacks.append(seven)
        if eight:
            attacks.append(eight)
        if attacks:
            return attacks
        return False
