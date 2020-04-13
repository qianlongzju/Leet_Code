class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        num, result = [-1] * n, []
        col, pie, na = set(), set(), set()
        def _dfs(level):
            if level == n:
                result.append(num)
                return
            for i in range(n):
                if i in col or level + i in pie or level - i in na:
                    continue
                num[level] = i
                col.add(i)
                pie.add(level + i)
                na.add(level - i)
                _dfs(level+1)
                col.remove(i)
                pie.remove(level + i)
                na.remove(level - i)

        _dfs(0)
        return len(result)

    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.count = 0
        self.dfs(n, 0, 0, 0, 0)
        return self.count

    def dfs(self, n, row, cols, pie, na):
        if row == n:
            self.count += 1
            return
        bits = (~(cols | pie | na)) & ((1 << n) - 1)
        while bits:
            p = bits & -bits
            self.dfs(n, row + 1, cols | p, (pie | p) << 1, (na | p) >> 1)
            bits &= bits - 1
