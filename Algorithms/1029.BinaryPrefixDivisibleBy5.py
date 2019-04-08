class Solution(object):
    def prefixesDivBy5(self, A):
        """
        :type A: List[int]
        :rtype: List[bool]
        """
        n = 0
        result = []
        for i in range(len(A)):
            n = (n << 1) + A[i]
            if n % 5 == 0:
                result.append(True)
            else:
                result.append(False)
        return result
