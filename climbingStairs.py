class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        a = 1
        b = 1
        for i in range(1, n):
            temp = a + b
            a = b
            b = temp
        return b
