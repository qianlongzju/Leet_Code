class Solution:
    # @param {integer} n
    # @return {string[]}
    def generateParenthesis(self, n):
        self.result = []
        self.helper(0, 0, "", n)
        return self.result

    def helper(self, left, right, s, n):
        if left == n and right == n:
            self.result.append(s)
            return
        if left < n:
            self.helper(left + 1, right, s + "(", n)
        if right < left:
            self.helper(left, right + 1, s + ")", n)
