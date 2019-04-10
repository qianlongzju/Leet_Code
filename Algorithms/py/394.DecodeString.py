class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if '[' not in s:
            return s
        for k in range(len(s)):
            if s[k].isdigit():
                break
        i = s.index('[')
        j = s.index(']')
        while s[:j+1].count(']') != s[:j+1].count('['):
            j = s.index(']', j+1)
        return s[:k] + self.decodeString(s[i+1:j]) * int(s[k:i]) + self.decodeString(s[j+1:])
