class Solution(object):
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        s = 0
        n = len(A)
        lefts, rights = [0] * n, [0] * n
        for i in range(n):
            left_n = 1
            while i-left_n >= 0 and A[i-left_n] > A[i]:
                left_n += lefts[i-left_n]
            lefts[i] = left_n
        for i in range(n-1, -1, -1):
            right_n = 1
            while i+right_n < n and A[i+right_n] >= A[i]:
                right_n += rights[i+right_n]
            rights[i] = right_n
        for i in range(n):
            s += A[i] * lefts[i] * rights[i]
        return s % (10**9 + 7)
