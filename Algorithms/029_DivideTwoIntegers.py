class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        positive = True
        un_dividend = dividend
        un_divisor = divisor
        if un_dividend < 0:
            positive = not positive
            un_dividend = -un_dividend
        if un_divisor < 0:
            positive = not positive
            un_divisor = -un_divisor
        if un_divisor == 1:
            if positive:
                if un_dividend == 2147483648:
                    return 2147483647
                return un_dividend
            else:
                return -un_dividend
        result = 0
        while un_divisor <= un_dividend:
            temp = un_divisor
            shift = 0
            while (temp << 1) <= un_dividend:
                temp <<= 1
                shift += 1
            un_dividend -= temp
            result += 1 << shift
        if positive:
            return result
        else:
            return -result
