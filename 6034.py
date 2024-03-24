class Solution(object):
    def triangularSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        newNums = [(a+b)%10 for a, b in zip(nums[0:-1], nums[1:])]
        return self.triangularSum(newNums)
