import unittest
import data
from pieces import pawn, rook, queen, king, bishop, horse

b = data.board()


class MyTestCase(unittest.TestCase):

    def test_black_horse_move(self):
        self.assertFalse(horse.BlackHorse(0, 0).black_horse_move(b))
        self.assertFalse(horse.BlackHorse(1, 8).black_horse_move(b))
        self.assertFalse(horse.BlackHorse(0, 15).black_horse_move(b))
        result = [[2, 2, 4, 1], [2, 2, 4, 3]]
        self.assertEqual(horse.BlackHorse(2, 2).black_horse_move(b), result)
        result = [[8, 8, 10, 7], [8, 8, 10, 9], [8, 8, 9, 10], [8, 8, 7, 10],
                  [8, 8, 9, 6], [8, 8, 7, 6], [8, 8, 6, 7], [8, 8, 6, 9]]
        self.assertEqual(horse.BlackHorse(8, 8).black_horse_move(b), result)
        result = [[11, 15, 10, 13], [11, 15, 9, 14]]
        self.assertEqual(horse.BlackHorse(11, 15).black_horse_move(b), result)

    def test_white_horse_move(self):
        self.assertFalse(horse.WhiteHorse(15, 15).white_horse_move(b))
        self.assertFalse(horse.WhiteHorse(14, 8).white_horse_move(b))
        self.assertFalse(horse.WhiteHorse(15, 0).white_horse_move(b))
        result = [[13, 13, 11, 12], [13, 13, 11, 14]]
        self.assertEqual(horse.WhiteHorse(13, 13).white_horse_move(b), result)
        result = [[8, 8, 6, 7], [8, 8, 6, 9], [8, 8, 9, 10], [8, 8, 7, 10],
                  [8, 8, 9, 6], [8, 8, 7, 6], [8, 8, 10, 7], [8, 8, 10, 9]]
        self.assertEqual(horse.WhiteHorse(8, 8).white_horse_move(b), result)
        result = [[4, 0, 5, 2], [4, 0, 6, 1]]
        self.assertEqual(horse.WhiteHorse(4, 0).white_horse_move(b), result)

    def test_black_horse_attack(self):
        self.assertFalse(horse.BlackHorse(0, 0).black_horse_attack(b))
        self.assertFalse(horse.BlackHorse(0, 8).black_horse_attack(b))
        self.assertFalse(horse.BlackHorse(8, 8).black_horse_attack(b))
        result = [['B', 14, 8, 15, 10], ['P', 14, 8, 13, 10], ['P', 14, 8, 12, 9],
                  ['P', 14, 8, 12, 7], ['Q', 14, 8, 15, 6], ['P', 14, 8, 13, 6]]
        self.assertEqual(horse.BlackHorse(14, 8).black_horse_attack(b), result)
        result = [['H', 13, 4, 15, 3], ['B', 13, 4, 15, 5], ['Q', 13, 4, 14, 6],
                  ['P', 13, 4, 12, 6], ['H', 13, 4, 14, 2], ['P', 13, 4, 12, 2]]
        self.assertEqual(horse.BlackHorse(13, 4).black_horse_attack(b), result)
        result = [['B', 12, 6, 14, 5], ['Q', 12, 6, 14, 7], ['P', 12, 6, 13, 8], ['P', 12, 6, 13, 4]]
        self.assertEqual(horse.BlackHorse(12, 6).black_horse_attack(b), result)

    def test_white_horse_attack(self):
        self.assertFalse(horse.WhiteHorse(15, 15).white_horse_attack(b))
        self.assertFalse(horse.WhiteHorse(8, 8).white_horse_attack(b))
        self.assertFalse(horse.WhiteHorse(15, 8).white_horse_attack(b))
        result = [['p', 1, 8, 3, 7], ['p', 1, 8, 3, 9], ['p', 1, 8, 2, 10],
                  ['b', 1, 8, 0, 10], ['q', 1, 8, 0, 6], ['p', 1, 8, 2, 6]]
        self.assertEqual(horse.WhiteHorse(1, 8).white_horse_attack(b), result)
        result = [['p', 2, 4, 3, 6], ['q', 2, 4, 1, 6], ['b', 2, 4, 0, 5],
                  ['h', 2, 4, 0, 3], ['h', 2, 4, 1, 2], ['p', 2, 4, 3, 2]]
        self.assertEqual(horse.WhiteHorse(2, 4).white_horse_attack(b), result)
        result = [['p', 3, 6, 2, 8], ['q', 3, 6, 1, 7], ['b', 3, 6, 1, 5], ['p', 3, 6, 2, 4]]
        self.assertEqual(horse.WhiteHorse(3, 6).white_horse_attack(b), result)

    def test_black_king_attack(self):
        self.assertFalse(king.BlackKing(0, 0).black_king_attack(b))
        self.assertFalse(king.BlackKing(0, 8).black_king_attack(b))
        self.assertFalse(king.BlackKing(8, 8).black_king_attack(b))
        result = [['R', 15, 15, 14, 15], ['R', 15, 15, 14, 14], ['R', 15, 15, 15, 14]]
        self.assertEqual(king.BlackKing(15, 15).black_king_attack(b), result)
        result = [['P', 12, 10, 13, 10], ['P', 12, 10, 13, 9], ['P', 12, 10, 13, 11],
                  ['P', 12, 10, 12, 9], ['P', 12, 10, 12, 11]]
        self.assertEqual(king.BlackKing(12, 10).black_king_attack(b), result)
        result = [['H', 13, 13, 14, 13], ['H', 13, 13, 14, 12], ['R', 13, 13, 14, 14],
                  ['P', 13, 13, 12, 13], ['P', 13, 13, 12, 12], ['P', 13, 13, 12, 14],
                  ['P', 13, 13, 13, 12], ['P', 13, 13, 13, 14]]
        self.assertEqual(king.BlackKing(13, 13).black_king_attack(b), result)

    def test_white_king_attack(self):
        self.assertFalse(king.WhiteKing(15, 15).white_king_attack(b))
        self.assertFalse(king.WhiteKing(15, 8).white_king_attack(b))
        self.assertFalse(king.WhiteKing(8, 8).white_king_attack(b))
        result = [['r', 0, 0, 1, 0], ['r', 0, 0, 1, 1], ['r', 0, 0, 0, 1]]
        self.assertEqual(king.WhiteKing(0, 0).white_king_attack(b), result)
        result = [['p', 3, 6, 2, 6], ['p', 3, 6, 2, 5], ['p', 3, 6, 2, 7],
                  ['p', 3, 6, 3, 5], ['p', 3, 6, 3, 7]]
        self.assertEqual(king.WhiteKing(3, 6).white_king_attack(b), result)
        result = [['r', 2, 15, 1, 15], ['r', 2, 15, 1, 14], ['p', 2, 15, 3, 15],
                  ['p', 2, 15, 3, 14], ['p', 2, 15, 2, 14]]
        self.assertEqual(king.WhiteKing(2, 15).white_king_attack(b), result)


    def test_black_rook_attack(self):
        self.assertFalse(rook.BlackRook(0, 0).black_rook_attack(b))
        self.assertFalse(rook.BlackRook(2, 15).black_rook_attack(b))
        result = [['P', 8, 8, 12, 8]]
        self.assertEqual(rook.BlackRook(8, 8).black_rook_attack(b), result)
        result = [['P', 12, 8, 13, 8], ['P', 12, 8, 12, 7], ['P', 12, 8, 12, 9]]
        self.assertEqual(rook.BlackRook(12, 8).black_rook_attack(b), result)
        result = [['R', 14, 14, 15, 14], ['P', 14, 14, 13, 14], ['H', 14, 14, 14, 13],
                  ['R', 14, 14, 14, 15]]
        self.assertEqual(rook.BlackRook(14, 14).black_rook_attack(b), result)

    def test_white_rook_attack(self):
        self.assertFalse(rook.WhiteRook(15, 15).white_rook_attack(b))
        self.assertFalse(rook.WhiteRook(13, 2).white_rook_attack(b))
        result = [['p', 8, 8, 3, 8]]
        self.assertEqual(rook.WhiteRook(8, 8).white_rook_attack(b), result)
        result = [['p', 2, 8, 3, 8], ['k', 2, 8, 1, 8], ['p', 2, 8, 2, 7],
                  ['p', 2, 8, 2, 9]]
        self.assertEqual(rook.WhiteRook(2, 8).white_rook_attack(b), result)
        result = [['r', 0, 0, 1, 0], ['r', 0, 0, 0, 1]]
        self.assertEqual(rook.WhiteRook(0, 0).white_rook_attack(b), result)

    def test_black_pawn_attack(self):
        self.assertFalse(pawn.BlackPawn(3, 0).black_pawn_attack(b))
        self.assertFalse(pawn.BlackPawn(3, 15).black_pawn_attack(b))
        self.assertFalse(pawn.BlackPawn(8, 8).black_pawn_attack(b))
        result = [['P', 12, 12, 13, 11], ['P', 12, 12, 13, 13]]
        self.assertEqual(pawn.BlackPawn(12, 12).black_pawn_attack(b), result)
        result = [['P', 12, 15, 13, 14]]
        self.assertEqual(pawn.BlackPawn(12, 15).black_pawn_attack(b), result)
        result = [['R', 14, 0, 15, 1]]
        self.assertEqual(pawn.BlackPawn(14, 0).black_pawn_attack(b), result)

    def test_white_pawn_attack(self):
        self.assertFalse(pawn.WhitePawn(13, 0).white_pawn_attack(b))
        self.assertFalse(pawn.WhitePawn(13, 15).white_pawn_attack(b))
        self.assertFalse(pawn.WhitePawn(8, 8).white_pawn_attack(b))
        result = [['b', 1, 6, 0, 5], ['q', 1, 6, 0, 7]]
        self.assertEqual(pawn.WhitePawn(1, 6).white_pawn_attack(b), result)
        result = [['p', 4, 15, 3, 14]]
        self.assertEqual(pawn.WhitePawn(4, 15).white_pawn_attack(b), result)
        result = [['p', 4, 0, 3, 1]]
        self.assertEqual(pawn.WhitePawn(4, 0).white_pawn_attack(b), result)

    def test_black_bishop_attack(self):
        self.assertFalse(bishop.BlackBishop(0, 0).black_bishop_attack(b))
        self.assertFalse(bishop.BlackBishop(0, 13).black_bishop_attack(b))
        self.assertFalse(bishop.BlackBishop(2, 15).black_bishop_attack(b))
        result = [['P', 8, 8, 12, 12], ['P', 8, 8, 12, 4]]
        self.assertEqual(bishop.BlackBishop(8, 8).black_bishop_attack(b), result)
        result = [['P', 8, 15, 12, 11]]
        self.assertEqual(bishop.BlackBishop(8, 15).black_bishop_attack(b), result)
        result = [['R', 13, 0, 14, 1], ['P', 13, 0, 12, 1]]
        self.assertEqual(bishop.BlackBishop(13, 0).black_bishop_attack(b), result)

    def test_white_bishop_attack(self):
        self.assertFalse(bishop.WhiteBishop(15, 15).white_bishop_attack(b))
        self.assertFalse(bishop.WhiteBishop(13, 11).white_bishop_attack(b))
        self.assertFalse(bishop.WhiteBishop(15, 0).white_bishop_attack(b))
        result = [['p', 8, 8, 3, 13], ['p', 8, 8, 3, 3]]
        self.assertEqual(bishop.WhiteBishop(8, 8).white_bishop_attack(b), result)
        result = [['k', 0, 8, 1, 9], ['q', 0, 8, 1, 7]]
        self.assertEqual(bishop.WhiteBishop(0, 8).white_bishop_attack(b), result)
        result = [['q', 2, 6, 1, 7], ['b', 2, 6, 1, 5], ['p', 2, 6, 3, 7],
                  ['p', 2, 6, 3, 5]]
        self.assertEqual(bishop.WhiteBishop(2, 6).white_bishop_attack(b), result)

    def test_black_queen_attack(self):
        self.assertFalse(queen.BlackQueen(0, 0).black_queen_attack(b))
        self.assertFalse(queen.BlackQueen(2, 10).black_queen_attack(b))
        self.assertFalse(queen.BlackQueen(0, 15).black_queen_attack(b))
        result = [['P', 8, 8, 12, 12], ['P', 8, 8, 12, 4], ['P', 8, 8, 12, 8]]
        self.assertEqual(queen.BlackQueen(8, 8).black_queen_attack(b), result)
        result = [['R', 15, 15, 14, 14], ['R', 15, 15, 14, 15], ['R', 15, 15, 15, 14]]
        self.assertEqual(queen.BlackQueen(15, 15).black_queen_attack(b), result)
        result = [['Q', 13, 6, 14, 7], ['B', 13, 6, 14, 5], ['P', 13, 6, 12, 7], ['P', 13, 6, 12, 5],
                  ['Q', 13, 6, 14, 6], ['P', 13, 6, 12, 6], ['P', 13, 6, 13, 5], ['P', 13, 6, 13, 7]]
        self.assertEqual(queen.BlackQueen(13, 6).black_queen_attack(b), result)

    def test_white_queen_attack(self):
        self.assertFalse(queen.WhiteQueen(15, 15).white_queen_attack(b))
        self.assertFalse(queen.WhiteQueen(15, 0).white_queen_attack(b))
        self.assertFalse(queen.WhiteQueen(13, 6).white_queen_attack(b))
        result = [['p', 8, 8, 3, 13], ['p', 8, 8, 3, 3], ['p', 8, 8, 3, 8]]
        self.assertEqual(queen.WhiteQueen(8, 8).white_queen_attack(b), result)
        result = [['p', 5, 15, 3, 13], ['p', 5, 15, 3, 15]]
        self.assertEqual(queen.WhiteQueen(5, 15).white_queen_attack(b), result)
        result = [['q', 2, 6, 1, 7], ['b', 2, 6, 1, 5], ['p', 2, 6, 3, 7], ['p', 2, 6, 3, 5], ['p', 2, 6, 3, 6],
                  ['q', 2, 6, 1, 6], ['p', 2, 6, 2, 5], ['p', 2, 6, 2, 7]]
        self.assertEqual(queen.WhiteQueen(2, 6).white_queen_attack(b), result)


if __name__ == '__main__':
    unittest.main()
