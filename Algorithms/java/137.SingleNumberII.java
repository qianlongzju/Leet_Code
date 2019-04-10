public class Solution {
    public int singleNumber(int[] nums) {
        int result = 0;
        for (int j=0; j < 32; ++j) {
            int tmp = 0;
            int bitOps = 1 << j;
            for (int i=0; i < nums.length; ++i) {
                if ((nums[i] & bitOps) != 0) {
                    tmp ++;
                }
            }
            result += (tmp%3) << j;
        }
        return result;
    }
}
