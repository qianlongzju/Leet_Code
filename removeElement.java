public class Solution {
    public int removeElement(int[] A, int elem) {
        // Start typing your Java solution below
        // DO NOT write main() function
        int n = A.length;
        for (int i=0; i < n; i++) {
            while (A[i] == elem) {
                n --;
                if (i >= n)
                    return n;
                A[i] = A[n];
            }
        }
        return n;
    }
}
