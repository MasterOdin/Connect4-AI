"""
Tester for board module
"""
from __future__ import print_function
from six import StringIO
from board import Board
import tests.test_boards as test_boards


def test_new_board():
    """
    Test that new board has expected properties
    """
    test_board = Board()
    assert test_board.ROWS == 8
    assert test_board.COLUMNS == 8
    assert test_board.board == [[0]*8]*8


def test_check_print_board_empty():
    """
    Check to see if printing empty board works right
    """
    test_board = Board()
    out = StringIO()
    test_board.print_board(out=out)
    expected = ("0 "*8+"\n")*8+"\n"
    assert expected == out.getvalue()


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


def test_add_piece_invalid_column():
    """
    Test adding a piece to the board outside of the columns
    """
    test_board = Board()
    assert test_board.can_add_piece(-1) is False and \
           test_board.add_piece(-1, 1) is False
    assert test_board.can_add_piece(test_board.COLUMNS) is False and \
           test_board.add_piece(test_board.COLUMNS, 1) is False


def test_add_piece_full_column():
    """
    Attempt to add a piece to a full column
    """
    test_board = Board()
    i = 0
    while i < test_board.ROWS:
        assert test_board.can_add_piece(0) is True and \
            test_board.add_piece(0, 1) is True
        i += 1
    assert test_board.can_add_piece(0) is False and \
        test_board.add_piece(0, 1) is False


def test_print_with_few_pieces():
    """
    Print the board that contains a few pieces
    """
    test_board = Board()
    test_board.add_piece(0, 2)
    test_board.add_piece(5, 1)
    test_board.add_piece(6, 2)
    out = StringIO()
    test_board.print_board(out=out)
    expected = ("0 "*test_board.COLUMNS+"\n")*(test_board.ROWS-1)
    expected += "2 0 0 0 0 1 2 " + ("0 "*(test_board.COLUMNS-7))+"\n\n"
    assert expected == out.getvalue()


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


def test_check_win_vertical():
    """
    Test for checking if connect 4 on vertical axis in corners (bounds)
    """
    test_board = Board()
    test_board.board = test_boards.VERTICAL_WIN_1
    assert test_board.check_winner(1)
    test_board.board = test_boards.VERTICAL_WIN_2
    assert test_board.check_winner(2)
    test_board.board = test_boards.VERTICAL_WIN_3
    assert test_board.check_winner(1)
    test_board.board = test_boards.VERTICAL_WIN_4
    assert test_board.check_winner(2)


def test_check_win_horizontal():
    """
    Test for checking if connect 4 on horizontal axis in corners (bounds)
    """
    test_board = Board()
    test_board.board = test_boards.HORIZONTAL_WIN_1
    assert test_board.check_winner(1)
    test_board.board = test_boards.HORIZONTAL_WIN_2
    assert test_board.check_winner(2)
    test_board.board = test_boards.HORIZONTAL_WIN_3
    assert test_board.check_winner(1)
    test_board.board = test_boards.HORIZONTAL_WIN_4
    assert test_board.check_winner(2)


def test_check_no_win():
    """
    test for if board returns false if no winner
    """
    test_board = Board()
    assert test_board.check_winner(1) is False
