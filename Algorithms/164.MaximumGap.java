public class Solution {
    public int maximumGap(int[] nums) {
        int n = nums.length;
        if (n < 2)
            return 0;
        int A = nums[0];
        int B = nums[0];
        for (int i=0; i < n; i++) {
            if (nums[i] > A) 
                A = nums[i];
            if (nums[i] < B) 
                B = nums[i];
        }
        int bucketRange = (int)(((A - B)*1.0 / (n - 1)) + 0.5);
        if (bucketRange < 1)
            bucketRange = 1;
        int bucketLen = (int)(((A - B)*1.0 / bucketRange) + 0.5) + 1;
        int[] buckets = new int[2*bucketLen];
        for (int i = 0; i < 2*bucketLen; i++)
            buckets[i] = -1;
        for (int i = 0; i < n; i++) {
            int loc = (int)(((nums[i] - B)*1.0 / bucketRange) + 0.5);
            if (buckets[loc*2] == -1) {
                buckets[loc*2] = nums[i];
                buckets[loc*2+1] = nums[i];
                continue;
            }
            if (buckets[loc*2] > nums[i])
                buckets[loc*2] = nums[i];
            if (buckets[loc*2+1] < nums[i])
                buckets[loc*2+1] = nums[i];
        }
        int maxGap = 0;
        int i = 0; 
        while (i < bucketLen) {
            if (buckets[2*i] == -1) {
                i ++;
                continue;
            }
            int j = i + 1;
            while (j < bucketLen) {
                if (buckets[2*j] == -1) {
                    j ++;
                    continue;
                }
                if ((buckets[2*j] - buckets[i*2+1]) > maxGap)
                    maxGap = buckets[2*j] - buckets[2*i+1];
                break;
            }
            i = j;
        }
        return maxGap;
    }
}
