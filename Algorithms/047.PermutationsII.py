class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        num.sort()
        self.result = []
        self.permutation = []
        self.isVisited = [False] * len(num)
        self.DFS(num)
        return self.result
        
    def DFS(self, num):
        if len(self.permutation) == len(num):
            self.result.append(self.permutation[:])
            return
        for i in range(len(num)):
            if self.isVisited[i]: continue
            if i != 0 and num[i] == num[i-1] and self.isVisited[i] == self.isVisited[i-1]: continue
            self.isVisited[i] = True
            self.permutation.append(num[i])
            self.DFS(num)
            self.permutation.pop()
            self.isVisited[i] = False