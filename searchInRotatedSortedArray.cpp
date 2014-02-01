#include "leetcode.h"
class Solution {
public:
    int search(int A[], int n, int target) {
        int left = 0; 
        int right = n - 1;
        while (left <= right) {
            int middle = left + ((right - left) >> 1);
            if (target == A[middle]) {
                return middle;
            } else if (target == A[left]) {
                return left;
            } else if (target == A[right]) {
                return right;
            } else if (A[middle] > A[left]) {
                if (target < A[middle] && target > A[left])
                    right = middle - 1;
                else
                    left = middle + 1;
            } else {
                if (target > A[middle] && target < A[right])
                    left = middle + 1;
                else
                    right = middle - 1;
            }
        }
        return -1;
    }
};
int main() {
    Solution s;
    int A[] = {8, 9, 2, 3, 4};
    cout << s.search(A, 5, 9) << endl;
    return 0;
}
