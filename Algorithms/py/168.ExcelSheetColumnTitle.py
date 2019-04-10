class Solution:
    # @return a string
    def convertToTitle(self, nums):
        s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        length = len(s)
        result = ""
        while nums > 0:
                nums -= 1
                result = s[nums%length] + result
                nums /= length
        return result
