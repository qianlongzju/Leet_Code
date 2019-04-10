class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n == 0:
            return 0
        sell, buy, cool = [0] * n, [0] * n, [0] * n
        buy[0] = -prices[0]
        for i in range(1, n):
            sell[i] = max(buy[i-1]+prices[i], sell[i-1]) 
            buy[i] = max(cool[i-1]-prices[i], buy[i-1])
            cool[i] = max(sell[i-1], buy[i-1], cool[i-1])
        return sell[-1]
