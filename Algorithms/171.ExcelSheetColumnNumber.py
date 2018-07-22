class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        num = 0
        for c in s:
            num = 26*num + table.index(c) + 1
        return num
