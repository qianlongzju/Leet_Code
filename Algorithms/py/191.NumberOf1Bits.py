class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        for i in range(32):
            if n & 1 == 1:
                count += 1
            n >>= 1
        return count

    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        cnt = 0
        while n:
            n &= (n - 1)
            cnt += 1
        return cnt
