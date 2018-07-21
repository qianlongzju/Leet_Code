class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [-1, -1]
        low, high, middle = 0, len(nums)-1, 0
        while low <= high:
            middle = low + (high-low)/2;
            if nums[middle] < target:
                low = middle + 1
            elif nums[middle] > target:
                high = middle - 1
            if nums[middle] == target:
                break
        if nums[middle] != target:
            return [-1, -1]
        low = middle
        while low >= 0 and nums[low] == target:
            low -= 1
        high = middle
        while high < len(nums) and nums[high] == target:
            high += 1
        return  low+1, high-1
