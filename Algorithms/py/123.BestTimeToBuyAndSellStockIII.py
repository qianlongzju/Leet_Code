class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        n = len(prices)
        if n <= 1:
            return 0
        left, right = [0 for i in range(n)], [0 for i in range(n)]
        minimum, maximum = prices[0], prices[n-1]
        for i in range(1, n):
            minimum = min(prices[i], minimum)
            left[i] = max(left[i-1], prices[i] - minimum)
        for i in range(n-2, -1, -1):
            maximum = max(prices[i], maximum)
            right[i] = max(right[i+1], maximum - prices[i])
        return max(left[i] + right[i] for i in range(n))

    def maxProfit(self, prices):
        if not prices: return 0
        res = 0
        profit = [[[0]*2 for _ in range(3)] for _ in range(len(prices))]

        profit[0][0][0], profit[0][0][1] = 0, -prices[0]
        profit[0][1][0], profit[0][1][1] = -sys.maxint, -sys.maxint
        profit[0][2][0], profit[0][2][1] = -sys.maxint, -sys.maxint

        for i in range(1, len(prices)):
            profit[i][0][0] = profit[i-1][0][0]
            profit[i][0][1] = max(profit[i-1][0][1], profit[i-1][0][0]-prices[i])

            profit[i][1][0] = max(profit[i-1][1][0], profit[i-1][0][1]+prices[i])
            profit[i][1][1] = max(profit[i-1][1][1], profit[i-1][1][0]-prices[i])

            profit[i][2][0] = max(profit[i-1][2][0], profit[i-1][1][1]+prices[i])

        end = len(prices) - 1
        return max(profit[end][0][0], profit[end][1][0], profit[end][2][0])

