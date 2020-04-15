# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/solution/yi-ge-tong-yong-fang-fa-tuan-mie-6-dao-gu-piao-wen/
# https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/solution/tuan-mie-fang-fa-de-pythonshi-xian-by-jiang-yun-ji/
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        n = len(prices)
        if k >= n//2:
            res = 0
            for i in range(1,n):
                if prices[i] > prices[i-1]:
                    res += prices[i] - prices[i-1]
            return res
        P = [[[0]*2 for _ in range(k+1)] for _ in range(n)]
        for kk in range(k+1):
                P[-1][kk][1] = -float('inf')
                P[0][kk][1] = -float('inf')
        for i in range(n):
            for kk in range(1, k+1):
                P[i][kk][0] = max(P[i-1][kk][0], P[i-1][kk][1]+prices[i])
                P[i][kk][1] = max(P[i-1][kk][1], P[i-1][kk-1][0]-prices[i])
        return P[-1][-1][0]

    def maxProfit_k_inf(self, prices):
        n = len(prices)
        dp_i_0, dp_i_1 = 0, -sys.maxint
        for i in range(n):
            temp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, temp - prices[i])
        return dp_i_0

    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if k > n / 2:
            return self.maxProfit_k_inf(prices)

        dp = [[[0]*2 for _ in range(k+1)] for _ in range(n)]
        for kk in range(k+1):
            dp[-1][kk][1] = -float('inf')
            dp[0][kk][1] = -float('inf')
        for i in range(n):
            for kk in range(1, k+1):
                dp[i][kk][0] = max(dp[i-1][kk][0], dp[i-1][kk][1] + prices[i])
                dp[i][kk][1] = max(dp[i-1][kk][1], dp[i-1][kk-1][0] - prices[i])
        return dp[-1][-1][0]
