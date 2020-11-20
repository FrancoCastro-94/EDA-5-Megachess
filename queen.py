import rook as r
import bishop as b


class blackQueen(r.blackRook, b.blackBishop):
    def __init__(self, row, col):
        r.blackRook.__init__(self, row, col)
        b.blackBishop.__init__(self, row, col)
        self.row = row
        self.col = col
    def queenAttack(self, tablero):
        possibleAttack = r.blackRook.attac(tablero, self.row, self.col)
        possibleAttack.append(b.blackBishop.attack(tablero, self.row, self.col))
        return possibleAttack