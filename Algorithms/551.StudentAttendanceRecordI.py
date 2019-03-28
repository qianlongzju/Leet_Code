class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        flag = False
        count_A, count_L = 0, 0
        for c in s:
            if c == 'A':
                count_A += 1
                if count_A > 1:
                    return False
                count_L = 0
            elif c == 'L':
                count_L += 1
                if count_L > 2:
                    return False
            else:
                count_L = 0
        return True
