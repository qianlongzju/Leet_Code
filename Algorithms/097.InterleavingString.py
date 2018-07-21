class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        n, m = len(s1), len(s2)
        IL = [[False] * (m+1) for i in range(n+1)]
        if m+n != len(s3):
            return False
        for i in range(n+1):
            for j in range(m+1):
                if i == 0 and j == 0:
                    IL[i][j] = True
                elif i == 0:
                    if s2[j-1] == s3[j-1]:
                        IL[i][j] = IL[i][j-1]
                elif j == 0:
                    if s1[i-1] == s3[i-1]:
                        IL[i][j] = IL[i-1][j]
                elif s1[i-1] == s3[i+j-1] and s2[j-1] != s3[i+j-1]:
                    IL[i][j] = IL[i-1][j]
                elif s2[j-1] == s3[i+j-1] and s1[i-1] != s3[i+j-1]:
                    IL[i][j] = IL[i][j-1]
                elif s1[i-1] == s3[i+j-1] and s2[j-1] == s3[i+j-1]:
                    IL[i][j] = IL[i][j-1] or IL[i-1][j]
        return IL[n][m]
