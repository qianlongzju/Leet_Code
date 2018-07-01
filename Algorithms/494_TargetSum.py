class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        m = {}
        return self.findTargetSumWaysInterval(nums, 0, len(nums)-1, S, m)
    
    def findTargetSumWaysInterval(self, nums, start, end, S, m):
        if start > end:
            return S == 0
        if (start, S) in m:
            return m[(start, S)]
        t = self.findTargetSumWaysInterval(nums, start+1, end, S+nums[start], m) + self.findTargetSumWaysInterval(nums, start+1, end, S-nums[start], m)
        m[(start, S)] = t
        return t
