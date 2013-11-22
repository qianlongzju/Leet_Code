#include "leetcode.h"
class Solution {
public:
    double pow(double x, int n) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        double result = 1.0;
        if (n == 0)
            return 1.0;
        bool positive = true;
        if (n < 0) {
            positive = false;
            n = -n;
        }
        while (n != 0) {
            if (n%2 == 1) {
                result *= x;
            }
            x *= x;
            n /= 2;
        }
        if (positive) {
            return result;
        }
        else {
            return 1/result;
        }
        
    }
};
