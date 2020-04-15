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
