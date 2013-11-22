import java.util.*;
public class Solution {
    public double findMedianSortedArrays(int A[], int B[]) {
        int total = A.length + B.length;
        if (total % 2 == 1)
            return find_kth(A, B, total / 2 + 1);
        else
            return (find_kth(A, B, total / 2)
                    + find_kth(A, B, total / 2 + 1)) / 2;
    }
    private double find_kth(int A[], int B[], int k) {
        //always assume that m is equal or smaller than n
        int m = A.length;
        int n = B.length;
        if (m > n) return find_kth(B, A, k);
        if (m == 0) return B[k - 1];
        if (k == 1) {
            if (A[0] < B[0])
                return A[0];
            else 
                return B[0];
        }
        //divide k into two parts
        int pa = 0;
        if (k / 2 > m)
            pa = m;
        else 
            pa = k / 2;
        int pb = k - pa;
        if (A[pa - 1] < B[pb - 1])
            return find_kth(Arrays.copyOfRange(A, pa, A.length), B, k - pa);
        else if (A[pa - 1] > B[pb - 1])
            return find_kth(A, Arrays.copyOfRange(B, pb, B.length), k - pb);
        else
            return A[pa - 1];
    }
}
