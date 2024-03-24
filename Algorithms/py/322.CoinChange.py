class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        coins = sorted(coins)
        table = [-1] * (amount + 1)
        table[0] = 0
        for i in range(amount+1):
            for coin in coins:
                if i < coin:
                    break
                if table[i-coin] != -1:
                    if table[i] == -1:
                        table[i] = table[i-coin] + 1
                    else:
                        table[i] = min(table[i], table[i-coin] + 1)
        return table[-1]
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        coins = sorted(coins)
        table = [-1] * (amount + 1)
        table[0] = 0
        for i in range(amount+1):
            if table[i] == -1:
                continue
            for coin in coins:
                if i+coin > amount:
                    break
                if table[i+coin] != -1:
                    table[i+coin] = min(table[i+coin], table[i] + 1)
                else:
                    table[i+coin] = table[i] + 1
        return table[-1]
