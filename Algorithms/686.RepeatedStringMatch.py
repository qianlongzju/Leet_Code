class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        n = len(B) // len(A)
        if (A * (n)).find(B) != -1:
            return n
        if (A * (n+1)).find(B) != -1:
            return n+1
        if (A * (n+2)).find(B) != -1:
            return n+2
        return -1
