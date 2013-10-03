//public class Solution {
public class divideToIntegers {
    public int divide(int dividend, int divisor) {
        // Start typing your Java solution below
        // DO NOT write main() function
        boolean positive = true;
        long un_dividend = dividend;
        long un_divisor = divisor;
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
                return (int)un_dividend;
            }
            else {
                return (int)-un_dividend;
            }
        }
        int result = 0;
        while (un_divisor <= un_dividend) {
            long temp = un_divisor;
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
}
