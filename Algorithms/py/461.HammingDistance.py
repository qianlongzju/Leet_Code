class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        count = 0
        z = x ^ y
        for i in range(32):
            if z & 0x01 == 1:
                count += 1
            z >>= 1
        return count
