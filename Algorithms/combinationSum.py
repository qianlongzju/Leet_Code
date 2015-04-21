class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        self.result = []
        self.comb = []
        candidates.sort()
        self.DFS(candidates, target, 0)
        return self.result
    
    def DFS(self, candidates, target, i):
        if sum(self.comb) == target:
            self.result.append(self.comb[:])
            return
        if sum(self.comb) > target:
            return
        for i in range(i, len(candidates)):
            self.comb.append(candidates[i])
            self.DFS(candidates, target, i)
            self.comb.pop()
