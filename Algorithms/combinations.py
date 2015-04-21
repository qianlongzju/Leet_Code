class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        self.result = []
        self.path = []
        self.DFS(n, k, 1)
        return self.result

    def DFS(self, n, k, level):
        if len(self.path) == k:
            self.result.append(self.path[:])
            return
        for i in range(level, n+1):
            self.path.append(i)
            self.DFS(n, k, i+1)
            self.path.pop()
