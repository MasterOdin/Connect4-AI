"""
AI Module
"""
from __future__ import print_function
from player import Player
from heuristics import Random

__author__ = "Matthew 'MasterOdin' Peveler"
__license__ = "The MIT License (MIT)"

class AI(Player):
    """
    This is an AI player that implements some heuristic for move selection
    """
    def __init__(self, piece, heuristic=Random):
        super(AI, self).__init__(piece)
        self.heuristic = heuristic

    def get_move(self, board):
        """
        blah

        :return:
        """
        col = self.heuristic.get_best_column(board)
        print("Player", self.piece+" column ==>", col)
        return col

    def get_type(self):
        """
        just a dummy function
        :return:
        """
        return "AI Agent - " + self.heuristic.NAME + " (Player "+self.piece+")"
