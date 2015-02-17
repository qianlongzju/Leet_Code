class Solution:
    # @return an integer
    def reverse(self, x):
        flag = 1
        if x < 0:
            flag = -1
            x = -x
        ret = flag * int(str(x)[::-1])
        if ret > 2147483647 or ret < -2147483648:
            return 0
        return ret
