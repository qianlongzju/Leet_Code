class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = set()
        n = len(nums)
        def helper(loc, tmp):
            if len(tmp) > 1 and tmp not in result:
                result.add(tmp)
            for i in range(loc+1, n):
                if nums[i] >= tmp[-1]:
                    helper(i, tmp + (nums[i], ))
        for i in range(n):
            helper(i, (nums[i], ))
        return [list(r) for r in result]
