class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s = [c for c in s]
        t = [c for c in t]
        s.sort()
        t.sort()
        for i in range(len(s)):
            if t[i] != s[i]:
                return t[i]
        return t[-1]
