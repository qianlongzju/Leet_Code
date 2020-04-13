class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        mx, mn, result = (A[0], ) * 3
        for i in range(1, len(A)):
            a, b = A[i] * mx, A[i] * mn
            mx, mn = max(A[i], a, b), min(A[i], a, b)
            result = max(mx, result)
        return result
