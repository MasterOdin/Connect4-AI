"""
main game logic
"""
from __future__ import print_function
from board import Board
from player import Player
from ai import AI


def run_game():
    """
    runs the game :D
    """
    game_board = Board()

    player1 = Player("1")
    player2 = AI("2")
    # players_turn = 1

    while game_board.has_winner(player1.piece, player2.piece):
        pass

    i = 0
    while i < 4:
        game_board.add_piece(i, 1)
        i += 1

    game_board.print_board()

if __name__ == "__main__":
    run_game()
