class Solution:
    # @return a string
    def convertToTitle(self, num):
        s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        length = len(s)
        result = ""
        while num > 0:
                num -= 1
                result = s[num%length] + result
                num /= length
        return result
