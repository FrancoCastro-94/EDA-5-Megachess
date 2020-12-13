from pieces.rook import BlackRook, WhiteRook
from pieces.bishop import BlackBishop, WhiteBishop


class WhiteQueen(WhiteRook, WhiteBishop):
    def __init__(self, row, col):
        WhiteRook.__init__(self, row, col)
        WhiteBishop.__init__(self, row, col)

    def white_queen_attack(self, board, attacks):
        self.white_bishop_attack(board, attacks)
        self.white_rook_attack(board, attacks)
        return attacks


class BlackQueen(BlackRook, BlackBishop):
    def __init__(self, row, col):
        BlackRook.__init__(self, row, col)
        BlackBishop.__init__(self, row, col)

    def black_queen_attack(self, board, attacks):
        self.black_bishop_attack(board, attacks)
        self.black_rook_attack(board, attacks)
        return attacks
