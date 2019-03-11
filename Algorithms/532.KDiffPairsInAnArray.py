class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        result = set()
        i, j = 0, 1
        count = 0
        while i < len(nums) and j < len(nums):
            if i == j:
                j += 1
                continue
            diff = nums[j] - nums[i]
            if diff == k:
                result.add((nums[i], nums[j]))
                i += 1
                j += 1
            elif diff < k:
                j += 1
            else:
                i += 1
        return len(result)
