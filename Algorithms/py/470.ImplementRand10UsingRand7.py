# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution(object):
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            a = rand7()
            b = rand7()
            t = (a - 1) * 7 + b
            if t <= 40: return t % 10 + 1
            t = (t - 40 - 1) * 7 + rand7()
            if t <= 60: return t % 10 + 1
            t = (t - 60 - 1) * 7 + rand7()
            if t <= 20: return t % 10 + 1
