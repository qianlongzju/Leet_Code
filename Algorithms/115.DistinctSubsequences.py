class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        n, m = len(s), len(t)
        result = [[0] * (n+1) for i in range(m+1)]
        result[0][0] = 1
        for i in range(1, m+1):
            result[i][0] = 0
        for j in range(1, n+1):
            result[0][j] = 1
        for i in range(1, m+1):
            for j in range(1, n+1):
                result[i][j] = result[i][j-1]
                if s[j-1] == t[i-1]:
                    result[i][j] += result[i-1][j-1]
        return result[m][n]
