class Solution(object):
    def rearrangeCharacters(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: int
        """
        d1 = {}
        d2 = {}
        for c in s:
            if c not in d1:
                d1[c] = 0
            d1[c] += 1
        for c in target:
            if c not in d2:
                d2[c] = 0
            d2[c] += 1 
        t = None
        for c in d2:
            if c not in d1 or d1[c] < d2[c]:
                return 0
            if not t:
                t = int(d1[c]/d2[c])
            t = min(t, int(d1[c]/d2[c]))
        return t
