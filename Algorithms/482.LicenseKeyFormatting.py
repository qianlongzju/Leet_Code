class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        s = [c.upper() for c in S if c != '-']
        j = len(s) - 1
        result = []
        while j >= K-1:
            result.append("".join(s[j-K+1:j+1]))
            j -= K
        if j >= 0:
            result.append("".join(s[:j+1]))
        return "-".join(result[::-1])
