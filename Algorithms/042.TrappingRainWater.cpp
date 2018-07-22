class Solution {
public:
    int trap(vector<int>& height) {
        int n = height.size();
        if (n == 0)
            return 0;
        int leftToRight[n];
        int rightToLeft[n];
        leftToRight[0] = 0;
        rightToLeft[n-1] = 0;
        for (int i = 1; i < n; ++i) {
            leftToRight[i] = max(leftToRight[i-1], height[i-1]);
            rightToLeft[n-i-1] = max(rightToLeft[n-i], height[n-i]);
        }
        int total = 0;
        for (int i=1; i < n-1; i++) {
            int h = min(leftToRight[i], rightToLeft[i]);
            if (h > height[i])
                total += h - height[i];
        }
        return total;
    }
};
