class Solution:
    # @return a list of integers
    def grayCode(self, n):
        v = []
        for i in range(1 << n):
            v.append((i >> 1) ^ i)
        return v
