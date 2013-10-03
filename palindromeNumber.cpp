#include <stdio.h>
class Solution {
public:
    bool isPalindrome(int x) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        if (x < 0) {
            return false;
        }
        long long i = 1;
        while (i*10 <= x) {
            i *= 10;
        }
        while (x >= 10) {
            if (x/i == x%10) {
                x = x % i;
                x /= 10;
                i /= 100;
            }
            else {
                return false;
            }
        }
        return true;
    }
};

int main() {
    Solution *s = new Solution();
    bool flag = s->isPalindrome(1874994781);
    if (flag) {
        printf("YES");
    }
    return 0;
}

