#include "leetcode.h"
class Solution {
public:
    bool search(int A[], int n, int target) {
        // left typing your C/C++ solution below
        // DO NOT write int main() function
        int left = 0; 
        int right = n - 1;
        while (left <= right) {
            int middle = left + (right - left) / 2;
            // cout << middle << endl;
            if (target == A[middle]) {
                return true;
            } else if (target == A[left]) {
                return true;
            } else if (target == A[right]) {
                return true;
            } else if (A[middle] > A[left]) {
                if (target > A[middle]) {
                    left = middle + 1;
                } else {
                    if (target > A[left]) {
                        right = middle - 1;
                    } else {
                        left = middle + 1;
                    }
                }
            } else if (A[middle] < A[left]) {
                if (target < A[middle]) {
                    right = middle - 1;
                } else {
                    if (target > A[right]) {
                        right = middle - 1;
                    } else {
                        left = middle + 1;
                    }
                }
            }
            else {
                left ++;
            }
        }
        return false;
    }
};
int main() {
    Solution s;
    int A[] = {1, 1, 3, 1};
    cout << s.search(A, 4, 3) << endl;
    cout << "A" << endl;
    int B[] = {1, 3, 1, 1, 1};
    cout << s.search(B, 5, 3) << endl;
    return 0;
}

