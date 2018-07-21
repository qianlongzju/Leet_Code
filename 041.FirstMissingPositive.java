public class Solution {
    public int firstMissingPositive(int[] A) {
        int n = A.length;
        for (int i=0; i < n; i++) {
            while (A[i] <= n  && A[i] > 0 && A[i] != i+1) {
                int temp = A[A[i]-1];
                if (temp == A[i]) {
                    break;
                }
                A[A[i]-1] = A[i];
                A[i] = temp;
            }
        }        
        for (int i=0; i < n; i++) {
            if (A[i] != i+1) {
                return i+1;
            }
        }
        return n+1;
    }
}
