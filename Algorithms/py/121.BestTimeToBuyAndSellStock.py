class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        if len(prices) <= 1: return 0
        minimum, maximum = prices[0], 0
        for i in range(1, len(prices)):
            minimum = min(prices[i], minimum)
            maximum = max(prices[i] - minimum, maximum)
        return maximum

    def maxProfit(self, prices):
        if not prices: return 0
        res = 0
        profit = [[0] * 3 for _ in range(len(prices))]

        profit[0][0], profit[0][1], profit[0][2] = 0, -prices[0], 0

        for i in range(1, len(prices)):
            profit[i][0] = profit[i-1][0]
            profit[i][1] = max(profit[i-1][1], profit[i-1][0] - prices[i])
            profit[i][2] = profit[i-1][1] + prices[i]
            res = max(res, profit[i][0],  profit[i][2])
        return res

    def maxProfit(self, prices):
        if not prices:
            return 0
        dp_i_0, dp_i_1 = 0, -sys.maxint
        for i in range(len(prices)):
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, -prices[i])
        return dp_i_0

    def maxProfit(self, prices):
        if not prices:
            return 0
        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]
        for i in range(n):
            if i == 0:
                dp[i][0] = 0
                dp[i][1] = -prices[i]
                continue
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], -prices[i])
        return dp[n - 1][0]

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        min_price = prices[0]
        profit = 0
        for price in prices[1:]:
            if price > min_price:
                profit = max(price-min_price, profit)
            min_price = min(price, min_price)
        return profit