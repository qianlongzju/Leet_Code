public class Solution {
    public int majorityElement(int[] nums) {
        int previous = 0;
        int count = 0;
        for (int i = 0; i < nums.length; i++) {
            if (count == 0) {
                previous = nums[i];
                count ++;
            } else {
                if (previous == nums[i]) {
                    count ++;
                } else {
                    count --;
                }
            }
        }
        return previous;  
    }
}
