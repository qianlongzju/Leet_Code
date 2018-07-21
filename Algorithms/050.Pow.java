public class Solution {
    public double myPow(double x, int n) {
        double result = 1.0;
        if (n == 0)
            return 1.0;
        boolean positive = true;
        long nn = n;
        if (n < 0) {
            positive = false;
            nn = -nn;
        }
        while (nn != 0) {
            if (nn%2 == 1) {
                result *= x;
            }
            x *= x;
            nn /= 2;
        }
        if (positive) {
            return result;
        }
        else {
            return 1/result;
        }
    }
}
