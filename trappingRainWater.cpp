#include "leetcode.h"
// http://blog.unieagle.net/2012/10/31/leetcode%E9%A2%98%E7%9B%AE%EF%BC%9Atrapping-rain-water/
class Solution {
public:
    int trap(int A[], int n) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        int total = 0;
        int leftToRight[n];
        int highest = 0;
        for (int i = 0; i < n; ++i) {
            leftToRight[i] = highest;
            if (A[i] > highest) {
                highest = A[i];
            }
        }
        highest = 0;
        for (int i = n-1; i >= 0; i --) {
            if (A[i] > highest) {
                highest = A[i];
            } else if (A[i] < leftToRight[i]) {
                total += highest > leftToRight[i] ? leftToRight[i]: highest;
                total -= A[i];
            }
        }
        return total;
    }
};
int main() {
    Solution s;
    int a[] = {0,1,0,2,1,0,1,3,2,1,2,1};
    cout << s.trap(a, 12) << endl;
    int b[] = {4, 2, 0, 3, 2, 5};
    cout << s.trap(b, 6) << endl;
    return 0;
}

