import java.util.*;
public class Solution {
    public int jump(int[] A) {
        int n = A.length;
        int maxIndex = 0;
        int[] steps = new int[n];
        for (int i=0; i < n; i++) {
            steps[i] = Integer.MAX_VALUE;
        }
        steps[0] = 0;
        for (int i=0; i < n && i <= maxIndex; i++) {
            for (int j=maxIndex+1; j <= i+A[i] && j < n; j++) {
                if (steps[i]+1 < steps[j]) {
                    steps[j] = steps[i] + 1;
                }
            }
            if (i+A[i] < maxIndex) {
                continue;
            }
            maxIndex = i + A[i];
            if (maxIndex >= n-1) {
                break;
            }
        }
        return steps[n-1];
    }
}
