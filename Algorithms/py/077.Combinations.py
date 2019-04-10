class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        result, path = [], []
        def _dfs(level):
            if len(path) == k:
                result.append(path[:])
                return
            for i in range(level, n+1):
                path.append(i)
                _dfs(i+1)
                path.pop()
        _dfs(1)
        return result

