import java.util.*;
public class Solution {
    public int trap(int[] A) {
        int n = A.length;
        if (n < 3)
            return 0;
        int[] leftToRight = new int[n];
        int[] rightToLeft = new int[n];
        leftToRight[0] = 0;
        rightToLeft[n-1] = 0;
        for (int i = 1; i < n; ++i) {
            leftToRight[i] = Math.max(leftToRight[i-1], A[i-1]);
            rightToLeft[n-i-1] = Math.max(rightToLeft[n-i], A[n-i]);
        }
        int total = 0;
        for (int i=1; i < n-1; i++) {
            int height = Math.min(leftToRight[i], rightToLeft[i]);
            if (height > A[i]) 
                total += height - A[i];
        }
        return total;
    }
}
