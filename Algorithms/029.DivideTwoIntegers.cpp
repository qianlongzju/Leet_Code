class Solution {
public:
    int divide(int dividend, int divisor) {
        bool positive = true;
        long long un_dividend = dividend;
        long long un_divisor = divisor;
        if (un_dividend < 0) {
            positive = !positive;
            un_dividend = -un_dividend;
        }
        if (un_divisor < 0) {
            positive = !positive;
            un_divisor = -un_divisor;
        }
        if (un_divisor == 1) {
            if (positive) {
                if (un_dividend == 2147483648L)
                    return 2147483647;
                return un_dividend;
            }
            else {
                return -un_dividend;
            }
        }
        int result = 0;
        while (un_divisor <= un_dividend) {
            long long temp = un_divisor;
            int shift = 0;
            while ((temp << 1) <= un_dividend) {
                temp <<= 1;
                shift ++;
            }
            un_dividend -= temp;
            result += 1 << shift;
        }
        if (positive) {
            return result;
        }
        else {
            return -result;
        }
    }
};
