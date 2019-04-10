class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        c = 0
        i = len(A)-1
        while i >= 0 and (K > 0 or c > 0):
            s = A[i] + K%10 + c
            A[i], c, K = s%10, s/10, K/10
            i -= 1
        while K > 0 or c > 0:
            s = K%10 + c
            K, c = K/10, s/10
            A.insert(0, s%10)
        return A
