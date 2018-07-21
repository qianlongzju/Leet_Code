class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxProduct(self, A):
        max_product, min_product, result = A[0], A[0], A[0]
        for i in range(1, len(A)):
            mx, mn = max_product, min_product
            max_product = max(max(A[i], A[i] * mx), A[i] * mn)
            min_product = min(min(A[i], A[i] * mx), A[i] * mn)
            result = max(max_product, result)
        return result
