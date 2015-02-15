#include "leetcode.h"
class Solution {
public:
    int atoi(string str) {
        int len = str.size();
        int i = 0;
        bool positive = true;
        long long result = 0;
        while (i < len && isspace(str[i])) 
            i ++;
        if (i < len && str[i] == '+') 
            i ++;
        else if (i < len && str[i] == '-') {
            positive = false;
            i ++;
        }
        while (i < len) {
            if (isdigit(str[i])) {
                if (result > 214748364 || (result == 214748364 && (str[i] - '0') >= 8)) {
                    return positive? 2147483647:-2147483648;
                }
                result = 10*result + (str[i] - '0');
            } else {
                break;
            }
            i ++;
        }
        if (positive)
            return result;
        else 
            return -result;
    }
};
int main() {
    Solution s;
    cout << s.atoi(" 1.3") << endl;
    cout << s.atoi("9223372036854775809") << endl;
    return 0;
}
