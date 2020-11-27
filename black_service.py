from pawn import BlackPawn
from queen import BlackQueen


def black_sort_attack(attacks):
    for a in attacks:  # [False,False,False,False,[['Q',1,3,6,3]]]
        if a:
            for i in a:
                if i[0] == 'Q':
                    attacks.insert(0, a)
                if i[0] == 'R':
                    attacks.insert(1, a)
                if i[0] == 'B':
                    attacks.insert(2, a)
                if i[0] == 'H':
                    attacks.insert(3, a)
    return attacks


class BlackTurn:
    def __init__(self, board):
        self.board = board
        self.pawns = list()
        self.queens = list()
        self.attacks = list()
        self.moves = list()

    def update(self):
        for row in range(16):
            for col in range(16):
                if self.board[row][col] == 'p':
                    black_pawn = BlackPawn(row, col)
                    self.pawns.append(black_pawn)
                    attack = black_pawn.black_pawn_attack(self.board)
                    self.attacks.append(attack)
                if self.board[row][col] == 'q':
                    black_queen = BlackQueen(row, col)
                    self.attacks.append(black_queen.black_queen_attack(self.board))

        self.attacks = black_sort_attack(self.attacks)
        return self.attacks
