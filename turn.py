from pawn import BlackPawn
from pawn import WhitePawn
from queen import BlackQueen
from queen import WhiteQueen
from rook import BlackRook
from rook import WhiteRook
from bishop import BlackBishop
from bishop import WhiteBishop


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
                    self.pawns.append(BlackPawn(row, col))
                    continue
                if self.board[row][col] == 'q':
                    self.queens.append(BlackQueen(row, col))
                    continue
                if self.board[row][col] == 'r':
                    self.rooks.append(BlackRook(row, col))
                    continue
                if self.board[row][col] == 'b':
                    self.bishops.append(BlackBishop(row, col))
                    continue

    def possible_attacks(self):

        for p in self.pawns:
            self.attacks.append(p.black_pawn_attack(self.board))
        for r in self.rooks:
            self.attacks.append(r.black_rook_attack(self.board))
        for b in self.bishops:
            self.attacks.append(b.black_bishop_attack(self.board))
        for q in self.queens:
            self.attacks.append(q.black_bishop_attack(self.board))
            self.attacks.append(q.black_rook_attack(self.board))
        self.attacks = black_sort_attack(self.attacks)
        print(self.attacks)
        return self.attacks

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
                    self.pawns.append(WhitePawn(row, col))
                    continue
                if self.board[row][col] == 'Q':
                    self.queens.append(WhiteQueen(row, col))
                    continue
                if self.board[row][col] == 'R':
                    self.rooks.append(WhiteRook(row, col))
                    continue
                if self.board[row][col] == 'B':
                    self.bishops.append(WhiteBishop(row, col))
                    continue

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
        self.attacks = white_sort_attack(self.attacks)
        print(self.attacks)
        return self.attacks
