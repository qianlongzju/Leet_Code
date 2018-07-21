class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        digits = ["1"]
        number = []
        for i in range(n-1):
            count = 1
            for i in range(1, len(digits)):
                if digits[i] == digits[i-1]:
                    count += 1
                else:
                    number.append(str(count))
                    number.append(digits[i-1])
                    count = 1
            number.append(str(count))
            number.append(digits[-1])
            digits, number = number, []
        return "".join(digits)
