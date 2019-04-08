class Solution(object):
    def maxTurbulenceSize(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 2:
            return len(A)
        elif len(A) == 2:
            return 1 if A[0] == A[1] else 2
        n = len(A)
        start = 0
        maxlen = 1
        for i in range(1, n-1):
            if A[i] == A[i-1]:
                start = i
                continue
            if (A[i+1]-A[i])*(A[i]-A[i-1]) < 0:
                continue
            maxlen = max(maxlen , i-start+1)
            start = i
        if (A[n-1]-A[n-2])*(A[n-2]-A[n-3]) < 0:
            maxlen = max(maxlen , n-1-start+1)
        return maxlen
