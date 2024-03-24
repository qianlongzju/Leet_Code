class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins = sorted(coins)
        counts = [0] * (amount+1)
        for i in range(1, amount + 1):
            x = [counts[i-coin] for coin in coins if i >= coin]
            #print('x',x, amount, coins)
            if len(x) and min(x) >= 0:
                counts[i] = min(x) + 1
            else:
                counts[i] = -1
        if counts[amount] < 0:
            return -1
        else:
            return counts[amount]

