class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        p = 1
        for i in range(len(digits)-1, -1, -1):
            digits[i] += p
            p = digits[i] / 10
            digits[i] %= 10
            if p == 0:
                return digits
        if p != 0:
            digits = [1] + digits
        return digits
