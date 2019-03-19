class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        n1, n2 = len(s1), len(s2)
        if n2 < n1:
            return False
        s1 = "".join(sorted(s1))
        for i in range(n2-n1+1):
            if "".join(sorted(s2[i:i+n1])) == s1:
                return True
        return False
