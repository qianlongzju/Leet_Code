class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        d = []
        for i in range(len(A)):
            if A[i] != B[i]:
                d.append(i)
                if len(d) > 2:
                    return False
        if len(d) == 1:
            return False
        if len(d) == 2:
            return A[d[0]] == B[d[1]] and A[d[1]] == B[d[0]]
        c = collections.Counter(A)
        for k, v in c.items():
            if v > 1:
                return True
        return False
