class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        self.num = [0] * n
        self.result = []
        self.DFS(n, 0)
        return self.result
        
    def DFS(self, n, level):
        if level == n:
            self.result.append(self.getBoard(n))
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
    
    def getBoard(self, n):
        result = []
        for number in self.num:
            row = ""
            for i in range(n):
                row += "Q" if i+1 == number else "."
            result.append(row)
        return result
        
