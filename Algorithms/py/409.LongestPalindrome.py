class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        import collections
        c = collections.Counter(s)
        count = 0
        odd = 0
        for k, v in c.items():
            if v & 0x01 == 1:
                odd = 1
            count += v // 2
        return odd + count * 2
