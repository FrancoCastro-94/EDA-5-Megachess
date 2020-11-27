import rook as r
import bishop as b


class BlackQueen(r.BlackRook, b.BlackBishop):
    def __init__(self, row, col):
        r.BlackRook.__init__(self, row, col)
        b.BlackBishop.__init__(self, row, col)
        self.row = row
        self.col = col


class WhiteQueen(r.WhiteRook, b.WhiteBishop):
    def __init__(self, row, col):
        r.WhiteRook.__init__(self, row, col)
        b.WhiteBishop.__init__(self, row, col)
        self.row = row
        self.col = col

    def queen_attack(self, board):
        bishop = self.white_bishop_attack(board)
        rook = self.attack_rook(board)
        possibleAttack = []
        if bishop:
            possibleAttack.append(bishop)
        if rook:
            possibleAttack.append(rook)
        if possibleAttack:
            return possibleAttack
        return False
