class Solution {
public:
    int singleNumber(int A[], int n) {
        int result = 0;
        for (int j=0; j < 32; ++j) {
            int tmp = 0;
            int bitOps = 1 << j;
            for (int i=0; i < n; ++i) {
                if (A[i] & bitOps) {
                    tmp ++;
                }
            }
            result += (tmp%3) << j;
        }
        return result;
    }
};
