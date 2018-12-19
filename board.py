import numpy as np


class Board:
    def __init__(self, positions=None, win=1000, loose=-1000, draw=0):
        self.win = win
        self.loose = loose
        self.draw = draw
        self.roundcount=1

        if positions is not None:
            self.positions = positions
        else:
            self.positions = np.zeros((6, 7), dtype=np.int)

    def display(self, last_move=None):
        if last_move is None:
            print('\n{}. Board:\n'.format(self.roundcount) + '-' * 14)
            self.roundcount+=1
        else:
            print('\n{}. Board (last move {}):\n'.format(self.roundcount, last_move+1) + '-' * 14)
            self.roundcount+=1
        print(' '.join(map(str, np.arange(7) + 1)) + '\n')
        for line in self.positions:
            print(' '.join(map(str, line)))
        print('-' * 14)

    def drop(self, pos, token):
        if pos in self.possible_drops():
            idxs = np.arange(6)
            idx = idxs[self.positions[:, pos] == 0][-1]
            self.positions[idx, pos] = token
        else:
            print('impossible move!')

    def is_game_over(self):
        if self.possible_drops().size == 0 or self.is_winner(1) or self.is_winner(2):
            return True
        return False

    def possible_drops(self):
        idxs = np.arange(7)
        positions = idxs[self.positions[0, :] == 0]
        return positions

    def eval(self, token):

        if self.is_winner(token=token):
            return self.win

        elif self.is_winner(token=3 - token):
            return self.loose

        else:
            weights = np.array(
                [[3, 4, 5, 7, 5, 4, 3], [4, 6, 8, 10, 8, 6, 4], [5, 8, 11, 13, 11, 8, 5], [5, 8, 11, 13, 11, 8, 5],
                 [4, 6, 8, 10, 8, 6, 4], [3, 4, 5, 7, 5, 4, 3]])
            value = np.sum(np.multiply(np.array(self.positions == token), weights))
            # three = self.series_of_three(token=token)

            return self.draw + value# +three


    def is_winner(self, token):

        # horizontal
        for row in self.positions:
            for starts in np.arange(self.positions.shape[1] - 4 + 1):
                if row[starts:starts + 4].sum() == 4 * token and all(np.equal(row[starts], row[starts:starts + 4])):
                    return True

        # vertical
        for col in self.positions.T:
            for starts in np.arange(self.positions.shape[0] - 4 + 1):
                if col[starts:starts + 4].sum() == 4 * token and all(np.equal(col[starts], col[starts:starts + 4])):
                    return True

        # diagonal top left - bottom right
        for row in np.arange(self.positions.shape[0] - 4 + 1):
            for col in np.arange(self.positions.shape[1] - 4 + 1):
                b = self.positions
                summation = b[row, col] + b[row + 1, col + 1] + b[row + 2, col + 2] + b[row + 3, col + 3]
                all_same = all([b[row, col] == b[row + 1, col + 1], b[row, col] == b[row + 2, col + 2],
                                b[row, col] == b[row + 3, col + 3]])
                if summation == 4 * token and all_same:
                    return True

        # diagonal bottom left - top right
        for row in np.arange(self.positions.shape[0] - 4 + 1) + 3:
            for col in np.arange(self.positions.shape[1] - 4 + 1):
                b = self.positions
                summation = b[row, col] + b[row - 1, col + 1] + b[row - 2, col + 2] + b[row - 3, col + 3]
                all_same = all([b[row, col] == b[row - 1, col + 1], b[row, col] == b[row - 2, col + 2],
                                b[row, col] == b[row - 3, col + 3]])
                if summation == 4 * token and all_same:
                    return True
        return False

    def series_of_three(self, token, num=3):
        # function to count series of three (or whatever is specified by num)
        count = 0
        # horizontal
        for row in self.positions:
            for starts in np.arange(self.positions.shape[1] - num + 1):
                if row[starts:starts + num].sum() == num * token and all(np.equal(row[starts], row[starts:starts + num])):
                    count += 1

        # vertical
        for col in self.positions.T:
            for starts in np.arange(self.positions.shape[0] - num + 1):
                if col[starts:starts + num].sum() == num * token and all(np.equal(col[starts], col[starts:starts + num])):
                    count += 1

        # diagonal top left - bottom right
        for row in np.arange(self.positions.shape[0] - num + 1):
            for col in np.arange(self.positions.shape[1] - num + 1):
                b = self.positions
                summation = b[row, col] + b[row + 1, col + 1] + b[row + 2, col + 2]
                all_same = all([b[row, col] == b[row + 1, col + 1], b[row, col] == b[row + 2, col + 2]])
                if summation == num * token and all_same:
                    count += 1

        # diagonal bottom left - top right
        for row in np.arange(self.positions.shape[0] - num + 1) + (num - 1):
            for col in np.arange(self.positions.shape[1] - num + 1):
                b = self.positions
                summation = b[row, col] + b[row - 1, col + 1] + b[row - 2, col + 2]
                all_same = all([b[row, col] == b[row - 1, col + 1], b[row, col] == b[row - 2, col + 2]])
                if summation == num * token and all_same:
                    count += 1
        return count
