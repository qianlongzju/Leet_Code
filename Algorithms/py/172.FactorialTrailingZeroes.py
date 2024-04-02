class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        a = 5
        count = 0
        while a <= n:
            count += n//a
            a *= 5
        return count