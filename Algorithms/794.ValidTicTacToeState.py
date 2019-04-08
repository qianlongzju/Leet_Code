class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        def win(c):
            for i in range(3):
                if all(board[i][j] == c for j in range(3)):
                    return True
            for j in range(3):
                if all(board[i][j] == c for i in range(3)):
                    return True
            if all(board[i][i] == c for i in range(3)):
                return True
            if all(board[i][2-i] == c for i in range(3)):
                return True
            return False
        def count():
            count_X, count_O = 0, 0
            for i in range(3):
                for j in range(3):
                    if board[i][j] == 'X':
                        count_X += 1
                    elif board[i][j] == 'O':
                        count_O += 1
            return count_X, count_O
        count_X, count_O = count()
        if count_O > count_X or count_O < count_X-1:
            return False
        if count_O == 0:
            return count_X <= 1
        win_x, win_o = win('X'), win('O')
        if win_x:
            return count_O == count_X-1
        if win_o:
            return count_O == count_X
        return True
