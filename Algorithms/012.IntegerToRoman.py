class Solution:
    symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"];
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1];
    # @return a string
    def intToRoman(self, nums):
        i = 0
        s = ""
        while nums:
            k = nums / self.values[i]
            for j in range(k):
                s += self.symbols[i]
                nums -= self.values[i]
            i += 1
        return s
