# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution(object):
    def rand10(self):
        """
        :rtype: int
        """
        a = rand7()
        b = rand7()
        while (a - 1) * 7 + b > 40:
            a = rand7()
            b = rand7()
            #a, b = rand7(), rand7()
        return (7 * (a - 1) + b - 1) % 10 + 1
