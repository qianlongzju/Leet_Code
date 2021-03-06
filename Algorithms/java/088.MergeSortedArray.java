public class Solution {
    public void merge(int A[], int m, int B[], int n) {
        int[] C = new int[m+n];
        int i = 0;
        int j = 0;
        int k = 0;
        while (i < m && j < n) {
            if (A[i] < B[j]) {
                C[k++] = A[i++];
            }
            else {
                C[k++] = B[j++];
            }
        }
        while (i < m) {
            C[k++] = A[i++];
        }
        while (j < n) {
            C[k++] = B[j++];
        }
        k = 0;
        while (k < (m+n)) {
            A[k] = C[k];
            k++;
        }
    }
}
