class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        result = []
        i, j = 0, len(A)-1
        while i < j:
            if abs(A[i]) < abs(A[j]):
                result.insert(0, A[j] ** 2)
                j -= 1
            else:
                result.insert(0, A[i] ** 2)
                i += 1
        result.insert(0, A[i] ** 2)
        return result
