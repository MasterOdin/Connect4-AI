"""
This module contains logic for a Connect-4 board
"""


class Board(object):
    """
    This Board contains all the information for a Connect-4 board

    Attributes:
        board (list of lists): a column major list of list containing the
            Connect4 Board. The list is added to from bottom up for the row
            (so ROWS-1, then ROWS-2, etc.)
        COLUMNS: number of columns in the board
        ROWS: number of rows in the board
    """
    COLUMNS = 8
    ROWS = 8

    def __init__(self):
        self.board = [[0 for x in range(self.ROWS)]
                      for y in range(self.COLUMNS)]

    def add_piece(self, column, player):
        """

        :param column:
        :param player:
        :return:
        """
        piece_added = False
        for row in range(self.COLUMNS-1, -1, -1):
            if self.board[column][row] == 0:
                self.board[column][row] = player
                piece_added = True
                break
        return piece_added

    def check_winner(self, player):
        """

        :param player:
        :return:
        """
        # check down a column
        count = 0
        for i in range(self.COLUMNS):
            for j in range(self.ROWS):
                if self.board[i][j] == player:
                    count += 1
                else:
                    count = 0

                if count == 4:
                    return True
            count = 0

        # check across a row
        count = 0
        for i in range(self.ROWS):
            for j in range(self.COLUMNS):
                if self.board[j][i] == player:
                    count += 1
                else:
                    count = 0
                if count == 4:
                    return True
            count = 0
        return False
