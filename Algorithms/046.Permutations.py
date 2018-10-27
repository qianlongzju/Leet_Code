class Solution:
    # @param nums, a list of integer
    # @return a list of lists of integers
    def permute(self, nums):
        result, permutation = [], []
        visited = [False] * len(nums)
        def _dfs():
            if len(permutation) == len(nums):
                result.append(permutation[:])
                return
            for i in range(len(nums)):
                if visited[i]: continue
                visited[i] = True
                permutation.append(nums[i])
                _dfs()
                permutation.pop()
                visited[i] = False
        _dfs()
        return result
        
