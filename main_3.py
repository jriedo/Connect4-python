import numpy as np
from board import Board
from ai import AI
from game import Game
from communication import  ArduinoCommunication

"""
works with different files for each class, no player class, choose which one to begin, both players may be computers
"""

if __name__ == '__main__':
    """
    player 1: human/pc
    player 2: pc
    """
    depth = 4
    WIN = 5000
    LOOSE = -5000
    DRAW = 0

    # human vs ai, human starts
    ac = ArduinoCommunication()
    mybrain = AI(player=2, depth=depth, win=WIN, loose=LOOSE)
    myboard = Board(win=WIN, loose=LOOSE, draw=DRAW)
    mygame = Game(start_player=1,board=myboard, comm=ac, both_are_pc=False, player_2_ai=mybrain)
    mygame.start()

    # # ai vs ai
    # brain_1 = AI(player=1, depth=10, win=WIN, loose=LOOSE)
    # brain_2 = AI(player=2, depth=10, win=WIN, loose=LOOSE)
    # myboard = Board(win=WIN, loose=LOOSE, draw=DRAW)
    # mygame = Game(start_player=2, board=myboard, both_are_pc=True, player_1_ai=brain_1, player_2_ai=brain_2)
    # mygame.start()
