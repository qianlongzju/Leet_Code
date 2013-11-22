#include "leetcode.h"
class Solution {
public:
    int sqrt(int x) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        if (x == 0) {
            return 0;
        }
        double last = 0;
        double res = 1;
        while (last != res) {
            last = res;
            res = (x/last + last) / 2;
        }
        return int(res);
    }
};
