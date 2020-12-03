import rook as r
import bishop as b


class BlackQueen(r.BlackRook, b.BlackBishop):
    def __init__(self, row, col):
        r.BlackRook.__init__(self, row, col)
        b.BlackBishop.__init__(self, row, col)
        self.row = row
        self.col = col

    def black_queen_attack(self, board):
        bishop = self.black_bishop_attack(board)
        rook = self.black_rook_attack(board)
        possibleAttack = []
        if bishop:
            possibleAttack.extend(bishop)
        if rook:
            possibleAttack.extend(rook)
        if possibleAttack:
            return possibleAttack
        return False


class WhiteQueen(r.WhiteRook, b.WhiteBishop):
    def __init__(self, row, col):
        r.WhiteRook.__init__(self, row, col)
        b.WhiteBishop.__init__(self, row, col)
        self.row = row
        self.col = col

    def white_queen_attack(self, board):
        bishop = self.white_bishop_attack(board)
        rook = self.white_rook_attack(board)
        possibleAttack = []
        if bishop:
            possibleAttack.extend(bishop)
        if rook:
            possibleAttack.extend(rook)
        if possibleAttack:
            return possibleAttack
        return False
