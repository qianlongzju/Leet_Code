class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        charMap = [-1] * 256
        i, maxLen = 0, 0
        for j in range(len(s)):
            if charMap[ord(s[j])] >= i:
                i = charMap[ord(s[j])] + 1
            charMap[ord(s[j])] = j
            maxLen = max(j - i + 1, maxLen)
        return maxLen
