class Solution(object):
    def longestArithSeqLength(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        def helper(A):
            dp = [[1] * 20000 for i in range(len(A))]
            ans = 1
            for i in range(1, len(A)):
                for j in range(i-1, -1, -1):
                    diff = A[i]-A[j]
                    diff += 10000
                    dp[i][diff] = max(dp[i][diff], dp[j][diff] + 1)
                    ans = max(ans, dp[i][diff])
            return ans
        return helper(A)
        #return max(helper(A), helper(A[::-1]))
