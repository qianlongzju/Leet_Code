class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        ugly = [1]
        p2, p3, p5 = 0, 0, 0
        for i in range(1, n):
            a, b, c = ugly[p2]*2, ugly[p3]*3, ugly[p5]*5
            u = min(a, b, c)
            ugly.append(u)
            if u == a:
                p2 += 1
            if u == b:
                p3 += 1
            if u == c:
                p5 += 1
        return ugly[-1]
