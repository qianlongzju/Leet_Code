#include "leetcode.h"
class Solution {
public:
    int removeDuplicates(int A[], int n) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        if (n == 0 || n == 1) {
            return n;
        }
        int j = 0;
        for (int i=1; i < n; i++) {
            if (A[i] != A[i-1]) {
                A[++j] = A[i];
            }
        }
        return j+1;
    }
};
