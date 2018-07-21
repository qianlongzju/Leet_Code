class Solution:
    # @param digits, a string
    # @return a string[]
    def letterCombinations(self, digits):
        self.letters = ["", "", "abc", "def", "ghi", "jkl", "mno",
                    "pqrs", "tuv", "wxyz"]
        self.results = []
        self.phone = []
        self.DFS(digits, 0)
        return self.results
        
    def DFS(self, digits, level):
        if level == len(digits):
            if level: self.results.append("".join(self.phone))
            return
        for c in self.letters[ord(digits[level]) - ord('0')]:
            self.phone.append(c)
            self.DFS(digits, level+1)
            self.phone.pop()
