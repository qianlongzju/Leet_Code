import java.util.*;
public class Solution {
    public int maxProfit(int[] prices) {
        // Start typing your Java solution below
        // DO NOT write main() function
        int max = 0;
        if (prices.length <= 1) {
            return 0;
        }
        int minimum = prices[0];
        for (int i=1; i < prices.length; i++) {
            if (prices[i] < minimum) {
                minimum = prices[i];
            } 
            if (prices[i] - minimum > max) {
                max = prices[i] - minimum;
            }
        }
        return max;
    }
}
