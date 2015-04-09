class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        self.results = []
        self.current = []
        S = sorted(S)
        self.subsetsHelper(S, 0)
        return self.results

    def subsetsHelper(self, S, pos):
        self.results.append(self.current[:])
        for i in range(pos, len(S)):
            if i != pos and S[i] == S[i-1]: continue
            self.current.append(S[i])
            self.subsetsHelper(S, i+1)
            self.current.pop()
