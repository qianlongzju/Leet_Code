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
    int numTrees(int n) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        // C(2n, n) / (n+1)
        // catalan
        double result = 1;
        for (int i=1; i <= n; i++) {
            result *= (2*n-i+1)*1.0/i;
        }
        result /= n+1;
        return result;
    }
    int numTrees2(int n) {
        int num[n+1];
        num[0] = 1;
        for (int i=1; i <=n; i++) {
            num[i] = 0;
            for (int j=1; j <= i; j++) {
                num[i] += num[j-1]*num[i-j];
            }
        }
        return num[n];
    }
};
int main() {
    Solution s;
    cout << s.numTrees(3) << endl;

    return 0;
}

