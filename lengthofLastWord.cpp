#include "leetcode.h"
class Solution {
public:
    int lengthOfLastWord(const char *s) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        int n = strlen(s);
        if (n == 0) {
            return 0;
        }
        bool wordBegin = false;
        int count = 0;
        for (int i=n-1; i >= 0; i--) {
            if (s[i] != ' ') {
                if (wordBegin) {
                    count++;
                }
                else {
                    wordBegin = true;
                    count++;
                }
            }
            else {
                if (wordBegin) {
                    return count;
                }
            }
        }
        return count;
    }
};
