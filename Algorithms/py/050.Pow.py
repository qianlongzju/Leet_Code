class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1.0
        positive = True
        if n < 0:
            positive = False
            n = -n
        result = 1.0
        while n:
            if n & 1: 
                result *= x
            n /= 2
            x *= x
        return result if positive else 1/result
