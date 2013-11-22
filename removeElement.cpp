#include "leetcode.h"
class Solution {
public:
    int removeElement(int A[], int n, int elem) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        for (int i=0; i < n; i++) {
            while (A[i] == elem) {
                n --;
                if (i >= n)
                    return n;
                A[i] = A[n];
            }
        }
        return n;
    }
};
