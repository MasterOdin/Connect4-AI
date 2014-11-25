from __future__ import print_function
from board import Board

if __name__ == "__main__":
    game_board = Board()
    i = 0
    while i < 4:
        game_board.add_piece(i, 1)
        i += 1

    game_board.print_board()