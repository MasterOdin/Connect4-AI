"""
This is the player module
"""
from __future__ import print_function


class Player(object):
    """

    Attributes:
        piece: the piece that represents the player on the board
    """
    def __init__(self, piece):
        self.piece = piece

    def get_move(self):
        """
        blah
        :return:
        """
        raise NotImplementedError("This isn't done yet")

    def blah(self):
        """
        a dummy function
        :return:
        """
        pass
