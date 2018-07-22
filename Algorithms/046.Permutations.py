class Solution:
    # @param nums, a list of integer
    # @return a list of lists of integers
    def permute(self, nums):
        self.result = []
        self.permutation = []
        self.isVisited = [False] * len(nums)
        self.dfs(nums)
        return self.result
        
    def dfs(self, nums):
        if len(self.permutation) == len(nums):
            self.result.append(self.permutation[:])
            return
        for i in range(len(nums)):
            if self.isVisited[i]: continue
            self.isVisited[i] = True
            self.permutation.append(nums[i])
            self.dfs(nums)
            self.permutation.pop()
            self.isVisited[i] = False
