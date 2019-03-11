class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = [0] * 26
        for c in s:
            count[ord(c) - ord('a')] += 1
        for i in range(len(s)):
            c = s[i]
            if count[ord(c) - ord('a')] == 1:
                return i
        return -1
