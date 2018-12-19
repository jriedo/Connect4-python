import numpy as np
import time

class Game:
    def __init__(self, start_player=1, board=None, comm=None, both_are_pc=False, player_1_ai=None, player_2_ai=None):
        self.token_1 = 1
        self.token_2 = 2

        self.ai_1 = player_1_ai
        self.ai_2 = player_2_ai

        self.both_are_pc = both_are_pc
        self.start_player = start_player

        self.board = board
        self.ac = comm
        self.total_time_p_1 = 0
        self.total_time_p_2 = 0

    def start(self):
        if self.start_player == 1:
            if self.both_are_pc:
                self.computer_move(self.token_1)
            else:
                self.human_move()
        else:
            self.computer_move(self.token_2)

    def human_move(self):
        try:
            move = int(input('enter move: ')) - 1
        except ValueError:
            print("not a valid move")
            self.human_move()

        if np.any(move == self.board.possible_drops()):
            self.board.drop(move, self.token_1)
            if self.board.is_game_over():
                if self.board.is_winner(self.token_1):
                    self.board.display(last_move=move)
                    print('yaaay, you won!')
                else:
                    print('well, at least a draw.')
            else:
                self.computer_move(self.token_2)
        else:
            print('Invalid move, think again!')
            self.human_move()

    def computer_move(self, token):
        delta = 0
        if token == 1:
            st = time.time()
            pos = self.ai_1.best_move(self.board)
            delta = time.time()-st
            self.total_time_p_1 = self.total_time_p_1 + delta

        else:
            st = time.time()
            pos = self.ai_2.best_move(self.board)
            delta = time.time()-st
            self.total_time_p_2 = self.total_time_p_2 + delta


        self.board.drop(pos, token)
        self.physical_drop(pos)
        self.board.display(last_move=pos)

        print('time elapsed: {:0.0f} s'.format(delta))
        if self.board.is_game_over():
            print('total time player 1: {} s'.format(self.total_time_p_1))
            print('total time player 2: {} s'.format(self.total_time_p_2))
            if self.board.is_winner(token):
                if self.both_are_pc:
                    print('player {} won!'.format(token))
                else:
                    print('you failed!')
            else:
                print('well, it is a draw.')
        else:
            if self.both_are_pc:
                self.computer_move(token=3 - token)
            else:
                self.human_move()

    def physical_drop(self, pos):
        self.spy.start()
        while(!self.spy.dropped):
            self.ac.drop(pos)