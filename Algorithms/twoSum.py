class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mapping = dict((num, i) for i, num in enumerate(nums))
        for i, num in enumerate(nums):
            gap = target - num
            if gap in mapping and mapping[gap] != i:
                return [i, mapping[gap]]
