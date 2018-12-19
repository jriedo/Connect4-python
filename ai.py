from board import Board

class AI:
    def __init__(self, player=1, depth=4, win=1000, loose=-1000):
        self.depth = depth
        self.move = -1
        self.token = player
        self.win = win
        self.loose = loose

    def best_move(self, board):
        alpha = -10000
        beta = 10000
        best_score = self._max_value(board, self.depth, alpha, beta)
        return self.move


    def _max_value(self, board, d, alpha, beta):

        if board.is_game_over() or d == 0:
            return board.eval(token=self.token)
        else:
            actions = board.possible_drops()

            score = -10000

            for a in actions:
                tmp_board = Board(board.positions.copy())
                tmp_board.drop(pos=a, token=self.token)
                s = self._min_value(board=tmp_board, d=d - 1, alpha=alpha, beta=beta)
                # update score, if score is higher than previous
                if s > score:
                    score = s
                    if d == self.depth:
                        self.move = a
                # update alpha, if a greater score was found
                if alpha < s:
                    alpha = s
                # stop searching if a lower score has already been found in other branch
                if beta <= alpha:
                    break
            return score

    def _min_value(self, board, d, alpha, beta):
        if board.is_game_over() or d == 0:
            return board.eval(token=self.token)
        else:
            actions = board.possible_drops()
            score = 10000

            for a in actions:
                tmp_board = Board(board.positions.copy())
                tmp_board.drop(pos=a, token=3-self.token)
                s = self._max_value(board=tmp_board, d=d - 1, alpha=alpha, beta=beta)
                if s < score:
                    score = s
                # update beta if a smaller score was found
                if beta > s:
                    beta = s
                # stop searching if a greater score has already been found in other branch
                if alpha >= beta:
                    break
            return score