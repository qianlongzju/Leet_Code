class Solution(object):
    def rob_recursive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.mem = {}
        return self.rob_index(nums, 0)
    
    def rob_index(self, nums, index):
        if index >= len(nums):
            return 0
        if index in self.mem:
            return self.mem[index]
        
        self.mem[index] = max(nums[index] + self.rob_index(nums, index+2), self.rob_index(nums, index+1))
        return self.mem[index]

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[-1]
