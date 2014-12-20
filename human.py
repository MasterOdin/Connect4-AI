"""
Human Module
"""
from player import Player
from six import PY2

__author__ = "Matthew 'MasterOdin' Peveler"
__license__ = "The MIT License (MIT)"


class Human(Player):
    """
    this is the AI base class?
    """
    def get_move(self, board):
        """

        :return:
        """
        while True:
            col = input("Player "+self.piece+" Column ==> ").strip()
            if not col.isdigit() or not board.can_add_piece(int(col)):
                continue
            else:
                return int(col)

    def get_type(self):
        """
        return that this is a human player
        :return: (str) "Human"
        """
        return "Human (Player "+self.piece+")"

# fix for input so works same as Python 2 & 3
if PY2:
    # pylint: disable=undefined-variable, invalid-name, redefined-builtin
    input = raw_input
else:
    pass
