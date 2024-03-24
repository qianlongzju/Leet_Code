
class Solution(object):
    def numberOfWays(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 0 1 0 | 1 0 1
        n = len(s)
        res = 0
        zeros_left, zeros_right = [0]*n, [0]*n
        ones_left, ones_right = [0]*n, [0]*n
        for i in range(n-1):
            zeros_left[i+1] = zeros_left[i]
            ones_left[i+1] = ones_left[i]
            if s[i] == '0':
                 zeros_left[i+1] += 1
            else:
                ones_left[i+1] += 1
        for i in range(n-1, 1, -1):
            zeros_right[i-1] = zeros_right[i]
            ones_right[i-1] = ones_right[i]
            if s[i] == '0':
                 zeros_right[i-1] += 1
            else:
                ones_right[i-1] += 1
        for i in range(1, n-1):
            if s[i] == '0':
                res += ones_left[i] * ones_right[i]
            else:
                res += zeros_left[i] * zeros_right[i]
        return res
