class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        wb = [False] * n
        for i in range(n):
            if wb[i] == False and s[:i+1] in wordDict:
                wb[i] = True
            if wb[i]:
                if i == n-1: return True
                for j in range(i+1, n):
                    if wb[j] == False and s[i+1:j+1] in wordDict:
                        wb[j] = True
                    if j == n-1 and wb[j]:return True
        return False
