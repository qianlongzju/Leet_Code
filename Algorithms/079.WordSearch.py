class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def exist(self, board, word):
        def _dfs(board, word, m, n, level, i, j):
            if level == len(word): return True
            if i < 0 or j < 0 or i >= m or j >= n: return False
            if board[i][j] != word[level]: return False
            if visited[i][j]: return False
            visited[i][j] = True
            res = (_dfs(board, word, m, n, level+1, i-1, j)
                    or _dfs(board, word, m, n, level+1, i+1, j)
                    or _dfs(board, word, m, n, level+1, i, j-1)
                    or _dfs(board, word, m, n, level+1, i, j+1)
                    )
            visited[i][j] = False
            return res
        m, n = len(board), len(board[0])
        visited = [[False for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if _dfs(board, word, m, n, 0, i, j):
                    return True
        return False

