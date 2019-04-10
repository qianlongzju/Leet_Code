public class Solution {
    public int threeSumClosest(int[] nums, int target) {
        Arrays.sort(nums);
        int n = nums.length;
        int lowestGap = Integer.MAX_VALUE;
        int closestSum = 0;
        for (int i = 0; i < n; i++) {
            while (i > 0 && i < n && nums[i] == nums[i-1])
                i++;
            int j = i + 1;
            int k = n - 1;
            while (j < k) {
                int total = nums[i] + nums[j] + nums[k];
                int gap = Math.abs(target - total);
                if (gap < lowestGap) {
                    lowestGap = gap;
                    closestSum = total;
                }
                if (total < target) {
                    j++;
                    while (j < k && nums[j] == nums[j-1])
                        j++;
                } else if (total > target) {
                    k--;
                    while (k > j && nums[k] == nums[k+1])
                        k--;
                } else
                    return closestSum;
            }
        }
        return closestSum;
    }
}
