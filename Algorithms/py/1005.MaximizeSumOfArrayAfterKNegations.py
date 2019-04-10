class Solution(object):
    def largestSumAfterKNegations(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        A.sort()
        j = 0
        for i in range(K):
            if A[j] < 0:
                A[j] = -A[j]
                j += 1
            elif A[j] == 0:
                pass
            else:
                if j > 0 and A[j] > A[j-1]:
                    j -= 1
                    A[j] = -A[j]
                else:
                    A[j] = -A[j]
        return sum(A)
