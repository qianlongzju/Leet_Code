class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"
        if num < 0:
            num = 2 ** 32 + num
        result = ""
        d = [str(i) for i in range(10)] + [c for c in 'abcdef']
        while num > 0:
            num, result = num / 16, d[num%16] + result
        return result
