class Solution(object):
    def baseNeg2(self, N):
        """
        :type N: int
        :rtype: str
        """
        if N == 0:
            return "0"
        result = []
        while N != 0:
            a, b = N % (-2), N / (-2)
            #print '1', a, b
            if a < 0:
                a += 2
                b += 1
            #print '2', a, b
            N = b
            result.append(str(a))
            #N = N/ (-2)
        return "".join(result[::-1])
