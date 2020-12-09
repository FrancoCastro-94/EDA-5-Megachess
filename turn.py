from pieces.pawn import BlackPawn, WhitePawn
from pieces.queen import BlackQueen, WhiteQueen
from pieces.rook import BlackRook, WhiteRook
from pieces.bishop import BlackBishop, WhiteBishop
from pieces.horse import BlackHorse, WhiteHorse
from pieces.king import BlackKing, WhiteKing


def black_sort_attack(attacks):
    sorted_attacks = []
    for a in attacks:
        if a:
            for i in a:
                if i[0] == 'K':
                    sorted_attacks.insert(0, i)
                if i[0] == 'R':
                    sorted_attacks.insert(1, i)
                if i[0] == 'B':
                    sorted_attacks.insert(2, i)
                if i[0] == 'H':
                    sorted_attacks.insert(3, i)
                if i[0] == 'P':
                    sorted_attacks.insert(4, i)
                if i[0] == 'Q':
                    sorted_attacks.insert(5, i)
    return sorted_attacks


class BlackTurn:
    def __init__(self, board):
        self.board = board
        self.pawns = list()
        self.horses = list()
        self.attacks = list()

        """self.queens = list()
        self.rooks = list()
        self.bishops = list()
        self.moves = list()"""

    def update(self):
        for row in range(16):
            for col in range(16):

                if self.board[row][col] == 'r':
                    self.attacks.append(BlackRook(row, col).black_rook_attack(self.board))
                    continue
                if self.board[row][col] == 'b':
                    self.attacks.append(BlackBishop(row, col).black_bishop_attack(self.board))
                    continue
                if self.board[row][col] == 'h':
                    h = BlackHorse(row, col)
                    self.horses.append(h)
                    self.attacks.append(h.black_horse_attack(self.board))
                    continue
                if self.board[row][col] == 'p':
                    p = BlackPawn(row, col)
                    self.pawns.append(p)
                    self.attacks.append(p.black_pawn_attack(self.board))
                    continue
                if self.board[row][col] == 'q':
                    self.attacks.append(BlackQueen(row, col).black_bishop_attack(self.board))
                    continue
                if self.board[row][col] == 'k':
                    self.attacks.append(BlackKing(row, col).black_king_attack(self.board))
                    continue
        self.attacks = black_sort_attack(self.attacks)
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
                    sorted_attacks.insert(0, i)
                if i[0] == 'r':
                    sorted_attacks.insert(1, i)
                if i[0] == 'b':
                    sorted_attacks.insert(2, i)
                if i[0] == 'k':
                    sorted_attacks.insert(3, i)
                if i[0] == 'h':
                    sorted_attacks.insert(4, i)
                if i[0] == 'p' and i[3] in [5, 6]:
                    sorted_attacks.insert(5, i)
    return sorted_attacks


class WhiteTurn:

    def __init__(self, board):
        self.board = board
        self.pawns = list()
        self.horses = list()
        self.rooks_attacks = list()
        self.queens_attacks = list()
        self.bishops_attacks = list()
        self.horses_attacks = list()
        self.kings_attacks = list()
        self.pawns_attacks = list()
        self.attacks = list()

    def update(self):
        for row in range(15, -1, -1):
            for col in range(15, -1, -1):

                if self.board[row][col] == 'P':
                    p = WhitePawn(row, col)
                    self.pawns.append(p)
                    self.pawns_attacks.append(p.white_pawn_attack(self.board))
                    continue
                if self.board[row][col] == 'Q':
                    self.queens_attacks.append(WhiteQueen(row, col).white_queen_attack(self.board))
                    continue
                if self.board[row][col] == 'R':
                    self.rooks_attacks.append(WhiteRook(row, col).white_rook_attack(self.board))
                    continue
                if self.board[row][col] == 'B':
                    self.bishops_attacks.append(WhiteBishop(row, col).white_bishop_attack(self.board))
                    continue
                if self.board[row][col] == 'H':
                    h = WhiteHorse(row, col)
                    self.horses.append(h)
                    self.horses_attacks.append(h.white_horse_attack(self.board))
                    continue
                if self.board[row][col] == 'K':
                    self.kings_attacks.append(WhiteKing(row, col).white_king_attack(self.board))
                    continue
        self.attacks = self.kings_attacks + self.pawns_attacks + self.queens_attacks + \
                       self.horses_attacks + self.bishops_attacks + self.rooks_attacks
        self.attacks = white_sort_attack(self.attacks)
        return self.attacks

