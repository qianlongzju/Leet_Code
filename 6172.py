class Solution(object):
    def isStrictlyPalindromic(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def palind(n, i):
            res = []
            while n:
                res.append(n % i)
                n /= i
            for i in range(len(res)):
                if res[i] != res[len(res)-1-i]:
                    return False
            return True
        for i in range(2, n-1):
            if not palind(n, i):
                return False
        return True
