"""
This is the player module
"""
__author__ = "Matthew 'MasterOdin' Peveler"
__license__ = "The MIT License (MIT)"


class Player(object):
    """

    Attributes:
        piece: the piece that represents the player on the board
    """
    def __init__(self, piece):
        if type(piece) != str:
            raise TypeError("Piece should be of type str")
        self.piece = piece

    def get_move(self, board):
        """
        blah
        :return:
        """
        raise NotImplementedError("This isn't done yet")

    def get_type(self):
        """
        a dummy function
        :return:
        """
        raise NotImplementedError("This isn't done yet")

    def __str__(self):
        """
        String function
        :return:
        """
        return self.get_type()
