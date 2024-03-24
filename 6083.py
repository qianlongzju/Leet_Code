class Solution(object):
    def digitCount(self, num):
        """
        :type num: str
        :rtype: bool
        """
        for i in range(len(num)):
            if num.count(str(i)) != int(num[i]):
                return False
        return True
