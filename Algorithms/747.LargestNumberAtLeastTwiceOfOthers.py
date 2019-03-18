class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return -1
        m = max(nums)
        j = nums.index(m)
        for i in range(len(nums)):
            if i != j and m < nums[i] * 2:
                return -1
        return nums.index(m)
