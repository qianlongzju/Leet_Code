class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        count = 0
        while num & 0x01 == 0:
            num >>= 1
            count += 1
        if count & 0x01 == 1:
            return False
        i = 3
        while i*i < num:
            if num % i == 0:
                count = 0
                while num % i == 0:
                    count += 1
                    num /= i
                if count & 0x01 == 1:
                    return False
            i += 2
        if i * i == num or num == 1:
            return True
        return False
