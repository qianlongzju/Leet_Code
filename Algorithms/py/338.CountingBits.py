class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result = [0]
        k = 0
        while True:
            for i in range(2**k, 2**(k+1)):
                if i > num:
                    return result
                result.append(result[i-2**k] + 1)
            k += 1

    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result = [0] * (num + 1)
        for i in range(1, num + 1):
            result[i] = result[i & (i-1)] + 1
        return result
