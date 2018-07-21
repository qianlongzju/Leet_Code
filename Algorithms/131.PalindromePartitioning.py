class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        self.result = []
        self.par = []
        self.partitionHelper(s, 0)
        return self.result
        
    def partitionHelper(self, s, start):
        if start == len(s):
            self.result.append(self.par[:])
            return
        
        for i in range(start+1, len(s)+1):
            t = s[start:i]
            if t == t[::-1]:
                self.par.append(t)
                self.partitionHelper(s, i)
                self.par.pop()
