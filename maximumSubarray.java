public class Solution {
    public int maxSubArray(int[] A) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        return maxSubsequenceSum(A, 0, A.length-1);
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
        maxLeftSum = maxSubsequenceSum(A, left, center);
        maxRightSum = maxSubsequenceSum(A, center+1, right);
        
        maxLeftBorderSum = leftBorderSum = A[center];
        for (i = center-1; i >= left; i--) {
            leftBorderSum += A[i];
            if (leftBorderSum > maxLeftBorderSum) {
                maxLeftBorderSum = leftBorderSum;
            }
        }

        maxRightBorderSum = rightBorderSum = A[center+1];
        for (i = center+2; i <= right; i++) {
            rightBorderSum += A[i];
            if (rightBorderSum > maxRightBorderSum) {
                maxRightBorderSum = rightBorderSum;
            }
        }

        int sum = maxLeftBorderSum + maxRightBorderSum;
        if (maxLeftSum > sum) {
            sum = maxLeftSum;
        }
        if (maxRightSum > sum) {
            sum = maxRightSum;
        }
        return sum;
    }
    public int maxSubArray2(int[] A) {
        // Start typing your Java solution below
        // DO NOT write main() function
        int thisSum, maxSum;
        thisSum = maxSum = A[0];
        for (int i=1; i < A.length; i++) {
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
}
