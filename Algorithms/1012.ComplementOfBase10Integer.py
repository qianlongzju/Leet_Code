class Solution(object):
    def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0:
            return 1
        result = 0
        i = 0
        while N > 0:
            if N & 0x01 == 0:
                result += 1 << i
            N >>= 1
            i += 1
        return result
