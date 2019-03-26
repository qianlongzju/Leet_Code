class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sorted_nums = sorted(nums)
        count = 0
        for i in range(len(nums)):
            if nums[i] == sorted_nums[i]:
                count += 1
            else:
                break
        else:
            return 0
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == sorted_nums[i]:
                count += 1
            else:
                break
        return len(nums) - count
