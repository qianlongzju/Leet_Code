class Solution(object):
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        m, n = len(A), len(A[0])
        total = 0
        for i in range(m):
            if A[i][0] == 0:
                for j in range(n):
                    A[i][j] = 1-A[i][j]
        for j in range(n-1, -1, -1):
            s = sum(A[i][j] for i in range(m))
            total += 2**(n-j-1) * max(s, m-s)
        return total
