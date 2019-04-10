class Solution:
    # @return a string
    def getPermutation(self, n, k):
        def _factorial(n):
            result = 1
            for i in range(2, n+1):
                result *= i
            return result

        def _kth_permutation(s, k, permutation):
            if len(s) == 1:
                permutation.append(str(s[0]))
                return
            p = _factorial(len(s)-1)
            a = s[(k-1)/p]
            permutation.append(str(a))
            k -= ((k-1)/p)*p
            s.remove(a)
            _kth_permutation(s, k, permutation)
        permutation = []
        s = range(1, n+1)
        _kth_permutation(s, k, permutation)
        return "".join(permutation)
