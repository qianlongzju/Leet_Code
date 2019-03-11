class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0 or num & (num-1) != 0:
            return False
        return (num & 0x55555555) != 0
