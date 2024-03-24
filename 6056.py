class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        res = ""
        for i in range(len(num)-2):
            #print(num, i, res)
            if num[i] == num[i+1] and num[i+1] == num[i+2]:
                if res == '' or num[i] > res[0]:
                    res = num[i:i+3]
            #print(res)
        return res
