class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        candidates.sort()
        self.result = []
        self.comb = []
        self.DFS(candidates, target, 0)
        return self.result
    
    def DFS(self, candidates, target, level):
        if target == 0:
            self.result.append(self.comb[:])
            return
        for i in range(level, len(candidates)):
            if candidates[i] > target: break
            self.comb.append(candidates[i])
            self.DFS(candidates, target-candidates[i], i)
            self.comb.pop()
