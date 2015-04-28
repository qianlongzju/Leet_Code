class Solution:
    # @param {integer} n
    # @return {integer}
    def totalNQueens(self, n):
        self.num = [0] * n
        self.result = 0
        self.DFS(n, 0)
        return self.result
        
    def DFS(self, n, level):
        if level == n:
            self.result += 1
            return
        for i in range(n):
            self.num[level] = i+1
            if self.isValid(level):
                self.DFS(n, level+1)
                
    def isValid(self, level):
        for i in range(level):
            if self.num[level] == self.num[i]:
                return False
            if abs(self.num[level] - self.num[i]) == (level - i):
                return False
        return True
