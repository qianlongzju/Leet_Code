class Solution:
    # @param {integer} n
    # @return {string[]}
    def generateParenthesis(self, n):
        result = []
        def _helper(left, right, s, n):
            if left == n and right == n:
                result.append(s)
                return
            if left < n:
                _helper(left + 1, right, s + "(", n)
            if right < left:
                _helper(left, right + 1, s + ")", n)
        _helper(0, 0, "", n)
        return result

