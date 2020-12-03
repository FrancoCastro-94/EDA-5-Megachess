def black_horse_move(board, row, col):
    if row > 15 < 0 or col > 15 < 0:
        return False
    if board[row][col] == ' ':
        return [row, col]


def black_attack_one(board, row, col):
    if row + 2 > 15 or col - 1 < 0:
        return False
    if board[row + 2][col - 1].isupper():
        return [board[row + 2][col - 1], row, col, row + 2, col - 1]
    return False


def black_attack_two(board, row, col):
    if row + 2 > 15 or col + 1 > 15:
        return False
    if board[row + 2][col + 1].isupper():
        return [board[row + 2][col + 1], row, col, row + 2, col + 1]
    return False


def black_attack_three(board, row, col):
    if row + 1 > 15 or col + 2 > 15:
        return False
    if board[row + 1][col + 2].isupper():
        return [board[row + 1][col + 2], row, col, row + 1, col + 2]
    return False


def black_attack_four(board, row, col):
    if row - 1 < 0 or col + 2 > 15:
        return False
    if board[row - 1][col + 2].isupper():
        return [board[row - 1][col + 2], row, col, row - 1, col + 2]
    return False


def black_attack_five(board, row, col):
    if row - 2 < 0 or col + 1 > 16:
        return False
    if board[row - 2][col + 1].isupper():
        return [board[row - 2][col + 1], row, col, row - 2, col + 1]
    return False


def black_attack_six(board, row, col):
    if row - 2 < 0 or col - 1 < 0:
        return False
    if board[row - 2][col - 1].isupper():
        return [board[row - 2][col - 1], row, col, row - 2, col - 1]
    return False


def black_attack_seven(board, row, col):
    if row - 1 < 0 or col - 2 < 0:
        return False
    if board[row - 1][col - 2].isupper():
        return [board[row - 1][col - 2], row, col, row - 1, col - 2]
    return False


def black_attack_eight(board, row, col):
    if row + 1 > 15 or col - 2 < 0:
        return False
    if board[row + 1][col - 2].isupper():
        return [board[row + 1][col - 2], row, col, row + 1, col - 2]
    return False


class BlackHorse:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def black_horse_attack(self, board):
        attacks = []
        one = black_attack_one(board, self.row, self.col)
        two = black_attack_two(board, self.row, self.col)
        three = black_attack_three(board, self.row, self.col)
        four = black_attack_four(board, self.row, self.col)
        five = black_attack_five(board, self.row, self.col)
        six = black_attack_six(board, self.row, self.col)
        seven = black_attack_seven(board, self.row, self.col)
        eight = black_attack_eight(board, self.row, self.col)
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


# ------------------------------------------------------ WHITE ------------------------------------------------------ #

def white_horse_move(board, row, col):
    if row > 15 < 0 or col > 15 < 0:
        return False
    if board[row][col] == ' ':
        return [row, col]


def white_attack_one(board, row, col):
    if row + 2 > 15 or col - 1 < 0:
        return False
    if board[row + 2][col - 1].islower():
        return [board[row + 2][col - 1], row, col, row + 2, col - 1]
    return False


def white_attack_two(board, row, col):
    if row + 2 > 15 or col + 1 > 15:
        return False
    if board[row + 2][col + 1].islower():
        return [board[row + 2][col + 1], row, col, row + 2, col + 1]
    return False


def white_attack_three(board, row, col):
    if row + 1 > 15 or col + 2 > 15:
        return False
    if board[row + 1][col + 2].islower():
        return [board[row + 1][col + 2], row, col, row + 1, col + 2]
    return False


def white_attack_four(board, row, col):
    if row - 1 < 0 or col + 2 > 15:
        return False
    if board[row - 1][col + 2].islower():
        return [board[row - 1][col + 2], row, col, row - 1, col + 2]
    return False


def white_attack_five(board, row, col):
    if row - 2 < 0 or col + 1 > 15:
        return False
    if board[row - 2][col + 1].islower():
        return [board[row - 2][col + 1], row, col, row - 2, col + 1]
    return False


def white_attack_six(board, row, col):
    if row - 2 < 0 or col - 1 < 0:
        return False
    if board[row - 2][col - 1].islower():
        return [board[row - 2][col - 1], row, col, row - 2, col - 1]
    return False


def white_attack_seven(board, row, col):
    if row - 1 < 0 or col - 2 < 0:
        return False
    if board[row - 1][col - 2].islower():
        return [board[row - 1][col - 2], row, col, row - 1, col - 2]
    return False


def white_attack_eight(board, row, col):
    if row + 1 > 15 or col - 2 < 0:
        return False
    if board[row + 1][col - 2].islower():
        return [board[row + 1][col - 2], row, col, row + 1, col - 2]
    return False


class WhiteHorse:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def white_horse_attack(self, board):
        attacks = []
        one = white_attack_one(board, self.row, self.col)
        two = white_attack_two(board, self.row, self.col)
        three = white_attack_three(board, self.row, self.col)
        four = white_attack_four(board, self.row, self.col)
        five = white_attack_five(board, self.row, self.col)
        six = white_attack_six(board, self.row, self.col)
        seven = white_attack_seven(board, self.row, self.col)
        eight = white_attack_eight(board, self.row, self.col)
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
