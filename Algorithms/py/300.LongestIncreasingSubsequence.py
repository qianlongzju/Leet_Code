class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        length_list = [1] * len(nums)
        for i in range(len(nums)):
            smaller = [length_list[j] for j in range(0, i) if nums[j] < nums[i]]
            if len(smaller) == 0:
                continue
            length_list[i] = max(smaller) + 1
        return max(length_list)
