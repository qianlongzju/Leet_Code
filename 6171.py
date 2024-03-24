class Solution(object):
    def findSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n < 3:
            return False
        d = {}
        for i in range(n-1):
            if nums[i] + nums[i+1] not in d:
                d[nums[i] + nums[i+1]] = 1
            else:
                return True
        return False
