class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum2(self, candidates, target):
        self.result = []
        self.comb = []
        candidates.sort()
        self.DFS(candidates, target, 0)
        return self.result
    
    def DFS(self, candidates, target, i):
        s = sum(self.comb)
        if s > target:
            return
        if s == target and self.comb not in self.result:
            self.result.append(self.comb[:])
            return
        for i in xrange(i, len(candidates)):
            if s + candidates[i] > target:
                return
            self.comb.append(candidates[i])
            self.DFS(candidates, target, i+1)
            self.comb.pop()


s = Solution()
candidates = [13,23,25,11,7,26,14,11,27,27,26,12,8,20,22,34,27,17,5,26,31,11,16,27,13,20,29,18,7,14,13,15,25,25,21,27,16,22,33,8,15,25,16,18,10,25,9,24,7,32,15,26,30,19]
print s.combinationSum2(candidates, 25)

candidates = [6,33,9,8,16,14,6,32,16,30,15,19,20,27,33,12,14,34,27,8,12,27,12,5,20,6,16,17,21,21,25,23,11,21,26,22,22,19,19,33,15,22,17,30,14,7,29,15,7,21,18,6,5,25,29,20,18]
print s.combinationSum2(candidates, 27)
