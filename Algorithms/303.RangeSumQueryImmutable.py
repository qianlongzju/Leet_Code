class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.d = {}

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if (i, j) in self.d:
            return self.d[(i, j)]
        s = 0
        for k in range(i, j + 1):
            s += self.nums[k]
        self.d[(i, j)] = s
        return s

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
