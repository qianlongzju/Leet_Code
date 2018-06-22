#include "leetcode.h"
class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t x = 1 << 31;
        uint32_t result = 0;
        while(n != 0) {
            if (n % 2 == 1) {
                result += x;
            }
            n >>= 1;
            x >>= 1;
        }
        return result;
    }
};

int main() {
    Solution s;
    cout << s.reverseBits(0) << endl;
    return 0;
}
