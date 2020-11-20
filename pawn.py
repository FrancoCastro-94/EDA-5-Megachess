
def blackRightkAttack(tablero, row, col):
    try:
        if tablero[row + 1][col + 1].isupper:
            return [True, tablero[row + 1][col + 1], row, col, row + 1, col + 1]
    except:
        return[False]

def blackLeftAttack(tablero, row, col):
    try:
        if tablero[row + 1][col - 1].isupper:
            return [True, tablero[row + 1][col - 1], row, col, row + 1, col - 1]
    except:
        return[False]

def black_move_two(tablero, row, col, is_first_move):
    if is_first_move:
        if tablero[row + 1][col] == ' ' and tablero[row + 2][col] == ' ':
            return [True, row, col, row + 2, col]
    return [False]

def black_move(tablero, row, col):
    if tablero[row + 1][col] == ' ':
        return [True, row, col, row + 1, col]
    return [False]

class blackPawn:

    def __init__(self, row, col):
        self.col = col
        self.row = row
        self.isFirstMove = True

    def attack(self, tablero):
        left = blackLeftAttack(tablero, self.row, self.col)
        right = blackRightkAttack(tablero, self.row, self.col)
        possibleAttack = [False]
        if left[0]:
            possibleAttack[0] = True
            possibleAttack.append(left)
        if right[0]:
            possibleAttack[0] = True
            possibleAttack.append(right)
        return possibleAttack

    def move_two(self, tablero):
        self.is_first_move = False
        return black_move_two(tablero, self.row, self.col, self.isFirstMove)
    def move(self, tablero):
        return black_move(tablero, self.row, self.col)

