class Solution:
    # @param s, a string
    # @return an integer
    def longestValidParentheses(self, s):
        stack = []
        t = ['#' for i in range(len(s))]
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            elif stack:
                t[stack.pop()] = '*'
                t[i] = '*'
        max_length, length = 0, 0
        for i in range(len(t)):
            if t[i] == '*':
                length += 1
            else:
                max_length, length = max(max_length, length), 0
        return max(max_length, length)
