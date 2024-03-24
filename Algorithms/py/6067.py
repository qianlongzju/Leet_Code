class Solution(object):
    def waysToSplitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = sum(nums)
        n = len(nums)
        left = 0
        c = 0
        for i in range(n-1):
            left += nums[i]
            if left >= total - left:
                c += 1
        return c
