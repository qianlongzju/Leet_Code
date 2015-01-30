class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        n = len(A)
        if n < 3:
            return 0
        leftToRight = [0] * n
        rightToLeft = [0] * n
        leftToRight[0] = 0
        rightToLeft[n-1] = 0
        for i in range(1, n):
            leftToRight[i] = max(leftToRight[i-1], A[i-1])
            rightToLeft[n-i-1] = max(rightToLeft[n-i], A[n-i])
        total = 0
        for i in range(1, n-1):
            height = min(leftToRight[i], rightToLeft[i])
            if height > A[i]: 
                total += height - A[i]
        return total
