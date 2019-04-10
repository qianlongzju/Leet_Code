class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        flag = None
        while n > 0:
            if n & 0x01 == 1:
                if flag == True:
                    return False
                flag = True
            else:
                if flag == False:
                    return False
                flag = False
            n >>= 1
        return True
