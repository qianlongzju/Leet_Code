class Solution {
public:
    int trap(int A[], int n) {
        int leftToRight[n];
        int rightToLeft[n];
        leftToRight[0] = 0;
        rightToLeft[n-1] = 0;
        for (int i = 1; i < n; ++i) {
            leftToRight[i] = max(leftToRight[i-1], A[i-1]);
            rightToLeft[n-i-1] = max(rightToLeft[n-i], A[n-i]);
        }
        int total = 0;
        for (int i=1; i < n-1; i++) {
            int height = min(leftToRight[i], rightToLeft[i]);
            if (height > A[i]) 
                total += height - A[i];
        }
        return total;
    }
};
