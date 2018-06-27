class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        d = dict()
        return self.numDecodingsIndex(s, 0, d)

    def numDecodingsIndex(self, s, index, d):
        if index in d:
            return d[index]
        n = len(s)
        if index == n:
            return 1
        elif index == n-1:
            if s[index] == '0':
                return 0
            else:
                return 1
        else:
            count = 0
            if s[index] != '0':
                count = self.numDecodingsIndex(s, index+1, d)
                if s[index] == '1' or (s[index] == '2' and ord(s[index+1])-ord('0') <= 6):
                    count += self.numDecodingsIndex(s, index+2, d)
            d[index] = count
            return count
