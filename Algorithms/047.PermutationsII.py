class Solution:
    # @param nums, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, nums):
        nums.sort()
        self.result = []
        self.permutation = []
        self.isVisited = [False] * len(nums)
        self.DFS(nums)
        return self.result
        
    def DFS(self, nums):
        if len(self.permutation) == len(nums):
            self.result.append(self.permutation[:])
            return
        for i in range(len(nums)):
            if self.isVisited[i]: continue
            if i != 0 and nums[i] == nums[i-1] and self.isVisited[i] == self.isVisited[i-1]: continue
            self.isVisited[i] = True
            self.permutation.append(nums[i])
            self.DFS(nums)
            self.permutation.pop()
            self.isVisited[i] = False
