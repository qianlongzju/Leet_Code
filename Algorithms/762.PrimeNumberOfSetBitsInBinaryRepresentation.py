class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
        def _get_1_bits(x):
            count = 0
            while x != 0:
                x = x & (x-1)
                count += 1
            return count
        count = 0
        for x in range(L, R+1):
            if _get_1_bits(x) in primes:
                count += 1
        return count
