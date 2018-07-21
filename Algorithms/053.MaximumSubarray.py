class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        maxEndingHere, maxSoFar = A[0], A[0]
        for i in range(1, len(A)):
            maxEndingHere = max(A[i], maxEndingHere + A[i])
            maxSoFar = max(maxSoFar, maxEndingHere)
        return maxSoFar
