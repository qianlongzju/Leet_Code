class Solution:
    # @param s, a string
    # @return a boolean
    def isNumber(self, s):
        i = 0
        n = len(s)
        while i < n and s[i].isspace():
            i += 1
        if i < n and (s[i] == '+' or s[i] == '-'):
            i += 1
        isNumeric = False
        while i < n and s[i].isdigit():
            i += 1
            isNumeric = True
        if i < n and s[i] == '.':
            i += 1
            while i < n and s[i].isdigit():
                i += 1
                isNumeric = True
        if isNumeric and i < n and s[i] == 'e':
            i += 1
            isNumeric = False
            if i < n and (s[i] == '+' or s[i] == '-'):
                i += 1
            while i < n and s[i].isdigit():
                i += 1
                isNumeric = True
        while i < n and s[i].isspace():
            i += 1
        return isNumeric and i == n
