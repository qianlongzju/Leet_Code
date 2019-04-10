class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        m = {}
        def dfs(i, S):
            if i >= len(nums):
                return S == 0
            if (i, S) in m:
                return m[(i, S)]
            t = dfs(i+1, S+nums[i]) + dfs(i+1, S-nums[i])
            m[(i, S)] = t
            return t
        return dfs(0, S)
