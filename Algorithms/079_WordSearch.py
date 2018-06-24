class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        m, n = len(board), len(board[0])
        self.visited = [[False for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if self.DFS(board, word, m, n, 0, i, j):
                    return True
        return False

    def DFS(self, board, word, m, n, level, i, j):
        if level == len(word): return True
        if i < 0 or j < 0 or i >= m or j >= n: return False
        if board[i][j] != word[level]: return False
        if self.visited[i][j]: return False
        self.visited[i][j] = True
        res = (self.DFS(board, word, m, n, level+1, i-1, j)
                or self.DFS(board, word, m, n, level+1, i+1, j)
                or self.DFS(board, word, m, n, level+1, i, j-1)
                or self.DFS(board, word, m, n, level+1, i, j+1)
                )
        self.visited[i][j] = False
        return res
