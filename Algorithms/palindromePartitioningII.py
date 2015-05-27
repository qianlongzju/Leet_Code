class Solution:
    # @param {string} s
    # @return {integer}
    def minCut(self, s):
        n = len(s)
        cuts = [n-i-1 for i in range(n+1)]
        isPalindrome = [[False for i in range(n)] for j in range(n)]
        for i in range(n)[::-1]:
            for j in range(i, n):
                if s[i] == s[j] and (j - i < 2 or isPalindrome[i + 1][j - 1]):
                    isPalindrome[i][j] = True
                    cuts[i] = min(cuts[j+1] + 1, cuts[i])
        return cuts[0]
