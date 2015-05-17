class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a string[]
    def wordBreak(self, s, wordDict):
        self.result = []
        self.sentence = []
        f = [True] + [False for i in range(len(s))]
        self.words = [[False for i in range(len(s))] for j in range(len(s)+1)]
        for i in range(1, len(s)+1):
            for j in range(i-1, -1, -1):
                if f[j] and s[j:i] in wordDict:
                    f[i] = True
                    self.words[i][j] = True
        self.DFS(s, len(s))
        return self.result

    def DFS(self, s, level):
        if level == 0:
            self.result.append(" ".join(self.sentence[::-1]))
            return
        for i in range(level):
            if self.words[level][i]:
                self.sentence.append(s[i:level])
                self.DFS(s, i)
                self.sentence.pop()
