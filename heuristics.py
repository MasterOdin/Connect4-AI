"""
AI Heuristics for various evaluation methods
"""
from __future__ import print_function
import random

__author__ = "Matthew 'MasterOdin' Peveler"
__license__ = "The MIT License (MIT)"


class Heuristic(object):
    """
    This is the heuristic interface
    """
    @staticmethod
    def get_best_column(board):
        """
        Get the best column based on some heuristic
        :param board:
        :return:
        """
        raise NotImplementedError("Not yet implemented")

    @staticmethod
    def get_column_value(board, column):
        """
        Get the particular value for a column based on some heuristic
        :param board:
        :param column:
        :return:
        """
        raise NotImplementedError("Not yet implemented")


class Random(Heuristic):
    """
    Random heuristic. Just returns valid random column
    """
    NAME = "Random"

    def __init__(self):
        pass

    @staticmethod
    def get_best_column(board):
        col = -1
        while not board.can_add_piece(col):
            col = random.randint(0, board.COLUMNS)
        return col

    @staticmethod
    def get_column_value(board, column):
        pass


class MinMax(Heuristic):
    """
    MinMax heuristic for AI agent
    """
    NAME = "MinMax"

    def __init__(self):
        pass

    @staticmethod
    def get_best_column(board):
        pass

    @staticmethod
    def get_column_value(board, column):
        pass
