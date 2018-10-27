class Solution:
    # @param nums, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, nums):
        nums.sort()
        result, permutation = [], []
        visited = [False] * len(nums)
        def _dfs():
            if len(permutation) == len(nums):
                result.append(permutation[:])
                return
            for i in range(len(nums)):
                if visited[i]: continue
                if i != 0 and nums[i] == nums[i-1] and visited[i-1] == False: continue
                visited[i] = True
                permutation.append(nums[i])
                _dfs()
                permutation.pop()
                visited[i] = False
        _dfs()
        return result
        
