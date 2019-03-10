class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        count = 0
        i, j = len(g)-1, len(s)-1
        while i >= 0 and j >= 0:
            if s[j] >= g[i]:
                count += 1
                j -= 1
                i -= 1
            else:
                i -= 1
        return count
