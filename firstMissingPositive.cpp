#include "leetcode.h"
class Solution {
public:
    int firstMissingPositive(int A[], int n) {
        for (int i=0; i < n; i++) {
            while (A[i] <= n  && A[i] > 0 && A[i] != i+1) {
                int temp = A[A[i]-1];
                if (temp == A[i]) {
                    break;
                }
                A[A[i]-1] = A[i];
                A[i] = temp;
            }
        }        
        for (int i=0; i < n; i++) {
            if (A[i] != i+1) {
                return i+1;
            }
        }
        return n+1;
    }
};
int main() {
    Solution s;
    int a[] = {1, 2, 0};
    cout << s.firstMissingPositive(a, 3) << endl;
    int b[] = {3, 4, -1, 1};
    cout << s.firstMissingPositive(b, 4) << endl;
    int c[] = {1, 1};
    cout << s.firstMissingPositive(c, 2) << endl;
    return 0;
}

