class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def check(i, j):
            target = 15
            iis = [i-1, i, i+1]
            jjs = [j-1, j, j+1]
            s = set()
            for ii in iis:
                for jj in jjs:
                    s.add(grid[ii][jj])
            if s != set(i for i in range(1, 10)):
                return False
            for ii in iis:
                if sum(grid[ii][jj] for jj in jjs) != target:
                    return False
            for jj in jjs:
                if sum(grid[ii][jj] for ii in iis) != target:
                    return False
            if sum(grid[i+d][j+d] for d in range(-1, 2)) != target:
                return False
            if sum(grid[i-d][j+d] for d in range(-1, 2)) != target:
                return False
            
            return True
        count = 0
        m, n = len(grid), len(grid[0])
        for i in range(1, m-1):
            for j in range(1, n-1):
                if check(i, j):
                    count += 1
        return count
