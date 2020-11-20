def blackForwardRight(tablero, row, col):
    try:
        for i in range(1, 16):
            if tablero[row + i][col + i].islower:
                return [False]
            if tablero[row + i][col + i].isupper:
                return [True, tablero[row + i][col + i], row + i, col + i]
    except:
        return [False]


def blackForwardLeft(tablero, row, col):
    try:
        for i in range(1, 16):
            if tablero[row + i][col - i].islower:
                return [False]
            if tablero[row + i][col - i].isupper:
                return [True, tablero[row + i][col - i], row + i, col - i]
    except:
        return [False]


def blackBackLeft(tablero, row, col):
    try:
        for i in range(1, 16):
            if tablero[row - i][col - i].islower:
                return [False]
            if tablero[row - i][col - i].isupper:
                return [True, tablero[row - i][col - i], row - i, col - i]
    except:
        return [False]


def blackBackRight(tablero, row, col):
    try:
        for i in range(1, 16):
            if tablero[row - i][col + i].islower:
                return [False]
            if tablero[row - i][col + i].isupper:
                return [True, tablero[row - i][col + i], row - i, col + i]
    except:
        return [False]


class blackBishop:

    def __init__(self, row, col):
        self.row = row
        self.col = col

    def attack(self, tablero):
        forwardRight = blackForwardRight(tablero, self.row, self.col)
        forwardLeft = blackForwardLeft(tablero, self.row, self.col)
        backRight = blackBackRight(tablero, self.row, self.col)
        backLeft = blackBackLeft(tablero, self.row, self.col)
        possibleAttack = [False]
        if blackForwardRight[0]:
            possibleAttack[0] = True
            possibleAttack.append(forwardRight)
        if blackForwardLeft[0]:
            possibleAttack[0] = True
            possibleAttack.append(forwardLeft)
        if blackBackRight[0]:
            possibleAttack[0] = True
            possibleAttack.append(backRight)
        if blackBackLeft[0]:
            possibleAttack[0] = True
            possibleAttack.append(backLeft)
        return possibleAttack
