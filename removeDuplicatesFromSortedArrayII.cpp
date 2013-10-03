class Solution {
public:
    int removeDuplicates(int A[], int n) {
        // Start typing your C/C++ solution below
        // DO NOT write int main() function
        if (n == 0 || n == 1 || n == 2) {
            return n;
        }
        int B[n];
        B[0] = A[0];
        B[1] = A[1];
        int j = 1;
        for (int i=2; i < n; i++) {
            if (!(A[i] == A[i-1] && A[i] == A[i-2])) {
                B[++j] = A[i];
            }
        }
        for (int i=0; i <= j; i++) {
            A[i] = B[i];
        }
        return j+1;
    }
};
