class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        s = [c for c in str]
        for i in range(len(s)):
            c = s[i]
            if ord(c) >= ord('A') and ord(c) <= ord('Z'):
                s[i] = chr(ord('a') - ord('A') + ord(c))
        return "".join(s)
