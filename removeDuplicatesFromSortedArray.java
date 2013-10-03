public class Solution {
    public int removeDuplicates(int[] A) {
        // Start typing your Java solution below
        // DO NOT write main() function
        int n = A.length;
        if (n == 0 || n == 1) {
            return n;
        }
        int j = 0;
        for (int i=1; i < n; i++) {
            if (A[i] != A[i-1]) {
                A[++j] = A[i];
            }
        }
        return j+1;
        
    }
}
