class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 10
        if n > 10:
            return 0
        temp = 9
        result = 10
        for i in range(n-1):
            temp *= 9-i
            result += temp
        return result
