class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        result = 0
        i = 0
        while num > 1:
            if num % 2 == 0:
                result += 1 << i
            num >>= 1
            i += 1
        return result
