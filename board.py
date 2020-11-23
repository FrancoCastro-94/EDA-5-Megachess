import pawn
import queen


def white_sort_attack(attacks):
    for a in attacks:
        if a:
            if a[0] == 'Q':
                attacks.insert(0, a)
            if a[0] == 'R':
                attacks.insert(1, a)
            if a[0] == 'B':
                attacks.insert(2, a)
            if a[0] == 'H':
                attacks.insert(3, a)
    return attacks


class WhiteBoard:
    def __init__(self, board):
        self.board = board
        self.pawns = list()
        self.queens = list()
        self.attacks = list()

    def update(self):
        for row in range(16, -1, -1):
            for col in range(16, -1, -1):
                if self.board[row][col] == 'P':
                    self.pawns.append(pawn.WhitePawn(row, col))
                if self.board[row][col] == 'Q':
                    self.queens.append(queen.WhiteQueen(row, col))

    def possible_attacks(self):
        for p in self.pawns:
            self.attacks.append(p.atack(self.board))
        for q in self.queens:
            self.attacks.append(q.atack(self.board))
        self.attacks = white_sort_attack(self.attacks)
        return self.attacks
