class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 2:
            return n
        j = 1
        for i in range(2, n):
            if nums[i] != nums[j-1]:
                j += 1
                nums[j] = nums[i]
        return j+1
