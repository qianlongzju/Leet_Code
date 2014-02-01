class Solution:
    # @return a string
    def getPermutation(self, n, k):
        permutation = []
        s = range(1, n+1)
        self.kth_permutation(s, k, permutation)
        return "".join(permutation)

    def factorial(self, n):
        result = 1
        for i in range(2, n+1):
            result *= i
        return result

    def kth_permutation(self, s, k, permutation):
        if len(s) == 1:
            permutation.append(str(s[0]))
            return
        p = self.factorial(len(s)-1)
        a = s[(k-1)/p]
        permutation.append(str(a))
        k -= ((k-1)/p)*p
        s.remove(a)
        self.kth_permutation(s, k, permutation)

if __name__ == '__main__':
    s = Solution()
    print s.getPermutation(3, 1)
    print s.getPermutation(3, 2)
    print s.getPermutation(3, 3)
    print s.getPermutation(3, 4)
    print s.getPermutation(3, 5)
    print s.getPermutation(3, 6)
