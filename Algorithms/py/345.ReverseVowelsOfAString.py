class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        t = 'aeiouAEIOU'
        s = [c for c in s]
        i, j = 0, len(s)-1
        while i < j:
            if s[i] not in t:
                i += 1
                continue
            if s[j] not in t:
                j -= 1
                continue
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return "".join(s)
