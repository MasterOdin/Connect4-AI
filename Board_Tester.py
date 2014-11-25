"""
Tester for board module
"""

import nose
from board import Board


def test_new_board():
    """
    Test that new board has expected properties
    """
    test_board = Board()
    assert test_board.ROWS == 8
    assert test_board.COLUMNS == 8
    assert test_board.board == [[0]*8]*8


def test_add_piece():
    """
    Test adding a piece to the board
    """
    test_board = Board()
    test_board.add_piece(0, 2)
    assert test_board.board[0][test_board.ROWS-1] == 2 and \
        test_board.board[0][test_board.ROWS-2] == 0
    test_board.add_piece(0, 1)
    assert test_board.board[0][test_board.ROWS-1] == 2 and \
        test_board.board[0][test_board.ROWS-2] == 1



def test_check_win():
    """
    Test for checking for a connect 4
    """
    test_board = Board()
    i = 0
    while i < 4:
        test_board.add_piece(4, 1)
        i += 1

if __name__ == "__main__":
    nose.runmodule()
