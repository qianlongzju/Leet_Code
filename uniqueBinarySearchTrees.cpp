#include "leetcode.h"
class Solution {
public:
    int numTrees(int n) {
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

