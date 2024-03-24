class Solution(object):
    def minBitFlips(self, start, goal):
        """
        :type start: int
        :type goal: int
        :rtype: int
        """
        c = 0
        while start != 0 or goal != 0:
            if (start & 0x01) != (goal & 0x01):
                c += 1
            start >>= 1
            goal >>= 1
        return c
