class Solution(object):
    def divisorSubstrings(self, num, k):
        """
        :type num: int
        :type k: int
        :rtype: int
        """
        c = 0
        for i in range(k, len(str(num))+1):
            s_num = int(str(num)[i-k:i])
            if s_num != 0 and num % s_num == 0:
                c += 1
        return c
