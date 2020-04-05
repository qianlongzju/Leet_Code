class Solution(object):
    def maxSumTwoNoOverlap(self, A, L, M):
        """
        :type A: List[int]
        :type L: int
        :type M: int
        :rtype: int
        """
        n = len(A)
        def helper(arr, l):
            result = sum(arr[:l])
            maximum = result
            for i in range(l, len(arr)):
                result += arr[i]-arr[i-l]
                maximum = max(maximum, result)
            return maximum
        
        result = sum(A[:L+M])
        for l in range(n):
            if l >= L and n-l >= M:
                result = max(result, helper(A[:l], L) + helper(A[l:], M))
            if l >= M and n-l >= L:
                result = max(result, helper(A[:l], M) + helper(A[l:], L))
        return result
