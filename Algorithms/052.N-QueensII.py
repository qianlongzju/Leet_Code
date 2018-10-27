class Solution:
    # @param {integer} n
    # @return {integer}
    def totalNQueens(self, n):
        num, self.result = [0] * n, 0
        def _dfs(level):
            if level == n:
                self.result += 1
                return
            for i in range(n):
                num[level] = i+1
                if _isValid(level):
                    _dfs(level+1)

        def _isValid(level):
            for i in range(level):
                if num[level] == num[i]:
                    return False
                if abs(num[level] - num[i]) == (level - i):
                    return False
            return True
        _dfs(0)
        return self.result
