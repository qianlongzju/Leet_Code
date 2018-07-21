class Solution:
    # @return an integer
    def atoi(self, str):
        length = len(str)
        i = 0
        positive = True
        result = 0
        while i < length and str[i].isspace():
            i += 1
        if i < length and str[i] == '+':
            i += 1
        elif i < length and str[i] == '-':
            positive = False
            i += 1
        while i < length:
            if str[i].isdigit():
                if result > 214748364 or (result == 214748364 and (ord(str[i]) - ord('0')) >= 8):
                    return 2147483647 if positive else -2147483648
                result = 10*result + (ord(str[i]) - ord('0'))
            else:
                break
            i += 1
        if positive:
            return result
        else:
            return -result
