def white_right_attack(board, row, col):
    try:
        if board[row - 1][col + 1].islower():
            return [board[row - 1][col + 1], row, col, row - 1, col + 1]
    except:
        return False


def white_left_attack(board, row, col):
    try:
        if board[row - 1][col - 1].islower():
            return [board[row - 1][col - 1], row, col, row - 1, col - 1]
    except:
        return False


def white_move_two(board, row, col, is_first_move):
    if is_first_move:
        if board[row - 1][col] == ' ' and board[row - 2][col] == ' ':
            return [row, col, row - 2, col]
    return False


def white_move(board, row, col):
    if board[row - 1][col] == ' ':
        return [row, col, row - 1, col]
    else:
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

    def move_two(self, board, is_first_move):
        return white_move_two(board, self.row, self.col, is_first_move)

    def move(self, board):
        return white_move(board, self.row, self.col)


# --------------------------------------------------------------------

def black_right_attack(board, row, col):
    try:
        if board[row + 1][col + 1].isupper():
            return [board[row + 1][col + 1], row, col, row + 1, col + 1]
    except:
        return False


def black_left_attack(board, row, col):
    try:
        if board[row + 1][col - 1].isupper():
            return [board[row + 1][col - 1], row, col, row + 1, col - 1]
    except:
        return False


def black_move_two(board, row, col, is_first_move):
    if is_first_move:
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

    def move_two(self, board, is_first_move):
        return black_move_two(board, self.row, self.col, is_first_move)

    def move(self, board):
        return black_move(board, self.row, self.col)
