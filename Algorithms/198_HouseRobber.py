class Solution(object):
    def rob(self, nums):
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
