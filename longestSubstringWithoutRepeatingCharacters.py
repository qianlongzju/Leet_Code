class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        charMap = [-1] * 256
        i = 0
        maxLen = 0
        for j in range(len(s)):
            if charMap[ord(s[j])] >= i:
                i = charMap[ord(s[j])] + 1
            charMap[ord(s[j])] = j
            maxLen = max(j - i + 1, maxLen)
        return maxLen
