"""
Tester for board module
"""
from __future__ import print_function
from board import Board
from six import StringIO


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


def test_check_win_column():
    """
    Test for checking for a connect 4
    """
    test_board = Board()
    i = 0
    while i < 4:
        test_board.add_piece(4, 1)
        i += 1
    assert test_board.check_winner(1)

    test_board.clear_board()


def test_check_win_row():
    """
    Test for checking for a connect 4 on a row
    """
    test_board = Board()
    i = 0
    while i < 4:
        test_board.add_piece(i, 1)
        i += 1

    assert test_board.board[0][test_board.ROWS-1] == 1
    assert test_board.board[1][test_board.ROWS-1] == 1
    assert test_board.board[2][test_board.ROWS-1] == 1
    assert test_board.board[3][test_board.ROWS-1] == 1
    assert test_board.board[3][test_board.ROWS-2] == 0
    assert test_board.check_winner(1)


def test_check_no_win():
    test_board = Board()
    assert test_board.check_winner(1) is False


def test_check_print_board_empty():
    """
    blah
    """
    test_board = Board()
    out = StringIO()
    test_board.print_board(out=out)
    expected = ("0 "*8+"\n")*8
    assert expected == out.getvalue()