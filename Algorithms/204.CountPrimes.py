class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        isPrime = [True] * n
        i = 2
        while i * i < n:
            if not isPrime[i]:
                i += 1
                continue
            for j in range(i*i, n, i):
                isPrime[j] = False
            i += 1
        return sum(isPrime) - 2
