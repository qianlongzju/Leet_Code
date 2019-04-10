class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        m = len(board)
        if m == 0:
            return
        n = len(board[0])
        for i in range(m):
            self.bfs(board, i, 0)
            self.bfs(board, i, n-1)
        for j in range(1, n-1):
            self.bfs(board, 0, j)
            self.bfs(board, m-1, j)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == '+':
                    board[i][j] = 'O'

    def bfs(self, board, i, j):
        n = len(board[0])
        q = []
        self.visit(board, i, j, q)
        while q:
            x = q.pop(0)
            ii = x / n
            jj = x % n
            self.visit(board, ii-1, jj, q)
            self.visit(board, ii+1, jj, q)
            self.visit(board, ii, jj-1, q)
            self.visit(board, ii, jj+1, q)

    def visit(self, board, i, j, q):
        m = len(board)
        n = len(board[0])
        if i < 0 or j < 0 or i >= m or j >= n or board[i][j] != 'O':
            return
        board[i][j] = '+';
        q.append(i * n + j)
