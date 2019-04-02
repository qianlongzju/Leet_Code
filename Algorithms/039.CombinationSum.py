class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        result, comb = [], []
        def dfs(target, level):
            if target == 0:
                result.append(comb[:])
                return
            for i in range(level, len(candidates)):
                if candidates[i] > target: break
                comb.append(candidates[i])
                dfs(target-candidates[i], i)
                comb.pop()
        dfs(target, 0)
        return result
