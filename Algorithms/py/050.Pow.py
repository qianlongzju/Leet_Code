class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1.0
        if n < 0:
            return 1/self.myPow(x, -n)
        result = 1.0
        while n:
            if n & 1: 
                result *= x
            n //= 2
            x *= x
        return result