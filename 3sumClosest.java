import java.util.*;
public class Solution {
    public int threeSumClosest(int[] num, int target) {
        // Start typing your Java solution below
        // DO NOT write main() function
        Arrays.sort(num);
        int n = num.length;
        int lowestGap = Integer.MAX_VALUE;
        int closestSum = 0;
        for (int i = 0;i < n; i++) {
            int j = i + 1;
            int k = n - 1;
            while (j < k) {
                int sum_three = num[i] + num[j] + num[k];
                int gap = target - sum_three;
                if (gap < 0) {
                    gap = -gap;
                }
                if (gap < lowestGap) {
                    lowestGap = gap;
                    closestSum = sum_three;
                }
                if (sum_three < target) {
                    j++;
                } else if (sum_three > target) {
                    k--;
                } else {
                    j++;
                    k--;
                }
            }
        }
        return closestSum;
    }
}
