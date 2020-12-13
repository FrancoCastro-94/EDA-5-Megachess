from pieces.pawn import BlackPawn, WhitePawn
from pieces.queen import BlackQueen, WhiteQueen
from pieces.rook import BlackRook, WhiteRook
from pieces.bishop import BlackBishop, WhiteBishop
from pieces.horse import BlackHorse, WhiteHorse
from pieces.king import BlackKing, WhiteKing


class WhiteTurn:

    def __init__(self, board):
        self.board = board
        self.pawns = list()
        self.horses = list()
        self.attacks = list()

    def update_pieces(self):  # update pieces needed to move and attacks
        for row in range(15, -1, -1):
            for col in range(15, -1, -1):

                if self.board[row][col] == ' ':
                    continue
                if self.board[row][col] == 'P':
                    p = WhitePawn(row, col)
                    self.pawns.append(p)
                    p.white_pawn_attack(self.board, self.attacks)
                    continue
                if self.board[row][col] == 'H':
                    h = WhiteHorse(row, col)
                    self.horses.append(h)
                    h.white_horse_attack(self.board, self.attacks)
                    continue
                if self.board[row][col] == 'R':
                    WhiteRook(row, col).white_rook_attack(self.board, self.attacks)
                    continue
                if self.board[row][col] == 'B':
                    WhiteBishop(row, col).white_bishop_attack(self.board, self.attacks)
                    continue
                if self.board[row][col] == 'Q':
                    WhiteQueen(row, col).white_queen_attack(self.board, self.attacks)
                    continue
                if self.board[row][col] == 'K':
                    WhiteKing(row, col).white_king_attack(self.board, self.attacks)
                    continue

        attack = white_prioritize_attack(self.attacks)
        return attack


class BlackTurn:
    def __init__(self, board):
        self.board = board
        self.pawns = list()
        self.horses = list()
        self.attacks = list()

    def update_pieces(self):  # update pieces needed to move and attacks
        for row in range(16):
            for col in range(16):

                if self.board[row][col] == ' ':
                    continue
                if self.board[row][col] == 'p':
                    p = BlackPawn(row, col)
                    self.pawns.append(p)
                    p.black_pawn_attack(self.board, self.attacks)
                    continue
                if self.board[row][col] == 'q':
                    BlackQueen(row, col).black_queen_attack(self.board, self.attacks)
                    continue
                if self.board[row][col] == 'h':
                    h = BlackHorse(row, col)
                    self.horses.append(h)
                    h.black_horse_attack(self.board, self.attacks)
                    continue
                if self.board[row][col] == 'r':
                    BlackRook(row, col).black_rook_attack(self.board, self.attacks)
                    continue
                if self.board[row][col] == 'b':
                    BlackBishop(row, col).black_bishop_attack(self.board, self.attacks)
                    continue
                if self.board[row][col] == 'k':
                    BlackKing(row, col).black_king_attack(self.board, self.attacks)
                    continue
        attack = black_prioritize_attack(self.attacks)
        return attack


# prioritizes attacks according to the value of attacks and only attacks pawns in row 5, 6 and 7
def white_prioritize_attack(attacks):
    prioritize_attacks = [False, False, False, False, False, False]
    for a in attacks:
        if a:
            if a[0] == 'q':
                prioritize_attacks.insert(0, a)
            if a[0] == 'r':
                prioritize_attacks.insert(1, a)
            if a[0] == 'b':
                prioritize_attacks.insert(2, a)
            if a[0] == 'k':
                prioritize_attacks.insert(3, a)
            if a[0] == 'h':
                prioritize_attacks.insert(4, a)
            if a[0] == 'p' and a[3] in [5, 6, 7]:
                prioritize_attacks.insert(5, a)
    return prioritize_attacks


# prioritizes attacks according to the value of attacks and only attacks pawns in row 8, 9 and 10
def black_prioritize_attack(attacks):
    prioritize_attacks = [False, False, False, False, False, False]
    for a in attacks:
        if a:
            if a[0] == 'Q':
                prioritize_attacks[0] = a
            if a[0] == 'R':
                prioritize_attacks[1] = a
            if a[0] == 'B':
                prioritize_attacks[2] = a
            if a[0] == 'K':
                prioritize_attacks[3] = a
            if a[0] == 'H':
                prioritize_attacks[4] = a
            if a[0] == 'P' and a[3] in [8, 9, 10]:
                prioritize_attacks[5] = a
    return prioritize_attacks
