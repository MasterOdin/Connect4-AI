from __future__ import print_function


class Player(object):
    """

    Attributes:
        piece: the piece that represents the player on the board
    """
    def __init__(self, piece):
        self.piece = piece

    def get_move(self):
        raise NotImplementedError("This isn't done yet")

