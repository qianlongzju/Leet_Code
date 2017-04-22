import java.util.*;
public class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> mapping = new HashMap<>();
        for (int i=0; i < nums.length; i++) {
            mapping.put(nums[i], i);
        }
        for (int i = 0; i < nums.length; i++) {
            int gap = target - nums[i];
            if (mapping.containsKey(gap) &&
                    mapping.get(gap) != i) {
                return new int[]{i, mapping.get(gap)};
            }
        }
        return null;
    }
}
