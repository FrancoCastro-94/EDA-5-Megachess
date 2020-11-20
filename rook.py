def upBlackAttac(tablero, row, col):
    try:
        for i in range(1, 16):
            if tablero[row + i][col].islower:
                return [False]
            if tablero[row + i][col].isupper:
                return [True, tablero[row + i][col], row + i, col]
    except:
        return [False]


def downBlackAttac(tablero, row, col):
    try:
        for i in range(1, 16):
            if tablero[row - i][col].islower:
                return [False]
            if tablero[row - i][col].isupper:
                return [True, tablero[row - i][col], row - i, col]
    except:
        return [False]

def leftBlackAttac(tablero, row, col):
    try:
        for i in range(1, 16):
            if tablero[row][col - i].islower:
                return [False]
            if tablero[row][col - i].isupper:
                return [True, tablero[row - i][col], row, col - i]
    except:
        return [False]

def rightBlackAttac(tablero, row, col):
    try:
        for i in range(1, 16):
            if tablero[row][col + i].islower:
                return [False]
            if tablero[row][col + i].isupper:
                return [True, tablero[row][col + i], row, col + i]
    except:
        return [False]


class blackRook:
    def __init__(self, row, col):
        self.row = row
        self.col = col

    def attac(self, tablero):
        up = upBlackAttac(tablero, self.row, self.col)
        down = downBlackAttac(tablero, self.row, self.col)
        left = leftBlackAttac(tablero, self.row, self.col)
        right = rightBlackAttac(tablero, self.row, self.col)
        possibleAttac = [False]
        if up[0]:
            possibleAttac[0] = True
            possibleAttac.append(up)
        if down[0]:
            possibleAttac[0] = True
            possibleAttac.append(down)
        if left[0]:
            possibleAttac[0] = True
            possibleAttac.append(left)
        if right[0]:
            possibleAttac[0] = True
            possibleAttac.append(right)
        return possibleAttac