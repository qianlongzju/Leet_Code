#include "leetcode.h"
class Solution {
public:
    int maxSubArray(int A[], int n) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        return maxSubsequenceSum(A, 0, n-1);
    }
    int maxSubsequenceSum(int A[], int left, int right) {
        int maxLeftSum, maxRightSum;
        int maxLeftBorderSum, maxRightBorderSum;
        int leftBorderSum, rightBorderSum;
        int center, i;
        if (left == right) {
            return A[left];
        }

        center = (left + right) / 2;
        //cout << left << endl;
        //cout << right << endl;
        //cout << center << endl;
        maxLeftSum = maxSubsequenceSum(A, left, center);
        //cout << "maxLeftSum:" << maxLeftSum << endl;
        maxRightSum = maxSubsequenceSum(A, center+1, right);
        //cout << "maxRightSum:" << maxRightSum << endl;
        
        maxLeftBorderSum = leftBorderSum = A[center];
        for (i = center-1; i >= left; i--) {
            leftBorderSum += A[i];
            if (leftBorderSum > maxLeftBorderSum) {
                maxLeftBorderSum = leftBorderSum;
            }
        }
        //cout << maxLeftBorderSum << endl;

        maxRightBorderSum = rightBorderSum = A[center+1];
        for (i = center+2; i <= right; i++) {
            rightBorderSum += A[i];
            if (rightBorderSum > maxRightBorderSum) {
                maxRightBorderSum = rightBorderSum;
            }
        }
        //cout << maxRightBorderSum << endl;

        int sum = maxLeftBorderSum + maxRightBorderSum;
        if (maxLeftSum > sum) {
            sum = maxLeftSum;
        }
        if (maxRightSum > sum) {
            sum = maxRightSum;
        }
        return sum;
    }
    int maxSubArray2(int A[], int n) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        int thisSum, maxSum;
        thisSum = maxSum = A[0];
        for (int i=1; i < n; i++) {
            if (thisSum < 0) {
                thisSum = 0;
            }
            thisSum += A[i];
            if (thisSum > maxSum) {
                maxSum = thisSum;
            }
        }
        return maxSum;
    }
};

int main() {
    Solution s;
    int a[] = {1, 2};
    cout << s.maxSubArray(a, 2) << endl;
    return 0;
}
