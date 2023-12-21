'''
Tic-Tac-Toe Game
-------------------------------------------------------------
'''

import random

class TicTacToe:

    def __init__(self) -> None:
        self.board = []

    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.apend('-')
            self.board.append(row)