public class Solution {
    public int maxProduct(int[] A) {
        int n = A.length;
        int max = A[0], min = A[0], result = A[0];
        for (int i = 1; i < n; i++) {
            int mx = max, mn = min;
            max = Math.max(Math.max(A[i], mx * A[i]), mn * A[i]);
            min = Math.min(Math.min(A[i], mx * A[i]), mn * A[i]);
            result = Math.max(result, max);
        }
        return result;
    }
}
