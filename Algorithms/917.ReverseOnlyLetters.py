class Solution(object):
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        s = [c for c in S]
        i, j = 0, len(s)-1
        while i < j:
            while i < len(s) and not s[i].isalpha():
                i += 1
            while j >= 0 and not s[j].isalpha():
                j -= 1
            if i < j:
                s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
        return "".join(s)
