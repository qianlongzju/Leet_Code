#include "leetcode.h"
class Solution {
public:
    int jump(int A[], int n) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        int maxIndex = 0;
        int steps[n];
        for (int i=0; i < n; i++) {
            steps[i] = INT_MAX;
        }
        steps[0] = 0;
        for (int i=0; i < n && i <= maxIndex; i++) {
            for (int j=maxIndex+1; j <= i+A[i] && j < n; j++) {
                if (steps[i]+1 < steps[j]) {
                    steps[j] = steps[i] + 1;
                }
            }
            if (i+A[i] < maxIndex) {
                continue;
            }
            maxIndex = i + A[i];
            if (maxIndex >= n-1) {
                break;
            }
        }
        return steps[n-1];
    }
};
int main() {
    int n = 25000-23697+2;
    int A[n];
    for (int i=0; i < 25000; i++) {
        if (25000-i >= 23697)
            A[i] = 25000-i;
    }
    A[n-1] = 23;
    Solution s;
    cout << s.jump(A, n) << endl;
    A[0] = 1;
    A[1] = 2;
    A[2] = 3;
    cout << s.jump(A, 3) << endl;
    return 0;
}

