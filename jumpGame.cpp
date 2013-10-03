#include <iostream>
#include <string>
#include <stack>
#include <vector>
#include <set>
#include <algorithm>
#include <limits.h>
using namespace std;
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};
class Solution {
public:
    bool canJump(int A[], int n) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        int maxIndex = 0;
        for (int i=0; i < n && i <= maxIndex; i++) {
            if (i+A[i] < maxIndex) {
                continue;
            }
            maxIndex = i + A[i];
            if (maxIndex >= n-1) {
                return true;
            }
        }
        return false;
    }
};
int main() {
    int n = 25003;
    int A[25003];
    for (int i=0; i < 25000; i++) {
        A[i] = 25000-i;
    }
    A[25000] = 1;
    A[25001] = 0;
    A[25002] = 0;
    Solution s;
   // cout << s.canJump(A, n) << endl;
    A[0] = 0;
    A[1] = 1;
    cout << s.canJump(A, 2) << endl;
    return 0;
}

