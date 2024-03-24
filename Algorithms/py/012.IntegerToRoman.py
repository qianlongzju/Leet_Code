class Solution:
    def intToRoman(self, num: int) -> str:
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        i = 0
        s = ""
        while num:
            k = int(num / values[i])
            for j in range(k):
                s += symbols[i]
                num -= values[i]
            i += 1
        return s