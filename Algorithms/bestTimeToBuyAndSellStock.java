public class Solution {
    public int maxProfit(int[] prices) {
        if (prices.length <= 1) {
            return 0;
        }
        int minimum = prices[0];
        int maximum = 0;
        for (int i=1; i < prices.length; i++) {
            minimum = Math.min(prices[i], minimum);
            maximum = Math.max(prices[i] - minimum, maximum);
        }
        return maximum;
    }
}
