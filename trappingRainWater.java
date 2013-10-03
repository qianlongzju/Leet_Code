import java.util.*;
public class Solution {
    public int trap(int[] A) {
        // Start typing your Java solution below
        // DO NOT write main() function
        int total = 0;
        int n = A.length;
        int[] leftToRight = new int[n];
        int highest = 0;
        for (int i = 0; i < n; ++i) {
            leftToRight[i] = highest;
            if (A[i] > highest) {
                highest = A[i];
            }
        }
        highest = 0;
        for (int i = n-1; i >= 0; i --) {
            if (A[i] > highest) {
                highest = A[i];
            } else if (A[i] < leftToRight[i]) {
                total += highest > leftToRight[i] ? leftToRight[i]: highest;
                total -= A[i];
            }
        }
        return total;
    }
}
