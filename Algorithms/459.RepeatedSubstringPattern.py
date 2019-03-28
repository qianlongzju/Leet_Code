class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in range(1, len(s)/2+1):
            sub = s[:i]
            if len(s) % len(sub) == 0:
                n = len(s) / len(sub)
                if s == sub * n:
                    return True
        return False
