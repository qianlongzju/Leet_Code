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
