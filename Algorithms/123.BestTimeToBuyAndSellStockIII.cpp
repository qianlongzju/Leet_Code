class Solution {
public:
    int maxProfit(vector<int> &prices) {
        int n = prices.size();
        if (n <= 1) {
            return 0;
        }
        int leftToRight[n];
        int rightToLeft[n];
        for (int i=0; i < n; i++) {
            leftToRight[i] = 0;
            rightToLeft[i] = 0;
        }
        int max = 0; 
        int minimum = prices[0];
        for (int i=1; i < n; i++) {
            if (prices[i] < minimum) {
                minimum = prices[i];
            } else if (prices[i] - minimum > max) {
                max = prices[i] - minimum;
            }
            leftToRight[i] = max;
        }
        max = 0;
        int maximum = prices[n-1];
        for (int i=n-2; i >= 0; i--) {
            if (prices[i] > maximum) {
                maximum = prices[i];
            } else if (maximum - prices[i] > max) {
                max = maximum - prices[i];
            }
            rightToLeft[i] = max;
        }
        max = 0;
        for (int i=0; i < n-1; i++) {
            int temp = leftToRight[i] + rightToLeft[i+1];
            if (max < temp) {
                max = temp;
            }
        }
        if (rightToLeft[0] > max) {
            max = rightToLeft[0];
        }
        if (leftToRight[n-1] > max) {
            max = leftToRight[n-1];
        }
        return max;
    }
};
