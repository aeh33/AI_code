def expand(self, depth):
    result = []
    if depth > 5:
        return result
    i = self.board.index(0)
    if not i in [6, 7, 8]:
        result.append(self.get_new_board(i, i + 3, moves))
    if not i in [2, 5, 8]:
        result.append(self.get_new_board(i, i + 1, moves))
    if not i in [0, 1, 2]:
        result.append(self.get_new_board(i, i - 3, moves))
    if not i in [0, 3, 6]:
        result.append(self.get_new_board(i, i - 1, moves))
    return result
