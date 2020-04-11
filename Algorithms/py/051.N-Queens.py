class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        num, result = [-1] * n, []
        col, pie, na = set(), set(), set()
        def _dfs(level):
            if level == n:
                result.append(_getBoard())
                return
            for i in range(n):
                if i in col or level + i in pie or level - i in na:
                    continue
                num[level] = i
                col.add(i)
                pie.add(level + i)
                na.add(level - i)
                #if _isValid(level):
                #    _dfs(level+1)
                _dfs(level+1)
                col.remove(i)
                pie.remove(level + i)
                na.remove(level - i)

        def _isValid(level):
            for i in range(level):
                if num[level] == num[i]:
                    return False
                if abs(num[level] - num[i]) == (level - i):
                    return False
            return True

        def _getBoard():
            return ['.'*i + 'Q' + '.'*(n-i-1) for i in num]
            #return ["".join(["Q" if i == number else "." for i in range(n) ]) for number in num]

        _dfs(0)
        return result
