class Solution:
    # @param digits, a string
    # @return a string[]
    def letterCombinations(self, digits):
        letters = ["", "", "abc", "def", "ghi", "jkl", "mno",
                    "pqrs", "tuv", "wxyz"]
        results, phone = [], []

        def _dfs(digits, level):
            if level == len(digits):
                if level: results.append("".join(phone))
                return
            for c in letters[ord(digits[level]) - ord('0')]:
                phone.append(c)
                _dfs(digits, level+1)
                phone.pop()
        _dfs(digits, 0)
        return results
