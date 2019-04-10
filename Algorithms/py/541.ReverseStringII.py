class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = [c for c in s]
        i = 0
        while len(s) - i >= k:
            ii = i
            j = i + k - 1
            while ii < j:
                s[ii], s[j] = s[j], s[ii]
                ii += 1
                j -= 1
            i += 2*k
        else:
            j = len(s)-1
            while i < j:
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1
        return "".join(s)
