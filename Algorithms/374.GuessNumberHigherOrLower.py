# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, high = 1, n
        while low <= high:
            i = low + (high - low) / 2
            if guess(i) == 0:
                return i
            elif guess(i) == 1:
                low = i + 1
            else:
                high = i - 1
        return 1
