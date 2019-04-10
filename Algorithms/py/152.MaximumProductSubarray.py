class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        mx, mn, result = A[0], A[0], A[0]
        for i in range(1, len(A)):
            mx, mn = max(A[i], A[i] * mx, A[i] * mn), min(A[i], A[i] * mx, A[i] * mn)
            result = max(mx, result)
        return result
