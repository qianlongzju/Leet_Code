class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1:
            return n
        max_length, length = 1, 1
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                length += 1
            else:
                max_length = max(max_length, length)
                length = 1
        max_length = max(max_length, length)
        return max_length
