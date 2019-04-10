class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        digit = 1
        while n > digit * ((10**(digit-1)) * 9):
            n -= digit * ((10**(digit-1)) * 9)
            digit += 1
        t = n // digit 
        if n % digit == 0:
            return str(10**(digit-1)-1 + t)[-1]
        else:
            return str(10**(digit-1)-1 + t + 1)[n - t*digit-1]
