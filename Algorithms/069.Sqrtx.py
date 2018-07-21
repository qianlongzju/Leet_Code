class Solution:
    # @param {integer} x
    # @return {integer}
    def mySqrt(self, x):
        if not x: return x
        last = 0
        result = x
        while result != last:
            last = result
            result = (x/result + result) / 2.0
        return int(result)
