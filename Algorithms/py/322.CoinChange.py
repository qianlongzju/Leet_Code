class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount <= 0:
            return 0
        coins = sorted(coins)
        table = [0] * amount
        for coin in coins:
            if coin > amount:
                continue
            table[coin-1] = 1
        for i in range(amount):
            if table[i] != 0:
                continue
            l = [table[i-coins[j]] for j in range(len(coins))
                    if i >= coins[j] and table[i-coins[j]] != 0]
            if len(l) == 0:
                continue
            table[i] = min(l) + 1
        return table[-1]
