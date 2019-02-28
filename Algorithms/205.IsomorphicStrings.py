class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        l = len(s)
        if l == 0 or l == 1:
            return True
        d = {t[0]:s[0]}
        for i in range(1, l):
            if t[i] in d:
                if d[t[i]] == s[i]:
                    continue
                else:
                    return False
            if s[i] in d.values():
                return False
            d[t[i]] = s[i]
        return True
