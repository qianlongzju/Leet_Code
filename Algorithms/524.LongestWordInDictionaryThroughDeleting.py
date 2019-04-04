class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        d.sort(key=lambda x: (-len(x), x))
        def match(s, t):
            i, j = 0, 0
            while i < len(s) and j < len(t):
                if s[i] == t[j]:
                    j += 1
                i += 1
            return j == len(t)
        for word in d:
            if match(s, word):
                return word
        return ""
