class Solution(object):
    def largestInteger(self, num):
        """
        :type num: int
        :rtype: int
        """
        num_str = str(num)
        digits = [(i, num_str[i]) for i in range(len(num_str))]
        odd = [digit for digit in digits if int(digit[1]) % 2 == 1]
        even = [digit for digit in digits if int(digit[1]) % 2 == 0]
        odd_index = [digit[0] for digit in odd]
        odd_val = [int(digit[1]) for digit in odd]
        even_index = [digit[0] for digit in even]
        even_val = [int(digit[1]) for digit in even]
        result = [0] * len(num_str)
        odd_val = sorted(odd_val, reverse=True)
        even_val = sorted(even_val, reverse=True)
        for i in range(len(odd_index)):
            result[odd_index[i]] = odd_val[i]
        for i in range(len(even_index)):
            result[even_index[i]] = even_val[i]
        return int("".join([str(i) for i in result]))
