class Solution:
    # @param {integer} x
    # @return {integer}
    def mySqrt(self, x):
        i, j = 0, x
        while i <= j:
            mid = (i + j) // 2
            if mid * mid <= x and (mid+1) * (mid+1) > x:
                return mid
            elif mid * mid > x:
                j = mid - 1
            else:
                i = mid + 1

    def mySqrt_1(self, x):
        if not x: return x
        last = 0
        result = x
        while result != last:
            last = result
            result = (x/result + result) / 2.0
        return int(result)
