class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        import math
        i = 0
        squares = set()
        limit = int(math.sqrt(c))
        for i in range(limit+1):
            squares.add(i*i)
        for i in range(limit+1):
            if c-i*i in squares:
                return True
        return False
