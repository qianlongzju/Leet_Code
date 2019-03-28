class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count, count_0, count_1 = 0, 0, 0
        for i in range(len(s)):
            if s[i] == '0':
                if i > 0 and s[i-1] == '1':
                    count_0 = 0
                count_0 += 1
                if count_0 <= count_1:
                    count += 1
            elif s[i] == '1':
                if i > 0 and s[i-1] == '0':
                    count_1 = 0
                count_1 += 1
                if count_0 >= count_1:
                    count += 1
        return count
