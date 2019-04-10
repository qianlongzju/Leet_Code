class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math
        x = int((math.sqrt(8*n + 1) - 1) / 2)
        return x
