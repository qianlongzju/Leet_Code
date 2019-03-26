class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            j = abs(nums[i])-1
            nums[j] = -abs(nums[j])
        return [i+1 for i in range(len(nums)) if nums[i] > 0]
