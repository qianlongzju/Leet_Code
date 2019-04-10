class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        return num - 9*((num-1)//9)
    
    def addDigits1(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num > 9:
            x = 0
            while num:
                x += num % 10
                num /= 10
            num = x
        return num
