class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        def _check(c, used):
            if c == '.': return True
            if used[int(c)-1]: 
                return False
            else:
                used[int(c)-1] = True
                return True

        for i in range(9):
            used = [False] * 9
            for j in range(9):
                if not _check(board[i][j], used):
                    return False
            used = [False] * 9
            for j in range(9):
                if not _check(board[j][i], used):
                    return False
        for i in range(3):
            for j in range(3):
                used = [False] * 9
                for k in range(3):
                    for l in range(3):
                        if not _check(board[i*3+k][j*3+l], used):
                            return False
        return True
