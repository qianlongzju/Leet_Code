class Solution {
public:
    int maxProduct(int A[], int n) {
        int max_product = A[0], min_product = A[0], result = A[0];
        for (int i = 0; i < n; i++) {
            int mx = max_product, mn = min_product;
            max_product = max(max(A[i], mx * A[i]), mn * A[i]);
            min_product = min(min(A[i], mx * A[i]), mn * A[i]);
            result = max(result, max_product);
        }
        return result;
    }
};
