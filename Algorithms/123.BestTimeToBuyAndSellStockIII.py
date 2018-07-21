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
