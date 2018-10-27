class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        candidates.sort()
        result, comb = [], []
        def _dfs(candidates, target, level):
            if target == 0:
                result.append(comb[:])
                return
            for i in range(level, len(candidates)):
                if candidates[i] > target: break
                comb.append(candidates[i])
                _dfs(candidates, target-candidates[i], i)
                comb.pop()
        _dfs(candidates, target, 0)
        return result
    
