class Solution(object):
    def clumsy(self, N):
        """
        :type N: int
        :rtype: int
        """
        result = [N]
        opera = 0
        for i in range(N-1, 0, -1):
            if opera == 0:
                result[-1] *= i
            elif opera == 1:
                if result[-1] < 0:
                    result[-1] = -((-result[-1]) / i)
                else:
                    result[-1] /= i
            elif opera == 2:
                result.append(i)
            else:
                result.append(-i)
            opera = (opera + 1) % 4
        #print result
        return sum(result)
