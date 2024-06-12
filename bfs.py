class State:
    def _init_(self, board, goal, depth=0):
        self.board = board
        self.depth = depth
        self.goal = goal

    def get_new_board(self, i1, i2, depth):
        new_board = self.board[:]
        new_board[i1], new_board[i2] = new_board[i2], new_board[i1]
        return State(new_board, self.goal, depth)

    def expand(self, depth):
        result = []
        i = self.board.index(0)
        if not i in [0, 3, 6]:
            result.append(self.get_new_board(i, i - 1, depth))
        if not i in [0, 1, 2]:
            result.append(self.get_new_board(i, i - 3, depth))
        if not i in [2, 5, 8]:
            result.append(self.get_new_board(i, i + 1, depth))
        if not i in [6, 7, 8]:
            result.append(self.get_new_board(i, i + 3, depth))
        return result

    def __str__(self):
        return (
            str(self.board[:3])
            + "\n"
            + str(self.board[3:6])
            + "\n"
            + str(self.board[6:])
            + "\n"
            + "------------------"
        )

    def __eq__(self, other):
        return self.board == other.board

    def __ne__(self, other):
        return self.board != other.board


puzzle = [2, 8, 3, 1, 6, 4, 7, 0, 5]

goal = [1, 2, 3, 8, 0, 4, 7, 6, 5]
