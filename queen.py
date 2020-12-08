from pieces.rook import BlackRook, WhiteRook
from pieces.bishop import BlackBishop, WhiteBishop


class BlackQueen(BlackRook, BlackBishop):
    def __init__(self, row, col):
        BlackRook.__init__(self, row, col)
        BlackBishop.__init__(self, row, col)

    def black_queen_attack(self, board):
        attacks = list()
        bishop = self.black_bishop_attack(board)
        rook = self.black_rook_attack(board)
        if bishop:
            attacks.extend(bishop)
        if rook:
            attacks.extend(rook)
        if attacks:
            return attacks
        return False


class WhiteQueen(WhiteRook, WhiteBishop):
    def __init__(self, row, col):
        WhiteRook.__init__(self, row, col)
        WhiteBishop.__init__(self, row, col)

    def white_queen_attack(self, board):
        bishop = self.white_bishop_attack(board)
        rook = self.white_rook_attack(board)
        attacks = list()
        if bishop:
            attacks.extend(bishop)
        if rook:
            attacks.extend(rook)
        if attacks:
            return attacks
        return False
