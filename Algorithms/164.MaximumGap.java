public class Solution {
    public int maximumGap(int[] num) {
        int n = num.length;
        if (n < 2)
            return 0;
        int A = num[0];
        int B = num[0];
        for (int i=0; i < n; i++) {
            if (num[i] > A) 
                A = num[i];
            if (num[i] < B) 
                B = num[i];
        }
        int bucketRange = (int)(((A - B)*1.0 / (n - 1)) + 0.5);
        if (bucketRange < 1)
            bucketRange = 1;
        int bucketLen = (int)(((A - B)*1.0 / bucketRange) + 0.5) + 1;
        int[] buckets = new int[2*bucketLen];
        for (int i = 0; i < 2*bucketLen; i++)
            buckets[i] = -1;
        for (int i = 0; i < n; i++) {
        	int loc = (int)(((num[i] - B)*1.0 / bucketRange) + 0.5);
        	if (buckets[loc*2] == -1) {
        		buckets[loc*2] = num[i];
        		buckets[loc*2+1] = num[i];
        		continue;
        	}
        	if (buckets[loc*2] > num[i])
        		buckets[loc*2] = num[i];
        	if (buckets[loc*2+1] < num[i])
        		buckets[loc*2+1] = num[i];
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
