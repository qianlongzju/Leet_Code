class Solution:
    # @param {float} x
    # @param {integer} n
    # @return {float}
    def myPow(self, x, n):
        if n == 0:
            return 1.0
        positive = True
        if n < 0:
            positive = False
            n = -n
        result = 1.0
        while n:
            if n % 2: result *= x
            n /= 2
            x *= x
        return result if positive else 1/result
