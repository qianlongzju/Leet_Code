class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        candidates = range(1, 10)
        result, comb = [], []
        def dfs(target, level):
            if len(comb) > k:
                return
            if target == 0 and len(comb) == k:
                result.append(comb[:])
                return
            for i in range(level, len(candidates)):
                if candidates[i] > target: break
                comb.append(candidates[i])
                dfs(target-candidates[i], i+1)
                comb.pop()
        dfs(n, 0)
        return result
