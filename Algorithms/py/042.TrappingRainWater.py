class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n < 3:
            return 0
        leftToRight, rightToLeft = [0] * n, [0] * n
        leftToRight[0], rightToLeft[n-1] = 0, 0
        for i in range(1, n):
            leftToRight[i] = max(leftToRight[i-1], height[i-1])
            rightToLeft[n-i-1] = max(rightToLeft[n-i], height[n-i])
        total = 0
        for i in range(1, n-1):
            total += max(0, min(leftToRight[i], rightToLeft[i]) - height[i])
        return total