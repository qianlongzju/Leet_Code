class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        def _isValid(board, x, y):
            for i in range(9):
                if i != x and board[i][y] == board[x][y]:
                    return False
                if i != y and board[x][i] == board[x][y]:
                    return False
            for i in range((x/3)*3, (x/3+1)*3):
                for j in range((y/3)*3, (y/3+1)*3):
                    if i != x and j != y and board[i][j] == board[x][y]:
                        return False
            return True

        def _solveSudokuHelper(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] != '.':
                        continue
                    for k in range(9):
                        board[i][j] = str(k + 1)
                        if _isValid(board, i, j) and _solveSudokuHelper(board):
                            return True
                    board[i][j] = '.'
                    return False
            return True

        _solveSudokuHelper(board)

