class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        maxlen, start, end, cur = 0, 0, 0, 0
        count = [0] * 26
        while end < len(s):
            i = ord(s[end]) - ord('A')
            count[i] += 1
            cur = max(cur, count[i])
            while end-start+1-cur > k:
                count[ord(s[start])-ord('A')] -= 1
                start += 1
            maxlen = max(maxlen, end-start +1)
            end += 1
        return maxlen
