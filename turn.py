from pawn import BlackPawn
from pawn import WhitePawn
from queen import BlackQueen
from queen import WhiteQueen
from rook import BlackRook
from rook import WhiteRook
from bishop import BlackBishop
from bishop import WhiteBishop
from horse import BlackHorse
from horse import WhiteHorse
from king import BlackKing
from king import WhiteKing


def black_sort_attack(attacks):
    sorted_attacks = []
    for a in attacks:
        if a:
            for i in a:
                if i[0] == 'Q':
                    sorted_attacks.insert(0, a)
                if i[0] == 'R':
                    sorted_attacks.insert(1, a)
                if i[0] == 'B':
                    sorted_attacks.insert(2, a)
                if i[0] == 'H':
                    sorted_attacks.insert(3, a)
    return sorted_attacks


class BlackTurn:
    def __init__(self, board):
        self.board = board
        self.pawns = list()
        self.queens = list()
        self.rooks = list()
        self.bishops = list()
        self.attacks = list()
        self.moves = list()

    def update(self):
        for row in range(16):
            for col in range(16):
                if self.board[row][col] == 'p':
                    p = BlackPawn(row, col)
                    self.pwans.append(p)
                    self.pawns.append(BlackPawn(row, col))
                    continue
                if self.board[row][col] == 'q':
                    q = BlackQueen(row, col)
                    self.attacks.append(q.black_bishop_attack(self.board))
                    self.attacks.append(q.black_rook_attack(self.board))
                    continue
                if self.board[row][col] == 'h':
                    self.attacks.append(BlackHorse(row, col).black_horse_attack(self.board))
                    continue
                if self.board[row][col] == 'r':
                    self.attacks.append(BlackRook(row, col).black_rook_attack(self.board))
                    continue
                if self.board[row][col] == 'b':
                    self.attacks.append(BlackBishop(row, col).black_bishop_attack(self.board))
                    continue
                if self.board[row][col] == 'k':
                    self.attacks.append(BlackKing(row, col).black_king_attack(self.board))
                    continue
        self.attacks = white_sort_attack(self.attacks)
        return self.attacks


"""
    def possible_attacks(self):

        for r in self.rooks:
            self.attacks.append(r.black_rook_attack(self.board))
        for b in self.bishops:
            self.attacks.append(b.black_bishop_attack(self.board))
        for q in self.queens:
            self.attacks.append(q.black_bishop_attack(self.board))
            self.attacks.append(q.black_rook_attack(self.board))
        for p in self.pawns:
            self.attacks.append(p.black_pawn_attack(self.board))
        for h in self.horses:
            self.attacks.append(h.black_horse_attack(self.board))
        self.attacks = black_sort_attack(self.attacks)
        print(self.attacks)
        return self.attacks
"""


# -------------------------------------------- WHITE BOARD --------------------------------------- #


def white_sort_attack(attacks):
    sorted_attacks = []
    for a in attacks:
        if a:
            for i in a:
                if i[0] == 'q':
                    sorted_attacks.insert(0, a)
                if i[0] == 'r':
                    sorted_attacks.insert(1, a)
                if i[0] == 'b':
                    sorted_attacks.insert(2, a)
                if i[0] == 'h':
                    sorted_attacks.insert(3, a)
    return sorted_attacks


class WhiteTurn:

    def __init__(self, board):
        self.board = board
        self.pawns = list()
        self.queens = list()
        self.rooks = list()
        self.bishops = list()
        self.attacks = list()
        self.moves = list()

    def update(self):
        for row in range(15, -1, -1):
            for col in range(15, -1, -1):
                if self.board[row][col] == 'P':
                    p = WhitePawn(row, col)
                    self.pawns.append(p)
                    self.attacks.append(p.white_pawn_attack(self.board))
                    continue
                if self.board[row][col] == 'Q':
                    q = WhiteQueen(row, col)
                    self.attacks.append(q.white_bishop_attack(self.board))
                    self.attacks.append(q.white_rook_attack(self.board))
                    continue
                if self.board[row][col] == 'H':
                    self.attacks.append(WhiteHorse(row, col).white_horse_attack(self.board))
                    continue
                if self.board[row][col] == 'R':
                    self.attacks.append(WhiteRook(row, col).white_rook_attack(self.board))
                    continue
                if self.board[row][col] == 'B':
                    self.attacks.append(WhiteBishop(row, col).white_bishop_attack(self.board))
                    continue
                if self.board[row][col] == 'K':
                    self.attacks.append(WhiteKing(row, col).white_king_attack(self.board))
                    continue
        self.attacks = white_sort_attack(self.attacks)
        return self.attacks


"""
    def possible_attacks(self):
        for p in self.pawns:
            self.attacks.append(p.white_pawn_attack(self.board))
        for q in self.queens:
            self.attacks.append(q.white_bishop_attack(self.board))
            self.attacks.append(q.white_rook_attack(self.board))
        for r in self.rooks:
            self.attacks.append(r.white_rook_attack(self.board))
        for b in self.bishops:
            self.attacks.append(b.white_bishop_attack(self.board))
        for h in self.horses:
            self.attacks.append(h.white_horse_attack(self.board))
        self.attacks = white_sort_attack(self.attacks)
        print(self.attacks)
        return self.attacks
"""
