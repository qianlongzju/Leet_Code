class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        index = [i for i in range(len(self.nums)) if self.nums[i] == target]
        import random
        k = random.randint(0, len(index)-1)
        return index[k]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
