class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1, 0, -1):
            if nums[i] <= nums[i-1]:
                continue
            for j in range(len(nums)-1, i-1, -1):
                if nums[j] > nums[i-1]:
                    nums[i-1], nums[j] = nums[j], nums[i-1]
                    nums[i:] = nums[i:][::-1]
                    return
        nums[:] = nums[::-1]
