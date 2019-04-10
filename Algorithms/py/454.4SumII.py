class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        s = {}
        for a in A:
            for b in B:
                if a + b in s:
                    s[a+b] += 1
                else:
                    s[a+b] = 1
        count = 0
        for c in C:
            for d in D:
                if -(c+d) in s:
                    count += s[-(c+d)]
        return count
