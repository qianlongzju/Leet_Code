class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        maxlen = 0
        count = 0
        start = 0
        for i in range(len(A)):
            if A[i] == 1:
                continue
            count += 1
            if count > K:
                maxlen = max(maxlen, i-start)
                while A[start] == 1:
                    start += 1
                start += 1
                count -= 1
        maxlen = max(maxlen, len(A)-1-start+1)
        return maxlen
