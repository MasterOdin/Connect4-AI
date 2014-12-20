"""
main game logic
"""
from __future__ import print_function
from board import Board
from human import Human
from ai import AI

__author__ = "Matthew 'MasterOdin' Peveler"
__license__ = "The MIT License (MIT)"

def run_game():
    """
    runs the game :D
    """
    game_board = Board()

    player1 = Human("1")
    player2 = AI("2")
    print(player1, "vs", player2)
    # players_turn = 1

    while not game_board.has_winner:
        col = player1.get_move(game_board)
        game_board.add_piece(col, player1.piece)
        col = player2.get_move(game_board)
        game_board.add_piece(col, player2.piece)
        game_board.print_board()

if __name__ == "__main__":
    run_game()
