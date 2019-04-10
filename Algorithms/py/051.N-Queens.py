class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        num, result = [0] * n, []
        def _dfs(level):
            if level == n:
                result.append(_getBoard())
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

        def _getBoard():
            return ["".join(["Q" if i+1 == number else "." for i in range(n) ]) for number in num]

        _dfs(0)
        return result

