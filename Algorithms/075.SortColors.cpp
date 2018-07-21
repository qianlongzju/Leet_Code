class Solution {
public:
    void sortColors(int A[], int n) {
        int i=0, j=n-1;
        while (i < n && A[i] == 0) {
            i++;
        }
        while (j >= 0 && A[j] == 2) {
            j--;
        }
        for (int k = i; k <= j; ++k)
        {
            if (A[k] == 0) {
                int temp = A[i];
                A[i] = A[k];
                A[k] = temp;
                while (A[i] == 0) {
                    i++;
                }
                if (A[k] == 2) {
                    int temp = A[j];
                    A[j] = A[k];
                    A[k] = temp;
                    while (A[j] == 2) {
                        j--;
                    }
                }
            }
            if (A[k] == 2) {
                int temp = A[j];
                A[j] = A[k];
                A[k] = temp;
                while (A[j] == 2) {
                    j--;
                }
                if (A[k] == 0) {
                    int temp = A[i];
                    A[i] = A[k];
                    A[k] = temp;
                    while (A[i] == 0) {
                        i++;
                    }
                }
            }
            if (k < i) {
                k = i;
            }
        }
    }
};
