class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        min_a, min_b = m, n
        for a, b in ops:
            min_a = min(min_a, a)
            min_b = min(min_b, b)
            if min_a * min_b == 1:
                return 1
        return min_a*min_b
