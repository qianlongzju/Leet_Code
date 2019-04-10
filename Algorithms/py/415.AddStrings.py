class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if len(num1) > len(num2):
            num1, num2 = num2, num1
        c, i, j = 0, len(num1)-1, len(num2)-1
        result = ""
        while i >= 0 or j >= 0 or c:
            s = c
            if i >= 0:
                s += ord(num1[i]) - ord('0')
                i -= 1
            if j >= 0:
                s += ord(num2[j]) - ord('0')
                j -= 1
            s, c = s % 10, s / 10
            result = str(s) + result
        return result
