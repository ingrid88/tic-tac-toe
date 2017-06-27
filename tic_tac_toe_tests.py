import unittest
import tictactoe as tictactoe


class TestTicTacToe(unittest.TestCase):

    def test_first_column_player_one_wins(self):
        s = tictactoe.State([
            [1, 1, None],
            [1, 1, None],
            [1, None, None]], 1)

        self.assertEqual(tictactoe.did_win(s), True)

    def test_first_row_player_one_wins(self):
        s = tictactoe.State([
            [1, 1, None],
            [1, 1, 1],
            [None, None, None]], 0)

        self.assertEqual(tictactoe.did_win(s), True)

    def test_first_column_player_one_wins_2(self):
        s = tictactoe.State([
            [1, 1, None],
            [1, 1, None],
            [1, None, None]], 0)

        self.assertEqual(tictactoe.did_win(s), True)

    def test_top_diagonal_player_one_wins(self):
        s = tictactoe.State([
            [1, 1, None],
            [1, 1, None],
            [2, None, 1]], 1)

        self.assertEqual(tictactoe.did_win(s), True)

    def test_stalemate(self):
        s = tictactoe.State([
            [1, 1, 2],
            [2, 1, 1],
            [1, 2, 2]], 1)

        self.assertEqual(tictactoe.did_win(s), False)

    def test_top_diagonal_player_zero_wins(self):
        s = tictactoe.State([
            [2, 1, None],
            [1, 2, None],
            [2, None, 2]], 1)

        self.assertEqual(tictactoe.did_win(s), True)

    def test_noone_wins(self):
        s = tictactoe.State([
            [2, 1, None],
            [1, 2, None],
            [2, None, None]], 1)

        self.assertEqual(tictactoe.did_win(s), False)

    def test_empty_board_noone_wins(self):
        s = tictactoe.State([
            [None, None, None],
            [None, None, None],
            [None, None, None]], 1)

        self.assertEqual(tictactoe.did_win(s), False)

if __name__ == '__main__':
    unittest.main()
