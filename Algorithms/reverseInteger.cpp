#include "leetcode.h"
class Solution {
public:
    int reverse(int x) {
        int y = 0;
        while (x) {
            if (abs(y) > 214748364 || (abs(y) == 214748364 && (x % 10) >= 8)) {
                return 0;
            }
            y = (10 * y) + (x % 10);
            x /= 10;
        }
        return y;
    }
};

int main() {
    Solution s;
    cout << s.reverse(1056389759) << endl;
    cout << s.reverse(-2147483648) << endl;
    return 0;
}
