from board import Board

"""
implements pure minimax, no pruning
"""
class AI:
    def __init__(self, player=1, depth=4):
        self.depth = depth
        self.move = -1
        self.token = player

    def best_move(self, board):
        best_score = self._max_value(board, self.depth)
        return self.move

    def _max_value(self, board, d):

        if board.is_game_over() or d == 0:
            return board.eval(token=self.token)
        else:
            actions = board.possible_drops()

            score = -10000

            for a in actions:
                tmp_board = Board(board.positions.copy())
                tmp_board.drop(pos=a, token=self.token)
                s = self._min_value(board=tmp_board, d=d - 1)
                if s > score:
                    score = s
                    if d == self.depth:
                        self.move = a
            return score

    def _min_value(self, board, d):
        if board.is_game_over() or d == 0:
            return board.eval(token=self.token)
        else:
            actions = board.possible_drops()
            score = 10000

            for a in actions:
                tmp_board = Board(board.positions.copy())
                tmp_board.drop(pos=a, token=3-self.token)
                s = self._max_value(board=tmp_board, d=d - 1)
                if s < score:
                    score = s
            return score