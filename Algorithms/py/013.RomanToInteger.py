class Solution:
    # @return an integer
    def romanToInt(self, s):
        mapping = {'I': 1, 'V':5, 'X':10,
            'L':50, 'C':100, 'D':500, 'M':1000}
        prev, total = 0, 0
        for c in s:
            curr = mapping[c]
            total += curr - 2 * prev if curr > prev else curr
            prev = curr
        return total
