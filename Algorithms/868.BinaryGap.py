class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        flag = False
        max_dist = 0
        index = 0
        while N:
            if N & 0x01 == 1:
                if not flag:
                    flag = True
                else:
                    max_dist = max(max_dist, index-i)
                i = index
            N >>= 1
            index += 1
        return max_dist
