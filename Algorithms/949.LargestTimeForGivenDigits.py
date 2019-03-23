class Solution(object):
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        def valid(a, b, c, d):
            h = 10*a + b
            m = 10*c + d
            if h >= 24 or m >= 60:
                return False
            return True
        import itertools
        result = []
        for p in itertools.permutations(A):
            if valid(*p):
                result.append(p)
        if result == []:
            return ""
        p = max(result)
        return "%02d:%02d" % (10*p[0]+p[1], 10*p[2]+p[3])
