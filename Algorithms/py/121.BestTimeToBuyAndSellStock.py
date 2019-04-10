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
