class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"
        flag = 1
        if num < 0:
            flag = -1
            num = -num
        result = []
        while num > 0:
            result.append(str(num % 7))
            num /= 7
        r = "".join(result[::-1])
        if flag == -1:
            r = "-" + r
        return r
